# -*- coding: utf-8 -*- 
import urllib, unicodedata, string
from HTMLParser import HTMLParser

PROXY = "http://jacoelt:8*ziydwys@crlwsgateway_cluster.salmat.com.au:8080"
HOME_URL = "http://www.pokepedia.fr"
BASE_URL = "http://www.pokepedia.fr/index.php/Liste_des_Pok%C3%A9mon_par_statistiques_de_base"

def main():
    
    buildList()
    
def buildList():
    resp = urllib.urlopen(BASE_URL, proxies={"http":PROXY})
    p = MainPageParser()
    p.feed(resp.read().decode("utf-8"))
    
    print p.data

def getAttr(attrs, attr):
    for e in attrs:
        if e[0] == attr:
            return e[1]
    return ""

class MainPageParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        
        self.inTable = False
        self.inTr = False
        self.inTd = False
        
        self.data = []
    
    def handle_starttag(self, tag, attrs):
        if tag == "table" and getAttr(attrs, "class") == "tableaustandard sortable":
            self.inTable = True
        
        if self.inTable and tag == "tr":
            self.inTr = True
            self.cell = 0
        
        if self.inTr and tag == "td":
            self.inTd = True
            self.cell += 1
            
        if self.inTr and self.cell == 3 and tag == "a":
            resp = urllib.urlopen(HOME_URL + getAttr(attrs, "href"), proxies={"http":PROXY})
            p = PokemonParser()
            p.feed(resp.read().decode("utf-8"))
            print p.getData()
            self.data.append(p.getData())
        
    def handle_endtag(self, tag):
        if self.inTd and tag == "td":
            self.inTd = False
            
        if self.inTr and tag == "tr":
            self.inTr = False
        
        if tag == "table":
            self.inTable = False
    
    
class PokemonParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        
        self.nameP = NameParser()
        self.evolutionP = EvolutionsParser()
        self.sizeP = SizeParser()
        
    
    def getData(self):
        return {self.nameP.data: {
            "evolutions": self.evolutionP.data,
            "size": self.sizeP.data,
        }}

    def handle_starttag(self, tag, attrs):
        self.nameP.handle_starttag(tag, attrs)
        self.evolutionP.handle_starttag(tag, attrs)
        self.sizeP.handle_starttag(tag, attrs)
        
    def handle_endtag(self, tag):
        self.nameP.handle_endtag(tag)
        self.evolutionP.handle_endtag(tag)
        self.sizeP.handle_endtag(tag)
    
    def handle_data(self, data):
        self.nameP.handle_data(data)
        self.evolutionP.handle_data(data)
        self.sizeP.handle_data(data)

class EvolutionsParser():
    def __init__(self):
        self.data = []
        self.inH3 = False
        self.getTable = False
        self.inTable = False
        self.inTd = False
        self.inSmall = False
        self.getContent = False
        self.getContentIfEquals = ""
        self.smallContent = ""
    
    def handle_starttag(self, tag, attrs):
        if tag == "h3":
            self.inH3 = True
            
            if self.getTable:
                self.getTable = False
        
        if self.inH3 and tag == "span" and getAttr(attrs, "id") == ".C3.89volution":
            self.getTable = True
        
        if self.getTable and tag == "table":
            self.inTable = True
        
        if self.inTable and tag == "td":
            self.inTd = True
        
        if self.inTd and tag == "small":
            self.getContent = True
            self.inSmall = True
        
        if self.inTd and tag == "strong":
            self.getContent = True
        
        if self.inTd and not self.inSmall and tag == "a":
            self.getContentIfEquals = getAttr(attrs, "title")
            
    
    def handle_data(self, data):
        if self.getContent:
            if self.inSmall:
                self.smallContent += " " + normalize(data)
            else:
                self.data.append(normalize(data))
        
        if self.getContentIfEquals and data == self.getContentIfEquals:
            self.data.append(normalize(data))
    
    def handle_endtag(self, tag):
        if tag == "a":
            self.getContentIfEquals = ""
        
        if tag == "strong":
            self.getContent = False
        
        if tag == "small":
            self.getContent = False
            self.inSmall = False
            if (self.smallContent.strip()):
                self.data.append(self.smallContent.strip())
                self.smallContent = ""
        
        if tag == "td":
            self.inTd = False
        
        if tag == "table":
            self.getTable = False
            self.inTable = False
        
        if tag == "h3":
            self.inH3 = False


class NameParser():
    def __init__(self):
        self.data = ""
        
        self.inTable = False
        self.getContent = False
        
    def handle_starttag(self, tag, attrs):
        if tag == "table" and getAttr(attrs, "class").find("ficheinfo") > -1:
            self.inTable = True
        
        if self.inTable and tag == "th" and getAttr(attrs, "class") == u"ent\xeatesection" and getAttr(attrs, "colspan") == "4":
            self.getContent = True
        
    def handle_data(self, data):
        if self.getContent:
            self.data = normalize(data)
            self.getContent = False
        
    def handle_endtag(self, tag):
        if self.inTable and tag == "table":
            self.inTable = False


class SizeParser():
    def __init__(self):
        self.data = ""
        
        self.inTable = False
        self.checkContent = False
        self.getNextTd = False
        self.getContent = False
        
    def handle_starttag(self, tag, attrs):
        if tag == "table" and getAttr(attrs, "class").find("ficheinfo") > -1:
            self.inTable = True
        
        if self.inTable and tag == "th":
            self.checkContent = True
        
        if self.getNextTd and tag == "td":
            self.getContent = True
        
    def handle_data(self, data):
        if self.checkContent and data == "Taille":
            self.getNextTd = True
            
        if self.getContent:
            self.data = normalize(data.splice(0, data.find(", soit")))
        
    def handle_endtag(self, tag):
        if self.getNextTd and tag == "td":
            self.getContent = False
            self.getNextTd = False
        
        if self.checkContent and tag == "th":
            self.checkContent = False
        
        if self.inTable and tag == "table":
            self.inTable = False


def normalize(text):
    return text.strip().replace(u"\xe9", "e").replace(u"\xe8", "e").replace(u"\xc9", "E")

main()

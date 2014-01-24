import urllib
from HTMLParser import HTMLParser

HOME_URL = "http://www.pokepedia.fr"
BASE_URL = "http://www.pokepedia.fr/index.php/Liste_des_Pok%C3%A9mon_par_statistiques_de_base"

def main():
    resp = urllib.urlopen(BASE_URL)
    p = MainPageParser()
    p.feed(resp.read().decode("utf-8"))
    
    print p.data

def getAttr(attrs, attr):
    for e in attrs:
        if e[0] == attr:
            return e[1]
    return None

class MainPageParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        
        self.inTable = False
        self.inTr = False
        self.inTd = False
        self.inImg = False
        self.inLink = False
        
        self.data = []
        self.currentObj = {}
    
    def handle_starttag(self, tag, attrs):
        if tag == "table" and getAttr(attrs, "class") == "tableaustandard sortable":
            self.inTable = True
        
        if self.inTable and tag == "tr":
            self.inTr = True
            self.cell = 0
        
        if self.inTr and tag == "td":
            self.inTd = True
            self.cell += 1
            
        if self.inTr and self.cell == 2 and tag == "img":
            self.currentObj["miniat"] = getAttr(attrs, "src")
            
        if self.inTr and self.cell == 3 and tag == "a":
            self.inLink = True
            
            resp = urllib.urlopen(HOME_URL + getAttr(attrs, "href"))
            p = PokemonParser()
            p.feed(resp.read().decode("utf-8"))
            self.currentObj["image"] = p.data
        
    def handle_endtag(self, tag):
        if self.inLink and tag == "a":
            self.inLink = False
        
        if self.inTd and tag == "td":
            self.inTd = False
            
        if self.inTr and tag == "tr":
            self.inTr = False
            self.data.append(self.currentObj)
            print self.currentObj
            self.currentObj = {}
        
        if tag == "table":
            self.inTable = False
        
    def handle_data(self, data):
        if self.inTr:
            if self.cell == 1 and self.inTd:
                self.currentObj["number"] = data.strip()
            if self.cell == 3 and self.inTd and self.inLink:
                self.currentObj["name"] = data.strip()
    
    
class PokemonParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.inTd = False
    
    def handle_starttag(self, tag, attrs):
        if tag == "td" and getAttr(attrs, "class") == "illustration":
            self.inTd = True
            
        if self.inTd and tag == "img":
            self.data = getAttr(attrs, "src")
        
    def handle_endtag(self, tag):
        if self.inTd and tag == "td":
            self.inTd = False

main()

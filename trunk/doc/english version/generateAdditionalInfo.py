# -*- coding: utf-8 -*- 
import urllib, unicodedata, string
from HTMLParser import HTMLParser

PROXY = "http://jacoelt:8*ziydwys@crlwsgateway_cluster.salmat.com.au:8080"
HOME_URL = "http://bulbapedia.bulbagarden.net"
BASE_URL = "http://bulbapedia.bulbagarden.net/wiki/LPBBS"

def main(list):
    
    buildList()
    return
    
    text = ""
    spacing = "        "
    for name, info in list.items():
    
    # name = "Kirlia"
    # info = list[name]
        
        tree = generate_evolution_tree(info["evolutions"], list)
        
        text += spacing + "p = perName.get(\"{name}\");\n".format(name=name)
        text += spacing + "p.evolutions = " + get_text_from_evolution_tree(tree) + ";\n"
        
        text += spacing + "p.catchRate = \"{}\";\n".format(info["catch"])
        text += spacing + "p.weight = \"{}\";\n".format(info["weight"])
        text += spacing + "p.hatch = \"{}\";\n".format(info["hatch"])
        text += spacing + "p.gender = \"{}\";\n".format(info["gender"])
        text += spacing + "p.ev = \"{}\";\n".format(info["ev"])
        text += spacing + "p.eggGroup = \"{}\";\n".format(info["egg"])
        text += spacing + "p.size = \"{}\";\n\n".format(info["size"])

    print text

def get_text_from_evolution_tree(evolution_tree):
    if not evolution_tree:
        return "null"
        
    if not evolution_tree.nodes:
        return "new EvolutionNode(perName.get(\"{name}\"), null)".format(name=evolution_tree.name)
    
    text = "new EvolutionNode(perName.get(\"{name}\"), new HashMap<String, EvolutionNode>(){{{{".format(name=evolution_tree.name)
    
    for path, evolutions in evolution_tree.nodes.items():
        text += "this.put(\"{path}\", ".format(path=path) + get_text_from_evolution_tree(evolutions) + ");"
    
    return text + "}})"
    

def generate_evolution_tree(evolution_chain, list):
    # Special cases:
    if "Ralts" in evolution_chain:
        return EvolutionNode(evolution_chain[0], {
            evolution_chain[1]: EvolutionNode(evolution_chain[2], {
                evolution_chain[3]: EvolutionNode(evolution_chain[5], {
                    evolution_chain[7]: EvolutionNode(evolution_chain[8], {})
                }),
                evolution_chain[4]: EvolutionNode(evolution_chain[6], {})
            })
        })
        
    
    if len(evolution_chain) < 1:
        return None
    
    name = evolution_chain[0]
    
    if not evolution_chain[1:]:
        return EvolutionNode(name, {})
    
    # Considering that an evolution that has multiple children is always a leaf
    # 2nd element is always a path, if 3rd element is also a path, all remaining paths can be matched against corresponding child
    if list.has_key(evolution_chain[2]):
        # 3rd element is a name
        return EvolutionNode(name, {evolution_chain[1]: generate_evolution_tree(evolution_chain[2:], list)})
    else:
        # 3rd element is a path
        evolution_paths = filter(lambda x: not list.has_key(x), evolution_chain[1:])
        evolutions = map(lambda x: EvolutionNode(x, {}), filter(lambda x: list.has_key(x), evolution_chain[1:]))
        
        return EvolutionNode(name, {k:v for k,v in zip(evolution_paths, evolutions)})

    
class EvolutionNode():
    def __init__(self, name, nodes):
        self.name = name
        self.nodes = nodes
    
    def __repr__(self):
        return self.name + "->" + str(self.nodes)




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
        
        self.currentData = None
        self.name = ""
        self.data = {}
    
    def handle_starttag(self, tag, attrs):
        if tag == "table" and getAttr(attrs, "class") == "tableaustandard sortable":
            self.inTable = True
        
        if self.inTable and tag == "tr":
            self.inTr = True
            self.cell = 0
        
        if self.inTr and tag == "td":
            self.inTd = True
            self.cell += 1
            
        if self.inTd and self.cell == 3 and tag == "a":
            resp = urllib.urlopen(HOME_URL + getAttr(attrs, "href"), proxies={"http":PROXY})
            p = PokemonParser()
            p.feed(resp.read().decode("utf-8"))
            self.currentData = p.getData()
        
    def handle_data(self, data):
        if self.inTd and self.cell == 3:
            self.name += normalize(data)
        
    def handle_endtag(self, tag):
        if self.inTd and tag == "td":
            self.inTd = False
            if self.name and self.currentData:
                print {self.name: self.currentData}
                self.data.update({self.name: self.currentData})
                self.name = ""
            
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
        self.weightP = WeightParser()
        self.hatchP = HatchParser()
        self.evP = EVParser()
        self.genderP = GenderParser()
        self.catchP = CatchParser()
        self.eggP = EggParser()
        
    
    def getData(self):
        # return {self.nameP.data: {
            # "evolutions": self.evolutionP.data,
            # "size": self.sizeP.data,
            # "weight": self.weightP.data,
            # "hatch": self.hatchP.data,
            # "ev": self.evP.data,
            # "gender": self.genderP.data,
            # "catch": self.catchP.data,
            # "egg": self.eggP.data,
        # }}
        return {
            "evolutions": self.evolutionP.data,
            "size": self.sizeP.data,
            "weight": self.weightP.data,
            "hatch": self.hatchP.data,
            "ev": self.evP.data,
            "gender": self.genderP.data,
            "catch": self.catchP.data,
            "egg": self.eggP.data,
        }

    def handle_starttag(self, tag, attrs):
        # self.nameP.handle_starttag(tag, attrs)
        self.evolutionP.handle_starttag(tag, attrs)
        self.sizeP.handle_starttag(tag, attrs)
        self.weightP.handle_starttag(tag, attrs)
        self.hatchP.handle_starttag(tag, attrs)
        self.evP.handle_starttag(tag, attrs)
        self.genderP.handle_starttag(tag, attrs)
        self.catchP.handle_starttag(tag, attrs)
        self.eggP.handle_starttag(tag, attrs)
        
    def handle_endtag(self, tag):
        # self.nameP.handle_endtag(tag)
        self.evolutionP.handle_endtag(tag)
        self.sizeP.handle_endtag(tag)
        self.weightP.handle_endtag(tag)
        self.hatchP.handle_endtag(tag)
        self.evP.handle_endtag(tag)
        self.genderP.handle_endtag(tag)
        self.catchP.handle_endtag(tag)
        self.eggP.handle_endtag(tag)
    
    def handle_data(self, data):
        # self.nameP.handle_data(data)
        self.evolutionP.handle_data(data)
        self.sizeP.handle_data(data)
        self.weightP.handle_data(data)
        self.hatchP.handle_data(data)
        self.evP.handle_data(data)
        self.genderP.handle_data(data)
        self.catchP.handle_data(data)
        self.eggP.handle_data(data)

class EvolutionsParser():
    def __init__(self):
        self.data = []
        self.inH3 = False
        self.getTable = False
        self.inTable = False
        self.inTr = False
        self.colNum = 0
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
        
        if self.inTable and tag == "tr":
            self.inTr = True
            
        if self.inTr and tag == "td":
            self.inTd = True
            self.colNum += 1
        
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
            
        if tag == "tr":
            self.inTr = False
            self.colNum = 0
        
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

class StandardInfoParser():
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
        if self.checkContent and self.check_data(data):
            self.getNextTd = True
            
        if self.getContent:
            self.extract_content(data)
        
    def handle_endtag(self, tag):
        if self.getNextTd and tag == "td":
            self.getContent = False
            self.getNextTd = False
        
        if self.checkContent and tag == "th":
            self.checkContent = False
        
        if self.inTable and tag == "table":
            self.inTable = False
    
    def check_data(self, data):
        return True
    
    def extract_content(self, data):
        self.data = data


class SizeParser(StandardInfoParser):
    def __init__(self):
        StandardInfoParser.__init__(self)
    
    def check_data(self, data):
        return data == "Taille"
    
    def extract_content(self, data):
        try:
            i = data.index(", soit")
            self.data = normalize(data[0:i])
        except ValueError:
            self.data = normalize(data)

class WeightParser(StandardInfoParser):
    def __init__(self):
        StandardInfoParser.__init__(self)
    
    def check_data(self, data):
        return data == "Poids"
    
    def extract_content(self, data):
        try:
            i = data.index(", soit")
            self.data = normalize(data[0:i])
        except ValueError:
            self.data = normalize(data)

class HatchParser(StandardInfoParser):
    def __init__(self):
        StandardInfoParser.__init__(self)
    
    def check_data(self, data):
        return normalize(data).endswith("closion")
    
    def extract_content(self, data):
        self.data = normalize(data)

class EVParser(StandardInfoParser):
    def __init__(self):
        StandardInfoParser.__init__(self)
    
    def check_data(self, data):
        return data == "Points effort"
    
    def extract_content(self, data):
        self.data += normalize(data)

class GenderParser(StandardInfoParser):
    def __init__(self):
        StandardInfoParser.__init__(self)
    
    def check_data(self, data):
        return data == "Sexe"
    
    def extract_content(self, data):
        self.data += normalize(data)

class CatchParser(StandardInfoParser):
    def __init__(self):
        StandardInfoParser.__init__(self)
    
    def check_data(self, data):
        return data == "Taux de capture"
    
    def extract_content(self, data):
        self.data = normalize(data)

class EggParser(StandardInfoParser):
    def __init__(self):
        StandardInfoParser.__init__(self)
    
    def check_data(self, data):
        return data == "Groupe"
    
    def extract_content(self, data):
        self.data += normalize(data)


def normalize(text):
    return text.strip()\
        .replace(u"\xe9", "e")\
        .replace(u"\xe8", "e")\
        .replace(u"\xea", "e")\
        .replace(u"\xe0", "a")\
        .replace(u"\xe2", "a")\
        .replace(u"\xef", "i")\
        .replace(u"\xf4", "o")\
        .replace(u"\xe7", "c")\
        .replace(u"\u0153", "oe")\
        .replace(u"\xc9", "E")\
        .replace(u"\u2640", " F")\
        .replace(u"\u2642", " M")\
        .replace(u"\u2014", "")

list = {}

main(list)

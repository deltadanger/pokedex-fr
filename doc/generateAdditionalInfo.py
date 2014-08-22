# -*- coding: utf-8 -*- 
import urllib, unicodedata, string, re
from HTMLParser import HTMLParser

PROXY = "http://jacoelt:8*ziydwys@crlwsgateway_cluster.salmat.com.au:8080"
HOME_URL = "http://www.pokepedia.fr"
BASE_URL = "http://www.pokepedia.fr/index.php/Liste_des_Pok%C3%A9mon_par_statistiques_de_base"


egg_group_matching = {
    "Vol": "FLYING",
    "Amorphe": "AMORPHOUS",
    "Eau 1": "WATER1",
    "Eau 2": "WATER2",
    "Eau 3": "WATER3",
    "Dragon": "DRAGON",
    "Fee": "FAIRY",
    "Humanoide": "HUMANLIKE",
    "Indetermine": "UNKNOWN",
    "Insecte": "BUG",
    "Metamorph": "DITTO",
    "Mineral": "MINERAL",
    "Monstre": "MONSTER",
    "Sol": "FIELD",
    "Plante": "GRASS",
    "Sans Oeuf": "NO_EGG",
    "Sans oeuf": "NO_EGG",
    "": "NO_EGG",
}

ev_name_matching = {
    "PV": "life_short",
    "PV.": "life_short",
    "Att.": "att_short",
    "Att": "att_short",
    "Def.": "def_short",
    "Def": "def_short",
    "Def0": "def_short",
    "Att. Spe": "spatt_short",
    "Att Spe.": "spatt_short",
    "Att. Spe.": "spatt_short",
    "Def. Spe": "spdef_short",
    "Def. Spe.": "spdef_short",
    "Vit.": "speed_short",
}

def main(list, name_match):


    text = ""
    spacing = "        "
    for name, info in list.items():
    
    # name = "Kirlia"
    # info = list[name]
        
        # weight = info["weight"].replace("kg", "").replace(",", ".")
        
        # hatch = -1
        # match = re.match("\d+ cycles - (\d+) pas", info["hatch"])
        # if match:
            # hatch = match.group(1)
        
        # gender = -1
        # match = re.match("([\d\.]+)% femelle; [\d\.]+% male", info["gender"])
        # if match:
            # gender = match.group(1)
        
        # evs = ""
        # for ev in re.split("[;,]", info["ev"]):
            # ev_match = re.match("\+(\d) (.*)", ev)
            # if ev_match:
                # evs += "this.append({}, R.string.{});".format(ev_match.group(1), ev_name_matching[ev_match.group(2)])
        
        # egg_groups = []
        # for egg_group in info["egg"].split("/"):
            # egg_groups.append("EggGroup." + egg_group_matching[egg_group])
        
        # size = info["size"].replace("m", "").replace(",", ".")
        
        
        tree = generate_evolution_tree(info["evolutions"], list)
        text += str(tree)
        
        # text += spacing + "p = perName.get(ctx.getString(R.string.name_{name}));\n".format(name=toId(name))
        # text += spacing + "p.evolutions = " + get_text_from_evolution_tree(tree) + ";\n"
        
        # text += spacing + "p.catchRate = {};\n".format(info["catch"] if info["catch"] else "-1")
        # text += spacing + "p.weight = {}f;\n".format(weight)
        # text += spacing + "p.hatch = {};\n".format(hatch)
        # text += spacing + "p.gender = {}f;\n".format(gender)
        # text += spacing + "p.ev = new SparseIntArray(){{{{{}}}}};\n".format(evs)
        # text += spacing + "p.eggGroup = new EggGroup[]{{{}}};\n".format(",".join(egg_groups))
        # text += spacing + "p.size = {}f;\n\n".format(size)

    print tree

def get_text_from_evolution_tree(evolution_tree):
    if not evolution_tree:
        return "null"
        
    if not evolution_tree.nodes:
        return "new EvolutionNode(perName.get(ctx.getString(R.string.name_{name})), null)".format(name=toId(evolution_tree.name))
    
    text = "new EvolutionNode(perName.get(ctx.getString(R.string.name_{name})), new HashMap<String, EvolutionNode>(){{{{".format(name=toId(evolution_tree.name))
    
    for path, evolutions in evolution_tree.nodes.items():
        if path.startswith("Niveau "):
            path = "ctx.getString(R.string.level) + \"" + path[7:] + '"'
        else:
            path = '"' + path + '"'
        text += "this.put({path}, ".format(path=path) + get_text_from_evolution_tree(evolutions) + ");"
    
    return text + "}})"
    

def generate_evolution_tree(evolution_chain, list):
    # Special cases:
    if "Tarsal" in evolution_chain:
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
        .replace("é", "e")\
        .replace("è", "e")\
        .replace("ê", "e")\
        .replace("à", "a")\
        .replace("â", "a")\
        .replace("ï", "i")\
        .replace("ô", "o")\
        .replace("ç", "c")\
        .replace("ç", "c")\
        .replace("œ", "oe")\
        .replace("É", "e")
        # .replace(u"\xe9", "e")\
        # .replace(u"\xe8", "e")\
        # .replace(u"\xea", "e")\
        # .replace(u"\xe0", "a")\
        # .replace(u"\xe2", "a")\
        # .replace(u"\xef", "i")\
        # .replace(u"\xf4", "o")\
        # .replace(u"\xe7", "c")\
        # .replace(u"\u0153", "oe")\
        # .replace(u"\xc9", "E")\
        # .replace(u"\u2640", " F")\
        # .replace(u"\u2642", " M")\
        # .replace(u"\u2014", "")

def toId(text):
    text = text.lower()\
        .replace(" ", "_")\
        .replace("-", "_")\
        .replace(".", "")\
        .replace("'", "")\
        .replace("(", "")\
        .replace(")", "")
    
    return name_match[text]

name_match = {'scorplane': 'gligar', 'snubbull': 'snubbull', 'ratentif': 'patrat', 'hypnomade': 'hypno', 'mammochon': 'mamoswine', 'phyllali': 'leafeon', 'celebi': 'celebi', 'togetic': 'togetic', 'carabing': 'karrablast', 'metamorph': 'ditto', 'mega_ectoplasma': 'mega_gengar', 'ossatueur': 'marowak', 'monaflemit': 'slaking', 'palkia': 'palkia', 'nymphali': 'sylveon', 'loupio': 'chinchou', 'mega_absol': 'mega_absol', 'noctali': 'umbreon', 'baggaid': 'scrafty', 'abra': 'abra', 'debugant': 'tyrogue', 'pifeuil': 'nuzleaf', 'tarpaud': 'politoed', 'demolosse': 'houndoom', 'miradar': 'watchog', 'kaimorse': 'walrein', 'stalgamin': 'snorunt', 'teddiursa': 'teddiursa', 'azurill': 'azurill', 'registeel': 'registeel', 'amonita': 'omanyte', 'lamperoie': 'eelektrik', 'mesmerella': 'gothorita', 'qwilfish': 'qwilfish', 'pharamp': 'ampharos', 'galopa': 'rapidash', 'roitiflam': 'emboar', 'marisson': 'chespin', 'furaiglon': 'rufflet', 'electhor': 'zapdos', 'lewsor': 'elgyem', 'hippopotas': 'hippopotas', 'mega_mewtwo_x': 'mega_mewtwo_x', 'mega_mewtwo_y': 'mega_mewtwo_y', 'armulys': 'silcoon', 'florges': 'florges', 'fouinette': 'sentret', 'heliatronc': 'sunflora', 'pitrouille_taille_ultra': 'pumpkaboo_super_size', 'moufouette': 'stunky', 'zeblitz': 'zebstrika', 'torterra': 'torterra', 'simularbre': 'sudowoodo', 'insolourdo': 'dunsparce', 'zorua': 'zorua', 'meganium': 'meganium', 'ymphect': 'pupitar', 'vigoroth': 'vigoroth', 'roselia': 'roselia', 'givrali': 'glaceon', 'poussifeu': 'torchic', 'baggiguane': 'scraggy', 'lombre': 'lombre', 'tartard': 'poliwrath', 'delcatty': 'delcatty', 'abo': 'ekans', 'mysdibule': 'mawile', 'melo': 'cleffa', 'arkeapti': 'archen', 'ningale': 'nincada', 'kecleon': 'kecleon', 'vaututrice': 'mandibuzz', 'minidraco': 'dratini', 'goelise': 'wingull', 'floette': 'floette', 'ouvrifier': 'gurdurr', 'tropius': 'tropius', 'mew': 'mew', 'banshitrouye_taille_ultra': 'gourgeist_super_size', 'tenefix': 'sableye', 'ptera': 'aerodactyl', 'tylton': 'swablu', 'dracolosse': 'dragonite', 'negapi': 'minun', 'rhinoferos': 'rhydon', 'eoko': 'chimecho', 'passerouge': 'fletchling', 'tentacruel': 'tentacruel', 'armaldo': 'armaldo', 'ptiravi': 'happiny', 'sorbebe': 'vanillite', 'kyurem': 'kyurem_normal_kyurem', 'dedenne': 'dedenne', 'drascore': 'drapion', 'chaffreux': 'purugly', 'mega_scarhino': 'mega_heracross', 'banshitrouye_taille_normale': 'gourgeist_average_size', 'desseliande': 'trevenant', 'cotovol': 'jumpluff', 'pyrax': 'volcarona', 'cryptero': 'sigilyph', 'maracachi': 'maractus', 'chrysacier': 'metapod', 'okeoke': 'wynaut', 'ecrapince': 'corphish', 'munja': 'shedinja', 'symbios': 'reuniclus', 'lancargot': 'escavalier', 'poissirene': 'goldeen', 'motisma_forme_tonte': 'rotom_fan_rotom', 'spiritomb': 'spiritomb', 'meios': 'duosion', 'papilusion': 'butterfree', 'heatran': 'heatran', 'cliticlic': 'klinklang', 'xatu': 'xatu', 'gardevoir': 'gardevoir', 'jungko': 'sceptile', 'qulbutoke': 'wobbuffet', 'ramboum': 'loudred', 'charmina': 'medicham', 'floravol': 'skiploom', 'staross': 'starmie', 'tygnon': 'hitmonchan', 'absol': 'absol', 'pyronille': 'larvesta', 'escargaume': 'shelmet', 'taupiqueur': 'diglett', 'blindalys': 'cascoon', 'mustebouee': 'buizel', 'granbull': 'granbull', 'noarfang': 'noctowl', 'lainergie': 'flaaffy', 'fragilady': 'lilligant', 'lippoutou': 'jynx', 'motisma_forme_helice': 'rotom_mow_rotom', 'teraclope': 'dusclops', 'moustillon': 'oshawott', 'brocelome': 'phantump', 'cochignon': 'piloswine', 'lucario': 'lucario', 'ohmassacre': 'eelektross', 'maskadra': 'masquerain', 'onix': 'onix', 'grodrive': 'drifblim', 'seviper': 'seviper', 'nostenfer': 'crobat', 'boskara': 'grotle', 'feunard': 'ninetales', 'kranidos': 'cranidos', 'croaporal': 'frogadier', 'elecsprint': 'manectric', 'mistigrix': 'meowstic', 'makuhita': 'makuhita', 'donphan': 'donphan', 'sabelette': 'sandshrew', 'sonistrelle': 'noibat', 'artikodin': 'articuno', 'coxyclaque': 'ledian', 'gloupti': 'gulpin', 'victini': 'victini', 'miamiasme': 'trubbish', 'mega_brasegali': 'mega_blaziken', 'noadkoko': 'exeggutor', 'pachirisu': 'pachirisu', 'gueriaigle': 'braviary', 'mateloutre': 'dewott', 'motisma_forme_normale': 'rotom_normal_rotom', 'psystigri': 'espurr', 'venalgue': 'skrelp', 'pingoleon': 'empoleon', 'arbok': 'arbok', 'opermine': 'binacle', 'goupelin': 'delphox', 'octillery': 'octillery', 'crapustule': 'seismitoad', 'melofee': 'clefairy', 'lippouti': 'smoochum', 'arcanin': 'arcanine', 'grindur': 'ferroseed', 'genesect': 'genesect', 'mucuscule': 'goomy', 'deoxys_forme_de_base': 'deoxys_normal_forme', 'crikzik': 'kricketot', 'ursaring': 'ursaring', 'noeunoeuf': 'exeggcute', 'm_mime': 'mr_mime', 'sapereau': 'bunnelby', 'psykokwak': 'psyduck', 'funecire': 'litwick', 'entei': 'entei', 'lanturn': 'lanturn', 'sancoki': 'shellos', 'barpau': 'feebas', 'melancolux': 'lampent', 'lugia': 'lugia', 'boreas_forme_totemique': 'tornadus_therian_forme', 'zekrom': 'zekrom', 'scarabrute': 'pinsir', 'couaneton': 'ducklett', 'voltorbe': 'voltorb', 'magireve': 'mismagius', 'ponchiot': 'lillipup', 'marcacrin': 'swinub', 'krabby': 'krabby', 'diamat': 'zweilous', 'tritonde': 'tympole', 'bastiodon': 'bastiodon', 'amonistar': 'omastar', 'drackhaus': 'shelgon', 'blizzi': 'snover', 'sulfura': 'moltres', 'phione': 'phione', 'dynavolt': 'electrike', 'lugulabre': 'chandelure', 'etouraptor': 'staraptor', 'kabuto': 'kabuto', 'limagma': 'slugma', 'kadabra': 'kadabra', 'kaiminus': 'totodile', 'mystherbe': 'oddish', 'mega_leviator': 'mega_gyarados', 'cupcanaille': 'slurpuff', 'arcko': 'treecko', 'capidextre': 'ambipom', 'prinplouf': 'prinplup', 'zebibron': 'blitzle', 'mime_jr': 'mime_jr', 'boustiflor': 'weepinbell', 'draby': 'bagon', 'ferosinge': 'mankey', 'serpang': 'huntail', 'tarsal': 'ralts', 'luxray': 'luxray', 'lamantine': 'dewgong', 'peregrain': 'spewpa', 'bouldeneu': 'tangrowth', 'tortank': 'blastoise', 'kabutops': 'kabutops', 'demanta': 'mantine', 'sepiatop': 'inkay', 'caninos': 'growlithe', 'nanmeouie': 'audino', 'empiflor': 'victreebel', 'herbizarre': 'ivysaur', 'pyroli': 'flareon', 'tritosor': 'gastrodon', 'joliflor': 'bellossom', 'carmache': 'gabite', 'demeteros_forme_totemique': 'landorus_therian_forme', 'tengalice': 'shiftry', 'magneti': 'magnemite', 'meloetta_forme_danse': 'meloetta_pirouette_forme', 'embrylex': 'larvitar', 'persian': 'persian', 'monorpale': 'honedge', 'oniglali': 'glalie', 'pandarbare': 'pangoro', 'mega_charmina': 'mega_medicham', 'kravarech': 'dragalge', 'manternel': 'leavanny', 'helionceau': 'litleo', 'magnezone': 'magnezone', 'terrakium': 'terrakion', 'rhinolove': 'swoobat', 'colossinge': 'primeape', 'moyade': 'jellicent', 'kapoera': 'hitmontop', 'chuchmur': 'whismur', 'tutankafer': 'cofagrigus', 'archeodong': 'bronzong', 'zoroark': 'zoroark', 'mangriff': 'zangoose', 'mega_pharamp': 'mega_ampharos', 'braisillon': 'fletchinder', 'etourmi': 'starly', 'trompignon': 'foongus', 'emolga': 'emolga', 'scarhino': 'heracross', 'posipi': 'plusle', 'porygon2': 'porygon2', 'mega_tyranocif': 'mega_tyranitar', 'anchwatt': 'tynamo', 'mega_scarabrute': 'mega_pinsir', 'girafarig': 'girafarig', 'tetarte': 'poliwhirl', 'nidorino': 'nidorino', 'nidorina': 'nidorina', 'latias': 'latias', 'chlorobule': 'petilil', 'mushana': 'musharna', 'volcaropod': 'magcargo', 'terhal': 'beldum', 'mega_blizzaroi': 'mega_abomasnow', 'sucroquin': 'swirlix', 'lakmecygne': 'swanna', 'lixy': 'shinx', 'shaofouine': 'mienshao', 'mamanbo': 'alomomola', 'bargantua': 'basculin', 'altaria': 'altaria', 'kokiyas': 'shellder', 'darumarond': 'darumaka', 'colhomard': 'crawdaunt', 'fouinar': 'furret', 'papinox': 'dustox', 'manaphy': 'manaphy', 'cocotine': 'aromatisse', 'brouhabam': 'exploud', 'sepiatroce': 'malamar', 'kyurem_blanc': 'kyurem_white_kyurem', 'seracrawl': 'avalugg', 'strassie': 'carbink', 'maganon': 'magmortar', 'kungfouine': 'mienfoo', 'meditikka': 'meditite', 'manzai': 'bonsly', 'feunnec': 'fennekin', 'mega_alakazam': 'mega_alakazam', 'maraiste': 'quagsire', 'couverdure': 'swadloon', 'mygavolt': 'galvantula', 'galvaran': 'helioptile', 'triopikeur': 'dugtrio', 'kicklee': 'hitmonlee', 'golgopathe': 'barbaracle', 'motisma_forme_chaleur': 'rotom_heat_rotom', 'cacnea': 'cacnea', 'coquiperl': 'clamperl', 'ptyranidur': 'tyrunt', 'mega_elecsprint': 'mega_manectric', 'mega_carchacrok': 'mega_garchomp', 'morpheo': 'castform', 'tyranocif': 'tyranitar', 'judokrak': 'throh', 'bulbizarre': 'bulbasaur', 'crabicoque': 'dwebble', 'gobou': 'mudkip', 'excavarenne': 'diggersby', 'seleroc': 'lunatone', 'remoraid': 'remoraid', 'chacripan': 'purrloin', 'flamoutan': 'simisear', 'shaymin_forme_terrestre': 'shaymin_land_forme', 'chartor': 'torkoal', 'dimocles': 'doublade', 'roucarnage': 'pidgeot', 'leuphorie': 'blissey', 'banshitrouye_taille_mini': 'gourgeist_small_size', 'charkos': 'rampardos', 'mega_mysdibule': 'mega_mawile', 'flingouste': 'clauncher', 'suicune': 'suicune', 'clic': 'klang', 'ectoplasma': 'gengar', 'miaouss': 'meowth', 'tortipouss': 'turtwig', 'nirondelle': 'taillow', 'lilia': 'lileep', 'mega_cizayox': 'mega_scizor', 'migalos': 'ariados', 'lokhlass': 'lapras', 'poissoroy': 'seaking', 'gaulet': 'amoonguss', 'kaorine': 'claydol', 'parecool': 'slakoth', 'regirock': 'regirock', 'ponchien': 'herdier', 'wattouat': 'mareep', 'grolem': 'golem', 'granivol': 'hoppip', 'mewtwo': 'mewtwo', 'smogo': 'koffing', 'tranchodon': 'haxorus', 'muplodocus': 'goodra', 'rhinastoc': 'rhyperior', 'carvanha': 'carvanha', 'cadoizo': 'delibird', 'ceribou': 'cherubi', 'pitrouille_taille_normale': 'pumpkaboo_average_size', 'limonde': 'stunfisk', 'libegon': 'flygon', 'mega_florizarre': 'mega_venusaur', 'hippodocus': 'hippowdon', 'crefollet': 'mesprit', 'flobio': 'marshtomp', 'canarticho': 'farfetchd', 'metalosse': 'metagross', 'siderella': 'gothitelle', 'azumarill': 'azumarill', 'pitrouille_taille_maxi': 'pumpkaboo_large_size', 'fantominus': 'gastly', 'pitrouille_taille_mini': 'pumpkaboo_small_size', 'jirachi': 'jirachi', 'arceus': 'arceus', 'elektek': 'electabuzz', 'racaillou': 'geodude', 'togekiss': 'togekiss', 'ecayon': 'finneon', 'leviator': 'gyarados', 'lumivole': 'illumise', 'crocrodil': 'croconaw', 'grelacon': 'bergmite', 'dialga': 'dialga', 'momartik': 'froslass', 'vostourno': 'vullaby', 'coudlangue': 'lickilicky', 'yveltal': 'yveltal', 'polichombr': 'shuppet', 'dimoret': 'weavile', 'roucoups': 'pidgeotto', 'farfaduvet': 'whimsicott', 'flamajou': 'pansear', 'rototaupe': 'drilbur', 'deoxys_forme_vitesse': 'deoxys_speed_forme', 'hericendre': 'cyndaquil', 'pashmilla': 'cinccino', 'coupenotte': 'axew', 'lumineon': 'lumineon', 'camerupt': 'camerupt', 'coatox': 'toxicroak', 'venipatte': 'venipede', 'dragmara': 'aurorus', 'vivaldaim': 'deerling', 'minotaupe': 'excadrill', 'zarbi': 'unown', 'galifeu': 'combusken', 'milobellus': 'milotic', 'feurisson': 'quilava', 'zigzaton': 'zigzagoon', 'machoc': 'machop', 'tentacool': 'tentacool', 'solaroc': 'solrock', 'sorboul': 'vanillish', 'wailmer': 'wailmer', 'laggron': 'swampert', 'chovsourir': 'woobat', 'nodulithe': 'roggenrola', 'darumacho_mode_normal': 'darmanitan_standard_mode', 'yanmega': 'yanmega', 'magneton': 'magneton', 'aeropteryx': 'archeops', 'fulguris_forme_totemique': 'thundurus_therian_forme', 'tutafeh': 'yamask', 'chetiflor': 'bellsprout', 'melodelfe': 'clefable', 'colimucus': 'sliggoo', 'tiplouf': 'piplup', 'cacturne': 'cacturne', 'grotichon': 'pignite', 'salameche': 'charmander', 'anorith': 'anorith', 'deoxys_forme_defense': 'deoxys_defense_forme', 'electrode': 'electrode', 'nucleos': 'solosis', 'hypocean': 'seadra', 'motisma_forme_lavage': 'rotom_wash_rotom', 'iguolta': 'heliolisk', 'gringolem': 'golett', 'sorbouboul': 'vanilluxe', 'foretress': 'forretress', 'giratina_forme_originelle': 'giratina_origin_forme', 'corboss': 'honchkrow', 'scrutella': 'gothita', 'ramoloss': 'slowpoke', 'kangourex': 'kangaskhan', 'doduo': 'doduo', 'fluvetin': 'spritzee', 'hariyama': 'hariyama', 'muciole': 'volbeat', 'scobolide': 'whirlipede', 'machopeur': 'machoke', 'elekid': 'elekid', 'trioxhydre': 'hydreigon', 'dardargnan': 'beedrill', 'blindepique': 'chesnaught', 'majaspic': 'serperior', 'parasect': 'parasect', 'galeking': 'aggron', 'xerneas': 'xerneas', 'rattata': 'rattata', 'metang': 'metang', 'relicanth': 'relicanth', 'feuillajou': 'pansage', 'gamblast': 'clawitzer', 'shaymin_forme_celeste': 'shaymin_sky_forme', 'steelix': 'steelix', 'lepidonille': 'scatterbug', 'simiabraz': 'infernape', 'babimanta': 'mantyke', 'megapagos': 'carracosta', 'pandespiegle': 'pancham', 'goupix': 'vulpix', 'gruikui': 'tepig', 'banshitrouye_taille_maxi': 'gourgeist_large_size', 'kraknoix': 'trapinch', 'crefadet': 'azelf', 'typhlosion': 'typhlosion', 'dodrio': 'dodrio', 'rondoudou': 'jigglypuff', 'statitik': 'joltik', 'flotajou': 'panpour', 'blizzaroi': 'abomasnow', 'drattak': 'salamence', 'hypotrempe': 'horsea', 'trousselin': 'klefki', 'wailord': 'wailord', 'leopardus': 'liepard', 'medhyena': 'poochyena', 'galekid': 'aron', 'gigalithe': 'gigalith', 'darumacho_mode_daruma': 'darmanitan_zen_mode', 'keldeo': 'keldeo', 'hyporoi': 'kingdra', 'macronium': 'bayleef', 'spoink': 'spoink', 'rafflesia': 'vileplume', 'charmillon': 'beautifly', 'cheniselle_cape_sol': 'wormadam_sandy_cloak', 'lianaja': 'servine', 'exagide_forme_parade': 'aegislash_blade_forme', 'aeromite': 'venomoth', 'colombeau': 'tranquill', 'coxy': 'ledyba', 'feuforeve': 'misdreavus', 'munna': 'munna', 'cresselia': 'cresselia', 'neitram': 'beheeyem', 'carapagos': 'tirtouga', 'meloetta_forme_voix': 'meloetta_aria_forme', 'spectrum': 'haunter', 'goinfrex': 'munchlax', 'kyogre': 'kyogre', 'yanma': 'yanma', 'mega_demolosse': 'mega_houndoom', 'mastouffe': 'stoutland', 'mega_dracaufeu_x': 'mega_charizard_x', 'mega_dracaufeu_y': 'mega_charizard_y', 'deoxys_forme_attaque': 'deoxys_attack_forme', 'groret': 'grumpig', 'solochi': 'deino', 'pomdepik': 'pineco', 'noacier': 'ferrothorn', 'skelenox': 'duskull', 'gallame': 'gallade', 'drakkarmin': 'druddigon', 'lineon': 'linoone', 'chamallot': 'numel', 'groudon': 'groudon', 'flagadoss': 'slowbro', 'osselait': 'cubone', 'roucool': 'pidgey', 'lovdisc': 'luvdisc', 'farfuret': 'sneasel', 'moufflair': 'skuntank', 'brutalibre': 'hawlucha', 'couafarel': 'furfrou', 'luxio': 'luxio', 'boreas_forme_avatar': 'tornadus_incarnate_forme', 'alakazam': 'alakazam', 'melokrik': 'kricketune', 'clamiral': 'samurott', 'draco': 'dragonair', 'avaltout': 'swalot', 'fulguris_forme_avatar': 'thundurus_incarnate_forme', 'lockpin': 'lopunny', 'golemastoc': 'golurk', 'nidoran_m': 'nidoran_m', 'crehelf': 'uxie', 'nidoran_f': 'nidoran_f', 'raichu': 'raichu', 'cizayox': 'scizor', 'crabaraque': 'crustle', 'pikachu': 'pikachu', 'bruyverne': 'noivern', 'rayquaza': 'rayquaza', 'haydaim': 'sawsbuck', 'coconfort': 'kakuna', 'kirlia': 'kirlia', 'larveyette': 'sewaddle', 'doudouvet': 'cottonee', 'frison': 'bouffalant', 'kyurem_noir': 'kyurem_black_kyurem', 'mega_gardevoir': 'mega_gardevoir', 'regice': 'regice', 'mascaiman': 'sandile', 'batracne': 'palpitoad', 'flabebe': 'flabebe', 'scorvol': 'gliscor', 'tarinor': 'nosepass', 'giratina_forme_alternative': 'giratina_altered_forme', 'aspicot': 'weedle', 'leveinard': 'chansey', 'miasmax': 'garbodor', 'zygarde': 'zygarde', 'polarhume': 'cubchoo', 'nosferalto': 'golbat', 'fermite': 'durant', 'mega_tortank': 'mega_blastoise', 'brasegali': 'blaziken', 'rexillius': 'tyrantrum', 'brutapode': 'scolipede', 'cradopaud': 'croagunk', 'spinda': 'spinda', 'mentali': 'espeon', 'togepi': 'togepi', 'tauros': 'tauros', 'natu': 'natu', 'nosferapti': 'zubat', 'paras': 'paras', 'axoloto': 'wooper', 'skitty': 'skitty', 'scalproie': 'bisharp', 'raikou': 'raikou', 'geolithe': 'boldore', 'toudoudou': 'igglybuff', 'bekipan': 'pelipper', 'akwakwak': 'golduck', 'hexagel': 'cryogonal', 'tadmorv': 'grimer', 'keunotor': 'bidoof', 'capumain': 'aipom', 'rhinocorne': 'rhyhorn', 'grainipiot': 'seedot', 'cheniselle_cape_dechet': 'wormadam_trash_cloak', 'latios': 'latios', 'ludicolo': 'ludicolo', 'ponyta': 'ponyta', 'ouisticram': 'chimchar', 'regigigas': 'regigigas', 'chaglam': 'glameow', 'phanpy': 'phanpy', 'ortide': 'gloom', 'mega_kangourex': 'mega_kangaskhan', 'tic': 'klink', 'nidoqueen': 'nidoqueen', 'chenipotte': 'wurmple', 'mimigal': 'spinarak', 'germignon': 'chikorita', 'phogleur': 'sealeo', 'rapasdepic': 'fearow', 'korillon': 'chingling', 'musteflott': 'floatzel', 'boguerisse': 'quilladin', 'chapignon': 'breloom', 'flambusard': 'talonflame', 'rattatac': 'raticate', 'insecateur': 'scyther', 'evoli': 'eevee', 'vacilys': 'cradily', 'mackogneur': 'machamp', 'viskuse': 'frillish', 'grenousse': 'froakie', 'elekable': 'electivire', 'grodoudou': 'wigglytuff', 'barbicha': 'whiscash', 'archeomire': 'bronzor', 'baudrive': 'drifloon', 'voltali': 'jolteon', 'cabriolaine': 'skiddo', 'karaclee': 'sawk', 'motisma_forme_froid': 'rotom_frost_rotom', 'feuiloutan': 'simisage', 'ceriflor': 'cherrim', 'poichigeon': 'pidove', 'porygon_z': 'porygon_z', 'darkrai': 'darkrai', 'noctunoir': 'dusknoir', 'krabboss': 'kingler', 'smogogo': 'weezing', 'apireine': 'vespiquen', 'cornebre': 'murkrow', 'papilord': 'mothim', 'roserade': 'roserade', 'viridium': 'virizion', 'prismillon': 'vivillon', 'riolu': 'riolu', 'tarinorme': 'probopass', 'sharpedo': 'sharpedo', 'gravalanch': 'graveler', 'saquedeneu': 'tangela', 'pijako': 'chatot', 'amphinobi': 'greninja', 'aquali': 'vaporeon', 'nidoking': 'nidoking', 'reptincel': 'charmeleon', 'deflaisan': 'unfezant', 'ronflex': 'snorlax', 'incisache': 'fraxure', 'ptitard': 'poliwag', 'mega_branette': 'mega_banette', 'nenupiot': 'lotad', 'corayon': 'corsola', 'stari': 'staryu', 'etourvol': 'staravia', 'marill': 'marill', 'arakdo': 'surskit', 'demeteros_forme_avatar': 'landorus_incarnate_forme', 'betochef': 'conkeldurr', 'carabaffe': 'wartortle', 'chimpenfeu': 'monferno', 'escroco': 'krokorok', 'piafabec': 'spearow', 'nemelios': 'pyroar', 'cheniselle_cape_plante': 'wormadam_plant_cloak', 'flotoutan': 'simipour', 'vibraninf': 'vibrava', 'chinchidou': 'minccino', 'reshiram': 'reshiram', 'cobaltium': 'cobalion', 'roussil': 'braixen', 'balbuto': 'baltoy', 'porygon': 'porygon', 'aligatueur': 'feraligatr', 'scalpion': 'pawniard', 'carchacrok': 'garchomp', 'otaria': 'seel', 'exagide_forme_assaut': 'aegislash_shield_forme', 'magicarpe': 'magikarp', 'dracaufeu': 'charizard', 'heledelle': 'swellow', 'mega_ptera': 'mega_aerodactyl', 'carapuce': 'squirtle', 'queulorior': 'smeargle', 'ecremeuh': 'miltank', 'grahyena': 'mightyena', 'chenipan': 'caterpie', 'castorno': 'bibarel', 'mega_lucario': 'mega_lucario', 'malosse': 'houndour', 'obalie': 'spheal', 'cerfrousse': 'stantler', 'rosabyss': 'gorebyss', 'ninjask': 'ninjask', 'massko': 'grovyle', 'rozbouton': 'budew', 'vortente': 'carnivine', 'florizarre': 'venusaur', 'limaspeed': 'accelgor', 'grotadmorv': 'muk', 'polagriffe': 'beartic', 'cheniti': 'burmy', 'airmure': 'skarmory', 'magby': 'magby', 'rapion': 'skorupi', 'caratroc': 'shuckle', 'charpenti': 'timburr', 'balignon': 'shroomish', 'vipelierre': 'snivy', 'roigada': 'slowking', 'pichu': 'pichu', 'crustabri': 'cloyster', 'sablaireau': 'sandslash', 'aflamanoir': 'heatmor', 'mega_galeking': 'mega_aggron', 'ho_oh': 'ho_oh', 'griknot': 'gible', 'hoot_hoot': 'hoot_hoot', 'apitrini': 'combee', 'excelangue': 'lickitung', 'galegon': 'lairon', 'mimitoss': 'venonat', 'barloche': 'barboach', 'crocorible': 'krookodile', 'branette': 'banette', 'amagara': 'amaura', 'dinoclier': 'shieldon', 'magmar': 'magmar', 'laporeille': 'buneary', 'soporifik': 'drowzee', 'chevroum': 'gogoat', 'tournegrin': 'sunkern'}

list = {}
list.update ({u'Bulbizarre': {'catch': u'45', 'weight': u'6,9kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Bulbizarre', u'Niveau 16', u'Herbizarre', u'Niveau 32', u'Florizarre', u'Florizarrite', u'Mega-Florizarre'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att. Spe', 'egg': u'Monstre/Plante', 'size': u'0,7m'}})
list.update ({u'Herbizarre': {'catch': u'45', 'weight': u'13,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Bulbizarre', u'Niveau 16', u'Herbizarre', u'Niveau 32', u'Florizarre', u'Florizarrite', u'Mega-Florizarre'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att. Spe; +1 Def. Spe', 'egg': u'Monstre/Plante', 'size': u'1,0m'}})
list.update ({u'Florizarre': {'catch': u'45', 'weight': u'100,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Bulbizarre', u'Niveau 16', u'Herbizarre', u'Niveau 32', u'Florizarre', u'Florizarrite', u'Mega-Florizarre'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att. Spe; +1 Def. Spe', 'egg': u'Monstre/Plante', 'size': u'2,0m'}})
list.update ({u'Mega-Florizarre': {'catch': u'', 'weight': u'155,5kg', 'hatch': u'', 'evolutions': [u'Bulbizarre', u'Niveau 16', u'Herbizarre', u'Niveau 32', u'Florizarre', u'Florizarrite', u'Mega-Florizarre'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'', 'egg': u'', 'size': u'2,4m'}})
list.update ({u'Salameche': {'catch': u'45', 'weight': u'8,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Salameche', u'Niveau 16', u'Reptincel', u'Niveau 36', u'Dracaufeu', u'Dracaufite X', u'Dracaufite Y', u'Mega-Dracaufeu X', u'Mega-Dracaufeu Y'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Vit.', 'egg': u'Dragon/Monstre', 'size': u'0,6m'}})
list.update ({u'Reptincel': {'catch': u'45', 'weight': u'19,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Salameche', u'Niveau 16', u'Reptincel', u'Niveau 36', u'Dracaufeu', u'Dracaufite X', u'Dracaufite Y', u'Mega-Dracaufeu X', u'Mega-Dracaufeu Y'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Vit.; +1 Att. Spe', 'egg': u'Monstre/Dragon', 'size': u'1,1m'}})
list.update ({u'Dracaufeu': {'catch': u'45', 'weight': u'90,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Salameche', u'Niveau 16', u'Reptincel', u'Niveau 36', u'Dracaufeu', u'Dracaufite X', u'Dracaufite Y', u'Mega-Dracaufeu X', u'Mega-Dracaufeu Y'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+3 Att. Spe', 'egg': u'Dragon/Monstre', 'size': u'1,7m'}})
list.update ({u'Mega-Dracaufeu X': {'catch': u'', 'weight': u'110,5kg', 'hatch': u'', 'evolutions': [u'Salameche', u'Niveau 16', u'Reptincel', u'Niveau 36', u'Dracaufeu', u'Dracaufite X', u'Dracaufite Y', u'Mega-Dracaufeu X', u'Mega-Dracaufeu Y'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'', 'egg': u'', 'size': u'1,7m'}})
list.update ({u'Mega-Dracaufeu Y': {'catch': u'', 'weight': u'100,5kg', 'hatch': u'', 'evolutions': [u'Salameche', u'Niveau 16', u'Reptincel', u'Niveau 36', u'Dracaufeu', u'Dracaufite X', u'Dracaufite Y', u'Mega-Dracaufeu X', u'Mega-Dracaufeu Y'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'', 'egg': u'', 'size': u'1,7m'}})
list.update ({u'Carapuce': {'catch': u'45', 'weight': u'9,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Carapuce', u'Niveau 16', u'Carabaffe', u'Niveau 36', u'Tortank', u'Tortankite', u'Mega-Tortank'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Def.', 'egg': u'Eau 1/Monstre', 'size': u'0,5m'}})
list.update ({u'Carabaffe': {'catch': u'45', 'weight': u'22,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Carapuce', u'Niveau 16', u'Carabaffe', u'Niveau 36', u'Tortank', u'Tortankite', u'Mega-Tortank'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Def.; +1 Def. Spe', 'egg': u'Eau 1/Monstre', 'size': u'1,0m'}})
list.update ({u'Tortank': {'catch': u'45', 'weight': u'85,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Carapuce', u'Niveau 16', u'Carabaffe', u'Niveau 36', u'Tortank', u'Tortankite', u'Mega-Tortank'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+3 Def. Spe', 'egg': u'Eau 1/Monstre', 'size': u'1,6m'}})
list.update ({u'Mega-Tortank': {'catch': u'', 'weight': u'101,1kg', 'hatch': u'', 'evolutions': [u'Carapuce', u'Niveau 16', u'Carabaffe', u'Niveau 36', u'Tortank', u'Tortankite', u'Mega-Tortank'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'', 'egg': u'', 'size': u'1,6m'}})
list.update ({u'Chenipan': {'catch': u'255', 'weight': u'2,9kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Chenipan', u'Niveau 7', u'Chrysacier', u'Niveau 10', u'Papilusion'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Insecte', 'size': u'0,3m'}})
list.update ({u'Chrysacier': {'catch': u'120', 'weight': u'9,9kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Chenipan', u'Niveau 7', u'Chrysacier', u'Niveau 10', u'Papilusion'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Insecte', 'size': u'0,7m'}})
list.update ({u'Papilusion': {'catch': u'45', 'weight': u'32,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Chenipan', u'Niveau 7', u'Chrysacier', u'Niveau 10', u'Papilusion'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe; +1 Def. Spe', 'egg': u'Insecte', 'size': u'1,1m'}})
list.update ({u'Aspicot': {'catch': u'255', 'weight': u'3,2kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Aspicot', u'Niveau 7', u'Coconfort', u'Niveau 10', u'Dardargnan'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Insecte', 'size': u'0,3m'}})
list.update ({u'Coconfort': {'catch': u'120', 'weight': u'10,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Aspicot', u'Niveau 7', u'Coconfort', u'Niveau 10', u'Dardargnan'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Insecte', 'size': u'0,6m'}})
list.update ({u'Dardargnan': {'catch': u'45', 'weight': u'29,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Aspicot', u'Niveau 7', u'Coconfort', u'Niveau 10', u'Dardargnan'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.; +1 Def. Spe', 'egg': u'Insecte', 'size': u'1,0m'}})
list.update ({u'Roucool': {'catch': u'255', 'weight': u'1,8kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Roucool', u'Niveau 18', u'Roucoups', u'Niveau 36', u'Roucarnage'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Vol', 'size': u'0,3m'}})
list.update ({u'Roucoups': {'catch': u'120', 'weight': u'30,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Roucool', u'Niveau 18', u'Roucoups', u'Niveau 36', u'Roucarnage'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Vol', 'size': u'1,1m'}})
list.update ({u'Roucarnage': {'catch': u'45', 'weight': u'39,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Roucool', u'Niveau 18', u'Roucoups', u'Niveau 36', u'Roucarnage'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Vit.', 'egg': u'Vol', 'size': u'1,5m'}})
list.update ({u'Rattata': {'catch': u'255', 'weight': u'3,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Rattata', u'Niveau 20', u'Rattatac'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,3m'}})
list.update ({u'Rattatac': {'catch': u'127', 'weight': u'18,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Rattata', u'Niveau 20', u'Rattatac'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'0,7m'}})
list.update ({u'Piafabec': {'catch': u'255', 'weight': u'2,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Piafabec', u'Niveau 20', u'Rapasdepic'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Vol', 'size': u'0,3m'}})
list.update ({u'Rapasdepic': {'catch': u'90', 'weight': u'38,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Piafabec', u'Niveau 20', u'Rapasdepic'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Vol', 'size': u'1,2m'}})
list.update ({u'Abo': {'catch': u'255', 'weight': u'6,9kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Abo', u'Niveau 22', u'Arbok'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol/Dragon', 'size': u'2,0m'}})
list.update ({u'Arbok': {'catch': u'90', 'weight': u'65,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Abo', u'Niveau 22', u'Arbok'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol/Dragon', 'size': u'3,5m'}})
list.update ({u'Pikachu': {'catch': u'190', 'weight': u'6,0kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Pichu', u'Bonheur', u'Pikachu', u'Avec une Pierre Foudre', u'Raichu'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol/Fee', 'size': u'0,4m'}})
list.update ({u'Raichu': {'catch': u'75', 'weight': u'30,0kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Pichu', u'Bonheur', u'Pikachu', u'Avec une Pierre Foudre', u'Raichu'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Vit.', 'egg': u'Sol/Fee', 'size': u'0,8m'}})
list.update ({u'Sabelette': {'catch': u'255', 'weight': u'12,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Sabelette', u'Niveau 22', u'Sablaireau'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Sol', 'size': u'0,6m'}})
list.update ({u'Sablaireau': {'catch': u'90', 'weight': u'29,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Sabelette', u'Niveau 22', u'Sablaireau'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Nidoran F': {'catch': u'235', 'weight': u'7,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Nidoran F', u'Niveau 16', u'Nidorina', u'Avec une Pierre Lune', u'Nidoqueen'], 'gender': u'100% femelle; 0% male', 'ev': u'+1 PV', 'egg': u'Monstre/Sol', 'size': u'0,4m'}})
list.update ({u'Nidorina': {'catch': u'120', 'weight': u'20,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Nidoran F', u'Niveau 16', u'Nidorina', u'Avec une Pierre Lune', u'Nidoqueen'], 'gender': u'100% femelle; 0% male', 'ev': u'+2 PV', 'egg': u'Sans oeuf', 'size': u'0,8m'}})
list.update ({u'Nidoqueen': {'catch': u'45', 'weight': u'60,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Nidoran F', u'Niveau 16', u'Nidorina', u'Avec une Pierre Lune', u'Nidoqueen'], 'gender': u'100% femelle; 0% male', 'ev': u'+3 PV', 'egg': u'Sans oeuf', 'size': u'1,3m'}})
list.update ({u'Nidoran M': {'catch': u'235', 'weight': u'9,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Nidoran M', u'Niveau 16', u'Nidorino', u'Avec une Pierre Lune', u'Nidoking'], 'gender': u'0% femelle; 100% male', 'ev': u'+1 Att.', 'egg': u'Monstre/Sol', 'size': u'0,5m'}})
list.update ({u'Nidorino': {'catch': u'120', 'weight': u'19,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Nidoran M', u'Niveau 16', u'Nidorino', u'Avec une Pierre Lune', u'Nidoking'], 'gender': u'0% femelle; 100% male', 'ev': u'+2 Att.', 'egg': u'Monstre/Sol', 'size': u'0,9m'}})
list.update ({u'Nidoking': {'catch': u'45', 'weight': u'62,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Nidoran M', u'Niveau 16', u'Nidorino', u'Avec une Pierre Lune', u'Nidoking'], 'gender': u'0% femelle; 100% male', 'ev': u'+3 Att.', 'egg': u'Monstre/Sol', 'size': u'1,4m'}})
list.update ({u'Melofee': {'catch': u'150', 'weight': u'7,5kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Melo', u'Bonheur', u'Melofee', u'Avec une Pierre Lune', u'Melodelfe'], 'gender': u'75% femelle; 25% male', 'ev': u'+2 PV', 'egg': u'Fee', 'size': u'0,6m'}})
list.update ({u'Melodelfe': {'catch': u'25', 'weight': u'40,0kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Melo', u'Bonheur', u'Melofee', u'Avec une Pierre Lune', u'Melodelfe'], 'gender': u'75% femelle; 25% male', 'ev': u'+3 PV', 'egg': u'Fee', 'size': u'1,3m'}})
list.update ({u'Goupix': {'catch': u'190', 'weight': u'9,9kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Goupix', u'Avec une Pierre Feu', u'Feunard'], 'gender': u'25% femelle; 75% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,6m'}})
list.update ({u'Feunard': {'catch': u'75', 'weight': u'19,9kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Goupix', u'Avec une Pierre Feu', u'Feunard'], 'gender': u'75% femelle; 25% male', 'ev': u'+1 Vit.; +1 Def. Spe', 'egg': u'Sol', 'size': u'1,1m'}})
list.update ({u'Rondoudou': {'catch': u'170', 'weight': u'5,5kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Toudoudou', u'Bonheur', u'Rondoudou', u'Avec une Pierre Lune', u'Grodoudou'], 'gender': u'75% femelle; 25% male', 'ev': u'+2 PV', 'egg': u'Fee', 'size': u'0,5m'}})
list.update ({u'Grodoudou': {'catch': u'50', 'weight': u'12,0kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Toudoudou', u'Bonheur', u'Rondoudou', u'Avec une Pierre Lune', u'Grodoudou'], 'gender': u'75% femelle; 25% male', 'ev': u'+3 PV', 'egg': u'Fee', 'size': u'1,0m'}})
list.update ({u'Nosferapti': {'catch': u'255', 'weight': u'7,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Nosferapti', u'Niveau 22', u'Nosferalto', u'Bonheur', u'Nostenfer'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Vol', 'size': u'0,8m'}})
list.update ({u'Nosferalto': {'catch': u'90', 'weight': u'55,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Nosferapti', u'Niveau 22', u'Nosferalto', u'Bonheur', u'Nostenfer'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Vol', 'size': u'1,6m'}})
list.update ({u'Mystherbe': {'catch': u'255', 'weight': u'5,4kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Mystherbe', u'Niveau 21', u'Ortide', u'Avec une Pierre Plante', u'Avec une Pierresoleil', u'Rafflesia', u'Joliflor'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Plante', 'size': u'0,5m'}})
list.update ({u'Ortide': {'catch': u'120', 'weight': u'8,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Mystherbe', u'Niveau 21', u'Ortide', u'Avec une Pierre Plante', u'Avec une Pierresoleil', u'Rafflesia', u'Joliflor'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Plante', 'size': u'0,8m'}})
list.update ({u'Rafflesia': {'catch': u'45', 'weight': u'18,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Mystherbe', u'Niveau 21', u'Ortide', u'Avec une Pierre Plante', u'Avec une Pierresoleil', u'Rafflesia', u'Joliflor'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att. Spe', 'egg': u'Plante', 'size': u'1,2m'}})
list.update ({u'Paras': {'catch': u'190', 'weight': u'5,4kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Paras', u'Niveau 24', u'Parasect'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Insecte/Plante', 'size': u'0,3m'}})
list.update ({u'Parasect': {'catch': u'75', 'weight': u'29,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Paras', u'Niveau 24', u'Parasect'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.; +1 Def.', 'egg': u'Insecte/Plante', 'size': u'1,0m'}})
list.update ({u'Mimitoss': {'catch': u'190', 'weight': u'30,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Mimitoss', u'Niveau 31', u'Aeromite'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Insecte', 'size': u'1,0m'}})
list.update ({u'Aeromite': {'catch': u'75', 'weight': u'12,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Mimitoss', u'Niveau 31', u'Aeromite'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe; +1 Vit.', 'egg': u'Insecte', 'size': u'1,5m'}})
list.update ({u'Taupiqueur': {'catch': u'255', 'weight': u'0,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Taupiqueur', u'Niveau 26', u'Triopikeur'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,2m'}})
list.update ({u'Triopikeur': {'catch': u'50', 'weight': u'33,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Taupiqueur', u'Niveau 26', u'Triopikeur'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'0,7m'}})
list.update ({u'Miaouss': {'catch': u'255', 'weight': u'4,2kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Miaouss', u'Niveau 28', u'Persian'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,4m'}})
list.update ({u'Persian': {'catch': u'90', 'weight': u'32,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Miaouss', u'Niveau 28', u'Persian'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Psykokwak': {'catch': u'190', 'weight': u'19,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Psykokwak', u'Niveau 33', u'Akwakwak'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Eau 1/Sol', 'size': u'0,8m'}})
list.update ({u'Akwakwak': {'catch': u'75', 'weight': u'76,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Psykokwak', u'Niveau 33', u'Akwakwak'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Eau 1/Sol', 'size': u'1,7m'}})
list.update ({u'Ferosinge': {'catch': u'190', 'weight': u'28,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ferosinge', u'Niveau 28', u'Colossinge'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol', 'size': u'0,5m'}})
list.update ({u'Colossinge': {'catch': u'75', 'weight': u'32,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ferosinge', u'Niveau 28', u'Colossinge'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Caninos': {'catch': u'190', 'weight': u'19,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Caninos', u'Avec une Pierre Feu', u'Arcanin'], 'gender': u'25% femelle; 75% male', 'ev': u'+1 Att', 'egg': u'Sol', 'size': u'0,7m'}})
list.update ({u'Arcanin': {'catch': u'75', 'weight': u'155,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Caninos', u'Avec une Pierre Feu', u'Arcanin'], 'gender': u'25% femelle; 75% male', 'ev': u'+2 Att.', 'egg': u'Sol', 'size': u'1,9m'}})
list.update ({u'Ptitard': {'catch': u'255', 'weight': u'12,4kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ptitard', u'Niveau 25', u'Tetarte', u'Avec une Pierre Eau', u'Echange en tenant Roche Royale', u'Tartard', u'Tarpaud'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Eau 1', 'size': u'0,6m'}})
list.update ({u'Tetarte': {'catch': u'120', 'weight': u'20,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ptitard', u'Niveau 25', u'Tetarte', u'Avec une Pierre Eau', u'Echange en tenant Roche Royale', u'Tartard', u'Tarpaud'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Eau 1', 'size': u'1,0m'}})
list.update ({u'Tartard': {'catch': u'45', 'weight': u'54,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ptitard', u'Niveau 25', u'Tetarte', u'Avec une Pierre Eau', u'Echange en tenant Roche Royale', u'Tartard', u'Tarpaud'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Def.', 'egg': u'Eau 1', 'size': u'1,3m'}})
list.update ({u'Abra': {'catch': u'200', 'weight': u'19,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Abra', u'Niveau 16', u'Kadabra', u'Echange', u'Alakazam', u'Alakazamite', u'Mega-Alakazam'], 'gender': u'25% femelle; 75% male', 'ev': u'+1 Att. Spe', 'egg': u'Humanoide', 'size': u'0,9m'}})
list.update ({u'Kadabra': {'catch': u'100', 'weight': u'56,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Abra', u'Niveau 16', u'Kadabra', u'Echange', u'Alakazam', u'Alakazamite', u'Mega-Alakazam'], 'gender': u'25% femelle; 75% male', 'ev': u'+2 Att. Spe', 'egg': u'Humanoide', 'size': u'1,3m'}})
list.update ({u'Alakazam': {'catch': u'50', 'weight': u'48,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Abra', u'Niveau 16', u'Kadabra', u'Echange', u'Alakazam', u'Alakazamite', u'Mega-Alakazam'], 'gender': u'25% femelle; 75% male', 'ev': u'+3 Att. Spe', 'egg': u'Humanoide', 'size': u'1,5m'}})
list.update ({u'Mega-Alakazam': {'catch': u'', 'weight': u'48,0kg', 'hatch': u'', 'evolutions': [u'Abra', u'Niveau 16', u'Kadabra', u'Echange', u'Alakazam', u'Alakazamite', u'Mega-Alakazam'], 'gender': u'25% femelle; 75% male', 'ev': u'', 'egg': u'', 'size': u'1,2m'}})
list.update ({u'Machoc': {'catch': u'180', 'weight': u'19,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Machoc', u'Niveau 28', u'Machopeur', u'Echange', u'Mackogneur'], 'gender': u'25% femelle; 75% male', 'ev': u'+1 Att.', 'egg': u'Humanoide', 'size': u'0,8m'}})
list.update ({u'Machopeur': {'catch': u'90', 'weight': u'70,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Machoc', u'Niveau 28', u'Machopeur', u'Echange', u'Mackogneur'], 'gender': u'25% femelle; 75% male', 'ev': u'+2 Att.', 'egg': u'Humanoide', 'size': u'1,5m'}})
list.update ({u'Mackogneur': {'catch': u'45', 'weight': u'130,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Machoc', u'Niveau 28', u'Machopeur', u'Echange', u'Mackogneur'], 'gender': u'25% femelle; 75% male', 'ev': u'+3 Att.', 'egg': u'Humanoide', 'size': u'1,6m'}})
list.update ({u'Chetiflor': {'catch': u'255', 'weight': u'4,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Chetiflor', u'Niveau 21', u'Boustiflor', u'Avec une Pierre Plante', u'Empiflor'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Plante', 'size': u'0,7m'}})
list.update ({u'Boustiflor': {'catch': u'120', 'weight': u'6,4kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Chetiflor', u'Niveau 21', u'Boustiflor', u'Avec une Pierre Plante', u'Empiflor'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Plante', 'size': u'1,0m'}})
list.update ({u'Empiflor': {'catch': u'45', 'weight': u'15,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Chetiflor', u'Niveau 21', u'Boustiflor', u'Avec une Pierre Plante', u'Empiflor'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att.', 'egg': u'Plante', 'size': u'1,7m'}})
list.update ({u'Tentacool': {'catch': u'190', 'weight': u'45,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tentacool', u'Niveau 30', u'Tentacruel'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Eau 3', 'size': u'0,9m'}})
list.update ({u'Tentacruel': {'catch': u'60', 'weight': u'55,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tentacool', u'Niveau 30', u'Tentacruel'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def. Spe', 'egg': u'Eau 3', 'size': u'1,6m'}})
list.update ({u'Racaillou': {'catch': u'255', 'weight': u'20,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Racaillou', u'Niveau 25', u'Gravalanch', u'Echange', u'Grolem'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Mineral', 'size': u'0,4m'}})
list.update ({u'Gravalanch': {'catch': u'120', 'weight': u'105,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Racaillou', u'Niveau 25', u'Gravalanch', u'Echange', u'Grolem'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Mineral', 'size': u'1,0m'}})
list.update ({u'Grolem': {'catch': u'45', 'weight': u'300,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Racaillou', u'Niveau 25', u'Gravalanch', u'Echange', u'Grolem'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Def.', 'egg': u'Mineral', 'size': u'1,4m'}})
list.update ({u'Ponyta': {'catch': u'190', 'weight': u'30,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ponyta', u'Niveau 40', u'Galopa'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Galopa': {'catch': u'60', 'weight': u'95,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ponyta', u'Niveau 40', u'Galopa'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'1,7m'}})
list.update ({u'Ramoloss': {'catch': u'190', 'weight': u'36,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ramoloss', u'Niveau 37', u'Echange en tenant Roche Royale', u'Flagadoss', u'Roigada'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Monstre/Eau 1', 'size': u'1,2m'}})
list.update ({u'Flagadoss': {'catch': u'75', 'weight': u'78,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ramoloss', u'Niveau 37', u'Echange en tenant Roche Royale', u'Flagadoss', u'Roigada'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Monstre/Eau 1', 'size': u'1,6m'}})
list.update ({u'Magneti': {'catch': u'190', 'weight': u'6,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Magneti', u'Niveau 30', u'Magneton', u'Gain de niveau dans un lieu indique', u'Magnezone'], 'gender': u'Asexue', 'ev': u'+1 Att. Spe', 'egg': u'Mineral', 'size': u'0,3m'}})
list.update ({u'Magneton': {'catch': u'60', 'weight': u'60,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Magneti', u'Niveau 30', u'Magneton', u'Gain de niveau dans un lieu indique', u'Magnezone'], 'gender': u'Asexue', 'ev': u'+2 Att. Spe', 'egg': u'Mineral', 'size': u'1,0m'}})
list.update ({u'Canarticho': {'catch': u'45', 'weight': u'15,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Vol/Sol', 'size': u'0,8m'}})
list.update ({u'Doduo': {'catch': u'190', 'weight': u'39,2kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Doduo', u'Niveau 31', u'Dodrio'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Vol', 'size': u'1,4m'}})
list.update ({u'Dodrio': {'catch': u'45', 'weight': u'85,2kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Doduo', u'Niveau 31', u'Dodrio'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Vol', 'size': u'1,8m'}})
list.update ({u'Otaria': {'catch': u'190', 'weight': u'90,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Otaria', u'Niveau 34', u'Lamantine'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Eau 1/Sol', 'size': u'1,1m'}})
list.update ({u'Lamantine': {'catch': u'75', 'weight': u'120,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Otaria', u'Niveau 34', u'Lamantine'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def. Spe', 'egg': u'Eau 1/Sol', 'size': u'1,7m'}})
list.update ({u'Tadmorv': {'catch': u'190', 'weight': u'30,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tadmorv', u'Niveau 38', u'Grotadmorv'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Indetermine', 'size': u'0,9m'}})
list.update ({u'Grotadmorv': {'catch': u'75', 'weight': u'30,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tadmorv', u'Niveau 38', u'Grotadmorv'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV; +1 Att.', 'egg': u'Indetermine', 'size': u'1,2m'}})
list.update ({u'Kokiyas': {'catch': u'190', 'weight': u'4,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Kokiyas', u'Avec une Pierre Eau', u'Crustabri'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Eau 3', 'size': u'0,3m'}})
list.update ({u'Crustabri': {'catch': u'60', 'weight': u'132,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Kokiyas', u'Avec une Pierre Eau', u'Crustabri'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Eau 3', 'size': u'1,5m'}})
list.update ({u'Fantominus': {'catch': u'190', 'weight': u'0,1kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Fantominus', u'Niveau 25', u'Spectrum', u'Echange', u'Ectoplasma', u'Ectoplasmite', u'Mega-Ectoplasma'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Indetermine', 'size': u'1,3m'}})
list.update ({u'Spectrum': {'catch': u'90', 'weight': u'0,1kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Fantominus', u'Niveau 25', u'Spectrum', u'Echange', u'Ectoplasma', u'Ectoplasmite', u'Mega-Ectoplasma'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Indetermine', 'size': u'1,6m'}})
list.update ({u'Ectoplasma': {'catch': u'45', 'weight': u'40,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Fantominus', u'Niveau 25', u'Spectrum', u'Echange', u'Ectoplasma', u'Ectoplasmite', u'Mega-Ectoplasma'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att. Spe', 'egg': u'Indetermine', 'size': u'1,5m'}})
list.update ({u'Mega-Ectoplasma': {'catch': u'', 'weight': u'40,5kg', 'hatch': u'', 'evolutions': [u'Fantominus', u'Niveau 25', u'Spectrum', u'Echange', u'Ectoplasma', u'Ectoplasmite', u'Mega-Ectoplasma'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'', 'size': u'1,4m'}})
list.update ({u'Onix': {'catch': u'45', 'weight': u'210,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Onix', u'Echange en tenant Peau Metal', u'Steelix'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Mineral', 'size': u'8,8m'}})
list.update ({u'Soporifik': {'catch': u'190', 'weight': u'32,4kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Soporifik', u'Niveau 26', u'Hypnomade'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Humanoide', 'size': u'1,0m'}})
list.update ({u'Hypnomade': {'catch': u'75', 'weight': u'75,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Soporifik', u'Niveau 26', u'Hypnomade'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def. Spe', 'egg': u'Humanoide', 'size': u'1,6m'}})
list.update ({u'Krabby': {'catch': u'225', 'weight': u'6,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Krabby', u'Niveau 28', u'Krabboss'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Eau 3', 'size': u'0,4m'}})
list.update ({u'Krabboss': {'catch': u'60', 'weight': u'60,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Krabby', u'Niveau 28', u'Krabboss'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Eau 3', 'size': u'1,3m'}})
list.update ({u'Voltorbe': {'catch': u'190', 'weight': u'10,4kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Voltorbe', u'Niveau 30', u'Electrode'], 'gender': u'Asexue', 'ev': u'+1 Vit.', 'egg': u'Mineral', 'size': u'0,5m'}})
list.update ({u'Electrode': {'catch': u'60', 'weight': u'66,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Voltorbe', u'Niveau 30', u'Electrode'], 'gender': u'Asexue', 'ev': u'+2 Vit.', 'egg': u'Mineral', 'size': u'1,2m'}})
list.update ({u'Noeunoeuf': {'catch': u'90', 'weight': u'2,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Noeunoeuf', u'Avec une Pierre Plante', u'Noadkoko'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Plante', 'size': u'0,4m'}})
list.update ({u'Noadkoko': {'catch': u'45', 'weight': u'120,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Noeunoeuf', u'Avec une Pierre Plante', u'Noadkoko'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Plante', 'size': u'2,0m'}})
list.update ({u'Osselait': {'catch': u'190', 'weight': u'6,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Osselait', u'Niveau 28', u'Ossatueur'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Monstre', 'size': u'0,4m'}})
list.update ({u'Ossatueur': {'catch': u'75', 'weight': u'45,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Osselait', u'Niveau 28', u'Ossatueur'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Monstre', 'size': u'1,0m'}})
list.update ({u'Kicklee': {'catch': u'45', 'weight': u'49,8kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Debugant', u'Niveau 20, Attaque Defense', u'Niveau 20, Attaque Defense', u'Niveau 20, Attaque et Defense identiques', u'Kicklee', u'Tygnon', u'Kapoera'], 'gender': u'0% femelle; 100% male', 'ev': u'+2 Att.', 'egg': u'Humanoide', 'size': u'1,5m'}})
list.update ({u'Tygnon': {'catch': u'45', 'weight': u'50,2kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Debugant', u'Niveau 20, Attaque Defense', u'Niveau 20, Attaque Defense', u'Niveau 20, Attaque et Defense identiques', u'Kicklee', u'Tygnon', u'Kapoera'], 'gender': u'0% femelle; 100% male', 'ev': u'+2 Def. Spe', 'egg': u'Humanoide', 'size': u'1,4m'}})
list.update ({u'Excelangue': {'catch': u'45', 'weight': u'65,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Excelangue', u"En apprenant l'attaque Roulade", u'Coudlangue'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Monstre', 'size': u'1,2m'}})
list.update ({u'Smogo': {'catch': u'190', 'weight': u'1,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Smogo', u'Niveau 35', u'Smogogo'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Indetermine', 'size': u'0,6m'}})
list.update ({u'Smogogo': {'catch': u'60', 'weight': u'9,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Smogo', u'Niveau 35', u'Smogogo'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Indetermine', 'size': u'1,2m'}})
list.update ({u'Rhinocorne': {'catch': u'120', 'weight': u'115,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Rhinocorne', u'Niveau 42', u'Rhinoferos', u"Echange en tenant l'objet Protecteur", u'Rhinastoc'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Monstre/Sol', 'size': u'1,0m'}})
list.update ({u'Rhinoferos': {'catch': u'60', 'weight': u'120,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Rhinocorne', u'Niveau 42', u'Rhinoferos', u"Echange en tenant l'objet Protecteur", u'Rhinastoc'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Monstre/Sol', 'size': u'1,9m'}})
list.update ({u'Leveinard': {'catch': u'30', 'weight': u'34,6kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Ptiravi', u'Gain de niveau en tenant une Pierre Ovale', u'Leveinard', u'Bonheur', u'Leuphorie'], 'gender': u'100% femelle; 0% male', 'ev': u'+2 PV', 'egg': u'Fee', 'size': u'1,1m'}})
list.update ({u'Saquedeneu': {'catch': u'45', 'weight': u'35,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Saquedeneu', u"En apprenant l'attaque Pouv.Antique", u'Bouldeneu'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Plante', 'size': u'1,0m'}})
list.update ({u'Kangourex': {'catch': u'45', 'weight': u'80,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Kangourex', u'Kangourexite', u'Mega-Kangourex'], 'gender': u'100% femelle; 0% male', 'ev': u'+2 PV', 'egg': u'Monstre', 'size': u'2,2m'}})
list.update ({u'Mega-Kangourex': {'catch': u'', 'weight': u'100,0kg', 'hatch': u'', 'evolutions': [u'Kangourex', u'Kangourexite', u'Mega-Kangourex'], 'gender': u'100% femelle; 0% male', 'ev': u'', 'egg': u'', 'size': u'2,2m'}})
list.update ({u'Hypotrempe': {'catch': u'225', 'weight': u'8,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Hypotrempe', u'Niveau 32', u'Hypocean', u"Echange en tenant l'objet Ecaille Draco", u'Hyporoi'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Eau 1/Dragon', 'size': u'0,4m'}})
list.update ({u'Hypocean': {'catch': u'75', 'weight': u'25,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Hypotrempe', u'Niveau 32', u'Hypocean', u"Echange en tenant l'objet Ecaille Draco", u'Hyporoi'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.; +1 Att. Spe', 'egg': u'Eau 1/Dragon', 'size': u'1,2m'}})
list.update ({u'Poissirene': {'catch': u'225', 'weight': u'15,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Poissirene', u'Niveau 33', u'Poissoroy'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Eau 2', 'size': u'0,6m'}})
list.update ({u'Poissoroy': {'catch': u'60', 'weight': u'39,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Poissirene', u'Niveau 33', u'Poissoroy'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Eau 2', 'size': u'1,3m'}})
list.update ({u'Stari': {'catch': u'225', 'weight': u'34,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Stari', u'Pierre Eau', u'Staross'], 'gender': u'Asexue', 'ev': u'+1 Vit.', 'egg': u'Eau 3', 'size': u'0,8m'}})
list.update ({u'Staross': {'catch': u'60', 'weight': u'80,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Stari', u'Pierre Eau', u'Staross'], 'gender': u'Asexue', 'ev': u'+2 Vit.', 'egg': u'Eau 3', 'size': u'1,1m'}})
list.update ({u'M. Mime': {'catch': u'45', 'weight': u'54,5kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Mime Jr.', u"En apprenant l'attaque Copie", u'M. Mime'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def. Spe', 'egg': u'Humanoide', 'size': u'1,3m'}})
list.update ({u'Insecateur': {'catch': u'45', 'weight': u'56,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Insecateur', u'Echange en tenant Peau Metal', u'Cizayox', u'Mega-Evolution', u'Mega-Cizayox'], 'gender': u'Repartition inconnue', 'ev': u'+1 Att.', 'egg': u'Insecte', 'size': u'1,5m'}})
list.update ({u'Lippoutou': {'catch': u'45', 'weight': u'40,6kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Lippouti', u'Niveau 30', u'Lippoutou'], 'gender': u'100% femelle; 0% male', 'ev': u'+2 Att. Spe', 'egg': u'Humanoide', 'size': u'1,4m'}})
list.update ({u'Elektek': {'catch': u'45', 'weight': u'30,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Elekid', u'Niveau 30', u'Elektek', u'Echange en tenant Electiriseur', u'Elekable'], 'gender': u'25% femelle; 75% male', 'ev': u'+2 Vit.', 'egg': u'Humanoide', 'size': u'1,1m'}})
list.update ({u'Magmar': {'catch': u'45', 'weight': u'44,5kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Magby', u'Niveau 30', u'Magmar', u'Echange en tenant Magmariseur', u'Maganon'], 'gender': u'25% femelle; 75% male', 'ev': u'+2 Att. Spe', 'egg': u'Humanoide', 'size': u'1,3m'}})
list.update ({u'Scarabrute': {'catch': u'45', 'weight': u'55,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Scarabrute', u'Scarabruite', u'Mega-Scarabrute'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Insecte', 'size': u'1,5m'}})
list.update ({u'Mega-Scarabrute': {'catch': u'', 'weight': u'59kg', 'hatch': u'', 'evolutions': [u'Scarabrute', u'Scarabruite', u'Mega-Scarabrute'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'', 'size': u'1,7m'}})
list.update ({u'Tauros': {'catch': u'45', 'weight': u'88,4kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'0% femelle; 100% male', 'ev': u'+1 Att.; +1 Vit.', 'egg': u'Sol', 'size': u'1,4m'}})
list.update ({u'Magicarpe': {'catch': u'255', 'weight': u'10,0kg', 'hatch': u'4 cycles - 1280 pas', 'evolutions': [u'Magicarpe', u'Niveau 20', u'Leviator', u'Leviatorite', u'Mega-Leviator'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Eau 2/Dragon', 'size': u'0,9m'}})
list.update ({u'Leviator': {'catch': u'45', 'weight': u'235,0kg', 'hatch': u'4 cycles - 1280 pas', 'evolutions': [u'Magicarpe', u'Niveau 20', u'Leviator', u'Leviatorite', u'Mega-Leviator'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Eau 2/Dragon', 'size': u'6,5m'}})
list.update ({u'Mega-Leviator': {'catch': u'', 'weight': u'305,0kg', 'hatch': u'', 'evolutions': [u'Magicarpe', u'Niveau 20', u'Leviator', u'Leviatorite', u'Mega-Leviator'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'', 'size': u'6,5m'}})
list.update ({u'Lokhlass': {'catch': u'45', 'weight': u'220,0kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Monstre/Eau 1', 'size': u'2,5m'}})
list.update ({u'Metamorph': {'catch': u'35', 'weight': u'4,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 PV', 'egg': u'Metamorph', 'size': u'0,3m'}})
list.update ({u'Evoli': {'catch': u'45', 'weight': u'6,5kg', 'hatch': u'34 cycles - 8960 pas', 'evolutions': [u'Evoli', u'Avec une Pierre Eau', u'Avec une Pierre Foudre', u'Avec une Pierre Feu', u'Bonheur , Jour', u'Bonheur , Nuit', u"Pres d'une Pierre Mousse + gagne un niveau", u"Pres d'une Pierre Glacee + gagne un niveau", u"2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Def. Spe', 'egg': u'Sol', 'size': u'0,3m'}})
list.update ({u'Aquali': {'catch': u'45', 'weight': u'29,0kg', 'hatch': u'34 cycles - 8960 pas', 'evolutions': [u'Evoli', u'Avec une Pierre Eau', u'Avec une Pierre Foudre', u'Avec une Pierre Feu', u'Bonheur , Jour', u'Bonheur , Nuit', u"Pres d'une Pierre Mousse + gagne un niveau", u"Pres d'une Pierre Glacee + gagne un niveau", u"2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 PV', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Voltali': {'catch': u'45', 'weight': u'24,5kg', 'hatch': u'34 cycles - 8960 pas', 'evolutions': [u'Evoli', u'Avec une Pierre Eau', u'Avec une Pierre Foudre', u'Avec une Pierre Feu', u'Bonheur , Jour', u'Bonheur , Nuit', u"Pres d'une Pierre Mousse + gagne un niveau", u"Pres d'une Pierre Glacee + gagne un niveau", u"2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'0,8m'}})
list.update ({u'Pyroli': {'catch': u'45', 'weight': u'25,9kg', 'hatch': u'34 cycles - 8960 pas', 'evolutions': [u'Evoli', u'Avec une Pierre Eau', u'Avec une Pierre Foudre', u'Avec une Pierre Feu', u'Bonheur , Jour', u'Bonheur , Nuit', u"Pres d'une Pierre Mousse + gagne un niveau", u"Pres d'une Pierre Glacee + gagne un niveau", u"2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att.', 'egg': u'Sol', 'size': u'0,9m'}})
list.update ({u'Porygon': {'catch': u'45', 'weight': u'36,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Porygon', u'Echange en tenant Ameliorator', u'Porygon2', u'Echange en tenant CD Douteux', u'Porygon-Z'], 'gender': u'Asexue', 'ev': u'+1 Att. Spe', 'egg': u'Mineral', 'size': u'0,8m'}})
list.update ({u'Amonita': {'catch': u'45', 'weight': u'7,5kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [u'Amonita', u'Niveau 40', u'Amonistar'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Def.', 'egg': u'Eau 1/Eau 3', 'size': u'0,4m'}})
list.update ({u'Amonistar': {'catch': u'45', 'weight': u'35,0kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [u'Amonita', u'Niveau 40', u'Amonistar'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Def.', 'egg': u'Eau 1/Eau 3', 'size': u'1,0m'}})
list.update ({u'Kabuto': {'catch': u'45', 'weight': u'11,5kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [u'Kabuto', u'Niveau 40', u'Kabutops'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Def.', 'egg': u'Eau 1/Eau 3', 'size': u'0,5m'}})
list.update ({u'Kabutops': {'catch': u'45', 'weight': u'40,5kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [u'Kabuto', u'Niveau 40', u'Kabutops'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att.', 'egg': u'Eau 1/Eau 3', 'size': u'1,3m'}})
list.update ({u'Ptera': {'catch': u'45', 'weight': u'59,0kg', 'hatch': u'34 cycles - 8960 pas', 'evolutions': [u'Ptera', u'Pteraite', u'Mega-Ptera'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Vit.', 'egg': u'Vol', 'size': u'1,8m'}})
list.update ({u'Ronflex': {'catch': u'25', 'weight': u'460,0kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Goinfrex', u'Bonheur', u'Ronflex'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 PV', 'egg': u'Monstre', 'size': u'2,1m'}})
list.update ({u'Artikodin': {'catch': u'3', 'weight': u'55,4kg', 'hatch': u'79 cycles - 20480 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Def. Spe', 'egg': u'Sans oeuf', 'size': u'1,7m'}})
list.update ({u'Electhor': {'catch': u'3', 'weight': u'52,6kg', 'hatch': u'79 cycles - 20480 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Att. Spe', 'egg': u'Sans oeuf', 'size': u'1,6m'}})
list.update ({u'Sulfura': {'catch': u'3', 'weight': u'60,0kg', 'hatch': u'79 cycles - 20480 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Att. Spe', 'egg': u'Sans oeuf', 'size': u'2,0m'}})
list.update ({u'Minidraco': {'catch': u'45', 'weight': u'3,3kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Minidraco', u'Niveau 30', u'Draco', u'Niveau 55', u'Dracolosse'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Dragon/Eau 1', 'size': u'1,8m'}})
list.update ({u'Draco': {'catch': u'45', 'weight': u'16,5kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Minidraco', u'Niveau 30', u'Draco', u'Niveau 55', u'Dracolosse'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Dragon/Eau 1', 'size': u'4,0m'}})
list.update ({u'Dracolosse': {'catch': u'45', 'weight': u'210,0kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Minidraco', u'Niveau 30', u'Draco', u'Niveau 55', u'Dracolosse'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att.', 'egg': u'Dragon/Eau 1', 'size': u'2,2m'}})
list.update ({u'Mewtwo': {'catch': u'3', 'weight': u'122,0kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [u'Mewtwo', u'Mewtwoite X', u'Mewtwoite Y', u'Mega-Mewtwo X', u'Mega-Mewtwo Y'], 'gender': u'Asexue', 'ev': u'+3 Att. Spe', 'egg': u'Sans oeuf', 'size': u'2,0m'}})
list.update ({u'Mega-Mewtwo X': {'catch': u'', 'weight': u'127,0kg', 'hatch': u'', 'evolutions': [u'Mewtwo', u'Mewtwoite X', u'Mewtwoite Y', u'Mega-Mewtwo X', u'Mega-Mewtwo Y'], 'gender': u'Asexue', 'ev': u'', 'egg': u'', 'size': u'2,3m'}})
list.update ({u'Mega-Mewtwo Y': {'catch': u'', 'weight': u'33,0kg', 'hatch': u'', 'evolutions': [u'Mewtwo', u'Mewtwoite X', u'Mewtwoite Y', u'Mega-Mewtwo X', u'Mega-Mewtwo Y'], 'gender': u'Asexue', 'ev': u'', 'egg': u'', 'size': u'1,5m'}})
list.update ({u'Mew': {'catch': u'45', 'weight': u'4,0kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 PV', 'egg': u'Sans oeuf', 'size': u'0,4m'}})
list.update ({u'Germignon': {'catch': u'45', 'weight': u'6,4kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Germignon', u'Niveau 16', u'Macronium', u'Niveau 32', u'Meganium'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Def. Spe', 'egg': u'Monstre/Plante', 'size': u'0,9m'}})
list.update ({u'Macronium': {'catch': u'45', 'weight': u'15,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Germignon', u'Niveau 16', u'Macronium', u'Niveau 32', u'Meganium'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Def.; +1 Def. Spe', 'egg': u'Monstre/Plante', 'size': u'1,2m'}})
list.update ({u'Meganium': {'catch': u'45', 'weight': u'100,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Germignon', u'Niveau 16', u'Macronium', u'Niveau 32', u'Meganium'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Def.; +2 Def. Spe', 'egg': u'Monstre/Plante', 'size': u'1,8m'}})
list.update ({u'Hericendre': {'catch': u'45', 'weight': u'7,9kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Hericendre', u'Niveau 14', u'Feurisson', u'Niveau 36', u'Typhlosion'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,5m'}})
list.update ({u'Feurisson': {'catch': u'45', 'weight': u'19kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Hericendre', u'Niveau 14', u'Feurisson', u'Niveau 36', u'Typhlosion'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att. Spe, +1 Def. Spe', 'egg': u'Sol', 'size': u'0,9m'}})
list.update ({u'Typhlosion': {'catch': u'45', 'weight': u'79,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Hericendre', u'Niveau 14', u'Feurisson', u'Niveau 36', u'Typhlosion'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+3 Att. Spe', 'egg': u'Sol', 'size': u'1,7m'}})
list.update ({u'Kaiminus': {'catch': u'45', 'weight': u'9,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Kaiminus', u'Niveau 18', u'Crocrodil', u'Niveau 30', u'Aligatueur'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att.', 'egg': u'Monstre/Eau 1', 'size': u'0,6m'}})
list.update ({u'Crocrodil': {'catch': u'45', 'weight': u'25,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Kaiminus', u'Niveau 18', u'Crocrodil', u'Niveau 30', u'Aligatueur'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att.; +1 Def.', 'egg': u'Monstre/Eau 1', 'size': u'1,1m'}})
list.update ({u'Aligatueur': {'catch': u'45', 'weight': u'88,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Kaiminus', u'Niveau 18', u'Crocrodil', u'Niveau 30', u'Aligatueur'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att.; +1 Def.', 'egg': u'Eau 1/Monstre', 'size': u'2,3m'}})
list.update ({u'Fouinette': {'catch': u'255', 'weight': u'6,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Fouinette', u'Niveau 15', u'Fouinar'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol', 'size': u'0,8m'}})
list.update ({u'Fouinar': {'catch': u'90', 'weight': u'32,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Fouinette', u'Niveau 15', u'Fouinar'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'1,8m'}})
list.update ({u'Hoot-hoot': {'catch': u'255', 'weight': u'21,2kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Hoot-hoot', u'Niveau 20', u'Noarfang'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Vol', 'size': u'0,7m'}})
list.update ({u'Noarfang': {'catch': u'90', 'weight': u'40,8kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Hoot-hoot', u'Niveau 20', u'Noarfang'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Vol', 'size': u'1,6m'}})
list.update ({u'Coxy': {'catch': u'255', 'weight': u'10,8kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Coxy', u'Niveau 18', u'Coxyclaque'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Insecte', 'size': u'1,0m'}})
list.update ({u'Coxyclaque': {'catch': u'90', 'weight': u'35,6kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Coxy', u'Niveau 18', u'Coxyclaque'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Insecte', 'size': u'1,4m'}})
list.update ({u'Mimigal': {'catch': u'255', 'weight': u'8,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Mimigal', u'Niveau 22', u'Migalos'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Insecte', 'size': u'0,5m'}})
list.update ({u'Migalos': {'catch': u'90', 'weight': u'33,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Mimigal', u'Niveau 22', u'Migalos'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Insecte', 'size': u'1,1m'}})
list.update ({u'Nostenfer': {'catch': u'90', 'weight': u'75,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Nosferapti', u'Niveau 22', u'Nosferalto', u'Bonheur', u'Nostenfer'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Vit.', 'egg': u'Vol', 'size': u'1,8m'}})
list.update ({u'Loupio': {'catch': u'190', 'weight': u'12,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Loupio', u'Niveau 27', u'Lanturn'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Eau 2', 'size': u'0,5m'}})
list.update ({u'Lanturn': {'catch': u'75', 'weight': u'22,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Loupio', u'Niveau 27', u'Lanturn'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Eau 2', 'size': u'1,2m'}})
list.update ({u'Pichu': {'catch': u'190', 'weight': u'2,0kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Pichu', u'Bonheur', u'Pikachu', u'Avec une Pierre Foudre', u'Raichu'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sans oeuf', 'size': u'0,3m'}})
list.update ({u'Melo': {'catch': u'150', 'weight': u'3,0kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Melo', u'Bonheur', u'Melofee', u'Avec une Pierre Lune', u'Melodelfe'], 'gender': u'75% femelle; 25% male', 'ev': u'+1 Def. Spe', 'egg': u'Sans oeuf', 'size': u'0,3m'}})
list.update ({u'Toudoudou': {'catch': u'45', 'weight': u'1,0kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Toudoudou', u'Bonheur', u'Rondoudou', u'Avec une Pierre Lune', u'Grodoudou'], 'gender': u'-75% femelle; 175% male', 'ev': u'+1 PV', 'egg': u'Sans oeuf', 'size': u'0,3m'}})
list.update ({u'Togepi': {'catch': u'190', 'weight': u'1,5kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Togepi', u'Bonheur', u'Togetic', u'Avec une Pierre Eclat', u'Togekiss'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Def. Spe', 'egg': u'Sans oeuf', 'size': u'0,3m'}})
list.update ({u'Togetic': {'catch': u'75', 'weight': u'3,2kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Togepi', u'Bonheur', u'Togetic', u'Avec une Pierre Eclat', u'Togekiss'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Vit.', 'egg': u'Vol/Fee', 'size': u'0,6m'}})
list.update ({u'Natu': {'catch': u'190', 'weight': u'2,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Natu', u'Niveau 25', u'Xatu'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Vol', 'size': u'0,2m'}})
list.update ({u'Xatu': {'catch': u'75', 'weight': u'15,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Natu', u'Niveau 25', u'Xatu'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe; +1 Vit.', 'egg': u'Vol', 'size': u'1,5m'}})
list.update ({u'Wattouat': {'catch': u'235', 'weight': u'7,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Wattouat', u'Niveau 15', u'Lainergie', u'Niveau 30', u'Pharamp', u'Pharampite', u'Mega-Pharamp'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Sol/Monstre', 'size': u'0,6m'}})
list.update ({u'Lainergie': {'catch': u'120', 'weight': u'13,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Wattouat', u'Niveau 15', u'Lainergie', u'Niveau 30', u'Pharamp', u'Pharampite', u'Mega-Pharamp'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Sol/Monstre', 'size': u'0,8m'}})
list.update ({u'Pharamp': {'catch': u'45', 'weight': u'61,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Wattouat', u'Niveau 15', u'Lainergie', u'Niveau 30', u'Pharamp', u'Pharampite', u'Mega-Pharamp'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Monstre/Sol', 'size': u'1,4m'}})
list.update ({u'Mega-Pharamp': {'catch': u'', 'weight': u'61,5kg', 'hatch': u'', 'evolutions': [u'Wattouat', u'Niveau 15', u'Lainergie', u'Niveau 30', u'Pharamp', u'Pharampite', u'Mega-Pharamp'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'', 'size': u'1,4m'}})
list.update ({u'Joliflor': {'catch': u'45', 'weight': u'5,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Mystherbe', u'Niveau 21', u'Ortide', u'Avec une Pierre Plante', u'Avec une Pierresoleil', u'Rafflesia', u'Joliflor'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Def. Spe', 'egg': u'Plante', 'size': u'0,4m'}})
list.update ({u'Marill': {'catch': u'190', 'weight': u'8,5kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Azurill', u'Bonheur', u'Marill', u'Niveau 18', u'Azumarill'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Eau 1/Fee', 'size': u'0,4m'}})
list.update ({u'Azumarill': {'catch': u'75', 'weight': u'28,5kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Azurill', u'Bonheur', u'Marill', u'Niveau 18', u'Azumarill'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 PV', 'egg': u'Eau 1/Fee', 'size': u'0,8m'}})
list.update ({u'Simularbre': {'catch': u'65', 'weight': u'61,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Manzai', u"En apprenant l'attaque Copie", u'Simularbre'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Mineral', 'size': u'1,4m'}})
list.update ({u'Tarpaud': {'catch': u'45', 'weight': u'33,9kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ptitard', u'Niveau 25', u'Tetarte', u'Avec une Pierre Eau', u'Echange en tenant Roche Royale', u'Tartard', u'Tarpaud'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Eau 1', 'size': u'1,1m'}})
list.update ({u'Granivol': {'catch': u'255', 'weight': u'0,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Granivol', u'Niveau 18', u'Floravol', u'Niveau 27', u'Cotovol'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Fee/Plante', 'size': u'0,4m'}})
list.update ({u'Floravol': {'catch': u'120', 'weight': u'1,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Granivol', u'Niveau 18', u'Floravol', u'Niveau 27', u'Cotovol'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Fee/Plante', 'size': u'0,6m'}})
list.update ({u'Cotovol': {'catch': u'45', 'weight': u'3,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Granivol', u'Niveau 18', u'Floravol', u'Niveau 27', u'Cotovol'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Vit.', 'egg': u'Fee/Plante', 'size': u'0,8m'}})
list.update ({u'Capumain': {'catch': u'45', 'weight': u'11,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Capumain', u"En connaissant l'attaque Coup Double", u'Capidextre'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,8m'}})
list.update ({u'Tournegrin': {'catch': u'235', 'weight': u'1,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tournegrin', u'Avec une Pierresoleil', u'Heliatronc'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Plante', 'size': u'0,3m'}})
list.update ({u'Heliatronc': {'catch': u'120', 'weight': u'8,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tournegrin', u'Avec une Pierresoleil', u'Heliatronc'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Plante', 'size': u'0,8m'}})
list.update ({u'Yanma': {'catch': u'75', 'weight': u'38,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Yanma', u"En apprenant l' attaque  Pouv.Antique", u'Yanmega'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Insecte', 'size': u'1,2m'}})
list.update ({u'Axoloto': {'catch': u'255', 'weight': u'8,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Axoloto', u'Niveau 20', u'Maraiste'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Eau 1/Sol', 'size': u'0,4m'}})
list.update ({u'Maraiste': {'catch': u'90', 'weight': u'75,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Axoloto', u'Niveau 20', u'Maraiste'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Eau 1/Sol', 'size': u'1,4m'}})
list.update ({u'Mentali': {'catch': u'45', 'weight': u'26,5kg', 'hatch': u'34 cycles - 8960 pas', 'evolutions': [u'Evoli', u'Avec une Pierre Eau', u'Avec une Pierre Foudre', u'Avec une Pierre Feu', u'Bonheur , Jour', u'Bonheur , Nuit', u"Pres d'une Pierre Mousse + gagne un niveau", u"Pres d'une Pierre Glacee + gagne un niveau", u"2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att. Spe', 'egg': u'Sol', 'size': u'0,9m'}})
list.update ({u'Noctali': {'catch': u'45', 'weight': u'27,0kg', 'hatch': u'34 cycles - 8960 pas', 'evolutions': [u'Evoli', u'Avec une Pierre Eau', u'Avec une Pierre Foudre', u'Avec une Pierre Feu', u'Bonheur , Jour', u'Bonheur , Nuit', u"Pres d'une Pierre Mousse + gagne un niveau", u"Pres d'une Pierre Glacee + gagne un niveau", u"2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Def. Spe.', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Cornebre': {'catch': u'30', 'weight': u'2,1kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Cornebre', u'Avec une Pierre Nuit', u'Corboss'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Vol', 'size': u'0,5m'}})
list.update ({u'Roigada': {'catch': u'70', 'weight': u'79,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ramoloss', u'Niveau 37', u'Echange en tenant Roche Royale', u'Flagadoss', u'Roigada'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Def. Spe', 'egg': u'Monstre/Eau 1', 'size': u'2,0m'}})
list.update ({u'Feuforeve': {'catch': u'45', 'weight': u'1,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Feuforeve', u'Avec une Pierre Nuit', u'Magireve'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe; +1 Def. Spe', 'egg': u'Indetermine', 'size': u'0,7m'}})
list.update ({u'Zarbi': {'catch': u'225', 'weight': u'5,0kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att.; +1 Att. Spe', 'egg': u'Sans oeuf', 'size': u'0,5m'}})
list.update ({u'Qulbutoke': {'catch': u'45', 'weight': u'28,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Okeoke', u'Niveau 15', u'Qulbutoke'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Indetermine', 'size': u'1,3m'}})
list.update ({u'Girafarig': {'catch': u'60', 'weight': u'41,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Sol', 'size': u'1,5m'}})
list.update ({u'Pomdepik': {'catch': u'190', 'weight': u'7,2kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Pomdepik', u'Niveau 31', u'Foretress'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Insecte', 'size': u'0,6m'}})
list.update ({u'Foretress': {'catch': u'75', 'weight': u'125,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Pomdepik', u'Niveau 31', u'Foretress'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Insecte', 'size': u'1,2m'}})
list.update ({u'Insolourdo': {'catch': u'190', 'weight': u'14,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Sol', 'size': u'1,5m'}})
list.update ({u'Scorplane': {'catch': u'60', 'weight': u'64,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Scorplane', u'Gagne un niveau de nuit en tenant un Croc Rasoir', u'Scorvol'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Insecte', 'size': u'1,1m'}})
list.update ({u'Steelix': {'catch': u'25', 'weight': u'400,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Onix', u'Echange en tenant Peau Metal', u'Steelix'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Mineral', 'size': u'9,2m'}})
list.update ({u'Snubbull': {'catch': u'190', 'weight': u'7,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Snubbull', u'Niveau 23', u'Granbull'], 'gender': u'75% femelle; 25% male', 'ev': u'+1 Att.', 'egg': u'Sol/Fee', 'size': u'0,6m'}})
list.update ({u'Granbull': {'catch': u'75', 'weight': u'48,7kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Snubbull', u'Niveau 23', u'Granbull'], 'gender': u'75% femelle; 25% male', 'ev': u'+2 Att.', 'egg': u'Sol/Fee', 'size': u'1,4m'}})
list.update ({u'Qwilfish': {'catch': u'45', 'weight': u'3,9kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Eau 2', 'size': u'0,5m'}})
list.update ({u'Cizayox': {'catch': u'25', 'weight': u'118,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Insecateur', u'Echange en tenant Peau Metal', u'Cizayox', u'Mega-Evolution', u'Mega-Cizayox'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Insecte', 'size': u'1,8m'}})
list.update ({u'Mega-Cizayox': {'catch': u'', 'weight': u'125kg', 'hatch': u'', 'evolutions': [u'Insecateur', u'Echange en tenant Peau Metal', u'Cizayox', u'Cizayoxite', u'Mega-Cizayox'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'', 'size': u'2m'}})
list.update ({u'Caratroc': {'catch': u'190', 'weight': u'20,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.; +1 Def. Spe', 'egg': u'Insecte', 'size': u'0,6m'}})
list.update ({u'Scarhino': {'catch': u'45', 'weight': u'54,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Scarhino', u'Scarhinoite', u'Mega-Scarhino'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Insecte', 'size': u'1,5m'}})
list.update ({u'Mega-Scarhino': {'catch': u'', 'weight': u'62,5kg', 'hatch': u'', 'evolutions': [u'Scarhino', u'Scarhinoite', u'Mega-Scarhino'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'', 'size': u'1,7m'}})
list.update ({u'Farfuret': {'catch': u'60', 'weight': u'28,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Farfuret', u'Gagne un niveau de nuit en tenant une Griffe Rasoir', u'Dimoret'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,9m'}})
list.update ({u'Teddiursa': {'catch': u'120', 'weight': u'8,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Teddiursa', u'Niveau 30', u'Ursaring'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol', 'size': u'0,6m'}})
list.update ({u'Ursaring': {'catch': u'60', 'weight': u'125,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Teddiursa', u'Niveau 30', u'Ursaring'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Sol', 'size': u'1,8m'}})
list.update ({u'Limagma': {'catch': u'190', 'weight': u'35,0kg', 'hatch': u'21 cycles - 5610 pas', 'evolutions': [u'Limagma', u'Niveau 38', u'Volcaropod'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Indetermine', 'size': u'0,7m'}})
list.update ({u'Volcaropod': {'catch': u'75', 'weight': u'55,0kg', 'hatch': u'21 cycles - 5610 pas', 'evolutions': [u'Limagma', u'Niveau 38', u'Volcaropod'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Indetermine', 'size': u'0,8m'}})
list.update ({u'Marcacrin': {'catch': u'225', 'weight': u'6,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Marcacrin', u'Niveau 33', u'Cochignon', u"En connaissant l'attaque Pouv.Antique", u'Mammochon'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol', 'size': u'0,4m'}})
list.update ({u'Cochignon': {'catch': u'75', 'weight': u'55,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Marcacrin', u'Niveau 33', u'Cochignon', u"En connaissant l'attaque Pouv.Antique", u'Mammochon'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV; +1 Att.', 'egg': u'Sol', 'size': u'1,1m'}})
list.update ({u'Corayon': {'catch': u'45', 'weight': u'5,0kg', 'hatch': u'20 cycles - 5376 pas', 'evolutions': [], 'gender': u'75% femelle; 25% male', 'ev': u'+1 Def.; +1 Def. Spe', 'egg': u'Eau 1/Eau 3', 'size': u'0,6m'}})
list.update ({u'Remoraid': {'catch': u'190', 'weight': u'12,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Remoraid', u'Niveau 25', u'Octillery'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Eau 1/Eau 2', 'size': u'0,6m'}})
list.update ({u'Octillery': {'catch': u'75', 'weight': u'28,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Remoraid', u'Niveau 25', u'Octillery'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.; +1 Att. Spe', 'egg': u'Eau 1/Eau 2', 'size': u'0,9m'}})
list.update ({u'Cadoizo': {'catch': u'45', 'weight': u'16,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Eau 1/Sol', 'size': u'0,9m'}})
list.update ({u'Demanta': {'catch': u'25', 'weight': u'220,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Babimanta', u"Gain de niveau avec Remoraid dans l'equipe", u'Demanta'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def. Spe', 'egg': u'Eau 1', 'size': u'2,1m'}})
list.update ({u'Airmure': {'catch': u'25', 'weight': u'50,5kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Vol', 'size': u'1,7m'}})
list.update ({u'Malosse': {'catch': u'120', 'weight': u'10,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Malosse', u'Niveau 24', u'Demolosse', u'Demolossite', u'Mega-Demolosse'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Sol', 'size': u'0,6m'}})
list.update ({u'Demolosse': {'catch': u'4', 'weight': u'35,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Malosse', u'Niveau 24', u'Demolosse', u'Demolossite', u'Mega-Demolosse'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Sol', 'size': u'1,4m'}})
list.update ({u'Mega-Demolosse': {'catch': u'', 'weight': u'35kg', 'hatch': u'', 'evolutions': [u'Malosse', u'Niveau 24', u'Demolosse', u'Demolossite', u'Mega-Demolosse'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'', 'size': u'1,4m'}})
list.update ({u'Hyporoi': {'catch': u'45', 'weight': u'152,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Hypotrempe', u'Niveau 32', u'Hypocean', u"Echange en tenant l'objet Ecaille Draco", u'Hyporoi'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.; +1 Att. Spe; +1 Def. Spe', 'egg': u'Eau 1/Dragon', 'size': u'1,8m'}})
list.update ({u'Phanpy': {'catch': u'120', 'weight': u'33,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Phanpy', u'Niveau 25', u'Donphan'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Sol', 'size': u'0,5m'}})
list.update ({u'Donphan': {'catch': u'60', 'weight': u'120,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Phanpy', u'Niveau 25', u'Donphan'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.; +1 Def.', 'egg': u'Sol', 'size': u'1,1m'}})
list.update ({u'Porygon2': {'catch': u'45', 'weight': u'32,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Porygon', u'Echange en tenant Ameliorator', u'Porygon2', u'Echange en tenant CD Douteux', u'Porygon-Z'], 'gender': u'Asexue', 'ev': u'+2 Att. Spe', 'egg': u'Mineral', 'size': u'0,6m'}})
list.update ({u'Cerfrousse': {'catch': u'45', 'weight': u'71,2kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol', 'size': u'1,4m'}})
list.update ({u'Queulorior': {'catch': u'45', 'weight': u'58,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'1,2m'}})
list.update ({u'Debugant': {'catch': u'75', 'weight': u'21,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Debugant', u'Niveau 20, Attaque Defense', u'Niveau 20, Attaque Defense', u'Niveau 20, Attaque et Defense identiques', u'Kicklee', u'Tygnon', u'Kapoera'], 'gender': u'0% femelle; 100% male', 'ev': u'+2 Att.', 'egg': u'Sans oeuf', 'size': u'0,7m'}})
list.update ({u'Kapoera': {'catch': u'45', 'weight': u'48,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Debugant', u'Niveau 20, Attaque Defense', u'Niveau 20, Attaque Defense', u'Niveau 20, Attaque et Defense identiques', u'Kicklee', u'Tygnon', u'Kapoera'], 'gender': u'0% femelle; 100% male', 'ev': u'+2 Def. Spe', 'egg': u'Humanoide', 'size': u'1,4m'}})
list.update ({u'Lippouti': {'catch': u'45', 'weight': u'6,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Lippouti', u'Niveau 30', u'Lippoutou'], 'gender': u'100% femelle; 0% male', 'ev': u'+1 Att. Spe', 'egg': u'Sans oeuf', 'size': u'0,6m'}})
list.update ({u'Elekid': {'catch': u'45', 'weight': u'23,5kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Elekid', u'Niveau 30', u'Elektek', u'Echange en tenant Electiriseur', u'Elekable'], 'gender': u'25% femelle; 75% male', 'ev': u'+1 Vit.', 'egg': u'Sans oeuf', 'size': u'0,6m'}})
list.update ({u'Magby': {'catch': u'45', 'weight': u'21,4kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Magby', u'Niveau 30', u'Magmar', u'Echange en tenant Magmariseur', u'Maganon'], 'gender': u'25% femelle; 75% male', 'ev': u'+1 Vit.', 'egg': u'Sans oeuf', 'size': u'0,7m'}})
list.update ({u'Ecremeuh': {'catch': u'45', 'weight': u'75,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'100% femelle; 0% male', 'ev': u'+2 Def.', 'egg': u'Sol', 'size': u'1,2m'}})
list.update ({u'Leuphorie': {'catch': u'30', 'weight': u'46,8kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Ptiravi', u'Gain de niveau en tenant une Pierre Ovale', u'Leveinard', u'Bonheur', u'Leuphorie'], 'gender': u'100% femelle; 0% male', 'ev': u'+3 PV', 'egg': u'Fee', 'size': u'1,5m'}})
list.update ({u'Raikou': {'catch': u'3', 'weight': u'178,0kg', 'hatch': u'79 cycles - 20480 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att. Spe; +2 Vit.', 'egg': u'Sans oeuf', 'size': u'1,9m'}})
list.update ({u'Entei': {'catch': u'3', 'weight': u'198,0kg', 'hatch': u'79 cycles - 20480 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 PV; +2 Att.', 'egg': u'Sans oeuf', 'size': u'2,1m'}})
list.update ({u'Suicune': {'catch': u'3', 'weight': u'187,0kg', 'hatch': u'79 cycles - 20480 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Def.; +2 Def. Spe', 'egg': u'Sans oeuf', 'size': u'2,0m'}})
list.update ({u'Embrylex': {'catch': u'45', 'weight': u'72,0kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Embrylex', u'Niveau 30', u'Ymphect', u'Niveau 55', u'Tyranocif', u'Tyranocivite', u'Mega-Tyranocif'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Monstre', 'size': u'0,6m'}})
list.update ({u'Ymphect': {'catch': u'45', 'weight': u'152,0kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Embrylex', u'Niveau 30', u'Ymphect', u'Niveau 55', u'Tyranocif', u'Tyranocivite', u'Mega-Tyranocif'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Monstre', 'size': u'1,2m'}})
list.update ({u'Tyranocif': {'catch': u'45', 'weight': u'202,0kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Embrylex', u'Niveau 30', u'Ymphect', u'Niveau 55', u'Tyranocif', u'Tyranocivite', u'Mega-Tyranocif'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att.', 'egg': u'Monstre', 'size': u'2,0m'}})
list.update ({u'Mega-Tyranocif': {'catch': u'', 'weight': u'255,0kg', 'hatch': u'', 'evolutions': [u'Embrylex', u'Niveau 30', u'Ymphect', u'Niveau 55', u'Tyranocif', u'Tyranocivite', u'Mega-Tyranocif'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'', 'size': u'2,5m'}})
list.update ({u'Lugia': {'catch': u'3', 'weight': u'216,0kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Def. Spe', 'egg': u'Sans oeuf', 'size': u'5,2m'}})
list.update ({u'Ho-Oh': {'catch': u'3', 'weight': u'199,0kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Def. Spe', 'egg': u'Sans oeuf', 'size': u'3,8m'}})
list.update ({u'Celebi': {'catch': u'45', 'weight': u'5,0kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 PV', 'egg': u'Sans oeuf', 'size': u'0,6m'}})
list.update ({u'Arcko': {'catch': u'45', 'weight': u'5,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Arcko', u'Niveau 16', u'Massko', u'Niveau 36', u'Jungko'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Vit.', 'egg': u'Monstre/Dragon', 'size': u'0,5m'}})
list.update ({u'Massko': {'catch': u'45', 'weight': u'21,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Arcko', u'Niveau 16', u'Massko', u'Niveau 36', u'Jungko'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Vit.', 'egg': u'Monstre/Dragon', 'size': u'0,9m'}})
list.update ({u'Jungko': {'catch': u'45', 'weight': u'52,2kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Arcko', u'Niveau 16', u'Massko', u'Niveau 36', u'Jungko'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+3 Vit.', 'egg': u'Monstre/Dragon', 'size': u'1,7m'}})
list.update ({u'Poussifeu': {'catch': u'45', 'weight': u'2,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Poussifeu', u'Niveau 16', u'Galifeu', u'Niveau 36', u'Brasegali', u'Brasegalite', u'Mega-Brasegali'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att. Spe', 'egg': u'Sol', 'size': u'0,4m'}})
list.update ({u'Galifeu': {'catch': u'45', 'weight': u'19,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Poussifeu', u'Niveau 16', u'Galifeu', u'Niveau 36', u'Brasegali', u'Brasegalite', u'Mega-Brasegali'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att.; +1 Att. Spe', 'egg': u'Sol', 'size': u'0,9m'}})
list.update ({u'Brasegali': {'catch': u'45', 'weight': u'52,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Poussifeu', u'Niveau 16', u'Galifeu', u'Niveau 36', u'Brasegali', u'Brasegalite', u'Mega-Brasegali'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+3 Att.', 'egg': u'Sol', 'size': u'1,9m'}})
list.update ({u'Mega-Brasegali': {'catch': u'', 'weight': u'52kg', 'hatch': u'', 'evolutions': [u'Poussifeu', u'Niveau 16', u'Galifeu', u'Niveau 36', u'Brasegali', u'Brasegalite', u'Mega-Brasegali'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'', 'egg': u'', 'size': u'1,9m'}})
list.update ({u'Gobou': {'catch': u'45', 'weight': u'7,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Gobou', u'Niveau 16', u'Flobio', u'Niveau 36', u'Laggron'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att.', 'egg': u'Monstre/Eau 1', 'size': u'0,4m'}})
list.update ({u'Flobio': {'catch': u'45', 'weight': u'28,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Gobou', u'Niveau 16', u'Flobio', u'Niveau 36', u'Laggron'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att.', 'egg': u'Monstre/Eau 1', 'size': u'0,7m'}})
list.update ({u'Laggron': {'catch': u'45', 'weight': u'81,9kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Gobou', u'Niveau 16', u'Flobio', u'Niveau 36', u'Laggron'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+3 Att.', 'egg': u'Monstre/Eau 1', 'size': u'1,6m'}})
list.update ({u'Medhyena': {'catch': u'255', 'weight': u'13,6kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Medhyena', u'Niveau 18', u'Grahyena'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol', 'size': u'0,5m'}})
list.update ({u'Grahyena': {'catch': u'127', 'weight': u'37,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Medhyena', u'Niveau 18', u'Grahyena'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Zigzaton': {'catch': u'255', 'weight': u'17,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Zigzaton', u'Niveau 20', u'Lineon'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,4m'}})
list.update ({u'Lineon': {'catch': u'90', 'weight': u'32,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Zigzaton', u'Niveau 20', u'Lineon'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'0,5m'}})
list.update ({u'Chenipotte': {'catch': u'255', 'weight': u'3,6kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Chenipotte', u'Niveau 7, au hasard', u'Niveau 7, au hasard', u'Armulys', u'Blindalys', u'Niveau 10', u'Niveau 10', u'Charmillon', u'Papinox'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Insecte', 'size': u'0,3m'}})
list.update ({u'Armulys': {'catch': u'120', 'weight': u'10,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Chenipotte', u'Niveau 7, au hasard', u'Niveau 7, au hasard', u'Armulys', u'Blindalys', u'Niveau 10', u'Niveau 10', u'Charmillon', u'Papinox'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Insecte', 'size': u'0,6m'}})
list.update ({u'Charmillon': {'catch': u'45', 'weight': u'28,4kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Chenipotte', u'Niveau 7, au hasard', u'Niveau 7, au hasard', u'Armulys', u'Blindalys', u'Niveau 10', u'Niveau 10', u'Charmillon', u'Papinox'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att. Spe', 'egg': u'Insecte', 'size': u'1,0m'}})
list.update ({u'Blindalys': {'catch': u'120', 'weight': u'11,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Chenipotte', u'Niveau 7, au hasard', u'Niveau 7, au hasard', u'Armulys', u'Blindalys', u'Niveau 10', u'Niveau 10', u'Charmillon', u'Papinox'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Insecte', 'size': u'0,7m'}})
list.update ({u'Papinox': {'catch': u'45', 'weight': u'31,6kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Chenipotte', u'Niveau 7, au hasard', u'Niveau 7, au hasard', u'Armulys', u'Blindalys', u'Niveau 10', u'Niveau 10', u'Charmillon', u'Papinox'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Def. Spe', 'egg': u'Insecte', 'size': u'1,2m'}})
list.update ({u'Nenupiot': {'catch': u'255', 'weight': u'2,6kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Nenupiot', u'Niveau 14', u'Lombre', u'Avec une Pierre Eau', u'Ludicolo'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Eau 1/Plante', 'size': u'0,5m'}})
list.update ({u'Lombre': {'catch': u'120', 'weight': u'32,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Nenupiot', u'Niveau 14', u'Lombre', u'Avec une Pierre Eau', u'Ludicolo'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def. Spe', 'egg': u'Eau 1/Plante', 'size': u'1,2m'}})
list.update ({u'Ludicolo': {'catch': u'45', 'weight': u'55,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Nenupiot', u'Niveau 14', u'Lombre', u'Avec une Pierre Eau', u'Ludicolo'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Def. Spe', 'egg': u'Eau 1/Plante', 'size': u'1,5m'}})
list.update ({u'Grainipiot': {'catch': u'255', 'weight': u'4,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Grainipiot', u'Niveau 14', u'Pifeuil', u'Avec une Pierre Plante', u'Tengalice'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Sol/Plante', 'size': u'0,5m'}})
list.update ({u'Pifeuil': {'catch': u'120', 'weight': u'28,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Grainipiot', u'Niveau 14', u'Pifeuil', u'Avec une Pierre Plante', u'Tengalice'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Sol/Plante', 'size': u'1,0m'}})
list.update ({u'Tengalice': {'catch': u'45', 'weight': u'59,6kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Grainipiot', u'Niveau 14', u'Pifeuil', u'Avec une Pierre Plante', u'Tengalice'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att.', 'egg': u'Sol/Plante', 'size': u'1,3m'}})
list.update ({u'Nirondelle': {'catch': u'200', 'weight': u'2,3kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Nirondelle', u'Niveau 22', u'Heledelle'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Vol', 'size': u'0,3m'}})
list.update ({u'Heledelle': {'catch': u'45', 'weight': u'19,8kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Nirondelle', u'Niveau 22', u'Heledelle'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Vol', 'size': u'0,7m'}})
list.update ({u'Goelise': {'catch': u'190', 'weight': u'9,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Goelise', u'Niveau 25', u'Bekipan'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Eau 1/Vol', 'size': u'0,6m'}})
list.update ({u'Bekipan': {'catch': u'45', 'weight': u'28,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Goelise', u'Niveau 25', u'Bekipan'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Eau 1/Vol', 'size': u'1,2m'}})
list.update ({u'Tarsal': {'catch': u'235', 'weight': u'6,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tarsal', u'Niveau 20', u'Kirlia', u'Niveau 30', u'Male + Pierre Aube', u'Gardevoir', u'Gallame', u'Gardevoirite', u'Mega-Gardevoir'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Indetermine', 'size': u'0,4m'}})
list.update ({u'Kirlia': {'catch': u'120', 'weight': u'20,2kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tarsal', u'Niveau 20', u'Kirlia', u'Niveau 30', u'Male + Pierre Aube', u'Gardevoir', u'Gallame', u'Gardevoirite', u'Mega-Gardevoir'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Indetermine', 'size': u'0,8m'}})
list.update ({u'Gardevoir': {'catch': u'45', 'weight': u'48,4kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tarsal', u'Niveau 20', u'Kirlia', u'Niveau 30', u'Male + Pierre Aube', u'Gardevoir', u'Gallame', u'Gardevoirite', u'Mega-Gardevoir'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att. Spe', 'egg': u'Indetermine', 'size': u'1,6m'}})
list.update ({u'Mega-Gardevoir': {'catch': u'', 'weight': u'48,4kg', 'hatch': u'', 'evolutions': [u'Tarsal', u'Niveau 20', u'Kirlia', u'Niveau 30', u'Male + Pierre Aube', u'Gardevoir', u'Gallame', u'Gardevoirite', u'Mega-Gardevoir'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'', 'size': u'1,6m'}})
list.update ({u'Arakdo': {'catch': u'200', 'weight': u'1,7kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Arakdo', u'Niveau 22', u'Maskadra'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Eau 1/Insecte', 'size': u'0,5m'}})
list.update ({u'Maskadra': {'catch': u'75', 'weight': u'3,6kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Arakdo', u'Niveau 22', u'Maskadra'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe; +1 Def. Spe', 'egg': u'Eau 1/Insecte', 'size': u'0,8m'}})
list.update ({u'Balignon': {'catch': u'255', 'weight': u'4,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Balignon', u'Niveau 23', u'Chapignon'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Fee/Plante', 'size': u'0,4m'}})
list.update ({u'Chapignon': {'catch': u'90', 'weight': u'39,2kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Balignon', u'Niveau 23', u'Chapignon'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Fee/Plante', 'size': u'1,2m'}})
list.update ({u'Parecool': {'catch': u'255', 'weight': u'24,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Parecool', u'Niveau 18', u'Vigoroth', u'Niveau 36', u'Monaflemit'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Sol', 'size': u'0,8m'}})
list.update ({u'Vigoroth': {'catch': u'120', 'weight': u'46,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Parecool', u'Niveau 18', u'Vigoroth', u'Niveau 36', u'Monaflemit'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'1,4m'}})
list.update ({u'Monaflemit': {'catch': u'45', 'weight': u'130,5kg', 'hatch': u'15 cycles - 4095 pas', 'evolutions': [u'Parecool', u'Niveau 18', u'Vigoroth', u'Niveau 36', u'Monaflemit'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 PV', 'egg': u'Sol', 'size': u'2,0m'}})
list.update ({u'Ningale': {'catch': u'255', 'weight': u'5,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Ningale', u'Niveau 20', u"Niveau 20, emplacement libre et Poke Ball dans l'inventaire", u'Ninjask', u'Munja'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Insecte', 'size': u'0,5m'}})
list.update ({u'Ninjask': {'catch': u'120', 'weight': u'12,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Ningale', u'Niveau 20', u"Niveau 20, emplacement libre et Poke Ball dans l'inventaire", u'Ninjask', u'Munja'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Insecte', 'size': u'0,8m'}})
list.update ({u'Munja': {'catch': u'45', 'weight': u'1,2kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Ningale', u'Niveau 20', u"Niveau 20, emplacement libre et Poke Ball dans l'inventaire", u'Ninjask', u'Munja'], 'gender': u'Asexue', 'ev': u'+2 PV', 'egg': u'Mineral', 'size': u'0,8m'}})
list.update ({u'Chuchmur': {'catch': u'190', 'weight': u'16,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Chuchmur', u'Niveau 20', u'Ramboum', u'Niveau 40', u'Brouhabam'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Monstre/Sol', 'size': u'0,6m'}})
list.update ({u'Ramboum': {'catch': u'120', 'weight': u'40,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Chuchmur', u'Niveau 20', u'Ramboum', u'Niveau 40', u'Brouhabam'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Monstre/Sol', 'size': u'1,0m'}})
list.update ({u'Brouhabam': {'catch': u'45', 'weight': u'84,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Chuchmur', u'Niveau 20', u'Ramboum', u'Niveau 40', u'Brouhabam'], 'gender': u'45% femelle; 55% male', 'ev': u'+3 PV', 'egg': u'Monstre/Sol', 'size': u'1,5m'}})
list.update ({u'Makuhita': {'catch': u'180', 'weight': u'86,4kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Makuhita', u'Niveau 24', u'Hariyama'], 'gender': u'25% femelle; 75% male', 'ev': u'+1 PV', 'egg': u'Humanoide', 'size': u'1,0m'}})
list.update ({u'Hariyama': {'catch': u'200', 'weight': u'253,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Makuhita', u'Niveau 24', u'Hariyama'], 'gender': u'25% femelle; 75% male', 'ev': u'+2 PV', 'egg': u'Humanoide', 'size': u'2,3m'}})
list.update ({u'Azurill': {'catch': u'60', 'weight': u'2,0kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Azurill', u'Bonheur', u'Marill', u'Niveau 18', u'Azumarill'], 'gender': u'75% femelle; 25% male', 'ev': u'+1 PV', 'egg': u'Sans oeuf', 'size': u'0,2m'}})
list.update ({u'Tarinor': {'catch': u'255', 'weight': u'97,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tarinor', u'Gain de niveau dans un lieu indique', u'Tarinorme'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Mineral', 'size': u'1,0m'}})
list.update ({u'Skitty': {'catch': u'255', 'weight': u'11,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Skitty', u'Avec une Pierre Lune', u'Delcatty'], 'gender': u'75% femelle; 25% male', 'ev': u'+1 Vit.', 'egg': u'Sol/Fee', 'size': u'0,6m'}})
list.update ({u'Delcatty': {'catch': u'60', 'weight': u'32,6kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Skitty', u'Avec une Pierre Lune', u'Delcatty'], 'gender': u'75% femelle; 25% male', 'ev': u'+1 PV; +1 Vit.', 'egg': u'Sol/Fee', 'size': u'1,1m'}})
list.update ({u'Tenefix': {'catch': u'45', 'weight': u'11,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.; +1 Def.', 'egg': u'Humanoide', 'size': u'0,5m'}})
list.update ({u'Mysdibule': {'catch': u'45', 'weight': u'11,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Mysdibule', u'Mysdibulite', u'Mega-Mysdibule'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.; +1 Def.', 'egg': u'Sol/Fee', 'size': u'0,6m'}})
list.update ({u'Mega-Mysdibule': {'catch': u'', 'weight': u'23,5kg', 'hatch': u'', 'evolutions': [u'Mysdibule', u'Mysdibulite', u'Mega-Mysdibule'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'', 'size': u'1,0m'}})
list.update ({u'Galekid': {'catch': u'180', 'weight': u'60,0kg', 'hatch': u'34 cycles - 8960 pas', 'evolutions': [u'Galekid', u'Niveau 32', u'Galegon', u'Niveau 42', u'Galeking', u'Galekingite', u'Mega-Galeking'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Monstre', 'size': u'0,4m'}})
list.update ({u'Galegon': {'catch': u'90', 'weight': u'120,0kg', 'hatch': u'34 cycles - 8960 pas', 'evolutions': [u'Galekid', u'Niveau 32', u'Galegon', u'Niveau 42', u'Galeking', u'Galekingite', u'Mega-Galeking'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Monstre', 'size': u'0,9m'}})
list.update ({u'Galeking': {'catch': u'45', 'weight': u'360,0kg', 'hatch': u'34 cycles - 8960 pas', 'evolutions': [u'Galekid', u'Niveau 32', u'Galegon', u'Niveau 42', u'Galeking', u'Galekingite', u'Mega-Galeking'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Def.', 'egg': u'Monstre', 'size': u'2,1m'}})
list.update ({u'Mega-Galeking': {'catch': u'', 'weight': u'395kg', 'hatch': u'', 'evolutions': [u'Galekid', u'Niveau 32', u'Galegon', u'Niveau 42', u'Galeking', u'Galekingite', u'Mega-Galeking'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'', 'size': u'2,2m'}})
list.update ({u'Meditikka': {'catch': u'180', 'weight': u'11,2kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Meditikka', u'Niveau 37', u'Charmina', u'Charminite', u'Mega-Charmina'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Humanoide', 'size': u'0,6m'}})
list.update ({u'Charmina': {'catch': u'90', 'weight': u'31,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Meditikka', u'Niveau 37', u'Charmina', u'Charminite', u'Mega-Charmina'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Humanoide', 'size': u'1,3m'}})
list.update ({u'Mega-Charmina': {'catch': u'', 'weight': u'31,5kg', 'hatch': u'', 'evolutions': [u'Meditikka', u'Niveau 37', u'Charmina', u'Charminite', u'Mega-Charmina'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'', 'size': u'1,3m'}})
list.update ({u'Dynavolt': {'catch': u'120', 'weight': u'15,2kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Dynavolt', u'Niveau 26', u'Elecsprint', u'Mega-Evolution', u'Mega-Elecsprint'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,6m'}})
list.update ({u'Elecsprint': {'catch': u'45', 'weight': u'40,2kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Dynavolt', u'Niveau 26', u'Elecsprint', u'Mega-Evolution', u'Mega-Elecsprint'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'1,5m'}})
list.update ({u'Mega-Elecsprint': {'catch': u'', 'weight': u'44kg', 'hatch': u'', 'evolutions': [u'Dynavolt', u'Niveau 26', u'Elecsprint', u'Elecsprintite', u'Mega-Elecsprint'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'', 'size': u'1,8m'}})
list.update ({u'Posipi': {'catch': u'200', 'weight': u'4,2kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Fee', 'size': u'0,4m'}})
list.update ({u'Negapi': {'catch': u'200', 'weight': u'4,2kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Fee', 'size': u'0,4m'}})
list.update ({u'Muciole': {'catch': u'150', 'weight': u'17,7kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [], 'gender': u'0% femelle; 100% male', 'ev': u'+1 Vit.', 'egg': u'Insecte/Humanoide', 'size': u'0,7m'}})
list.update ({u'Lumivole': {'catch': u'150', 'weight': u'17,7kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [], 'gender': u'100% femelle; 0% male', 'ev': u'+1 Vit.', 'egg': u'Insecte/Humanoide', 'size': u'0,6m'}})
list.update ({u'Roselia': {'catch': u'150', 'weight': u'2,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Rozbouton', u'Bonheur , Jour', u'Roselia', u'Avec une Pierre Eclat', u'Roserade'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Fee/Plante', 'size': u'0,3m'}})
list.update ({u'Gloupti': {'catch': u'225', 'weight': u'10,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Gloupti', u'Niveau 26', u'Avaltout'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Indetermine', 'size': u'0,4m'}})
list.update ({u'Avaltout': {'catch': u'75', 'weight': u'80,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Gloupti', u'Niveau 26', u'Avaltout'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Indetermine', 'size': u'1,7m'}})
list.update ({u'Carvanha': {'catch': u'225', 'weight': u'20,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Carvanha', u'Niveau 30', u'Sharpedo'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Eau 2', 'size': u'0,8m'}})
list.update ({u'Sharpedo': {'catch': u'60', 'weight': u'88,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Carvanha', u'Niveau 30', u'Sharpedo'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Eau 2', 'size': u'1,8m'}})
list.update ({u'Wailmer': {'catch': u'125', 'weight': u'130,0kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Wailmer', u'Niveau 40', u'Wailord'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Sol/Eau 2', 'size': u'2,0m'}})
list.update ({u'Wailord': {'catch': u'60', 'weight': u'398,0kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Wailmer', u'Niveau 40', u'Wailord'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Sol/Eau 2', 'size': u'14,5m'}})
list.update ({u'Chamallot': {'catch': u'255', 'weight': u'24,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Chamallot', u'Niveau 33', u'Camerupt'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Sol', 'size': u'0,7m'}})
list.update ({u'Camerupt': {'catch': u'150', 'weight': u'220,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Chamallot', u'Niveau 33', u'Camerupt'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.; +1 Att. Spe', 'egg': u'Sol', 'size': u'1,9m'}})
list.update ({u'Chartor': {'catch': u'90', 'weight': u'80,4kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Sol', 'size': u'0,5m'}})
list.update ({u'Spoink': {'catch': u'255', 'weight': u'30,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Spoink', u'Niveau 32', u'Groret'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Sol', 'size': u'0,7m'}})
list.update ({u'Groret': {'catch': u'60', 'weight': u'71,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Spoink', u'Niveau 32', u'Groret'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def. Spe', 'egg': u'Sol', 'size': u'0,9m'}})
list.update ({u'Spinda': {'catch': u'255', 'weight': u'5,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Sol/Humanoide', 'size': u'1,1m'}})
list.update ({u'Kraknoix': {'catch': u'255', 'weight': u'15,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Kraknoix', u'Niveau 35', u'Vibraninf', u'Niveau 45', u'Libegon'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Insecte', 'size': u'0,7m'}})
list.update ({u'Vibraninf': {'catch': u'120', 'weight': u'15,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Kraknoix', u'Niveau 35', u'Vibraninf', u'Niveau 45', u'Libegon'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.; +1 Vit.', 'egg': u'Insecte', 'size': u'1,1m'}})
list.update ({u'Libegon': {'catch': u'45', 'weight': u'82,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Kraknoix', u'Niveau 35', u'Vibraninf', u'Niveau 45', u'Libegon'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.; +2 Vit.', 'egg': u'Insecte', 'size': u'2,0m'}})
list.update ({u'Cacnea': {'catch': u'190', 'weight': u'51,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Cacnea', u'Niveau 32', u'Cacturne'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Plante/Humanoide', 'size': u'0,4m'}})
list.update ({u'Cacturne': {'catch': u'60', 'weight': u'77,4kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Cacnea', u'Niveau 32', u'Cacturne'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.; +1 Att. Spe', 'egg': u'Plante/Humanoide', 'size': u'1,3m'}})
list.update ({u'Tylton': {'catch': u'255', 'weight': u'1,2kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tylton', u'Niveau 35', u'Altaria'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Vol/Dragon', 'size': u'0,4m'}})
list.update ({u'Altaria': {'catch': u'45', 'weight': u'20,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tylton', u'Niveau 35', u'Altaria'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def. Spe', 'egg': u'Vol/Dragon', 'size': u'1,1m'}})
list.update ({u'Mangriff': {'catch': u'90', 'weight': u'40,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Sol', 'size': u'1,3m'}})
list.update ({u'Seviper': {'catch': u'90', 'weight': u'52,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Sol/Dragon', 'size': u'2,7m'}})
list.update ({u'Seleroc': {'catch': u'45', 'weight': u'168,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+2 Att. Spe', 'egg': u'Mineral', 'size': u'1,0m'}})
list.update ({u'Solaroc': {'catch': u'45', 'weight': u'154,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+2 Att.', 'egg': u'Mineral', 'size': u'1,2m'}})
list.update ({u'Barloche': {'catch': u'190', 'weight': u'1,9kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Barloche', u'Niveau 30', u'Barbicha'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Eau 2', 'size': u'0,4m'}})
list.update ({u'Barbicha': {'catch': u'75', 'weight': u'23,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Barloche', u'Niveau 30', u'Barbicha'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Eau 2', 'size': u'0,9m'}})
list.update ({u'Ecrapince': {'catch': u'205', 'weight': u'11,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Ecrapince', u'Niveau 30', u'Colhomard'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Eau 1/Eau 3', 'size': u'0,6m'}})
list.update ({u'Colhomard': {'catch': u'255', 'weight': u'32,8kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Ecrapince', u'Niveau 30', u'Colhomard'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Eau 1/Eau 3', 'size': u'1,1m'}})
list.update ({u'Balbuto': {'catch': u'255', 'weight': u'21,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Balbuto', u'Niveau 36', u'Kaorine'], 'gender': u'Asexue', 'ev': u'+1 Vit.', 'egg': u'Mineral', 'size': u'0,5m'}})
list.update ({u'Kaorine': {'catch': u'90', 'weight': u'108,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Balbuto', u'Niveau 36', u'Kaorine'], 'gender': u'Asexue', 'ev': u'+2 Vit.', 'egg': u'Mineral', 'size': u'1,5m'}})
list.update ({u'Lilia': {'catch': u'45', 'weight': u'23,8kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [u'Lilia', u'Niveau 40', u'Vacilys'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Def. Spe', 'egg': u'Eau 3', 'size': u'1,0m'}})
list.update ({u'Vacilys': {'catch': u'45', 'weight': u'60,4kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [u'Lilia', u'Niveau 40', u'Vacilys'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Def. Spe', 'egg': u'Eau 3', 'size': u'1,5m'}})
list.update ({u'Anorith': {'catch': u'45', 'weight': u'12,5kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [u'Anorith', u'Niveau 40', u'Armaldo'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att.', 'egg': u'Eau 3', 'size': u'0,7m'}})
list.update ({u'Armaldo': {'catch': u'45', 'weight': u'68,2kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [u'Anorith', u'Niveau 40', u'Armaldo'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att.', 'egg': u'Eau 3', 'size': u'1,5m'}})
list.update ({u'Barpau': {'catch': u'255', 'weight': u'7,4kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Barpau', u"Niveau de Beaute superieur ou egal a 170 (3eme et 4eme generations) ou Echange en tenant l'objet Bel'Ecaille (5eme et 6eme generations) ou Tenir le Voile Venus (Pokemon Donjon Mystere)", u'Milobellus'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Eau 1/Dragon', 'size': u'0,6m'}})
list.update ({u'Milobellus': {'catch': u'60', 'weight': u'162,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Barpau', u"Niveau de Beaute superieur ou egal a 170 (3eme et 4eme generations) ou Echange en tenant l'objet Bel'Ecaille (5eme et 6eme generations) ou Tenir le Voile Venus (Pokemon Donjon Mystere)", u'Milobellus'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def. Spe', 'egg': u'Dragon/Eau 1', 'size': u'6,2m'}})
list.update ({u'Morpheo': {'catch': u'45', 'weight': u'0,8kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Fee/Indetermine', 'size': u'0,3m'}})
list.update ({u'Kecleon': {'catch': u'45', 'weight': u'22,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Polichombr': {'catch': u'225', 'weight': u'2,3kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Polichombr', u'Niveau 37', u'Branette', u'Branettite', u'Mega-Branette'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Indetermine', 'size': u'0,6m'}})
list.update ({u'Branette': {'catch': u'45', 'weight': u'12,5kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Polichombr', u'Niveau 37', u'Branette', u'Branettite', u'Mega-Branette'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Indetermine', 'size': u'1,1m'}})
list.update ({u'Mega-Branette': {'catch': u'', 'weight': u'13kg', 'hatch': u'', 'evolutions': [u'Polichombr', u'Niveau 37', u'Branette', u'Branettite', u'Mega-Branette'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'', 'size': u'1,2m'}})
list.update ({u'Skelenox': {'catch': u'190', 'weight': u'15,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Skelenox', u'Niveau 37', u'Teraclope', u"Echange en tenant l'objet Tissu Fauche", u'Noctunoir'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Indetermine', 'size': u'0,8m'}})
list.update ({u'Teraclope': {'catch': u'90', 'weight': u'30,6kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Skelenox', u'Niveau 37', u'Teraclope', u"Echange en tenant l'objet Tissu Fauche", u'Noctunoir'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.; +1 Def. Spe', 'egg': u'Indetermine', 'size': u'1,6m'}})
list.update ({u'Tropius': {'catch': u'200', 'weight': u'100,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Monstre/Plante', 'size': u'2,0m'}})
list.update ({u'Eoko': {'catch': u'45', 'weight': u'1,0kg', 'hatch': u'25 cycles - 6655 pas', 'evolutions': [u'Korillon', u'Bonheur , Nuit', u'Eoko'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe; +1 Def. Spe', 'egg': u'Indetermine', 'size': u'0,6m'}})
list.update ({u'Absol': {'catch': u'30', 'weight': u'47,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Absol', u'Absolite', u'Mega-Absol'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Sol', 'size': u'1,2m'}})
list.update ({u'Mega-Absol': {'catch': u'', 'weight': u'49,0kg', 'hatch': u'', 'evolutions': [u'Absol', u'Absolite', u'Mega-Absol'], 'gender': u'100% femelle; 0% male', 'ev': u'', 'egg': u'', 'size': u'1,2m'}})
list.update ({u'Okeoke': {'catch': u'125', 'weight': u'14,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Okeoke', u'Niveau 15', u'Qulbutoke'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Sans oeuf', 'size': u'0,6m'}})
list.update ({u'Stalgamin': {'catch': u'190', 'weight': u'16,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Stalgamin', u'Niveau 42', u'Femelle + Pierre Aube', u'Oniglali', u'Momartik'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Fee/Mineral', 'size': u'0,7m'}})
list.update ({u'Oniglali': {'catch': u'75', 'weight': u'256,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Stalgamin', u'Niveau 42', u'Femelle + Pierre Aube', u'Oniglali', u'Momartik'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Fee/Mineral', 'size': u'1,5m'}})
list.update ({u'Obalie': {'catch': u'255', 'weight': u'39,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Obalie', u'Niveau 32', u'Phogleur', u'Niveau 44', u'Kaimorse'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Eau 1/Sol', 'size': u'0,8m'}})
list.update ({u'Phogleur': {'catch': u'120', 'weight': u'87,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Obalie', u'Niveau 32', u'Phogleur', u'Niveau 44', u'Kaimorse'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Eau 1/Sol', 'size': u'1,1m'}})
list.update ({u'Kaimorse': {'catch': u'45', 'weight': u'150,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Obalie', u'Niveau 32', u'Phogleur', u'Niveau 44', u'Kaimorse'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 PV', 'egg': u'Eau 1/Sol', 'size': u'1,4m'}})
list.update ({u'Coquiperl': {'catch': u'255', 'weight': u'52,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Coquiperl', u'Echange en tenant une Dent Ocean', u'Echange en tenant une Ecaille Ocean', u'Serpang', u'Rosabyss'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Eau 1', 'size': u'0,4m'}})
list.update ({u'Serpang': {'catch': u'60', 'weight': u'27,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Coquiperl', u'Echange en tenant une Dent Ocean', u'Echange en tenant une Ecaille Ocean', u'Serpang', u'Rosabyss'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.; +1 Def.', 'egg': u'Eau 1', 'size': u'1,7m'}})
list.update ({u'Rosabyss': {'catch': u'60', 'weight': u'22,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Coquiperl', u'Echange en tenant une Dent Ocean', u'Echange en tenant une Ecaille Ocean', u'Serpang', u'Rosabyss'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Eau 1', 'size': u'1,8m'}})
list.update ({u'Relicanth': {'catch': u'25', 'weight': u'23,4kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 PV; +1 Def.', 'egg': u'Eau 1/Eau 2', 'size': u'1,0m'}})
list.update ({u'Lovdisc': {'catch': u'225', 'weight': u'8,7kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'75% femelle; 25% male', 'ev': u'+1 Vit.', 'egg': u'Eau 2', 'size': u'0,6m'}})
list.update ({u'Draby': {'catch': u'45', 'weight': u'42,1kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Draby', u'Niveau 30', u'Drackhaus', u'Niveau 50', u'Drattak'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Dragon', 'size': u'0,6m'}})
list.update ({u'Drackhaus': {'catch': u'45', 'weight': u'110,5kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Draby', u'Niveau 30', u'Drackhaus', u'Niveau 50', u'Drattak'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Dragon', 'size': u'1,1m'}})
list.update ({u'Drattak': {'catch': u'45', 'weight': u'102,6kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Draby', u'Niveau 30', u'Drackhaus', u'Niveau 50', u'Drattak'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att.', 'egg': u'Dragon', 'size': u'1,5m'}})
list.update ({u'Terhal': {'catch': u'3', 'weight': u'95,2kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Terhal', u'Niveau 20', u'Metang', u'Niveau 45', u'Metalosse'], 'gender': u'Asexue', 'ev': u'+1 Def.', 'egg': u'Mineral', 'size': u'0,6m'}})
list.update ({u'Metang': {'catch': u'3', 'weight': u'202,5kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Terhal', u'Niveau 20', u'Metang', u'Niveau 45', u'Metalosse'], 'gender': u'Asexue', 'ev': u'+2 Def.', 'egg': u'Mineral', 'size': u'1,2m'}})
list.update ({u'Metalosse': {'catch': u'3', 'weight': u'550,0kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Terhal', u'Niveau 20', u'Metang', u'Niveau 45', u'Metalosse'], 'gender': u'Asexue', 'ev': u'+3 Def.', 'egg': u'Mineral', 'size': u'1,6m'}})
list.update ({u'Regirock': {'catch': u'3', 'weight': u'230,0kg', 'hatch': u'79 cycles - 20480 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Def.', 'egg': u'Sans oeuf', 'size': u'1,7m'}})
list.update ({u'Regice': {'catch': u'3', 'weight': u'175,0kg', 'hatch': u'79 cycles - 20480 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Def. Spe', 'egg': u'Sans oeuf', 'size': u'1,8m'}})
list.update ({u'Registeel': {'catch': u'3', 'weight': u'205,0kg', 'hatch': u'79 cycles - 20480 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+2 Def.; +1 Def. Spe', 'egg': u'Sans oeuf', 'size': u'1,9m'}})
list.update ({u'Latias': {'catch': u'3', 'weight': u'40,0kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'100% femelle; 0% male', 'ev': u'+3 Def. Spe', 'egg': u'Sans oeuf', 'size': u'1,4m'}})
list.update ({u'Latios': {'catch': u'3', 'weight': u'60,0kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'0% femelle; 100% male', 'ev': u'+3 Att. Spe', 'egg': u'Sans oeuf', 'size': u'2,0m'}})
list.update ({u'Kyogre': {'catch': u'5', 'weight': u'352,0kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Att. Spe', 'egg': u'Sans oeuf', 'size': u'4,5m'}})
list.update ({u'Groudon': {'catch': u'5', 'weight': u'950,0kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Att.', 'egg': u'Sans oeuf', 'size': u'3,5m'}})
list.update ({u'Rayquaza': {'catch': u'3', 'weight': u'206,5kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+2 Att.; +1 Att. Spe', 'egg': u'Sans oeuf', 'size': u'7,0m'}})
list.update ({u'Jirachi': {'catch': u'3', 'weight': u'1,1kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 PV', 'egg': u'Sans oeuf', 'size': u'0,3m'}})
list.update ({u'Deoxys (Forme de Base)': {'catch': u'3', 'weight': u'60,8kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att.; +1 Att. Spe; +1 Vit.', 'egg': u'Sans oeuf', 'size': u'1,7m'}})
list.update ({u'Deoxys (Forme Attaque)': {'catch': u'3', 'weight': u'60,8kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att.; +1 Att. Spe; +1 Vit.', 'egg': u'Sans oeuf', 'size': u'1,7m'}})
list.update ({u'Deoxys (Forme Defense)': {'catch': u'3', 'weight': u'60,8kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att.; +1 Att. Spe; +1 Vit.', 'egg': u'Sans oeuf', 'size': u'1,7m'}})
list.update ({u'Deoxys (Forme Vitesse)': {'catch': u'3', 'weight': u'60,8kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att.; +1 Att. Spe; +1 Vit.', 'egg': u'Sans oeuf', 'size': u'1,7m'}})
list.update ({u'Tortipouss': {'catch': u'45', 'weight': u'10,2kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tortipouss', u'Niveau 18', u'Boskara', u'Niveau 32', u'Torterra'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att.', 'egg': u'Monstre/Plante', 'size': u'0,4m'}})
list.update ({u'Boskara': {'catch': u'45', 'weight': u'97,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tortipouss', u'Niveau 18', u'Boskara', u'Niveau 32', u'Torterra'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att.; +1 Att. Spe', 'egg': u'Monstre/Plante', 'size': u'1,1m'}})
list.update ({u'Torterra': {'catch': u'45', 'weight': u'310,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tortipouss', u'Niveau 18', u'Boskara', u'Niveau 32', u'Torterra'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att.; +1 Def.', 'egg': u'Monstre/Plante', 'size': u'2,2m'}})
list.update ({u'Ouisticram': {'catch': u'45', 'weight': u'6,2kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ouisticram', u'Niveau 14', u'Chimpenfeu', u'Niveau 36', u'Simiabraz'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Vit.', 'egg': u'Sol/Humanoide', 'size': u'0,5m'}})
list.update ({u'Chimpenfeu': {'catch': u'45', 'weight': u'22,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ouisticram', u'Niveau 14', u'Chimpenfeu', u'Niveau 36', u'Simiabraz'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att. Spe; +1 Vit.', 'egg': u'Sol/Humanoide', 'size': u'0,9m'}})
list.update ({u'Simiabraz': {'catch': u'45', 'weight': u'55kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ouisticram', u'Niveau 14', u'Chimpenfeu', u'Niveau 36', u'Simiabraz'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att.; +1 Att. Spe; +1 Vit.', 'egg': u'Sol/Humanoide', 'size': u'1,2m'}})
list.update ({u'Tiplouf': {'catch': u'45', 'weight': u'5,2kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tiplouf', u'Niveau 16', u'Prinplouf', u'Niveau 36', u'Pingoleon'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att. Spe', 'egg': u'Eau 1/Sol', 'size': u'0,4m'}})
list.update ({u'Prinplouf': {'catch': u'45', 'weight': u'23,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tiplouf', u'Niveau 16', u'Prinplouf', u'Niveau 36', u'Pingoleon'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att. Spe', 'egg': u'Eau 1/Sol', 'size': u'0,8m'}})
list.update ({u'Pingoleon': {'catch': u'45', 'weight': u'84,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tiplouf', u'Niveau 16', u'Prinplouf', u'Niveau 36', u'Pingoleon'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+3 Att. Spe', 'egg': u'Eau 1/Sol', 'size': u'1,7m'}})
list.update ({u'Etourmi': {'catch': u'255', 'weight': u'2,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Etourmi', u'Niveau 14', u'Etourvol', u'Niveau 34', u'Etouraptor'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Vol', 'size': u'0,3m'}})
list.update ({u'Etourvol': {'catch': u'120', 'weight': u'15,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Etourmi', u'Niveau 14', u'Etourvol', u'Niveau 34', u'Etouraptor'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Vol', 'size': u'0,6m'}})
list.update ({u'Etouraptor': {'catch': u'45', 'weight': u'24,9kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Etourmi', u'Niveau 14', u'Etourvol', u'Niveau 34', u'Etouraptor'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att.', 'egg': u'Vol', 'size': u'1,2m'}})
list.update ({u'Keunotor': {'catch': u'255', 'weight': u'20,0kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Keunotor', u'Niveau 15', u'Castorno'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Eau 1/Sol', 'size': u'0,5m'}})
list.update ({u'Castorno': {'catch': u'127', 'weight': u'31,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Keunotor', u'Niveau 15', u'Castorno'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Eau 1/Sol', 'size': u'1,0m'}})
list.update ({u'Crikzik': {'catch': u'255', 'weight': u'2,2kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Crikzik', u'Niveau 10', u'Melokrik'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Insecte', 'size': u'0,3m'}})
list.update ({u'Melokrik': {'catch': u'45', 'weight': u'25,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Crikzik', u'Niveau 10', u'Melokrik'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Insecte', 'size': u'1,0m'}})
list.update ({u'Lixy': {'catch': u'235', 'weight': u'9,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Lixy', u'Niveau 15', u'Luxio', u'Niveau 30', u'Luxray'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol', 'size': u'0,5m'}})
list.update ({u'Luxio': {'catch': u'120', 'weight': u'30,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Lixy', u'Niveau 15', u'Luxio', u'Niveau 30', u'Luxray'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Sol', 'size': u'0,9m'}})
list.update ({u'Luxray': {'catch': u'45', 'weight': u'42,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Lixy', u'Niveau 15', u'Luxio', u'Niveau 30', u'Luxray'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att.', 'egg': u'Sol', 'size': u'1,4m'}})
list.update ({u'Rozbouton': {'catch': u'255', 'weight': u'1,2kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Rozbouton', u'Bonheur , Jour', u'Roselia', u'Avec une Pierre Eclat', u'Roserade'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Sans oeuf', 'size': u'0,2m'}})
list.update ({u'Roserade': {'catch': u'75', 'weight': u'14,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Rozbouton', u'Bonheur , Jour', u'Roselia', u'Avec une Pierre Eclat', u'Roserade'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att. Spe', 'egg': u'Fee/Plante', 'size': u'0,9m'}})
list.update ({u'Kranidos': {'catch': u'45', 'weight': u'31,5kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [u'Kranidos', u'Niveau 30', u'Charkos'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att.', 'egg': u'Monstre', 'size': u'0,9m'}})
list.update ({u'Charkos': {'catch': u'45', 'weight': u'102,5kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [u'Kranidos', u'Niveau 30', u'Charkos'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att.', 'egg': u'Monstre', 'size': u'1,6m'}})
list.update ({u'Dinoclier': {'catch': u'45', 'weight': u'57,0kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [u'Dinoclier', u'Niveau 30', u'Bastiodon'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Def.', 'egg': u'Monstre', 'size': u'0,5m'}})
list.update ({u'Bastiodon': {'catch': u'45', 'weight': u'149,5kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [u'Dinoclier', u'Niveau 30', u'Bastiodon'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Def.', 'egg': u'Monstre', 'size': u'1,3m'}})
list.update ({u'Cheniti': {'catch': u'120', 'weight': u'3,4kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Cheniti', u'Si Femelle, Niveau 20', u'Si Male, Niveau 20', u'Cheniselle (Cape Plante)', u'Papilord'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Insecte', 'size': u'0,2m'}})
list.update ({u'Cheniselle (Cape Plante)': {'catch': u'45', 'weight': u'6,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Cheniti', u'Si Femelle, Niveau 20', u'Si Male, Niveau 20', u'Cheniselle (Cape Plante)', u'Papilord'], 'gender': u'100% femelle; 0% male', 'ev': u'+2 Def. Spe', 'egg': u'Insecte', 'size': u'0,5m'}})
list.update ({u'Cheniselle (Cape Sol)': {'catch': u'45', 'weight': u'6,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Cheniti', u'Si Femelle, Niveau 20', u'Si Male, Niveau 20', u'Cheniselle (Cape Sol)', u'Papilord'], 'gender': u'100% femelle; 0% male', 'ev': u'+2 Def. Spe', 'egg': u'Insecte', 'size': u'0,5m'}})
list.update ({u'Cheniselle (Cape Dechet)': {'catch': u'45', 'weight': u'6,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Cheniti', u'Si Femelle, Niveau 20', u'Si Male, Niveau 20', u'Cheniselle (Cape Dechet)', u'Papilord'], 'gender': u'100% femelle; 0% male', 'ev': u'+2 Def. Spe', 'egg': u'Insecte', 'size': u'0,5m'}})
list.update ({u'Papilord': {'catch': u'45', 'weight': u'23,3kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Cheniti', u'Si Femelle, Niveau 20', u'Si Male, Niveau 20', u'Cheniselle (Cape Plante)', u'Papilord'], 'gender': u'0% femelle; 100% male', 'ev': u'+1 Att.; +1 Att. Spe', 'egg': u'Insecte', 'size': u'0,9m'}})
list.update ({u'Apitrini': {'catch': u'120', 'weight': u'5,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Apitrini', u'Si Femelle, Niveau 21', u'Si Male', u'Apireine'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Vit.', 'egg': u'Insecte', 'size': u'0,3m'}})
list.update ({u'Apireine': {'catch': u'45', 'weight': u'38,5kg', 'hatch': u'14 cycles - 3840 pas', 'evolutions': [u'Apitrini', u'Si Femelle, Niveau 21', u'Si Male', u'Apireine'], 'gender': u'100% femelle; 0% male', 'ev': u'+1 Def.; +1 Def. Spe', 'egg': u'Insecte', 'size': u'1,2m'}})
list.update ({u'Pachirisu': {'catch': u'200', 'weight': u'3,9kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Fee/Sol', 'size': u'0,4m'}})
list.update ({u'Mustebouee': {'catch': u'190', 'weight': u'29,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Mustebouee', u'niveau 26', u'Musteflott'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Eau 1/Sol', 'size': u'0,7m'}})
list.update ({u'Musteflott': {'catch': u'75', 'weight': u'33,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Mustebouee', u'niveau 26', u'Musteflott'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Eau 1/Sol', 'size': u'1,1m'}})
list.update ({u'Ceribou': {'catch': u'190', 'weight': u'3,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ceribou', u'Niveau 25', u'Ceriflor'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Fee/Plante', 'size': u'0,4m'}})
list.update ({u'Ceriflor': {'catch': u'75', 'weight': u'9,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ceribou', u'Niveau 25', u'Ceriflor'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Fee/Plante', 'size': u'0,5m'}})
list.update ({u'Sancoki': {'catch': u'190', 'weight': u'6,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Sancoki', u'niveau 30', u'Tritosor'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Eau 1/Indetermine', 'size': u'0,3m'}})
list.update ({u'Tritosor': {'catch': u'75', 'weight': u'29,9kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Sancoki', u'niveau 30', u'Tritosor'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Eau 1/Indetermine', 'size': u'0,9m'}})
list.update ({u'Capidextre': {'catch': u'45', 'weight': u'20,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Capumain', u"En connaissant l'attaque Coup Double + passer un niveau", u'Capidextre'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'1,2m'}})
list.update ({u'Baudrive': {'catch': u'125', 'weight': u'1,2kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [u'Baudrive', u'Niveau 28', u'Grodrive'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Indetermine', 'size': u'0,4m'}})
list.update ({u'Grodrive': {'catch': u'60', 'weight': u'15,0kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [u'Baudrive', u'Niveau 28', u'Grodrive'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Indetermine', 'size': u'1,2m'}})
list.update ({u'Laporeille': {'catch': u'190', 'weight': u'5,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Laporeille', u'Bonheur', u'Lockpin'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol/Humanoide', 'size': u'0,4m'}})
list.update ({u'Lockpin': {'catch': u'60', 'weight': u'33,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Laporeille', u'Bonheur', u'Lockpin'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol/Humanoide', 'size': u'1,2m'}})
list.update ({u'Magireve': {'catch': u'45', 'weight': u'4,4kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Feuforeve', u'Avec une Pierre Nuit', u'Magireve'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe;  +1 Def. Spe', 'egg': u'Indetermine', 'size': u'0,9m'}})
list.update ({u'Corboss': {'catch': u'30', 'weight': u'27,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Cornebre', u'Avec une Pierre Nuit', u'Corboss'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Vol', 'size': u'0,9m'}})
list.update ({u'Chaglam': {'catch': u'190', 'weight': u'3,9kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Chaglam', u'niveau 38', u'Chaffreux'], 'gender': u'75% femelle; 25% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,75m'}})
list.update ({u'Chaffreux': {'catch': u'75', 'weight': u'43,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Chaglam', u'niveau 38', u'Chaffreux'], 'gender': u'75% femelle; 25% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Korillon': {'catch': u'120', 'weight': u'0,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Korillon', u'Bonheur , Nuit', u'Eoko'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Sans oeuf', 'size': u'0,2m'}})
list.update ({u'Moufouette': {'catch': u'225', 'weight': u'19,2kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Moufouette', u'niveau 34', u'Moufflair'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,4m'}})
list.update ({u'Moufflair': {'catch': u'60', 'weight': u'38,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Moufouette', u'niveau 34', u'Moufflair'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Archeomire': {'catch': u'255', 'weight': u'60,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Archeomire', u'niveau 33', u'Archeodong'], 'gender': u'Asexue', 'ev': u'+1 Def.', 'egg': u'Mineral', 'size': u'0,5m'}})
list.update ({u'Archeodong': {'catch': u'90', 'weight': u'187,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Archeomire', u'niveau 33', u'Archeodong'], 'gender': u'Asexue', 'ev': u'+1 Def.; +1 Def. Spe', 'egg': u'Mineral', 'size': u'1,3m'}})
list.update ({u'Manzai': {'catch': u'255', 'weight': u'15,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Manzai', u"En apprenant l'attaque Copie", u'Simularbre'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Sans oeuf', 'size': u'0,5m'}})
list.update ({u'Mime Jr.': {'catch': u'145', 'weight': u'13,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Mime Jr.', u"En apprenant l'attaque Copie", u'M. Mime'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Sans oeuf', 'size': u'0,6m'}})
list.update ({u'Ptiravi': {'catch': u'130', 'weight': u'24,4kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Ptiravi', u'Gain de niveau en journee en tenant une Pierre Ovale', u'Leveinard', u'Bonheur', u'Leuphorie'], 'gender': u'100% femelle; 0% male', 'ev': u'+1 PV', 'egg': u'Sans oeuf', 'size': u'0,6m'}})
list.update ({u'Pijako': {'catch': u'30', 'weight': u'1,9kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Vol', 'size': u'0,5m'}})
list.update ({u'Spiritomb': {'catch': u'100', 'weight': u'108kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Indetermine', 'size': u'1,0m'}})
list.update ({u'Griknot': {'catch': u'45', 'weight': u'20,5kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Griknot', u'Niveau 24', u'Carmache', u'Niveau 48', u'Carchacrok', u'Carchacrokite', u'Mega-Carchacrok'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Dragon/Monstre', 'size': u'0,7m'}})
list.update ({u'Carmache': {'catch': u'45', 'weight': u'56,0kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Griknot', u'Niveau 24', u'Carmache', u'Niveau 48', u'Carchacrok', u'Carchacrokite', u'Mega-Carchacrok'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Dragon/Monstre', 'size': u'1,4m'}})
list.update ({u'Carchacrok': {'catch': u'45', 'weight': u'95,0kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Griknot', u'Niveau 24', u'Carmache', u'Niveau 48', u'Carchacrok', u'Carchacrokite', u'Mega-Carchacrok'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att.', 'egg': u'Dragon/Monstre', 'size': u'1,9m'}})
list.update ({u'Mega-Carchacrok': {'catch': u'', 'weight': u'95,0kg', 'hatch': u'', 'evolutions': [u'Griknot', u'Niveau 24', u'Carmache', u'Niveau 48', u'Carchacrok', u'Carchacrokite', u'Mega-Carchacrok'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'', 'size': u'1,9m'}})
list.update ({u'Goinfrex': {'catch': u'50', 'weight': u'105,0kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Goinfrex', u'Bonheur', u'Ronflex'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 PV', 'egg': u'Sans oeuf', 'size': u'0,6m'}})
list.update ({u'Riolu': {'catch': u'75', 'weight': u'20,2kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Riolu', u'Bonheur + gagne un niveau de jour', u'Lucario', u'Lucarite', u'Mega-Lucario'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att.', 'egg': u'Sans oeuf', 'size': u'0,7m'}})
list.update ({u'Lucario': {'catch': u'45', 'weight': u'54,0kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Riolu', u'Bonheur + gagne un niveau de jour', u'Lucario', u'Lucarite', u'Mega-Lucario'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att.; +1 Att. Spe', 'egg': u'Sol/Humanoide', 'size': u'1,2m'}})
list.update ({u'Mega-Lucario': {'catch': u'', 'weight': u'57,5kg', 'hatch': u'', 'evolutions': [u'Riolu', u'Bonheur + gagne un niveau de jour', u'Lucario', u'Lucarite', u'Mega-Lucario'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'', 'egg': u'', 'size': u'1,5m'}})
list.update ({u'Hippopotas': {'catch': u'140', 'weight': u'49,5kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [u'Hippopotas', u'niveau 34', u'Hippodocus'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Sol', 'size': u'0,8m'}})
list.update ({u'Hippodocus': {'catch': u'60', 'weight': u'300,0kg', 'hatch': u'29 cycles - 7680 pas', 'evolutions': [u'Hippopotas', u'niveau 34', u'Hippodocus'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Sol', 'size': u'2,0m'}})
list.update ({u'Rapion': {'catch': u'120', 'weight': u'12,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Rapion', u'niveau 40', u'Drascore'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Insecte/Eau 3', 'size': u'0,8m'}})
list.update ({u'Drascore': {'catch': u'45', 'weight': u'61,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Rapion', u'Niveau 40', u'Drascore'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Insecte/Eau 3', 'size': u'1,3m'}})
list.update ({u'Cradopaud': {'catch': u'140', 'weight': u'23,0kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Cradopaud', u'niveau 37', u'Coatox'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Humanoide', 'size': u'0,7m'}})
list.update ({u'Coatox': {'catch': u'75', 'weight': u'44,4kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Cradopaud', u'niveau 37', u'Coatox'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Humanoide', 'size': u'1,3m'}})
list.update ({u'Vortente': {'catch': u'200', 'weight': u'27,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Plante', 'size': u'1,4m'}})
list.update ({u'Ecayon': {'catch': u'190', 'weight': u'7,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ecayon', u'niveau 31', u'Lumineon'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Eau 2', 'size': u'0,4m'}})
list.update ({u'Lumineon': {'catch': u'75', 'weight': u'24,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Ecayon', u'Niveau 31', u'Lumineon'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Eau 2', 'size': u'1,2m'}})
list.update ({u'Babimanta': {'catch': u'25', 'weight': u'65,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Babimanta', u"Gain de niveau avec Remoraid dans l'equipe", u'Demanta'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sans oeuf', 'size': u'1,0m'}})
list.update ({u'Blizzi': {'catch': u'120', 'weight': u'50,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Blizzi', u'Niveau 40', u'Blizzaroi', u'Blizzarite', u'Mega-Blizzaroi'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Monstre/Plante', 'size': u'1,0m'}})
list.update ({u'Blizzaroi': {'catch': u'60', 'weight': u'135,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Blizzi', u'Niveau 40', u'Blizzaroi', u'Blizzarite', u'Mega-Blizzaroi'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.; +1 Att. Spe', 'egg': u'Monstre/Plante', 'size': u'2,2m'}})
list.update ({u'Mega-Blizzaroi': {'catch': u'', 'weight': u'135,5kg', 'hatch': u'', 'evolutions': [u'Blizzi', u'Niveau 40', u'Blizzaroi', u'Blizzarite', u'Mega-Blizzaroi'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'', 'size': u'2,2m'}})
list.update ({u'Dimoret': {'catch': u'45', 'weight': u'34,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Farfuret', u'Gagne un niveau de nuit en tenant une Griffe Rasoir', u'Dimoret'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.; +1 Vit.', 'egg': u'Sol', 'size': u'1,1m'}})
list.update ({u'Magnezone': {'catch': u'30', 'weight': u'180,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Magneti', u'Niveau 30', u'Magneton', u'Gain de niveau dans un lieu indique', u'Magnezone'], 'gender': u'Asexue', 'ev': u'+3 Att. Spe', 'egg': u'Mineral', 'size': u'1,2m'}})
list.update ({u'Coudlangue': {'catch': u'30', 'weight': u'140,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Excelangue', u"En connaissant l'attaque Roulade", u'Coudlangue'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Monstre', 'size': u'1,7m'}})
list.update ({u'Rhinastoc': {'catch': u'30', 'weight': u'282,8kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Rhinocorne', u'Niveau 42', u'Rhinoferos', u"Echange en tenant l'objet Protecteur", u'Rhinastoc'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Monstre/Sol', 'size': u'2,4m'}})
list.update ({u'Bouldeneu': {'catch': u'30', 'weight': u'128,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Saquedeneu', u"En apprenant l'attaque Pouv.Antique", u'Bouldeneu'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Plante', 'size': u'2,0m'}})
list.update ({u'Elekable': {'catch': u'30', 'weight': u'140,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Elekid', u'Niveau 30', u'Elektek', u'Echange en tenant un Electiriseur', u'Elekable'], 'gender': u'75% femelle; 25% male', 'ev': u'+3 Att.', 'egg': u'Humanoide', 'size': u'1,8m'}})
list.update ({u'Maganon': {'catch': u'30', 'weight': u'68,0kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Magby', u'Niveau 30', u'Magmar', u'Echange en tenant Magmariseur', u'Maganon'], 'gender': u'25% femelle; 75% male', 'ev': u'+3 Att. Spe', 'egg': u'Humanoide', 'size': u'1,6m'}})
list.update ({u'Togekiss': {'catch': u'30', 'weight': u'38,0kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [u'Togepi', u'Bonheur', u'Togetic', u'Avec une Pierre Eclat', u'Togekiss'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att. Spe; +1 Def. Spe', 'egg': u'Vol/Fee', 'size': u'1,5m'}})
list.update ({u'Yanmega': {'catch': u'30', 'weight': u'51,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Yanma', u"En apprenant l'attaque Pouv.Antique", u'Yanmega'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Insecte', 'size': u'1,9m'}})
list.update ({u'Phyllali': {'catch': u'45', 'weight': u'25,5kg', 'hatch': u'34 cycles - 8960 pas', 'evolutions': [u'Evoli', u'Avec une Pierre Eau', u'Avec une Pierre Foudre', u'Avec une Pierre Feu', u'Bonheur , Jour', u'Bonheur , Nuit', u"Pres d'une Pierre Mousse + gagne un niveau", u"Pres d'une Pierre Glacee + gagne un niveau", u"2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Def.', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Givrali': {'catch': u'45', 'weight': u'25,9kg', 'hatch': u'34 cycles - 8960 pas', 'evolutions': [u'Evoli', u'Avec une Pierre Eau', u'Avec une Pierre Foudre', u'Avec une Pierre Feu', u'Bonheur , Jour', u'Bonheur , Nuit', u"Pres d'une Pierre Mousse + gagne un niveau", u"Pres d'une Pierre Glacee + gagne un niveau", u"2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att. Spe', 'egg': u'Sol', 'size': u'0,8m'}})
list.update ({u'Scorvol': {'catch': u'30', 'weight': u'42,5kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Scorplane', u'Gagne un niveau de nuit en tenant un Croc Rasoir', u'Scorvol'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Insecte', 'size': u'2,0m'}})
list.update ({u'Mammochon': {'catch': u'50', 'weight': u'291,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Marcacrin', u'Niveau 33', u'Cochignon', u"En connaissant l'attaque Pouv.Antique et lui faire monter d'un niveau", u'Mammochon'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att.', 'egg': u'Sol', 'size': u'2,5m'}})
list.update ({u'Porygon-Z': {'catch': u'30', 'weight': u'34,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Porygon', u'Echange en tenant Ameliorator', u'Porygon2', u'Echange en tenant CD Douteux', u'Porygon-Z'], 'gender': u'Asexue', 'ev': u'+3 Att. Spe', 'egg': u'Mineral', 'size': u'0,9m'}})
list.update ({u'Gallame': {'catch': u'60', 'weight': u'52,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tarsal', u'Niveau 20', u'Kirlia', u'Niveau 30', u'Male + Pierre Aube', u'Gardevoir', u'Gallame', u'Gardevoirite', u'Mega-Gardevoir'], 'gender': u'0% femelle; 100% male', 'ev': u'+2 Att.', 'egg': u'Indetermine', 'size': u'1,6m'}})
list.update ({u'Tarinorme': {'catch': u'60', 'weight': u'340,0kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Tarinor', u'Gain de niveau dans un lieu indique', u'Tarinorme'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def. Spe', 'egg': u'Mineral', 'size': u'1,4m'}})
list.update ({u'Noctunoir': {'catch': u'45', 'weight': u'106,6kg', 'hatch': u'24 cycles - 6400 pas', 'evolutions': [u'Skelenox', u'Niveau 37', u'Teraclope', u"Echange en tenant l'objet Tissu Fauche", u'Noctunoir'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def. Spe', 'egg': u'Indetermine', 'size': u'2,2m'}})
list.update ({u'Momartik': {'catch': u'75', 'weight': u'26,6kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [u'Stalgamin', u'Niveau 42', u'Femelle + Pierre Aube', u'Oniglali', u'Momartik'], 'gender': u'100% femelle; 0% male', 'ev': u'+2 Vit.', 'egg': u'Fee/Mineral', 'size': u'1,3m'}})
list.update ({u'Motisma (Forme Normale)': {'catch': u'45', 'weight': u'0,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att. Spe; +1 Vit.', 'egg': u'Indetermine', 'size': u'0,3m'}})
list.update ({u'Motisma (Forme Chaleur)': {'catch': u'45', 'weight': u'0,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att. Spe; +1 Vit.', 'egg': u'Indetermine', 'size': u'0,3m'}})
list.update ({u'Motisma (Forme Lavage)': {'catch': u'45', 'weight': u'0,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att. Spe; +1 Vit.', 'egg': u'Indetermine', 'size': u'0,3m'}})
list.update ({u'Motisma (Forme Froid)': {'catch': u'45', 'weight': u'0,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att. Spe; +1 Vit.', 'egg': u'Indetermine', 'size': u'0,3m'}})
list.update ({u'Motisma (Forme Tonte)': {'catch': u'45', 'weight': u'0,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att. Spe; +1 Vit.', 'egg': u'Indetermine', 'size': u'0,3m'}})
list.update ({u'Motisma (Forme Helice)': {'catch': u'45', 'weight': u'0,3kg', 'hatch': u'19 cycles - 5120 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att. Spe; +1 Vit.', 'egg': u'Indetermine', 'size': u'0,3m'}})
list.update ({u'Crehelf': {'catch': u'3', 'weight': u'0,3kg', 'hatch': u'79 cycles - 20480 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+2 Def.; +1 Def. Spe', 'egg': u'Sans oeuf', 'size': u'0,3m'}})
list.update ({u'Crefollet': {'catch': u'3', 'weight': u'0,3kg', 'hatch': u'79 cycles - 20480 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att. Spe; +1 Def. Spe; +1 Vit.', 'egg': u'Sans oeuf', 'size': u'0,3m'}})
list.update ({u'Crefadet': {'catch': u'3', 'weight': u'0,3kg', 'hatch': u'79 cycles - 20480 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+2 Att.; +1 Att. Spe', 'egg': u'Sans oeuf', 'size': u'0,3m'}})
list.update ({u'Dialga': {'catch': u'30', 'weight': u'683kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Att. Spe', 'egg': u'Sans oeuf', 'size': u'5,4m'}})
list.update ({u'Palkia': {'catch': u'30', 'weight': u'336,0kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Att. Spe', 'egg': u'Sans oeuf', 'size': u'4,2m'}})
list.update ({u'Heatran': {'catch': u'3', 'weight': u'430,0kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att. Spe', 'egg': u'Sans oeuf', 'size': u'1,7m'}})
list.update ({u'Regigigas': {'catch': u'3', 'weight': u'420,0kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Att.', 'egg': u'Sans oeuf', 'size': u'3,7m'}})
list.update ({u'Giratina (Forme Alternative)': {'catch': u'3', 'weight': u'750kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 PV', 'egg': u'Sans oeuf', 'size': u'4,5m'}})
list.update ({u'Giratina (Forme Originelle)': {'catch': u'3', 'weight': u'750kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 PV', 'egg': u'Sans oeuf', 'size': u'4,5m'}})
list.update ({u'Cresselia': {'catch': u'3', 'weight': u'85,6kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'100% femelle; 0% male', 'ev': u'+3 Vit.', 'egg': u'Sans oeuf', 'size': u'1,5m'}})
list.update ({u'Phione': {'catch': u'30', 'weight': u'3,1kg', 'hatch': u'41 cycles - 10710 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 PV', 'egg': u'Eau 1/Fee', 'size': u'0,4m'}})
list.update ({u'Manaphy': {'catch': u'3', 'weight': u'1,4kg', 'hatch': u'9 cycles - 2560 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 PV', 'egg': u'Eau 1/Fee', 'size': u'0,3m'}})
list.update ({u'Darkrai': {'catch': u'3', 'weight': u'50,5kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Vit.; +2 Att. Spe', 'egg': u'Sans oeuf', 'size': u'1,5m'}})
list.update ({u'Shaymin (Forme Terrestre)': {'catch': u'45', 'weight': u'2,1kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 PV', 'egg': u'Sans oeuf', 'size': u'0,2m'}})
list.update ({u'Shaymin (Forme Celeste)': {'catch': u'45', 'weight': u'2,1kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 PV', 'egg': u'Sans oeuf', 'size': u'0,2m'}})
list.update ({u'Arceus': {'catch': u'3', 'weight': u'320,0kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 PV', 'egg': u'Sans oeuf', 'size': u'3,2m'}})
list.update ({u'Victini': {'catch': u'3', 'weight': u'4kg', 'hatch': u'119 cycles - 30720 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 PV', 'egg': u'Sans oeuf', 'size': u'0,4m'}})
list.update ({u'Vipelierre': {'catch': u'45', 'weight': u'8,1kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Vipelierre', u'Niveau 17', u'Lianaja', u'Niveau 36', u'Majaspic'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Vit.', 'egg': u'Sol/Plante', 'size': u'0,6m'}})
list.update ({u'Lianaja': {'catch': u'45', 'weight': u'16kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Vipelierre', u'Niveau 17', u'Lianaja', u'Niveau 36', u'Majaspic'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Vit.', 'egg': u'Sol/Plante', 'size': u'0,8m'}})
list.update ({u'Majaspic': {'catch': u'45', 'weight': u'63kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Vipelierre', u'Niveau 17', u'Lianaja', u'Niveau 36', u'Majaspic'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+3 Vit.', 'egg': u'Sol/Plante', 'size': u'3,3m'}})
list.update ({u'Gruikui': {'catch': u'45', 'weight': u'9,9kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Gruikui', u'Niveau 17', u'Grotichon', u'Niveau 36', u'Roitiflam'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 PV', 'egg': u'Sol', 'size': u'0,5m'}})
list.update ({u'Grotichon': {'catch': u'45', 'weight': u'55,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Gruikui', u'Niveau 17', u'Grotichon', u'Niveau 36', u'Roitiflam'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att.', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Roitiflam': {'catch': u'45', 'weight': u'150kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Gruikui', u'Niveau 17', u'Grotichon', u'Niveau 36', u'Roitiflam'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+3 Att.', 'egg': u'Sol', 'size': u'1,6m'}})
list.update ({u'Moustillon': {'catch': u'45', 'weight': u'5,9kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Moustillon', u'Niveau 17', u'Mateloutre', u'Niveau 36', u'Clamiral'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att. Spe.', 'egg': u'Sol', 'size': u'0,5m'}})
list.update ({u'Mateloutre': {'catch': u'45', 'weight': u'24,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Moustillon', u'Niveau 17', u'Mateloutre', u'Niveau 36', u'Clamiral'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att. Spe.', 'egg': u'Sol', 'size': u'0,8m'}})
list.update ({u'Clamiral': {'catch': u'45', 'weight': u'94,6kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Moustillon', u'Niveau 17', u'Mateloutre', u'Niveau 36', u'Clamiral'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+3 Att. Spe.', 'egg': u'Sol', 'size': u'1,5m'}})
list.update ({u'Ratentif': {'catch': u'255', 'weight': u'11,6kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Ratentif', u'Niveau 20', u'Miradar'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol', 'size': u'0,5m'}})
list.update ({u'Miradar': {'catch': u'255', 'weight': u'27kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Ratentif', u'Niveau 20', u'Miradar'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol', 'size': u'1,1m'}})
list.update ({u'Ponchiot': {'catch': u'255', 'weight': u'4,1kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Ponchiot', u'Niveau 16', u'Ponchien', u'Niveau 32', u'Mastouffe'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol', 'size': u'0,4m'}})
list.update ({u'Ponchien': {'catch': u'120', 'weight': u'14,7kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Ponchiot', u'Niveau 16', u'Ponchien', u'Niveau 32', u'Mastouffe'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Sol', 'size': u'0,9m'}})
list.update ({u'Mastouffe': {'catch': u'45', 'weight': u'61,0kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Ponchiot', u'Niveau 16', u'Ponchien', u'Niveau 32', u'Mastouffe'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att.', 'egg': u'Sol', 'size': u'1,2m'}})
list.update ({u'Chacripan': {'catch': u'255', 'weight': u'10,1kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Chacripan', u'Niveau 20', u'Leopardus'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,4m'}})
list.update ({u'Leopardus': {'catch': u'90', 'weight': u'37,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Chacripan', u'Niveau 20', u'Leopardus'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'1,1m'}})
list.update ({u'Feuillajou': {'catch': u'190', 'weight': u'10,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Feuillajou', u'Avec une Pierre Plante', u'Feuiloutan'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,6m'}})
list.update ({u'Feuiloutan': {'catch': u'75', 'weight': u'30,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Feuillajou', u'Avec une Pierre Plante', u'Feuiloutan'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'1,1m'}})
list.update ({u'Flamajou': {'catch': u'190', 'weight': u'11,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Flamajou', u'Avec une Pierre Feu', u'Flamoutan'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,5m'}})
list.update ({u'Flamoutan': {'catch': u'75', 'weight': u'28,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Flamajou', u'Avec une Pierre Feu', u'Flamoutan'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Flotajou': {'catch': u'190', 'weight': u'13,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Flotajou', u'Avec une Pierre Eau', u'Flotoutan'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,6m'}})
list.update ({u'Flotoutan': {'catch': u'75', 'weight': u'29,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Flotajou', u'Avec une Pierre Eau', u'Flotoutan'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Munna': {'catch': u'190', 'weight': u'23,3kg', 'hatch': u'10 cycles - 2805 pas', 'evolutions': [u'Munna', u'Avec une Pierre Lune', u'Mushana'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Sol', 'size': u'0,6m'}})
list.update ({u'Mushana': {'catch': u'75', 'weight': u'60,5kg', 'hatch': u'10 cycles - 2805 pas', 'evolutions': [u'Munna', u'Avec une Pierre Lune', u'Mushana'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Sol', 'size': u'1,1m'}})
list.update ({u'Poichigeon': {'catch': u'255', 'weight': u'2,1kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Poichigeon', u'Niveau 21', u'Colombeau', u'Niveau 32', u'Deflaisan'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Vol', 'size': u'0,3m'}})
list.update ({u'Colombeau': {'catch': u'120', 'weight': u'15,0kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Poichigeon', u'Niveau 21', u'Colombeau', u'Niveau 32', u'Deflaisan'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Vol', 'size': u'0,6m'}})
list.update ({u'Deflaisan': {'catch': u'45', 'weight': u'29,0kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Poichigeon', u'Niveau 21', u'Colombeau', u'Niveau 32', u'Deflaisan'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att.', 'egg': u'Vol', 'size': u'1,2m'}})
list.update ({u'Zebibron': {'catch': u'190', 'weight': u'29,8kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Zebibron', u'Niveau 27', u'Zeblitz'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,8m'}})
list.update ({u'Zeblitz': {'catch': u'75', 'weight': u'79,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Zebibron', u'Niveau 27', u'Zeblitz'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'1,6m'}})
list.update ({u'Nodulithe': {'catch': u'255', 'weight': u'18,0kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Nodulithe', u'Niveau 25', u'Geolithe', u'Echange', u'Gigalithe'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Mineral', 'size': u'0,4m'}})
list.update ({u'Geolithe': {'catch': u'120', 'weight': u'102,0kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Nodulithe', u'Niveau 25', u'Geolithe', u'Echange', u'Gigalithe'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.; +1 Def.', 'egg': u'Mineral', 'size': u'0,9m'}})
list.update ({u'Gigalithe': {'catch': u'45', 'weight': u'260,0kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Nodulithe', u'Niveau 25', u'Geolithe', u'Echange', u'Gigalithe'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att.', 'egg': u'Mineral', 'size': u'1,7m'}})
list.update ({u'Chovsourir': {'catch': u'190', 'weight': u'2,1kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Chovsourir', u'Bonheur', u'Rhinolove'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol/Vol', 'size': u'0,4m'}})
list.update ({u'Rhinolove': {'catch': u'45', 'weight': u'10,5kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Chovsourir', u'Bonheur', u'Rhinolove'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol/Vol', 'size': u'0,9m'}})
list.update ({u'Rototaupe': {'catch': u'120', 'weight': u'8,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Rototaupe', u'Niveau 31', u'Minotaupe'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol', 'size': u'0,3m'}})
list.update ({u'Minotaupe': {'catch': u'60', 'weight': u'40,4kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Rototaupe', u'Niveau 31', u'Minotaupe'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Sol', 'size': u'0,7m'}})
list.update ({u'Nanmeouie': {'catch': u'255', 'weight': u'31,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Fee', 'size': u'1,1m'}})
list.update ({u'Charpenti': {'catch': u'190', 'weight': u'12,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Charpenti', u'Niveau 25', u'Ouvrifier', u'Echange', u'Betochef'], 'gender': u'25% femelle; 75% male', 'ev': u'+1 Att.', 'egg': u'Humanoide', 'size': u'0,6m'}})
list.update ({u'Ouvrifier': {'catch': u'90', 'weight': u'40,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Charpenti', u'Niveau 25', u'Ouvrifier', u'Echange', u'Betochef'], 'gender': u'25% femelle; 75% male', 'ev': u'+2 Att.', 'egg': u'Humanoide', 'size': u'1,2m'}})
list.update ({u'Betochef': {'catch': u'45', 'weight': u'87,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Charpenti', u'Niveau 25', u'Ouvrifier', u'Echange', u'Betochef'], 'gender': u'25% femelle; 75% male', 'ev': u'+3 Att.', 'egg': u'Humanoide', 'size': u'1,4m'}})
list.update ({u'Tritonde': {'catch': u'255', 'weight': u'4,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Tritonde', u'Niveau 25', u'Batracne', u'Niveau 36', u'Crapustule'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Eau 1', 'size': u'0,5m'}})
list.update ({u'Batracne': {'catch': u'120', 'weight': u'17,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Tritonde', u'Niveau 25', u'Batracne', u'Niveau 36', u'Crapustule'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Eau 1', 'size': u'0,8m'}})
list.update ({u'Crapustule': {'catch': u'45', 'weight': u'62,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Tritonde', u'Niveau 25', u'Batracne', u'Niveau 36', u'Crapustule'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 PV', 'egg': u'Eau 1', 'size': u'1,5m'}})
list.update ({u'Judokrak': {'catch': u'45', 'weight': u'55,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [], 'gender': u'0% femelle; 100% male', 'ev': u'+2 PV', 'egg': u'Humanoide', 'size': u'1,3m'}})
list.update ({u'Karaclee': {'catch': u'45', 'weight': u'51,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [], 'gender': u'0% femelle; 100% male', 'ev': u'+2 Att.', 'egg': u'Humanoide', 'size': u'1,4m'}})
list.update ({u'Larveyette': {'catch': u'255', 'weight': u'2,5kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Larveyette', u'Niveau 20', u'Couverdure', u'Bonheur', u'Manternel'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Insecte', 'size': u'0,3m'}})
list.update ({u'Couverdure': {'catch': u'120', 'weight': u'7,3kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Larveyette', u'Niveau 20', u'Couverdure', u'Bonheur', u'Manternel'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Insecte', 'size': u'0,5m'}})
list.update ({u'Manternel': {'catch': u'45', 'weight': u'20,5kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Larveyette', u'Niveau 20', u'Couverdure', u'Bonheur', u'Manternel'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att.', 'egg': u'Insecte', 'size': u'1,2m'}})
list.update ({u'Venipatte': {'catch': u'255', 'weight': u'5,3kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Venipatte', u'Niveau 22', u'Scobolide', u'Niveau 30', u'Brutapode'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Insecte', 'size': u'0,4m'}})
list.update ({u'Scobolide': {'catch': u'120', 'weight': u'58,5kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Venipatte', u'Niveau 22', u'Scobolide', u'Niveau 30', u'Brutapode'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Insecte', 'size': u'1,2m'}})
list.update ({u'Brutapode': {'catch': u'45', 'weight': u'200,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Venipatte', u'Niveau 22', u'Scobolide', u'Niveau 30', u'Brutapode'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Vit.', 'egg': u'Insecte', 'size': u'2,5m'}})
list.update ({u'Doudouvet': {'catch': u'190', 'weight': u'0,6kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Doudouvet', u'Avec une Pierresoleil', u'Farfaduvet'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Plante/Fee', 'size': u'0,3m'}})
list.update ({u'Farfaduvet': {'catch': u'75', 'weight': u'6,6kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Doudouvet', u'Avec une Pierresoleil', u'Farfaduvet'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Plante/Fee', 'size': u'0,7m'}})
list.update ({u'Chlorobule': {'catch': u'190', 'weight': u'6,6kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Chlorobule', u'Avec une Pierresoleil', u'Fragilady'], 'gender': u'100% femelle; 0% male', 'ev': u'+1 Att. Spe', 'egg': u'Plante', 'size': u'0,5m'}})
list.update ({u'Fragilady': {'catch': u'75', 'weight': u'16,3kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Chlorobule', u'Avec une Pierresoleil', u'Fragilady'], 'gender': u'100% femelle; 0% male', 'ev': u'+2 Att. Spe', 'egg': u'Plante', 'size': u'1,1m'}})
list.update ({u'Bargantua': {'catch': u'25', 'weight': u'18,0kg', 'hatch': u'40 cycles - 10455 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Eau 2', 'size': u'1,0m'}})
list.update ({u'Mascaiman': {'catch': u'180', 'weight': u'15,2kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Mascaiman', u'Niveau 29', u'Escroco', u'Niveau 40', u'Crocorible'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol', 'size': u'0,7m'}})
list.update ({u'Escroco': {'catch': u'90', 'weight': u'33,4kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Mascaiman', u'Niveau 29', u'Escroco', u'Niveau 40', u'Crocorible'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Crocorible': {'catch': u'45', 'weight': u'96,3kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Mascaiman', u'Niveau 29', u'Escroco', u'Niveau 40', u'Crocorible'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att.', 'egg': u'Sol', 'size': u'1,5m'}})
list.update ({u'Darumarond': {'catch': u'120', 'weight': u'37,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Darumarond', u'Niveau 35', u'Darumacho'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol', 'size': u'0,6m'}})
list.update ({u'Darumacho (Mode Normal)': {'catch': u'60', 'weight': u'92,9kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Darumarond', u'Niveau 35', u'Darumacho'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att', 'egg': u'Sol', 'size': u'1,3m'}})
list.update ({u'Darumacho (Mode Daruma)': {'catch': u'60', 'weight': u'92,9kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Darumarond', u'Niveau 35', u'Darumacho'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att', 'egg': u'Sol', 'size': u'1,3m'}})
list.update ({u'Maracachi': {'catch': u'255', 'weight': u'28,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Plante', 'size': u'1,0m'}})
list.update ({u'Crabicoque': {'catch': u'190', 'weight': u'14,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Crabicoque', u'Niveau 34', u'Crabaraque'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Insecte/Mineral', 'size': u'0,3m'}})
list.update ({u'Crabaraque': {'catch': u'75', 'weight': u'200,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Crabicoque', u'Niveau 34', u'Crabaraque'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Insecte/Mineral', 'size': u'1,4m'}})
list.update ({u'Baggiguane': {'catch': u'180', 'weight': u'11,8kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Baggiguane', u'Niveau 39', u'Baggaid'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Dragon/Sol', 'size': u'0,6m'}})
list.update ({u'Baggaid': {'catch': u'90', 'weight': u'30,0kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Baggiguane', u'Niveau 39', u'Baggaid'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Sol/Dragon', 'size': u'1,1m'}})
list.update ({u'Cryptero': {'catch': u'45', 'weight': u'14,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Vol', 'size': u'1,4m'}})
list.update ({u'Tutafeh': {'catch': u'190', 'weight': u'1,5kg', 'hatch': u'25 cycles - 6630 pas', 'evolutions': [u'Tutafeh', u'Niveau 34', u'Tutankafer'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Mineral/Indetermine', 'size': u'0,5m'}})
list.update ({u'Tutankafer': {'catch': u'90', 'weight': u'76,5kg', 'hatch': u'25 cycles - 6630 pas', 'evolutions': [u'Tutafeh', u'Niveau 34', u'Tutankafer'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Mineral/Indetermine', 'size': u'1,7m'}})
list.update ({u'Carapagos': {'catch': u'45', 'weight': u'16,5kg', 'hatch': u'30 cycles - 7905 pas', 'evolutions': [u'Carapagos', u'Niveau 37', u'Megapagos'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Def.', 'egg': u'Eau 1/Eau 3', 'size': u'0,7m'}})
list.update ({u'Megapagos': {'catch': u'45', 'weight': u'81,0kg', 'hatch': u'30 cycles - 7905 pas', 'evolutions': [u'Carapagos', u'Niveau 37', u'Megapagos'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Def.', 'egg': u'Eau 1/Eau 3', 'size': u'1,2m'}})
list.update ({u'Arkeapti': {'catch': u'45', 'weight': u'9,5kg', 'hatch': u'30 cycles - 7905 pas', 'evolutions': [u'Arkeapti', u'Niveau 37', u'Aeropteryx'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att.', 'egg': u'Vol', 'size': u'0,6m'}})
list.update ({u'Aeropteryx': {'catch': u'45', 'weight': u'32,0kg', 'hatch': u'30 cycles - 7905 pas', 'evolutions': [u'Arkeapti', u'Niveau 37', u'Aeropteryx'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att.', 'egg': u'Vol/Eau 3', 'size': u'1,4m'}})
list.update ({u'Miamiasme': {'catch': u'190', 'weight': u'31,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Miamiasme', u'Niveau 36', u'Miasmax'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Mineral', 'size': u'0,6m'}})
list.update ({u'Miasmax': {'catch': u'60', 'weight': u'107,3kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Miamiasme', u'Niveau 36', u'Miasmax'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Mineral', 'size': u'1,9m'}})
list.update ({u'Zorua': {'catch': u'75', 'weight': u'12,5kg', 'hatch': u'25 cycles - 6630 pas', 'evolutions': [u'Zorua', u'Niveau 30', u'Zoroark'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att. Spe', 'egg': u'Sol', 'size': u'0,7m'}})
list.update ({u'Zoroark': {'catch': u'45', 'weight': u'81,1kg', 'hatch': u'21 cycles - 5535 pas', 'evolutions': [u'Zorua', u'Niv 30', u'Zoroark'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att. Spe', 'egg': u'Sol', 'size': u'1,6m'}})
list.update ({u'Chinchidou': {'catch': u'255', 'weight': u'5,8kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Chinchidou', u'Avec une Pierre Eclat', u'Pashmilla'], 'gender': u'75% femelle; 25% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,4m'}})
list.update ({u'Pashmilla': {'catch': u'255', 'weight': u'7,5kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Chinchidou', u'Avec une Pierre Eclat', u'Pashmilla'], 'gender': u'75% femelle; 25% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'0,5m'}})
list.update ({u'Scrutella': {'catch': u'200', 'weight': u'5,8kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Scrutella', u'Niveau 32', u'Mesmerella', u'Niveau 41', u'Siderella'], 'gender': u'75% femelle; 25% male', 'ev': u'+1 Def. Spe', 'egg': u'Humanoide', 'size': u'0,4m'}})
list.update ({u'Mesmerella': {'catch': u'100', 'weight': u'18,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Scrutella', u'Niveau 32', u'Mesmerella', u'Niveau 41', u'Siderella'], 'gender': u'75% femelle; 25% male', 'ev': u'+2 Def. Spe', 'egg': u'Humanoide', 'size': u'0,7m'}})
list.update ({u'Siderella': {'catch': u'50', 'weight': u'44kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Scrutella', u'Niveau 32', u'Mesmerella', u'Niveau 41', u'Siderella'], 'gender': u'75% femelle; 25% male', 'ev': u'+3 Att. Spe.', 'egg': u'Humanoide', 'size': u'1,5m'}})
list.update ({u'Nucleos': {'catch': u'200', 'weight': u'1,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Nucleos', u'Niveau 32', u'Meios', u'Niveau 41', u'Symbios'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Indetermine', 'size': u'0,3m'}})
list.update ({u'Meios': {'catch': u'100', 'weight': u'8,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Nucleos', u'Niveau 32', u'Meios', u'Niveau 41', u'Symbios'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Indetermine', 'size': u'0,6m'}})
list.update ({u'Symbios': {'catch': u'50', 'weight': u'20,1kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Nucleos', u'Niveau 32', u'Meios', u'Niveau 41', u'Symbios'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att. Spe', 'egg': u'Indetermine', 'size': u'1,0m'}})
list.update ({u'Couaneton': {'catch': u'190', 'weight': u'5,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Couaneton', u'Niveau 35', u'Lakmecygne'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Eau 1/Vol', 'size': u'0,5m'}})
list.update ({u'Lakmecygne': {'catch': u'45', 'weight': u'24,2kg', 'hatch': u'30 cycles - 7905 pas', 'evolutions': [u'Couaneton', u'Niveau 35', u'Lakmecygne'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Eau 1/Vol', 'size': u'1,3m'}})
list.update ({u'Sorbebe': {'catch': u'255', 'weight': u'5,7kg', 'hatch': u'13 cycles - 3533 pas', 'evolutions': [u'Sorbebe', u'Niveau 35', u'Sorboul', u'Niveau 47', u'Sorbouboul'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Mineral', 'size': u'0,4m'}})
list.update ({u'Sorboul': {'catch': u'120', 'weight': u'41,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Sorbebe', u'Niveau 35', u'Sorboul', u'Niveau 47', u'Sorbouboul'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Mineral', 'size': u'1,1m'}})
list.update ({u'Sorbouboul': {'catch': u'45', 'weight': u'57,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Sorbebe', u'Niveau 35', u'Sorboul', u'Niveau 47', u'Sorbouboul'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att. Spe', 'egg': u'Mineral', 'size': u'1,5m'}})
list.update ({u'Vivaldaim': {'catch': u'190', 'weight': u'19,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Vivaldaim', u'Niveau 34', u'Haydaim'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,6m'}})
list.update ({u'Haydaim': {'catch': u'75', 'weight': u'92,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Vivaldaim', u'Niveau 34', u'Haydaim'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Sol', 'size': u'1,9m'}})
list.update ({u'Emolga': {'catch': u'200', 'weight': u'5,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'0,4m'}})
list.update ({u'Carabing': {'catch': u'200', 'weight': u'5,9kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Carabing', u'Echange avec Escargaume', u'Lancargot'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Insecte', 'size': u'0,5m'}})
list.update ({u'Lancargot': {'catch': u'75', 'weight': u'33,0kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Carabing', u'Echange avec Escargaume', u'Lancargot'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Insecte', 'size': u'1,0m'}})
list.update ({u'Trompignon': {'catch': u'190', 'weight': u'1,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Trompignon', u'Niveau 39', u'Gaulet'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Plante', 'size': u'0,2m'}})
list.update ({u'Gaulet': {'catch': u'75', 'weight': u'10,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Trompignon', u'Niveau 39', u'Gaulet'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Plante', 'size': u'0,6m'}})
list.update ({u'Viskuse': {'catch': u'190', 'weight': u'33,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Viskuse', u'Niveau 40', u'Moyade'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Indetermine', 'size': u'1,2m'}})
list.update ({u'Moyade': {'catch': u'60', 'weight': u'135,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Viskuse', u'Niveau 40', u'Moyade'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def. Spe', 'egg': u'Indetermine', 'size': u'2,2m'}})
list.update ({u'Mamanbo': {'catch': u'75', 'weight': u'31,6kg', 'hatch': u'40 cycles - 10455 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Eau 1/Eau 2', 'size': u'1,2m'}})
list.update ({u'Statitik': {'catch': u'190', 'weight': u'0,6kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Statitik', u'Niveau 36', u'Mygavolt'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Insecte', 'size': u'0,1m'}})
list.update ({u'Mygavolt': {'catch': u'75', 'weight': u'14,3kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Statitik', u'Niveau 36', u'Mygavolt'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Insecte', 'size': u'0,8m'}})
list.update ({u'Grindur': {'catch': u'255', 'weight': u'18,8kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Grindur', u'Niveau 40', u'Noacier'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Plante/Mineral', 'size': u'0,6m'}})
list.update ({u'Noacier': {'catch': u'90', 'weight': u'110kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Grindur', u'Niveau 40', u'Noacier'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Plante/Mineral', 'size': u'1,0m'}})
list.update ({u'Tic': {'catch': u'130', 'weight': u'21,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Tic', u'Niveau 38', u'Clic', u'Niveau 49', u'Cliticlic'], 'gender': u'Asexue', 'ev': u'+1 Def', 'egg': u'Mineral', 'size': u'0,3m'}})
list.update ({u'Clic': {'catch': u'60', 'weight': u'51,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Tic', u'Niveau 38', u'Clic', u'Niveau 49', u'Cliticlic'], 'gender': u'Asexue', 'ev': u'+2 Def0', 'egg': u'Mineral', 'size': u'0,6m'}})
list.update ({u'Cliticlic': {'catch': u'30', 'weight': u'81,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Tic', u'Niveau 38', u'Clic', u'Niveau 49', u'Cliticlic'], 'gender': u'Asexue', 'ev': u'+3 Def.', 'egg': u'Mineral', 'size': u'0,6m'}})
list.update ({u'Anchwatt': {'catch': u'190', 'weight': u'0,3kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Anchwatt', u'Niveau 39', u'Lamperoie', u'Avec une Pierre Foudre', u'Ohmassacre'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Indetermine', 'size': u'0,2m'}})
list.update ({u'Lamperoie': {'catch': u'60', 'weight': u'22,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Anchwatt', u'Niveau 39', u'Lamperoie', u'Avec une Pierre Foudre', u'Ohmassacre'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Indetermine', 'size': u'1,2m'}})
list.update ({u'Ohmassacre': {'catch': u'30', 'weight': u'80,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Anchwatt', u'Niveau 39', u'Lamperoie', u'Avec une Pierre Foudre', u'Ohmassacre'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att.', 'egg': u'Indetermine', 'size': u'2,1m'}})
list.update ({u'Lewsor': {'catch': u'255', 'weight': u'9,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Lewsor', u'Niveau 42', u'Neitram'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Humanoide', 'size': u'0,5m'}})
list.update ({u'Neitram': {'catch': u'90', 'weight': u'34,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Lewsor', u'Niveau 42', u'Neitram'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Humanoide', 'size': u'1,0m'}})
list.update ({u'Funecire': {'catch': u'190', 'weight': u'3,1kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Funecire', u'Niveau 41', u'Melancolux', u'Avec une Pierre Nuit', u'Lugulabre'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Indetermine', 'size': u'0,3m'}})
list.update ({u'Melancolux': {'catch': u'190', 'weight': u'13,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Funecire', u'Niveau 41', u'Melancolux', u'Avec une Pierre Nuit', u'Lugulabre'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Indetermine', 'size': u'0,6m'}})
list.update ({u'Lugulabre': {'catch': u'45', 'weight': u'34,3kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Funecire', u'Niveau 41', u'Melancolux', u'Avec une Pierre Nuit', u'Lugulabre'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att. Spe', 'egg': u'Indetermine', 'size': u'1,0m'}})
list.update ({u'Coupenotte': {'catch': u'75', 'weight': u'18,0kg', 'hatch': u'40 cycles - 10455 pas', 'evolutions': [u'Coupenotte', u'Niveau 38', u'Incisache', u'Niveau 48', u'Tranchodon'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Monstre/Dragon', 'size': u'0,6m'}})
list.update ({u'Incisache': {'catch': u'60', 'weight': u'36,0kg', 'hatch': u'40 cycles - 10455 pas', 'evolutions': [u'Coupenotte', u'Niveau 38', u'Incisache', u'Niveau 48', u'Tranchodon'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Monstre/Dragon', 'size': u'1,0m'}})
list.update ({u'Tranchodon': {'catch': u'45', 'weight': u'105,5kg', 'hatch': u'40 cycles - 10455 pas', 'evolutions': [u'Coupenotte', u'Niveau 38', u'Incisache', u'Niveau 48', u'Tranchodon'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att.', 'egg': u'Monstre/Dragon', 'size': u'1,8m'}})
list.update ({u'Polarhume': {'catch': u'120', 'weight': u'8,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Polarhume', u'Niveau 37', u'Polagriffe'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol', 'size': u'0,5m'}})
list.update ({u'Polagriffe': {'catch': u'60', 'weight': u'260,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Polarhume', u'Niveau 37', u'Polagriffe'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Sol', 'size': u'2,6m'}})
list.update ({u'Hexagel': {'catch': u'25', 'weight': u'148,0kg', 'hatch': u'25 cycles - 6630 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+2 Def. Spe', 'egg': u'Mineral', 'size': u'1,1m'}})
list.update ({u'Escargaume': {'catch': u'200', 'weight': u'7,7kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Escargaume', u'Echange avec Carabing', u'Limaspeed'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Insecte', 'size': u'0,4m'}})
list.update ({u'Limaspeed': {'catch': u'75', 'weight': u'23,5kg', 'hatch': u'15 cycles - 4080 pas', 'evolutions': [u'Escargaume', u'Echange avec Carabing', u'Limaspeed'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Insecte', 'size': u'0,8m'}})
list.update ({u'Limonde': {'catch': u'75', 'weight': u'11,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Eau 1/Indetermine', 'size': u'0,7m'}})
list.update ({u'Kungfouine': {'catch': u'180', 'weight': u'20,0kg', 'hatch': u'25 cycles - 6630 pas', 'evolutions': [u'Kungfouine', u'Niveau 50', u'Shaofouine'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol/Humanoide', 'size': u'0,8m'}})
list.update ({u'Shaofouine': {'catch': u'45', 'weight': u'35,5kg', 'hatch': u'25 cycles - 6630 pas', 'evolutions': [u'Kungfouine', u'Niveau 50', u'Shaofouine'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Sol/Humanoide', 'size': u'1,4m'}})
list.update ({u'Drakkarmin': {'catch': u'45', 'weight': u'139,0kg', 'hatch': u'30 cycles - 7905 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Dragon/Monstre', 'size': u'1,6m'}})
list.update ({u'Gringolem': {'catch': u'190', 'weight': u'92,0kg', 'hatch': u'25 cycles - 6630 pas', 'evolutions': [u'Gringolem', u'Niveau 43', u'Golemastoc'], 'gender': u'Asexue', 'ev': u'+1 Att.', 'egg': u'Mineral', 'size': u'1,0m'}})
list.update ({u'Golemastoc': {'catch': u'90', 'weight': u'330,0kg', 'hatch': u'25 cycles - 6630 pas', 'evolutions': [u'Gringolem', u'Niveau 43', u'Golemastoc'], 'gender': u'Asexue', 'ev': u'+2 Att.', 'egg': u'Mineral', 'size': u'2,8m'}})
list.update ({u'Scalpion': {'catch': u'120', 'weight': u'10,2kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Scalpion', u'Niveau 52', u'Scalproie'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Humanoide', 'size': u'0,5m'}})
list.update ({u'Scalproie': {'catch': u'45', 'weight': u'70,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Scalpion', u'Niveau 52', u'Scalproie'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Humanoide', 'size': u'1,6m'}})
list.update ({u'Frison': {'catch': u'45', 'weight': u'94,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Sol', 'size': u'1,6m'}})
list.update ({u'Furaiglon': {'catch': u'190', 'weight': u'10,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Furaiglon', u'Niveau 54', u'Gueriaigle'], 'gender': u'0% femelle; 100% male', 'ev': u'+1 Att.', 'egg': u'Vol', 'size': u'0,5m'}})
list.update ({u'Gueriaigle': {'catch': u'60', 'weight': u'41kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Furaiglon', u'Niveau 54', u'Gueriaigle'], 'gender': u'0% femelle; 100% male', 'ev': u'+2 Att.', 'egg': u'Vol', 'size': u'1,5m'}})
list.update ({u'Vostourno': {'catch': u'190', 'weight': u'9,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Vostourno', u'Niveau 54', u'Vaututrice'], 'gender': u'100% femelle; 0% male', 'ev': u'+1 Def.', 'egg': u'Vol', 'size': u'0,5m'}})
list.update ({u'Vaututrice': {'catch': u'60', 'weight': u'39,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Vostourno', u'Niveau 54', u'Vaututrice'], 'gender': u'100% femelle; 0% male', 'ev': u'+2 Vit.', 'egg': u'Vol', 'size': u'1,2m'}})
list.update ({u'Aflamanoir': {'catch': u'90', 'weight': u'58,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att Spe.', 'egg': u'Sol', 'size': u'1,4m'}})
list.update ({u'Fermite': {'catch': u'90', 'weight': u'33,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Insecte', 'size': u'0,3m'}})
list.update ({u'Solochi': {'catch': u'45', 'weight': u'17,3kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Solochi', u'Niveau 50', u'Diamat', u'Niveau 64', u'Trioxhydre'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Dragon', 'size': u'0,8m'}})
list.update ({u'Diamat': {'catch': u'190', 'weight': u'50,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [u'Solochi', u'Niveau 50', u'Diamat', u'Niveau 64', u'Trioxhydre'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Dragon', 'size': u'1,4m'}})
list.update ({u'Trioxhydre': {'catch': u'30', 'weight': u'160,0kg', 'hatch': u'40 cycles - 10455 pas', 'evolutions': [u'Solochi', u'Niveau 50', u'Diamat', u'Niveau 64', u'Trioxhydre'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att. Spe', 'egg': u'Dragon', 'size': u'1,8m'}})
list.update ({u'Pyronille': {'catch': u'45', 'weight': u'28,8kg', 'hatch': u'40 cycles - 10455 pas', 'evolutions': [u'Pyronille', u'Niveau 59', u'Pyrax'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Insecte', 'size': u'1,1m'}})
list.update ({u'Pyrax': {'catch': u'15', 'weight': u'46kg', 'hatch': u'39 cycles - 10240 pas', 'evolutions': [u'Pyronille', u'Niveau 59', u'Pyrax'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Att. Spe', 'egg': u'Insecte', 'size': u'1,6m'}})
list.update ({u'Cobaltium': {'catch': u'3', 'weight': u'250kg', 'hatch': u'80 cycles - 20655 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Def.', 'egg': u'Sans oeuf', 'size': u'2,1m'}})
list.update ({u'Terrakium': {'catch': u'3', 'weight': u'260kg', 'hatch': u'80 cycles - 20655 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Att.', 'egg': u'Sans oeuf', 'size': u'1,9m'}})
list.update ({u'Viridium': {'catch': u'5', 'weight': u'200,0kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Def. Spe', 'egg': u'Sans oeuf', 'size': u'2,0m'}})
list.update ({u'Boreas (Forme Avatar)': {'catch': u'3', 'weight': u'63,0kg', 'hatch': u'120 cycles - 30855 pas', 'evolutions': [], 'gender': u'0% femelle; 100% male', 'ev': u'+3 Att. Spe', 'egg': u'Sans oeuf', 'size': u'1,5m'}})
list.update ({u'Boreas (Forme Totemique)': {'catch': u'3', 'weight': u'63,0kg', 'hatch': u'120 cycles - 30855 pas', 'evolutions': [], 'gender': u'0% femelle; 100% male', 'ev': u'+3 Att. Spe', 'egg': u'Sans oeuf', 'size': u'1,5m'}})
list.update ({u'Fulguris (Forme Avatar)': {'catch': u'3', 'weight': u'65kg', 'hatch': u'120 cycles - 30855 pas', 'evolutions': [], 'gender': u'0% femelle; 100% male', 'ev': u'+3 Att. Spe', 'egg': u'Sans oeuf', 'size': u'1,5m'}})
list.update ({u'Fulguris (Forme Totemique)': {'catch': u'3', 'weight': u'65kg', 'hatch': u'120 cycles - 30855 pas', 'evolutions': [], 'gender': u'0% femelle; 100% male', 'ev': u'+3 Att. Spe', 'egg': u'Sans oeuf', 'size': u'1,5m'}})
list.update ({u'Reshiram': {'catch': u'45', 'weight': u'330kg', 'hatch': u'120 cycles - 30855 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Att. Spe', 'egg': u'Sans oeuf', 'size': u'3,2m'}})
list.update ({u'Zekrom': {'catch': u'45', 'weight': u'345kg', 'hatch': u'120 cycles - 30855 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 Att.', 'egg': u'Sans oeuf', 'size': u'2,9m'}})
list.update ({u'Demeteros (Forme Avatar)': {'catch': u'3', 'weight': u'68,0kg', 'hatch': u'120 cycles - 30855 pas', 'evolutions': [], 'gender': u'0% femelle; 100% male', 'ev': u'+3 Att.', 'egg': u'Sans oeuf', 'size': u'1,5m'}})
list.update ({u'Demeteros (Forme Totemique)': {'catch': u'3', 'weight': u'68,0kg', 'hatch': u'120 cycles - 30855 pas', 'evolutions': [], 'gender': u'0% femelle; 100% male', 'ev': u'+3 Att.', 'egg': u'Sans oeuf', 'size': u'1,5m'}})
list.update ({u'Kyurem Noir': {'catch': u'3', 'weight': u'325kg', 'hatch': u'120 cycles - 30855 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 PV; +1 Att.; +1 Def. Spe', 'egg': u'Sans oeuf', 'size': u'3,0m'}})
list.update ({u'Kyurem Blanc': {'catch': u'3', 'weight': u'325kg', 'hatch': u'120 cycles - 30855 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 PV; +1 Att.; +1 Def. Spe', 'egg': u'Sans oeuf', 'size': u'3,0m'}})
list.update ({u'Keldeo': {'catch': u'3', 'weight': u'48,5kg', 'hatch': u'80 cycles - 20655 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att. Spe; +1 Def. Spe; +1 Vit.', 'egg': u'Sans oeuf', 'size': u'1,4m'}})
list.update ({u'Meloetta (Forme Voix)': {'catch': u'5', 'weight': u'6,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att. Spe; +1 Def. Spe; +1 Vit.', 'egg': u'Sans oeuf', 'size': u'0,6m'}})
list.update ({u'Meloetta (Forme Danse)': {'catch': u'5', 'weight': u'6,5kg', 'hatch': u'20 cycles - 5355 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att. Spe; +1 Def. Spe; +1 Vit.', 'egg': u'Sans oeuf', 'size': u'0,6m'}})
list.update ({u'Genesect': {'catch': u'3', 'weight': u'82,5kg', 'hatch': u'120 cycles - 30855 pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Att.; +1 Att. Spe; +1 Vit.', 'egg': u'Sans oeuf', 'size': u'1,5m'}})
list.update ({u'Marisson': {'catch': u'45', 'weight': u'9,0kg', 'hatch': u'pas', 'evolutions': [u'Marisson', u'Niveau 16', u'Boguerisse', u'Niveau 36', u'Blindepique'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Def.', 'egg': u'Sol', 'size': u'0,4m'}})
list.update ({u'Boguerisse': {'catch': u'45', 'weight': u'29,0kg', 'hatch': u'pas', 'evolutions': [u'Marisson', u'Niveau 16', u'Boguerisse', u'Niveau 36', u'Blindepique'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Def.', 'egg': u'Sol', 'size': u'0,7m'}})
list.update ({u'Blindepique': {'catch': u'45', 'weight': u'90,0kg', 'hatch': u'pas', 'evolutions': [u'Marisson', u'Niveau 16', u'Boguerisse', u'Niveau 36', u'Blindepique'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+3 Def.', 'egg': u'Sol', 'size': u'1,6m'}})
list.update ({u'Feunnec': {'catch': u'45', 'weight': u'9,4kg', 'hatch': u'pas', 'evolutions': [u'Feunnec', u'Niveau 16', u'Roussil', u'Niveau 36', u'Goupelin'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att. Spe', 'egg': u'Sol', 'size': u'0,4m'}})
list.update ({u'Roussil': {'catch': u'45', 'weight': u'14,5kg', 'hatch': u'pas', 'evolutions': [u'Feunnec', u'Niveau 16', u'Roussil', u'Niveau 36', u'Goupelin'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att. Spe', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Goupelin': {'catch': u'45', 'weight': u'39,0kg', 'hatch': u'pas', 'evolutions': [u'Feunnec', u'Niveau 16', u'Roussil', u'Niveau 36', u'Goupelin'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+3 Att. Spe', 'egg': u'Sol', 'size': u'1,5m'}})
list.update ({u'Grenousse': {'catch': u'45', 'weight': u'7,0kg', 'hatch': u'pas', 'evolutions': [u'Grenousse', u'Niveau 16', u'Croaporal', u'Niveau 36', u'Amphinobi'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Vit.', 'egg': u'Eau 1', 'size': u'0,3m'}})
list.update ({u'Croaporal': {'catch': u'45', 'weight': u'10,9kg', 'hatch': u'pas', 'evolutions': [u'Grenousse', u'Niveau 16', u'Croaporal', u'Niveau 36', u'Amphinobi'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Vit.', 'egg': u'Eau 1', 'size': u'0,6m'}})
list.update ({u'Amphinobi': {'catch': u'45', 'weight': u'40,0kg', 'hatch': u'pas', 'evolutions': [u'Grenousse', u'Niveau 16', u'Croaporal', u'Niveau 36', u'Amphinobi'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+3 Vit.', 'egg': u'Eau 1', 'size': u'1,5m'}})
list.update ({u'Sapereau': {'catch': u'', 'weight': u'5,0kg', 'hatch': u'pas', 'evolutions': [u'Sapereau', u'Niveau 20', u'Excavarenne'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,4m'}})
list.update ({u'Excavarenne': {'catch': u'5', 'weight': u'42,4kg', 'hatch': u'pas', 'evolutions': [u'Sapereau', u'Niveau 20', u'Excavarenne'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Passerouge': {'catch': u'', 'weight': u'1,7kg', 'hatch': u'pas', 'evolutions': [u'Passerouge', u'Niveau 17', u'Braisillon', u'Niveau 35', u'Flambusard'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Vol', 'size': u'0,3m'}})
list.update ({u'Braisillon': {'catch': u'', 'weight': u'16,0kg', 'hatch': u'pas', 'evolutions': [u'Passerouge', u'Niveau 17', u'Braisillon', u'Niveau 35', u'Flambusard'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Vol', 'size': u'0,7m'}})
list.update ({u'Flambusard': {'catch': u'', 'weight': u'24,5kg', 'hatch': u'pas', 'evolutions': [u'Passerouge', u'Niveau 17', u'Braisillon', u'Niveau 35', u'Flambusard'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Vit.', 'egg': u'Vol', 'size': u'1,2m'}})
list.update ({u'Lepidonille': {'catch': u'', 'weight': u'2,5kg', 'hatch': u'pas', 'evolutions': [u'Lepidonille', u'Niveau 9', u'Peregrain', u'Niveau 12', u'Prismillon'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Insecte', 'size': u'0,3m'}})
list.update ({u'Peregrain': {'catch': u'', 'weight': u'8,4kg', 'hatch': u'pas', 'evolutions': [u'Lepidonille', u'Niveau 9', u'Peregrain', u'Niveau 12', u'Prismillon'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Insecte', 'size': u'0,3m'}})
list.update ({u'Prismillon': {'catch': u'', 'weight': u'17,0kg', 'hatch': u'pas', 'evolutions': [u'Lepidonille', u'Niveau 9', u'Peregrain', u'Niveau 12', u'Prismillon'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 PV.; +1 Att. Spe; +1 Vit.', 'egg': u'', 'size': u'1,2m'}})
list.update ({u'Helionceau': {'catch': u'', 'weight': u'13,5kg', 'hatch': u'pas', 'evolutions': [u'Helionceau', u'Niveau 35', u'Nemelios'], 'gender': u'75% femelle; 25% male', 'ev': u'+1 Att. Spe', 'egg': u'Sol', 'size': u'0,6m'}})
list.update ({u'Nemelios': {'catch': u'', 'weight': u'81,5kg', 'hatch': u'pas', 'evolutions': [u'Helionceau', u'Niveau 35', u'Nemelios'], 'gender': u'75% femelle; 25% male', 'ev': u'+2 Att. Spe', 'egg': u'Sol', 'size': u'1,5m'}})
list.update ({u'Flabebe': {'catch': u'', 'weight': u'0,1kg', 'hatch': u'pas', 'evolutions': [u'Flabebe', u'Niveau 19', u'Floette', u'Avec une Pierre Eclat', u'Florges'], 'gender': u'100% femelle; 0% male', 'ev': u'+1 Def. Spe', 'egg': u'Fee', 'size': u'0,1m'}})
list.update ({u'Floette': {'catch': u'', 'weight': u'0,9kg', 'hatch': u'pas', 'evolutions': [u'Flabebe', u'Niveau 19', u'Floette', u'Avec une Pierre Eclat', u'Florges'], 'gender': u'100% femelle; 0% male', 'ev': u'+2 Def. Spe', 'egg': u'Fee', 'size': u'0,2m'}})
list.update ({u'Florges': {'catch': u'', 'weight': u'10,0kg', 'hatch': u'pas', 'evolutions': [u'Flabebe', u'Niveau 19', u'Floette', u'Avec une Pierre Eclat', u'Florges'], 'gender': u'100% femelle; 0% male', 'ev': u'+3 Def. Spe', 'egg': u'Fee', 'size': u'1,1m'}})
list.update ({u'Cabriolaine': {'catch': u'', 'weight': u'31,0kg', 'hatch': u'pas', 'evolutions': [u'Cabriolaine', u'Niveau 32', u'Chevroum'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Sol', 'size': u'0,9m'}})
list.update ({u'Chevroum': {'catch': u'', 'weight': u'91,0kg', 'hatch': u'pas', 'evolutions': [u'Cabriolaine', u'Niveau 32', u'Chevroum'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Sol', 'size': u'1,7m'}})
list.update ({u'Pandespiegle': {'catch': u'', 'weight': u'8,0kg', 'hatch': u'pas', 'evolutions': [u'Pandespiegle', u"Niveau 32, en ayant un Pokemon dans l'equipe", u'Pandarbare'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Sol/Humanoide', 'size': u'0,6m'}})
list.update ({u'Pandarbare': {'catch': u'', 'weight': u'136,0kg', 'hatch': u'pas', 'evolutions': [u'Pandespiegle', u"Niveau 32, avec un Pokemon dans l'equipe", u'Pandarbare'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Sol/Humanoide', 'size': u'2,1m'}})
list.update ({u'Couafarel': {'catch': u'', 'weight': u'28,0kg', 'hatch': u'pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Sol/Humanoide', 'size': u'1,2m'}})
list.update ({u'Psystigri': {'catch': u'', 'weight': u'3,5kg', 'hatch': u'pas', 'evolutions': [u'Psystigri', u'Niveau 25', u'Mistigrix'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Sol', 'size': u'0,3m'}})
list.update ({u'Mistigrix': {'catch': u'', 'weight': u'8,5kg', 'hatch': u'pas', 'evolutions': [u'Psystigri', u'Niveau 25', u'Mistigrix'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol', 'size': u'0,6m'}})
list.update ({u'Monorpale': {'catch': u'', 'weight': u'2,0kg', 'hatch': u'pas', 'evolutions': [u'Monorpale', u'Niveau 35', u'Dimocles', u'Avec une Pierre Nuit', u'Exagide (Forme Parade)'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Mineral', 'size': u'0,8m'}})
list.update ({u'Dimocles': {'catch': u'', 'weight': u'4,5kg', 'hatch': u'pas', 'evolutions': [u'Monorpale', u'Niveau 35', u'Dimocles', u'Avec une Pierre Nuit', u'Exagide (Forme Parade)'], 'gender': u'50% femelle; 50% male', 'ev': u'', 'egg': u'Mineral', 'size': u'0,8m'}})
list.update ({u'Exagide (Forme Assaut)': {'catch': u'', 'weight': u'53,0kg', 'hatch': u'18 cycles - 4845 pas', 'evolutions': [u'Monorpale', u'Niveau 35', u'Dimocles', u'Avec une Pierre Nuit', u'Exagide (Forme Assaut)'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.; +1 Def. Spe', 'egg': u'Mineral', 'size': u'1,7m'}})
list.update ({u'Exagide (Forme Parade)': {'catch': u'', 'weight': u'53,0kg', 'hatch': u'18 cycles - 4845 pas', 'evolutions': [u'Monorpale', u'Niveau 35', u'Dimocles', u'Avec une Pierre Nuit', u'Exagide (Forme Parade)'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.; +1 Def. Spe', 'egg': u'Mineral', 'size': u'1,7m'}})
list.update ({u'Fluvetin': {'catch': u'', 'weight': u'0,5kg', 'hatch': u'pas', 'evolutions': [u'Fluvetin', u'Echange en tenant Sachet Senteur', u'Cocotine'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 PV', 'egg': u'Fee', 'size': u'0,2m'}})
list.update ({u'Cocotine': {'catch': u'', 'weight': u'15,5kg', 'hatch': u'pas', 'evolutions': [u'Fluvetin', u'Echange en tenant Sachet Senteur', u'Cocotine'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 PV', 'egg': u'Fee', 'size': u'0,8m'}})
list.update ({u'Sucroquin': {'catch': u'', 'weight': u'3,5kg', 'hatch': u'pas', 'evolutions': [u'Sucroquin', u'Echange en tenant Chantibonbon', u'Cupcanaille'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Fee', 'size': u'0,4m'}})
list.update ({u'Cupcanaille': {'catch': u'', 'weight': u'5,0kg', 'hatch': u'pas', 'evolutions': [u'Sucroquin', u'Echange en tenant Chantibonbon', u'Cupcanaille'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Fee', 'size': u'0,8m'}})
list.update ({u'Sepiatop': {'catch': u'', 'weight': u'3,5kg', 'hatch': u'pas', 'evolutions': [u'Sepiatop', u'Niveau 30, en retournant la 3DS', u'Sepiatroce'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Eau 1/Eau 2', 'size': u'0,4m'}})
list.update ({u'Sepiatroce': {'catch': u'', 'weight': u'47,0kg', 'hatch': u'pas', 'evolutions': [u'Sepiatop', u'Niveau 30, en retournant la 3DS', u'Sepiatroce'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Eau 1/Eau 2', 'size': u'1,5m'}})
list.update ({u'Opermine': {'catch': u'', 'weight': u'31,0kg', 'hatch': u'pas', 'evolutions': [u'Opermine', u'Niveau 39', u'Golgopathe'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Eau 3', 'size': u'0,5m'}})
list.update ({u'Golgopathe': {'catch': u'', 'weight': u'96,0kg', 'hatch': u'pas', 'evolutions': [u'Opermine', u'Niveau 39', u'Golgopathe'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Eau 3/Eau 1', 'size': u'1,3m'}})
list.update ({u'Venalgue': {'catch': u'', 'weight': u'7,3kg', 'hatch': u'pas', 'evolutions': [u'Venalgue', u'Niveau 48', u'Kravarech'], 'gender': u'Repartition inconnue', 'ev': u'+1 Def. Spe', 'egg': u'Eau 1/Dragon', 'size': u'0,5m'}})
list.update ({u'Kravarech': {'catch': u'', 'weight': u'81,5kg', 'hatch': u'pas', 'evolutions': [u'Venalgue', u'Niveau 48', u'Kravarech'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def. Spe', 'egg': u'Eau 1/Dragon', 'size': u'1,8m'}})
list.update ({u'Flingouste': {'catch': u'', 'weight': u'8,3kg', 'hatch': u'pas', 'evolutions': [u'Flingouste', u'Niveau 37', u'Gamblast'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att. Spe', 'egg': u'Eau 1/Eau 3', 'size': u'0,5m'}})
list.update ({u'Gamblast': {'catch': u'', 'weight': u'35,3kg', 'hatch': u'pas', 'evolutions': [u'Flingouste', u'Niveau 37', u'Gamblast'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att. Spe', 'egg': u'Eau 1/Eau 3', 'size': u'1,3m'}})
list.update ({u'Galvaran': {'catch': u'', 'weight': u'6,0kg', 'hatch': u'pas', 'evolutions': [u'Galvaran', u'Avec une Pierresoleil', u'Iguolta'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Monstre/Dragon', 'size': u'0,5m'}})
list.update ({u'Iguolta': {'catch': u'', 'weight': u'21,0kg', 'hatch': u'pas', 'evolutions': [u'Galvaran', u'Avec une Pierresoleil', u'Iguolta'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Monstre/Dragon', 'size': u'1,0m'}})
list.update ({u'Ptyranidur': {'catch': u'', 'weight': u'26,0kg', 'hatch': u'pas', 'evolutions': [u'Ptyranidur', u'Niveau 39 pendant la journee', u'Rexillius'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 Att.', 'egg': u'', 'size': u'0,8m'}})
list.update ({u'Rexillius': {'catch': u'', 'weight': u'270,0kg', 'hatch': u'pas', 'evolutions': [u'Ptyranidur', u'Niveau 39 pendant la journee', u'Rexillius'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Att.', 'egg': u'', 'size': u'2,5m'}})
list.update ({u'Amagara': {'catch': u'45', 'weight': u'25,2kg', 'hatch': u'pas', 'evolutions': [u'Amagara', u'Niveau 39 pendant la nuit', u'Dragmara'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+1 PV', 'egg': u'', 'size': u'1,3m'}})
list.update ({u'Dragmara': {'catch': u'45', 'weight': u'225,0kg', 'hatch': u'pas', 'evolutions': [u'Amagara', u'Niveau 39 pendant la nuit', u'Dragmara'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 PV', 'egg': u'Monstre', 'size': u'2,7m'}})
list.update ({u'Nymphali': {'catch': u'45', 'weight': u'23,5kg', 'hatch': u'34 cycles - 8960 pas', 'evolutions': [u'Evoli', u'Avec une Pierre Eau', u'Avec une Pierre Foudre', u'Avec une Pierre Feu', u'Bonheur , Jour', u'Bonheur , Nuit', u"Pres d'une Pierre Mousse + gagne un niveau", u"Pres d'une Pierre Glacee + gagne un niveau", u"2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], 'gender': u'12.5% femelle; 87.5% male', 'ev': u'+2 Def. Spe', 'egg': u'Sol', 'size': u'1,0m'}})
list.update ({u'Brutalibre': {'catch': u'', 'weight': u'21,5kg', 'hatch': u'pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Humanoide', 'size': u'0,8m'}})
list.update ({u'Dedenne': {'catch': u'', 'weight': u'2,2kg', 'hatch': u'pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Sol/Fee', 'size': u'0,2m'}})
list.update ({u'Strassie': {'catch': u'', 'weight': u'5,7kg', 'hatch': u'pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+1 Def.; +1 Def. Spe', 'egg': u'Fee/Mineral', 'size': u'0,3m'}})
list.update ({u'Mucuscule': {'catch': u'', 'weight': u'2,8kg', 'hatch': u'pas', 'evolutions': [u'Mucuscule', u'Niveau 40', u'Colimucus', u'Niveau 50, quand il pleut', u'Muplodocus'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def. Spe', 'egg': u'Dragon', 'size': u'0,3m'}})
list.update ({u'Colimucus': {'catch': u'', 'weight': u'17,5kg', 'hatch': u'pas', 'evolutions': [u'Mucuscule', u'Niveau 40', u'Colimucus', u'Niveau 50, quand il pleut', u'Muplodocus'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def. Spe', 'egg': u'Dragon', 'size': u'0,8m'}})
list.update ({u'Muplodocus': {'catch': u'', 'weight': u'150,5kg', 'hatch': u'pas', 'evolutions': [u'Mucuscule', u'Niveau 40', u'Colimucus', u'Niveau 50, quand il pleut', u'Muplodocus'], 'gender': u'50% femelle; 50% male', 'ev': u'+3 Def. Spe', 'egg': u'Dragon', 'size': u'2,0m'}})
list.update ({u'Trousselin': {'catch': u'', 'weight': u'3,0kg', 'hatch': u'pas', 'evolutions': [], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Mineral', 'size': u'0,2m'}})
list.update ({u'Brocelome': {'catch': u'', 'weight': u'7,0kg', 'hatch': u'pas', 'evolutions': [u'Brocelome', u'Echange', u'Desseliande'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Att.', 'egg': u'Plante/Indetermine', 'size': u'0,4m'}})
list.update ({u'Desseliande': {'catch': u'', 'weight': u'71kg', 'hatch': u'pas', 'evolutions': [u'Brocelome', u'Echange', u'Desseliande'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Att.', 'egg': u'Plante/Indetermine', 'size': u'1,5m'}})
list.update ({u'Pitrouille (Taille Mini)': {'catch': u'', 'weight': u'3,5kg', 'hatch': u'pas', 'evolutions': [u'Pitrouille (Taille Mini)', u'Echange', u'Banshitrouye (Taille Mini)'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Indetermine', 'size': u'0,3m'}})
list.update ({u'Pitrouille (Taille Normale)': {'catch': u'', 'weight': u'3,5kg', 'hatch': u'pas', 'evolutions': [u'Pitrouille (Taille Normale)', u'Echange', u'Banshitrouye (Taille Normale)'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Indetermine', 'size': u'0,3m'}})
list.update ({u'Pitrouille (Taille Maxi)': {'catch': u'', 'weight': u'3,5kg', 'hatch': u'pas', 'evolutions': [u'Pitrouille (Taille Maxi)', u'Echange', u'Banshitrouye (Taille Maxi)'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Indetermine', 'size': u'0,3m'}})
list.update ({u'Pitrouille (Taille Ultra)': {'catch': u'', 'weight': u'3,5kg', 'hatch': u'pas', 'evolutions': [u'Pitrouille (Taille Ultra)', u'Echange', u'Banshitrouye (Taille Ultra)'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Indetermine', 'size': u'0,3m'}})
list.update ({u'Banshitrouye (Taille Mini)': {'catch': u'', 'weight': u'9,5kg', 'hatch': u'pas', 'evolutions': [u'Pitrouille (Taille Mini)', u'Echange', u'Banshitrouye (Taille Mini)'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Indetermine', 'size': u'0,7m'}})
list.update ({u'Banshitrouye (Taille Normale)': {'catch': u'', 'weight': u'9,5kg', 'hatch': u'pas', 'evolutions': [u'Pitrouille (Taille Normale)', u'Echange', u'Banshitrouye (Taille Normale)'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Indetermine', 'size': u'0,7m'}})
list.update ({u'Banshitrouye (Taille Maxi)': {'catch': u'', 'weight': u'9,5kg', 'hatch': u'pas', 'evolutions': [u'Pitrouille (Taille Maxi)', u'Echange', u'Banshitrouye (Taille Maxi)'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Indetermine', 'size': u'0,7m'}})
list.update ({u'Banshitrouye (Taille Ultra)': {'catch': u'', 'weight': u'9,5kg', 'hatch': u'pas', 'evolutions': [u'Pitrouille (Taille Ultra)', u'Echange', u'Banshitrouye (Taille Ultra)'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Indetermine', 'size': u'0,7m'}})
list.update ({u'Grelacon': {'catch': u'', 'weight': u'99,5kg', 'hatch': u'pas', 'evolutions': [u'Grelacon', u'Niveau 37', u'Seracrawl'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Def.', 'egg': u'Monstre', 'size': u'1,0m'}})
list.update ({u'Seracrawl': {'catch': u'', 'weight': u'505,0kg', 'hatch': u'pas', 'evolutions': [u'Grelacon', u'Niveau 37', u'Seracrawl'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Def.', 'egg': u'Monstre', 'size': u'2,0m'}})
list.update ({u'Sonistrelle': {'catch': u'', 'weight': u'8,0kg', 'hatch': u'pas', 'evolutions': [u'Sonistrelle', u'Niveau 48', u'Bruyverne'], 'gender': u'50% femelle; 50% male', 'ev': u'+1 Vit.', 'egg': u'Vol', 'size': u'0,5m'}})
list.update ({u'Bruyverne': {'catch': u'', 'weight': u'85,0kg', 'hatch': u'pas', 'evolutions': [u'Sonistrelle', u'Niveau 48', u'Bruyverne'], 'gender': u'50% femelle; 50% male', 'ev': u'+2 Vit.', 'egg': u'Vol', 'size': u'1,5m'}})
list.update ({u'Xerneas': {'catch': u'30', 'weight': u'215,0kg', 'hatch': u'pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 PV', 'egg': u'Sans oeuf', 'size': u'3,0m'}})
list.update ({u'Yveltal': {'catch': u'30', 'weight': u'203,0kg', 'hatch': u'pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 PV', 'egg': u'Sans oeuf', 'size': u'5,8m'}})
list.update ({u'Zygarde': {'catch': u'', 'weight': u'305,0kg', 'hatch': u'pas', 'evolutions': [], 'gender': u'Asexue', 'ev': u'+3 PV', 'egg': u'Sans oeuf', 'size': u'5,0m'}})

main(list, name_match)

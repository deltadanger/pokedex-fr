import urllib, unicodedata, string
from HTMLParser import HTMLParser

HOME_URL = "http://www.pokepedia.fr"
BASE_URL = "http://www.pokepedia.fr/index.php/Liste_des_Pok%C3%A9mon_par_statistiques_de_base"

def main(pkList, evoList):
    text = ""
    
    for name in pkList:
        evos = []
        for evolutions in evoList:
            if name in evolutions:
                for evo in evolutions:
                    evos.append('PokemonList.perName.get("{}")'.format(evo))
        
        text += '        PokemonList.perName.get("{}").evolutions = new Pokemon[]{{'.format(name) + ','.join(evos) + '};\n'
    
    print text
    
    
    
def buildList():
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
            self.inLink = True
            
            resp = urllib.urlopen(HOME_URL + getAttr(attrs, "href"))
            p = PokemonParser()
            p.feed(resp.read().decode("utf-8"))
            print p.data
            self.data.append(p.data)
        
    def handle_endtag(self, tag):
        if self.inLink and tag == "a":
            self.inLink = False
        
        if self.inTd and tag == "td":
            self.inTd = False
            
        if self.inTr and tag == "tr":
            self.inTr = False
        
        if tag == "table":
            self.inTable = False
    
    
class PokemonParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        
        self.data = []
        
        self.inH3 = False
        self.getTable = False
        self.inTable = False
        self.row = 0
        self.inTd = False
        self.getContent = False
        self.getContentIfEquals = ""
    
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
            self.row += 1
        
        if self.inTable and tag == "td":
            self.inTd = True
        
        if self.inTd and tag == "strong":
            self.getContent = True
        
        if self.inTd and tag == "a" and self.row%2 == 0:
            self.getContentIfEquals = getAttr(attrs, "title")
        
    def handle_endtag(self, tag):
        if tag == "a":
            self.getContentIfEquals = ""
        
        if tag == "strong":
            self.getContent = False
        
        if tag == "td":
            self.inTd = False
        
        if tag == "table":
            self.getTable = False
            self.inTable = False
            self.row = 0
        
        if tag == "h3":
            self.inH3 = False
    
    def handle_data(self, data):
        if self.getContent:
            self.data.append(data)
        
        if self.getContentIfEquals and data == self.getContentIfEquals:
            self.data.append(data)
        


#~ [u'Bulbizarre', u'Herbizarre', u'Florizarre', u'Mega-Florizarre']
#~ [u'Bulbizarre', u'Herbizarre', u'Florizarre', u'Mega-Florizarre']
#~ [u'Bulbizarre', u'Herbizarre', u'Florizarre', u'Mega-Florizarre']
#~ [u'Bulbizarre', u'Herbizarre', u'Florizarre', u'Mega-Florizarre']
#~ [u'Salameche', u'Reptincel', u'Dracaufeu', u'Mega-Dracaufeu X', u'Mega-Dracaufeu Y']
#~ [u'Salameche', u'Reptincel', u'Dracaufeu', u'Mega-Dracaufeu X', u'Mega-Dracaufeu Y']
#~ [u'Salameche', u'Reptincel', u'Dracaufeu', u'Mega-Dracaufeu X', u'Mega-Dracaufeu Y']
#~ [u'Salameche', u'Reptincel', u'Dracaufeu', u'Mega-Dracaufeu X', u'Mega-Dracaufeu Y']
#~ [u'Salameche', u'Reptincel', u'Dracaufeu', u'Mega-Dracaufeu X', u'Mega-Dracaufeu Y']
#~ [u'Carapuce', u'Carabaffe', u'Tortank', u'Mega-Tortank']
#~ [u'Carapuce', u'Carabaffe', u'Tortank', u'Mega-Tortank']
#~ [u'Carapuce', u'Carabaffe', u'Tortank', u'Mega-Tortank']
#~ [u'Carapuce', u'Carabaffe', u'Tortank', u'Mega-Tortank']
#~ [u'Chenipan', u'Chrysacier', u'Papilusion']
#~ [u'Chenipan', u'Chrysacier', u'Papilusion']
#~ [u'Chenipan', u'Chrysacier', u'Papilusion']
#~ [u'Aspicot', u'Coconfort', u'Dardargnan']
#~ [u'Aspicot', u'Coconfort', u'Dardargnan']
#~ [u'Aspicot', u'Coconfort', u'Dardargnan']
#~ [u'Roucool', u'Roucoups', u'Roucarnage']
#~ [u'Roucool', u'Roucoups', u'Roucarnage']
#~ [u'Roucool', u'Roucoups', u'Roucarnage']
#~ [u'Rattata', u'Rattatac']
#~ [u'Rattata', u'Rattatac']
#~ [u'Piafabec', u'Rapasdepic']
#~ [u'Piafabec', u'Rapasdepic']
#~ [u'Abo', u'Arbok']
#~ [u'Abo', u'Arbok']
#~ [u'Pichu', u'Pikachu', u'Raichu']
#~ [u'Pichu', u'Pikachu', u'Raichu']
#~ [u'Sabelette', u'Sablaireau']
#~ [u'Sabelette', u'Sablaireau']
#~ [u'Nidoran F', u'Nidorina', u'Nidoqueen']
#~ [u'Nidoran F', u'Nidorina', u'Nidoqueen']
#~ [u'Nidoran F', u'Nidorina', u'Nidoqueen']
#~ [u'Nidoran M', u'Nidorino', u'Nidoking']
#~ [u'Nidoran M', u'Nidorino', u'Nidoking']
#~ [u'Nidoran M', u'Nidorino', u'Nidoking']
#~ [u'Melo', u'Melofee', u'Melodelfe']
#~ [u'Melo', u'Melofee', u'Melodelfe']
#~ [u'Goupix', u'Feunard']
#~ [u'Goupix', u'Feunard']
#~ [u'Toudoudou', u'Rondoudou', u'Grodoudou']
#~ [u'Toudoudou', u'Rondoudou', u'Grodoudou']
#~ [u'Nosferapti', u'Nosferalto', u'Nostenfer']
#~ [u'Nosferapti', u'Nosferalto', u'Nostenfer']
#~ [u'Mystherbe', u'Ortide', u'Rafflesia', u'Joliflor']
#~ [u'Mystherbe', u'Ortide', u'Rafflesia', u'Joliflor']
#~ [u'Mystherbe', u'Ortide', u'Rafflesia', u'Joliflor']
#~ [u'Paras', u'Parasect']
#~ [u'Paras', u'Parasect']
#~ [u'Mimitoss', u'Aeromite']
#~ [u'Mimitoss', u'Aeromite']
#~ [u'Taupiqueur', u'Triopikeur']
#~ [u'Taupiqueur', u'Triopikeur']
#~ [u'Miaouss', u'Persian']
#~ [u'Miaouss', u'Persian']
#~ [u'Psykokwak', u'Akwakwak']
#~ [u'Psykokwak', u'Akwakwak']
#~ [u'Ferosinge', u'Colossinge']
#~ [u'Ferosinge', u'Colossinge']
#~ [u'Caninos', u'Arcanin']
#~ [u'Caninos', u'Arcanin']
#~ [u'Ptitard', u'Tetarte', u'Tartard', u'Tarpaud']
#~ [u'Ptitard', u'Tetarte', u'Tartard', u'Tarpaud']
#~ [u'Ptitard', u'Tetarte', u'Tartard', u'Tarpaud']
#~ [u'Abra', u'Kadabra', u'Alakazam', u'Mega-Alakazam']
#~ [u'Abra', u'Kadabra', u'Alakazam', u'Mega-Alakazam']
#~ [u'Abra', u'Kadabra', u'Alakazam', u'Mega-Alakazam']
#~ [u'Abra', u'Kadabra', u'Alakazam', u'Mega-Alakazam']
#~ [u'Machoc', u'Machopeur', u'Mackogneur']
#~ [u'Machoc', u'Machopeur', u'Mackogneur']
#~ [u'Machoc', u'Machopeur', u'Mackogneur']
#~ [u'Chetiflor', u'Boustiflor', u'Empiflor']
#~ [u'Chetiflor', u'Boustiflor', u'Empiflor']
#~ [u'Chetiflor', u'Boustiflor', u'Empiflor']
#~ [u'Tentacool', u'Tentacruel']
#~ [u'Tentacool', u'Tentacruel']
#~ [u'Racaillou', u'Gravalanch', u'Grolem']
#~ [u'Racaillou', u'Gravalanch', u'Grolem']
#~ [u'Racaillou', u'Gravalanch', u'Grolem']
#~ [u'Ponyta', u'Galopa']
#~ [u'Ponyta', u'Galopa']
#~ [u'Ramoloss', u'Flagadoss', u'Roigada']
#~ [u'Ramoloss', u'Flagadoss', u'Roigada']
#~ [u'Magneti', u'Magneton', u'Magnezone']
#~ [u'Magneti', u'Magneton', u'Magnezone']
#~ []
#~ [u'Doduo', u'Dodrio']
#~ [u'Doduo', u'Dodrio']
#~ [u'Otaria', u'Lamantine']
#~ [u'Otaria', u'Lamantine']
#~ [u'Tadmorv', u'Grotadmorv']
#~ [u'Tadmorv', u'Grotadmorv']
#~ [u'Kokiyas', u'Crustabri']
#~ [u'Kokiyas', u'Crustabri']
#~ [u'Fantominus', u'Spectrum', u'Ectoplasma', u'Mega-Ectoplasma']
#~ [u'Fantominus', u'Spectrum', u'Ectoplasma', u'Mega-Ectoplasma']
#~ [u'Fantominus', u'Spectrum', u'Ectoplasma', u'Mega-Ectoplasma']
#~ [u'Fantominus', u'Spectrum', u'Ectoplasma', u'Mega-Ectoplasma']
#~ [u'Onix', u'Steelix']
#~ [u'Soporifik', u'Hypnomade']
#~ [u'Soporifik', u'Hypnomade']
#~ [u'Krabby', u'Krabboss']
#~ [u'Krabby', u'Krabboss']
#~ [u'Voltorbe', u'Electrode']
#~ [u'Voltorbe', u'Electrode']
#~ [u'Noeunoeuf', u'Noadkoko']
#~ [u'Noeunoeuf', u'Noadkoko']
#~ [u'Osselait', u'Ossatueur']
#~ [u'Osselait', u'Ossatueur']
#~ [u'Debugant', u'Kicklee', u'Tygnon', u'Kapoera']
#~ [u'Debugant', u'Kicklee', u'Tygnon', u'Kapoera']
#~ [u'Excelangue', u'Coudlangue']
#~ [u'Smogo', u'Smogogo']
#~ [u'Smogo', u'Smogogo']
#~ [u'Rhinocorne', u'Rhinoferos', u'Rhinastoc']
#~ [u'Rhinocorne', u'Rhinoferos', u'Rhinastoc']
#~ [u'Ptiravi', u'Leveinard', u'Leuphorie']
#~ [u'Saquedeneu', u'Bouldeneu']
#~ [u'Kangourex', u'Mega-Kangourex']
#~ [u'Kangourex', u'Mega-Kangourex']
#~ [u'Hypotrempe', u'Hypocean', u'Hyporoi']
#~ [u'Hypotrempe', u'Hypocean', u'Hyporoi']
#~ [u'Poissirene', u'Poissoroy']
#~ [u'Poissirene', u'Poissoroy']
#~ []
#~ []
#~ [u'Mime Jr.', u'M. Mime']
#~ [u'Insecateur', u'Cizayox', u'Mega-Cizayox']
#~ [u'Lippouti', u'Lippoutou']
#~ [u'Elekid', u'Elektek', u'Elekable']
#~ [u'Magby', u'Magmar', u'Maganon']
#~ [u'Scarabrute', u'Mega-Scarabrute']
#~ [u'Scarabrute', u'Mega-Scarabrute']
#~ []
#~ [u'Magicarpe', u'Leviator', u'Mega-Leviator']
#~ [u'Magicarpe', u'Leviator', u'Mega-Leviator']
#~ [u'Magicarpe', u'Leviator', u'Mega-Leviator']
#~ []
#~ []
#~ [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali']
#~ [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali']
#~ [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali']
#~ [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali']
#~ [u'Porygon', u'Porygon2', u'Porygon-Z']
#~ [u'Amonita', u'Amonistar']
#~ [u'Amonita', u'Amonistar']
#~ [u'Kabuto', u'Kabutops']
#~ [u'Kabuto', u'Kabutops']
#~ [u'Ptera', u'Mega-Ptera']
#~ [u'Goinfrex', u'Ronflex']
#~ []
#~ []
#~ []
#~ [u'Minidraco', u'Draco', u'Dracolosse']
#~ [u'Minidraco', u'Draco', u'Dracolosse']
#~ [u'Minidraco', u'Draco', u'Dracolosse']
#~ [u'Mewtwo', u'Mega-Mewtwo X', u'Mega-Mewtwo Y']
#~ [u'Mewtwo', u'Mega-Mewtwo X', u'Mega-Mewtwo Y']
#~ [u'Mewtwo', u'Mega-Mewtwo X', u'Mega-Mewtwo Y']
#~ []
#~ [u'Germignon', u'Macronium', u'Meganium']
#~ [u'Germignon', u'Macronium', u'Meganium']
#~ [u'Germignon', u'Macronium', u'Meganium']
#~ [u'Hericendre', u'Feurisson', u'Typhlosion']
#~ [u'Hericendre', u'Feurisson', u'Typhlosion']
#~ [u'Hericendre', u'Feurisson', u'Typhlosion']
#~ [u'Kaiminus', u'Crocrodil', u'Aligatueur']
#~ [u'Kaiminus', u'Crocrodil', u'Aligatueur']
#~ [u'Kaiminus', u'Crocrodil', u'Aligatueur']
#~ [u'Fouinette', u'Fouinar']
#~ [u'Fouinette', u'Fouinar']
#~ [u'Hoot-hoot', u'Noarfang']
#~ [u'Hoot-hoot', u'Noarfang']
#~ [u'Coxy', u'Coxyclaque']
#~ [u'Coxy', u'Coxyclaque']
#~ [u'Mimigal', u'Migalos']
#~ [u'Mimigal', u'Migalos']
#~ [u'Nosferapti', u'Nosferalto', u'Nostenfer']
#~ [u'Loupio', u'Lanturn']
#~ [u'Loupio', u'Lanturn']
#~ [u'Pichu', u'Pikachu', u'Raichu']
#~ [u'Melo', u'Melofee', u'Melodelfe']
#~ [u'Toudoudou', u'Rondoudou', u'Grodoudou']
#~ [u'Togepi', u'Togetic', u'Togekiss']
#~ [u'Togepi', u'Togetic', u'Togekiss']
#~ [u'Natu', u'Xatu']
#~ [u'Natu', u'Xatu']
#~ [u'Wattouat', u'Lainergie', u'Pharamp', u'Mega-Pharamp']
#~ [u'Wattouat', u'Lainergie', u'Pharamp', u'Mega-Pharamp']
#~ [u'Wattouat', u'Lainergie', u'Pharamp', u'Mega-Pharamp']
#~ [u'Wattouat', u'Lainergie', u'Pharamp', u'Mega-Pharamp']
#~ [u'Mystherbe', u'Ortide', u'Rafflesia', u'Joliflor']
#~ [u'Azurill', u'Marill', u'Azumarill']
#~ [u'Azurill', u'Marill', u'Azumarill']
#~ [u'Manzai', u'Simularbre']
#~ [u'Ptitard', u'Tetarte', u'Tartard', u'Tarpaud']
#~ [u'Granivol', u'Floravol', u'Cotovol']
#~ [u'Granivol', u'Floravol', u'Cotovol']
#~ [u'Granivol', u'Floravol', u'Cotovol']
#~ [u'Capumain', u'Capidextre']
#~ [u'Tournegrin', u'Heliatronc']
#~ [u'Tournegrin', u'Heliatronc']
#~ [u'Yanma', u'Yanmega']
#~ [u'Axoloto', u'Maraiste']
#~ [u'Axoloto', u'Maraiste']
#~ [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali']
#~ [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali']
#~ [u'Cornebre', u'Corboss']
#~ [u'Ramoloss', u'Flagadoss', u'Roigada']
#~ [u'Feuforeve', u'Magireve']
#~ []
#~ [u'Okeoke', u'Qulbutoke']
#~ []
#~ [u'Pomdepik', u'Foretress']
#~ [u'Pomdepik', u'Foretress']
#~ []
#~ [u'Scorplane', u'Scorvol']
#~ [u'Onix', u'Steelix']
#~ [u'Snubbull', u'Granbull']
#~ [u'Snubbull', u'Granbull']
#~ []
#~ [u'Insecateur', u'Cizayox', u'Mega-Cizayox']
#~ [u'Insecateur', u'Cizayox', u'Mega-Cizayox']
#~ []
#~ [u'Scarhino', u'Mega-Scarhino']
#~ [u'Scarhino', u'Mega-Scarhino']
#~ [u'Farfuret', u'Dimoret']
#~ [u'Teddiursa', u'Ursaring']
#~ [u'Teddiursa', u'Ursaring']
#~ [u'Limagma', u'Volcaropod']
#~ [u'Limagma', u'Volcaropod']
#~ [u'Marcacrin', u'Cochignon', u'Mammochon']
#~ [u'Marcacrin', u'Cochignon', u'Mammochon']
#~ []
#~ [u'Remoraid', u'Octillery']
#~ [u'Remoraid', u'Octillery']
#~ []
#~ [u'Babimanta', u'Demanta']
#~ []
#~ [u'Malosse', u'Demolosse', u'Mega-Demolosse']
#~ [u'Malosse', u'Demolosse', u'Mega-Demolosse']
#~ [u'Malosse', u'Demolosse', u'Mega-Demolosse']
#~ [u'Hypotrempe', u'Hypocean', u'Hyporoi']
#~ [u'Phanpy', u'Donphan']
#~ [u'Phanpy', u'Donphan']
#~ [u'Porygon', u'Porygon2', u'Porygon-Z']
#~ []
#~ []
#~ [u'Debugant', u'Kicklee', u'Tygnon', u'Kapoera']
#~ [u'Debugant', u'Kicklee', u'Tygnon', u'Kapoera']
#~ [u'Lippouti', u'Lippoutou']
#~ [u'Elekid', u'Elektek', u'Elekable']
#~ [u'Magby', u'Magmar', u'Maganon']
#~ []
#~ [u'Ptiravi', u'Leveinard', u'Leuphorie']
#~ []
#~ []
#~ []
#~ [u'Embrylex', u'Ymphect', u'Tyranocif', u'Mega-Tyranocif']
#~ [u'Embrylex', u'Ymphect', u'Tyranocif', u'Mega-Tyranocif']
#~ [u'Embrylex', u'Ymphect', u'Tyranocif', u'Mega-Tyranocif']
#~ [u'Embrylex', u'Ymphect', u'Tyranocif', u'Mega-Tyranocif']
#~ []
#~ []
#~ []
#~ [u'Arcko', u'Massko', u'Jungko']
#~ [u'Arcko', u'Massko', u'Jungko']
#~ [u'Arcko', u'Massko', u'Jungko']
#~ [u'Poussifeu', u'Galifeu', u'Brasegali', u'Mega-Brasegali']
#~ [u'Poussifeu', u'Galifeu', u'Brasegali', u'Mega-Brasegali']
#~ [u'Poussifeu', u'Galifeu', u'Brasegali', u'Mega-Brasegali']
#~ [u'Poussifeu', u'Galifeu', u'Brasegali', u'Mega-Brasegali']
#~ [u'Gobou', u'Flobio', u'Laggron']
#~ [u'Gobou', u'Flobio', u'Laggron']
#~ [u'Gobou', u'Flobio', u'Laggron']
#~ [u'Medhyena', u'Grahyena']
#~ [u'Medhyena', u'Grahyena']
#~ [u'Zigzaton', u'Lineon']
#~ [u'Zigzaton', u'Lineon']
#~ [u'Chenipotte', u'Armulys', u'Blindalys', u'Charmillon', u'Papinox']
#~ [u'Chenipotte', u'Armulys', u'Blindalys', u'Charmillon', u'Papinox']
#~ [u'Chenipotte', u'Armulys', u'Blindalys', u'Charmillon', u'Papinox']
#~ [u'Chenipotte', u'Armulys', u'Blindalys', u'Charmillon', u'Papinox']
#~ [u'Chenipotte', u'Armulys', u'Blindalys', u'Charmillon', u'Papinox']
#~ [u'Nenupiot', u'Lombre', u'Ludicolo']
#~ [u'Nenupiot', u'Lombre', u'Ludicolo']
#~ [u'Nenupiot', u'Lombre', u'Ludicolo']
#~ [u'Grainipiot', u'Pifeuil', u'Tengalice']
#~ [u'Grainipiot', u'Pifeuil', u'Tengalice']
#~ [u'Grainipiot', u'Pifeuil', u'Tengalice']
#~ [u'Nirondelle', u'Heledelle']
#~ [u'Nirondelle', u'Heledelle']
#~ [u'Goelise', u'Bekipan']
#~ [u'Goelise', u'Bekipan']
#~ [u'Tarsal', u'Kirlia', u'Gardevoir', u'Gallame', u'Mega-Gardevoir']
#~ [u'Tarsal', u'Kirlia', u'Gardevoir', u'Gallame', u'Mega-Gardevoir']
#~ [u'Tarsal', u'Kirlia', u'Gardevoir', u'Gallame', u'Mega-Gardevoir']
#~ [u'Tarsal', u'Kirlia', u'Gardevoir', u'Gallame', u'Mega-Gardevoir']
#~ [u'Arakdo', u'Maskadra']
#~ [u'Arakdo', u'Maskadra']
#~ [u'Balignon', u'Chapignon']
#~ [u'Balignon', u'Chapignon']
#~ [u'Parecool', u'Vigoroth', u'Monaflemit']
#~ [u'Parecool', u'Vigoroth', u'Monaflemit']
#~ [u'Parecool', u'Vigoroth', u'Monaflemit']
#~ [u'Ningale', u'Ninjask', u'Munja']
#~ [u'Ningale', u'Ninjask', u'Munja']
#~ [u'Ningale', u'Ninjask', u'Munja']
#~ [u'Chuchmur', u'Ramboum', u'Brouhabam']
#~ [u'Chuchmur', u'Ramboum', u'Brouhabam']
#~ [u'Chuchmur', u'Ramboum', u'Brouhabam']
#~ [u'Makuhita', u'Hariyama']
#~ [u'Makuhita', u'Hariyama']
#~ [u'Azurill', u'Marill', u'Azumarill']
#~ [u'Tarinor', u'Tarinorme']
#~ [u'Skitty', u'Delcatty']
#~ [u'Skitty', u'Delcatty']
#~ []
#~ [u'Mysdibule', u'Mega-Mysdibule']
#~ [u'Mysdibule', u'Mega-Mysdibule']
#~ [u'Galekid', u'Galegon', u'Galeking', u'Mega-Galeking']
#~ [u'Galekid', u'Galegon', u'Galeking', u'Mega-Galeking']
#~ [u'Galekid', u'Galegon', u'Galeking', u'Mega-Galeking']
#~ [u'Galekid', u'Galegon', u'Galeking', u'Mega-Galeking']
#~ [u'Meditikka', u'Charmina', u'Mega-Charmina']
#~ [u'Meditikka', u'Charmina', u'Mega-Charmina']
#~ [u'Meditikka', u'Charmina', u'Mega-Charmina']
#~ [u'Dynavolt', u'Elecsprint', u'Mega-Elecsprint']
#~ [u'Dynavolt', u'Elecsprint', u'Mega-Elecsprint']
#~ [u'Dynavolt', u'Elecsprint', u'Mega-Elecsprint']
#~ []
#~ []
#~ []
#~ []
#~ [u'Rozbouton', u'Roselia', u'Roserade']
#~ [u'Gloupti', u'Avaltout']
#~ [u'Gloupti', u'Avaltout']
#~ [u'Carvanha', u'Sharpedo']
#~ [u'Carvanha', u'Sharpedo']
#~ [u'Wailmer', u'Wailord']
#~ [u'Wailmer', u'Wailord']
#~ [u'Chamallot', u'Camerupt']
#~ [u'Chamallot', u'Camerupt']
#~ []
#~ [u'Spoink', u'Groret']
#~ [u'Spoink', u'Groret']
#~ []
#~ [u'Kraknoix', u'Vibraninf', u'Libegon']
#~ [u'Kraknoix', u'Vibraninf', u'Libegon']
#~ [u'Kraknoix', u'Vibraninf', u'Libegon']
#~ [u'Cacnea', u'Cacturne']
#~ [u'Cacnea', u'Cacturne']
#~ [u'Tylton', u'Altaria']
#~ [u'Tylton', u'Altaria']
#~ []
#~ []
#~ []
#~ []
#~ [u'Barloche', u'Barbicha']
#~ [u'Barloche', u'Barbicha']
#~ [u'Ecrapince', u'Colhomard']
#~ [u'Ecrapince', u'Colhomard']
#~ [u'Balbuto', u'Kaorine']
#~ [u'Balbuto', u'Kaorine']
#~ [u'Lilia', u'Vacilys']
#~ [u'Lilia', u'Vacilys']
#~ [u'Anorith', u'Armaldo']
#~ [u'Anorith', u'Armaldo']
#~ [u'Barpau', u'Milobellus']
#~ [u'Barpau', u'Milobellus']
#~ []
#~ []
#~ [u'Polichombr', u'Branette', u'Mega-Branette']
#~ [u'Polichombr', u'Branette', u'Mega-Branette']
#~ [u'Polichombr', u'Branette', u'Mega-Branette']
#~ [u'Skelenox', u'Teraclope', u'Noctunoir']
#~ [u'Skelenox', u'Teraclope', u'Noctunoir']
#~ []
#~ [u'Korillon', u'Eoko']
#~ [u'Absol', u'Mega-Absol']
#~ [u'Absol', u'Mega-Absol']
#~ [u'Okeoke', u'Qulbutoke']
#~ [u'Stalgamin', u'Oniglali', u'Momartik']
#~ [u'Stalgamin', u'Oniglali', u'Momartik']
#~ [u'Obalie', u'Phogleur', u'Kaimorse']
#~ [u'Obalie', u'Phogleur', u'Kaimorse']
#~ [u'Obalie', u'Phogleur', u'Kaimorse']
#~ [u'Coquiperl', u'Serpang', u'Rosabyss']
#~ [u'Coquiperl', u'Serpang', u'Rosabyss']
#~ [u'Coquiperl', u'Serpang', u'Rosabyss']
#~ []
#~ []
#~ [u'Draby', u'Drackhaus', u'Drattak']
#~ [u'Draby', u'Drackhaus', u'Drattak']
#~ [u'Draby', u'Drackhaus', u'Drattak']
#~ [u'Terhal', u'Metang', u'Metalosse']
#~ [u'Terhal', u'Metang', u'Metalosse']
#~ [u'Terhal', u'Metang', u'Metalosse']
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ [u'Tortipouss', u'Boskara', u'Torterra']
#~ [u'Tortipouss', u'Boskara', u'Torterra']
#~ [u'Tortipouss', u'Boskara', u'Torterra']
#~ [u'Ouisticram', u'Chimpenfeu', u'Simiabraz']
#~ [u'Ouisticram', u'Chimpenfeu', u'Simiabraz']
#~ [u'Ouisticram', u'Chimpenfeu', u'Simiabraz']
#~ [u'Tiplouf', u'Prinplouf', u'Pingoleon']
#~ [u'Tiplouf', u'Prinplouf', u'Pingoleon']
#~ [u'Tiplouf', u'Prinplouf', u'Pingoleon']
#~ [u'Etourmi', u'Etourvol', u'Etouraptor']
#~ [u'Etourmi', u'Etourvol', u'Etouraptor']
#~ [u'Etourmi', u'Etourvol', u'Etouraptor']
#~ [u'Keunotor', u'Castorno']
#~ [u'Keunotor', u'Castorno']
#~ [u'Crikzik', u'Melokrik']
#~ [u'Crikzik', u'Melokrik']
#~ [u'Lixy', u'Luxio', u'Luxray']
#~ [u'Lixy', u'Luxio', u'Luxray']
#~ [u'Lixy', u'Luxio', u'Luxray']
#~ [u'Rozbouton', u'Roselia', u'Roserade']
#~ [u'Rozbouton', u'Roselia', u'Roserade']
#~ [u'Kranidos', u'Charkos']
#~ [u'Kranidos', u'Charkos']
#~ [u'Dinoclier', u'Bastiodon']
#~ [u'Dinoclier', u'Bastiodon']
#~ [u'Cheniti', u'Cheniselle', u'Papilord']
#~ [u'Cheniti', u'Cheniselle', u'Papilord']
#~ [u'Cheniti', u'Cheniselle', u'Papilord']
#~ [u'Cheniti', u'Cheniselle', u'Papilord']
#~ [u'Cheniti', u'Cheniselle', u'Papilord']
#~ [u'Apitrini', u'Apireine']
#~ [u'Apitrini', u'Apireine']
#~ []
#~ [u'Mustebouee', u'Musteflott']
#~ [u'Mustebouee', u'Musteflott']
#~ [u'Ceribou', u'Ceriflor']
#~ [u'Ceribou', u'Ceriflor']
#~ [u'Sancoki', u'Tritosor']
#~ [u'Sancoki', u'Tritosor']
#~ [u'Capumain', u'Capidextre']
#~ [u'Baudrive', u'Grodrive']
#~ [u'Baudrive', u'Grodrive']
#~ [u'Laporeille', u'Lockpin']
#~ [u'Laporeille', u'Lockpin']
#~ [u'Feuforeve', u'Magireve']
#~ [u'Cornebre', u'Corboss']
#~ [u'Chaglam', u'Chaffreux']
#~ [u'Chaglam', u'Chaffreux']
#~ [u'Korillon', u'Eoko']
#~ [u'Moufouette', u'Moufflair']
#~ [u'Moufouette', u'Moufflair']
#~ [u'Archeomire', u'Archeodong']
#~ [u'Archeomire', u'Archeodong']
#~ [u'Manzai', u'Simularbre']
#~ [u'Mime Jr.', u'M. Mime']
#~ [u'Ptiravi', u'Leveinard', u'Leuphorie']
#~ []
#~ []
#~ [u'Griknot', u'Carmache', u'Carchacrok', u'Mega-Carchacrok']
#~ [u'Griknot', u'Carmache', u'Carchacrok', u'Mega-Carchacrok']
#~ [u'Griknot', u'Carmache', u'Carchacrok', u'Mega-Carchacrok']
#~ [u'Griknot', u'Carmache', u'Carchacrok', u'Mega-Carchacrok']
#~ [u'Goinfrex', u'Ronflex']
#~ [u'Riolu', u'Lucario', u'Mega-Lucario']
#~ [u'Riolu', u'Lucario', u'Mega-Lucario']
#~ [u'Riolu', u'Lucario', u'Mega-Lucario']
#~ [u'Hippopotas', u'Hippodocus']
#~ [u'Hippopotas', u'Hippodocus']
#~ [u'Rapion', u'Drascore']
#~ [u'Rapion', u'Drascore']
#~ [u'Cradopaud', u'Coatox']
#~ [u'Cradopaud', u'Coatox']
#~ []
#~ [u'Ecayon', u'Lumineon']
#~ [u'Ecayon', u'Lumineon']
#~ [u'Babimanta', u'Demanta']
#~ [u'Blizzi', u'Blizzaroi', u'Mega-Blizzaroi']
#~ [u'Blizzi', u'Blizzaroi', u'Mega-Blizzaroi']
#~ [u'Blizzi', u'Blizzaroi', u'Mega-Blizzaroi']
#~ [u'Farfuret', u'Dimoret']
#~ [u'Magneti', u'Magneton', u'Magnezone']
#~ [u'Excelangue', u'Coudlangue']
#~ [u'Rhinocorne', u'Rhinoferos', u'Rhinastoc']
#~ [u'Saquedeneu', u'Bouldeneu']
#~ [u'Elekid', u'Elektek', u'Elekable']
#~ [u'Magby', u'Magmar', u'Maganon']
#~ [u'Togepi', u'Togetic', u'Togekiss']
#~ [u'Yanma', u'Yanmega']
#~ [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali']
#~ [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali']
#~ [u'Scorplane', u'Scorvol']
#~ [u'Marcacrin', u'Cochignon', u'Mammochon']
#~ [u'Porygon', u'Porygon2', u'Porygon-Z']
#~ [u'Tarsal', u'Kirlia', u'Gardevoir', u'Gallame', u'Mega-Gardevoir']
#~ [u'Tarinor', u'Tarinorme']
#~ [u'Skelenox', u'Teraclope', u'Noctunoir']
#~ [u'Stalgamin', u'Oniglali', u'Momartik']
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ [u'Vipelierre', u'Lianaja', u'Majaspic']
#~ [u'Vipelierre', u'Lianaja', u'Majaspic']
#~ [u'Vipelierre', u'Lianaja', u'Majaspic']
#~ [u'Gruikui', u'Grotichon', u'Roitiflam']
#~ [u'Gruikui', u'Grotichon', u'Roitiflam']
#~ [u'Gruikui', u'Grotichon', u'Roitiflam']
#~ [u'Moustillon', u'Mateloutre', u'Clamiral']
#~ [u'Moustillon', u'Mateloutre', u'Clamiral']
#~ [u'Moustillon', u'Mateloutre', u'Clamiral']
#~ [u'Ratentif', u'Miradar']
#~ [u'Ratentif', u'Miradar']
#~ [u'Ponchiot', u'Ponchien', u'Mastouffe']
#~ [u'Ponchiot', u'Ponchien', u'Mastouffe']
#~ [u'Ponchiot', u'Ponchien', u'Mastouffe']
#~ [u'Chacripan', u'Leopardus']
#~ [u'Chacripan', u'Leopardus']
#~ [u'Feuillajou', u'Feuiloutan']
#~ [u'Feuillajou', u'Feuiloutan']
#~ [u'Flamajou', u'Flamoutan']
#~ [u'Flamajou', u'Flamoutan']
#~ [u'Flotajou', u'Flotoutan']
#~ [u'Flotajou', u'Flotoutan']
#~ [u'Munna', u'Mushana']
#~ [u'Munna', u'Mushana']
#~ [u'Poichigeon', u'Colombeau', u'Deflaisan']
#~ [u'Poichigeon', u'Colombeau', u'Deflaisan']
#~ [u'Poichigeon', u'Colombeau', u'Deflaisan']
#~ [u'Zebibron', u'Zeblitz']
#~ [u'Zebibron', u'Zeblitz']
#~ [u'Nodulithe', u'Geolithe', u'Gigalithe']
#~ [u'Nodulithe', u'Geolithe', u'Gigalithe']
#~ [u'Nodulithe', u'Geolithe', u'Gigalithe']
#~ [u'Chovsourir', u'Rhinolove']
#~ [u'Chovsourir', u'Rhinolove']
#~ [u'Rototaupe', u'Minotaupe']
#~ [u'Rototaupe', u'Minotaupe']
#~ []
#~ [u'Charpenti', u'Ouvrifier', u'Betochef']
#~ [u'Charpenti', u'Ouvrifier', u'Betochef']
#~ [u'Charpenti', u'Ouvrifier', u'Betochef']
#~ [u'Tritonde', u'Batracne', u'Crapustule']
#~ [u'Tritonde', u'Batracne', u'Crapustule']
#~ [u'Tritonde', u'Batracne', u'Crapustule']
#~ []
#~ []
#~ [u'Larveyette', u'Couverdure', u'Manternel']
#~ [u'Larveyette', u'Couverdure', u'Manternel']
#~ [u'Larveyette', u'Couverdure', u'Manternel']
#~ [u'Venipatte', u'Scobolide', u'Brutapode']
#~ [u'Venipatte', u'Scobolide', u'Brutapode']
#~ [u'Venipatte', u'Scobolide', u'Brutapode']
#~ [u'Doudouvet', u'Farfaduvet']
#~ [u'Doudouvet', u'Farfaduvet']
#~ [u'Chlorobule', u'Fragilady']
#~ [u'Chlorobule', u'Fragilady']
#~ []
#~ [u'Mascaiman', u'Escroco', u'Crocorible']
#~ [u'Mascaiman', u'Escroco', u'Crocorible']
#~ [u'Mascaiman', u'Escroco', u'Crocorible']
#~ [u'Darumarond', u'Darumacho']
#~ [u'Darumarond', u'Darumacho']
#~ [u'Darumarond', u'Darumacho']
#~ []
#~ [u'Crabicoque', u'Crabaraque']
#~ [u'Crabicoque', u'Crabaraque']
#~ [u'Baggiguane', u'Baggaid']
#~ [u'Baggiguane', u'Baggaid']
#~ []
#~ [u'Tutafeh', u'Tutankafer']
#~ [u'Tutafeh', u'Tutankafer']
#~ [u'Carapagos', u'Megapagos']
#~ [u'Carapagos', u'Megapagos']
#~ [u'Arkeapti', u'Aeropteryx']
#~ [u'Arkeapti', u'Aeropteryx']
#~ [u'Miamiasme', u'Miasmax']
#~ [u'Miamiasme', u'Miasmax']
#~ [u'Zorua', u'Zoroark']
#~ [u'Zorua', u'Zoroark']
#~ [u'Chinchidou', u'Pashmilla']
#~ [u'Chinchidou', u'Pashmilla']
#~ [u'Scrutella', u'Mesmerella', u'Siderella']
#~ [u'Scrutella', u'Mesmerella', u'Siderella']
#~ [u'Scrutella', u'Mesmerella', u'Siderella']
#~ [u'Nucleos', u'Meios']
#~ [u'Nucleos', u'Meios']
#~ [u'Nucleos', u'Meios', u'Symbios200e']
#~ [u'Couaneton', u'Lakmecygne']
#~ [u'Couaneton', u'Lakmecygne']
#~ [u'Sorbebe', u'Sorboul', u'Sorbouboul']
#~ [u'Sorbebe', u'Sorboul', u'Sorbouboul']
#~ [u'Sorbebe', u'Sorboul', u'Sorbouboul']
#~ [u'Vivaldaim', u'Haydaim']
#~ [u'Vivaldaim', u'Haydaim']
#~ []
#~ [u'Carabing', u'Lancargot']
#~ [u'Carabing', u'Lancargot']
#~ [u'Trompignon', u'Gaulet']
#~ [u'Trompignon', u'Gaulet']
#~ [u'Viskuse', u'Moyade']
#~ [u'Viskuse', u'Moyade']
#~ []
#~ [u'Statitik', u'Mygavolt']
#~ [u'Statitik', u'Mygavolt']
#~ [u'Grindur', u'Noacier']
#~ [u'Grindur', u'Noacier']
#~ [u'Tic', u'Clic', u'Cliticlic']
#~ [u'Tic', u'Clic', u'Cliticlic']
#~ [u'Tic', u'Clic', u'Cliticlic']
#~ [u'Anchwatt', u'Lamperoie', u'Ohmassacre']
#~ [u'Anchwatt', u'Lamperoie', u'Ohmassacre']
#~ [u'Anchwatt', u'Lamperoie', u'Ohmassacre']
#~ [u'Lewsor', u'Neitram']
#~ [u'Lewsor', u'Neitram']
#~ [u'Funecire', u'Melancolux', u'Lugulabre']
#~ [u'Funecire', u'Melancolux', u'Lugulabre']
#~ [u'Funecire', u'Melancolux', u'Lugulabre']
#~ [u'Coupenotte', u'Incisache', u'Tranchodon']
#~ [u'Coupenotte', u'Incisache', u'Tranchodon']
#~ [u'Coupenotte', u'Incisache', u'Tranchodon']
#~ [u'Polarhume', u'Polagriffe']
#~ [u'Polarhume', u'Polagriffe']
#~ []
#~ [u'Escargaume', u'Limaspeed']
#~ [u'Escargaume', u'Limaspeed']
#~ []
#~ [u'Kungfouine', u'Shaofouine']
#~ [u'Kungfouine', u'Shaofouine']
#~ []
#~ [u'Gringolem', u'Golemastoc']
#~ [u'Gringolem', u'Golemastoc']
#~ [u'Scalpion', u'Scalproie']
#~ [u'Scalpion', u'Scalproie']
#~ []
#~ [u'Furaiglon', u'Gueriaigle']
#~ [u'Furaiglon', u'Gueriaigle']
#~ [u'Vostourno', u'Vaututrice']
#~ [u'Vostourno', u'Vaututrice']
#~ []
#~ []
#~ [u'Solochi', u'Diamat', u'Trioxhydre']
#~ [u'Solochi', u'Diamat', u'Trioxhydre']
#~ [u'Solochi', u'Diamat', u'Trioxhydre']
#~ [u'Pyronille', u'Pyrax']
#~ [u'Pyronille', u'Pyrax']
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ []
#~ [u'Marisson', u'Boguerisse', u'Blindepique']
#~ [u'Marisson', u'Boguerisse', u'Blindepique']
#~ [u'Marisson', u'Boguerisse', u'Blindepique']
#~ [u'Feunnec', u'Roussil', u'Goupelin']
#~ [u'Feunnec', u'Roussil', u'Goupelin']
#~ [u'Feunnec', u'Roussil', u'Goupelin']
#~ [u'Grenousse', u'Croaporal', u'Amphinobi']
#~ [u'Grenousse', u'Croaporal', u'Amphinobi']
#~ [u'Grenousse', u'Croaporal', u'Amphinobi']
#~ [u'Sapereau', u'Excavarenne']
#~ [u'Sapereau', u'Excavarenne']
#~ [u'Passerouge', u'Braisillon', u'Flambusard']
#~ [u'Passerouge', u'Braisillon', u'Flambusard']
#~ [u'Passerouge', u'Braisillon', u'Flambusard']
#~ [u'Lepidonille', u'Peregrain', u'Prismillon']
#~ [u'Lepidonille', u'Peregrain', u'Prismillon']
#~ [u'Lepidonille', u'Peregrain', u'Prismillon']
#~ [u'Helionceau', u'Nemelios']
#~ [u'Helionceau', u'Nemelios']
#~ [u'Flabebe', u'Floette', u'Florges']
#~ [u'Flabebe', u'Floette', u'Florges']
#~ [u'Flabebe', u'Floette', u'Florges']
#~ [u'Cabriolaine', u'Chevroum']
#~ [u'Cabriolaine', u'Chevroum']
#~ [u'Pandespiegle', u'Pandarbare']
#~ [u'Pandespiegle', u'Pandarbare']
#~ []
#~ [u'Psystigri', u'Mistigrix']
#~ [u'Psystigri', u'Mistigrix']
#~ [u'Monorpale', u'Dimocles', u'Exagide']
#~ [u'Monorpale', u'Dimocles', u'Exagide']
#~ [u'Monorpale', u'Dimocles', u'Exagide']
#~ [u'Monorpale', u'Dimocles', u'Exagide']
#~ [u'Fluvetin', u'Cocotine']
#~ [u'Fluvetin', u'Cocotine']
#~ [u'Sucroquin', u'Cupcanaille']
#~ [u'Sucroquin', u'Cupcanaille']
#~ [u'Sepiatop', u'Sepiatroce']
#~ [u'Sepiatop', u'Sepiatroce']
#~ [u'Opermine', u'Golgopathe']
#~ [u'Opermine', u'Golgopathe']
#~ [u'Venalgue', u'Kravarech']
#~ [u'Venalgue', u'Kravarech']
#~ [u'Flingouste', u'Gamblast']
#~ [u'Flingouste', u'Gamblast']
#~ [u'Galvaran', u'Iguolta']
#~ [u'Galvaran', u'Iguolta']
#~ [u'Ptyranidur', u'Rexillius']
#~ [u'Ptyranidur', u'Rexillius']
#~ [u'Amagara', u'Dragmara']
#~ [u'Amagara', u'Dragmara']
#~ [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali']
#~ []
#~ []
#~ []
#~ [u'Mucuscule', u'Colimucus', u'Muplodocus']
#~ [u'Mucuscule', u'Colimucus', u'Muplodocus']
#~ [u'Mucuscule', u'Colimucus', u'Muplodocus']
#~ []
#~ [u'Brocelome', u'Desseliande']
#~ [u'Brocelome', u'Desseliande']
#~ [u'Pitrouille', u'Banshitrouye']
#~ [u'Pitrouille', u'Banshitrouye']
#~ [u'Pitrouille', u'Banshitrouye']
#~ [u'Pitrouille', u'Banshitrouye']
#~ [u'Pitrouille', u'Banshitrouye']
#~ [u'Pitrouille', u'Banshitrouye']
#~ [u'Pitrouille', u'Banshitrouye']
#~ [u'Pitrouille', u'Banshitrouye']
#~ [u'Grelacon', u'Seracrawl']
#~ [u'Grelacon', u'Seracrawl']
#~ [u'Sonistrelle', u'Bruyverne']
#~ [u'Sonistrelle', u'Bruyverne']
#~ []
#~ []
#~ []
#~ list = [[u'Bulbizarre', u'Herbizarre', u'Florizarre', u'Mega-Florizarre'], [u'Bulbizarre', u'Herbizarre', u'Florizarre', u'Mega-Florizarre'], [u'Bulbizarre', u'Herbizarre', u'Florizarre', u'Mega-Florizarre'], [u'Bulbizarre', u'Herbizarre', u'Florizarre', u'Mega-Florizarre'], [u'Salameche', u'Reptincel', u'Dracaufeu', u'Mega-Dracaufeu X', u'Mega-Dracaufeu Y'], [u'Salameche', u'Reptincel', u'Dracaufeu', u'Mega-Dracaufeu X', u'Mega-Dracaufeu Y'], [u'Salameche', u'Reptincel', u'Dracaufeu', u'Mega-Dracaufeu X', u'Mega-Dracaufeu Y'], [u'Salameche', u'Reptincel', u'Dracaufeu', u'Mega-Dracaufeu X', u'Mega-Dracaufeu Y'], [u'Salameche', u'Reptincel', u'Dracaufeu', u'Mega-Dracaufeu X', u'Mega-Dracaufeu Y'], [u'Carapuce', u'Carabaffe', u'Tortank', u'Mega-Tortank'], [u'Carapuce', u'Carabaffe', u'Tortank', u'Mega-Tortank'], [u'Carapuce', u'Carabaffe', u'Tortank', u'Mega-Tortank'], [u'Carapuce', u'Carabaffe', u'Tortank', u'Mega-Tortank'], [u'Chenipan', u'Chrysacier', u'Papilusion'], [u'Chenipan', u'Chrysacier', u'Papilusion'], [u'Chenipan', u'Chrysacier', u'Papilusion'], [u'Aspicot', u'Coconfort', u'Dardargnan'], [u'Aspicot', u'Coconfort', u'Dardargnan'], [u'Aspicot', u'Coconfort', u'Dardargnan'], [u'Roucool', u'Roucoups', u'Roucarnage'], [u'Roucool', u'Roucoups', u'Roucarnage'], [u'Roucool', u'Roucoups', u'Roucarnage'], [u'Rattata', u'Rattatac'], [u'Rattata', u'Rattatac'], [u'Piafabec', u'Rapasdepic'], [u'Piafabec', u'Rapasdepic'], [u'Abo', u'Arbok'], [u'Abo', u'Arbok'], [u'Pichu', u'Pikachu', u'Raichu'], [u'Pichu', u'Pikachu', u'Raichu'], [u'Sabelette', u'Sablaireau'], [u'Sabelette', u'Sablaireau'], [u'Nidoran F', u'Nidorina', u'Nidoqueen'], [u'Nidoran F', u'Nidorina', u'Nidoqueen'], [u'Nidoran F', u'Nidorina', u'Nidoqueen'], [u'Nidoran M', u'Nidorino', u'Nidoking'], [u'Nidoran M', u'Nidorino', u'Nidoking'], [u'Nidoran M', u'Nidorino', u'Nidoking'], [u'Melo', u'Melofee', u'Melodelfe'], [u'Melo', u'Melofee', u'Melodelfe'], [u'Goupix', u'Feunard'], [u'Goupix', u'Feunard'], [u'Toudoudou', u'Rondoudou', u'Grodoudou'], [u'Toudoudou', u'Rondoudou', u'Grodoudou'], [u'Nosferapti', u'Nosferalto', u'Nostenfer'], [u'Nosferapti', u'Nosferalto', u'Nostenfer'], [u'Mystherbe', u'Ortide', u'Rafflesia', u'Joliflor'], [u'Mystherbe', u'Ortide', u'Rafflesia', u'Joliflor'], [u'Mystherbe', u'Ortide', u'Rafflesia', u'Joliflor'], [u'Paras', u'Parasect'], [u'Paras', u'Parasect'], [u'Mimitoss', u'Aeromite'], [u'Mimitoss', u'Aeromite'], [u'Taupiqueur', u'Triopikeur'], [u'Taupiqueur', u'Triopikeur'], [u'Miaouss', u'Persian'], [u'Miaouss', u'Persian'], [u'Psykokwak', u'Akwakwak'], [u'Psykokwak', u'Akwakwak'], [u'Ferosinge', u'Colossinge'], [u'Ferosinge', u'Colossinge'], [u'Caninos', u'Arcanin'], [u'Caninos', u'Arcanin'], [u'Ptitard', u'Tetarte', u'Tartard', u'Tarpaud'], [u'Ptitard', u'Tetarte', u'Tartard', u'Tarpaud'], [u'Ptitard', u'Tetarte', u'Tartard', u'Tarpaud'], [u'Abra', u'Kadabra', u'Alakazam', u'Mega-Alakazam'], [u'Abra', u'Kadabra', u'Alakazam', u'Mega-Alakazam'], [u'Abra', u'Kadabra', u'Alakazam', u'Mega-Alakazam'], [u'Abra', u'Kadabra', u'Alakazam', u'Mega-Alakazam'], [u'Machoc', u'Machopeur', u'Mackogneur'], [u'Machoc', u'Machopeur', u'Mackogneur'], [u'Machoc', u'Machopeur', u'Mackogneur'], [u'Chetiflor', u'Boustiflor', u'Empiflor'], [u'Chetiflor', u'Boustiflor', u'Empiflor'], [u'Chetiflor', u'Boustiflor', u'Empiflor'], [u'Tentacool', u'Tentacruel'], [u'Tentacool', u'Tentacruel'], [u'Racaillou', u'Gravalanch', u'Grolem'], [u'Racaillou', u'Gravalanch', u'Grolem'], [u'Racaillou', u'Gravalanch', u'Grolem'], [u'Ponyta', u'Galopa'], [u'Ponyta', u'Galopa'], [u'Ramoloss', u'Flagadoss', u'Roigada'], [u'Ramoloss', u'Flagadoss', u'Roigada'], [u'Magneti', u'Magneton', u'Magnezone'], [u'Magneti', u'Magneton', u'Magnezone'], [], [u'Doduo', u'Dodrio'], [u'Doduo', u'Dodrio'], [u'Otaria', u'Lamantine'], [u'Otaria', u'Lamantine'], [u'Tadmorv', u'Grotadmorv'], [u'Tadmorv', u'Grotadmorv'], [u'Kokiyas', u'Crustabri'], [u'Kokiyas', u'Crustabri'], [u'Fantominus', u'Spectrum', u'Ectoplasma', u'Mega-Ectoplasma'], [u'Fantominus', u'Spectrum', u'Ectoplasma', u'Mega-Ectoplasma'], [u'Fantominus', u'Spectrum', u'Ectoplasma', u'Mega-Ectoplasma'], [u'Fantominus', u'Spectrum', u'Ectoplasma', u'Mega-Ectoplasma'], [u'Onix', u'Steelix'], [u'Soporifik', u'Hypnomade'], [u'Soporifik', u'Hypnomade'], [u'Krabby', u'Krabboss'], [u'Krabby', u'Krabboss'], [u'Voltorbe', u'Electrode'], [u'Voltorbe', u'Electrode'], [u'Noeunoeuf', u'Noadkoko'], [u'Noeunoeuf', u'Noadkoko'], [u'Osselait', u'Ossatueur'], [u'Osselait', u'Ossatueur'], [u'Debugant', u'Kicklee', u'Tygnon', u'Kapoera'], [u'Debugant', u'Kicklee', u'Tygnon', u'Kapoera'], [u'Excelangue', u'Coudlangue'], [u'Smogo', u'Smogogo'], [u'Smogo', u'Smogogo'], [u'Rhinocorne', u'Rhinoferos', u'Rhinastoc'], [u'Rhinocorne', u'Rhinoferos', u'Rhinastoc'], [u'Ptiravi', u'Leveinard', u'Leuphorie'], [u'Saquedeneu', u'Bouldeneu'], [u'Kangourex', u'Mega-Kangourex'], [u'Kangourex', u'Mega-Kangourex'], [u'Hypotrempe', u'Hypocean', u'Hyporoi'], [u'Hypotrempe', u'Hypocean', u'Hyporoi'], [u'Poissirene', u'Poissoroy'], [u'Poissirene', u'Poissoroy'], [], [], [u'Mime Jr.', u'M. Mime'], [u'Insecateur', u'Cizayox', u'Mega-Cizayox'], [u'Lippouti', u'Lippoutou'], [u'Elekid', u'Elektek', u'Elekable'], [u'Magby', u'Magmar', u'Maganon'], [u'Scarabrute', u'Mega-Scarabrute'], [u'Scarabrute', u'Mega-Scarabrute'], [], [u'Magicarpe', u'Leviator', u'Mega-Leviator'], [u'Magicarpe', u'Leviator', u'Mega-Leviator'], [u'Magicarpe', u'Leviator', u'Mega-Leviator'], [], [], [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], [u'Porygon', u'Porygon2', u'Porygon-Z'], [u'Amonita', u'Amonistar'], [u'Amonita', u'Amonistar'], [u'Kabuto', u'Kabutops'], [u'Kabuto', u'Kabutops'], [u'Ptera', u'Mega-Ptera'], [u'Goinfrex', u'Ronflex'], [], [], [], [u'Minidraco', u'Draco', u'Dracolosse'], [u'Minidraco', u'Draco', u'Dracolosse'], [u'Minidraco', u'Draco', u'Dracolosse'], [u'Mewtwo', u'Mega-Mewtwo X', u'Mega-Mewtwo Y'], [u'Mewtwo', u'Mega-Mewtwo X', u'Mega-Mewtwo Y'], [u'Mewtwo', u'Mega-Mewtwo X', u'Mega-Mewtwo Y'], [], [u'Germignon', u'Macronium', u'Meganium'], [u'Germignon', u'Macronium', u'Meganium'], [u'Germignon', u'Macronium', u'Meganium'], [u'Hericendre', u'Feurisson', u'Typhlosion'], [u'Hericendre', u'Feurisson', u'Typhlosion'], [u'Hericendre', u'Feurisson', u'Typhlosion'], [u'Kaiminus', u'Crocrodil', u'Aligatueur'], [u'Kaiminus', u'Crocrodil', u'Aligatueur'], [u'Kaiminus', u'Crocrodil', u'Aligatueur'], [u'Fouinette', u'Fouinar'], [u'Fouinette', u'Fouinar'], [u'Hoot-hoot', u'Noarfang'], [u'Hoot-hoot', u'Noarfang'], [u'Coxy', u'Coxyclaque'], [u'Coxy', u'Coxyclaque'], [u'Mimigal', u'Migalos'], [u'Mimigal', u'Migalos'], [u'Nosferapti', u'Nosferalto', u'Nostenfer'], [u'Loupio', u'Lanturn'], [u'Loupio', u'Lanturn'], [u'Pichu', u'Pikachu', u'Raichu'], [u'Melo', u'Melofee', u'Melodelfe'], [u'Toudoudou', u'Rondoudou', u'Grodoudou'], [u'Togepi', u'Togetic', u'Togekiss'], [u'Togepi', u'Togetic', u'Togekiss'], [u'Natu', u'Xatu'], [u'Natu', u'Xatu'], [u'Wattouat', u'Lainergie', u'Pharamp', u'Mega-Pharamp'], [u'Wattouat', u'Lainergie', u'Pharamp', u'Mega-Pharamp'], [u'Wattouat', u'Lainergie', u'Pharamp', u'Mega-Pharamp'], [u'Wattouat', u'Lainergie', u'Pharamp', u'Mega-Pharamp'], [u'Mystherbe', u'Ortide', u'Rafflesia', u'Joliflor'], [u'Azurill', u'Marill', u'Azumarill'], [u'Azurill', u'Marill', u'Azumarill'], [u'Manzai', u'Simularbre'], [u'Ptitard', u'Tetarte', u'Tartard', u'Tarpaud'], [u'Granivol', u'Floravol', u'Cotovol'], [u'Granivol', u'Floravol', u'Cotovol'], [u'Granivol', u'Floravol', u'Cotovol'], [u'Capumain', u'Capidextre'], [u'Tournegrin', u'Heliatronc'], [u'Tournegrin', u'Heliatronc'], [u'Yanma', u'Yanmega'], [u'Axoloto', u'Maraiste'], [u'Axoloto', u'Maraiste'], [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], [u'Cornebre', u'Corboss'], [u'Ramoloss', u'Flagadoss', u'Roigada'], [u'Feuforeve', u'Magireve'], [], [u'Okeoke', u'Qulbutoke'], [], [u'Pomdepik', u'Foretress'], [u'Pomdepik', u'Foretress'], [], [u'Scorplane', u'Scorvol'], [u'Onix', u'Steelix'], [u'Snubbull', u'Granbull'], [u'Snubbull', u'Granbull'], [], [u'Insecateur', u'Cizayox', u'Mega-Cizayox'], [u'Insecateur', u'Cizayox', u'Mega-Cizayox'], [], [u'Scarhino', u'Mega-Scarhino'], [u'Scarhino', u'Mega-Scarhino'], [u'Farfuret', u'Dimoret'], [u'Teddiursa', u'Ursaring'], [u'Teddiursa', u'Ursaring'], [u'Limagma', u'Volcaropod'], [u'Limagma', u'Volcaropod'], [u'Marcacrin', u'Cochignon', u'Mammochon'], [u'Marcacrin', u'Cochignon', u'Mammochon'], [], [u'Remoraid', u'Octillery'], [u'Remoraid', u'Octillery'], [], [u'Babimanta', u'Demanta'], [], [u'Malosse', u'Demolosse', u'Mega-Demolosse'], [u'Malosse', u'Demolosse', u'Mega-Demolosse'], [u'Malosse', u'Demolosse', u'Mega-Demolosse'], [u'Hypotrempe', u'Hypocean', u'Hyporoi'], [u'Phanpy', u'Donphan'], [u'Phanpy', u'Donphan'], [u'Porygon', u'Porygon2', u'Porygon-Z'], [], [], [u'Debugant', u'Kicklee', u'Tygnon', u'Kapoera'], [u'Debugant', u'Kicklee', u'Tygnon', u'Kapoera'], [u'Lippouti', u'Lippoutou'], [u'Elekid', u'Elektek', u'Elekable'], [u'Magby', u'Magmar', u'Maganon'], [], [u'Ptiravi', u'Leveinard', u'Leuphorie'], [], [], [], [u'Embrylex', u'Ymphect', u'Tyranocif', u'Mega-Tyranocif'], [u'Embrylex', u'Ymphect', u'Tyranocif', u'Mega-Tyranocif'], [u'Embrylex', u'Ymphect', u'Tyranocif', u'Mega-Tyranocif'], [u'Embrylex', u'Ymphect', u'Tyranocif', u'Mega-Tyranocif'], [], [], [], [u'Arcko', u'Massko', u'Jungko'], [u'Arcko', u'Massko', u'Jungko'], [u'Arcko', u'Massko', u'Jungko'], [u'Poussifeu', u'Galifeu', u'Brasegali', u'Mega-Brasegali'], [u'Poussifeu', u'Galifeu', u'Brasegali', u'Mega-Brasegali'], [u'Poussifeu', u'Galifeu', u'Brasegali', u'Mega-Brasegali'], [u'Poussifeu', u'Galifeu', u'Brasegali', u'Mega-Brasegali'], [u'Gobou', u'Flobio', u'Laggron'], [u'Gobou', u'Flobio', u'Laggron'], [u'Gobou', u'Flobio', u'Laggron'], [u'Medhyena', u'Grahyena'], [u'Medhyena', u'Grahyena'], [u'Zigzaton', u'Lineon'], [u'Zigzaton', u'Lineon'], [u'Chenipotte', u'Armulys', u'Blindalys', u'Charmillon', u'Papinox'], [u'Chenipotte', u'Armulys', u'Blindalys', u'Charmillon', u'Papinox'], [u'Chenipotte', u'Armulys', u'Blindalys', u'Charmillon', u'Papinox'], [u'Chenipotte', u'Armulys', u'Blindalys', u'Charmillon', u'Papinox'], [u'Chenipotte', u'Armulys', u'Blindalys', u'Charmillon', u'Papinox'], [u'Nenupiot', u'Lombre', u'Ludicolo'], [u'Nenupiot', u'Lombre', u'Ludicolo'], [u'Nenupiot', u'Lombre', u'Ludicolo'], [u'Grainipiot', u'Pifeuil', u'Tengalice'], [u'Grainipiot', u'Pifeuil', u'Tengalice'], [u'Grainipiot', u'Pifeuil', u'Tengalice'], [u'Nirondelle', u'Heledelle'], [u'Nirondelle', u'Heledelle'], [u'Goelise', u'Bekipan'], [u'Goelise', u'Bekipan'], [u'Tarsal', u'Kirlia', u'Gardevoir', u'Gallame', u'Mega-Gardevoir'], [u'Tarsal', u'Kirlia', u'Gardevoir', u'Gallame', u'Mega-Gardevoir'], [u'Tarsal', u'Kirlia', u'Gardevoir', u'Gallame', u'Mega-Gardevoir'], [u'Tarsal', u'Kirlia', u'Gardevoir', u'Gallame', u'Mega-Gardevoir'], [u'Arakdo', u'Maskadra'], [u'Arakdo', u'Maskadra'], [u'Balignon', u'Chapignon'], [u'Balignon', u'Chapignon'], [u'Parecool', u'Vigoroth', u'Monaflemit'], [u'Parecool', u'Vigoroth', u'Monaflemit'], [u'Parecool', u'Vigoroth', u'Monaflemit'], [u'Ningale', u'Ninjask', u'Munja'], [u'Ningale', u'Ninjask', u'Munja'], [u'Ningale', u'Ninjask', u'Munja'], [u'Chuchmur', u'Ramboum', u'Brouhabam'], [u'Chuchmur', u'Ramboum', u'Brouhabam'], [u'Chuchmur', u'Ramboum', u'Brouhabam'], [u'Makuhita', u'Hariyama'], [u'Makuhita', u'Hariyama'], [u'Azurill', u'Marill', u'Azumarill'], [u'Tarinor', u'Tarinorme'], [u'Skitty', u'Delcatty'], [u'Skitty', u'Delcatty'], [], [u'Mysdibule', u'Mega-Mysdibule'], [u'Mysdibule', u'Mega-Mysdibule'], [u'Galekid', u'Galegon', u'Galeking', u'Mega-Galeking'], [u'Galekid', u'Galegon', u'Galeking', u'Mega-Galeking'], [u'Galekid', u'Galegon', u'Galeking', u'Mega-Galeking'], [u'Galekid', u'Galegon', u'Galeking', u'Mega-Galeking'], [u'Meditikka', u'Charmina', u'Mega-Charmina'], [u'Meditikka', u'Charmina', u'Mega-Charmina'], [u'Meditikka', u'Charmina', u'Mega-Charmina'], [u'Dynavolt', u'Elecsprint', u'Mega-Elecsprint'], [u'Dynavolt', u'Elecsprint', u'Mega-Elecsprint'], [u'Dynavolt', u'Elecsprint', u'Mega-Elecsprint'], [], [], [], [], [u'Rozbouton', u'Roselia', u'Roserade'], [u'Gloupti', u'Avaltout'], [u'Gloupti', u'Avaltout'], [u'Carvanha', u'Sharpedo'], [u'Carvanha', u'Sharpedo'], [u'Wailmer', u'Wailord'], [u'Wailmer', u'Wailord'], [u'Chamallot', u'Camerupt'], [u'Chamallot', u'Camerupt'], [], [u'Spoink', u'Groret'], [u'Spoink', u'Groret'], [], [u'Kraknoix', u'Vibraninf', u'Libegon'], [u'Kraknoix', u'Vibraninf', u'Libegon'], [u'Kraknoix', u'Vibraninf', u'Libegon'], [u'Cacnea', u'Cacturne'], [u'Cacnea', u'Cacturne'], [u'Tylton', u'Altaria'], [u'Tylton', u'Altaria'], [], [], [], [], [u'Barloche', u'Barbicha'], [u'Barloche', u'Barbicha'], [u'Ecrapince', u'Colhomard'], [u'Ecrapince', u'Colhomard'], [u'Balbuto', u'Kaorine'], [u'Balbuto', u'Kaorine'], [u'Lilia', u'Vacilys'], [u'Lilia', u'Vacilys'], [u'Anorith', u'Armaldo'], [u'Anorith', u'Armaldo'], [u'Barpau', u'Milobellus'], [u'Barpau', u'Milobellus'], [], [], [u'Polichombr', u'Branette', u'Mega-Branette'], [u'Polichombr', u'Branette', u'Mega-Branette'], [u'Polichombr', u'Branette', u'Mega-Branette'], [u'Skelenox', u'Teraclope', u'Noctunoir'], [u'Skelenox', u'Teraclope', u'Noctunoir'], [], [u'Korillon', u'Eoko'], [u'Absol', u'Mega-Absol'], [u'Absol', u'Mega-Absol'], [u'Okeoke', u'Qulbutoke'], [u'Stalgamin', u'Oniglali', u'Momartik'], [u'Stalgamin', u'Oniglali', u'Momartik'], [u'Obalie', u'Phogleur', u'Kaimorse'], [u'Obalie', u'Phogleur', u'Kaimorse'], [u'Obalie', u'Phogleur', u'Kaimorse'], [u'Coquiperl', u'Serpang', u'Rosabyss'], [u'Coquiperl', u'Serpang', u'Rosabyss'], [u'Coquiperl', u'Serpang', u'Rosabyss'], [], [], [u'Draby', u'Drackhaus', u'Drattak'], [u'Draby', u'Drackhaus', u'Drattak'], [u'Draby', u'Drackhaus', u'Drattak'], [u'Terhal', u'Metang', u'Metalosse'], [u'Terhal', u'Metang', u'Metalosse'], [u'Terhal', u'Metang', u'Metalosse'], [], [], [], [], [], [], [], [], [], [], [], [], [], [u'Tortipouss', u'Boskara', u'Torterra'], [u'Tortipouss', u'Boskara', u'Torterra'], [u'Tortipouss', u'Boskara', u'Torterra'], [u'Ouisticram', u'Chimpenfeu', u'Simiabraz'], [u'Ouisticram', u'Chimpenfeu', u'Simiabraz'], [u'Ouisticram', u'Chimpenfeu', u'Simiabraz'], [u'Tiplouf', u'Prinplouf', u'Pingoleon'], [u'Tiplouf', u'Prinplouf', u'Pingoleon'], [u'Tiplouf', u'Prinplouf', u'Pingoleon'], [u'Etourmi', u'Etourvol', u'Etouraptor'], [u'Etourmi', u'Etourvol', u'Etouraptor'], [u'Etourmi', u'Etourvol', u'Etouraptor'], [u'Keunotor', u'Castorno'], [u'Keunotor', u'Castorno'], [u'Crikzik', u'Melokrik'], [u'Crikzik', u'Melokrik'], [u'Lixy', u'Luxio', u'Luxray'], [u'Lixy', u'Luxio', u'Luxray'], [u'Lixy', u'Luxio', u'Luxray'], [u'Rozbouton', u'Roselia', u'Roserade'], [u'Rozbouton', u'Roselia', u'Roserade'], [u'Kranidos', u'Charkos'], [u'Kranidos', u'Charkos'], [u'Dinoclier', u'Bastiodon'], [u'Dinoclier', u'Bastiodon'], [u'Cheniti', u'Cheniselle', u'Papilord'], [u'Cheniti', u'Cheniselle', u'Papilord'], [u'Cheniti', u'Cheniselle', u'Papilord'], [u'Cheniti', u'Cheniselle', u'Papilord'], [u'Cheniti', u'Cheniselle', u'Papilord'], [u'Apitrini', u'Apireine'], [u'Apitrini', u'Apireine'], [], [u'Mustebouee', u'Musteflott'], [u'Mustebouee', u'Musteflott'], [u'Ceribou', u'Ceriflor'], [u'Ceribou', u'Ceriflor'], [u'Sancoki', u'Tritosor'], [u'Sancoki', u'Tritosor'], [u'Capumain', u'Capidextre'], [u'Baudrive', u'Grodrive'], [u'Baudrive', u'Grodrive'], [u'Laporeille', u'Lockpin'], [u'Laporeille', u'Lockpin'], [u'Feuforeve', u'Magireve'], [u'Cornebre', u'Corboss'], [u'Chaglam', u'Chaffreux'], [u'Chaglam', u'Chaffreux'], [u'Korillon', u'Eoko'], [u'Moufouette', u'Moufflair'], [u'Moufouette', u'Moufflair'], [u'Archeomire', u'Archeodong'], [u'Archeomire', u'Archeodong'], [u'Manzai', u'Simularbre'], [u'Mime Jr.', u'M. Mime'], [u'Ptiravi', u'Leveinard', u'Leuphorie'], [], [], [u'Griknot', u'Carmache', u'Carchacrok', u'Mega-Carchacrok'], [u'Griknot', u'Carmache', u'Carchacrok', u'Mega-Carchacrok'], [u'Griknot', u'Carmache', u'Carchacrok', u'Mega-Carchacrok'], [u'Griknot', u'Carmache', u'Carchacrok', u'Mega-Carchacrok'], [u'Goinfrex', u'Ronflex'], [u'Riolu', u'Lucario', u'Mega-Lucario'], [u'Riolu', u'Lucario', u'Mega-Lucario'], [u'Riolu', u'Lucario', u'Mega-Lucario'], [u'Hippopotas', u'Hippodocus'], [u'Hippopotas', u'Hippodocus'], [u'Rapion', u'Drascore'], [u'Rapion', u'Drascore'], [u'Cradopaud', u'Coatox'], [u'Cradopaud', u'Coatox'], [], [u'Ecayon', u'Lumineon'], [u'Ecayon', u'Lumineon'], [u'Babimanta', u'Demanta'], [u'Blizzi', u'Blizzaroi', u'Mega-Blizzaroi'], [u'Blizzi', u'Blizzaroi', u'Mega-Blizzaroi'], [u'Blizzi', u'Blizzaroi', u'Mega-Blizzaroi'], [u'Farfuret', u'Dimoret'], [u'Magneti', u'Magneton', u'Magnezone'], [u'Excelangue', u'Coudlangue'], [u'Rhinocorne', u'Rhinoferos', u'Rhinastoc'], [u'Saquedeneu', u'Bouldeneu'], [u'Elekid', u'Elektek', u'Elekable'], [u'Magby', u'Magmar', u'Maganon'], [u'Togepi', u'Togetic', u'Togekiss'], [u'Yanma', u'Yanmega'], [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], [u'Scorplane', u'Scorvol'], [u'Marcacrin', u'Cochignon', u'Mammochon'], [u'Porygon', u'Porygon2', u'Porygon-Z'], [u'Tarsal', u'Kirlia', u'Gardevoir', u'Gallame', u'Mega-Gardevoir'], [u'Tarinor', u'Tarinorme'], [u'Skelenox', u'Teraclope', u'Noctunoir'], [u'Stalgamin', u'Oniglali', u'Momartik'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [u'Vipelierre', u'Lianaja', u'Majaspic'], [u'Vipelierre', u'Lianaja', u'Majaspic'], [u'Vipelierre', u'Lianaja', u'Majaspic'], [u'Gruikui', u'Grotichon', u'Roitiflam'], [u'Gruikui', u'Grotichon', u'Roitiflam'], [u'Gruikui', u'Grotichon', u'Roitiflam'], [u'Moustillon', u'Mateloutre', u'Clamiral'], [u'Moustillon', u'Mateloutre', u'Clamiral'], [u'Moustillon', u'Mateloutre', u'Clamiral'], [u'Ratentif', u'Miradar'], [u'Ratentif', u'Miradar'], [u'Ponchiot', u'Ponchien', u'Mastouffe'], [u'Ponchiot', u'Ponchien', u'Mastouffe'], [u'Ponchiot', u'Ponchien', u'Mastouffe'], [u'Chacripan', u'Leopardus'], [u'Chacripan', u'Leopardus'], [u'Feuillajou', u'Feuiloutan'], [u'Feuillajou', u'Feuiloutan'], [u'Flamajou', u'Flamoutan'], [u'Flamajou', u'Flamoutan'], [u'Flotajou', u'Flotoutan'], [u'Flotajou', u'Flotoutan'], [u'Munna', u'Mushana'], [u'Munna', u'Mushana'], [u'Poichigeon', u'Colombeau', u'Deflaisan'], [u'Poichigeon', u'Colombeau', u'Deflaisan'], [u'Poichigeon', u'Colombeau', u'Deflaisan'], [u'Zebibron', u'Zeblitz'], [u'Zebibron', u'Zeblitz'], [u'Nodulithe', u'Geolithe', u'Gigalithe'], [u'Nodulithe', u'Geolithe', u'Gigalithe'], [u'Nodulithe', u'Geolithe', u'Gigalithe'], [u'Chovsourir', u'Rhinolove'], [u'Chovsourir', u'Rhinolove'], [u'Rototaupe', u'Minotaupe'], [u'Rototaupe', u'Minotaupe'], [], [u'Charpenti', u'Ouvrifier', u'Betochef'], [u'Charpenti', u'Ouvrifier', u'Betochef'], [u'Charpenti', u'Ouvrifier', u'Betochef'], [u'Tritonde', u'Batracne', u'Crapustule'], [u'Tritonde', u'Batracne', u'Crapustule'], [u'Tritonde', u'Batracne', u'Crapustule'], [], [], [u'Larveyette', u'Couverdure', u'Manternel'], [u'Larveyette', u'Couverdure', u'Manternel'], [u'Larveyette', u'Couverdure', u'Manternel'], [u'Venipatte', u'Scobolide', u'Brutapode'], [u'Venipatte', u'Scobolide', u'Brutapode'], [u'Venipatte', u'Scobolide', u'Brutapode'], [u'Doudouvet', u'Farfaduvet'], [u'Doudouvet', u'Farfaduvet'], [u'Chlorobule', u'Fragilady'], [u'Chlorobule', u'Fragilady'], [], [u'Mascaiman', u'Escroco', u'Crocorible'], [u'Mascaiman', u'Escroco', u'Crocorible'], [u'Mascaiman', u'Escroco', u'Crocorible'], [u'Darumarond', u'Darumacho'], [u'Darumarond', u'Darumacho'], [u'Darumarond', u'Darumacho'], [], [u'Crabicoque', u'Crabaraque'], [u'Crabicoque', u'Crabaraque'], [u'Baggiguane', u'Baggaid'], [u'Baggiguane', u'Baggaid'], [], [u'Tutafeh', u'Tutankafer'], [u'Tutafeh', u'Tutankafer'], [u'Carapagos', u'Megapagos'], [u'Carapagos', u'Megapagos'], [u'Arkeapti', u'Aeropteryx'], [u'Arkeapti', u'Aeropteryx'], [u'Miamiasme', u'Miasmax'], [u'Miamiasme', u'Miasmax'], [u'Zorua', u'Zoroark'], [u'Zorua', u'Zoroark'], [u'Chinchidou', u'Pashmilla'], [u'Chinchidou', u'Pashmilla'], [u'Scrutella', u'Mesmerella', u'Siderella'], [u'Scrutella', u'Mesmerella', u'Siderella'], [u'Scrutella', u'Mesmerella', u'Siderella'], [u'Nucleos', u'Meios'], [u'Nucleos', u'Meios'], [u'Nucleos', u'Meios', u'Symbios200e'], [u'Couaneton', u'Lakmecygne'], [u'Couaneton', u'Lakmecygne'], [u'Sorbebe', u'Sorboul', u'Sorbouboul'], [u'Sorbebe', u'Sorboul', u'Sorbouboul'], [u'Sorbebe', u'Sorboul', u'Sorbouboul'], [u'Vivaldaim', u'Haydaim'], [u'Vivaldaim', u'Haydaim'], [], [u'Carabing', u'Lancargot'], [u'Carabing', u'Lancargot'], [u'Trompignon', u'Gaulet'], [u'Trompignon', u'Gaulet'], [u'Viskuse', u'Moyade'], [u'Viskuse', u'Moyade'], [], [u'Statitik', u'Mygavolt'], [u'Statitik', u'Mygavolt'], [u'Grindur', u'Noacier'], [u'Grindur', u'Noacier'], [u'Tic', u'Clic', u'Cliticlic'], [u'Tic', u'Clic', u'Cliticlic'], [u'Tic', u'Clic', u'Cliticlic'], [u'Anchwatt', u'Lamperoie', u'Ohmassacre'], [u'Anchwatt', u'Lamperoie', u'Ohmassacre'], [u'Anchwatt', u'Lamperoie', u'Ohmassacre'], [u'Lewsor', u'Neitram'], [u'Lewsor', u'Neitram'], [u'Funecire', u'Melancolux', u'Lugulabre'], [u'Funecire', u'Melancolux', u'Lugulabre'], [u'Funecire', u'Melancolux', u'Lugulabre'], [u'Coupenotte', u'Incisache', u'Tranchodon'], [u'Coupenotte', u'Incisache', u'Tranchodon'], [u'Coupenotte', u'Incisache', u'Tranchodon'], [u'Polarhume', u'Polagriffe'], [u'Polarhume', u'Polagriffe'], [], [u'Escargaume', u'Limaspeed'], [u'Escargaume', u'Limaspeed'], [], [u'Kungfouine', u'Shaofouine'], [u'Kungfouine', u'Shaofouine'], [], [u'Gringolem', u'Golemastoc'], [u'Gringolem', u'Golemastoc'], [u'Scalpion', u'Scalproie'], [u'Scalpion', u'Scalproie'], [], [u'Furaiglon', u'Gueriaigle'], [u'Furaiglon', u'Gueriaigle'], [u'Vostourno', u'Vaututrice'], [u'Vostourno', u'Vaututrice'], [], [], [u'Solochi', u'Diamat', u'Trioxhydre'], [u'Solochi', u'Diamat', u'Trioxhydre'], [u'Solochi', u'Diamat', u'Trioxhydre'], [u'Pyronille', u'Pyrax'], [u'Pyronille', u'Pyrax'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [u'Marisson', u'Boguerisse', u'Blindepique'], [u'Marisson', u'Boguerisse', u'Blindepique'], [u'Marisson', u'Boguerisse', u'Blindepique'], [u'Feunnec', u'Roussil', u'Goupelin'], [u'Feunnec', u'Roussil', u'Goupelin'], [u'Feunnec', u'Roussil', u'Goupelin'], [u'Grenousse', u'Croaporal', u'Amphinobi'], [u'Grenousse', u'Croaporal', u'Amphinobi'], [u'Grenousse', u'Croaporal', u'Amphinobi'], [u'Sapereau', u'Excavarenne'], [u'Sapereau', u'Excavarenne'], [u'Passerouge', u'Braisillon', u'Flambusard'], [u'Passerouge', u'Braisillon', u'Flambusard'], [u'Passerouge', u'Braisillon', u'Flambusard'], [u'Lepidonille', u'Peregrain', u'Prismillon'], [u'Lepidonille', u'Peregrain', u'Prismillon'], [u'Lepidonille', u'Peregrain', u'Prismillon'], [u'Helionceau', u'Nemelios'], [u'Helionceau', u'Nemelios'], [u'Flabebe', u'Floette', u'Florges'], [u'Flabebe', u'Floette', u'Florges'], [u'Flabebe', u'Floette', u'Florges'], [u'Cabriolaine', u'Chevroum'], [u'Cabriolaine', u'Chevroum'], [u'Pandespiegle', u'Pandarbare'], [u'Pandespiegle', u'Pandarbare'], [], [u'Psystigri', u'Mistigrix'], [u'Psystigri', u'Mistigrix'], [u'Monorpale', u'Dimocles', u'Exagide'], [u'Monorpale', u'Dimocles', u'Exagide'], [u'Monorpale', u'Dimocles', u'Exagide'], [u'Monorpale', u'Dimocles', u'Exagide'], [u'Fluvetin', u'Cocotine'], [u'Fluvetin', u'Cocotine'], [u'Sucroquin', u'Cupcanaille'], [u'Sucroquin', u'Cupcanaille'], [u'Sepiatop', u'Sepiatroce'], [u'Sepiatop', u'Sepiatroce'], [u'Opermine', u'Golgopathe'], [u'Opermine', u'Golgopathe'], [u'Venalgue', u'Kravarech'], [u'Venalgue', u'Kravarech'], [u'Flingouste', u'Gamblast'], [u'Flingouste', u'Gamblast'], [u'Galvaran', u'Iguolta'], [u'Galvaran', u'Iguolta'], [u'Ptyranidur', u'Rexillius'], [u'Ptyranidur', u'Rexillius'], [u'Amagara', u'Dragmara'], [u'Amagara', u'Dragmara'], [u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'], [], [], [], [u'Mucuscule', u'Colimucus', u'Muplodocus'], [u'Mucuscule', u'Colimucus', u'Muplodocus'], [u'Mucuscule', u'Colimucus', u'Muplodocus'], [], [u'Brocelome', u'Desseliande'], [u'Brocelome', u'Desseliande'], [u'Pitrouille', u'Banshitrouye'], [u'Pitrouille', u'Banshitrouye'], [u'Pitrouille', u'Banshitrouye'], [u'Pitrouille', u'Banshitrouye'], [u'Pitrouille', u'Banshitrouye'], [u'Pitrouille', u'Banshitrouye'], [u'Pitrouille', u'Banshitrouye'], [u'Pitrouille', u'Banshitrouye'], [u'Grelacon', u'Seracrawl'], [u'Grelacon', u'Seracrawl'], [u'Sonistrelle', u'Bruyverne'], [u'Sonistrelle', u'Bruyverne'], [], [], []]

# //        perName.get("Rattatac").evolutions = new Pokemon[]{perName.get("Rattata"),perName.get("Rattatac")};
# //        perName.get("Porygon-Z").evolutions = new Pokemon[]{perName.get("Porygon"),perName.get("Porygon2"),perName.get("Porygon-Z")};
# //        perName.get("Baggiguane").evolutions = new Pokemon[]{perName.get("Baggiguane"),perName.get("Baggaid")};
# //        perName.get("Noadkoko").evolutions = new Pokemon[]{perName.get("Noeunoeuf"),perName.get("Noadkoko")};
# //        perName.get("Gueriaigle").evolutions = new Pokemon[]{perName.get("Furaiglon"),perName.get("Gueriaigle")};
# //        perName.get("Polichombr").evolutions = new Pokemon[]{perName.get("Polichombr"),perName.get("Branette"),perName.get("Mega-Branette")};
# //        perName.get("Gaulet").evolutions = new Pokemon[]{perName.get("Trompignon"),perName.get("Gaulet")};
# //        perName.get("Hyporoi").evolutions = new Pokemon[]{perName.get("Hypotrempe"),perName.get("Hypocean"),perName.get("Hyporoi")};
# //        perName.get("Elekable").evolutions = new Pokemon[]{perName.get("Elekid"),perName.get("Elektek"),perName.get("Elekable")};
# //        perName.get("Roussil").evolutions = new Pokemon[]{perName.get("Feunnec"),perName.get("Roussil"),perName.get("Goupelin")};
# //        perName.get("Pashmilla").evolutions = new Pokemon[]{perName.get("Chinchidou"),perName.get("Pashmilla")};
# //        perName.get("Emolga").evolutions = new Pokemon[]{};
# //        perName.get("Grolem").evolutions = new Pokemon[]{perName.get("Racaillou"),perName.get("Gravalanch"),perName.get("Grolem")};
# //        perName.get("Cresselia").evolutions = new Pokemon[]{};
# //        perName.get("Flotoutan").evolutions = new Pokemon[]{perName.get("Flotajou"),perName.get("Flotoutan")};
# //        perName.get("Bekipan").evolutions = new Pokemon[]{perName.get("Goelise"),perName.get("Bekipan")};
# //        perName.get("Mateloutre").evolutions = new Pokemon[]{perName.get("Moustillon"),perName.get("Mateloutre"),perName.get("Clamiral")};
# //        perName.get("Dinoclier").evolutions = new Pokemon[]{perName.get("Dinoclier"),perName.get("Bastiodon")};
# //        perName.get("Absol").evolutions = new Pokemon[]{perName.get("Absol"),perName.get("Mega-Absol")};
# //        perName.get("Azurill").evolutions = new Pokemon[]{perName.get("Azurill"),perName.get("Marill"),perName.get("Azumarill")};
# //        perName.get("Apireine").evolutions = new Pokemon[]{perName.get("Apitrini"),perName.get("Apireine")};
# //        perName.get("Dracaufeu").evolutions = new Pokemon[]{perName.get("Salameche"),perName.get("Reptincel"),perName.get("Dracaufeu"),perName.get("Mega-Dracaufeu X"),perName.get("Mega-Dracaufeu Y")};
# //        perName.get("Solochi").evolutions = new Pokemon[]{perName.get("Solochi"),perName.get("Diamat"),perName.get("Trioxhydre")};
# //        perName.get("Motisma (Forme Tonte)").evolutions = new Pokemon[]{};
# //        perName.get("Volcaropod").evolutions = new Pokemon[]{perName.get("Limagma"),perName.get("Volcaropod")};
# //        perName.get("Boreas (Forme Totemique)").evolutions = new Pokemon[]{};
# //        perName.get("Meloetta (Forme Voix)").evolutions = new Pokemon[]{};
# //        perName.get("Snubbull").evolutions = new Pokemon[]{perName.get("Snubbull"),perName.get("Granbull")};
# //        perName.get("Sharpedo").evolutions = new Pokemon[]{perName.get("Carvanha"),perName.get("Sharpedo")};
# //        perName.get("Motisma (Forme Froid)").evolutions = new Pokemon[]{};
# //        perName.get("Mega-Mewtwo Y").evolutions = new Pokemon[]{perName.get("Mewtwo"),perName.get("Mega-Mewtwo X"),perName.get("Mega-Mewtwo Y")};
# //        perName.get("Tutafeh").evolutions = new Pokemon[]{perName.get("Tutafeh"),perName.get("Tutankafer")};
# //        perName.get("Noctunoir").evolutions = new Pokemon[]{perName.get("Skelenox"),perName.get("Teraclope"),perName.get("Noctunoir")};
# //        perName.get("Melodelfe").evolutions = new Pokemon[]{perName.get("Melo"),perName.get("Melofee"),perName.get("Melodelfe")};
# //        perName.get("Mega-Mewtwo X").evolutions = new Pokemon[]{perName.get("Mewtwo"),perName.get("Mega-Mewtwo X"),perName.get("Mega-Mewtwo Y")};
# //        perName.get("Celebi").evolutions = new Pokemon[]{};
# //        perName.get("Cocotine").evolutions = new Pokemon[]{perName.get("Fluvetin"),perName.get("Cocotine")};
# //        perName.get("Zorua").evolutions = new Pokemon[]{perName.get("Zorua"),perName.get("Zoroark")};
# //        perName.get("Mega-Elecsprint").evolutions = new Pokemon[]{perName.get("Dynavolt"),perName.get("Elecsprint"),perName.get("Mega-Elecsprint")};
# //        perName.get("Carabing").evolutions = new Pokemon[]{perName.get("Carabing"),perName.get("Lancargot")};
# //        perName.get("Okeoke").evolutions = new Pokemon[]{perName.get("Okeoke"),perName.get("Qulbutoke")};
# //        perName.get("Hypotrempe").evolutions = new Pokemon[]{perName.get("Hypotrempe"),perName.get("Hypocean"),perName.get("Hyporoi")};
# //        perName.get("Nymphali").evolutions = new Pokemon[]{perName.get("Evoli"),perName.get("Aquali"),perName.get("Voltali"),perName.get("Pyroli"),perName.get("Mentali"),perName.get("Noctali"),perName.get("Phyllali"),perName.get("Givrali"),perName.get("Nymphali")};
# //        perName.get("Venalgue").evolutions = new Pokemon[]{perName.get("Venalgue"),perName.get("Kravarech")};
# //        perName.get("Mega-Scarabrute").evolutions = new Pokemon[]{perName.get("Scarabrute"),perName.get("Mega-Scarabrute")};
# //        perName.get("Maraiste").evolutions = new Pokemon[]{perName.get("Axoloto"),perName.get("Maraiste")};
# //        perName.get("Mega-Florizarre").evolutions = new Pokemon[]{perName.get("Bulbizarre"),perName.get("Herbizarre"),perName.get("Florizarre"),perName.get("Mega-Florizarre")};
# //        perName.get("Papilusion").evolutions = new Pokemon[]{perName.get("Chenipan"),perName.get("Chrysacier"),perName.get("Papilusion")};
# //        perName.get("Charpenti").evolutions = new Pokemon[]{perName.get("Charpenti"),perName.get("Ouvrifier"),perName.get("Betochef")};
# //        perName.get("Doduo").evolutions = new Pokemon[]{perName.get("Doduo"),perName.get("Dodrio")};
# //        perName.get("Coatox").evolutions = new Pokemon[]{perName.get("Cradopaud"),perName.get("Coatox")};
# //        perName.get("Charmina").evolutions = new Pokemon[]{perName.get("Meditikka"),perName.get("Charmina"),perName.get("Mega-Charmina")};
# //        perName.get("Voltali").evolutions = new Pokemon[]{perName.get("Evoli"),perName.get("Aquali"),perName.get("Voltali"),perName.get("Pyroli"),perName.get("Mentali"),perName.get("Noctali"),perName.get("Phyllali"),perName.get("Givrali"),perName.get("Nymphali")};
# //        perName.get("Pitrouille (Taille Maxi)").evolutions = new Pokemon[]{};
# //        perName.get("Cheniselle (Cape Dechet)").evolutions = new Pokemon[]{perName.get("Cheniti"),perName.get("Cheniselle (Cape Dechet)"),perName.get("Papilord")};
# //        perName.get("Exagide (Forme Assaut)").evolutions = new Pokemon[]{perName.get("Monorpale"),perName.get("Dimocles"),perName.get("Exagide (Forme Assaut)")};
# //        perName.get("Joliflor").evolutions = new Pokemon[]{perName.get("Mystherbe"),perName.get("Ortide"),perName.get("Rafflesia"),perName.get("Joliflor")};
# //        perName.get("Tarsal").evolutions = new Pokemon[]{perName.get("Tarsal"),perName.get("Kirlia"),perName.get("Gardevoir"),perName.get("Gallame"),perName.get("Mega-Gardevoir")};
# //        perName.get("Scalpion").evolutions = new Pokemon[]{perName.get("Scalpion"),perName.get("Scalproie")};
# //        perName.get("Galegon").evolutions = new Pokemon[]{perName.get("Galekid"),perName.get("Galegon"),perName.get("Galeking"),perName.get("Mega-Galeking")};
# //        perName.get("Smogogo").evolutions = new Pokemon[]{perName.get("Smogo"),perName.get("Smogogo")};
# //        perName.get("Baudrive").evolutions = new Pokemon[]{perName.get("Baudrive"),perName.get("Grodrive")};
# //        perName.get("Libegon").evolutions = new Pokemon[]{perName.get("Kraknoix"),perName.get("Vibraninf"),perName.get("Libegon")};
# //        perName.get("Pomdepik").evolutions = new Pokemon[]{perName.get("Pomdepik"),perName.get("Foretress")};
# //        perName.get("Korillon").evolutions = new Pokemon[]{perName.get("Korillon"),perName.get("Eoko")};
# //        perName.get("Boguerisse").evolutions = new Pokemon[]{perName.get("Marisson"),perName.get("Boguerisse"),perName.get("Blindepique")};
# //        perName.get("Mime Jr.").evolutions = new Pokemon[]{perName.get("Mime Jr."),perName.get("M. Mime")};
# //        perName.get("Queulorior").evolutions = new Pokemon[]{};
# //        perName.get("Ecremeuh").evolutions = new Pokemon[]{};
# //        perName.get("Lineon").evolutions = new Pokemon[]{perName.get("Zigzaton"),perName.get("Lineon")};
# //        perName.get("Osselait").evolutions = new Pokemon[]{perName.get("Osselait"),perName.get("Ossatueur")};
# //        perName.get("Castorno").evolutions = new Pokemon[]{perName.get("Keunotor"),perName.get("Castorno")};
# //        perName.get("Hypnomade").evolutions = new Pokemon[]{perName.get("Soporifik"),perName.get("Hypnomade")};
# //        perName.get("Lilia").evolutions = new Pokemon[]{perName.get("Lilia"),perName.get("Vacilys")};
# //        perName.get("Motisma (Forme Helice)").evolutions = new Pokemon[]{};
# //        perName.get("Kranidos").evolutions = new Pokemon[]{perName.get("Kranidos"),perName.get("Charkos")};
# //        perName.get("Mammochon").evolutions = new Pokemon[]{perName.get("Marcacrin"),perName.get("Cochignon"),perName.get("Mammochon")};
# //        perName.get("Moufouette").evolutions = new Pokemon[]{perName.get("Moufouette"),perName.get("Moufflair")};
# //        perName.get("Miasmax").evolutions = new Pokemon[]{perName.get("Miamiasme"),perName.get("Miasmax")};
# //        perName.get("Aflamanoir").evolutions = new Pokemon[]{};
# //        perName.get("Makuhita").evolutions = new Pokemon[]{perName.get("Makuhita"),perName.get("Hariyama")};
# //        perName.get("Cerfrousse").evolutions = new Pokemon[]{};
# //        perName.get("Alakazam").evolutions = new Pokemon[]{perName.get("Abra"),perName.get("Kadabra"),perName.get("Alakazam"),perName.get("Mega-Alakazam")};
# //        perName.get("Mega-Dracaufeu X").evolutions = new Pokemon[]{perName.get("Salameche"),perName.get("Reptincel"),perName.get("Dracaufeu"),perName.get("Mega-Dracaufeu X"),perName.get("Mega-Dracaufeu Y")};
# //        perName.get("Reptincel").evolutions = new Pokemon[]{perName.get("Salameche"),perName.get("Reptincel"),perName.get("Dracaufeu"),perName.get("Mega-Dracaufeu X"),perName.get("Mega-Dracaufeu Y")};
# //        perName.get("Carapagos").evolutions = new Pokemon[]{perName.get("Carapagos"),perName.get("Megapagos")};
# //        perName.get("Hypocean").evolutions = new Pokemon[]{perName.get("Hypotrempe"),perName.get("Hypocean"),perName.get("Hyporoi")};
# //        perName.get("Tortipouss").evolutions = new Pokemon[]{perName.get("Tortipouss"),perName.get("Boskara"),perName.get("Torterra")};
# //        perName.get("Stalgamin").evolutions = new Pokemon[]{perName.get("Stalgamin"),perName.get("Oniglali"),perName.get("Momartik")};
# //        perName.get("Lancargot").evolutions = new Pokemon[]{perName.get("Carabing"),perName.get("Lancargot")};
# //        perName.get("Chuchmur").evolutions = new Pokemon[]{perName.get("Chuchmur"),perName.get("Ramboum"),perName.get("Brouhabam")};
# //        perName.get("Motisma (Forme Normale)").evolutions = new Pokemon[]{};
# //        perName.get("Maganon").evolutions = new Pokemon[]{perName.get("Magby"),perName.get("Magmar"),perName.get("Maganon")};
# //        perName.get("Parecool").evolutions = new Pokemon[]{perName.get("Parecool"),perName.get("Vigoroth"),perName.get("Monaflemit")};
# //        perName.get("Wattouat").evolutions = new Pokemon[]{perName.get("Wattouat"),perName.get("Lainergie"),perName.get("Pharamp"),perName.get("Mega-Pharamp")};
# //        perName.get("Opermine").evolutions = new Pokemon[]{perName.get("Opermine"),perName.get("Golgopathe")};
# //        perName.get("Prinplouf").evolutions = new Pokemon[]{perName.get("Tiplouf"),perName.get("Prinplouf"),perName.get("Pingoleon")};
# //        perName.get("Anchwatt").evolutions = new Pokemon[]{perName.get("Anchwatt"),perName.get("Lamperoie"),perName.get("Ohmassacre")};
# //        perName.get("Posipi").evolutions = new Pokemon[]{};
# //        perName.get("Exagide (Forme Parade)").evolutions = new Pokemon[]{perName.get("Monorpale"),perName.get("Dimocles"),perName.get("Exagide (Forme Parade)")};
# //        perName.get("Elekid").evolutions = new Pokemon[]{perName.get("Elekid"),perName.get("Elektek"),perName.get("Elekable")};
# //        perName.get("Flambusard").evolutions = new Pokemon[]{perName.get("Passerouge"),perName.get("Braisillon"),perName.get("Flambusard")};
# //        perName.get("Balbuto").evolutions = new Pokemon[]{perName.get("Balbuto"),perName.get("Kaorine")};
# //        perName.get("Yanma").evolutions = new Pokemon[]{perName.get("Yanma"),perName.get("Yanmega")};
# //        perName.get("Poichigeon").evolutions = new Pokemon[]{perName.get("Poichigeon"),perName.get("Colombeau"),perName.get("Deflaisan")};
# //        perName.get("Lamperoie").evolutions = new Pokemon[]{perName.get("Anchwatt"),perName.get("Lamperoie"),perName.get("Ohmassacre")};
# //        perName.get("Kirlia").evolutions = new Pokemon[]{perName.get("Tarsal"),perName.get("Kirlia"),perName.get("Gardevoir"),perName.get("Gallame"),perName.get("Mega-Gardevoir")};
# //        perName.get("Couaneton").evolutions = new Pokemon[]{perName.get("Couaneton"),perName.get("Lakmecygne")};
# //        perName.get("Mystherbe").evolutions = new Pokemon[]{perName.get("Mystherbe"),perName.get("Ortide"),perName.get("Rafflesia"),perName.get("Joliflor")};
# //        perName.get("Metang").evolutions = new Pokemon[]{perName.get("Terhal"),perName.get("Metang"),perName.get("Metalosse")};
# //        perName.get("Tritosor").evolutions = new Pokemon[]{perName.get("Sancoki"),perName.get("Tritosor")};
# //        perName.get("Dracolosse").evolutions = new Pokemon[]{perName.get("Minidraco"),perName.get("Draco"),perName.get("Dracolosse")};
# //        perName.get("Fragilady").evolutions = new Pokemon[]{perName.get("Chlorobule"),perName.get("Fragilady")};
# //        perName.get("Genesect").evolutions = new Pokemon[]{};
# //        perName.get("Nidorino").evolutions = new Pokemon[]{perName.get("Nidoran M"),perName.get("Nidorino"),perName.get("Nidoking")};
# //        perName.get("Branette").evolutions = new Pokemon[]{perName.get("Polichombr"),perName.get("Branette"),perName.get("Mega-Branette")};
# //        perName.get("Nidorina").evolutions = new Pokemon[]{perName.get("Nidoran F"),perName.get("Nidorina"),perName.get("Nidoqueen")};
# //        perName.get("Rhinoferos").evolutions = new Pokemon[]{perName.get("Rhinocorne"),perName.get("Rhinoferos"),perName.get("Rhinastoc")};
# //        perName.get("Regigigas").evolutions = new Pokemon[]{};
# //        perName.get("Tentacruel").evolutions = new Pokemon[]{perName.get("Tentacool"),perName.get("Tentacruel")};
# //        perName.get("Chlorobule").evolutions = new Pokemon[]{perName.get("Chlorobule"),perName.get("Fragilady")};
# //        perName.get("Darumacho (Mode Daruma)").evolutions = new Pokemon[]{perName.get("Darumarond"),perName.get("Darumacho (Mode Daruma)")};
# //        perName.get("Ferosinge").evolutions = new Pokemon[]{perName.get("Ferosinge"),perName.get("Colossinge")};
# //        perName.get("Flagadoss").evolutions = new Pokemon[]{perName.get("Ramoloss"),perName.get("Flagadoss"),perName.get("Roigada")};
# //        perName.get("Crikzik").evolutions = new Pokemon[]{perName.get("Crikzik"),perName.get("Melokrik")};
# //        perName.get("Florges").evolutions = new Pokemon[]{perName.get("Flabebe"),perName.get("Floette"),perName.get("Florges")};
# //        perName.get("Scarabrute").evolutions = new Pokemon[]{perName.get("Scarabrute"),perName.get("Mega-Scarabrute")};
# //        perName.get("Mimigal").evolutions = new Pokemon[]{perName.get("Mimigal"),perName.get("Migalos")};
# //        perName.get("Dodrio").evolutions = new Pokemon[]{perName.get("Doduo"),perName.get("Dodrio")};
# //        perName.get("Pijako").evolutions = new Pokemon[]{};
# //        perName.get("Lepidonille").evolutions = new Pokemon[]{perName.get("Lepidonille"),perName.get("Peregrain"),perName.get("Prismillon")};
# //        perName.get("Bargantua").evolutions = new Pokemon[]{};
# //        perName.get("Chrysacier").evolutions = new Pokemon[]{perName.get("Chenipan"),perName.get("Chrysacier"),perName.get("Papilusion")};
# //        perName.get("Electrode").evolutions = new Pokemon[]{perName.get("Voltorbe"),perName.get("Electrode")};
# //        perName.get("Sorbebe").evolutions = new Pokemon[]{perName.get("Sorbebe"),perName.get("Sorboul"),perName.get("Sorbouboul")};
# //        perName.get("Givrali").evolutions = new Pokemon[]{perName.get("Evoli"),perName.get("Aquali"),perName.get("Voltali"),perName.get("Pyroli"),perName.get("Mentali"),perName.get("Noctali"),perName.get("Phyllali"),perName.get("Givrali"),perName.get("Nymphali")};
# //        perName.get("Gloupti").evolutions = new Pokemon[]{perName.get("Gloupti"),perName.get("Avaltout")};
# //        perName.get("Gringolem").evolutions = new Pokemon[]{perName.get("Gringolem"),perName.get("Golemastoc")};
# //        perName.get("Miamiasme").evolutions = new Pokemon[]{perName.get("Miamiasme"),perName.get("Miasmax")};
# //        perName.get("Togepi").evolutions = new Pokemon[]{perName.get("Togepi"),perName.get("Togetic"),perName.get("Togekiss")};
# //        perName.get("Corboss").evolutions = new Pokemon[]{perName.get("Cornebre"),perName.get("Corboss")};
# //        perName.get("Flamajou").evolutions = new Pokemon[]{perName.get("Flamajou"),perName.get("Flamoutan")};
# //        perName.get("Etourvol").evolutions = new Pokemon[]{perName.get("Etourmi"),perName.get("Etourvol"),perName.get("Etouraptor")};
# //        perName.get("Abo").evolutions = new Pokemon[]{perName.get("Abo"),perName.get("Arbok")};
# //        perName.get("Obalie").evolutions = new Pokemon[]{perName.get("Obalie"),perName.get("Phogleur"),perName.get("Kaimorse")};
# //        perName.get("Octillery").evolutions = new Pokemon[]{perName.get("Remoraid"),perName.get("Octillery")};
# //        perName.get("Feuillajou").evolutions = new Pokemon[]{perName.get("Feuillajou"),perName.get("Feuiloutan")};
# //        perName.get("Zygarde").evolutions = new Pokemon[]{};
# //        perName.get("Pikachu").evolutions = new Pokemon[]{perName.get("Pichu"),perName.get("Pikachu"),perName.get("Raichu")};
# //        perName.get("Zoroark").evolutions = new Pokemon[]{perName.get("Zorua"),perName.get("Zoroark")};
# //        perName.get("Mega-Mysdibule").evolutions = new Pokemon[]{perName.get("Mysdibule"),perName.get("Mega-Mysdibule")};
# //        perName.get("Nodulithe").evolutions = new Pokemon[]{perName.get("Nodulithe"),perName.get("Geolithe"),perName.get("Gigalithe")};
# //        perName.get("Rhinastoc").evolutions = new Pokemon[]{perName.get("Rhinocorne"),perName.get("Rhinoferos"),perName.get("Rhinastoc")};
# //        perName.get("Mega-Gardevoir").evolutions = new Pokemon[]{perName.get("Tarsal"),perName.get("Kirlia"),perName.get("Gardevoir"),perName.get("Gallame"),perName.get("Mega-Gardevoir")};
# //        perName.get("Mega-Brasegali").evolutions = new Pokemon[]{perName.get("Poussifeu"),perName.get("Galifeu"),perName.get("Brasegali"),perName.get("Mega-Brasegali")};
# //        perName.get("Grainipiot").evolutions = new Pokemon[]{perName.get("Grainipiot"),perName.get("Pifeuil"),perName.get("Tengalice")};
# //        perName.get("Qwilfish").evolutions = new Pokemon[]{};
# //        perName.get("Carchacrok").evolutions = new Pokemon[]{perName.get("Griknot"),perName.get("Carmache"),perName.get("Carchacrok"),perName.get("Mega-Carchacrok")};
# //        perName.get("Latios").evolutions = new Pokemon[]{};
# //        perName.get("Groret").evolutions = new Pokemon[]{perName.get("Spoink"),perName.get("Groret")};
# //        perName.get("Cheniselle (Cape Plante)").evolutions = new Pokemon[]{perName.get("Cheniti"),perName.get("Cheniselle (Cape Plante)"),perName.get("Papilord")};
# //        perName.get("Oniglali").evolutions = new Pokemon[]{perName.get("Stalgamin"),perName.get("Oniglali"),perName.get("Momartik")};
# //        perName.get("Steelix").evolutions = new Pokemon[]{perName.get("Onix"),perName.get("Steelix")};
# //        perName.get("Crefollet").evolutions = new Pokemon[]{};
# //        perName.get("Electhor").evolutions = new Pokemon[]{};
# //        perName.get("Phanpy").evolutions = new Pokemon[]{perName.get("Phanpy"),perName.get("Donphan")};
# //        perName.get("Crehelf").evolutions = new Pokemon[]{};
# //        perName.get("Ortide").evolutions = new Pokemon[]{perName.get("Mystherbe"),perName.get("Ortide"),perName.get("Rafflesia"),perName.get("Joliflor")};
# //        perName.get("Metalosse").evolutions = new Pokemon[]{perName.get("Terhal"),perName.get("Metang"),perName.get("Metalosse")};
# //        perName.get("Azumarill").evolutions = new Pokemon[]{perName.get("Azurill"),perName.get("Marill"),perName.get("Azumarill")};
# //        perName.get("Kyogre").evolutions = new Pokemon[]{};
# //        perName.get("Mega-Branette").evolutions = new Pokemon[]{perName.get("Polichombr"),perName.get("Branette"),perName.get("Mega-Branette")};
# //        perName.get("Scorplane").evolutions = new Pokemon[]{perName.get("Scorplane"),perName.get("Scorvol")};
# //        perName.get("Chenipotte").evolutions = new Pokemon[]{perName.get("Chenipotte"),perName.get("Armulys"),perName.get("Blindalys"),perName.get("Charmillon"),perName.get("Papinox")};
# //        perName.get("Elektek").evolutions = new Pokemon[]{perName.get("Elekid"),perName.get("Elektek"),perName.get("Elekable")};
# //        perName.get("Vigoroth").evolutions = new Pokemon[]{perName.get("Parecool"),perName.get("Vigoroth"),perName.get("Monaflemit")};
# //        perName.get("Leveinard").evolutions = new Pokemon[]{perName.get("Ptiravi"),perName.get("Leveinard"),perName.get("Leuphorie")};
# //        perName.get("Fouinar").evolutions = new Pokemon[]{perName.get("Fouinette"),perName.get("Fouinar")};
# //        perName.get("Simularbre").evolutions = new Pokemon[]{perName.get("Manzai"),perName.get("Simularbre")};
# //        perName.get("Polagriffe").evolutions = new Pokemon[]{perName.get("Polarhume"),perName.get("Polagriffe")};
# //        perName.get("Maracachi").evolutions = new Pokemon[]{};
# //        perName.get("Dragmara").evolutions = new Pokemon[]{perName.get("Amagara"),perName.get("Dragmara")};
# //        perName.get("Insecateur").evolutions = new Pokemon[]{perName.get("Insecateur"),perName.get("Cizayox"),perName.get("Mega-Cizayox")};
# //        perName.get("Laporeille").evolutions = new Pokemon[]{perName.get("Laporeille"),perName.get("Lockpin")};
# //        perName.get("Hoot-hoot").evolutions = new Pokemon[]{perName.get("Hoot-hoot"),perName.get("Noarfang")};
# //        perName.get("Lokhlass").evolutions = new Pokemon[]{};
# //        perName.get("Spiritomb").evolutions = new Pokemon[]{};
# //        perName.get("Limagma").evolutions = new Pokemon[]{perName.get("Limagma"),perName.get("Volcaropod")};
# //        perName.get("Paras").evolutions = new Pokemon[]{perName.get("Paras"),perName.get("Parasect")};
# //        perName.get("Pyronille").evolutions = new Pokemon[]{perName.get("Pyronille"),perName.get("Pyrax")};
# //        perName.get("Symbios").evolutions = new Pokemon[]{perName.get("Nucleos"),perName.get("Meios"),perName.get("Symbios")};
# //        perName.get("Melo").evolutions = new Pokemon[]{perName.get("Melo"),perName.get("Melofee"),perName.get("Melodelfe")};
# //        perName.get("Lianaja").evolutions = new Pokemon[]{perName.get("Vipelierre"),perName.get("Lianaja"),perName.get("Majaspic")};
# //        perName.get("Arcko").evolutions = new Pokemon[]{perName.get("Arcko"),perName.get("Massko"),perName.get("Jungko")};
# //        perName.get("Archeomire").evolutions = new Pokemon[]{perName.get("Archeomire"),perName.get("Archeodong")};
# //        perName.get("Banshitrouye (Taille Normale)").evolutions = new Pokemon[]{};
# //        perName.get("Feuforeve").evolutions = new Pokemon[]{perName.get("Feuforeve"),perName.get("Magireve")};
# //        perName.get("Mega-Tortank").evolutions = new Pokemon[]{perName.get("Carapuce"),perName.get("Carabaffe"),perName.get("Tortank"),perName.get("Mega-Tortank")};
# //        perName.get("Venipatte").evolutions = new Pokemon[]{perName.get("Venipatte"),perName.get("Scobolide"),perName.get("Brutapode")};
# //        perName.get("Doudouvet").evolutions = new Pokemon[]{perName.get("Doudouvet"),perName.get("Farfaduvet")};
# //        perName.get("Lamantine").evolutions = new Pokemon[]{perName.get("Otaria"),perName.get("Lamantine")};
# //        perName.get("Parasect").evolutions = new Pokemon[]{perName.get("Paras"),perName.get("Parasect")};
# //        perName.get("Avaltout").evolutions = new Pokemon[]{perName.get("Gloupti"),perName.get("Avaltout")};
# //        perName.get("Voltorbe").evolutions = new Pokemon[]{perName.get("Voltorbe"),perName.get("Electrode")};
# //        perName.get("Magicarpe").evolutions = new Pokemon[]{perName.get("Magicarpe"),perName.get("Leviator"),perName.get("Mega-Leviator")};
# //        perName.get("Darumacho (Mode Normal)").evolutions = new Pokemon[]{perName.get("Darumarond"),perName.get("Darumacho (Mode Normal)")};
# //        perName.get("Heledelle").evolutions = new Pokemon[]{perName.get("Nirondelle"),perName.get("Heledelle")};
# //        perName.get("Noacier").evolutions = new Pokemon[]{perName.get("Grindur"),perName.get("Noacier")};
# //        perName.get("Laggron").evolutions = new Pokemon[]{perName.get("Gobou"),perName.get("Flobio"),perName.get("Laggron")};
# //        perName.get("Gobou").evolutions = new Pokemon[]{perName.get("Gobou"),perName.get("Flobio"),perName.get("Laggron")};
# //        perName.get("Canarticho").evolutions = new Pokemon[]{};
# //        perName.get("Groudon").evolutions = new Pokemon[]{};
# //        perName.get("Blizzaroi").evolutions = new Pokemon[]{perName.get("Blizzi"),perName.get("Blizzaroi"),perName.get("Mega-Blizzaroi")};
# //        perName.get("Tournegrin").evolutions = new Pokemon[]{perName.get("Tournegrin"),perName.get("Heliatronc")};
# //        perName.get("Nidoqueen").evolutions = new Pokemon[]{perName.get("Nidoran F"),perName.get("Nidorina"),perName.get("Nidoqueen")};
# //        perName.get("Altaria").evolutions = new Pokemon[]{perName.get("Tylton"),perName.get("Altaria")};
# //        perName.get("Roucool").evolutions = new Pokemon[]{perName.get("Roucool"),perName.get("Roucoups"),perName.get("Roucarnage")};
# //        perName.get("Cradopaud").evolutions = new Pokemon[]{perName.get("Cradopaud"),perName.get("Coatox")};
# //        perName.get("Malosse").evolutions = new Pokemon[]{perName.get("Malosse"),perName.get("Demolosse"),perName.get("Mega-Demolosse")};
# //        perName.get("Vaututrice").evolutions = new Pokemon[]{perName.get("Vostourno"),perName.get("Vaututrice")};
# //        perName.get("Togekiss").evolutions = new Pokemon[]{perName.get("Togepi"),perName.get("Togetic"),perName.get("Togekiss")};
# //        perName.get("Tritonde").evolutions = new Pokemon[]{perName.get("Tritonde"),perName.get("Batracne"),perName.get("Crapustule")};
# //        perName.get("Moufflair").evolutions = new Pokemon[]{perName.get("Moufouette"),perName.get("Moufflair")};
# //        perName.get("Tiplouf").evolutions = new Pokemon[]{perName.get("Tiplouf"),perName.get("Prinplouf"),perName.get("Pingoleon")};
# //        perName.get("Lumivole").evolutions = new Pokemon[]{};
# //        perName.get("Carmache").evolutions = new Pokemon[]{perName.get("Griknot"),perName.get("Carmache"),perName.get("Carchacrok"),perName.get("Mega-Carchacrok")};
# //        perName.get("Cliticlic").evolutions = new Pokemon[]{perName.get("Tic"),perName.get("Clic"),perName.get("Cliticlic")};
# //        perName.get("Giratina (Forme Originelle)").evolutions = new Pokemon[]{};
# //        perName.get("Poussifeu").evolutions = new Pokemon[]{perName.get("Poussifeu"),perName.get("Galifeu"),perName.get("Brasegali"),perName.get("Mega-Brasegali")};
# //        perName.get("Limaspeed").evolutions = new Pokemon[]{perName.get("Escargaume"),perName.get("Limaspeed")};
# //        perName.get("Iguolta").evolutions = new Pokemon[]{perName.get("Galvaran"),perName.get("Iguolta")};
# //        perName.get("Cheniti").evolutions = new Pokemon[]{perName.get("Cheniti"),perName.get("Cheniselle (Cape Plante)"),perName.get("Papilord")};
# //        perName.get("Kapoera").evolutions = new Pokemon[]{perName.get("Debugant"),perName.get("Kicklee"),perName.get("Tygnon"),perName.get("Kapoera")};
# //        perName.get("Pachirisu").evolutions = new Pokemon[]{};
# //        perName.get("Marill").evolutions = new Pokemon[]{perName.get("Azurill"),perName.get("Marill"),perName.get("Azumarill")};
# //        perName.get("Mega-Lucario").evolutions = new Pokemon[]{perName.get("Riolu"),perName.get("Lucario"),perName.get("Mega-Lucario")};
# //        perName.get("Skitty").evolutions = new Pokemon[]{perName.get("Skitty"),perName.get("Delcatty")};
# //        perName.get("Abra").evolutions = new Pokemon[]{perName.get("Abra"),perName.get("Kadabra"),perName.get("Alakazam"),perName.get("Mega-Alakazam")};
# //        perName.get("Couverdure").evolutions = new Pokemon[]{perName.get("Larveyette"),perName.get("Couverdure"),perName.get("Manternel")};
# //        perName.get("Grodoudou").evolutions = new Pokemon[]{perName.get("Toudoudou"),perName.get("Rondoudou"),perName.get("Grodoudou")};
# //        perName.get("Ptyranidur").evolutions = new Pokemon[]{perName.get("Ptyranidur"),perName.get("Rexillius")};
# //        perName.get("Kecleon").evolutions = new Pokemon[]{};
# //        perName.get("Deoxys (Forme Vitesse)").evolutions = new Pokemon[]{};
# //        perName.get("Crustabri").evolutions = new Pokemon[]{perName.get("Kokiyas"),perName.get("Crustabri")};
# //        perName.get("Motisma (Forme Chaleur)").evolutions = new Pokemon[]{};
# //        perName.get("Galvaran").evolutions = new Pokemon[]{perName.get("Galvaran"),perName.get("Iguolta")};
# //        perName.get("Fluvetin").evolutions = new Pokemon[]{perName.get("Fluvetin"),perName.get("Cocotine")};
# //        perName.get("Haydaim").evolutions = new Pokemon[]{perName.get("Vivaldaim"),perName.get("Haydaim")};
# //        perName.get("Kyurem (Noir)").evolutions = new Pokemon[]{};
# //        perName.get("Hippopotas").evolutions = new Pokemon[]{perName.get("Hippopotas"),perName.get("Hippodocus")};
# //        perName.get("Giratina (Forme Alternative)").evolutions = new Pokemon[]{};
# //        perName.get("Coconfort").evolutions = new Pokemon[]{perName.get("Aspicot"),perName.get("Coconfort"),perName.get("Dardargnan")};
# //        perName.get("Noeunoeuf").evolutions = new Pokemon[]{perName.get("Noeunoeuf"),perName.get("Noadkoko")};
# //        perName.get("Zigzaton").evolutions = new Pokemon[]{perName.get("Zigzaton"),perName.get("Lineon")};
# //        perName.get("Rattata").evolutions = new Pokemon[]{perName.get("Rattata"),perName.get("Rattatac")};
# //        perName.get("Girafarig").evolutions = new Pokemon[]{};
# //        perName.get("Otaria").evolutions = new Pokemon[]{perName.get("Otaria"),perName.get("Lamantine")};
# //        perName.get("Granbull").evolutions = new Pokemon[]{perName.get("Snubbull"),perName.get("Granbull")};
# //        perName.get("Kabutops").evolutions = new Pokemon[]{perName.get("Kabuto"),perName.get("Kabutops")};
# //        perName.get("Ratentif").evolutions = new Pokemon[]{perName.get("Ratentif"),perName.get("Miradar")};
# //        perName.get("Cheniselle (Cape Sol)").evolutions = new Pokemon[]{perName.get("Cheniti"),perName.get("Cheniselle (Cape Sol)"),perName.get("Papilord")};
# //        perName.get("Bulbizarre").evolutions = new Pokemon[]{perName.get("Bulbizarre"),perName.get("Herbizarre"),perName.get("Florizarre"),perName.get("Mega-Florizarre")};
# //        perName.get("Couafarel").evolutions = new Pokemon[]{};
# //        perName.get("Mega-Demolosse").evolutions = new Pokemon[]{perName.get("Malosse"),perName.get("Demolosse"),perName.get("Mega-Demolosse")};
# //        perName.get("Siderella").evolutions = new Pokemon[]{perName.get("Scrutella"),perName.get("Mesmerella"),perName.get("Siderella")};
# //        perName.get("Dedenne").evolutions = new Pokemon[]{};
# //        perName.get("Herbizarre").evolutions = new Pokemon[]{perName.get("Bulbizarre"),perName.get("Herbizarre"),perName.get("Florizarre"),perName.get("Mega-Florizarre")};
# //        perName.get("Lixy").evolutions = new Pokemon[]{perName.get("Lixy"),perName.get("Luxio"),perName.get("Luxray")};
# //        perName.get("Roucarnage").evolutions = new Pokemon[]{perName.get("Roucool"),perName.get("Roucoups"),perName.get("Roucarnage")};
# //        perName.get("Tarinor").evolutions = new Pokemon[]{perName.get("Tarinor"),perName.get("Tarinorme")};
# //        perName.get("Rapasdepic").evolutions = new Pokemon[]{perName.get("Piafabec"),perName.get("Rapasdepic")};
# //        perName.get("Embrylex").evolutions = new Pokemon[]{perName.get("Embrylex"),perName.get("Ymphect"),perName.get("Tyranocif"),perName.get("Mega-Tyranocif")};
# //        perName.get("Togetic").evolutions = new Pokemon[]{perName.get("Togepi"),perName.get("Togetic"),perName.get("Togekiss")};
# //        perName.get("Mega-Galeking").evolutions = new Pokemon[]{perName.get("Galekid"),perName.get("Galegon"),perName.get("Galeking"),perName.get("Mega-Galeking")};
# //        perName.get("Brouhabam").evolutions = new Pokemon[]{perName.get("Chuchmur"),perName.get("Ramboum"),perName.get("Brouhabam")};
# //        perName.get("Babimanta").evolutions = new Pokemon[]{perName.get("Babimanta"),perName.get("Demanta")};
# //        perName.get("Rhinolove").evolutions = new Pokemon[]{perName.get("Chovsourir"),perName.get("Rhinolove")};
# //        perName.get("Florizarre").evolutions = new Pokemon[]{perName.get("Bulbizarre"),perName.get("Herbizarre"),perName.get("Florizarre"),perName.get("Mega-Florizarre")};
# //        perName.get("Clamiral").evolutions = new Pokemon[]{perName.get("Moustillon"),perName.get("Mateloutre"),perName.get("Clamiral")};
# //        perName.get("Ronflex").evolutions = new Pokemon[]{perName.get("Goinfrex"),perName.get("Ronflex")};
# //        perName.get("Kyurem (Blanc)").evolutions = new Pokemon[]{};
# //        perName.get("Grotadmorv").evolutions = new Pokemon[]{perName.get("Tadmorv"),perName.get("Grotadmorv")};
# //        perName.get("Ptitard").evolutions = new Pokemon[]{perName.get("Ptitard"),perName.get("Tetarte"),perName.get("Tartard"),perName.get("Tarpaud")};
# //        perName.get("Mentali").evolutions = new Pokemon[]{perName.get("Evoli"),perName.get("Aquali"),perName.get("Voltali"),perName.get("Pyroli"),perName.get("Mentali"),perName.get("Noctali"),perName.get("Phyllali"),perName.get("Givrali"),perName.get("Nymphali")};
# //        perName.get("Betochef").evolutions = new Pokemon[]{perName.get("Charpenti"),perName.get("Ouvrifier"),perName.get("Betochef")};
# //        perName.get("Stari").evolutions = new Pokemon[]{};
# //        perName.get("Arkeapti").evolutions = new Pokemon[]{perName.get("Arkeapti"),perName.get("Aeropteryx")};
# //        perName.get("Crocorible").evolutions = new Pokemon[]{perName.get("Mascaiman"),perName.get("Escroco"),perName.get("Crocorible")};
# //        perName.get("Heatran").evolutions = new Pokemon[]{};
# //        perName.get("Ponyta").evolutions = new Pokemon[]{perName.get("Ponyta"),perName.get("Galopa")};
# //        perName.get("Crefadet").evolutions = new Pokemon[]{};
# //        perName.get("Escroco").evolutions = new Pokemon[]{perName.get("Mascaiman"),perName.get("Escroco"),perName.get("Crocorible")};
# //        perName.get("Hariyama").evolutions = new Pokemon[]{perName.get("Makuhita"),perName.get("Hariyama")};
# //        perName.get("Qulbutoke").evolutions = new Pokemon[]{perName.get("Okeoke"),perName.get("Qulbutoke")};
# //        perName.get("Staross").evolutions = new Pokemon[]{};
# //        perName.get("Hexagel").evolutions = new Pokemon[]{};
# //        perName.get("Lippouti").evolutions = new Pokemon[]{perName.get("Lippouti"),perName.get("Lippoutou")};
# //        perName.get("Bastiodon").evolutions = new Pokemon[]{perName.get("Dinoclier"),perName.get("Bastiodon")};
# //        perName.get("Peregrain").evolutions = new Pokemon[]{perName.get("Lepidonille"),perName.get("Peregrain"),perName.get("Prismillon")};
# //        perName.get("Carvanha").evolutions = new Pokemon[]{perName.get("Carvanha"),perName.get("Sharpedo")};
# //        perName.get("Pharamp").evolutions = new Pokemon[]{perName.get("Wattouat"),perName.get("Lainergie"),perName.get("Pharamp"),perName.get("Mega-Pharamp")};
# //        perName.get("Mega-Charmina").evolutions = new Pokemon[]{perName.get("Meditikka"),perName.get("Charmina"),perName.get("Mega-Charmina")};
# //        perName.get("Bouldeneu").evolutions = new Pokemon[]{perName.get("Saquedeneu"),perName.get("Bouldeneu")};
# //        perName.get("Heliatronc").evolutions = new Pokemon[]{perName.get("Tournegrin"),perName.get("Heliatronc")};
# //        perName.get("Gamblast").evolutions = new Pokemon[]{perName.get("Flingouste"),perName.get("Gamblast")};
# //        perName.get("Eoko").evolutions = new Pokemon[]{perName.get("Korillon"),perName.get("Eoko")};
# //        perName.get("Brutalibre").evolutions = new Pokemon[]{};
# //        perName.get("Furaiglon").evolutions = new Pokemon[]{perName.get("Furaiglon"),perName.get("Gueriaigle")};
# //        perName.get("Chevroum").evolutions = new Pokemon[]{perName.get("Cabriolaine"),perName.get("Chevroum")};
# //        perName.get("Flamoutan").evolutions = new Pokemon[]{perName.get("Flamajou"),perName.get("Flamoutan")};
# //        perName.get("Prismillon").evolutions = new Pokemon[]{perName.get("Lepidonille"),perName.get("Peregrain"),perName.get("Prismillon")};
# //        perName.get("Sonistrelle").evolutions = new Pokemon[]{perName.get("Sonistrelle"),perName.get("Bruyverne")};
# //        perName.get("Goupix").evolutions = new Pokemon[]{perName.get("Goupix"),perName.get("Feunard")};
# //        perName.get("Gravalanch").evolutions = new Pokemon[]{perName.get("Racaillou"),perName.get("Gravalanch"),perName.get("Grolem")};
# //        perName.get("Nostenfer").evolutions = new Pokemon[]{perName.get("Nosferapti"),perName.get("Nosferalto"),perName.get("Nostenfer")};
# //        perName.get("Chetiflor").evolutions = new Pokemon[]{perName.get("Chetiflor"),perName.get("Boustiflor"),perName.get("Empiflor")};
# //        perName.get("Motisma (Forme Lavage)").evolutions = new Pokemon[]{};
# //        perName.get("Lumineon").evolutions = new Pokemon[]{perName.get("Ecayon"),perName.get("Lumineon")};
# //        perName.get("Croaporal").evolutions = new Pokemon[]{perName.get("Grenousse"),perName.get("Croaporal"),perName.get("Amphinobi")};
# //        perName.get("Rhinocorne").evolutions = new Pokemon[]{perName.get("Rhinocorne"),perName.get("Rhinoferos"),perName.get("Rhinastoc")};
# //        perName.get("Leviator").evolutions = new Pokemon[]{perName.get("Magicarpe"),perName.get("Leviator"),perName.get("Mega-Leviator")};
# //        perName.get("Cryptero").evolutions = new Pokemon[]{};
# //        perName.get("Spoink").evolutions = new Pokemon[]{perName.get("Spoink"),perName.get("Groret")};
# //        perName.get("Dialga").evolutions = new Pokemon[]{};
# //        perName.get("Sabelette").evolutions = new Pokemon[]{perName.get("Sabelette"),perName.get("Sablaireau")};
# //        perName.get("Dynavolt").evolutions = new Pokemon[]{perName.get("Dynavolt"),perName.get("Elecsprint"),perName.get("Mega-Elecsprint")};
# //        perName.get("Pichu").evolutions = new Pokemon[]{perName.get("Pichu"),perName.get("Pikachu"),perName.get("Raichu")};
# //        perName.get("Terrakium").evolutions = new Pokemon[]{};
# //        perName.get("Amagara").evolutions = new Pokemon[]{perName.get("Amagara"),perName.get("Dragmara")};
# //        perName.get("Poissirene").evolutions = new Pokemon[]{perName.get("Poissirene"),perName.get("Poissoroy")};
# //        perName.get("Magby").evolutions = new Pokemon[]{perName.get("Magby"),perName.get("Magmar"),perName.get("Maganon")};
# //        perName.get("Farfaduvet").evolutions = new Pokemon[]{perName.get("Doudouvet"),perName.get("Farfaduvet")};
# //        perName.get("Lockpin").evolutions = new Pokemon[]{perName.get("Laporeille"),perName.get("Lockpin")};
# //        perName.get("Loupio").evolutions = new Pokemon[]{perName.get("Loupio"),perName.get("Lanturn")};
# //        perName.get("Elecsprint").evolutions = new Pokemon[]{perName.get("Dynavolt"),perName.get("Elecsprint"),perName.get("Mega-Elecsprint")};
# //        perName.get("Banshitrouye (Taille Ultra)").evolutions = new Pokemon[]{};
# //        perName.get("Keldeo").evolutions = new Pokemon[]{};
# //        perName.get("Jungko").evolutions = new Pokemon[]{perName.get("Arcko"),perName.get("Massko"),perName.get("Jungko")};
# //        perName.get("Boreas (Forme Avatar)").evolutions = new Pokemon[]{};
# //        perName.get("Registeel").evolutions = new Pokemon[]{};
# //        perName.get("Xatu").evolutions = new Pokemon[]{perName.get("Natu"),perName.get("Xatu")};
# //        perName.get("Skelenox").evolutions = new Pokemon[]{perName.get("Skelenox"),perName.get("Teraclope"),perName.get("Noctunoir")};
# //        perName.get("Etourmi").evolutions = new Pokemon[]{perName.get("Etourmi"),perName.get("Etourvol"),perName.get("Etouraptor")};
# //        perName.get("Aeromite").evolutions = new Pokemon[]{perName.get("Mimitoss"),perName.get("Aeromite")};
# //        perName.get("Tortank").evolutions = new Pokemon[]{perName.get("Carapuce"),perName.get("Carabaffe"),perName.get("Tortank"),perName.get("Mega-Tortank")};
# //        perName.get("Mega-Cizayox").evolutions = new Pokemon[]{perName.get("Insecateur"),perName.get("Cizayox"),perName.get("Mega-Cizayox")};
# //        perName.get("Minidraco").evolutions = new Pokemon[]{perName.get("Minidraco"),perName.get("Draco"),perName.get("Dracolosse")};
# //        perName.get("Trioxhydre").evolutions = new Pokemon[]{perName.get("Solochi"),perName.get("Diamat"),perName.get("Trioxhydre")};
# //        perName.get("Melofee").evolutions = new Pokemon[]{perName.get("Melo"),perName.get("Melofee"),perName.get("Melodelfe")};
# //        perName.get("Crabicoque").evolutions = new Pokemon[]{perName.get("Crabicoque"),perName.get("Crabaraque")};
# //        perName.get("Torterra").evolutions = new Pokemon[]{perName.get("Tortipouss"),perName.get("Boskara"),perName.get("Torterra")};
# //        perName.get("Rototaupe").evolutions = new Pokemon[]{perName.get("Rototaupe"),perName.get("Minotaupe")};
# //        perName.get("Ceribou").evolutions = new Pokemon[]{perName.get("Ceribou"),perName.get("Ceriflor")};
# //        perName.get("Keunotor").evolutions = new Pokemon[]{perName.get("Keunotor"),perName.get("Castorno")};
# //        perName.get("Nidoran F").evolutions = new Pokemon[]{perName.get("Nidoran F"),perName.get("Nidorina"),perName.get("Nidoqueen")};
# //        perName.get("Helionceau").evolutions = new Pokemon[]{perName.get("Helionceau"),perName.get("Nemelios")};
# //        perName.get("Entei").evolutions = new Pokemon[]{};
# //        perName.get("Nidoran M").evolutions = new Pokemon[]{perName.get("Nidoran M"),perName.get("Nidorino"),perName.get("Nidoking")};
# //        perName.get("Moustillon").evolutions = new Pokemon[]{perName.get("Moustillon"),perName.get("Mateloutre"),perName.get("Clamiral")};
# //        perName.get("Mygavolt").evolutions = new Pokemon[]{perName.get("Statitik"),perName.get("Mygavolt")};
# //        perName.get("Soporifik").evolutions = new Pokemon[]{perName.get("Soporifik"),perName.get("Hypnomade")};
# //        perName.get("Dimocles").evolutions = new Pokemon[]{perName.get("Monorpale"),perName.get("Dimocles"),perName.get("Exagide (Forme Assaut)")};
# //        perName.get("Riolu").evolutions = new Pokemon[]{perName.get("Riolu"),perName.get("Lucario"),perName.get("Mega-Lucario")};
# //        perName.get("Aspicot").evolutions = new Pokemon[]{perName.get("Aspicot"),perName.get("Coconfort"),perName.get("Dardargnan")};
# //        perName.get("Marcacrin").evolutions = new Pokemon[]{perName.get("Marcacrin"),perName.get("Cochignon"),perName.get("Mammochon")};
# //        perName.get("Mysdibule").evolutions = new Pokemon[]{perName.get("Mysdibule"),perName.get("Mega-Mysdibule")};
# //        perName.get("Chartor").evolutions = new Pokemon[]{};
# //        perName.get("Minotaupe").evolutions = new Pokemon[]{perName.get("Rototaupe"),perName.get("Minotaupe")};
# //        perName.get("Maskadra").evolutions = new Pokemon[]{perName.get("Arakdo"),perName.get("Maskadra")};
# //        perName.get("Yanmega").evolutions = new Pokemon[]{perName.get("Yanma"),perName.get("Yanmega")};
# //        perName.get("Melokrik").evolutions = new Pokemon[]{perName.get("Crikzik"),perName.get("Melokrik")};
# //        perName.get("Scobolide").evolutions = new Pokemon[]{perName.get("Venipatte"),perName.get("Scobolide"),perName.get("Brutapode")};
# //        perName.get("Massko").evolutions = new Pokemon[]{perName.get("Arcko"),perName.get("Massko"),perName.get("Jungko")};
# //        perName.get("Brasegali").evolutions = new Pokemon[]{perName.get("Poussifeu"),perName.get("Galifeu"),perName.get("Brasegali"),perName.get("Mega-Brasegali")};
# //        perName.get("Sepiatroce").evolutions = new Pokemon[]{perName.get("Sepiatop"),perName.get("Sepiatroce")};
# //        perName.get("Vostourno").evolutions = new Pokemon[]{perName.get("Vostourno"),perName.get("Vaututrice")};
# //        perName.get("Ossatueur").evolutions = new Pokemon[]{perName.get("Osselait"),perName.get("Ossatueur")};
# //        perName.get("Cabriolaine").evolutions = new Pokemon[]{perName.get("Cabriolaine"),perName.get("Chevroum")};
# //        perName.get("Lombre").evolutions = new Pokemon[]{perName.get("Nenupiot"),perName.get("Lombre"),perName.get("Ludicolo")};
# //        perName.get("Apitrini").evolutions = new Pokemon[]{perName.get("Apitrini"),perName.get("Apireine")};
# //        perName.get("Nirondelle").evolutions = new Pokemon[]{perName.get("Nirondelle"),perName.get("Heledelle")};
# //        perName.get("Chinchidou").evolutions = new Pokemon[]{perName.get("Chinchidou"),perName.get("Pashmilla")};
# //        perName.get("Arceus").evolutions = new Pokemon[]{};
# //        perName.get("Mega-Ptera").evolutions = new Pokemon[]{perName.get("Ptera"),perName.get("Mega-Ptera")};
# //        perName.get("Kadabra").evolutions = new Pokemon[]{perName.get("Abra"),perName.get("Kadabra"),perName.get("Alakazam"),perName.get("Mega-Alakazam")};
# //        perName.get("Regirock").evolutions = new Pokemon[]{};
# //        perName.get("Deoxys (Forme Attaque)").evolutions = new Pokemon[]{};
# //        perName.get("Tarpaud").evolutions = new Pokemon[]{perName.get("Ptitard"),perName.get("Tetarte"),perName.get("Tartard"),perName.get("Tarpaud")};
# //        perName.get("Sapereau").evolutions = new Pokemon[]{perName.get("Sapereau"),perName.get("Excavarenne")};
# //        perName.get("Cacturne").evolutions = new Pokemon[]{perName.get("Cacnea"),perName.get("Cacturne")};
# //        perName.get("Raichu").evolutions = new Pokemon[]{perName.get("Pichu"),perName.get("Pikachu"),perName.get("Raichu")};
# //        perName.get("Poissoroy").evolutions = new Pokemon[]{perName.get("Poissirene"),perName.get("Poissoroy")};
# //        perName.get("Vibraninf").evolutions = new Pokemon[]{perName.get("Kraknoix"),perName.get("Vibraninf"),perName.get("Libegon")};
# //        perName.get("Vacilys").evolutions = new Pokemon[]{perName.get("Lilia"),perName.get("Vacilys")};
# //        perName.get("Vivaldaim").evolutions = new Pokemon[]{perName.get("Vivaldaim"),perName.get("Haydaim")};
# //        perName.get("Tadmorv").evolutions = new Pokemon[]{perName.get("Tadmorv"),perName.get("Grotadmorv")};
# //        perName.get("Zarbi").evolutions = new Pokemon[]{};
# //        perName.get("Galifeu").evolutions = new Pokemon[]{perName.get("Poussifeu"),perName.get("Galifeu"),perName.get("Brasegali"),perName.get("Mega-Brasegali")};
# //        perName.get("Dardargnan").evolutions = new Pokemon[]{perName.get("Aspicot"),perName.get("Coconfort"),perName.get("Dardargnan")};
# //        perName.get("Polarhume").evolutions = new Pokemon[]{perName.get("Polarhume"),perName.get("Polagriffe")};
# //        perName.get("Tylton").evolutions = new Pokemon[]{perName.get("Tylton"),perName.get("Altaria")};
# //        perName.get("Roitiflam").evolutions = new Pokemon[]{perName.get("Gruikui"),perName.get("Grotichon"),perName.get("Roitiflam")};
# //        perName.get("Manternel").evolutions = new Pokemon[]{perName.get("Larveyette"),perName.get("Couverdure"),perName.get("Manternel")};
# //        perName.get("Cornebre").evolutions = new Pokemon[]{perName.get("Cornebre"),perName.get("Corboss")};
# //        perName.get("Terhal").evolutions = new Pokemon[]{perName.get("Terhal"),perName.get("Metang"),perName.get("Metalosse")};
# //        perName.get("Shaofouine").evolutions = new Pokemon[]{perName.get("Kungfouine"),perName.get("Shaofouine")};
# //        perName.get("Papilord").evolutions = new Pokemon[]{perName.get("Cheniti"),perName.get("Cheniselle (Cape Plante)"),perName.get("Papilord")};
# //        perName.get("Fantominus").evolutions = new Pokemon[]{perName.get("Fantominus"),perName.get("Spectrum"),perName.get("Ectoplasma"),perName.get("Mega-Ectoplasma")};
# //        perName.get("Lakmecygne").evolutions = new Pokemon[]{perName.get("Couaneton"),perName.get("Lakmecygne")};
# //        perName.get("Kraknoix").evolutions = new Pokemon[]{perName.get("Kraknoix"),perName.get("Vibraninf"),perName.get("Libegon")};
# //        perName.get("Leuphorie").evolutions = new Pokemon[]{perName.get("Ptiravi"),perName.get("Leveinard"),perName.get("Leuphorie")};
# //        perName.get("Boskara").evolutions = new Pokemon[]{perName.get("Tortipouss"),perName.get("Boskara"),perName.get("Torterra")};
# //        perName.get("Charkos").evolutions = new Pokemon[]{perName.get("Kranidos"),perName.get("Charkos")};
# //        perName.get("Gigalithe").evolutions = new Pokemon[]{perName.get("Nodulithe"),perName.get("Geolithe"),perName.get("Gigalithe")};
# //        perName.get("Roucoups").evolutions = new Pokemon[]{perName.get("Roucool"),perName.get("Roucoups"),perName.get("Roucarnage")};
# //        perName.get("Ecayon").evolutions = new Pokemon[]{perName.get("Ecayon"),perName.get("Lumineon")};
# //        perName.get("Statitik").evolutions = new Pokemon[]{perName.get("Statitik"),perName.get("Mygavolt")};
# //        perName.get("Teraclope").evolutions = new Pokemon[]{perName.get("Skelenox"),perName.get("Teraclope"),perName.get("Noctunoir")};
# //        perName.get("Aquali").evolutions = new Pokemon[]{perName.get("Evoli"),perName.get("Aquali"),perName.get("Voltali"),perName.get("Pyroli"),perName.get("Mentali"),perName.get("Noctali"),perName.get("Phyllali"),perName.get("Givrali"),perName.get("Nymphali")};
# //        perName.get("Geolithe").evolutions = new Pokemon[]{perName.get("Nodulithe"),perName.get("Geolithe"),perName.get("Gigalithe")};
# //        perName.get("Draco").evolutions = new Pokemon[]{perName.get("Minidraco"),perName.get("Draco"),perName.get("Dracolosse")};
# //        perName.get("Magnezone").evolutions = new Pokemon[]{perName.get("Magneti"),perName.get("Magneton"),perName.get("Magnezone")};
# //        perName.get("Roselia").evolutions = new Pokemon[]{perName.get("Rozbouton"),perName.get("Roselia"),perName.get("Roserade")};
# //        perName.get("Monaflemit").evolutions = new Pokemon[]{perName.get("Parecool"),perName.get("Vigoroth"),perName.get("Monaflemit")};
# //        perName.get("Spinda").evolutions = new Pokemon[]{};
# //        perName.get("Tartard").evolutions = new Pokemon[]{perName.get("Ptitard"),perName.get("Tetarte"),perName.get("Tartard"),perName.get("Tarpaud")};
# //        perName.get("Palkia").evolutions = new Pokemon[]{};
# //        perName.get("Darumarond").evolutions = new Pokemon[]{perName.get("Darumarond"),perName.get("Darumacho (Mode Normal)")};
# //        perName.get("Munna").evolutions = new Pokemon[]{perName.get("Munna"),perName.get("Mushana")};
# //        perName.get("Tauros").evolutions = new Pokemon[]{};
# //        perName.get("Etouraptor").evolutions = new Pokemon[]{perName.get("Etourmi"),perName.get("Etourvol"),perName.get("Etouraptor")};
# //        perName.get("Frison").evolutions = new Pokemon[]{};
# //        perName.get("Raikou").evolutions = new Pokemon[]{};
# //        perName.get("Pingoleon").evolutions = new Pokemon[]{perName.get("Tiplouf"),perName.get("Prinplouf"),perName.get("Pingoleon")};
# //        perName.get("Hericendre").evolutions = new Pokemon[]{perName.get("Hericendre"),perName.get("Feurisson"),perName.get("Typhlosion")};
# //        perName.get("Arbok").evolutions = new Pokemon[]{perName.get("Abo"),perName.get("Arbok")};
# //        perName.get("Mesmerella").evolutions = new Pokemon[]{perName.get("Scrutella"),perName.get("Mesmerella"),perName.get("Siderella")};
# //        perName.get("Chimpenfeu").evolutions = new Pokemon[]{perName.get("Ouisticram"),perName.get("Chimpenfeu"),perName.get("Simiabraz")};
# //        perName.get("Psykokwak").evolutions = new Pokemon[]{perName.get("Psykokwak"),perName.get("Akwakwak")};
# //        perName.get("Boustiflor").evolutions = new Pokemon[]{perName.get("Chetiflor"),perName.get("Boustiflor"),perName.get("Empiflor")};
# //        perName.get("Porygon2").evolutions = new Pokemon[]{perName.get("Porygon"),perName.get("Porygon2"),perName.get("Porygon-Z")};
# //        perName.get("Kaimorse").evolutions = new Pokemon[]{perName.get("Obalie"),perName.get("Phogleur"),perName.get("Kaimorse")};
# //        perName.get("Akwakwak").evolutions = new Pokemon[]{perName.get("Psykokwak"),perName.get("Akwakwak")};
# //        perName.get("Tygnon").evolutions = new Pokemon[]{perName.get("Debugant"),perName.get("Kicklee"),perName.get("Tygnon"),perName.get("Kapoera")};
# //        perName.get("Goinfrex").evolutions = new Pokemon[]{perName.get("Goinfrex"),perName.get("Ronflex")};
# //        perName.get("Griknot").evolutions = new Pokemon[]{perName.get("Griknot"),perName.get("Carmache"),perName.get("Carchacrok"),perName.get("Mega-Carchacrok")};
# //        perName.get("Sucroquin").evolutions = new Pokemon[]{perName.get("Sucroquin"),perName.get("Cupcanaille")};
# //        perName.get("Escargaume").evolutions = new Pokemon[]{perName.get("Escargaume"),perName.get("Limaspeed")};
# //        perName.get("Monorpale").evolutions = new Pokemon[]{perName.get("Monorpale"),perName.get("Dimocles"),perName.get("Exagide (Forme Assaut)")};
# //        perName.get("Goupelin").evolutions = new Pokemon[]{perName.get("Feunnec"),perName.get("Roussil"),perName.get("Goupelin")};
# //        perName.get("Tenefix").evolutions = new Pokemon[]{};
# //        perName.get("Mustebouee").evolutions = new Pokemon[]{perName.get("Mustebouee"),perName.get("Musteflott")};
# //        perName.get("Nosferalto").evolutions = new Pokemon[]{perName.get("Nosferapti"),perName.get("Nosferalto"),perName.get("Nostenfer")};
# //        perName.get("Judokrak").evolutions = new Pokemon[]{};
# //        perName.get("Relicanth").evolutions = new Pokemon[]{};
# //        perName.get("Mushana").evolutions = new Pokemon[]{perName.get("Munna"),perName.get("Mushana")};
# //        perName.get("Ptiravi").evolutions = new Pokemon[]{perName.get("Ptiravi"),perName.get("Leveinard"),perName.get("Leuphorie")};
# //        perName.get("Coquiperl").evolutions = new Pokemon[]{perName.get("Coquiperl"),perName.get("Serpang"),perName.get("Rosabyss")};
# //        perName.get("Ohmassacre").evolutions = new Pokemon[]{perName.get("Anchwatt"),perName.get("Lamperoie"),perName.get("Ohmassacre")};
# //        perName.get("Brocelome").evolutions = new Pokemon[]{perName.get("Brocelome"),perName.get("Desseliande")};
# //        perName.get("Rozbouton").evolutions = new Pokemon[]{perName.get("Rozbouton"),perName.get("Roselia"),perName.get("Roserade")};
# //        perName.get("Scalproie").evolutions = new Pokemon[]{perName.get("Scalpion"),perName.get("Scalproie")};
# //        perName.get("Phogleur").evolutions = new Pokemon[]{perName.get("Obalie"),perName.get("Phogleur"),perName.get("Kaimorse")};
# //        perName.get("Neitram").evolutions = new Pokemon[]{perName.get("Lewsor"),perName.get("Neitram")};
# //        perName.get("Chovsourir").evolutions = new Pokemon[]{perName.get("Chovsourir"),perName.get("Rhinolove")};
# //        perName.get("Musteflott").evolutions = new Pokemon[]{perName.get("Mustebouee"),perName.get("Musteflott")};
# //        perName.get("Insolourdo").evolutions = new Pokemon[]{};
# //        perName.get("Mega-Tyranocif").evolutions = new Pokemon[]{perName.get("Embrylex"),perName.get("Ymphect"),perName.get("Tyranocif"),perName.get("Mega-Tyranocif")};
# //        perName.get("Munja").evolutions = new Pokemon[]{perName.get("Ningale"),perName.get("Ninjask"),perName.get("Munja")};
# //        perName.get("Drakkarmin").evolutions = new Pokemon[]{};
# //        perName.get("Sorbouboul").evolutions = new Pokemon[]{perName.get("Sorbebe"),perName.get("Sorboul"),perName.get("Sorbouboul")};
# //        perName.get("Mega-Blizzaroi").evolutions = new Pokemon[]{perName.get("Blizzi"),perName.get("Blizzaroi"),perName.get("Mega-Blizzaroi")};
# //        perName.get("Zekrom").evolutions = new Pokemon[]{};
# //        perName.get("Remoraid").evolutions = new Pokemon[]{perName.get("Remoraid"),perName.get("Octillery")};
# //        perName.get("Mamanbo").evolutions = new Pokemon[]{};
# //        perName.get("Meios").evolutions = new Pokemon[]{perName.get("Nucleos"),perName.get("Meios"),perName.get("Symbios")};
# //        perName.get("Noctali").evolutions = new Pokemon[]{perName.get("Evoli"),perName.get("Aquali"),perName.get("Voltali"),perName.get("Pyroli"),perName.get("Mentali"),perName.get("Noctali"),perName.get("Phyllali"),perName.get("Givrali"),perName.get("Nymphali")};
# //        perName.get("Mega-Pharamp").evolutions = new Pokemon[]{perName.get("Wattouat"),perName.get("Lainergie"),perName.get("Pharamp"),perName.get("Mega-Pharamp")};
# //        perName.get("Ramoloss").evolutions = new Pokemon[]{perName.get("Ramoloss"),perName.get("Flagadoss"),perName.get("Roigada")};
# //        perName.get("Cupcanaille").evolutions = new Pokemon[]{perName.get("Sucroquin"),perName.get("Cupcanaille")};
# //        perName.get("Carabaffe").evolutions = new Pokemon[]{perName.get("Carapuce"),perName.get("Carabaffe"),perName.get("Tortank"),perName.get("Mega-Tortank")};
# //        perName.get("Barbicha").evolutions = new Pokemon[]{perName.get("Barloche"),perName.get("Barbicha")};
# //        perName.get("Colombeau").evolutions = new Pokemon[]{perName.get("Poichigeon"),perName.get("Colombeau"),perName.get("Deflaisan")};
# //        perName.get("Baggaid").evolutions = new Pokemon[]{perName.get("Baggiguane"),perName.get("Baggaid")};
# //        perName.get("Ramboum").evolutions = new Pokemon[]{perName.get("Chuchmur"),perName.get("Ramboum"),perName.get("Brouhabam")};
# //        perName.get("Kicklee").evolutions = new Pokemon[]{perName.get("Debugant"),perName.get("Kicklee"),perName.get("Tygnon"),perName.get("Kapoera")};
# //        perName.get("Teddiursa").evolutions = new Pokemon[]{perName.get("Teddiursa"),perName.get("Ursaring")};
# //        perName.get("Karaclee").evolutions = new Pokemon[]{};
# //        perName.get("Serpang").evolutions = new Pokemon[]{perName.get("Coquiperl"),perName.get("Serpang"),perName.get("Rosabyss")};
# //        perName.get("Porygon").evolutions = new Pokemon[]{perName.get("Porygon"),perName.get("Porygon2"),perName.get("Porygon-Z")};
# //        perName.get("Mastouffe").evolutions = new Pokemon[]{perName.get("Ponchiot"),perName.get("Ponchien"),perName.get("Mastouffe")};
# //        perName.get("Pyrax").evolutions = new Pokemon[]{perName.get("Pyronille"),perName.get("Pyrax")};
# //        perName.get("Majaspic").evolutions = new Pokemon[]{perName.get("Vipelierre"),perName.get("Lianaja"),perName.get("Majaspic")};
# //        perName.get("Blindalys").evolutions = new Pokemon[]{perName.get("Chenipotte"),perName.get("Armulys"),perName.get("Blindalys"),perName.get("Charmillon"),perName.get("Papinox")};
# //        perName.get("Nenupiot").evolutions = new Pokemon[]{perName.get("Nenupiot"),perName.get("Lombre"),perName.get("Ludicolo")};
# //        perName.get("Foretress").evolutions = new Pokemon[]{perName.get("Pomdepik"),perName.get("Foretress")};
# //        perName.get("Mimitoss").evolutions = new Pokemon[]{perName.get("Mimitoss"),perName.get("Aeromite")};
# //        perName.get("Lippoutou").evolutions = new Pokemon[]{perName.get("Lippouti"),perName.get("Lippoutou")};
# //        perName.get("Negapi").evolutions = new Pokemon[]{};
# //        perName.get("Mega-Leviator").evolutions = new Pokemon[]{perName.get("Magicarpe"),perName.get("Leviator"),perName.get("Mega-Leviator")};
# //        perName.get("Mega-Dracaufeu Y").evolutions = new Pokemon[]{perName.get("Salameche"),perName.get("Reptincel"),perName.get("Dracaufeu"),perName.get("Mega-Dracaufeu X"),perName.get("Mega-Dracaufeu Y")};
# //        perName.get("Colimucus").evolutions = new Pokemon[]{perName.get("Mucuscule"),perName.get("Colimucus"),perName.get("Muplodocus")};
# //        perName.get("Ouisticram").evolutions = new Pokemon[]{perName.get("Ouisticram"),perName.get("Chimpenfeu"),perName.get("Simiabraz")};
# //        perName.get("Gruikui").evolutions = new Pokemon[]{perName.get("Gruikui"),perName.get("Grotichon"),perName.get("Roitiflam")};
# //        perName.get("Gallame").evolutions = new Pokemon[]{perName.get("Tarsal"),perName.get("Kirlia"),perName.get("Gardevoir"),perName.get("Gallame"),perName.get("Mega-Gardevoir")};
# //        perName.get("Flotajou").evolutions = new Pokemon[]{perName.get("Flotajou"),perName.get("Flotoutan")};
# //        perName.get("Pandespiegle").evolutions = new Pokemon[]{perName.get("Pandespiegle"),perName.get("Pandarbare")};
# //        perName.get("Muplodocus").evolutions = new Pokemon[]{perName.get("Mucuscule"),perName.get("Colimucus"),perName.get("Muplodocus")};
# //        perName.get("Blindepique").evolutions = new Pokemon[]{perName.get("Marisson"),perName.get("Boguerisse"),perName.get("Blindepique")};
# //        perName.get("Melancolux").evolutions = new Pokemon[]{perName.get("Funecire"),perName.get("Melancolux"),perName.get("Lugulabre")};
# //        perName.get("Viridium").evolutions = new Pokemon[]{};
# //        perName.get("Fouinette").evolutions = new Pokemon[]{perName.get("Fouinette"),perName.get("Fouinar")};
# //        perName.get("Desseliande").evolutions = new Pokemon[]{perName.get("Brocelome"),perName.get("Desseliande")};
# //        perName.get("Seviper").evolutions = new Pokemon[]{};
# //        perName.get("Germignon").evolutions = new Pokemon[]{perName.get("Germignon"),perName.get("Macronium"),perName.get("Meganium")};
# //        perName.get("Ponchiot").evolutions = new Pokemon[]{perName.get("Ponchiot"),perName.get("Ponchien"),perName.get("Mastouffe")};
# //        perName.get("Typhlosion").evolutions = new Pokemon[]{perName.get("Hericendre"),perName.get("Feurisson"),perName.get("Typhlosion")};
# //        perName.get("Demeteros (Forme Avatar)").evolutions = new Pokemon[]{};
# //        perName.get("Feunard").evolutions = new Pokemon[]{perName.get("Goupix"),perName.get("Feunard")};
# //        perName.get("Magneti").evolutions = new Pokemon[]{perName.get("Magneti"),perName.get("Magneton"),perName.get("Magnezone")};
# //        perName.get("Cobaltium").evolutions = new Pokemon[]{};
# //        perName.get("Persian").evolutions = new Pokemon[]{perName.get("Miaouss"),perName.get("Persian")};
# //        perName.get("Nidoking").evolutions = new Pokemon[]{perName.get("Nidoran M"),perName.get("Nidorino"),perName.get("Nidoking")};
# //        perName.get("Ninjask").evolutions = new Pokemon[]{perName.get("Ningale"),perName.get("Ninjask"),perName.get("Munja")};
# //        perName.get("Amphinobi").evolutions = new Pokemon[]{perName.get("Grenousse"),perName.get("Croaporal"),perName.get("Amphinobi")};
# //        perName.get("Nemelios").evolutions = new Pokemon[]{perName.get("Helionceau"),perName.get("Nemelios")};
# //        perName.get("Medhyena").evolutions = new Pokemon[]{perName.get("Medhyena"),perName.get("Grahyena")};
# //        perName.get("Evoli").evolutions = new Pokemon[]{perName.get("Evoli"),perName.get("Aquali"),perName.get("Voltali"),perName.get("Pyroli"),perName.get("Mentali"),perName.get("Noctali"),perName.get("Phyllali"),perName.get("Givrali"),perName.get("Nymphali")};
# //        perName.get("Barloche").evolutions = new Pokemon[]{perName.get("Barloche"),perName.get("Barbicha")};
# //        perName.get("Kabuto").evolutions = new Pokemon[]{perName.get("Kabuto"),perName.get("Kabutops")};
# //        perName.get("Grenousse").evolutions = new Pokemon[]{perName.get("Grenousse"),perName.get("Croaporal"),perName.get("Amphinobi")};
# //        perName.get("Kaorine").evolutions = new Pokemon[]{perName.get("Balbuto"),perName.get("Kaorine")};
# //        perName.get("Debugant").evolutions = new Pokemon[]{perName.get("Debugant"),perName.get("Kicklee"),perName.get("Tygnon"),perName.get("Kapoera")};
# //        perName.get("Ningale").evolutions = new Pokemon[]{perName.get("Ningale"),perName.get("Ninjask"),perName.get("Munja")};
# //        perName.get("Capidextre").evolutions = new Pokemon[]{perName.get("Capumain"),perName.get("Capidextre")};
# //        perName.get("Tic").evolutions = new Pokemon[]{perName.get("Tic"),perName.get("Clic"),perName.get("Cliticlic")};
# //        perName.get("Piafabec").evolutions = new Pokemon[]{perName.get("Piafabec"),perName.get("Rapasdepic")};
# //        perName.get("Camerupt").evolutions = new Pokemon[]{perName.get("Chamallot"),perName.get("Camerupt")};
# //        perName.get("Goelise").evolutions = new Pokemon[]{perName.get("Goelise"),perName.get("Bekipan")};
# //        perName.get("Funecire").evolutions = new Pokemon[]{perName.get("Funecire"),perName.get("Melancolux"),perName.get("Lugulabre")};
# //        perName.get("Golgopathe").evolutions = new Pokemon[]{perName.get("Opermine"),perName.get("Golgopathe")};
# //        perName.get("Reshiram").evolutions = new Pokemon[]{};
# //        perName.get("Excelangue").evolutions = new Pokemon[]{perName.get("Excelangue"),perName.get("Coudlangue")};
# //        perName.get("Tetarte").evolutions = new Pokemon[]{perName.get("Ptitard"),perName.get("Tetarte"),perName.get("Tartard"),perName.get("Tarpaud")};
# //        perName.get("Mega-Ectoplasma").evolutions = new Pokemon[]{perName.get("Fantominus"),perName.get("Spectrum"),perName.get("Ectoplasma"),perName.get("Mega-Ectoplasma")};
# //        perName.get("Flingouste").evolutions = new Pokemon[]{perName.get("Flingouste"),perName.get("Gamblast")};
# //        perName.get("Aligatueur").evolutions = new Pokemon[]{perName.get("Kaiminus"),perName.get("Crocrodil"),perName.get("Aligatueur")};
# //        perName.get("Magireve").evolutions = new Pokemon[]{perName.get("Feuforeve"),perName.get("Magireve")};
# //        perName.get("Luxray").evolutions = new Pokemon[]{perName.get("Lixy"),perName.get("Luxio"),perName.get("Luxray")};
# //        perName.get("Rosabyss").evolutions = new Pokemon[]{perName.get("Coquiperl"),perName.get("Serpang"),perName.get("Rosabyss")};
# //        perName.get("Galekid").evolutions = new Pokemon[]{perName.get("Galekid"),perName.get("Galegon"),perName.get("Galeking"),perName.get("Mega-Galeking")};
# //        perName.get("Ptera").evolutions = new Pokemon[]{perName.get("Ptera"),perName.get("Mega-Ptera")};
# //        perName.get("Galopa").evolutions = new Pokemon[]{perName.get("Ponyta"),perName.get("Galopa")};
# //        perName.get("Roigada").evolutions = new Pokemon[]{perName.get("Ramoloss"),perName.get("Flagadoss"),perName.get("Roigada")};
# //        perName.get("Jirachi").evolutions = new Pokemon[]{};
# //        perName.get("Pitrouille (Taille Mini)").evolutions = new Pokemon[]{};
# //        perName.get("Marisson").evolutions = new Pokemon[]{perName.get("Marisson"),perName.get("Boguerisse"),perName.get("Blindepique")};
# //        perName.get("Mascaiman").evolutions = new Pokemon[]{perName.get("Mascaiman"),perName.get("Escroco"),perName.get("Crocorible")};
# //        perName.get("Carapuce").evolutions = new Pokemon[]{perName.get("Carapuce"),perName.get("Carabaffe"),perName.get("Tortank"),perName.get("Mega-Tortank")};
# //        perName.get("Mangriff").evolutions = new Pokemon[]{};
# //        perName.get("Latias").evolutions = new Pokemon[]{};
# //        perName.get("Grahyena").evolutions = new Pokemon[]{perName.get("Medhyena"),perName.get("Grahyena")};
# //        perName.get("Lugia").evolutions = new Pokemon[]{};
# //        perName.get("Onix").evolutions = new Pokemon[]{perName.get("Onix"),perName.get("Steelix")};
# //        perName.get("Pyroli").evolutions = new Pokemon[]{perName.get("Evoli"),perName.get("Aquali"),perName.get("Voltali"),perName.get("Pyroli"),perName.get("Mentali"),perName.get("Noctali"),perName.get("Phyllali"),perName.get("Givrali"),perName.get("Nymphali")};
# //        perName.get("Magneton").evolutions = new Pokemon[]{perName.get("Magneti"),perName.get("Magneton"),perName.get("Magnezone")};
# //        perName.get("Incisache").evolutions = new Pokemon[]{perName.get("Coupenotte"),perName.get("Incisache"),perName.get("Tranchodon")};
# //        perName.get("Kokiyas").evolutions = new Pokemon[]{perName.get("Kokiyas"),perName.get("Crustabri")};
# //        perName.get("Racaillou").evolutions = new Pokemon[]{perName.get("Racaillou"),perName.get("Gravalanch"),perName.get("Grolem")};
# //        perName.get("Colhomard").evolutions = new Pokemon[]{perName.get("Ecrapince"),perName.get("Colhomard")};
# //        perName.get("Papinox").evolutions = new Pokemon[]{perName.get("Chenipotte"),perName.get("Armulys"),perName.get("Blindalys"),perName.get("Charmillon"),perName.get("Papinox")};
# //        perName.get("Manaphy").evolutions = new Pokemon[]{};
# //        perName.get("Crocrodil").evolutions = new Pokemon[]{perName.get("Kaiminus"),perName.get("Crocrodil"),perName.get("Aligatueur")};
# //        perName.get("Ectoplasma").evolutions = new Pokemon[]{perName.get("Fantominus"),perName.get("Spectrum"),perName.get("Ectoplasma"),perName.get("Mega-Ectoplasma")};
# //        perName.get("Nucleos").evolutions = new Pokemon[]{perName.get("Nucleos"),perName.get("Meios"),perName.get("Symbios")};
# //        perName.get("Vortente").evolutions = new Pokemon[]{};
# //        perName.get("Ecrapince").evolutions = new Pokemon[]{perName.get("Ecrapince"),perName.get("Colhomard")};
# //        perName.get("Coxyclaque").evolutions = new Pokemon[]{perName.get("Coxy"),perName.get("Coxyclaque")};
# //        perName.get("Lugulabre").evolutions = new Pokemon[]{perName.get("Funecire"),perName.get("Melancolux"),perName.get("Lugulabre")};
# //        perName.get("Moyade").evolutions = new Pokemon[]{perName.get("Viskuse"),perName.get("Moyade")};
# //        perName.get("Delcatty").evolutions = new Pokemon[]{perName.get("Skitty"),perName.get("Delcatty")};
# //        perName.get("Floette").evolutions = new Pokemon[]{perName.get("Flabebe"),perName.get("Floette"),perName.get("Florges")};
# //        perName.get("Tutankafer").evolutions = new Pokemon[]{perName.get("Tutafeh"),perName.get("Tutankafer")};
# //        perName.get("Meditikka").evolutions = new Pokemon[]{perName.get("Meditikka"),perName.get("Charmina"),perName.get("Mega-Charmina")};
# //        perName.get("Nanmeouie").evolutions = new Pokemon[]{};
# //        perName.get("Feunnec").evolutions = new Pokemon[]{perName.get("Feunnec"),perName.get("Roussil"),perName.get("Goupelin")};
# //        perName.get("Archeodong").evolutions = new Pokemon[]{perName.get("Archeomire"),perName.get("Archeodong")};
# //        perName.get("Axoloto").evolutions = new Pokemon[]{perName.get("Axoloto"),perName.get("Maraiste")};
# //        perName.get("Macronium").evolutions = new Pokemon[]{perName.get("Germignon"),perName.get("Macronium"),perName.get("Meganium")};
# //        perName.get("Rafflesia").evolutions = new Pokemon[]{perName.get("Mystherbe"),perName.get("Ortide"),perName.get("Rafflesia"),perName.get("Joliflor")};
# //        perName.get("Caratroc").evolutions = new Pokemon[]{};
# //        perName.get("Shaymin (Forme Celeste)").evolutions = new Pokemon[]{};
# //        perName.get("Ponchien").evolutions = new Pokemon[]{perName.get("Ponchiot"),perName.get("Ponchien"),perName.get("Mastouffe")};
# //        perName.get("Pifeuil").evolutions = new Pokemon[]{perName.get("Grainipiot"),perName.get("Pifeuil"),perName.get("Tengalice")};
# //        perName.get("Toudoudou").evolutions = new Pokemon[]{perName.get("Toudoudou"),perName.get("Rondoudou"),perName.get("Grodoudou")};
# //        perName.get("Sablaireau").evolutions = new Pokemon[]{perName.get("Sabelette"),perName.get("Sablaireau")};
# //        perName.get("Banshitrouye (Taille Mini)").evolutions = new Pokemon[]{};
# //        perName.get("Draby").evolutions = new Pokemon[]{perName.get("Draby"),perName.get("Drackhaus"),perName.get("Drattak")};
# //        perName.get("Rayquaza").evolutions = new Pokemon[]{};
# //        perName.get("Granivol").evolutions = new Pokemon[]{perName.get("Granivol"),perName.get("Floravol"),perName.get("Cotovol")};
# //        perName.get("Luxio").evolutions = new Pokemon[]{perName.get("Lixy"),perName.get("Luxio"),perName.get("Luxray")};
# //        perName.get("Ceriflor").evolutions = new Pokemon[]{perName.get("Ceribou"),perName.get("Ceriflor")};
# //        perName.get("Dimoret").evolutions = new Pokemon[]{perName.get("Farfuret"),perName.get("Dimoret")};
# //        perName.get("Amonita").evolutions = new Pokemon[]{perName.get("Amonita"),perName.get("Amonistar")};
# //        perName.get("Larveyette").evolutions = new Pokemon[]{perName.get("Larveyette"),perName.get("Couverdure"),perName.get("Manternel")};
# //        perName.get("Krabboss").evolutions = new Pokemon[]{perName.get("Krabby"),perName.get("Krabboss")};
# //        perName.get("Batracne").evolutions = new Pokemon[]{perName.get("Tritonde"),perName.get("Batracne"),perName.get("Crapustule")};
# //        perName.get("Tentacool").evolutions = new Pokemon[]{perName.get("Tentacool"),perName.get("Tentacruel")};
# //        perName.get("Hippodocus").evolutions = new Pokemon[]{perName.get("Hippopotas"),perName.get("Hippodocus")};
# //        perName.get("Wailmer").evolutions = new Pokemon[]{perName.get("Wailmer"),perName.get("Wailord")};
# //        perName.get("Magmar").evolutions = new Pokemon[]{perName.get("Magby"),perName.get("Magmar"),perName.get("Maganon")};
# //        perName.get("Caninos").evolutions = new Pokemon[]{perName.get("Caninos"),perName.get("Arcanin")};
# //        perName.get("Seleroc").evolutions = new Pokemon[]{};
# //        perName.get("Lucario").evolutions = new Pokemon[]{perName.get("Riolu"),perName.get("Lucario"),perName.get("Mega-Lucario")};
# //        perName.get("Machopeur").evolutions = new Pokemon[]{perName.get("Machoc"),perName.get("Machopeur"),perName.get("Mackogneur")};
# //        perName.get("Barpau").evolutions = new Pokemon[]{perName.get("Barpau"),perName.get("Milobellus")};
# //        perName.get("Armulys").evolutions = new Pokemon[]{perName.get("Chenipotte"),perName.get("Armulys"),perName.get("Blindalys"),perName.get("Charmillon"),perName.get("Papinox")};
# //        perName.get("Drascore").evolutions = new Pokemon[]{perName.get("Rapion"),perName.get("Drascore")};
# //        perName.get("Coudlangue").evolutions = new Pokemon[]{perName.get("Excelangue"),perName.get("Coudlangue")};
# //        perName.get("Tarinorme").evolutions = new Pokemon[]{perName.get("Tarinor"),perName.get("Tarinorme")};
# //        perName.get("Lovdisc").evolutions = new Pokemon[]{};
# //        perName.get("Saquedeneu").evolutions = new Pokemon[]{perName.get("Saquedeneu"),perName.get("Bouldeneu")};
# //        perName.get("Tengalice").evolutions = new Pokemon[]{perName.get("Grainipiot"),perName.get("Pifeuil"),perName.get("Tengalice")};
# //        perName.get("Golemastoc").evolutions = new Pokemon[]{perName.get("Gringolem"),perName.get("Golemastoc")};
# //        perName.get("Diamat").evolutions = new Pokemon[]{perName.get("Solochi"),perName.get("Diamat"),perName.get("Trioxhydre")};
# //        perName.get("Phyllali").evolutions = new Pokemon[]{perName.get("Evoli"),perName.get("Aquali"),perName.get("Voltali"),perName.get("Pyroli"),perName.get("Mentali"),perName.get("Noctali"),perName.get("Phyllali"),perName.get("Givrali"),perName.get("Nymphali")};
# //        perName.get("Mistigrix").evolutions = new Pokemon[]{perName.get("Psystigri"),perName.get("Mistigrix")};
# //        perName.get("Grotichon").evolutions = new Pokemon[]{perName.get("Gruikui"),perName.get("Grotichon"),perName.get("Roitiflam")};
# //        perName.get("Tropius").evolutions = new Pokemon[]{};
# //        perName.get("Salameche").evolutions = new Pokemon[]{perName.get("Salameche"),perName.get("Reptincel"),perName.get("Dracaufeu"),perName.get("Mega-Dracaufeu X"),perName.get("Mega-Dracaufeu Y")};
# //        perName.get("Victini").evolutions = new Pokemon[]{};
# //        perName.get("Ymphect").evolutions = new Pokemon[]{perName.get("Embrylex"),perName.get("Ymphect"),perName.get("Tyranocif"),perName.get("Mega-Tyranocif")};
# //        perName.get("Artikodin").evolutions = new Pokemon[]{};
# //        perName.get("Phione").evolutions = new Pokemon[]{};
# //        perName.get("Miaouss").evolutions = new Pokemon[]{perName.get("Miaouss"),perName.get("Persian")};
# //        perName.get("Braisillon").evolutions = new Pokemon[]{perName.get("Passerouge"),perName.get("Braisillon"),perName.get("Flambusard")};
# //        perName.get("Migalos").evolutions = new Pokemon[]{perName.get("Mimigal"),perName.get("Migalos")};
# //        perName.get("Manzai").evolutions = new Pokemon[]{perName.get("Manzai"),perName.get("Simularbre")};
# //        perName.get("Nosferapti").evolutions = new Pokemon[]{perName.get("Nosferapti"),perName.get("Nosferalto"),perName.get("Nostenfer")};
# //        perName.get("Arakdo").evolutions = new Pokemon[]{perName.get("Arakdo"),perName.get("Maskadra")};
# //        perName.get("Kaiminus").evolutions = new Pokemon[]{perName.get("Kaiminus"),perName.get("Crocrodil"),perName.get("Aligatueur")};
# //        perName.get("Charmillon").evolutions = new Pokemon[]{perName.get("Chenipotte"),perName.get("Armulys"),perName.get("Blindalys"),perName.get("Charmillon"),perName.get("Papinox")};
# //        perName.get("Zebibron").evolutions = new Pokemon[]{perName.get("Zebibron"),perName.get("Zeblitz")};
# //        perName.get("Coupenotte").evolutions = new Pokemon[]{perName.get("Coupenotte"),perName.get("Incisache"),perName.get("Tranchodon")};
# //        perName.get("Muciole").evolutions = new Pokemon[]{};
# //        perName.get("Cizayox").evolutions = new Pokemon[]{perName.get("Insecateur"),perName.get("Cizayox"),perName.get("Mega-Cizayox")};
# //        perName.get("Triopikeur").evolutions = new Pokemon[]{perName.get("Taupiqueur"),perName.get("Triopikeur")};
# //        perName.get("Floravol").evolutions = new Pokemon[]{perName.get("Granivol"),perName.get("Floravol"),perName.get("Cotovol")};
# //        perName.get("Ouvrifier").evolutions = new Pokemon[]{perName.get("Charpenti"),perName.get("Ouvrifier"),perName.get("Betochef")};
# //        perName.get("Darkrai").evolutions = new Pokemon[]{};
# //        perName.get("Mew").evolutions = new Pokemon[]{};
# //        perName.get("Grindur").evolutions = new Pokemon[]{perName.get("Grindur"),perName.get("Noacier")};
# //        perName.get("Balignon").evolutions = new Pokemon[]{perName.get("Balignon"),perName.get("Chapignon")};
# //        perName.get("Kravarech").evolutions = new Pokemon[]{perName.get("Venalgue"),perName.get("Kravarech")};
# //        perName.get("Chaglam").evolutions = new Pokemon[]{perName.get("Chaglam"),perName.get("Chaffreux")};
# //        perName.get("Xerneas").evolutions = new Pokemon[]{};
# //        perName.get("Cadoizo").evolutions = new Pokemon[]{};
# //        perName.get("Mega-Kangourex").evolutions = new Pokemon[]{perName.get("Kangourex"),perName.get("Mega-Kangourex")};
# //        perName.get("Chapignon").evolutions = new Pokemon[]{perName.get("Balignon"),perName.get("Chapignon")};
# //        perName.get("Lanturn").evolutions = new Pokemon[]{perName.get("Loupio"),perName.get("Lanturn")};
# //        perName.get("Simiabraz").evolutions = new Pokemon[]{perName.get("Ouisticram"),perName.get("Chimpenfeu"),perName.get("Simiabraz")};
# //        perName.get("Bruyverne").evolutions = new Pokemon[]{perName.get("Sonistrelle"),perName.get("Bruyverne")};
# //        perName.get("Mucuscule").evolutions = new Pokemon[]{perName.get("Mucuscule"),perName.get("Colimucus"),perName.get("Muplodocus")};
# //        perName.get("Chaffreux").evolutions = new Pokemon[]{perName.get("Chaglam"),perName.get("Chaffreux")};
# //        perName.get("Aeropteryx").evolutions = new Pokemon[]{perName.get("Arkeapti"),perName.get("Aeropteryx")};
# //        perName.get("Farfuret").evolutions = new Pokemon[]{perName.get("Farfuret"),perName.get("Dimoret")};
# //        perName.get("Cotovol").evolutions = new Pokemon[]{perName.get("Granivol"),perName.get("Floravol"),perName.get("Cotovol")};
# //        perName.get("Rondoudou").evolutions = new Pokemon[]{perName.get("Toudoudou"),perName.get("Rondoudou"),perName.get("Grodoudou")};
# //        perName.get("Sorboul").evolutions = new Pokemon[]{perName.get("Sorbebe"),perName.get("Sorboul"),perName.get("Sorbouboul")};
# //        perName.get("Amonistar").evolutions = new Pokemon[]{perName.get("Amonita"),perName.get("Amonistar")};
# //        perName.get("Clic").evolutions = new Pokemon[]{perName.get("Tic"),perName.get("Clic"),perName.get("Cliticlic")};
# //        perName.get("Meganium").evolutions = new Pokemon[]{perName.get("Germignon"),perName.get("Macronium"),perName.get("Meganium")};
# //        perName.get("Deoxys (Forme Defense)").evolutions = new Pokemon[]{};
# //        perName.get("Viskuse").evolutions = new Pokemon[]{perName.get("Viskuse"),perName.get("Moyade")};
# //        perName.get("Metamorph").evolutions = new Pokemon[]{};
# //        perName.get("Kangourex").evolutions = new Pokemon[]{perName.get("Kangourex"),perName.get("Mega-Kangourex")};
# //        perName.get("Pitrouille (Taille Normale)").evolutions = new Pokemon[]{};
# //        perName.get("Wailord").evolutions = new Pokemon[]{perName.get("Wailmer"),perName.get("Wailord")};
# //        perName.get("Colossinge").evolutions = new Pokemon[]{perName.get("Ferosinge"),perName.get("Colossinge")};
# //        perName.get("Yveltal").evolutions = new Pokemon[]{};
# //        perName.get("Fulguris (Forme Totemique)").evolutions = new Pokemon[]{};
# //        perName.get("Corayon").evolutions = new Pokemon[]{};
# //        perName.get("Mackogneur").evolutions = new Pokemon[]{perName.get("Machoc"),perName.get("Machopeur"),perName.get("Mackogneur")};
# //        perName.get("Rapion").evolutions = new Pokemon[]{perName.get("Rapion"),perName.get("Drascore")};
# //        perName.get("Feuiloutan").evolutions = new Pokemon[]{perName.get("Feuillajou"),perName.get("Feuiloutan")};
# //        perName.get("Ursaring").evolutions = new Pokemon[]{perName.get("Teddiursa"),perName.get("Ursaring")};
# //        perName.get("Anorith").evolutions = new Pokemon[]{perName.get("Anorith"),perName.get("Armaldo")};
# //        perName.get("Vipelierre").evolutions = new Pokemon[]{perName.get("Vipelierre"),perName.get("Lianaja"),perName.get("Majaspic")};
# //        perName.get("Gardevoir").evolutions = new Pokemon[]{perName.get("Tarsal"),perName.get("Kirlia"),perName.get("Gardevoir"),perName.get("Gallame"),perName.get("Mega-Gardevoir")};
# //        perName.get("Scarhino").evolutions = new Pokemon[]{perName.get("Scarhino"),perName.get("Mega-Scarhino")};
# //        perName.get("Demolosse").evolutions = new Pokemon[]{perName.get("Malosse"),perName.get("Demolosse"),perName.get("Mega-Demolosse")};
# //        perName.get("Crapustule").evolutions = new Pokemon[]{perName.get("Tritonde"),perName.get("Batracne"),perName.get("Crapustule")};
# //        perName.get("Crabaraque").evolutions = new Pokemon[]{perName.get("Crabicoque"),perName.get("Crabaraque")};
# //        perName.get("Tranchodon").evolutions = new Pokemon[]{perName.get("Coupenotte"),perName.get("Incisache"),perName.get("Tranchodon")};
# //        perName.get("Mewtwo").evolutions = new Pokemon[]{perName.get("Mewtwo"),perName.get("Mega-Mewtwo X"),perName.get("Mega-Mewtwo Y")};
# //        perName.get("Feurisson").evolutions = new Pokemon[]{perName.get("Hericendre"),perName.get("Feurisson"),perName.get("Typhlosion")};
# //        perName.get("Galeking").evolutions = new Pokemon[]{perName.get("Galekid"),perName.get("Galegon"),perName.get("Galeking"),perName.get("Mega-Galeking")};
# //        perName.get("Miradar").evolutions = new Pokemon[]{perName.get("Ratentif"),perName.get("Miradar")};
# //        perName.get("Tyranocif").evolutions = new Pokemon[]{perName.get("Embrylex"),perName.get("Ymphect"),perName.get("Tyranocif"),perName.get("Mega-Tyranocif")};
# //        perName.get("Scorvol").evolutions = new Pokemon[]{perName.get("Scorplane"),perName.get("Scorvol")};
# //        perName.get("Demanta").evolutions = new Pokemon[]{perName.get("Babimanta"),perName.get("Demanta")};
# //        perName.get("Solaroc").evolutions = new Pokemon[]{};
# //        perName.get("Passerouge").evolutions = new Pokemon[]{perName.get("Passerouge"),perName.get("Braisillon"),perName.get("Flambusard")};
# //        perName.get("Mega-Scarhino").evolutions = new Pokemon[]{perName.get("Scarhino"),perName.get("Mega-Scarhino")};
# //        perName.get("Flobio").evolutions = new Pokemon[]{perName.get("Gobou"),perName.get("Flobio"),perName.get("Laggron")};
# //        perName.get("Cochignon").evolutions = new Pokemon[]{perName.get("Marcacrin"),perName.get("Cochignon"),perName.get("Mammochon")};
# //        perName.get("Roserade").evolutions = new Pokemon[]{perName.get("Rozbouton"),perName.get("Roselia"),perName.get("Roserade")};
# //        perName.get("Chamallot").evolutions = new Pokemon[]{perName.get("Chamallot"),perName.get("Camerupt")};
# //        perName.get("Chacripan").evolutions = new Pokemon[]{perName.get("Chacripan"),perName.get("Leopardus")};
# //        perName.get("Psystigri").evolutions = new Pokemon[]{perName.get("Psystigri"),perName.get("Mistigrix")};
# //        perName.get("Scrutella").evolutions = new Pokemon[]{perName.get("Scrutella"),perName.get("Mesmerella"),perName.get("Siderella")};
# //        perName.get("Kungfouine").evolutions = new Pokemon[]{perName.get("Kungfouine"),perName.get("Shaofouine")};
# //        perName.get("Momartik").evolutions = new Pokemon[]{perName.get("Stalgamin"),perName.get("Oniglali"),perName.get("Momartik")};
# //        perName.get("Leopardus").evolutions = new Pokemon[]{perName.get("Chacripan"),perName.get("Leopardus")};
# //        perName.get("Ho-Oh").evolutions = new Pokemon[]{};
# //        perName.get("Krabby").evolutions = new Pokemon[]{perName.get("Krabby"),perName.get("Krabboss")};
# //        perName.get("Suicune").evolutions = new Pokemon[]{};
# //        perName.get("Zeblitz").evolutions = new Pokemon[]{perName.get("Zebibron"),perName.get("Zeblitz")};
# //        perName.get("Excavarenne").evolutions = new Pokemon[]{perName.get("Sapereau"),perName.get("Excavarenne")};
# //        perName.get("Donphan").evolutions = new Pokemon[]{perName.get("Phanpy"),perName.get("Donphan")};
# //        perName.get("Grelacon").evolutions = new Pokemon[]{perName.get("Grelacon"),perName.get("Seracrawl")};
# //        perName.get("Pitrouille (Taille Ultra)").evolutions = new Pokemon[]{};
# //        perName.get("Blizzi").evolutions = new Pokemon[]{perName.get("Blizzi"),perName.get("Blizzaroi"),perName.get("Mega-Blizzaroi")};
# //        perName.get("Mega-Absol").evolutions = new Pokemon[]{perName.get("Absol"),perName.get("Mega-Absol")};
# //        perName.get("Strassie").evolutions = new Pokemon[]{};
# //        perName.get("Trousselin").evolutions = new Pokemon[]{};
# //        perName.get("Morpheo").evolutions = new Pokemon[]{};
# //        perName.get("Airmure").evolutions = new Pokemon[]{};
# //        perName.get("M. Mime").evolutions = new Pokemon[]{perName.get("Mime Jr."),perName.get("M. Mime")};
# //        perName.get("Natu").evolutions = new Pokemon[]{perName.get("Natu"),perName.get("Xatu")};
# //        perName.get("Lainergie").evolutions = new Pokemon[]{perName.get("Wattouat"),perName.get("Lainergie"),perName.get("Pharamp"),perName.get("Mega-Pharamp")};
# //        perName.get("Mega-Carchacrok").evolutions = new Pokemon[]{perName.get("Griknot"),perName.get("Carmache"),perName.get("Carchacrok"),perName.get("Mega-Carchacrok")};
# //        perName.get("Coxy").evolutions = new Pokemon[]{perName.get("Coxy"),perName.get("Coxyclaque")};
# //        perName.get("Shaymin (Forme Terrestre)").evolutions = new Pokemon[]{};
# //        perName.get("Banshitrouye (Taille Maxi)").evolutions = new Pokemon[]{};
# //        perName.get("Cacnea").evolutions = new Pokemon[]{perName.get("Cacnea"),perName.get("Cacturne")};
# //        perName.get("Smogo").evolutions = new Pokemon[]{perName.get("Smogo"),perName.get("Smogogo")};
# //        perName.get("Arcanin").evolutions = new Pokemon[]{perName.get("Caninos"),perName.get("Arcanin")};
# //        perName.get("Milobellus").evolutions = new Pokemon[]{perName.get("Barpau"),perName.get("Milobellus")};
# //        perName.get("Taupiqueur").evolutions = new Pokemon[]{perName.get("Taupiqueur"),perName.get("Triopikeur")};
# //        perName.get("Capumain").evolutions = new Pokemon[]{perName.get("Capumain"),perName.get("Capidextre")};
# //        perName.get("Fulguris (Forme Avatar)").evolutions = new Pokemon[]{};
# //        perName.get("Machoc").evolutions = new Pokemon[]{perName.get("Machoc"),perName.get("Machopeur"),perName.get("Mackogneur")};
# //        perName.get("Ludicolo").evolutions = new Pokemon[]{perName.get("Nenupiot"),perName.get("Lombre"),perName.get("Ludicolo")};
# //        perName.get("Noarfang").evolutions = new Pokemon[]{perName.get("Hoot-hoot"),perName.get("Noarfang")};
# //        perName.get("Meloetta (Forme Danse)").evolutions = new Pokemon[]{};
# //        perName.get("Sepiatop").evolutions = new Pokemon[]{perName.get("Sepiatop"),perName.get("Sepiatroce")};
# //        perName.get("Fermite").evolutions = new Pokemon[]{};
# //        perName.get("Regice").evolutions = new Pokemon[]{};
# //        perName.get("Armaldo").evolutions = new Pokemon[]{perName.get("Anorith"),perName.get("Armaldo")};
# //        perName.get("Lewsor").evolutions = new Pokemon[]{perName.get("Lewsor"),perName.get("Neitram")};
# //        perName.get("Sancoki").evolutions = new Pokemon[]{perName.get("Sancoki"),perName.get("Tritosor")};
# //        perName.get("Demeteros (Forme Totemique)").evolutions = new Pokemon[]{};
# //        perName.get("Trompignon").evolutions = new Pokemon[]{perName.get("Trompignon"),perName.get("Gaulet")};
# //        perName.get("Empiflor").evolutions = new Pokemon[]{perName.get("Chetiflor"),perName.get("Boustiflor"),perName.get("Empiflor")};
# //        perName.get("Drackhaus").evolutions = new Pokemon[]{perName.get("Draby"),perName.get("Drackhaus"),perName.get("Drattak")};
# //        perName.get("Chenipan").evolutions = new Pokemon[]{perName.get("Chenipan"),perName.get("Chrysacier"),perName.get("Papilusion")};
# //        perName.get("Limonde").evolutions = new Pokemon[]{};
# //        perName.get("Grodrive").evolutions = new Pokemon[]{perName.get("Baudrive"),perName.get("Grodrive")};
# //        perName.get("Flabebe").evolutions = new Pokemon[]{perName.get("Flabebe"),perName.get("Floette"),perName.get("Florges")};
# //        perName.get("Mega-Alakazam").evolutions = new Pokemon[]{perName.get("Abra"),perName.get("Kadabra"),perName.get("Alakazam"),perName.get("Mega-Alakazam")};
# //        perName.get("Brutapode").evolutions = new Pokemon[]{perName.get("Venipatte"),perName.get("Scobolide"),perName.get("Brutapode")};
# //        perName.get("Deoxys (Forme de Base)").evolutions = new Pokemon[]{};
# //        perName.get("Megapagos").evolutions = new Pokemon[]{perName.get("Carapagos"),perName.get("Megapagos")};
# //        perName.get("Deflaisan").evolutions = new Pokemon[]{perName.get("Poichigeon"),perName.get("Colombeau"),perName.get("Deflaisan")};
# //        perName.get("Spectrum").evolutions = new Pokemon[]{perName.get("Fantominus"),perName.get("Spectrum"),perName.get("Ectoplasma"),perName.get("Mega-Ectoplasma")};
# //        perName.get("Pandarbare").evolutions = new Pokemon[]{perName.get("Pandespiegle"),perName.get("Pandarbare")};
# //        perName.get("Rexillius").evolutions = new Pokemon[]{perName.get("Ptyranidur"),perName.get("Rexillius")};
# //        perName.get("Sulfura").evolutions = new Pokemon[]{};
# //        perName.get("Drattak").evolutions = new Pokemon[]{perName.get("Draby"),perName.get("Drackhaus"),perName.get("Drattak")};
# //        perName.get("Seracrawl").evolutions = new Pokemon[]{perName.get("Grelacon"),perName.get("Seracrawl")};

evoList = [(u'Ptitard', u'Tetarte', u'Tartard', u'Tarpaud'), (u'Absol', u'Mega-Absol'), (u'Sapereau', u'Excavarenne'), (u'Kokiyas', u'Crustabri'), (u'Dynavolt', u'Elecsprint', u'Mega-Elecsprint'), (u'Polarhume', u'Polagriffe'), (u'Scorplane', u'Scorvol'), (u'Scarhino', u'Mega-Scarhino'), (u'Loupio', u'Lanturn'), (u'Sancoki', u'Tritosor'), (u'Rhinocorne', u'Rhinoferos', u'Rhinastoc'), (u'Solochi', u'Diamat', u'Trioxhydre'), (u'Ouisticram', u'Chimpenfeu', u'Simiabraz'), (u'Mimitoss', u'Aeromite'), (u'Meditikka', u'Charmina', u'Mega-Charmina'), (u'Aspicot', u'Coconfort', u'Dardargnan'), (u'Anorith', u'Armaldo'), (u'Charpenti', u'Ouvrifier', u'Betochef'), (u'Tutafeh', u'Tutankafer'), (u'Nirondelle', u'Heledelle'), (u'Fouinette', u'Fouinar'), (u'Krabby', u'Krabboss'), (u'Keunotor', u'Castorno'), (u'Ramoloss', u'Flagadoss', u'Roigada'), (u'Mysdibule', u'Mega-Mysdibule'), (u'Griknot', u'Carmache', u'Carchacrok', u'Mega-Carchacrok'), (u'Anchwatt', u'Lamperoie', u'Ohmassacre'), (u'Piafabec', u'Rapasdepic'), (u'Baudrive', u'Grodrive'), (u'Melo', u'Melofee', u'Melodelfe'), (u'Feuillajou', u'Feuiloutan'), (u'Tylton', u'Altaria'), (u'Rapion', u'Drascore'), (u'Amonita', u'Amonistar'), (u'Ceribou', u'Ceriflor'), (u'Tadmorv', u'Grotadmorv'), (u'Carapuce', u'Carabaffe', u'Tortank', u'Mega-Tortank'), (u'Arcko', u'Massko', u'Jungko'), (u'Poussifeu', u'Galifeu', u'Brasegali', u'Mega-Brasegali'), (u'Terhal', u'Metang', u'Metalosse'), (u'Malosse', u'Demolosse', u'Mega-Demolosse'), (u'Flabebe', u'Floette', u'Florges'), (u'Manzai', u'Simularbre'), (u'Chlorobule', u'Fragilady'), (u'Taupiqueur', u'Triopikeur'), (u'Chetiflor', u'Boustiflor', u'Empiflor'), (u'Poichigeon', u'Colombeau', u'Deflaisan'), (u'Snubbull', u'Granbull'), (u'Evoli', u'Aquali', u'Voltali', u'Pyroli', u'Mentali', u'Noctali', u'Phyllali', u'Givrali', u'Nymphali'), (u'Stalgamin', u'Oniglali', u'Momartik'), (u'Grindur', u'Noacier'), (u'Mime Jr.', u'M. Mime'), (u'Gruikui', u'Grotichon', u'Roitiflam'), (u'Machoc', u'Machopeur', u'Mackogneur'), (u'Flamajou', u'Flamoutan'), (u'Cradopaud', u'Coatox'), (u'Polichombr', u'Branette', u'Mega-Branette'), (u'Tritonde', u'Batracne', u'Crapustule'), (u'Debugant', u'Kicklee', u'Tygnon', u'Kapoera'), (u'Tortipouss', u'Boskara', u'Torterra'), (u'Kaiminus', u'Crocrodil', u'Aligatueur'), (u'Draby', u'Drackhaus', u'Drattak'), (u'Soporifik', u'Hypnomade'), (u'Korillon', u'Eoko'), (u'Medhyena', u'Grahyena'), (u'Kangourex', u'Mega-Kangourex'), (u'Ptiravi', u'Leveinard', u'Leuphorie'), (u'Lepidonille', u'Peregrain', u'Prismillon'), (u'Hypotrempe', u'Hypocean', u'Hyporoi'), (u'Barloche', u'Barbicha'), (u'Grainipiot', u'Pifeuil', u'Tengalice'), (u'Toudoudou', u'Rondoudou', u'Grodoudou'), (u'Galvaran', u'Iguolta'), (u'Cacnea', u'Cacturne'), (u'Barpau', u'Milobellus'), (u'Feunnec', u'Roussil', u'Goupelin'), (u'Chovsourir', u'Rhinolove'), (u'Axoloto', u'Maraiste'), (u'Cheniti', u'Cheniselle', u'Papilord'), (u'Chenipotte', u'Armulys', u'Blindalys', u'Charmillon', u'Papinox'), (u'Opermine', u'Golgopathe'), (u'Sonistrelle', u'Bruyverne'), (u'Arakdo', u'Maskadra'), (u'Balignon', u'Chapignon'), (u'Gobou', u'Flobio', u'Laggron'), (u'Nucleos', u'Meios', u'Symbios200e'), (u'Brocelome', u'Desseliande'), (u'Abo', u'Arbok'), (u'Crikzik', u'Melokrik'), (u'Kranidos', u'Charkos'), (u'Feuforeve', u'Magireve'), (u'Nosferapti', u'Nosferalto', u'Nostenfer'), (u'Germignon', u'Macronium', u'Meganium'), (u'Escargaume', u'Limaspeed'), (u'Gringolem', u'Golemastoc'), (u'Hericendre', u'Feurisson', u'Typhlosion'), (u'Crabicoque', u'Crabaraque'), (u'Scalpion', u'Scalproie'), (u'Kabuto', u'Kabutops'), (u'Voltorbe', u'Electrode'), (u'Racaillou', u'Gravalanch', u'Grolem'), (u'Blizzi', u'Blizzaroi', u'Mega-Blizzaroi'), (u'Natu', u'Xatu'), (u'Grelacon', u'Seracrawl'), (u'Rattata', u'Rattatac'), (u'Grenousse', u'Croaporal', u'Amphinobi'), (u'Makuhita', u'Hariyama'), (u'Ponchiot', u'Ponchien', u'Mastouffe'), (u'Capumain', u'Capidextre'), (u'Otaria', u'Lamantine'), (u'Pandespiegle', u'Pandarbare'), (u'Teddiursa', u'Ursaring'), (u'Marisson', u'Boguerisse', u'Blindepique'), (u'Azurill', u'Marill', u'Azumarill'), (u'Bulbizarre', u'Herbizarre', u'Florizarre', u'Mega-Florizarre'), (u'Togepi', u'Togetic', u'Togekiss'), (u'Parecool', u'Vigoroth', u'Monaflemit'), (u'Cornebre', u'Corboss'), (u'Chaglam', u'Chaffreux'), (u'Viskuse', u'Moyade'), (u'Pomdepik', u'Foretress'), (u'Magby', u'Magmar', u'Maganon'), (u'Kraknoix', u'Vibraninf', u'Libegon'), (u'Scrutella', u'Mesmerella', u'Siderella'), (u'Remoraid', u'Octillery'), (u'Poissirene', u'Poissoroy'), (u'Munna', u'Mushana'), (u'Roucool', u'Roucoups', u'Roucarnage'), (u'Arkeapti', u'Aeropteryx'), (u'Larveyette', u'Couverdure', u'Manternel'), (u'Miaouss', u'Persian'), (u'Coquiperl', u'Serpang', u'Rosabyss'), (u'Ningale', u'Ninjask', u'Munja'), (u'Archeomire', u'Archeodong'), (u'Chacripan', u'Leopardus'), (u'Sorbebe', u'Sorboul', u'Sorbouboul'), (u'Pichu', u'Pikachu', u'Raichu'), (u'Doduo', u'Dodrio'), (u'Pitrouille', u'Banshitrouye'), (u'Mustebouee', u'Musteflott'), (u'Lewsor', u'Neitram'), (u'Chenipan', u'Chrysacier', u'Papilusion'), (u'Moustillon', u'Mateloutre', u'Clamiral'), (u'Psykokwak', u'Akwakwak'), (u'Funecire', u'Melancolux', u'Lugulabre'), (u'Statitik', u'Mygavolt'), (u'Hippopotas', u'Hippodocus'), (u'Wailmer', u'Wailord'), (u'Scarabrute', u'Mega-Scarabrute'), (u'Etourmi', u'Etourvol', u'Etouraptor'), (u'Skitty', u'Delcatty'), (u'Marcacrin', u'Cochignon', u'Mammochon'), (u'Trompignon', u'Gaulet'), (u'Rototaupe', u'Minotaupe'), (u'Limagma', u'Volcaropod'), (u'Ponyta', u'Galopa'), (u'Spoink', u'Groret'), (u'Okeoke', u'Qulbutoke'), (u'Furaiglon', u'Gueriaigle'), (u'Sabelette', u'Sablaireau'), (u'Vostourno', u'Vaututrice'), (u'Balbuto', u'Kaorine'), (u'Noeunoeuf', u'Noadkoko'), (u'Darumarond', u'Darumacho'), (u'Smogo', u'Smogogo'), (u'Caninos', u'Arcanin'), (u'Ferosinge', u'Colossinge'), (u'Ecayon', u'Lumineon'), (u'Onix', u'Steelix'), (u'Skelenox', u'Teraclope', u'Noctunoir'), (u'Amagara', u'Dragmara'), (u'Saquedeneu', u'Bouldeneu'), (u'Tic', u'Clic', u'Cliticlic'), (u'Venalgue', u'Kravarech'), (u'Chuchmur', u'Ramboum', u'Brouhabam'), (u'Fantominus', u'Spectrum', u'Ectoplasma', u'Mega-Ectoplasma'), (u'Salameche', u'Reptincel', u'Dracaufeu', u'Mega-Dracaufeu X', u'Mega-Dracaufeu Y'), (u'Mystherbe', u'Ortide', u'Rafflesia', u'Joliflor'), (u'Gloupti', u'Avaltout'), (u'Elekid', u'Elektek', u'Elekable'), (u'Vipelierre', u'Lianaja', u'Majaspic'), (u'Insecateur', u'Cizayox', u'Mega-Cizayox'), (u'Obalie', u'Phogleur', u'Kaimorse'), (u'Ecrapince', u'Colhomard'), (u'Minidraco', u'Draco', u'Dracolosse'), (u'Magicarpe', u'Leviator', u'Mega-Leviator'), (u'Carabing', u'Lancargot'), (u'Miamiasme', u'Miasmax'), (u'Venipatte', u'Scobolide', u'Brutapode'), (u'Tarinor', u'Tarinorme'), (u'Farfuret', u'Dimoret'), (u'Pyronille', u'Pyrax'), (u'Goinfrex', u'Ronflex'), (u'Nidoran M', u'Nidorino', u'Nidoking'), (u'Sepiatop', u'Sepiatroce'), (u'Baggiguane', u'Baggaid'), (u'Mimigal', u'Migalos'), (u'Mascaiman', u'Escroco', u'Crocorible'), (), (u'Apitrini', u'Apireine'), (u'Ptera', u'Mega-Ptera'), (u'Couaneton', u'Lakmecygne'), (u'Nucleos', u'Meios'), (u'Coupenotte', u'Incisache', u'Tranchodon'), (u'Fluvetin', u'Cocotine'), (u'Kungfouine', u'Shaofouine'), (u'Doudouvet', u'Farfaduvet'), (u'Flingouste', u'Gamblast'), (u'Sucroquin', u'Cupcanaille'), (u'Dinoclier', u'Bastiodon'), (u'Riolu', u'Lucario', u'Mega-Lucario'), (u'Porygon', u'Porygon2', u'Porygon-Z'), (u'Tournegrin', u'Heliatronc'), (u'Passerouge', u'Braisillon', u'Flambusard'), (u'Laporeille', u'Lockpin'), (u'Moufouette', u'Moufflair'), (u'Zorua', u'Zoroark'), (u'Excelangue', u'Coudlangue'), (u'Monorpale', u'Dimocles', u'Exagide'), (u'Nenupiot', u'Lombre', u'Ludicolo'), (u'Chinchidou', u'Pashmilla'), (u'Lilia', u'Vacilys'), (u'Lixy', u'Luxio', u'Luxray'), (u'Carapagos', u'Megapagos'), (u'Tiplouf', u'Prinplouf', u'Pingoleon'), (u'Nodulithe', u'Geolithe', u'Gigalithe'), (u'Zigzaton', u'Lineon'), (u'Carvanha', u'Sharpedo'), (u'Tentacool', u'Tentacruel'), (u'Mewtwo', u'Mega-Mewtwo X', u'Mega-Mewtwo Y'), (u'Babimanta', u'Demanta'), (u'Osselait', u'Ossatueur'), (u'Ptyranidur', u'Rexillius'), (u'Phanpy', u'Donphan'), (u'Tarsal', u'Kirlia', u'Gardevoir', u'Gallame', u'Mega-Gardevoir'), (u'Embrylex', u'Ymphect', u'Tyranocif', u'Mega-Tyranocif'), (u'Mucuscule', u'Colimucus', u'Muplodocus'), (u'Ratentif', u'Miradar'), (u'Wattouat', u'Lainergie', u'Pharamp', u'Mega-Pharamp'), (u'Yanma', u'Yanmega'), (u'Paras', u'Parasect'), (u'Goupix', u'Feunard'), (u'Abra', u'Kadabra', u'Alakazam', u'Mega-Alakazam'), (u'Chamallot', u'Camerupt'), (u'Hoot-hoot', u'Noarfang'), (u'Goelise', u'Bekipan'), (u'Galekid', u'Galegon', u'Galeking', u'Mega-Galeking'), (u'Lippouti', u'Lippoutou'), (u'Rozbouton', u'Roselia', u'Roserade'), (u'Magneti', u'Magneton', u'Magnezone'), (u'Granivol', u'Floravol', u'Cotovol'), (u'Coxy', u'Coxyclaque'), (u'Zebibron', u'Zeblitz'), (u'Helionceau', u'Nemelios'), (u'Vivaldaim', u'Haydaim'), (u'Flotajou', u'Flotoutan'), (u'Psystigri', u'Mistigrix'), (u'Cabriolaine', u'Chevroum'), (u'Nidoran F', u'Nidorina', u'Nidoqueen')]
pkList = ['Rattatac', 'Porygon-Z', 'Baggiguane', 'Noadkoko', 'Gueriaigle', 'Polichombr', 'Gaulet', 'Hyporoi', 'Elekable', 'Roussil', 'Pashmilla', 'Emolga', 'Grolem', 'Cresselia', 'Flotoutan', 'Bekipan', 'Mateloutre', 'Dinoclier', 'Absol', 'Azurill', 'Apireine', 'Dracaufeu', 'Solochi', 'Motisma (Forme Tonte)', 'Volcaropod', 'Boreas (Forme Totemique)', 'Meloetta (Forme Voix)', 'Snubbull', 'Sharpedo', 'Motisma (Forme Froid)', 'Mega-Mewtwo Y', 'Tutafeh', 'Noctunoir', 'Melodelfe', 'Mega-Mewtwo X', 'Celebi', 'Cocotine', 'Zorua', 'Mega-Elecsprint', 'Carabing', 'Okeoke', 'Hypotrempe', 'Nymphali', 'Venalgue', 'Mega-Scarabrute', 'Maraiste', 'Mega-Florizarre', 'Papilusion', 'Charpenti', 'Doduo', 'Coatox', 'Charmina', 'Voltali', 'Pitrouille (Taille Maxi)', 'Cheniselle (Cape Dechet)', 'Exagide (Forme Assaut)', 'Joliflor', 'Tarsal', 'Scalpion', 'Galegon', 'Smogogo', 'Baudrive', 'Libegon', 'Pomdepik', 'Korillon', 'Boguerisse', 'Mime Jr.', 'Queulorior', 'Ecremeuh', 'Lineon', 'Osselait', 'Castorno', 'Hypnomade', 'Lilia', 'Motisma (Forme Helice)', 'Kranidos', 'Mammochon', 'Moufouette', 'Miasmax', 'Aflamanoir', 'Makuhita', 'Cerfrousse', 'Alakazam', 'Mega-Dracaufeu X', 'Reptincel', 'Carapagos', 'Hypocean', 'Tortipouss', 'Stalgamin', 'Lancargot', 'Chuchmur', 'Motisma (Forme Normale)', 'Maganon', 'Parecool', 'Wattouat', 'Opermine', 'Prinplouf', 'Anchwatt', 'Posipi', 'Exagide (Forme Parade)', 'Elekid', 'Flambusard', 'Balbuto', 'Yanma', 'Poichigeon', 'Lamperoie', 'Kirlia', 'Couaneton', 'Mystherbe', 'Metang', 'Tritosor', 'Dracolosse', 'Fragilady', 'Genesect', 'Nidorino', 'Branette', 'Nidorina', 'Rhinoferos', 'Regigigas', 'Tentacruel', 'Chlorobule', 'Darumacho (Mode Daruma)', 'Ferosinge', 'Flagadoss', 'Crikzik', 'Florges', 'Scarabrute', 'Mimigal', 'Dodrio', 'Pijako', 'Lepidonille', 'Bargantua', 'Chrysacier', 'Electrode', 'Sorbebe', 'Givrali', 'Gloupti', 'Gringolem', 'Miamiasme', 'Togepi', 'Corboss', 'Flamajou', 'Etourvol', 'Abo', 'Obalie', 'Octillery', 'Feuillajou', 'Zygarde', 'Pikachu', 'Zoroark', 'Mega-Mysdibule', 'Nodulithe', 'Rhinastoc', 'Mega-Gardevoir', 'Mega-Brasegali', 'Grainipiot', 'Qwilfish', 'Carchacrok', 'Latios', 'Groret', 'Cheniselle (Cape Plante)', 'Oniglali', 'Steelix', 'Crefollet', 'Electhor', 'Phanpy', 'Crehelf', 'Ortide', 'Metalosse', 'Azumarill', 'Kyogre', 'Mega-Branette', 'Scorplane', 'Chenipotte', 'Elektek', 'Vigoroth', 'Leveinard', 'Fouinar', 'Simularbre', 'Polagriffe', 'Maracachi', 'Dragmara', 'Insecateur', 'Laporeille', 'Hoot-hoot', 'Lokhlass', 'Spiritomb', 'Limagma', 'Paras', 'Pyronille', 'Symbios', 'Melo', 'Lianaja', 'Arcko', 'Archeomire', 'Banshitrouye (Taille Normale)', 'Feuforeve', 'Mega-Tortank', 'Venipatte', 'Doudouvet', 'Lamantine', 'Parasect', 'Avaltout', 'Voltorbe', 'Magicarpe', 'Darumacho (Mode Normal)', 'Heledelle', 'Noacier', 'Laggron', 'Gobou', 'Canarticho', 'Groudon', 'Blizzaroi', 'Tournegrin', 'Nidoqueen', 'Altaria', 'Roucool', 'Cradopaud', 'Malosse', 'Vaututrice', 'Togekiss', 'Tritonde', 'Moufflair', 'Tiplouf', 'Lumivole', 'Carmache', 'Cliticlic', 'Giratina (Forme Originelle)', 'Poussifeu', 'Limaspeed', 'Iguolta', 'Cheniti', 'Kapoera', 'Pachirisu', 'Marill', 'Mega-Lucario', 'Skitty', 'Abra', 'Couverdure', 'Grodoudou', 'Ptyranidur', 'Kecleon', 'Deoxys (Forme Vitesse)', 'Crustabri', 'Motisma (Forme Chaleur)', 'Galvaran', 'Fluvetin', 'Haydaim', 'Kyurem (Noir)', 'Hippopotas', 'Giratina (Forme Alternative)', 'Coconfort', 'Noeunoeuf', 'Zigzaton', 'Rattata', 'Girafarig', 'Otaria', 'Granbull', 'Kabutops', 'Ratentif', 'Cheniselle (Cape Sol)', 'Bulbizarre', 'Couafarel', 'Mega-Demolosse', 'Siderella', 'Dedenne', 'Herbizarre', 'Lixy', 'Roucarnage', 'Tarinor', 'Rapasdepic', 'Embrylex', 'Togetic', 'Mega-Galeking', 'Brouhabam', 'Babimanta', 'Rhinolove', 'Florizarre', 'Clamiral', 'Ronflex', 'Kyurem (Blanc)', 'Grotadmorv', 'Ptitard', 'Mentali', 'Betochef', 'Stari', 'Arkeapti', 'Crocorible', 'Heatran', 'Ponyta', 'Crefadet', 'Escroco', 'Hariyama', 'Qulbutoke', 'Staross', 'Hexagel', 'Lippouti', 'Bastiodon', 'Peregrain', 'Carvanha', 'Pharamp', 'Mega-Charmina', 'Bouldeneu', 'Heliatronc', 'Gamblast', 'Eoko', 'Brutalibre', 'Furaiglon', 'Chevroum', 'Flamoutan', 'Prismillon', 'Sonistrelle', 'Goupix', 'Gravalanch', 'Nostenfer', 'Chetiflor', 'Motisma (Forme Lavage)', 'Lumineon', 'Croaporal', 'Rhinocorne', 'Leviator', 'Cryptero', 'Spoink', 'Dialga', 'Sabelette', 'Dynavolt', 'Pichu', 'Terrakium', 'Amagara', 'Poissirene', 'Magby', 'Farfaduvet', 'Lockpin', 'Loupio', 'Elecsprint', 'Banshitrouye (Taille Ultra)', 'Keldeo', 'Jungko', 'Boreas (Forme Avatar)', 'Registeel', 'Xatu', 'Skelenox', 'Etourmi', 'Aeromite', 'Tortank', 'Mega-Cizayox', 'Minidraco', 'Trioxhydre', 'Melofee', 'Crabicoque', 'Torterra', 'Rototaupe', 'Ceribou', 'Keunotor', 'Nidoran F', 'Helionceau', 'Entei', 'Nidoran M', 'Moustillon', 'Mygavolt', 'Soporifik', 'Dimocles', 'Riolu', 'Aspicot', 'Marcacrin', 'Mysdibule', 'Chartor', 'Minotaupe', 'Maskadra', 'Yanmega', 'Melokrik', 'Scobolide', 'Massko', 'Brasegali', 'Sepiatroce', 'Vostourno', 'Ossatueur', 'Cabriolaine', 'Lombre', 'Apitrini', 'Nirondelle', 'Chinchidou', 'Arceus', 'Mega-Ptera', 'Kadabra', 'Regirock', 'Deoxys (Forme Attaque)', 'Tarpaud', 'Sapereau', 'Cacturne', 'Raichu', 'Poissoroy', 'Vibraninf', 'Vacilys', 'Vivaldaim', 'Tadmorv', 'Zarbi', 'Galifeu', 'Dardargnan', 'Polarhume', 'Tylton', 'Roitiflam', 'Manternel', 'Cornebre', 'Terhal', 'Shaofouine', 'Papilord', 'Fantominus', 'Lakmecygne', 'Kraknoix', 'Leuphorie', 'Boskara', 'Charkos', 'Gigalithe', 'Roucoups', 'Ecayon', 'Statitik', 'Teraclope', 'Aquali', 'Geolithe', 'Draco', 'Magnezone', 'Roselia', 'Monaflemit', 'Spinda', 'Tartard', 'Palkia', 'Darumarond', 'Munna', 'Tauros', 'Etouraptor', 'Frison', 'Raikou', 'Pingoleon', 'Hericendre', 'Arbok', 'Mesmerella', 'Chimpenfeu', 'Psykokwak', 'Boustiflor', 'Porygon2', 'Kaimorse', 'Akwakwak', 'Tygnon', 'Goinfrex', 'Griknot', 'Sucroquin', 'Escargaume', 'Monorpale', 'Goupelin', 'Tenefix', 'Mustebouee', 'Nosferalto', 'Judokrak', 'Relicanth', 'Mushana', 'Ptiravi', 'Coquiperl', 'Ohmassacre', 'Brocelome', 'Rozbouton', 'Scalproie', 'Phogleur', 'Neitram', 'Chovsourir', 'Musteflott', 'Insolourdo', 'Mega-Tyranocif', 'Munja', 'Drakkarmin', 'Sorbouboul', 'Mega-Blizzaroi', 'Zekrom', 'Remoraid', 'Mamanbo', 'Meios', 'Noctali', 'Mega-Pharamp', 'Ramoloss', 'Cupcanaille', 'Carabaffe', 'Barbicha', 'Colombeau', 'Baggaid', 'Ramboum', 'Kicklee', 'Teddiursa', 'Karaclee', 'Serpang', 'Porygon', 'Mastouffe', 'Pyrax', 'Majaspic', 'Blindalys', 'Nenupiot', 'Foretress', 'Mimitoss', 'Lippoutou', 'Negapi', 'Mega-Leviator', 'Mega-Dracaufeu Y', 'Colimucus', 'Ouisticram', 'Gruikui', 'Gallame', 'Flotajou', 'Pandespiegle', 'Muplodocus', 'Blindepique', 'Melancolux', 'Viridium', 'Fouinette', 'Desseliande', 'Seviper', 'Germignon', 'Ponchiot', 'Typhlosion', 'Demeteros (Forme Avatar)', 'Feunard', 'Magneti', 'Cobaltium', 'Persian', 'Nidoking', 'Ninjask', 'Amphinobi', 'Nemelios', 'Medhyena', 'Evoli', 'Barloche', 'Kabuto', 'Grenousse', 'Kaorine', 'Debugant', 'Ningale', 'Capidextre', 'Tic', 'Piafabec', 'Camerupt', 'Goelise', 'Funecire', 'Golgopathe', 'Reshiram', 'Excelangue', 'Tetarte', 'Mega-Ectoplasma', 'Flingouste', 'Aligatueur', 'Magireve', 'Luxray', 'Rosabyss', 'Galekid', 'Ptera', 'Galopa', 'Roigada', 'Jirachi', 'Pitrouille (Taille Mini)', 'Marisson', 'Mascaiman', 'Carapuce', 'Mangriff', 'Latias', 'Grahyena', 'Lugia', 'Onix', 'Pyroli', 'Magneton', 'Incisache', 'Kokiyas', 'Racaillou', 'Colhomard', 'Papinox', 'Manaphy', 'Crocrodil', 'Ectoplasma', 'Nucleos', 'Vortente', 'Ecrapince', 'Coxyclaque', 'Lugulabre', 'Moyade', 'Delcatty', 'Floette', 'Tutankafer', 'Meditikka', 'Nanmeouie', 'Feunnec', 'Archeodong', 'Axoloto', 'Macronium', 'Rafflesia', 'Caratroc', 'Shaymin (Forme Celeste)', 'Ponchien', 'Pifeuil', 'Toudoudou', 'Sablaireau', 'Banshitrouye (Taille Mini)', 'Draby', 'Rayquaza', 'Granivol', 'Luxio', 'Ceriflor', 'Dimoret', 'Amonita', 'Larveyette', 'Krabboss', 'Batracne', 'Tentacool', 'Hippodocus', 'Wailmer', 'Magmar', 'Caninos', 'Seleroc', 'Lucario', 'Machopeur', 'Barpau', 'Armulys', 'Drascore', 'Coudlangue', 'Tarinorme', 'Lovdisc', 'Saquedeneu', 'Tengalice', 'Golemastoc', 'Diamat', 'Phyllali', 'Mistigrix', 'Grotichon', 'Tropius', 'Salameche', 'Victini', 'Ymphect', 'Artikodin', 'Phione', 'Miaouss', 'Braisillon', 'Migalos', 'Manzai', 'Nosferapti', 'Arakdo', 'Kaiminus', 'Charmillon', 'Zebibron', 'Coupenotte', 'Muciole', 'Cizayox', 'Triopikeur', 'Floravol', 'Ouvrifier', 'Darkrai', 'Mew', 'Grindur', 'Balignon', 'Kravarech', 'Chaglam', 'Xerneas', 'Cadoizo', 'Mega-Kangourex', 'Chapignon', 'Lanturn', 'Simiabraz', 'Bruyverne', 'Mucuscule', 'Chaffreux', 'Aeropteryx', 'Farfuret', 'Cotovol', 'Rondoudou', 'Sorboul', 'Amonistar', 'Clic', 'Meganium', 'Deoxys (Forme Defense)', 'Viskuse', 'Metamorph', 'Kangourex', 'Pitrouille (Taille Normale)', 'Wailord', 'Colossinge', 'Yveltal', 'Fulguris (Forme Totemique)', 'Corayon', 'Mackogneur', 'Rapion', 'Feuiloutan', 'Ursaring', 'Anorith', 'Vipelierre', 'Gardevoir', 'Scarhino', 'Demolosse', 'Crapustule', 'Crabaraque', 'Tranchodon', 'Mewtwo', 'Feurisson', 'Galeking', 'Miradar', 'Tyranocif', 'Scorvol', 'Demanta', 'Solaroc', 'Passerouge', 'Mega-Scarhino', 'Flobio', 'Cochignon', 'Roserade', 'Chamallot', 'Chacripan', 'Psystigri', 'Scrutella', 'Kungfouine', 'Momartik', 'Leopardus', 'Ho-Oh', 'Krabby', 'Suicune', 'Zeblitz', 'Excavarenne', 'Donphan', 'Grelacon', 'Pitrouille (Taille Ultra)', 'Blizzi', 'Mega-Absol', 'Strassie', 'Trousselin', 'Morpheo', 'Airmure', 'M. Mime', 'Natu', 'Lainergie', 'Mega-Carchacrok', 'Coxy', 'Shaymin (Forme Terrestre)', 'Banshitrouye (Taille Maxi)', 'Cacnea', 'Smogo', 'Arcanin', 'Milobellus', 'Taupiqueur', 'Capumain', 'Fulguris (Forme Avatar)', 'Machoc', 'Ludicolo', 'Noarfang', 'Meloetta (Forme Danse)', 'Sepiatop', 'Fermite', 'Regice', 'Armaldo', 'Lewsor', 'Sancoki', 'Demeteros (Forme Totemique)', 'Trompignon', 'Empiflor', 'Drackhaus', 'Chenipan', 'Limonde', 'Grodrive', 'Flabebe', 'Mega-Alakazam', 'Brutapode', 'Deoxys (Forme de Base)', 'Megapagos', 'Deflaisan', 'Spectrum', 'Pandarbare', 'Rexillius', 'Sulfura', 'Drattak', 'Seracrawl']
main(pkList, evoList)

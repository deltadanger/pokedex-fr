import os, urllib
from HTMLParser import HTMLParser

list = {}

def main(types, megatypes, caracs, datatalents):
    types = types.split("\n")
    types = [types[i] + "/" + types[i+1] for i in range(0, len(types), 2)]
    
    for type in types:
        type = type.split("\t")
        name = type[2].strip()
        number = int(type[0][1:])
        type1, type2 = type[4].split("/")
        type2 = type2 or "NONE"
        
        list[name] = {"name": name, "number": number, "type1": type1, "type2": type2}
    
    
    for type in megatypes.split("\n"):
        type = type.split("\t")
        name = type[1].strip()
        number = int(type[0])
        type1, type2 = type[2].split("/")
        type2 = type2 or "NONE"
        
        talents = [type[3].strip().replace("-", "_").replace(" ", "_").replace(".", "").upper()]
        
        list[name] = {"name": name, "number": number, "type1": type1, "type2": type2, "talents": talents}
    
    
    for name, talents in datatalents.items():
        talents = [talent.strip().replace("-", "_").replace(" ", "_").replace(".", "").upper() for talent in talents]
        list[name].update({"talents":talents})
        
        
    toRemove = {}
    index = 0
    for carac in caracs.split("\n"):
        carac = carac.split("\t")
        name = carac[2].strip()
        number = int(carac[0])
        index += 1
        life = int(carac[3])
        attack = int(carac[4])
        defense = int(carac[5])
        spattack = int(carac[6])
        spdefense = int(carac[7])
        speed = int(carac[8])
        
        if name.find("(") == -1:
            list[name].update({"index": index, "life": life, "attack": attack, "defense": defense, "spattack": spattack, "spdefense": spdefense, "speed": speed})
        else:
            for baseName, p in list.items():
                if p["number"] == number and baseName.find("(") == -1:
                    break
            list[name] = list[baseName].copy()
            list[name].update({"name": name, "index": index, "life": life, "attack": attack, "defense": defense, "spattack": spattack, "spdefense": spdefense, "speed": speed})
            toRemove[baseName] = True
    
    for name, v in toRemove.items():
        # Decrease all indexes greater than the one to be removed
        for n, p in list.items():
            if list[name].has_key("index") and p.has_key("index") and p["index"] > list[name]["index"]:
                p["index"] -= 1
        del list[name]
    print list
    return
    
    text = ""
    for name, p in list.items():
        text += """

        talents = new ArrayList<Talent>(){{"""
        
        for talent in p["talents"]:
            text += "this.add(Talent.{});".format(talent)
        
        text += """}}}};
        this.put("{name}", new Pokemon("{name}", {number}, {index}, Type.{type1}, Type.{type2}, talents, {life}, {attack}, {defense}, {spattack}, {spdefense}, {speed}));""".format(**p)
    print text



types = """#001 	pokemon 	Bulbizarre 	Bulbasaur 	PLANTE
POISON		49 	65 	49 	65 	45
#002 	pokemon 	Herbizarre 	Ivysaur 	PLANTE
POISON		62 	80 	63 	80 	60
#003 	pokemon 	Florizarre 	Venusaur 	PLANTE
POISON		82 	100 	83 	100 	80
#004 	pokemon 	Salameche 	Charmander 	FEU
	52 	60 	43 	50 	65
#005 	pokemon 	Reptincel 	Charmeleon 	FEU
	64 	80 	58 	65 	80
#006 	pokemon 	Dracaufeu 	Charizard 	FEU
VOL		84 	109 	78 	85 	100
#007 	pokemon 	Carapuce 	Squirtle 	EAU
	48 	50 	65 	64 	43
#008 	pokemon 	Carabaffe 	Wartortle 	EAU
	58 	65 	80 	80 	63
#009 	pokemon 	Tortank 	Blastoise 	EAU
	83 	85 	100 	105 	78
#010 	pokemon 	Chenipan 	Caterpie 	INSECTE
	30 	20 	35 	20 	45
#011 	pokemon 	Chrysacier 	Metapod 	INSECTE
	20 	25 	55 	25 	30
#012 	pokemon 	Papilusion 	Butterfree 	INSECTE
VOL		45 	80 	50 	80 	70
#013 	pokemon 	Aspicot 	Weedle 	INSECTE
POISON		35 	20 	30 	20 	50
#014 	pokemon 	Coconfort 	Kakuna 	INSECTE
POISON		25 	25 	50 	25 	35
#015 	pokemon 	Dardargnan 	Beedrill 	INSECTE
POISON		80 	45 	40 	80 	75
#016 	pokemon 	Roucool 	Pidgey 	NORMAL
VOL		45 	35 	40 	35 	56
#017 	pokemon 	Roucoups 	Pidgeotto 	NORMAL
VOL		60 	50 	55 	50 	71
#018 	pokemon 	Roucarnage 	Pidgeot 	NORMAL
VOL		80 	70 	75 	70 	91
#019 	pokemon 	Rattata 	Rattata 	NORMAL
	56 	25 	35 	35 	72
#020 	pokemon 	Rattatac 	Raticate 	NORMAL
	81 	50 	60 	70 	97
#021 	pokemon 	Piafabec 	Spearow 	NORMAL
VOL		60 	31 	30 	31 	70
#022 	pokemon 	Rapasdepic 	Fearow 	NORMAL
VOL		90 	61 	65 	61 	100
#023 	pokemon 	Abo 	Ekans 	POISON
	60 	40 	44 	54 	55
#024 	pokemon 	Arbok 	Arbok 	POISON
	85 	65 	69 	79 	80
#025 	pokemon 	Pikachu 	Pikachu 	ELECTRIQUE
	55 	50 	30 	40 	90
#026 	pokemon 	Raichu 	Raichu 	ELECTRIQUE
	90 	90 	55 	80 	100
#027 	pokemon 	Sabelette 	Sandshrew 	SOL
	75 	20 	85 	30 	40
#028 	pokemon 	Sablaireau 	Sandslash 	SOL
	100 	45 	110 	55 	65
#029 	pokemon 	Nidoran F 	Nidoran? 	POISON
	47 	40 	52 	40 	41
#030 	pokemon 	Nidorina 	Nidorina 	POISON
	62 	55 	67 	55 	56
#031 	pokemon 	Nidoqueen 	Nidoqueen 	POISON
SOL		82 	75 	87 	85 	76
#032 	pokemon 	Nidoran M 	Nidoran? 	POISON
	57 	40 	40 	40 	50
#033 	pokemon 	Nidorino 	Nidorino 	POISON
	72 	55 	57 	55 	65
#034 	pokemon 	Nidoking 	Nidoking 	POISON
SOL		92 	85 	77 	75 	85
#035 	pokemon 	Melofee 	Clefairy 	NORMAL
	45 	60 	48 	65 	35
#036 	pokemon 	Melodelfe 	Clefable 	NORMAL
	70 	85 	73 	90 	65
#037 	pokemon 	Goupix 	Vulpix 	FEU
	41 	50 	40 	65 	65
#038 	pokemon 	Feunard 	Ninetales 	FEU
	76 	81 	75 	100 	100
#039 	pokemon 	Rondoudou 	Jigglypuff 	NORMAL
	45 	45 	20 	25 	20
#040 	pokemon 	Grodoudou 	Wigglytuff 	NORMAL
	70 	75 	45 	50 	45
#041 	pokemon 	Nosferapti 	Zubat 	POISON
VOL		45 	30 	35 	40 	55
#042 	pokemon 	Nosferalto 	Golbat 	POISON
VOL		80 	65 	70 	75 	90
#043 	pokemon 	Mystherbe 	Oddish 	PLANTE
POISON		45 	75 	50 	65 	55
#044 	pokemon 	Ortide 	Gloom 	PLANTE
POISON		65 	85 	70 	75 	40
#045 	pokemon 	Rafflesia 	Vileplume 	PLANTE
POISON		80 	100 	85 	90 	50
#046 	pokemon 	Paras 	Paras 	INSECTE
PLANTE		70 	45 	55 	55 	25
#047 	pokemon 	Parasect 	Parasect 	INSECTE
PLANTE		95 	60 	80 	80 	30
#048 	pokemon 	Mimitoss 	Venonat 	INSECTE
POISON		55 	40 	50 	55 	45
#049 	pokemon 	Aeromite 	Venomoth 	INSECTE
POISON		65 	90 	60 	75 	90
#050 	pokemon 	Taupiqueur 	Diglett 	SOL
	55 	35 	25 	45 	95
#051 	pokemon 	Triopikeur 	Dugtrio 	SOL
	80 	50 	50 	70 	120
#052 	pokemon 	Miaouss 	Meowth 	NORMAL
	45 	40 	35 	40 	90
#053 	pokemon 	Persian 	Persian 	NORMAL
	70 	65 	60 	65 	115
#054 	pokemon 	Psykokwak 	Psyduck 	EAU
	52 	65 	48 	50 	55
#055 	pokemon 	Akwakwak 	Golduck 	EAU
	82 	95 	78 	80 	85
#056 	pokemon 	Ferosinge 	Mankey 	COMBAT
	80 	35 	35 	45 	70
#057 	pokemon 	Colossinge 	Primeape 	COMBAT
	105 	60 	60 	70 	95
#058 	pokemon 	Caninos 	Growlithe 	FEU
	70 	70 	45 	50 	60
#059 	pokemon 	Arcanin 	Arcanine 	FEU
	110 	100 	80 	80 	95
#060 	pokemon 	Ptitard 	Poliwag 	EAU
	50 	40 	40 	40 	90
#061 	pokemon 	Tetarte 	Poliwhirl 	EAU
	65 	50 	65 	50 	90
#062 	pokemon 	Tartard 	Poliwrath 	EAU
COMBAT		85 	70 	95 	90 	70
#063 	pokemon 	Abra 	Abra 	PSY
	20 	105 	15 	55 	90
#064 	pokemon 	Kadabra 	Kadabra 	PSY
	35 	120 	30 	70 	105
#065 	pokemon 	Alakazam 	Alakazam 	PSY
	50 	135 	45 	85 	120
#066 	pokemon 	Machoc 	Machop 	COMBAT
	80 	35 	50 	35 	35
#067 	pokemon 	Machopeur 	Machoke 	COMBAT
	100 	50 	70 	60 	45
#068 	pokemon 	Mackogneur 	Machamp 	COMBAT
	130 	65 	80 	85 	55
#069 	pokemon 	Chetiflor 	Bellsprout 	PLANTE
POISON		75 	70 	35 	30 	40
#070 	pokemon 	Boustiflor 	Weepinbell 	PLANTE
POISON		90 	85 	50 	45 	55
#071 	pokemon 	Empiflor 	Victreebel 	PLANTE
POISON		105 	100 	65 	60 	70
#072 	pokemon 	Tentacool 	Tentacool 	EAU
POISON		40 	50 	35 	100 	70
#073 	pokemon 	Tentacruel 	Tentacruel 	EAU
POISON		70 	80 	65 	120 	100
#074 	pokemon 	Racaillou 	Geodude 	ROCHE
SOL		80 	30 	100 	30 	20
#075 	pokemon 	Gravalanch 	Graveler 	ROCHE
SOL		95 	45 	115 	45 	35
#076 	pokemon 	Grolem 	Golem 	ROCHE
SOL		110 	55 	130 	65 	45
#077 	pokemon 	Ponyta 	Ponyta 	FEU
	85 	65 	55 	65 	90
#078 	pokemon 	Galopa 	Rapidash 	FEU
	100 	80 	70 	80 	105
#079 	pokemon 	Ramoloss 	Slowpoke 	EAU
PSY		65 	40 	65 	40 	15
#080 	pokemon 	Flagadoss 	Slowbro 	EAU
PSY		75 	100 	110 	80 	30
#081 	pokemon 	Magneti 	Magnemite 	ELECTRIQUE
ACIER		35 	95 	70 	55 	45
#082 	pokemon 	Magneton 	Magneton 	ELECTRIQUE
ACIER		60 	120 	95 	70 	70
#083 	pokemon 	Canarticho 	Farfetch'd 	NORMAL
VOL		65 	58 	55 	62 	60
#084 	pokemon 	Doduo 	Doduo 	NORMAL
VOL		85 	35 	45 	35 	75
#085 	pokemon 	Dodrio 	Dodrio 	NORMAL
VOL		110 	60 	70 	60 	100
#086 	pokemon 	Otaria 	Seel 	EAU
	45 	45 	55 	70 	45
#087 	pokemon 	Lamantine 	Dewgong 	EAU
GLACE		70 	70 	80 	95 	70
#088 	pokemon 	Tadmorv 	Grimer 	POISON
	80 	40 	50 	50 	25
#089 	pokemon 	Grotadmorv 	Muk 	POISON
	105 	65 	75 	100 	50
#090 	pokemon 	Kokiyas 	Shellder 	EAU
	65 	45 	100 	25 	40
#091 	pokemon 	Crustabri 	Cloyster 	EAU
GLACE		95 	85 	180 	45 	70
#092 	pokemon 	Fantominus 	Gastly 	SPECTRE
POISON		35 	100 	30 	35 	80
#093 	pokemon 	Spectrum 	Haunter 	SPECTRE
POISON		50 	115 	45 	55 	95
#094 	pokemon 	Ectoplasma 	Gengar 	SPECTRE
POISON		65 	130 	60 	75 	110
#095 	pokemon 	Onix 	Onix 	ROCHE
SOL		45 	30 	160 	45 	70
#096 	pokemon 	Soporifik 	Drowzee 	PSY
	48 	43 	45 	90 	42
#097 	pokemon 	Hypnomade 	Hypno 	PSY
	73 	73 	70 	115 	67
#098 	pokemon 	Krabby 	Krabby 	EAU
	105 	25 	90 	25 	50
#099 	pokemon 	Krabboss 	Kingler 	EAU
	130 	50 	115 	50 	75
#100 	pokemon 	Voltorbe 	Voltorb 	ELECTRIQUE
	30 	55 	50 	55 	100
#101 	pokemon 	Electrode 	Electrode 	ELECTRIQUE
	50 	80 	70 	80 	140
#102 	pokemon 	Noeunoeuf 	Exeggcute 	PLANTE
PSY		40 	60 	80 	45 	40
#103 	pokemon 	Noadkoko 	Exeggutor 	PLANTE
PSY		95 	125 	85 	65 	55
#104 	pokemon 	Osselait 	Cubone 	SOL
	50 	40 	95 	50 	35
#105 	pokemon 	Ossatueur 	Marowak 	SOL
	80 	50 	110 	80 	45
#106 	pokemon 	Kicklee 	Hitmonlee 	COMBAT
	120 	35 	53 	110 	87
#107 	pokemon 	Tygnon 	Hitmonchan 	COMBAT
	105 	35 	79 	110 	76
#108 	pokemon 	Excelangue 	Lickitung 	NORMAL
	55 	60 	75 	75 	30
#109 	pokemon 	Smogo 	Koffing 	POISON
	65 	60 	95 	45 	35
#110 	pokemon 	Smogogo 	Weezing 	POISON
	90 	85 	120 	70 	60
#111 	pokemon 	Rhinocorne 	Rhyhorn 	SOL
ROCHE		85 	30 	95 	30 	25
#112 	pokemon 	Rhinoferos 	Rhydon 	SOL
ROCHE		130 	45 	120 	45 	40
#113 	pokemon 	Leveinard 	Chansey 	NORMAL
	5 	35 	5 	105 	50
#114 	pokemon 	Saquedeneu 	Tangela 	PLANTE
	55 	100 	115 	40 	60
#115 	pokemon 	Kangourex 	Kangaskhan 	NORMAL
	95 	40 	80 	80 	90
#116 	pokemon 	Hypotrempe 	Horsea 	EAU
	40 	70 	70 	25 	60
#117 	pokemon 	Hypocean 	Seadra 	EAU
	65 	95 	95 	45 	85
#118 	pokemon 	Poissirene 	Goldeen 	EAU
	67 	35 	60 	50 	63
#119 	pokemon 	Poissoroy 	Seaking 	EAU
	92 	65 	65 	80 	68
#120 	pokemon 	Stari 	Staryu 	EAU
	45 	70 	55 	55 	85
#121 	pokemon 	Staross 	Starmie 	EAU
PSY		75 	100 	85 	85 	115
#122 	pokemon 	M. Mime 	Mr. Mime 	PSY
	45 	100 	65 	120 	90
#123 	pokemon 	Insecateur 	Scyther 	INSECTE
VOL		110 	55 	80 	80 	105
#124 	pokemon 	Lippoutou 	Jynx 	GLACE
PSY		50 	115 	35 	95 	95
#125 	pokemon 	Elektek 	Electabuzz 	ELECTRIQUE
	83 	95 	57 	85 	105
#126 	pokemon 	Magmar 	Magmar 	FEU
	95 	100 	57 	85 	93
#127 	pokemon 	Scarabrute 	Pinsir 	INSECTE
	125 	55 	100 	70 	85
#128 	pokemon 	Tauros 	Tauros 	NORMAL
	100 	40 	95 	70 	110
#129 	pokemon 	Magicarpe 	Magikarp 	EAU
	10 	15 	55 	20 	80
#130 	pokemon 	Leviator 	Gyarados 	EAU
VOL		125 	60 	79 	100 	81
#131 	pokemon 	Lokhlass 	Lapras 	EAU
GLACE		85 	85 	80 	95 	60
#132 	pokemon 	Metamorph 	Ditto 	NORMAL
	48 	48 	48 	48 	48
#133 	pokemon 	Evoli 	Eevee 	NORMAL
	55 	45 	50 	65 	55
#134 	pokemon 	Aquali 	Vaporeon 	EAU
	65 	110 	60 	95 	65
#135 	pokemon 	Voltali 	Jolteon 	ELECTRIQUE
	65 	110 	60 	95 	130
#136 	pokemon 	Pyroli 	Flareon 	FEU
	130 	95 	60 	110 	65
#137 	pokemon 	Porygon 	Porygon 	NORMAL
	60 	85 	70 	75 	40
#138 	pokemon 	Amonita 	Omanyte 	ROCHE
EAU		40 	90 	100 	55 	35
#139 	pokemon 	Amonistar 	Omastar 	ROCHE
EAU		60 	115 	125 	70 	55
#140 	pokemon 	Kabuto 	Kabuto 	ROCHE
EAU		80 	55 	90 	45 	55
#141 	pokemon 	Kabutops 	Kabutops 	ROCHE
EAU		105 	65 	115 	70 	80
#142 	pokemon 	Ptera 	Aerodactyl 	ROCHE
VOL		105 	60 	65 	75 	130
#143 	pokemon 	Ronflex 	Snorlax 	NORMAL
	110 	65 	65 	110 	30
#144 	pokemon 	Artikodin 	Articuno 	GLACE
VOL		85 	95 	100 	125 	85
#145 	pokemon 	Electhor 	Zapdos 	ELECTRIQUE
VOL		90 	125 	85 	90 	100
#146 	pokemon 	Sulfura 	Moltres 	FEU
VOL		100 	125 	90 	85 	90
#147 	pokemon 	Minidraco 	Dratini 	DRAGON
	64 	50 	45 	50 	50
#148 	pokemon 	Draco 	Dragonair 	DRAGON
	84 	70 	85 	70 	70
#149 	pokemon 	Dracolosse 	Dragonite 	DRAGON
VOL		134 	100 	95 	100 	80
#150 	pokemon 	Mewtwo 	Mewtwo 	PSY
	110 	154 	90 	90 	130
#151 	pokemon 	Mew 	Mew 	PSY
	100 	100 	100 	100 	100
#152 	pokemon 	Germignon 	Chikorita 	PLANTE
	49 	49 	65 	65 	45
#153 	pokemon 	Macronium 	Bayleef 	PLANTE
	62 	63 	80 	80 	60
#154 	pokemon 	Meganium 	Meganium 	PLANTE
	82 	83 	100 	100 	80
#155 	pokemon 	Hericendre 	Cyndaquil 	FEU
	52 	60 	43 	50 	65
#156 	pokemon 	Feurisson 	Quilava 	FEU
	64 	80 	58 	65 	80
#157 	pokemon 	Typhlosion 	Typhlosion 	FEU
	84 	109 	78 	85 	100
#158 	pokemon 	Kaiminus 	Totodile 	EAU
	65 	44 	64 	48 	43
#159 	pokemon 	Crocrodil 	Croconaw 	EAU
	80 	59 	80 	63 	58
#160 	pokemon 	Aligatueur 	Feraligatr 	EAU
	105 	79 	100 	83 	78
#161 	pokemon 	Fouinette 	Sentret 	NORMAL
	46 	35 	34 	45 	20
#162 	pokemon 	Fouinar 	Furret 	NORMAL
	76 	45 	64 	55 	90
#163 	pokemon 	Hoot-hoot 	Hoot-hoot 	NORMAL
VOL		30 	36 	30 	56 	50
#164 	pokemon 	Noarfang 	Noctowl 	NORMAL
VOL		50 	76 	50 	96 	70
#165 	pokemon 	Coxy 	Ledyba 	INSECTE
VOL		20 	40 	30 	80 	55
#166 	pokemon 	Coxyclaque 	Ledian 	INSECTE
VOL		35 	55 	50 	110 	85
#167 	pokemon 	Mimigal 	Spinarak 	INSECTE
POISON		60 	40 	40 	40 	30
#168 	pokemon 	Migalos 	Ariados 	INSECTE
POISON		90 	60 	70 	60 	40
#169 	pokemon 	Nostenfer 	Crobat 	POISON
VOL		90 	70 	80 	80 	130
#170 	pokemon 	Loupio 	Chinchou 	EAU
ELECTRIQUE		38 	56 	38 	56 	67
#171 	pokemon 	Lanturn 	Lanturn 	EAU
ELECTRIQUE		58 	76 	58 	76 	67
#172 	pokemon 	Pichu 	Pichu 	ELECTRIQUE
	40 	35 	15 	35 	60
#173 	pokemon 	Melo 	Cleffa 	NORMAL
	25 	45 	28 	55 	15
#174 	pokemon 	Toudoudou 	Igglybuff 	NORMAL
	30 	40 	15 	20 	15
#175 	pokemon 	Togepi 	Togepi 	NORMAL
	20 	40 	65 	65 	20
#176 	pokemon 	Togetic 	Togetic 	NORMAL
VOL		40 	80 	85 	105 	40
#177 	pokemon 	Natu 	Natu 	PSY
VOL		50 	70 	45 	45 	70
#178 	pokemon 	Xatu 	Xatu 	PSY
VOL		75 	95 	70 	70 	95
#179 	pokemon 	Wattouat 	Mareep 	ELECTRIQUE
	40 	65 	40 	45 	35
#180 	pokemon 	Lainergie 	Flaaffy 	ELECTRIQUE
	55 	80 	55 	60 	45
#181 	pokemon 	Pharamp 	Ampharos 	ELECTRIQUE
	75 	115 	75 	70 	55
#182 	pokemon 	Joliflor 	Bellossom 	PLANTE
	80 	90 	85 	100 	50
#183 	pokemon 	Marill 	Marill 	EAU
	20 	20 	50 	50 	40
#184 	pokemon 	Azumarill 	Azumarill 	EAU
	50 	50 	80 	80 	50
#185 	pokemon 	Simularbre 	Sudowoodo 	ROCHE
	100 	30 	115 	65 	30
#186 	pokemon 	Tarpaud 	Politoed 	EAU
	75 	90 	75 	100 	70
#187 	pokemon 	Granivol 	Hoppip 	PLANTE
VOL		35 	35 	40 	55 	50
#188 	pokemon 	Floravol 	Skiploom 	PLANTE
VOL		45 	45 	50 	65 	80
#189 	pokemon 	Cotovol 	Jumpluff 	PLANTE
VOL		55 	55 	70 	85 	110
#190 	pokemon 	Capumain 	Aipom 	NORMAL
	70 	40 	55 	55 	85
#191 	pokemon 	Tournegrin 	Sunkern 	PLANTE
	30 	30 	30 	30 	30
#192 	pokemon 	Heliatronc 	Sunflora 	PLANTE
	75 	105 	55 	85 	30
#193 	pokemon 	Yanma 	Yanma 	INSECTE
VOL		65 	75 	45 	45 	95
#194 	pokemon 	Axoloto 	Wooper 	EAU
SOL		45 	25 	45 	25 	15
#195 	pokemon 	Maraiste 	Quagsire 	EAU
SOL		85 	65 	85 	65 	35
#196 	pokemon 	Mentali 	Espeon 	PSY
	65 	130 	60 	85 	110
#197 	pokemon 	Noctali 	Umbreon 	TENEBRE
	65 	60 	110 	130 	65
#198 	pokemon 	Cornebre 	Murkrow 	TENEBRE
VOL		85 	85 	42 	42 	91
#199 	pokemon 	Roigada 	Slowking 	EAU
PSY		75 	100 	80 	110 	30
#200 	pokemon 	Feuforeve 	Misdreavus 	SPECTRE
	60 	85 	60 	85 	85
#201 	pokemon 	Zarbi 	Unown 	PSY
	72 	72 	48 	48 	48
#202 	pokemon 	Qulbutoke 	Wobbuffet 	PSY
	33 	33 	58 	58 	33
#203 	pokemon 	Girafarig 	Girafarig 	NORMAL
PSY		80 	90 	65 	65 	85
#204 	pokemon 	Pomdepik 	Pineco 	INSECTE
	65 	35 	90 	35 	15
#205 	pokemon 	Foretress 	Forretress 	INSECTE
ACIER		90 	60 	140 	60 	40
#206 	pokemon 	Insolourdo 	Dunsparce 	NORMAL
	70 	65 	70 	65 	45
#207 	pokemon 	Scorplane 	Gligar 	SOL
VOL		75 	35 	108 	65 	85
#208 	pokemon 	Steelix 	Steelix 	ACIER
SOL		85 	55 	200 	65 	30
#209 	pokemon 	Snubbull 	Snubbull 	NORMAL
	80 	40 	50 	40 	30
#210 	pokemon 	Granbull 	Granbull 	NORMAL
	120 	60 	75 	60 	45
#211 	pokemon 	Qwilfish 	Qwilfish 	EAU
POISON		95 	55 	75 	55 	85
#212 	pokemon 	Cizayox 	Scizor 	INSECTE
ACIER		130 	55 	100 	80 	65
#213 	pokemon 	Caratroc 	Shuckle 	INSECTE
ROCHE		10 	10 	230 	230 	5
#214 	pokemon 	Scarhino 	Heracross 	INSECTE
COMBAT		125 	40 	75 	95 	85
#215 	pokemon 	Farfuret 	Sneasel 	TENEBRE
GLACE		95 	35 	55 	75 	115
#216 	pokemon 	Teddiursa 	Teddiursa 	NORMAL
	80 	50 	50 	50 	40
#217 	pokemon 	Ursaring 	Ursaring 	NORMAL
	130 	75 	75 	75 	55
#218 	pokemon 	Limagma 	Slugma 	FEU
	40 	70 	40 	40 	20
#219 	pokemon 	Volcaropod 	Magcargo 	FEU
ROCHE		50 	80 	120 	80 	30
#220 	pokemon 	Marcacrin 	Swinub 	GLACE
SOL		50 	30 	40 	30 	50
#221 	pokemon 	Cochignon 	Piloswine 	GLACE
SOL		100 	60 	80 	60 	50
#222 	pokemon 	Corayon 	Corsola 	EAU
ROCHE		55 	65 	85 	85 	35
#223 	pokemon 	Remoraid 	Remoraid 	EAU
	65 	65 	35 	35 	65
#224 	pokemon 	Octillery 	Octillery 	EAU
	105 	105 	75 	75 	45
#225 	pokemon 	Cadoizo 	Delibird 	GLACE
VOL		55 	65 	45 	45 	75
#226 	pokemon 	Demanta 	Mantine 	EAU
VOL		40 	80 	70 	140 	70
#227 	pokemon 	Airmure 	Skarmory 	ACIER
VOL		80 	40 	140 	70 	70
#228 	pokemon 	Malosse 	Houndour 	TENEBRE
FEU		60 	80 	30 	50 	65
#229 	pokemon 	Demolosse 	Houndoom 	TENEBRE
FEU		90 	110 	50 	80 	95
#230 	pokemon 	Hyporoi 	Kingdra 	EAU
DRAGON		95 	95 	95 	95 	85
#231 	pokemon 	Phanpy 	Phanpy 	SOL
	60 	40 	60 	40 	40
#232 	pokemon 	Donphan 	Donphan 	SOL
	120 	60 	120 	60 	50
#233 	pokemon 	Porygon2 	Porygon2 	NORMAL
	80 	105 	90 	95 	60
#234 	pokemon 	Cerfrousse 	Stantler 	NORMAL
	95 	85 	62 	65 	85
#235 	pokemon 	Queulorior 	Smeargle 	NORMAL
	20 	20 	35 	45 	75
#236 	pokemon 	Debugant 	Tyrogue 	COMBAT
	35 	35 	35 	35 	35
#237 	pokemon 	Kapoera 	Hitmontop 	COMBAT
	95 	35 	95 	110 	70
#238 	pokemon 	Lippouti 	Smoochum 	GLACE
PSY		30 	85 	15 	65 	65
#239 	pokemon 	Elekid 	Elekid 	ELECTRIQUE
	63 	65 	37 	55 	95
#240 	pokemon 	Magby 	Magby 	FEU
	75 	70 	37 	55 	83
#241 	pokemon 	Ecremeuh 	Miltank 	NORMAL
	80 	40 	105 	70 	100
#242 	pokemon 	Leuphorie 	Blissey 	NORMAL
	10 	75 	10 	135 	55
#243 	pokemon 	Raikou 	Raikou 	ELECTRIQUE
	85 	115 	75 	100 	115
#244 	pokemon 	Entei 	Entei 	FEU
	115 	90 	85 	75 	100
#245 	pokemon 	Suicune 	Suicune 	EAU
	75 	90 	115 	115 	85
#246 	pokemon 	Embrylex 	Larvitar 	ROCHE
SOL		64 	45 	50 	50 	41
#247 	pokemon 	Ymphect 	Pupitar 	ROCHE
SOL		84 	65 	70 	70 	51
#248 	pokemon 	Tyranocif 	Tyranitar 	ROCHE
TENEBRE		134 	95 	110 	100 	61
#249 	pokemon 	Lugia 	Lugia 	PSY
VOL		90 	90 	130 	154 	110
#250 	pokemon 	Ho-Oh 	Ho-Oh 	FEU
VOL		130 	110 	90 	154 	90
#251 	pokemon 	Celebi 	Celebi 	PSY
PLANTE		100 	100 	100 	100 	100
#252 	pokemon 	Arcko 	Treecko 	PLANTE
	45 	65 	35 	55 	70
#253 	pokemon 	Massko 	Grovyle 	PLANTE
	65 	85 	45 	65 	95
#254 	pokemon 	Jungko 	Sceptile 	PLANTE
	85 	105 	65 	85 	120
#255 	pokemon 	Poussifeu 	Torchic 	FEU
	60 	70 	40 	50 	45
#256 	pokemon 	Galifeu 	Combusken 	FEU
COMBAT		85 	85 	60 	60 	55
#257 	pokemon 	Brasegali 	Blaziken 	FEU
COMBAT		120 	110 	70 	70 	80
#258 	pokemon 	Gobou 	Mudkip 	EAU
	70 	50 	50 	50 	40
#259 	pokemon 	Flobio 	Marshtomp 	EAU
SOL		85 	60 	70 	70 	50
#260 	pokemon 	Laggron 	Swampert 	EAU
SOL		110 	85 	90 	90 	60
#261 	pokemon 	Medhyena 	Poochyena 	TENEBRE
	55 	30 	35 	30 	35
#262 	pokemon 	Grahyena 	Mightyena 	TENEBRE
	90 	60 	70 	60 	70
#263 	pokemon 	Zigzaton 	Zigzagoon 	NORMAL
	30 	30 	41 	41 	60
#264 	pokemon 	Lineon 	Linoone 	NORMAL
	70 	50 	61 	61 	100
#265 	pokemon 	Chenipotte 	Wurmple 	INSECTE
	45 	20 	35 	30 	20
#266 	pokemon 	Armulys 	Silcoon 	INSECTE
	35 	25 	55 	25 	15
#267 	pokemon 	Charmillon 	Beautifly 	INSECTE
VOL		70 	90 	50 	50 	65
#268 	pokemon 	Blindalys 	Cascoon 	INSECTE
	35 	25 	55 	25 	15
#269 	pokemon 	Papinox 	Dustox 	INSECTE
POISON		50 	50 	70 	90 	65
#270 	pokemon 	Nenupiot 	Lotad 	EAU
PLANTE		30 	40 	30 	50 	30
#271 	pokemon 	Lombre 	Lombre 	EAU
PLANTE		50 	60 	50 	70 	50
#272 	pokemon 	Ludicolo 	Ludicolo 	EAU
PLANTE		70 	90 	70 	100 	70
#273 	pokemon 	Grainipiot 	Seedot 	PLANTE
	40 	30 	50 	30 	30
#274 	pokemon 	Pifeuil 	Nuzleaf 	PLANTE
TENEBRE		70 	60 	40 	40 	60
#275 	pokemon 	Tengalice 	Shiftry 	PLANTE
TENEBRE		100 	90 	60 	60 	80
#276 	pokemon 	Nirondelle 	Taillow 	NORMAL
VOL		55 	30 	30 	30 	85
#277 	pokemon 	Heledelle 	Swellow 	NORMAL
VOL		85 	50 	60 	50 	125
#278 	pokemon 	Goelise 	Wingull 	EAU
VOL		30 	55 	30 	30 	85
#279 	pokemon 	Bekipan 	Pelipper 	EAU
VOL		50 	85 	100 	70 	65
#280 	pokemon 	Tarsal 	Ralts 	PSY
	25 	45 	25 	35 	40
#281 	pokemon 	Kirlia 	Kirlia 	PSY
	35 	65 	35 	55 	50
#282 	pokemon 	Gardevoir 	Gardevoir 	PSY
	65 	125 	65 	115 	80
#283 	pokemon 	Arakdo 	Surskit 	INSECTE
EAU		30 	50 	32 	52 	65
#284 	pokemon 	Maskadra 	Masquerain 	INSECTE
VOL		60 	80 	62 	82 	60
#285 	pokemon 	Balignon 	Shroomish 	PLANTE
	40 	40 	60 	60 	35
#286 	pokemon 	Chapignon 	Breloom 	PLANTE
COMBAT		130 	60 	80 	60 	70
#287 	pokemon 	Parecool 	Slakoth 	NORMAL
	60 	35 	60 	35 	30
#288 	pokemon 	Vigoroth 	Vigoroth 	NORMAL
	80 	55 	80 	55 	90
#289 	pokemon 	Monaflemit 	Slaking 	NORMAL
	160 	95 	100 	65 	100
#290 	pokemon 	Ningale 	Nincada 	INSECTE
SOL		45 	30 	90 	30 	40
#291 	pokemon 	Ninjask 	Ninjask 	INSECTE
VOL		90 	50 	45 	50 	160
#292 	pokemon 	Munja 	Shedinja 	INSECTE
SPECTRE		90 	30 	45 	30 	40
#293 	pokemon 	Chuchmur 	Whismur 	NORMAL
	51 	51 	23 	23 	28
#294 	pokemon 	Ramboum 	Loudred 	NORMAL
	71 	71 	43 	43 	48
#295 	pokemon 	Brouhabam 	Exploud 	NORMAL
	91 	91 	63 	63 	68
#296 	pokemon 	Makuhita 	Makuhita 	COMBAT
	60 	20 	30 	30 	25
#297 	pokemon 	Hariyama 	Hariyama 	COMBAT
	120 	40 	60 	60 	50
#298 	pokemon 	Azurill 	Azurill 	NORMAL
	20 	20 	40 	40 	20
#299 	pokemon 	Tarinor 	Nosepass 	ROCHE
	45 	45 	135 	90 	30
#300 	pokemon 	Skitty 	Skitty 	NORMAL
	45 	35 	45 	35 	50
#301 	pokemon 	Delcatty 	Delcatty 	NORMAL
	65 	55 	65 	55 	70
#302 	pokemon 	Tenefix 	Sableye 	TENEBRE
SPECTRE		75 	65 	75 	65 	50
#303 	pokemon 	Mysdibule 	Mawile 	ACIER
	85 	55 	85 	55 	50
#304 	pokemon 	Galekid 	Aron 	ACIER
ROCHE		70 	40 	100 	40 	30
#305 	pokemon 	Galegon 	Lairon 	ACIER
ROCHE		90 	50 	140 	50 	40
#306 	pokemon 	Galeking 	Aggron 	ACIER
ROCHE		110 	60 	180 	60 	50
#307 	pokemon 	Meditikka 	Meditite 	COMBAT
PSY		40 	40 	55 	55 	60
#308 	pokemon 	Charmina 	Medicham 	COMBAT
PSY		60 	60 	75 	75 	80
#309 	pokemon 	Dynavolt 	Electrike 	ELECTRIQUE
	45 	65 	40 	40 	65
#310 	pokemon 	Elecsprint 	Manectric 	ELECTRIQUE
	75 	105 	60 	60 	105
#311 	pokemon 	Posipi 	Plusle 	ELECTRIQUE
	50 	85 	40 	75 	95
#312 	pokemon 	Negapi 	Minun 	ELECTRIQUE
	40 	75 	50 	85 	95
#313 	pokemon 	Muciole 	Volbeat 	INSECTE
	73 	47 	55 	75 	85
#314 	pokemon 	Lumivole 	Illumise 	INSECTE
	47 	73 	55 	75 	85
#315 	pokemon 	Roselia 	Roselia 	PLANTE
POISON		60 	100 	45 	80 	65
#316 	pokemon 	Gloupti 	Gulpin 	POISON
	43 	43 	53 	53 	40
#317 	pokemon 	Avaltout 	Swalot 	POISON
	73 	73 	83 	83 	55
#318 	pokemon 	Carvanha 	Carvanha 	EAU
TENEBRE		90 	65 	20 	20 	65
#319 	pokemon 	Sharpedo 	Sharpedo 	EAU
TENEBRE		120 	95 	40 	40 	95
#320 	pokemon 	Wailmer 	Wailmer 	EAU
	70 	70 	35 	35 	60
#321 	pokemon 	Wailord 	Wailord 	EAU
	90 	90 	45 	45 	60
#322 	pokemon 	Chamallot 	Numel 	FEU
SOL		60 	65 	40 	45 	35
#323 	pokemon 	Camerupt 	Camerupt 	FEU
SOL		100 	105 	70 	75 	40
#324 	pokemon 	Chartor 	Torkoal 	FEU
	85 	85 	140 	70 	20
#325 	pokemon 	Spoink 	Spoink 	PSY
	25 	70 	35 	80 	60
#326 	pokemon 	Groret 	Grumpig 	PSY
	45 	90 	65 	110 	80
#327 	pokemon 	Spinda 	Spinda 	NORMAL
	60 	60 	60 	60 	60
#328 	pokemon 	Kraknoix 	Trapinch 	SOL
	100 	45 	45 	45 	10
#329 	pokemon 	Vibraninf 	Vibrava 	SOL
DRAGON		70 	50 	50 	50 	70
#330 	pokemon 	Libegon 	Flygon 	SOL
DRAGON		100 	80 	80 	80 	100
#331 	pokemon 	Cacnea 	Cacnea 	PLANTE
	85 	85 	40 	40 	35
#332 	pokemon 	Cacturne 	Cacturne 	PLANTE
TENEBRE		115 	115 	60 	60 	55
#333 	pokemon 	Tylton 	Swablu 	NORMAL
VOL		40 	40 	60 	75 	50
#334 	pokemon 	Altaria 	Altaria 	DRAGON
VOL		70 	70 	90 	105 	80
#335 	pokemon 	Mangriff 	Zangoose 	NORMAL
	115 	60 	60 	60 	90
#336 	pokemon 	Seviper 	Seviper 	POISON
	100 	100 	60 	60 	65
#337 	pokemon 	Seleroc 	Lunatone 	ROCHE
PSY		55 	95 	65 	85 	70
#338 	pokemon 	Solaroc 	Solrock 	ROCHE
PSY		95 	55 	85 	65 	70
#339 	pokemon 	Barloche 	Barboach 	EAU
SOL		48 	46 	43 	41 	60
#340 	pokemon 	Barbicha 	Whiscash 	EAU
SOL		78 	76 	73 	71 	60
#341 	pokemon 	Ecrapince 	Corphish 	EAU
	80 	50 	65 	35 	35
#342 	pokemon 	Colhomard 	Crawdaunt 	EAU
TENEBRE		120 	90 	85 	55 	55
#343 	pokemon 	Balbuto 	Baltoy 	SOL
PSY		40 	40 	55 	70 	55
#344 	pokemon 	Kaorine 	Claydol 	SOL
PSY		70 	70 	105 	120 	75
#345 	pokemon 	Lilia 	Lileep 	ROCHE
PLANTE		41 	61 	77 	87 	23
#346 	pokemon 	Vacilys 	Cradily 	ROCHE
PLANTE		81 	81 	97 	107 	43
#347 	pokemon 	Anorith 	Anorith 	ROCHE
INSECTE		95 	40 	50 	50 	75
#348 	pokemon 	Armaldo 	Armaldo 	ROCHE
INSECTE		125 	70 	100 	80 	45
#349 	pokemon 	Barpau 	Feebas 	EAU
	15 	10 	20 	55 	80
#350 	pokemon 	Milobellus 	Milotic 	EAU
	60 	100 	79 	125 	81
#351 	pokemon 	Morpheo 	Castform 	NORMAL
	70 	70 	70 	70 	70
#352 	pokemon 	Kecleon 	Kecleon 	NORMAL
	90 	60 	70 	120 	40
#353 	pokemon 	Polichombr 	Shuppet 	SPECTRE
	75 	63 	35 	33 	45
#354 	pokemon 	Branette 	Banette 	SPECTRE
	115 	83 	65 	63 	65
#355 	pokemon 	Skelenox 	Duskull 	SPECTRE
	40 	30 	90 	90 	25
#356 	pokemon 	Teraclope 	Dusclops 	SPECTRE
	70 	60 	130 	130 	25
#357 	pokemon 	Tropius 	Tropius 	PLANTE
VOL		68 	72 	83 	87 	51
#358 	pokemon 	Eoko 	Chimecho 	PSY
	50 	95 	70 	80 	65
#359 	pokemon 	Absol 	Absol 	TENEBRE
	130 	75 	60 	60 	75
#360 	pokemon 	Okeoke 	Wynaut 	PSY
	23 	23 	48 	48 	23
#361 	pokemon 	Stalgamin 	Snorunt 	GLACE
	50 	50 	50 	50 	50
#362 	pokemon 	Oniglali 	Glalie 	GLACE
	80 	80 	80 	80 	80
#363 	pokemon 	Obalie 	Spheal 	GLACE
EAU		40 	55 	50 	50 	25
#364 	pokemon 	Phogleur 	Sealeo 	GLACE
EAU		60 	75 	70 	70 	45
#365 	pokemon 	Kaimorse 	Walrein 	GLACE
EAU		80 	95 	90 	90 	65
#366 	pokemon 	Coquiperl 	Clamperl 	EAU
	64 	74 	85 	55 	32
#367 	pokemon 	Serpang 	Huntail 	EAU
	104 	94 	105 	75 	52
#368 	pokemon 	Rosabyss 	Gorebyss 	EAU
	84 	114 	105 	75 	52
#369 	pokemon 	Relicanth 	Relicanth 	EAU
ROCHE		90 	45 	130 	65 	55
#370 	pokemon 	Lovdisc 	Luvdisc 	EAU
	30 	40 	55 	65 	97
#371 	pokemon 	Draby 	Bagon 	DRAGON
	75 	40 	60 	30 	50
#372 	pokemon 	Drackhaus 	Shelgon 	DRAGON
	95 	60 	100 	50 	50
#373 	pokemon 	Drattak 	Salamence 	DRAGON
VOL		135 	110 	80 	80 	100
#374 	pokemon 	Terhal 	Beldum 	ACIER
PSY		55 	35 	80 	60 	30
#375 	pokemon 	Metang 	Metang 	ACIER
PSY		75 	55 	100 	80 	50
#376 	pokemon 	Metalosse 	Metagross 	ACIER
PSY		135 	95 	130 	90 	70
#377 	pokemon 	Regirock 	Regirock 	ROCHE
	100 	50 	200 	100 	50
#378 	pokemon 	Regice 	Regice 	GLACE
	50 	100 	100 	200 	50
#379 	pokemon 	Registeel 	Registeel 	ACIER
	75 	75 	150 	150 	50
#380 	pokemon 	Latias 	Latias 	DRAGON
PSY		80 	110 	90 	130 	110
#381 	pokemon 	Latios 	Latios 	DRAGON
PSY		90 	130 	80 	110 	110
#382 	pokemon 	Kyogre 	Kyogre 	EAU
	100 	150 	90 	140 	90
#383 	pokemon 	Groudon 	Groudon 	SOL
	150 	100 	140 	90 	90
#384 	pokemon 	Rayquaza 	Rayquaza 	DRAGON
VOL		150 	150 	90 	90 	95
#385 	pokemon 	Jirachi 	Jirachi 	ACIER
PSY		100 	100 	100 	100 	100
#386 	pokemon 	Deoxys 	Deoxys 	PSY
	150 	150 	50 	50 	150
#387 	pokemon 	Tortipouss 	Turtwig 	PLANTE
	68 	45 	64 	55 	31
#388 	pokemon 	Boskara 	Grotle 	PLANTE
	89 	65 	85 	55 	36
#389 	pokemon 	Torterra 	Torterra 	PLANTE
SOL		109 	75 	105 	85 	56
#390 	pokemon 	Ouisticram 	Chimchar 	FEU
	58 	58 	44 	44 	61
#391 	pokemon 	Chimpenfeu 	Monferno 	FEU
COMBAT		78 	78 	52 	52 	81
#392 	pokemon 	Simiabraz 	Infernape 	FEU
COMBAT		104 	104 	71 	71 	108
#393 	pokemon 	Tiplouf 	Piplup 	EAU
	51 	61 	53 	56 	40
#394 	pokemon 	Prinplouf 	Prinplup 	EAU
	66 	81 	68 	76 	50
#395 	pokemon 	Pingoleon 	Empoleon 	EAU
ACIER		86 	111 	88 	101 	60
#396 	pokemon 	Etourmi 	Starly 	NORMAL
VOL		55 	30 	30 	30 	60
#397 	pokemon 	Etourvol 	Staravia 	NORMAL
VOL		75 	40 	50 	40 	80
#398 	pokemon 	Etouraptor 	Staraptor 	NORMAL
VOL		120 	50 	70 	50 	100
#399 	pokemon 	Keunotor 	Bidoof 	NORMAL
	45 	35 	40 	40 	31
#400 	pokemon 	Castorno 	Bibarel 	NORMAL
EAU		85 	55 	60 	60 	71
#401 	pokemon 	Crikzik 	Kricketot 	INSECTE
	25 	25 	41 	41 	25
#402 	pokemon 	Melokrik 	Kricketune 	INSECTE
	85 	55 	51 	51 	65
#403 	pokemon 	Lixy 	Shinx 	ELECTRIQUE
	65 	40 	34 	34 	45
#404 	pokemon 	Luxio 	Luxio 	ELECTRIQUE
	85 	60 	49 	49 	60
#405 	pokemon 	Luxray 	Luxray 	ELECTRIQUE
	120 	95 	79 	79 	70
#406 	pokemon 	Rozbouton 	Budew 	PLANTE
	30 	50 	35 	70 	55
#407 	pokemon 	Roserade 	Roserade 	PLANTE
POISON		70 	125 	55 	105 	90
#408 	pokemon 	Kranidos 	Cranidos 	ROCHE
	125 	30 	40 	30 	58
#409 	pokemon 	Charkos 	Rampardos 	ROCHE
	165 	65 	60 	50 	58
#410 	pokemon 	Dinoclier 	Shieldon 	ROCHE
ACIER		42 	42 	118 	88 	30
#411 	pokemon 	Bastiodon 	Bastiodon 	ROCHE
ACIER		52 	47 	168 	138 	30
#412 	pokemon 	Cheniti 	Burmy 	INSECTE
	29 	29 	45 	45 	36
#413 	pokemon 	Cheniselle 	Wormadam 	INSECTE
	59 	79 	85 	105 	36
#414 	pokemon 	Papilord 	Mothim 	INSECTE
VOL		94 	94 	50 	50 	66
#415 	pokemon 	Apitrini 	Combee 	INSECTE
VOL		30 	30 	42 	42 	70
#416 	pokemon 	Apireine 	Vespiquen 	INSECTE
VOL		80 	80 	102 	102 	40
#417 	pokemon 	Pachirisu 	Pachirisu 	ELECTRIQUE
	45 	45 	70 	90 	95
#418 	pokemon 	Mustebouee 	Buizel 	EAU
	65 	60 	35 	30 	85
#419 	pokemon 	Musteflott 	Floatzel 	EAU
	105 	85 	55 	50 	115
#420 	pokemon 	Ceribou 	Cherubi 	PLANTE
	35 	62 	45 	53 	35
#421 	pokemon 	Ceriflor 	Cherrim 	PLANTE
	60 	87 	70 	78 	85
#422 	pokemon 	Sancoki 	Shellos 	EAU
	48 	57 	48 	62 	34
#423 	pokemon 	Tritosor 	Gastrodon 	EAU
SOL		83 	92 	68 	82 	39
#424 	pokemon 	Capidextre 	Ambipom 	NORMAL
	100 	60 	66 	66 	115
#425 	pokemon 	Baudrive 	Drifloon 	SPECTRE
VOL		50 	60 	34 	44 	70
#426 	pokemon 	Grodrive 	Drifblim 	SPECTRE
VOL		44 	54 	90 	80 	80
#427 	pokemon 	Laporeille 	Buneary 	NORMAL
	66 	44 	44 	56 	85
#428 	pokemon 	Lockpin 	Lopunny 	NORMAL
	76 	54 	84 	96 	105
#429 	pokemon 	Magireve 	Mismagius 	SPECTRE
	60 	105 	60 	105 	105
#430 	pokemon 	Corboss 	Honchkrow 	TENEBRE
VOL		125 	105 	52 	52 	71
#431 	pokemon 	Chaglam 	Glameow 	NORMAL
	55 	42 	42 	37 	85
#432 	pokemon 	Chaffreux 	Purugly 	NORMAL
	82 	64 	64 	59 	112
#433 	pokemon 	Korillon 	Chingling 	PSY
	30 	65 	50 	50 	45
#434 	pokemon 	Moufouette 	Stunky 	POISON
TENEBRE		63 	41 	47 	41 	74
#435 	pokemon 	Moufflair 	Skuntank 	POISON
TENEBRE		93 	71 	67 	61 	84
#436 	pokemon 	Archeomire 	Bronzor 	ACIER
PSY		24 	24 	86 	86 	23
#437 	pokemon 	Archeodong 	Bronzong 	ACIER
PSY		89 	79 	116 	116 	33
#438 	pokemon 	Manzai 	Bonsly 	ROCHE
	80 	10 	95 	45 	10
#439 	pokemon 	Mime Jr. 	Mime Jr. 	PSY
	25 	70 	45 	90 	60
#440 	pokemon 	Ptiravi 	Happiny 	NORMAL
	5 	15 	5 	65 	30
#441 	pokemon 	Pijako 	Chatot 	NORMAL
VOL		65 	92 	45 	42 	91
#442 	pokemon 	Spiritomb 	Spiritomb 	SPECTRE
TENEBRE		92 	92 	108 	108 	35
#443 	pokemon 	Griknot 	Gible 	DRAGON
SOL		70 	40 	45 	45 	42
#444 	pokemon 	Carmache 	Gabite 	DRAGON
SOL		90 	50 	65 	55 	82
#445 	pokemon 	Carchacrok 	Garchomp 	DRAGON
SOL		130 	80 	95 	85 	102
#446 	pokemon 	Goinfrex 	Munchlax 	NORMAL
	85 	40 	40 	85 	5
#447 	pokemon 	Riolu 	Riolu 	COMBAT
	70 	35 	40 	40 	60
#448 	pokemon 	Lucario 	Lucario 	COMBAT
ACIER		110 	115 	70 	70 	90
#449 	pokemon 	Hippopotas 	Hippopotas 	SOL
	72 	38 	78 	42 	32
#450 	pokemon 	Hippodocus 	Hippowdon 	SOL
	112 	68 	118 	72 	47
#451 	pokemon 	Rapion 	Skorupi 	POISON
INSECTE		50 	30 	90 	55 	65
#452 	pokemon 	Drascore 	Drapion 	POISON
TENEBRE		90 	60 	110 	75 	95
#453 	pokemon 	Cradopaud 	Croagunk 	POISON
COMBAT		61 	61 	40 	40 	50
#454 	pokemon 	Coatox 	Toxicroak 	POISON
COMBAT		106 	86 	65 	65 	85
#455 	pokemon 	Vortente 	Carnivine 	PLANTE
	100 	90 	72 	72 	46
#456 	pokemon 	Ecayon 	Finneon 	EAU
	49 	49 	56 	61 	66
#457 	pokemon 	Lumineon 	Lumineon 	EAU
	69 	69 	76 	86 	91
#458 	pokemon 	Babimanta 	Mantyke 	EAU
VOL		20 	60 	50 	120 	50
#459 	pokemon 	Blizzi 	Snover 	PLANTE
GLACE		62 	62 	50 	60 	40
#460 	pokemon 	Blizzaroi 	Abomasnow 	PLANTE
GLACE		92 	92 	75 	85 	60
#461 	pokemon 	Dimoret 	Weavile 	TENEBRE
GLACE		120 	45 	65 	85 	125
#462 	pokemon 	Magnezone 	Magnezone 	ELECTRIQUE
ACIER		70 	130 	115 	90 	60
#463 	pokemon 	Coudlangue 	Lickilicky 	NORMAL
	85 	80 	95 	95 	50
#464 	pokemon 	Rhinastoc 	Rhyperior 	SOL
ROCHE		140 	55 	130 	55 	40
#465 	pokemon 	Bouldeneu 	Tangrowth 	PLANTE
	100 	110 	125 	50 	50
#466 	pokemon 	Elekable 	Electivire 	ELECTRIQUE
	123 	95 	67 	85 	95
#467 	pokemon 	Maganon 	Magmortar 	FEU
	95 	125 	67 	95 	83
#468 	pokemon 	Togekiss 	Togekiss 	NORMAL
VOL		50 	120 	95 	115 	80
#469 	pokemon 	Yanmega 	Yanmega 	INSECTE
VOL		76 	116 	86 	56 	95
#470 	pokemon 	Phyllali 	Leafeon 	PLANTE
	110 	60 	130 	65 	95
#471 	pokemon 	Givrali 	Glaceon 	GLACE
	60 	130 	110 	95 	65
#472 	pokemon 	Scorvol 	Gliscor 	SOL
VOL		95 	45 	125 	75 	95
#473 	pokemon 	Mammochon 	Mamoswine 	GLACE
SOL		130 	70 	80 	60 	80
#474 	pokemon 	Porygon-Z 	Porygon-Z 	PSY
	80 	135 	70 	75 	90
#475 	pokemon 	Gallame 	Gallade 	PSY
COMBAT		125 	65 	65 	125 	80
#476 	pokemon 	Tarinorme 	Probopass 	ROCHE
ACIER		55 	75 	145 	150 	40
#477 	pokemon 	Noctunoir 	Dusknoir 	SPECTRE
	100 	65 	135 	135 	45
#478 	pokemon 	Momartik 	Froslass 	GLACE
SPECTRE		80 	80 	70 	70 	110
#479 	pokemon 	Motisma 	Rotom 	ELECTRIQUE
SPECTRE		50 	95 	77 	77 	91
#480 	pokemon 	Crehelf 	Uxie 	PSY
	75 	75 	130 	130 	95
#481 	pokemon 	Crefollet 	Mesprit 	PSY
	105 	105 	105 	105 	80
#482 	pokemon 	Crefadet 	Azelf 	PSY
	125 	125 	70 	70 	115
#483 	pokemon 	Dialga 	Dialga 	ACIER
DRAGON		120 	150 	120 	100 	90
#484 	pokemon 	Palkia 	Palkia 	EAU
DRAGON		120 	150 	100 	100 	100
#485 	pokemon 	Heatran 	Heatran 	FEU
ACIER		90 	130 	106 	106 	77
#486 	pokemon 	Regigigas 	Regigigas 	NORMAL
	160 	80 	110 	110 	100
#487 	pokemon 	Giratina 	Giratina 	SPECTRE
DRAGON		100 	100 	120 	120 	90
#488 	pokemon 	Cresselia 	Cresselia 	PSY
	70 	75 	120 	130 	85
#489 	pokemon 	Phione 	Phione 	EAU
	80 	80 	80 	80 	80
#490 	pokemon 	Manaphy 	Manaphy 	EAU
	100 	100 	100 	100 	100
#491 	pokemon 	Darkrai 	Darkrai 	TENEBRE
	90 	135 	90 	90 	125
#492 	pokemon 	Shaymin 	Shaymin 	PLANTE
	100 	100 	100 	100 	100
#493 	pokemon 	Arceus 	Arceus 	NORMAL
	120 	120 	120 	120 	120
#494 	pokemon 	Victini 	Victini 	PSY
FEU		100 	100 	100 	100 	100
#495 	pokemon 	Vipelierre 	Snivy 	PLANTE
	45 	45 	55 	55 	63
#496 	pokemon 	Lianaja 	Servine 	PLANTE
	60 	60 	75 	75 	83
#497 	pokemon 	Majaspic 	Serperior 	PLANTE
	75 	75 	95 	95 	113
#498 	pokemon 	Gruikui 	Tepig 	FEU
	63 	45 	45 	45 	45
#499 	pokemon 	Grotichon 	Pignite 	FEU
COMBAT		93 	70 	55 	55 	55
#500 	pokemon 	Roitiflam 	Emboar 	FEU
COMBAT		123 	100 	65 	65 	65
#501 	pokemon 	Moustillon 	Oshawott 	EAU
	55 	63 	45 	45 	45
#502 	pokemon 	Mateloutre 	Dewott 	EAU
	75 	83 	60 	60 	60
#503 	pokemon 	Clamiral 	Samurott 	EAU
	100 	108 	85 	70 	70
#504 	pokemon 	Ratentif 	Patrat 	NORMAL
	55 	35 	39 	39 	42
#505 	pokemon 	Miradar 	Watchog 	NORMAL
	85 	60 	69 	69 	77
#506 	pokemon 	Ponchiot 	Lillipup 	NORMAL
	60 	25 	45 	45 	55
#507 	pokemon 	Ponchien 	Herdier 	NORMAL
	80 	35 	65 	65 	60
#508 	pokemon 	Mastouffe 	Stoutland 	NORMAL
	100 	45 	90 	90 	80
#509 	pokemon 	Chacripan 	Purrloin 	TENEBRE
	50 	50 	37 	37 	66
#510 	pokemon 	Leopardus 	Liepard 	TENEBRE
	88 	88 	50 	50 	106
#511 	pokemon 	Feuillajou 	Pansage 	PLANTE
	53 	53 	48 	48 	64
#512 	pokemon 	Feuiloutan 	Simisage 	PLANTE
	98 	98 	63 	63 	101
#513 	pokemon 	Flamajou 	Pansear 	FEU
	53 	53 	48 	48 	64
#514 	pokemon 	Flamoutan 	Simisear 	FEU
	98 	98 	63 	63 	101
#515 	pokemon 	Flotajou 	Panpour 	EAU
	53 	53 	48 	48 	64
#516 	pokemon 	Flotoutan 	Simipour 	EAU
	98 	98 	63 	63 	101
#517 	pokemon 	Munna 	Munna 	PSY
	25 	67 	45 	55 	24
#518 	pokemon 	Mushana 	Musharna 	PSY
	55 	107 	85 	95 	29
#519 	pokemon 	Poichigeon 	Pidove 	NORMAL
VOL		55 	36 	50 	30 	43
#520 	pokemon 	Colombeau 	Tranquill 	NORMAL
VOL		77 	50 	62 	42 	65
#521 	pokemon 	Deflaisan 	Unfezant 	NORMAL
VOL		105 	65 	80 	55 	93
#522 	pokemon 	Zebibron 	Blitzle 	ELECTRIQUE
	60 	50 	32 	32 	76
#523 	pokemon 	Zeblitz 	Zebstrika 	ELECTRIQUE
	100 	80 	63 	63 	116
#524 	pokemon 	Nodulithe 	Roggenrola 	ROCHE
	75 	25 	85 	25 	15
#525 	pokemon 	Geolithe 	Boldore 	ROCHE
	105 	50 	105 	40 	20
#526 	pokemon 	Gigalithe 	Gigalith 	ROCHE
	135 	60 	130 	70 	25
#527 	pokemon 	Chovsourir 	Woobat 	PSY
VOL		45 	55 	43 	43 	72
#528 	pokemon 	Rhinolove 	Swoobat 	PSY
VOL		57 	77 	55 	55 	114
#529 	pokemon 	Rototaupe 	Drilbur 	SOL
	85 	30 	40 	45 	68
#530 	pokemon 	Minotaupe 	Excadrill 	SOL
ACIER		135 	50 	60 	65 	88
#531 	pokemon 	Nanmeouie 	Audino 	NORMAL
	60 	60 	86 	86 	50
#532 	pokemon 	Charpenti 	Timburr 	COMBAT
	80 	25 	55 	35 	35
#533 	pokemon 	Ouvrifier 	Gurdurr 	COMBAT
	105 	40 	85 	50 	40
#534 	pokemon 	Betochef 	Conkeldurr 	COMBAT
	140 	55 	95 	65 	45
#535 	pokemon 	Tritonde 	Tympole 	EAU
	50 	50 	40 	40 	64
#536 	pokemon 	Batracne 	Palpitoad 	EAU
SOL		65 	65 	55 	55 	69
#537 	pokemon 	Crapustule 	Seismitoad 	EAU
SOL		85 	85 	75 	75 	74
#538 	pokemon 	Judokrak 	Throh 	COMBAT
	100 	30 	85 	85 	45
#539 	pokemon 	Karaclee 	Sawk 	COMBAT
	125 	30 	75 	75 	85
#540 	pokemon 	Larveyette 	Sewaddle 	INSECTE
PLANTE		53 	40 	70 	60 	42
#541 	pokemon 	Couverdure 	Swadloon 	INSECTE
PLANTE		63 	50 	90 	80 	42
#542 	pokemon 	Manternel 	Leavanny 	INSECTE
PLANTE		103 	70 	80 	70 	92
#543 	pokemon 	Venipatte 	Venipede 	INSECTE
POISON		45 	30 	59 	39 	57
#544 	pokemon 	Scobolide 	Whirlipede 	INSECTE
POISON		55 	40 	99 	79 	47
#545 	pokemon 	Brutapode 	Scolipede 	INSECTE
POISON		90 	55 	89 	69 	112
#546 	pokemon 	Doudouvet 	Cottonee 	PLANTE
	27 	37 	60 	50 	66
#547 	pokemon 	Farfaduvet 	Whimsicott 	PLANTE
	67 	77 	85 	75 	116
#548 	pokemon 	Chlorobule 	Petilil 	PLANTE
	35 	70 	50 	50 	30
#549 	pokemon 	Fragilady 	Lilligant 	PLANTE
	60 	110 	75 	75 	90
#550 	pokemon 	Bargantua 	Basculin 	EAU
	92 	80 	65 	55 	98
#551 	pokemon 	Mascaiman 	Sandile 	SOL
TENEBRE		72 	35 	35 	35 	65
#552 	pokemon 	Escroco 	Krokorok 	SOL
TENEBRE		82 	45 	45 	45 	74
#553 	pokemon 	Crocorible 	Krookodile 	SOL
TENEBRE		117 	65 	70 	70 	92
#554 	pokemon 	Darumarond 	Darumaka 	FEU
	90 	15 	45 	45 	50
#555 	pokemon 	Darumacho 	Darmanitan 	FEU
	140 	30 	55 	55 	95
#556 	pokemon 	Maracachi 	Maractus 	PLANTE
	86 	106 	67 	67 	60
#557 	pokemon 	Crabicoque 	Dwebble 	INSECTE
ROCHE		65 	35 	85 	35 	55
#558 	pokemon 	Crabaraque 	Crustle 	INSECTE
ROCHE		95 	65 	125 	75 	45
#559 	pokemon 	Baggiguane 	Scraggy 	TENEBRE
COMBAT		75 	35 	70 	70 	48
#560 	pokemon 	Baggaid 	Scrafty 	TENEBRE
COMBAT		90 	45 	115 	115 	58
#561 	pokemon 	Cryptero 	Sigilyph 	PSY
VOL		58 	103 	80 	80 	97
#562 	pokemon 	Tutafeh 	Yamask 	SPECTRE
	30 	55 	85 	65 	30
#563 	pokemon 	Tutankafer 	Cofagrigus 	SPECTRE
	50 	95 	145 	105 	30
#564 	pokemon 	Carapagos 	Tirtouga 	EAU
ROCHE		78 	53 	103 	45 	22
#565 	pokemon 	Megapagos 	Carracosta 	EAU
ROCHE		108 	83 	133 	65 	32
#566 	pokemon 	Arkeapti 	Archen 	ROCHE
VOL		112 	74 	45 	45 	70
#567 	pokemon 	Aeropteryx 	Archeops 	ROCHE
VOL		140 	112 	65 	65 	110
#568 	pokemon 	Miamiasme 	Trubbish 	POISON
	50 	40 	62 	62 	65
#569 	pokemon 	Miasmax 	Garbodor 	POISON
	95 	60 	82 	82 	75
#570 	pokemon 	Zorua 	Zorua 	TENEBRE
	65 	80 	40 	40 	65
#571 	pokemon 	Zoroark 	Zoroark 	TENEBRE
	105 	120 	60 	60 	105
#572 	pokemon 	Chinchidou 	Minccino 	NORMAL
	50 	40 	40 	40 	75
#573 	pokemon 	Pashmilla 	Cinccino 	NORMAL
	95 	65 	60 	60 	115
#574 	pokemon 	Scrutella 	Gothita 	PSY
	30 	55 	50 	65 	45
#575 	pokemon 	Mesmerella 	Gothorita 	PSY
	45 	75 	70 	85 	55
#576 	pokemon 	Siderella 	Gothitelle 	PSY
	55 	95 	95 	110 	65
#577 	pokemon 	Nucleos 	Solosis 	PSY
	30 	105 	40 	50 	20
#578 	pokemon 	Meios 	Duosion 	PSY
	40 	125 	50 	60 	30
#579 	pokemon 	Symbios 	Reuniclus 	PSY
	65 	125 	75 	85 	30
#580 	pokemon 	Couaneton 	Ducklett 	EAU
VOL		44 	44 	50 	50 	55
#581 	pokemon 	Lakmecygne 	Swanna 	EAU
VOL		87 	87 	63 	63 	98
#582 	pokemon 	Sorbebe 	Vanillite 	GLACE
	50 	65 	50 	60 	44
#583 	pokemon 	Sorboul 	Vanillish 	GLACE
	65 	80 	65 	75 	59
#584 	pokemon 	Sorbouboul 	Vanilluxe 	GLACE
	95 	110 	85 	95 	79
#585 	pokemon 	Vivaldaim 	Deerling 	NORMAL
PLANTE		60 	40 	50 	50 	75
#586 	pokemon 	Haydaim 	Sawsbuck 	NORMAL
PLANTE		100 	60 	70 	70 	95
#587 	pokemon 	Emolga 	Emolga 	ELECTRIQUE
VOL		75 	75 	60 	60 	103
#588 	pokemon 	Carabing 	Karrablast 	INSECTE
	75 	40 	45 	45 	60
#589 	pokemon 	Lancargot 	Escavalier 	INSECTE
ACIER		135 	60 	105 	105 	20
#590 	pokemon 	Trompignon 	Foongus 	PLANTE
POISON		55 	55 	45 	55 	15
#591 	pokemon 	Gaulet 	Amoonguss 	PLANTE
POISON		85 	85 	70 	80 	30
#592 	pokemon 	Viskuse 	Frillish 	EAU
SPECTRE		40 	65 	50 	85 	40
#593 	pokemon 	Moyade 	Jellicent 	EAU
SPECTRE		60 	85 	70 	105 	60
#594 	pokemon 	Mamanbo 	Alomomola 	EAU
	75 	40 	80 	45 	65
#595 	pokemon 	Statitik 	Joltik 	INSECTE
ELECTRIQUE		47 	57 	50 	50 	65
#596 	pokemon 	Mygavolt 	Galvantula 	INSECTE
ELECTRIQUE		77 	97 	60 	60 	108
#597 	pokemon 	Grindur 	Ferroseed 	PLANTE
ACIER		50 	24 	91 	86 	10
#598 	pokemon 	Noacier 	Ferrothorn 	PLANTE
ACIER		94 	54 	131 	116 	20
#599 	pokemon 	Tic 	Klink 	ACIER
	55 	45 	70 	60 	30
#600 	pokemon 	Clic 	Klang 	ACIER
	80 	70 	95 	85 	50
#601 	pokemon 	Cliticlic 	Klinklang 	ACIER
	100 	70 	115 	85 	90
#602 	pokemon 	Anchwatt 	Tynamo 	ELECTRIQUE
	55 	45 	40 	40 	60
#603 	pokemon 	Lamperoie 	Eelektrik 	ELECTRIQUE
	85 	75 	70 	70 	40
#604 	pokemon 	Ohmassacre 	Eelektross 	ELECTRIQUE
	115 	105 	80 	80 	50
#605 	pokemon 	Lewsor 	Elgyem 	PSY
	55 	85 	55 	55 	30
#606 	pokemon 	Neitram 	Beheeyem 	PSY
	75 	125 	75 	95 	40
#607 	pokemon 	Funecire 	Litwick 	SPECTRE
FEU		30 	65 	55 	55 	20
#608 	pokemon 	Melancolux 	Lampent 	SPECTRE
FEU		40 	95 	60 	60 	55
#609 	pokemon 	Lugulabre 	Chandelure 	SPECTRE
FEU		55 	145 	90 	90 	80
#610 	pokemon 	Coupenotte 	Axew 	DRAGON
	87 	30 	60 	40 	57
#611 	pokemon 	Incisache 	Fraxure 	DRAGON
DRAGON		117 	40 	70 	50 	67
#612 	pokemon 	Tranchodon 	Haxorus 	DRAGON
	147 	60 	90 	70 	97
#613 	pokemon 	Polarhume 	Cubchoo 	GLACE
	70 	60 	40 	40 	40
#614 	pokemon 	Polagriffe 	Beartic 	GLACE
	110 	70 	80 	80 	50
#615 	pokemon 	Hexagel 	Cryogonal 	GLACE
	50 	95 	30 	135 	105
#616 	pokemon 	Escargaume 	Shelmet 	INSECTE
	40 	40 	85 	65 	25
#617 	pokemon 	Limaspeed 	Accelgor 	INSECTE
	70 	100 	40 	60 	145
#618 	pokemon 	Limonde 	Stunfisk 	ELECTRIQUE
SOL		66 	81 	84 	99 	32
#619 	pokemon 	Kungfouine 	Mienfoo 	COMBAT
	85 	55 	50 	50 	65
#620 	pokemon 	Shaofouine 	Mienshao 	COMBAT
	125 	95 	60 	60 	105
#621 	pokemon 	Drakkarmin 	Druddigon 	DRAGON
	120 	60 	90 	90 	48
#622 	pokemon 	Gringolem 	Golett 	SOL
SPECTRE		74 	35 	50 	50 	35
#623 	pokemon 	Golemastoc 	Golurk 	SOL
SPECTRE		124 	55 	80 	80 	55
#624 	pokemon 	Scalpion 	Pawniard 	ACIER
TENEBRE		85 	40 	70 	40 	60
#625 	pokemon 	Scalproie 	Bisharp 	ACIER
TENEBRE		125 	60 	100 	70 	70
#626 	pokemon 	Frison 	Bouffalant 	NORMAL
	110 	40 	95 	95 	55
#627 	pokemon 	Furaiglon 	Rufflet 	NORMAL
VOL		83 	37 	50 	50 	60
#628 	pokemon 	Gueriaigle 	Braviary 	NORMAL
VOL		123 	57 	75 	75 	80
#629 	pokemon 	Vostourno 	Vullaby 	TENEBRE
VOL		55 	45 	75 	65 	60
#630 	pokemon 	Vaututrice 	Mandibuzz 	TENEBRE
VOL		65 	55 	105 	95 	80
#631 	pokemon 	Aflamanoir 	Heatmor 	FEU
	97 	105 	66 	66 	65
#632 	pokemon 	Fermite 	Durant 	INSECTE
ACIER		109 	48 	112 	48 	109
#633 	pokemon 	Solochi 	Deino 	TENEBRE
DRAGON		65 	45 	50 	50 	38
#634 	pokemon 	Diamat 	Zweilous 	TENEBRE
DRAGON		85 	65 	70 	70 	58
#635 	pokemon 	Trioxhydre 	Hydreigon 	TENEBRE
DRAGON		105 	125 	90 	90 	98
#636 	pokemon 	Pyronille 	Larvesta 	INSECTE
FEU		85 	50 	55 	55 	60
#637 	pokemon 	Pyrax 	Volcarona 	INSECTE
FEU		60 	135 	65 	105 	100
#638 	pokemon 	Cobaltium 	Cobalion 	ACIER
COMBAT		90 	90 	129 	72 	108
#639 	pokemon 	Terrakium 	Terrakion 	ROCHE
COMBAT		129 	72 	90 	90 	108
#640 	pokemon 	Viridium 	Virizion 	PLANTE
COMBAT		90 	90 	72 	129 	108
#641 	pokemon 	Boreas 	Tornadus 	VOL
	115 	125 	70 	80 	111
#642 	pokemon 	Fulguris 	Thundurus 	ELECTRIQUE
VOL		115 	125 	70 	80 	111
#643 	pokemon 	Reshiram 	Reshiram 	DRAGON
FEU		120 	150 	100 	120 	90
#644 	pokemon 	Zekrom 	Zekrom 	DRAGON
ELECTRIQUE		150 	120 	120 	100 	90
#645 	pokemon 	Demeteros 	Landorus 	SOL
VOL		125 	115 	90 	80 	101
#646 	pokemon 	Kyurem 	Kyurem 	DRAGON
GLACE		130 	130 	90 	90 	95
#647 	pokemon 	Keldeo 	Keldeo 	EAU
COMBAT		72 	129 	90 	90 	108
#648 	pokemon 	Meloetta 	Meloetta 	NORMAL
PSY		77 	128 	77 	128 	90
#649 	pokemon 	Genesect 	Genesect 	INSECTE
ACIER		120 	120 	95 	95 	99
#650 	pokemon 	Marisson 	Chespin 	PLANTE
	61 	48 	65 	45 	38
#651 	pokemon 	Boguerisse 	Quilladin 	PLANTE
	78 	56 	95 	58 	57
#652 	pokemon 	Blindepique 	Chesnaught 	PLANTE
COMBAT		45 	62 	40 	60 	60
#653 	pokemon 	Feunnec 	Fennekin 	FEU
	45 	62 	40 	60 	60
#654 	pokemon 	Roussil 	Braixen 	FEU
	59 	90 	58 	70 	73
#655 	pokemon 	Goupelin 	Delphox 	FEU
PSY		69 	114 	72 	100 	104
#656 	pokemon 	Grenousse 	Froakie 	EAU
	56 	62 	40 	44 	----
#657 	pokemon 	Croaporal 	Frogadier 	EAU
	63 	83 	52 	56 	97
#658 	pokemon 	Amphinobi 	Greninja 	EAU
TENEBRE		95 	103 	67 	71 	122
#659 	pokemon 	Sapereau 	Bunnelby 	NORMAL
	36 	32 	38 	36 	57
#660 	pokemon 	Excavarenne 	Diggersby 	NORMAL
SOL		56 	50 	77 	77 	78
#661 	pokemon 	Passerouge 	Fletchling 	NORMAL
VOL		50 	40 	43 	38 	62
#662 	pokemon 	Braisillon 	Fletchinder 	FEU
VOL		73 	56 	55 	52 	84
#663 	pokemon 	Flambusard 	Talonflame 	FEU
VOL		81 	74 	71 	69 	126
#664 	pokemon 	Lepidonille 	Scatterbug 	INSECTE
	35 	27 	40 	25 	35
#665 	pokemon 	Peregrain 	Spewpa 	INSECTE
	22 	30 	27 	29 	29
#666 	pokemon 	Prismillon 	Vivillon 	INSECTE
VOL		52 	90 	50 	50 	89
#667 	pokemon 	Helionceau 	Litleo 	FEU
NORMAL		50 	73 	58 	54 	72
#668 	pokemon 	Nemelios 	Pyroar 	FEU
NORMAL		68 	109 	72 	66 	106
#669 	pokemon 	Flabebe 	Flabebe 	FEE
	38 	61 	39 	79 	42
#670 	pokemon 	Floette 	Floette 	FEE
	45 	75 	47 	98 	52
#671 	pokemon 	Florges 	Florges 	FEE
	65 	112 	68 	154 	----
#672 	pokemon 	Cabriolaine 	Skiddo 	PLANTE
	65 	62 	48 	57 	52
#673 	pokemon 	Chevroum 	Gogoat 	PLANTE
	100 	97 	62 	81 	68
#674 	pokemon 	Pandespiegle 	Pancham 	COMBAT
	82 	46 	62 	48 	43
#675 	pokemon 	Pandarbare 	Pangoro 	COMBAT
TENEBRE		124 	69 	78 	71 	58
#676 	pokemon 	Couafarel 	Furfrou 	NORMAL
	80 	65 	60 	90 	102
#677 	pokemon 	Psystigri 	Espurr 	PSY
	48 	63 	54 	60 	68
#678 	pokemon 	Mistigrix 	Meowstic 	PSY
	81 	74 	104 	48 	76
#679 	pokemon 	Monorpale 	Honedge 	ACIER
SPECTRE		80 	35 	100 	37 	28
#680 	pokemon 	Dimocles 	Doublade 	ACIER
SPECTRE		110 	45 	150 	49 	35
#681 	pokemon 	Exagide 	Aegislash 	ACIER
SPECTRE		50 	50 	150 	150 	60
#682 	pokemon 	Fluvetin 	Spritzee 	FEE
	52 	63 	60 	65 	23
#683 	pokemon 	Cocotine 	Aromatisse 	FEE
	72 	99 	72 	89 	29
#684 	pokemon 	Sucroquin 	Swirlix 	FEE
	48 	59 	66 	57 	49
#685 	pokemon 	Cupcanaille 	Slurpuff 	FEE
	80 	85 	86 	75 	72
#686 	pokemon 	Sepiatop 	Inkay 	TENEBRE
PSY		54 	37 	53 	46 	45
#687 	pokemon 	Sepiatroce 	Malamar 	TENEBRE
PSY		92 	68 	88 	75 	73
#688 	pokemon 	Opermine 	Binacle 	ROCHE
EAU		52 	39 	67 	56 	50
#689 	pokemon 	Golgopathe 	Barbaracle 	ROCHE
EAU		105 	54 	115 	86 	68
#690 	pokemon 	Venalgue 	Skrelp 	POISON
EAU		60 	60 	60 	60 	30
#691 	pokemon 	Kravarech 	Dragalge 	POISON
DRAGON		75 	97 	90 	123 	44
#692 	pokemon 	Flingouste 	Clauncher 	EAU
	53 	58 	62 	63 	44
#693 	pokemon 	Gamblast 	Clawitzer 	EAU
	73 	120 	88 	89 	59
#694 	pokemon 	Galvaran 	Helioptile 	ELECTRIQUE
NORMAL		38 	61 	33 	43 	70
#695 	pokemon 	Iguolta 	Heliolisk 	ELECTRIQUE
NORMAL		55 	109 	52 	94 	109
#696 	pokemon 	Ptyranidur 	Tyrunt 	ROCHE
DRAGON		89 	45 	77 	45 	48
#697 	pokemon 	Rexillius 	Tyrantrum 	ROCHE
DRAGON		121 	69 	119 	59 	71
#698 	pokemon 	Amagara 	Amaura 	ROCHE
GLACE		59 	67 	50 	63 	46
#699 	pokemon 	Dragmara 	Aurorus 	ROCHE
GLACE		77 	99 	72 	92 	58
#700 	pokemon 	Nymphali 	Sylveon 	FEE
	65 	110 	65 	130 	60
#701 	pokemon 	Brutalibre 	Hawlucha 	COMBAT
VOL		92 	74 	75 	63 	118
#702 	pokemon 	Dedenne 	Dedenne 	ELECTRIQUE
FEE		58 	81 	57 	67 	101
#703 	pokemon 	Strassie 	Carbink 	ROCHE
FEE		50 	50 	150 	150 	50
#704 	pokemon 	Mucuscule 	Goomy 	DRAGON
	50 	55 	35 	75 	40
#705 	pokemon 	Colimucus 	Sliggoo 	DRAGON
	75 	83 	53 	113 	60
#706 	pokemon 	Muplodocus 	Goodra 	DRAGON
	100 	110 	70 	150 	80
#707 	pokemon 	Trousselin 	Klefki 	ACIER
FEE		80 	80 	91 	87 	75
#708 	pokemon 	Brocelome 	Phantump 	SPECTRE
PLANTE		70 	50 	48 	60 	38
#709 	pokemon 	Desseliande 	Trevenant 	SPECTRE
PLANTE		110 	65 	76 	82 	56
#710 	pokemon 	Pitrouille 	Pumpkaboo 	SPECTRE
PLANTE		---- 	---- 	---- 	---- 	----
#711 	pokemon 	Banshitrouye 	Gourgeist 	SPECTRE
PLANTE		---- 	---- 	---- 	---- 	----
#712 	pokemon 	Grelacon 	Bergmite 	GLACE
	69 	32 	85 	35 	28
#713 	pokemon 	Seracrawl 	Avalugg 	GLACE
	117 	44 	184 	46 	28
#714 	pokemon 	Sonistrelle 	Noibat 	VOL
DRAGON		30 	45 	35 	40 	55
#715 	pokemon 	Bruyverne 	Onvern 	VOL
DRAGON		70 	97 	80 	80 	123
#716 	pokemon 	Xerneas 	Xerneas 	FEE
	131 	131 	95 	98 	99
#717 	pokemon 	Yveltal 	Yveltal 	TENEBRE
VOL		131 	131 	95 	98 	99
#718 	pokemon 	Zygarde 	Zygarde 	DRAGON
SOL		100 	81 	121 	95 	95"""

caracs = """001 	001 	Bulbizarre 	45 	49 	49 	65 	65 	45 	318 	53
002 	002 	Herbizarre 	62 	62 	63 	80 	80 	60 	405 	67,5
003 	003 	Florizarre 	80 	82 	83 	100 	100 	80 	525 	87,5
003 	003 	Mega-Florizarre 	80 	100 	123 	122 	120 	80 	625 	104,17
004 	004 	Salameche 	39 	52 	43 	60 	40 	65 	309 	51,5
005 	005 	Reptincel 	58 	64 	58 	80 	65 	80 	405 	67,5
006 	006 	Dracaufeu 	78 	84 	78 	109 	85 	100 	534 	89
006 	006 	Mega-Dracaufeu X 	78 	130 	111 	130 	85 	100 	634 	105,67
006 	006 	Mega-Dracaufeu Y 	78 	104 	78 	159 	115 	100 	634 	105,67
007 	007 	Carapuce 	44 	48 	65 	50 	64 	43 	314 	52,33
008 	008 	Carabaffe 	59 	63 	80 	65 	80 	58 	405 	67,5
009 	009 	Tortank 	79 	83 	100 	85 	105 	78 	530 	88,33
009 	009 	Mega-Tortank 	79 	103 	120 	135 	115 	78 	630 	105
010 	010 	Chenipan 	45 	30 	35 	20 	20 	45 	195 	32,5
011 	011 	Chrysacier 	50 	20 	55 	25 	25 	30 	205 	34,17
012 	012 	Papilusion 	60 	45 	50 	80 	80 	70 	385 	64,17
013 	013 	Aspicot 	40 	35 	30 	20 	20 	50 	195 	32,5
014 	014 	Coconfort 	45 	25 	50 	25 	25 	35 	205 	34,17
015 	015 	Dardargnan 	65 	80 	40 	45 	80 	75 	385 	64,18
016 	016 	Roucool 	40 	45 	40 	35 	35 	56 	251 	41,83
017 	017 	Roucoups 	63 	60 	55 	50 	50 	71 	349 	58,17
018 	018 	Roucarnage 	83 	80 	75 	70 	70 	91 	469 	78,17
019 	019 	Rattata 	30 	56 	35 	25 	35 	72 	253 	42,17
020 	020 	Rattatac 	55 	81 	60 	50 	70 	97 	413 	68,83
021 	021 	Piafabec 	40 	60 	30 	31 	31 	70 	262 	43,67
022 	022 	Rapasdepic 	65 	90 	65 	61 	61 	100 	442 	73,67
023 	023 	Abo 	35 	60 	44 	40 	54 	55 	288 	48
024 	024 	Arbok 	60 	85 	69 	65 	79 	80 	438 	73
025 	025 	Pikachu 	35 	55 	30 	50 	40 	90 	300 	50
026 	026 	Raichu 	60 	90 	55 	90 	80 	100 	475 	79,17
027 	027 	Sabelette 	50 	75 	85 	20 	30 	40 	300 	50
028 	028 	Sablaireau 	75 	100 	110 	45 	55 	65 	450 	75
029 	029 	Nidoran F 	55 	47 	52 	40 	40 	41 	275 	45,83
030 	030 	Nidorina 	70 	62 	67 	55 	55 	56 	365 	60,83
031 	031 	Nidoqueen 	90 	82 	87 	75 	85 	76 	495 	82,5
032 	032 	Nidoran M 	46 	57 	40 	40 	40 	50 	273 	45,5
033 	033 	Nidorino 	61 	72 	57 	55 	55 	65 	365 	60,83
034 	034 	Nidoking 	81 	92 	77 	85 	75 	85 	495 	82,5
035 	035 	Melofee 	70 	45 	48 	60 	65 	35 	323 	53,83
036 	036 	Melodelfe 	95 	70 	73 	85 	90 	60 	473 	78,83
037 	037 	Goupix 	38 	41 	40 	50 	65 	65 	299 	49,83
038 	038 	Feunard 	73 	76 	75 	81 	100 	100 	505 	84,17
039 	039 	Rondoudou 	115 	45 	20 	45 	25 	20 	270 	45
040 	040 	Grodoudou 	140 	70 	45 	75 	50 	45 	425 	70,83
041 	041 	Nosferapti 	40 	45 	35 	30 	40 	55 	245 	40,83
042 	042 	Nosferalto 	75 	80 	70 	65 	75 	90 	455 	75,83
043 	043 	Mystherbe 	45 	50 	55 	75 	65 	30 	320 	53,33
044 	044 	Ortide 	60 	65 	70 	85 	75 	40 	395 	65,83
045 	045 	Rafflesia 	75 	80 	85 	100 	90 	50 	480 	80
046 	046 	Paras 	35 	70 	55 	45 	55 	25 	285 	47,5
047 	047 	Parasect 	60 	95 	80 	60 	80 	30 	405 	67,5
048 	048 	Mimitoss 	60 	55 	50 	40 	55 	45 	305 	50,83
049 	049 	Aeromite 	70 	65 	60 	90 	75 	90 	450 	75
050 	050 	Taupiqueur 	10 	55 	25 	35 	45 	95 	265 	44,17
051 	051 	Triopikeur 	35 	80 	50 	50 	70 	120 	405 	67,5
052 	052 	Miaouss 	40 	45 	35 	40 	40 	90 	290 	48,33
053 	053 	Persian 	65 	70 	60 	65 	65 	115 	440 	73,33
054 	054 	Psykokwak 	50 	52 	48 	65 	50 	55 	320 	53,33
055 	055 	Akwakwak 	80 	82 	78 	95 	80 	85 	500 	83,33
056 	056 	Ferosinge 	40 	80 	35 	35 	45 	70 	305 	50,83
057 	057 	Colossinge 	65 	105 	60 	60 	70 	95 	455 	75,83
058 	058 	Caninos 	55 	70 	45 	70 	50 	60 	350 	58,33
059 	059 	Arcanin 	90 	110 	80 	100 	80 	95 	555 	92,5
060 	060 	Ptitard 	40 	50 	40 	40 	40 	90 	300 	50
061 	061 	Tetarte 	65 	65 	65 	50 	50 	90 	385 	64,17
062 	062 	Tartard 	90 	85 	95 	70 	90 	70 	500 	83,33
063 	063 	Abra 	25 	20 	15 	105 	55 	90 	310 	51,67
064 	064 	Kadabra 	40 	35 	30 	120 	70 	105 	400 	66,67
065 	065 	Alakazam 	55 	50 	45 	135 	85 	120 	490 	81,67
065 	065 	Mega-Alakazam 	55 	50 	65 	175 	95 	150 	590 	98,33
066 	066 	Machoc 	70 	80 	50 	35 	35 	35 	305 	50,83
067 	067 	Machopeur 	80 	100 	70 	50 	60 	45 	405 	67,5
068 	068 	Mackogneur 	90 	130 	80 	65 	85 	55 	505 	84,17
069 	069 	Chetiflor 	50 	75 	35 	70 	30 	40 	300 	50
070 	070 	Boustiflor 	65 	90 	50 	85 	45 	55 	390 	65
071 	071 	Empiflor 	80 	105 	65 	100 	60 	70 	480 	80
072 	072 	Tentacool 	40 	40 	35 	50 	100 	70 	335 	55,83
073 	073 	Tentacruel 	80 	70 	65 	80 	120 	100 	515 	85,83
074 	074 	Racaillou 	40 	80 	100 	30 	30 	20 	300 	50
075 	075 	Gravalanch 	55 	95 	115 	45 	45 	35 	390 	65
076 	076 	Grolem 	80 	110 	130 	55 	65 	45 	485 	80,83
077 	077 	Ponyta 	50 	85 	55 	65 	65 	90 	410 	68,33
078 	078 	Galopa 	65 	100 	70 	80 	80 	105 	500 	83,33
079 	079 	Ramoloss 	90 	65 	65 	40 	40 	15 	315 	52,5
080 	080 	Flagadoss 	95 	75 	110 	100 	80 	30 	490 	81,67
081 	081 	Magneti 	25 	35 	70 	95 	55 	45 	325 	54,17
082 	082 	Magneton 	50 	60 	95 	120 	70 	70 	465 	77,5
083 	083 	Canarticho 	52 	65 	55 	58 	62 	60 	352 	58,67
084 	084 	Doduo 	35 	85 	45 	35 	35 	75 	310 	51,67
085 	085 	Dodrio 	60 	110 	70 	60 	60 	100 	460 	76,67
086 	086 	Otaria 	65 	45 	55 	45 	70 	45 	325 	54,17
087 	087 	Lamantine 	90 	70 	80 	70 	95 	70 	475 	79,17
088 	088 	Tadmorv 	80 	80 	50 	40 	50 	25 	325 	54,17
089 	089 	Grotadmorv 	105 	105 	75 	65 	100 	50 	500 	83,33
090 	090 	Kokiyas 	30 	65 	100 	45 	25 	40 	305 	50,83
091 	091 	Crustabri 	50 	95 	180 	85 	45 	70 	525 	87,5
092 	092 	Fantominus 	30 	35 	30 	100 	35 	80 	310 	51,67
093 	093 	Spectrum 	45 	50 	45 	115 	55 	95 	405 	67,5
094 	094 	Ectoplasma 	60 	65 	60 	130 	75 	110 	500 	83,33
094 	094 	Mega-Ectoplasma 	60 	65 	80 	170 	95 	130 	600 	100
095 	095 	Onix 	35 	45 	160 	30 	45 	70 	385 	64,17
096 	096 	Soporifik 	60 	48 	45 	43 	90 	42 	328 	54,67
097 	097 	Hypnomade 	85 	73 	70 	73 	115 	67 	483 	80,5
098 	098 	Krabby 	30 	105 	90 	25 	25 	50 	325 	54,17
099 	099 	Krabboss 	55 	130 	115 	50 	50 	75 	475 	79,17
100 	100 	Voltorbe 	40 	30 	50 	55 	55 	100 	330 	55
101 	101 	Electrode 	60 	50 	70 	80 	80 	140 	480 	80
102 	102 	Noeunoeuf 	60 	40 	80 	60 	45 	40 	325 	54,17
103 	103 	Noadkoko 	95 	95 	85 	125 	65 	55 	520 	86,67
104 	104 	Osselait 	50 	50 	95 	40 	50 	35 	320 	53,33
105 	105 	Ossatueur 	60 	80 	110 	50 	80 	45 	425 	70,83
106 	106 	Kicklee 	50 	120 	53 	35 	110 	87 	455 	75,83
107 	107 	Tygnon 	50 	105 	79 	35 	110 	76 	455 	75,83
108 	108 	Excelangue 	90 	55 	75 	60 	75 	30 	385 	64,17
109 	109 	Smogo 	40 	65 	95 	60 	45 	35 	340 	56,67
110 	110 	Smogogo 	65 	90 	120 	85 	70 	60 	490 	81,67
111 	111 	Rhinocorne 	80 	85 	95 	30 	30 	25 	345 	57,5
112 	112 	Rhinoferos 	105 	130 	120 	45 	45 	40 	485 	80,83
113 	113 	Leveinard 	250 	5 	5 	35 	105 	50 	450 	75
114 	114 	Saquedeneu 	65 	55 	115 	100 	40 	60 	435 	72,5
115 	115 	Kangourex 	105 	95 	80 	40 	80 	90 	490 	81,67
115 	115 	Mega-Kangourex 	105 	125 	100 	60 	100 	100 	590 	98,33
116 	116 	Hypotrempe 	30 	40 	70 	70 	25 	60 	295 	48,17
117 	117 	Hypocean 	55 	65 	95 	95 	45 	85 	440 	73,33
118 	118 	Poissirene 	45 	67 	60 	35 	50 	63 	320 	53,33
119 	119 	Poissoroy 	80 	92 	65 	65 	80 	68 	450 	75
120 	120 	Stari 	30 	45 	55 	70 	55 	85 	340 	56,67
121 	121 	Staross 	60 	75 	85 	100 	85 	115 	520 	86,67
122 	122 	M. Mime 	40 	45 	65 	100 	120 	90 	460 	76,67
123 	123 	Insecateur 	70 	110 	80 	55 	80 	105 	500 	83,33
124 	124 	Lippoutou 	65 	50 	35 	115 	95 	95 	455 	75,83
125 	125 	Elektek 	65 	83 	57 	95 	85 	105 	490 	81,67
126 	126 	Magmar 	65 	95 	57 	100 	85 	93 	495 	82,5
127 	127 	Scarabrute 	65 	125 	100 	55 	70 	85 	500 	83,33
127 	127 	Mega-Scarabrute 	65 	155 	120 	65 	90 	105 	600 	100
128 	128 	Tauros 	75 	100 	95 	40 	70 	110 	490 	81,67
129 	129 	Magicarpe 	20 	10 	55 	15 	20 	80 	200 	33,33
130 	130 	Leviator 	95 	125 	79 	60 	100 	81 	540 	90
130 	130 	Mega-Leviator 	95 	155 	109 	70 	130 	81 	640 	106,67
131 	131 	Lokhlass 	130 	85 	80 	85 	95 	60 	535 	89,17
132 	132 	Metamorph 	48 	48 	48 	48 	48 	48 	288 	48
133 	133 	Evoli 	55 	55 	50 	45 	65 	55 	325 	54,17
134 	134 	Aquali 	130 	65 	60 	110 	95 	65 	525 	87,5
135 	135 	Voltali 	65 	65 	60 	110 	95 	130 	525 	87,5
136 	136 	Pyroli 	65 	130 	60 	95 	110 	65 	525 	87,5
137 	137 	Porygon 	65 	60 	70 	85 	75 	40 	395 	65,83
138 	138 	Amonita 	35 	40 	100 	90 	55 	35 	355 	59,17
139 	139 	Amonistar 	70 	60 	125 	115 	70 	55 	495 	82,5
140 	140 	Kabuto 	30 	80 	90 	55 	45 	55 	355 	59,17
141 	141 	Kabutops 	60 	115 	105 	65 	70 	80 	495 	82,5
142 	142 	Ptera 	80 	105 	65 	60 	75 	130 	515 	85,83
142 	142 	Mega-Ptera 	80 	135 	85 	70 	95 	150 	515 	85,83
143 	143 	Ronflex 	160 	110 	65 	65 	110 	30 	540 	90
144 	144 	Artikodin 	90 	85 	100 	95 	125 	85 	580 	96,67
145 	145 	Electhor 	90 	90 	85 	125 	90 	100 	580 	96,67
146 	146 	Sulfura 	90 	100 	90 	125 	85 	90 	580 	96,67
147 	147 	Minidraco 	41 	64 	45 	50 	50 	50 	300 	50
148 	148 	Draco 	61 	84 	65 	70 	70 	70 	420 	70
149 	149 	Dracolosse 	91 	134 	95 	100 	100 	80 	600 	100
150 	150 	Mewtwo 	106 	110 	90 	154 	90 	130 	680 	113,33
150 	150 	Mega-Mewtwo X 	106 	190 	100 	154 	100 	130 	780 	130
150 	150 	Mega-Mewtwo Y 	106 	150 	70 	194 	120 	140 	780 	130
151 	151 	Mew 	100 	100 	100 	100 	100 	100 	600 	100
152 	152 	Germignon 	45 	49 	65 	49 	65 	45 	318 	53
153 	153 	Macronium 	60 	62 	80 	63 	80 	60 	405 	67,5
154 	154 	Meganium 	80 	82 	100 	83 	100 	80 	525 	87,5
155 	155 	Hericendre 	39 	52 	43 	60 	50 	65 	309 	51,5
156 	156 	Feurisson 	58 	64 	58 	80 	65 	80 	405 	67,5
157 	157 	Typhlosion 	78 	84 	78 	109 	85 	100 	534 	89
158 	158 	Kaiminus 	50 	65 	64 	44 	48 	43 	314 	52,33
159 	159 	Crocrodil 	65 	80 	80 	59 	63 	58 	405 	67,5
160 	160 	Aligatueur 	85 	105 	100 	79 	83 	78 	530 	88,33
161 	161 	Fouinette 	35 	46 	34 	35 	45 	20 	215 	35,83
162 	162 	Fouinar 	85 	76 	64 	45 	55 	90 	415 	69,17
163 	163 	Hoot-hoot 	60 	30 	30 	36 	56 	50 	262 	43,67
164 	164 	Noarfang 	100 	50 	50 	76 	96 	70 	442 	73,67
165 	165 	Coxy 	40 	20 	30 	40 	80 	55 	265 	44,17
166 	166 	Coxyclaque 	55 	35 	50 	55 	110 	85 	390 	65
167 	167 	Mimigal 	40 	60 	40 	40 	40 	30 	250 	41,67
168 	168 	Migalos 	70 	90 	70 	60 	60 	40 	390 	65
169 	169 	Nostenfer 	85 	90 	80 	70 	80 	130 	535 	89,17
170 	170 	Loupio 	75 	38 	38 	56 	56 	67 	330 	55
171 	171 	Lanturn 	125 	58 	58 	76 	76 	67 	460 	76,67
172 	172 	Pichu 	20 	40 	15 	35 	35 	60 	205 	34,17
173 	173 	Melo 	50 	25 	28 	45 	55 	15 	218 	36,33
174 	174 	Toudoudou 	90 	30 	15 	40 	20 	15 	210 	35
175 	175 	Togepi 	35 	20 	65 	40 	65 	20 	245 	40,83
176 	176 	Togetic 	55 	40 	85 	80 	105 	40 	405 	67,5
177 	177 	Natu 	40 	50 	45 	70 	45 	70 	320 	53,33
178 	178 	Xatu 	65 	75 	70 	95 	70 	95 	470 	78,33
179 	179 	Wattouat 	55 	40 	40 	65 	45 	35 	280 	46,67
180 	180 	Lainergie 	70 	55 	55 	80 	60 	45 	365 	60,83
181 	181 	Pharamp 	90 	75 	75 	115 	90 	55 	500 	83,33
181 	181 	Mega-Pharamp 	90 	95 	105 	165 	110 	45 	610 	101,67
182 	182 	Joliflor 	75 	80 	85 	90 	100 	50 	480 	80
183 	183 	Marill 	70 	20 	50 	20 	50 	40 	250 	41,67
184 	184 	Azumarill 	100 	50 	80 	50 	80 	50 	410 	68,33
185 	185 	Simularbre 	70 	100 	115 	30 	65 	30 	410 	68,33
186 	186 	Tarpaud 	90 	75 	75 	90 	100 	70 	500 	83,33
187 	187 	Granivol 	35 	35 	40 	35 	55 	50 	250 	41,67
188 	188 	Floravol 	55 	45 	50 	45 	65 	80 	340 	56,67
189 	189 	Cotovol 	75 	55 	70 	55 	85 	110 	450 	75
190 	190 	Capumain 	55 	70 	55 	40 	55 	85 	360 	60
191 	191 	Tournegrin 	30 	30 	30 	30 	30 	30 	180 	30
192 	192 	Heliatronc 	75 	75 	55 	105 	85 	30 	425 	70,83
193 	193 	Yanma 	65 	65 	45 	75 	45 	95 	390 	65
194 	194 	Axoloto 	55 	45 	45 	25 	25 	15 	210 	35
195 	195 	Maraiste 	95 	85 	85 	65 	65 	35 	430 	71,67
196 	196 	Mentali 	65 	65 	60 	130 	95 	110 	525 	87,5
197 	197 	Noctali 	95 	65 	110 	60 	130 	65 	525 	87,5
198 	198 	Cornebre 	60 	85 	42 	85 	42 	91 	405 	67,5
199 	199 	Roigada 	95 	75 	80 	100 	110 	30 	490 	81,67
200 	200 	Feuforeve 	60 	60 	60 	85 	85 	85 	435 	72,5
201 	201 	Zarbi 	48 	72 	48 	72 	48 	48 	336 	56
202 	202 	Qulbutoke 	190 	33 	58 	33 	58 	33 	405 	67,5
203 	203 	Girafarig 	70 	80 	65 	90 	65 	85 	455 	75,83
204 	204 	Pomdepik 	50 	65 	90 	35 	35 	15 	290 	48,33
205 	205 	Foretress 	75 	90 	140 	60 	60 	40 	465 	77,5
206 	206 	Insolourdo 	100 	70 	70 	65 	65 	45 	415 	69,17
207 	207 	Scorplane 	65 	75 	105 	35 	65 	85 	430 	71,67
208 	208 	Steelix 	75 	85 	200 	55 	65 	30 	510 	85
209 	209 	Snubbull 	60 	80 	50 	40 	40 	30 	300 	50
210 	210 	Granbull 	90 	120 	75 	60 	60 	45 	450 	75
211 	211 	Qwilfish 	65 	95 	75 	55 	55 	85 	430 	71,67
212 	212 	Cizayox 	70 	130 	100 	55 	80 	65 	500 	83,33
212 	212 	Mega-Cizayox 	70 	150 	140 	65 	100 	75 	600 	100
213 	213 	Caratroc 	20 	10 	230 	10 	230 	5 	505 	84,17
214 	214 	Scarhino 	80 	125 	75 	40 	95 	85 	500 	83,33
214 	214 	Mega-Scarhino 	80 	185 	115 	40 	105 	75 	600 	100
215 	215 	Farfuret 	55 	95 	55 	35 	75 	115 	430 	71,67
216 	216 	Teddiursa 	60 	80 	50 	50 	50 	40 	330 	55
217 	217 	Ursaring 	90 	130 	75 	75 	75 	55 	500 	83,33
218 	218 	Limagma 	40 	40 	40 	70 	40 	20 	250 	41,67
219 	219 	Volcaropod 	50 	50 	120 	80 	80 	30 	410 	68,33
220 	220 	Marcacrin 	50 	50 	40 	30 	30 	50 	250 	41,67
221 	221 	Cochignon 	100 	100 	80 	60 	60 	50 	450 	75
222 	222 	Corayon 	55 	55 	85 	65 	85 	35 	380 	63,33
223 	223 	Remoraid 	35 	65 	35 	65 	35 	65 	300 	50
224 	224 	Octillery 	75 	105 	75 	105 	75 	45 	480 	80
225 	225 	Cadoizo 	45 	55 	45 	65 	45 	75 	330 	55
226 	226 	Demanta 	65 	40 	70 	80 	140 	70 	465 	77,5
227 	227 	Airmure 	65 	80 	140 	40 	70 	70 	465 	77,5
228 	228 	Malosse 	45 	60 	30 	80 	50 	65 	330 	55
229 	229 	Demolosse 	75 	90 	50 	110 	80 	95 	500 	83,33
229 	229 	Mega-Demolosse 	75 	90 	90 	140 	90 	115 	600 	100
230 	230 	Hyporoi 	75 	95 	95 	95 	95 	85 	540 	90
231 	231 	Phanpy 	90 	60 	60 	40 	40 	40 	330 	55
232 	232 	Donphan 	90 	120 	120 	60 	60 	50 	500 	83,33
233 	233 	Porygon2 	85 	80 	90 	105 	95 	60 	515 	85,83
234 	234 	Cerfrousse 	73 	95 	62 	85 	65 	85 	465 	77,5
235 	235 	Queulorior 	55 	20 	35 	20 	45 	75 	250 	41,67
236 	236 	Debugant 	35 	35 	35 	35 	35 	35 	210 	35
237 	237 	Kapoera 	50 	95 	95 	35 	110 	70 	455 	75,83
238 	238 	Lippouti 	45 	30 	15 	85 	65 	65 	305 	50,83
239 	239 	Elekid 	45 	63 	37 	65 	55 	95 	360 	60
240 	240 	Magby 	45 	75 	37 	70 	55 	83 	365 	60,83
241 	241 	Ecremeuh 	95 	80 	105 	40 	70 	100 	490 	81,67
242 	242 	Leuphorie 	255 	10 	10 	75 	135 	55 	540 	90
243 	243 	Raikou 	90 	85 	75 	115 	100 	115 	580 	96,67
244 	244 	Entei 	115 	115 	85 	90 	75 	100 	580 	96,67
245 	245 	Suicune 	100 	75 	115 	90 	115 	85 	580 	96,67
246 	246 	Embrylex 	50 	64 	50 	45 	50 	41 	300 	50
247 	247 	Ymphect 	70 	84 	70 	65 	70 	51 	410 	68,33
248 	248 	Tyranocif 	100 	134 	110 	95 	100 	61 	600 	100
248 	248 	Mega-Tyranocif 	100 	164 	150 	95 	120 	71 	700 	116,67
249 	249 	Lugia 	106 	90 	130 	90 	154 	110 	680 	113,33
250 	250 	Ho-Oh 	106 	130 	90 	110 	154 	90 	680 	113,33
251 	251 	Celebi 	100 	100 	100 	100 	100 	100 	600 	100
252 	252 	Arcko 	40 	45 	35 	65 	55 	70 	310 	51,67
253 	253 	Massko 	50 	65 	45 	85 	65 	95 	405 	67,5
254 	254 	Jungko 	70 	85 	65 	105 	85 	120 	530 	88,33
255 	255 	Poussifeu 	45 	60 	40 	70 	50 	45 	310 	51,67
256 	256 	Galifeu 	60 	85 	60 	85 	60 	55 	405 	67,5
257 	257 	Brasegali 	80 	120 	70 	110 	70 	80 	530 	88,33
257 	257 	Mega-Brasegali 	80 	160 	80 	130 	80 	100 	630 	105
258 	258 	Gobou 	50 	70 	50 	50 	50 	40 	310 	51,67
259 	259 	Flobio 	70 	85 	70 	60 	70 	50 	405 	67,5
260 	260 	Laggron 	100 	110 	90 	85 	90 	60 	535 	89,17
261 	261 	Medhyena 	35 	55 	35 	30 	30 	35 	220 	36,67
262 	262 	Grahyena 	70 	90 	70 	60 	60 	70 	420 	70
263 	263 	Zigzaton 	38 	30 	41 	30 	41 	60 	240 	40
264 	264 	Lineon 	78 	70 	61 	50 	61 	100 	420 	70
265 	265 	Chenipotte 	45 	45 	35 	20 	30 	20 	195 	32,5
266 	266 	Armulys 	50 	35 	55 	25 	25 	15 	205 	34,17
267 	267 	Charmillon 	60 	70 	50 	90 	50 	65 	385 	64,17
268 	268 	Blindalys 	50 	35 	55 	25 	25 	15 	205 	34,17
269 	269 	Papinox 	60 	50 	70 	50 	90 	65 	385 	64,17
270 	270 	Nenupiot 	40 	30 	30 	40 	50 	30 	220 	36,67
271 	271 	Lombre 	60 	50 	50 	60 	70 	50 	340 	56,67
272 	272 	Ludicolo 	80 	70 	70 	90 	100 	70 	480 	80
273 	273 	Grainipiot 	40 	40 	50 	30 	30 	30 	220 	36,67
274 	274 	Pifeuil 	70 	70 	40 	60 	40 	60 	340 	56,67
275 	275 	Tengalice 	90 	100 	60 	90 	60 	80 	480 	80
276 	276 	Nirondelle 	40 	55 	30 	30 	30 	85 	270 	45
277 	277 	Heledelle 	60 	85 	60 	50 	50 	125 	430 	71,67
278 	278 	Goelise 	40 	30 	30 	55 	30 	85 	270 	45
279 	279 	Bekipan 	60 	50 	100 	85 	70 	65 	430 	71,67
280 	280 	Tarsal 	28 	25 	25 	45 	35 	40 	198 	33
281 	281 	Kirlia 	38 	35 	35 	65 	55 	50 	278 	46,33
282 	282 	Gardevoir 	68 	65 	65 	125 	115 	80 	518 	86,33
282 	282 	Mega-Gardevoir 	68 	85 	65 	165 	135 	100 	618 	103
283 	283 	Arakdo 	40 	30 	32 	50 	52 	65 	269 	44,83
284 	284 	Maskadra 	70 	60 	62 	80 	82 	60 	414 	69
285 	285 	Balignon 	60 	40 	60 	40 	60 	35 	295 	49,17
286 	286 	Chapignon 	60 	130 	80 	60 	60 	70 	460 	76,67
287 	287 	Parecool 	60 	60 	60 	35 	35 	30 	280 	46,67
288 	288 	Vigoroth 	80 	80 	80 	55 	55 	90 	440 	77,33
289 	289 	Monaflemit 	150 	160 	100 	95 	65 	100 	670 	111,67
290 	290 	Ningale 	31 	45 	90 	30 	30 	40 	266 	44,33
291 	291 	Ninjask 	61 	90 	45 	50 	50 	160 	456 	76
292 	292 	Munja 	1 	90 	45 	30 	30 	40 	236 	39,33
293 	293 	Chuchmur 	64 	51 	23 	51 	23 	28 	240 	40
294 	294 	Ramboum 	84 	71 	43 	71 	43 	48 	360 	60
295 	295 	Brouhabam 	104 	91 	63 	91 	63 	68 	480 	80
296 	296 	Makuhita 	72 	60 	30 	20 	30 	25 	237 	39,5
297 	297 	Hariyama 	144 	120 	60 	40 	60 	50 	474 	79
298 	298 	Azurill 	50 	20 	40 	20 	40 	20 	190 	31,67
299 	299 	Tarinor 	30 	45 	135 	45 	90 	30 	375 	62,5
300 	300 	Skitty 	50 	45 	45 	35 	35 	50 	260 	43,33
301 	301 	Delcatty 	70 	65 	65 	55 	55 	70 	380 	63,33
302 	302 	Tenefix 	50 	75 	75 	65 	65 	50 	380 	63,33
303 	303 	Mysdibule 	50 	85 	85 	55 	55 	50 	380 	63,33
303 	303 	Mega-Mysdibule 	50 	105 	125 	55 	95 	50 	480 	80
304 	304 	Galekid 	50 	70 	100 	40 	40 	30 	330 	55
305 	305 	Galegon 	60 	90 	140 	50 	50 	40 	430 	71,67
306 	306 	Galeking 	70 	110 	180 	60 	60 	50 	530 	88,33
306 	306 	Mega-Galeking 	70 	140 	230 	60 	80 	50 	630 	105
307 	307 	Meditikka 	30 	40 	55 	40 	55 	60 	280 	46,67
308 	308 	Charmina 	60 	60 	75 	60 	75 	80 	410 	68,33
308 	308 	Mega-Charmina 	60 	100 	85 	80 	85 	100 	510 	85
309 	309 	Dynavolt 	40 	45 	40 	65 	40 	65 	295 	49,17
310 	310 	Elecsprint 	70 	75 	60 	105 	60 	105 	475 	79,17
310 	310 	Mega-Elecsprint 	70 	75 	80 	135 	80 	135 	575 	95,83
311 	311 	Posipi 	60 	50 	40 	85 	75 	95 	405 	67,5
312 	312 	Negapi 	60 	40 	50 	75 	85 	95 	405 	67,5
313 	313 	Muciole 	65 	73 	55 	47 	75 	85 	400 	66,67
314 	314 	Lumivole 	65 	47 	55 	73 	75 	85 	400 	66,67
315 	315 	Roselia 	50 	60 	45 	100 	80 	65 	400 	66,67
316 	316 	Gloupti 	70 	43 	53 	43 	53 	40 	302 	50,33
317 	317 	Avaltout 	100 	73 	83 	73 	83 	55 	467 	77,83
318 	318 	Carvanha 	45 	90 	20 	65 	20 	65 	305 	50,83
319 	319 	Sharpedo 	70 	120 	40 	95 	40 	95 	460 	76,67
320 	320 	Wailmer 	130 	70 	35 	70 	35 	60 	400 	66,67
321 	321 	Wailord 	170 	90 	45 	90 	45 	60 	500 	83,33
322 	322 	Chamallot 	60 	60 	40 	65 	45 	35 	305 	50,83
323 	323 	Camerupt 	70 	100 	70 	105 	75 	40 	460 	76,67
324 	324 	Chartor 	70 	85 	140 	85 	70 	20 	470 	78,33
325 	325 	Spoink 	60 	25 	35 	70 	80 	60 	330 	55
326 	326 	Groret 	80 	45 	65 	90 	110 	80 	470 	78,33
327 	327 	Spinda 	60 	60 	60 	60 	60 	60 	360 	60
328 	328 	Kraknoix 	45 	100 	45 	45 	45 	10 	290 	48,33
329 	329 	Vibraninf 	50 	70 	50 	50 	50 	70 	340 	56,67
330 	330 	Libegon 	80 	100 	80 	80 	80 	100 	520 	86,67
331 	331 	Cacnea 	50 	85 	40 	85 	40 	35 	335 	55,83
332 	332 	Cacturne 	70 	115 	60 	115 	60 	55 	475 	79,17
333 	333 	Tylton 	45 	40 	60 	40 	75 	50 	310 	51,67
334 	334 	Altaria 	75 	70 	90 	70 	105 	80 	490 	81,67
335 	335 	Mangriff 	73 	115 	60 	60 	60 	90 	458 	76,33
336 	336 	Seviper 	73 	100 	60 	100 	60 	65 	458 	76,33
337 	337 	Seleroc 	70 	55 	65 	95 	85 	70 	440 	73,33
338 	338 	Solaroc 	70 	95 	85 	55 	65 	70 	440 	73,33
339 	339 	Barloche 	50 	48 	43 	46 	41 	60 	288 	48
340 	340 	Barbicha 	110 	78 	73 	76 	71 	60 	468 	78
341 	341 	Ecrapince 	43 	80 	65 	50 	35 	35 	308 	51,33
342 	342 	Colhomard 	63 	120 	85 	90 	55 	55 	468 	78
343 	343 	Balbuto 	40 	40 	55 	40 	70 	55 	300 	50
344 	344 	Kaorine 	60 	70 	105 	70 	120 	75 	500 	83,33
345 	345 	Lilia 	66 	41 	77 	61 	87 	23 	355 	59,17
346 	346 	Vacilys 	86 	81 	97 	81 	107 	43 	495 	82,5
347 	347 	Anorith 	45 	95 	50 	40 	50 	75 	355 	59,17
348 	348 	Armaldo 	75 	125 	100 	70 	80 	45 	495 	82,5
349 	349 	Barpau 	20 	15 	20 	10 	55 	80 	200 	33,33
350 	350 	Milobellus 	95 	60 	79 	100 	125 	81 	540 	90
351 	351 	Morpheo 	70 	70 	70 	70 	70 	70 	420 	70
352 	352 	Kecleon 	60 	90 	70 	60 	120 	40 	440 	73,33
353 	353 	Polichombr 	44 	75 	35 	63 	33 	45 	295 	49,17
354 	354 	Branette 	64 	115 	65 	83 	63 	65 	455 	75,83
354 	354 	Mega-Branette 	64 	165 	75 	93 	83 	75 	555 	92,5
355 	355 	Skelenox 	20 	40 	90 	30 	90 	25 	295 	49,17
356 	356 	Teraclope 	40 	70 	130 	60 	130 	25 	455 	75,83
357 	357 	Tropius 	99 	68 	83 	72 	87 	51 	460 	76,67
358 	358 	Eoko 	65 	50 	70 	95 	80 	65 	425 	70,83
359 	359 	Absol 	65 	130 	60 	75 	60 	75 	465 	77,5
359 	359 	Mega-Absol 	65 	150 	60 	115 	60 	115 	565 	94,17
360 	360 	Okeoke 	95 	23 	48 	23 	48 	23 	260 	43,33
361 	361 	Stalgamin 	50 	50 	50 	50 	50 	50 	300 	50
362 	362 	Oniglali 	80 	80 	80 	80 	80 	80 	480 	80
363 	363 	Obalie 	70 	40 	50 	55 	50 	25 	290 	48,33
364 	364 	Phogleur 	90 	60 	70 	75 	70 	45 	410 	68,33
365 	365 	Kaimorse 	110 	80 	90 	95 	90 	65 	530 	88,33
366 	366 	Coquiperl 	35 	64 	85 	74 	55 	32 	345 	57,5
367 	367 	Serpang 	55 	104 	105 	94 	75 	52 	485 	80,83
368 	368 	Rosabyss 	55 	84 	105 	114 	75 	52 	485 	80,83
369 	369 	Relicanth 	100 	90 	130 	45 	65 	55 	485 	80,83
370 	370 	Lovdisc 	43 	30 	55 	40 	65 	97 	330 	55
371 	371 	Draby 	45 	75 	60 	40 	30 	50 	300 	50
372 	372 	Drackhaus 	65 	95 	100 	60 	50 	50 	420 	70
373 	373 	Drattak 	95 	135 	80 	110 	80 	100 	600 	100
374 	374 	Terhal 	40 	55 	80 	35 	60 	30 	300 	50
375 	375 	Metang 	60 	75 	100 	55 	80 	50 	420 	70
376 	376 	Metalosse 	80 	135 	130 	95 	90 	70 	600 	100
377 	377 	Regirock 	80 	100 	200 	50 	100 	50 	580 	96,67
378 	378 	Regice 	80 	50 	100 	100 	200 	50 	580 	96,67
379 	379 	Registeel 	80 	75 	150 	75 	150 	50 	580 	96,67
380 	380 	Latias 	80 	80 	90 	110 	130 	110 	600 	100
381 	381 	Latios 	80 	90 	80 	130 	110 	110 	600 	100
382 	382 	Kyogre 	100 	100 	90 	150 	140 	90 	670 	111,67
383 	383 	Groudon 	100 	150 	140 	100 	90 	90 	670 	111,67
384 	384 	Rayquaza 	105 	150 	90 	150 	90 	95 	680 	113,33
385 	385 	Jirachi 	100 	100 	100 	100 	100 	100 	600 	100
386 	386 	Deoxys (Forme de Base) 	50 	150 	50 	150 	50 	150 	600 	100
386 	386 	Deoxys (Forme Attaque) 	50 	180 	20 	180 	20 	150 	600 	100
386 	386 	Deoxys (Forme Defense) 	50 	70 	160 	70 	160 	90 	600 	100
386 	386 	Deoxys (Forme Vitesse) 	50 	95 	90 	95 	90 	180 	600 	100
387 	387 	Tortipouss 	55 	68 	64 	45 	55 	31 	318 	53
388 	388 	Boskara 	75 	89 	85 	55 	65 	36 	405 	67,5
389 	389 	Torterra 	95 	109 	105 	75 	85 	56 	525 	87,5
390 	390 	Ouisticram 	44 	58 	44 	58 	44 	61 	309 	51,5
391 	391 	Chimpenfeu 	64 	78 	52 	78 	52 	81 	405 	67,5
392 	392 	Simiabraz 	76 	104 	71 	104 	71 	108 	534 	89
393 	393 	Tiplouf 	53 	51 	53 	61 	56 	40 	314 	52,33
394 	394 	Prinplouf 	64 	66 	68 	81 	76 	50 	405 	67,5
395 	395 	Pingoleon 	84 	86 	88 	111 	101 	60 	530 	88,33
396 	396 	Etourmi 	40 	55 	30 	30 	30 	60 	245 	40,83
397 	397 	Etourvol 	55 	75 	50 	40 	40 	80 	340 	56,67
398 	398 	Etouraptor 	85 	120 	70 	50 	50 	100 	475 	79,17
399 	399 	Keunotor 	59 	45 	40 	35 	40 	31 	250 	41,67
400 	400 	Castorno 	79 	85 	60 	55 	60 	71 	410 	68,33
401 	401 	Crikzik 	37 	25 	41 	25 	41 	25 	194 	32,33
402 	402 	Melokrik 	77 	85 	51 	55 	51 	65 	384 	64
403 	403 	Lixy 	45 	65 	34 	40 	34 	45 	263 	43,83
404 	404 	Luxio 	60 	85 	49 	60 	49 	60 	363 	60,5
405 	405 	Luxray 	80 	120 	79 	95 	79 	70 	523 	87,17
406 	406 	Rozbouton 	40 	30 	35 	50 	70 	55 	280 	46,67
407 	407 	Roserade 	60 	70 	55 	125 	105 	90 	505 	84,17
408 	408 	Kranidos 	67 	125 	40 	30 	30 	58 	350 	58,33
409 	409 	Charkos 	97 	165 	60 	65 	50 	58 	495 	82,5
410 	410 	Dinoclier 	30 	42 	118 	42 	88 	30 	350 	58,33
411 	411 	Bastiodon 	60 	52 	168 	47 	138 	30 	495 	58,33
412 	412 	Cheniti 	40 	29 	45 	29 	45 	36 	224 	37,33
413 	413 	Cheniselle (Cape Plante) 	60 	59 	85 	79 	105 	36 	424 	70,67
413 	413 	Cheniselle (Cape Sol) 	60 	79 	105 	59 	85 	36 	424 	70,67
413 	413 	Cheniselle (Cape Dechet) 	60 	69 	95 	69 	95 	36 	424 	70,67
414 	414 	Papilord 	70 	94 	50 	94 	50 	66 	424 	70,67
415 	415 	Apitrini 	30 	30 	42 	30 	42 	70 	244 	40,67
416 	416 	Apireine 	70 	80 	102 	80 	102 	40 	474 	79
417 	417 	Pachirisu 	60 	45 	70 	45 	90 	95 	405 	67,5
418 	418 	Mustebouee 	55 	65 	35 	60 	30 	85 	330 	55
419 	419 	Musteflott 	85 	105 	55 	85 	50 	115 	495 	82,5
420 	420 	Ceribou 	45 	35 	45 	62 	53 	35 	275 	45;83
421 	421 	Ceriflor 	70 	60 	70 	87 	78 	85 	450 	75
422 	422 	Sancoki 	76 	48 	48 	57 	62 	34 	325 	54,17
423 	423 	Tritosor 	111 	83 	68 	92 	82 	39 	475 	79,17
424 	424 	Capidextre 	75 	100 	66 	60 	66 	115 	482 	80,33
425 	425 	Baudrive 	90 	50 	34 	60 	44 	70 	348 	58
426 	426 	Grodrive 	150 	80 	44 	90 	54 	80 	498 	83
427 	427 	Laporeille 	55 	66 	44 	44 	56 	85 	350 	58,33
428 	428 	Lockpin 	65 	76 	84 	54 	96 	105 	480 	80
429 	429 	Magireve 	60 	60 	60 	105 	105 	105 	495 	82,5
430 	430 	Corboss 	100 	125 	52 	105 	52 	71 	505 	84,17
431 	431 	Chaglam 	49 	55 	42 	42 	37 	85 	310 	51,67
432 	432 	Chaffreux 	71 	82 	64 	64 	59 	112 	452 	75,33
433 	433 	Korillon 	45 	30 	50 	65 	50 	45 	285 	47,5
434 	434 	Moufouette 	63 	63 	47 	41 	41 	74 	329 	54,83
435 	435 	Moufflair 	103 	93 	67 	71 	61 	84 	479 	79,83
436 	436 	Archeomire 	57 	24 	86 	24 	86 	23 	300 	50
437 	437 	Archeodong 	67 	89 	116 	79 	116 	33 	500 	83,33
438 	438 	Manzai 	50 	80 	95 	10 	45 	10 	290 	48,33
439 	439 	Mime Jr. 	20 	25 	45 	70 	90 	60 	310 	51,67
440 	440 	Ptiravi 	100 	5 	5 	15 	65 	30 	220 	36,67
441 	441 	Pijako 	76 	65 	45 	92 	42 	91 	411 	68,5
442 	442 	Spiritomb 	50 	92 	108 	92 	108 	35 	485 	80,83
443 	443 	Griknot 	58 	70 	45 	40 	45 	42 	300 	50
444 	444 	Carmache 	68 	90 	65 	50 	55 	82 	410 	68,33
445 	445 	Carchacrok 	108 	130 	95 	80 	85 	102 	600 	100
445 	445 	Mega-Carchacrok 	108 	170 	115 	120 	95 	92 	700 	116,67
446 	446 	Goinfrex 	135 	85 	40 	40 	85 	5 	390 	65
447 	447 	Riolu 	40 	70 	40 	35 	40 	60 	285 	47,5
448 	448 	Lucario 	70 	110 	70 	115 	70 	90 	525 	87,5
448 	448 	Mega-Lucario 	70 	145 	88 	140 	70 	112 	625 	104,17
449 	449 	Hippopotas 	68 	72 	78 	38 	42 	32 	330 	55
450 	450 	Hippodocus 	108 	112 	118 	68 	72 	47 	525 	87,5
451 	451 	Rapion 	40 	50 	90 	30 	55 	65 	330 	55
452 	452 	Drascore 	70 	90 	110 	60 	75 	95 	500 	83,33
453 	453 	Cradopaud 	48 	61 	40 	61 	40 	50 	300 	50
454 	454 	Coatox 	83 	106 	65 	86 	65 	85 	490 	81,67
455 	455 	Vortente 	74 	100 	72 	90 	72 	46 	454 	75,67
456 	456 	Ecayon 	49 	49 	56 	49 	61 	66 	330 	55
457 	457 	Lumineon 	69 	69 	76 	69 	86 	91 	460 	76,67
458 	458 	Babimanta 	45 	20 	50 	60 	120 	50 	345 	57,5
459 	459 	Blizzi 	60 	62 	50 	62 	60 	40 	334 	55,67
460 	460 	Blizzaroi 	90 	92 	75 	92 	85 	60 	494 	82,33
460 	460 	Mega-Blizzaroi 	90 	132 	105 	132 	105 	30 	594 	99
461 	461 	Dimoret 	70 	120 	65 	45 	85 	125 	510 	85
462 	462 	Magnezone 	70 	70 	115 	130 	90 	60 	535 	89,17
463 	463 	Coudlangue 	110 	85 	95 	80 	95 	50 	515 	85,83
464 	464 	Rhinastoc 	115 	140 	130 	55 	55 	40 	535 	89,17
465 	465 	Bouldeneu 	100 	100 	125 	110 	50 	50 	535 	89,17
466 	466 	Elekable 	75 	123 	67 	95 	85 	95 	540 	90
467 	467 	Maganon 	75 	95 	67 	125 	95 	83 	540 	90
468 	468 	Togekiss 	85 	50 	95 	120 	115 	80 	545 	90,83
469 	469 	Yanmega 	86 	76 	86 	116 	56 	95 	515 	85,83
470 	470 	Phyllali 	65 	110 	130 	60 	65 	95 	525 	87,5
471 	471 	Givrali 	65 	60 	110 	130 	95 	65 	525 	87,5
472 	472 	Scorvol 	75 	95 	125 	45 	75 	95 	510 	85
473 	473 	Mammochon 	110 	130 	80 	70 	60 	80 	530 	88,33
474 	474 	Porygon-Z 	85 	80 	70 	135 	75 	90 	535 	89,17
475 	475 	Gallame 	68 	125 	65 	65 	115 	80 	518 	86,33
476 	476 	Tarinorme 	60 	55 	145 	75 	150 	40 	525 	87,5
477 	477 	Noctunoir 	45 	100 	135 	65 	135 	45 	525 	87,5
478 	478 	Momartik 	70 	80 	70 	80 	70 	110 	480 	80
479 	479 	Motisma (Forme Normale) 	50 	50 	77 	95 	77 	91 	440 	73,33
479 	479 	Motisma (Forme Chaleur) 	50 	65 	107 	105 	107 	86 	520 	86,67
479 	479 	Motisma (Forme Lavage) 	50 	65 	107 	105 	107 	86 	520 	86,67
479 	479 	Motisma (Forme Froid) 	50 	65 	107 	105 	107 	86 	520 	86,67
479 	479 	Motisma (Forme Tonte) 	50 	65 	107 	105 	107 	86 	520 	86,67
479 	479 	Motisma (Forme Helice) 	50 	65 	107 	105 	107 	86 	520 	86,67
480 	480 	Crehelf 	75 	75 	130 	75 	130 	95 	580 	96,67
481 	481 	Crefollet 	80 	105 	105 	105 	105 	80 	580 	96,67
482 	482 	Crefadet 	75 	125 	70 	125 	70 	115 	580 	96,67
483 	483 	Dialga 	100 	120 	120 	150 	100 	90 	680 	113,33
484 	484 	Palkia 	90 	120 	100 	150 	120 	100 	680 	113,33
485 	485 	Heatran 	91 	90 	106 	130 	106 	77 	600 	100
486 	486 	Regigigas 	110 	160 	110 	80 	110 	100 	670 	111,67
487 	487 	Giratina (Forme Alternative) 	150 	100 	120 	100 	120 	90 	680 	113,33
487 	487 	Giratina (Forme Originelle) 	150 	120 	100 	120 	100 	90 	680 	113,33
488 	488 	Cresselia 	120 	70 	120 	75 	130 	85 	600 	100
489 	489 	Phione 	80 	80 	80 	80 	80 	80 	480 	80
490 	490 	Manaphy 	100 	100 	100 	100 	100 	100 	600 	100
491 	491 	Darkrai 	70 	90 	90 	135 	90 	125 	600 	100
492 	492 	Shaymin (Forme Terrestre) 	100 	100 	100 	100 	100 	100 	600 	100
492 	492 	Shaymin (Forme Celeste) 	100 	103 	75 	120 	75 	127 	600 	100
493 	493 	Arceus 	120 	120 	120 	120 	120 	120 	720 	120
494 	494 	Victini 	100 	100 	100 	100 	100 	100 	600 	100
495 	495 	Vipelierre 	45 	45 	55 	45 	55 	63 	308 	51,33
496 	496 	Lianaja 	60 	60 	75 	60 	75 	83 	413 	68,83
497 	497 	Majaspic 	75 	75 	95 	75 	95 	113 	528 	88
498 	498 	Gruikui 	65 	63 	45 	45 	45 	45 	308 	51,33
499 	499 	Grotichon 	90 	93 	55 	70 	55 	55 	418 	69,67
500 	500 	Roitiflam 	110 	123 	65 	100 	65 	65 	528 	88
501 	501 	Moustillon 	55 	55 	45 	63 	45 	45 	308 	51,33
502 	502 	Mateloutre 	75 	75 	60 	83 	60 	60 	413 	68,83
503 	503 	Clamiral 	95 	100 	85 	108 	70 	70 	528 	88
504 	504 	Ratentif 	45 	55 	39 	35 	39 	42 	255 	42,5
505 	505 	Miradar 	60 	85 	69 	60 	69 	77 	420 	70
506 	506 	Ponchiot 	45 	60 	45 	25 	45 	55 	275 	45,83
507 	507 	Ponchien 	65 	80 	65 	35 	65 	60 	370 	61,67
508 	508 	Mastouffe 	85 	100 	90 	45 	90 	80 	490 	81,67
509 	509 	Chacripan 	41 	50 	37 	50 	37 	66 	281 	46,83
510 	510 	Leopardus 	64 	88 	50 	88 	50 	106 	446 	74,33
511 	511 	Feuillajou 	50 	53 	48 	53 	48 	64 	316 	52,67
512 	512 	Feuiloutan 	75 	98 	63 	98 	63 	101 	498 	83
513 	513 	Flamajou 	50 	53 	48 	53 	48 	64 	316 	52,67
514 	514 	Flamoutan 	75 	98 	63 	98 	63 	101 	498 	83
515 	515 	Flotajou 	50 	53 	48 	53 	48 	64 	316 	52,67
516 	516 	Flotoutan 	75 	98 	63 	98 	63 	101 	498 	83
517 	517 	Munna 	76 	25 	45 	67 	55 	24 	292 	48,67
518 	518 	Mushana 	116 	55 	85 	107 	95 	29 	487 	81,17
519 	519 	Poichigeon 	50 	55 	50 	36 	30 	43 	264 	44
520 	520 	Colombeau 	62 	77 	62 	50 	42 	65 	358 	59,67
521 	521 	Deflaisan 	80 	105 	80 	65 	55 	93 	478 	79,67
522 	522 	Zebibron 	45 	60 	32 	50 	32 	76 	295 	49,17
523 	523 	Zeblitz 	75 	100 	63 	80 	63 	116 	497 	82,83
524 	524 	Nodulithe 	55 	75 	85 	25 	25 	15 	280 	46,67
525 	525 	Geolithe 	70 	105 	105 	50 	40 	20 	390 	65
526 	526 	Gigalithe 	85 	135 	130 	60 	70 	25 	505 	84,17
527 	527 	Chovsourir 	55 	45 	43 	55 	43 	72 	313 	52,17
528 	528 	Rhinolove 	67 	57 	55 	77 	55 	114 	425 	70,83
529 	529 	Rototaupe 	60 	85 	40 	30 	45 	68 	425 	70,83
530 	530 	Minotaupe 	110 	135 	60 	50 	65 	88 	508 	84,67
531 	531 	Nanmeouie 	103 	60 	86 	60 	86 	50 	445 	74,17
532 	532 	Charpenti 	75 	80 	55 	25 	35 	35 	305 	50,83
533 	533 	Ouvrifier 	85 	105 	85 	40 	50 	40 	405 	67,5
534 	534 	Betochef 	105 	140 	95 	55 	65 	45 	505 	84,17
535 	535 	Tritonde 	50 	50 	40 	50 	40 	64 	294 	49
536 	536 	Batracne 	75 	65 	55 	65 	55 	69 	384 	64
537 	537 	Crapustule 	105 	85 	75 	85 	75 	74 	499 	83,17
538 	538 	Judokrak 	120 	100 	85 	30 	85 	45 	465 	77,5
539 	539 	Karaclee 	75 	125 	75 	30 	75 	85 	465 	77,5
540 	540 	Larveyette 	45 	53 	70 	40 	60 	42 	310 	51,67
541 	541 	Couverdure 	55 	63 	90 	50 	80 	42 	380 	63,33
542 	542 	Manternel 	75 	103 	80 	70 	70 	92 	490 	81,67
543 	543 	Venipatte 	30 	45 	59 	30 	39 	57 	260 	43,33
544 	544 	Scobolide 	40 	55 	99 	40 	79 	47 	360 	60
545 	545 	Brutapode 	60 	90 	89 	55 	69 	112 	475 	79,17
546 	546 	Doudouvet 	40 	27 	60 	37 	50 	66 	280 	46,67
547 	547 	Farfaduvet 	60 	67 	85 	77 	75 	116 	480 	80
548 	548 	Chlorobule 	45 	35 	50 	70 	50 	30 	280 	46,67
549 	549 	Fragilady 	70 	60 	75 	110 	75 	90 	480 	80
550 	550 	Bargantua 	70 	92 	65 	80 	55 	98 	460 	76,67
551 	551 	Mascaiman 	50 	72 	35 	35 	35 	65 	292 	48,67
552 	552 	Escroco 	60 	82 	45 	45 	45 	74 	351 	58,5
553 	553 	Crocorible 	95 	117 	70 	65 	70 	92 	509 	84,83
554 	554 	Darumarond 	70 	90 	45 	15 	45 	50 	315 	52,5
555 	555 	Darumacho (Mode Normal) 	105 	140 	55 	30 	55 	95 	480 	80
555 	555 	Darumacho (Mode Daruma) 	105 	30 	105 	140 	105 	55 	540 	90
556 	556 	Maracachi 	75 	86 	67 	106 	67 	60 	461 	76,83
557 	557 	Crabicoque 	50 	65 	85 	35 	35 	55 	325 	54,17
558 	558 	Crabaraque 	70 	95 	125 	65 	75 	45 	475 	79,17
559 	559 	Baggiguane 	50 	75 	70 	35 	70 	48 	348 	58
560 	560 	Baggaid 	65 	90 	115 	45 	115 	58 	488 	81,33
561 	561 	Cryptero 	72 	58 	80 	103 	80 	97 	490 	81,67
562 	562 	Tutafeh 	38 	30 	85 	55 	65 	30 	303 	50,5
563 	563 	Tutankafer 	58 	50 	145 	95 	105 	30 	483 	80,5
564 	564 	Carapagos 	54 	78 	103 	53 	45 	22 	355 	59,17
565 	565 	Megapagos 	74 	108 	133 	83 	65 	32 	495 	82,5
566 	566 	Arkeapti 	55 	112 	45 	74 	45 	70 	401 	66,83
567 	567 	Aeropteryx 	75 	140 	65 	112 	65 	110 	567 	94,5
568 	568 	Miamiasme 	50 	50 	62 	40 	62 	65 	329 	54,83
569 	569 	Miasmax 	80 	95 	82 	60 	82 	75 	474 	79
570 	570 	Zorua 	40 	65 	40 	80 	40 	65 	330 	55
571 	571 	Zoroark 	60 	105 	60 	120 	60 	105 	510 	85
572 	572 	Chinchidou 	55 	50 	40 	40 	40 	75 	300 	50
573 	573 	Pashmilla 	75 	95 	60 	65 	60 	115 	470 	78,33
574 	574 	Scrutella 	45 	30 	50 	55 	65 	45 	290 	48,33
575 	575 	Mesmerella 	60 	45 	70 	75 	85 	55 	390 	65
576 	576 	Siderella 	70 	55 	95 	95 	110 	65 	490 	81,67
577 	577 	Nucleos 	45 	30 	40 	105 	50 	20 	290 	48,33
578 	578 	Meios 	65 	40 	50 	125 	60 	30 	370 	61,67
579 	579 	Symbios 	110 	65 	75 	125 	85 	30 	490 	81,67
580 	580 	Couaneton 	62 	44 	50 	44 	50 	55 	305 	50,83
581 	581 	Lakmecygne 	75 	87 	63 	87 	63 	98 	473 	78,83
582 	582 	Sorbebe 	36 	50 	50 	65 	60 	44 	305 	50,83
583 	583 	Sorboul 	51 	65 	65 	80 	75 	59 	395 	65,83
584 	584 	Sorbouboul 	71 	95 	85 	110 	95 	79 	535 	89,17
585 	585 	Vivaldaim 	60 	60 	50 	40 	50 	75 	335 	55,83
586 	586 	Haydaim 	80 	100 	70 	60 	70 	95 	475 	79,17
587 	587 	Emolga 	55 	75 	60 	75 	60 	103 	428 	71,33
588 	588 	Carabing 	50 	75 	45 	40 	45 	60 	315 	52,5
589 	589 	Lancargot 	70 	135 	105 	60 	105 	20 	495 	82,5
590 	590 	Trompignon 	69 	55 	45 	55 	55 	15 	294 	49
591 	591 	Gaulet 	114 	85 	70 	85 	80 	30 	464 	77,33
592 	592 	Viskuse 	55 	40 	50 	65 	85 	40 	335 	55,83
593 	593 	Moyade 	100 	60 	70 	85 	105 	60 	480 	80
594 	594 	Mamanbo 	165 	75 	80 	40 	45 	65 	470 	78,33
595 	595 	Statitik 	50 	47 	50 	57 	50 	65 	319 	53,17
596 	596 	Mygavolt 	70 	77 	60 	97 	60 	108 	472 	78,67
597 	597 	Grindur 	44 	50 	91 	24 	86 	10 	305 	50,83
598 	598 	Noacier 	74 	94 	131 	54 	116 	20 	489 	81,5
599 	599 	Tic 	40 	55 	70 	45 	60 	30 	300 	50
600 	600 	Clic 	60 	80 	95 	70 	85 	50 	440 	73,33
601 	601 	Cliticlic 	60 	100 	115 	70 	85 	90 	520 	86,67
602 	602 	Anchwatt 	35 	55 	40 	45 	40 	60 	275 	45,83
603 	603 	Lamperoie 	65 	85 	70 	75 	70 	40 	405 	67,5
604 	604 	Ohmassacre 	85 	115 	80 	105 	80 	50 	515 	85,83
605 	605 	Lewsor 	55 	55 	55 	85 	55 	30 	335 	55,83
606 	606 	Neitram 	75 	75 	75 	125 	95 	40 	485 	80,83
607 	607 	Funecire 	50 	30 	55 	65 	55 	20 	275 	45,83
608 	608 	Melancolux 	60 	40 	60 	95 	60 	55 	370 	61,67
609 	609 	Lugulabre 	60 	55 	90 	145 	90 	80 	520 	86,67
610 	610 	Coupenotte 	46 	87 	60 	30 	40 	57 	320 	53,33
611 	611 	Incisache 	66 	117 	70 	40 	50 	67 	410 	68,33
612 	612 	Tranchodon 	76 	147 	90 	60 	70 	97 	540 	90
613 	613 	Polarhume 	55 	70 	40 	60 	40 	40 	305 	50,83
614 	614 	Polagriffe 	95 	110 	80 	70 	80 	50 	485 	80,83
615 	615 	Hexagel 	70 	50 	30 	95 	135 	105 	485 	80,83
616 	616 	Escargaume 	50 	40 	85 	40 	65 	25 	305 	50,83
617 	617 	Limaspeed 	80 	70 	40 	100 	60 	145 	495 	82,5
618 	618 	Limonde 	109 	66 	84 	81 	99 	32 	471 	78,5
619 	619 	Kungfouine 	45 	85 	50 	55 	50 	65 	350 	58,33
620 	620 	Shaofouine 	65 	125 	60 	95 	60 	105 	510 	85
621 	621 	Drakkarmin 	77 	120 	90 	60 	90 	48 	485 	80,83
622 	622 	Gringolem 	59 	74 	50 	35 	50 	35 	303 	50,5
623 	623 	Golemastoc 	89 	124 	80 	55 	80 	55 	483 	80,5
624 	624 	Scalpion 	45 	85 	70 	40 	40 	60 	340 	56,67
625 	625 	Scalproie 	65 	125 	100 	60 	70 	70 	490 	81,67
626 	626 	Frison 	95 	110 	95 	40 	95 	55 	490 	81,67
627 	627 	Furaiglon 	70 	83 	50 	37 	50 	60 	350 	58,33
628 	628 	Gueriaigle 	100 	123 	75 	57 	75 	80 	510 	85
629 	629 	Vostourno 	70 	55 	75 	45 	65 	60 	370 	61,67
630 	630 	Vaututrice 	110 	65 	105 	55 	95 	80 	510 	85
631 	631 	Aflamanoir 	85 	97 	66 	105 	66 	65 	484 	80,67
632 	632 	Fermite 	58 	109 	112 	48 	48 	109 	484 	80,67
633 	633 	Solochi 	52 	65 	50 	45 	50 	38 	300 	50
634 	634 	Diamat 	72 	85 	70 	65 	70 	58 	420 	70
635 	635 	Trioxhydre 	92 	105 	90 	125 	90 	98 	600 	100
636 	636 	Pyronille 	55 	85 	55 	50 	55 	60 	360 	60
637 	637 	Pyrax 	85 	60 	65 	135 	105 	100 	550 	91,67
638 	638 	Cobaltium 	91 	90 	129 	90 	72 	108 	580 	96,67
639 	639 	Terrakium 	91 	129 	90 	72 	90 	108 	580 	96,67
640 	640 	Viridium 	91 	90 	72 	90 	129 	108 	580 	96,67
641 	641 	Boreas (Forme Avatar) 	79 	115 	70 	125 	80 	111 	580 	96,67
641 	641 	Boreas (Forme Totemique) 	79 	100 	80 	110 	90 	121 	580 	96,67
642 	642 	Fulguris (Forme Avatar) 	79 	115 	70 	125 	80 	111 	580 	96,67
642 	642 	Fulguris (Forme Totemique) 	79 	105 	70 	145 	80 	101 	580 	96,67
643 	643 	Reshiram 	100 	120 	100 	150 	120 	90 	680 	113,33
644 	644 	Zekrom 	100 	150 	120 	120 	100 	90 	680 	113,33
645 	645 	Demeteros (Forme Avatar) 	89 	125 	90 	115 	80 	101 	600 	100
645 	645 	Demeteros (Forme Totemique) 	89 	145 	90 	105 	80 	91 	600 	100
646 	646 	Kyurem 	125 	130 	90 	130 	90 	95 	660 	110
646 	646 	Kyurem (Noir) 	125 	170 	100 	120 	90 	95 	700 	116,66
646 	646 	Kyurem (Blanc) 	125 	120 	90 	170 	100 	95 	700 	116,66
647 	647 	Keldeo 	91 	72 	90 	129 	90 	108 	580 	96,67
648 	648 	Meloetta (Forme Voix) 	100 	77 	77 	128 	128 	90 	600 	100
648 	648 	Meloetta (Forme Danse) 	100 	128 	90 	77 	77 	128 	600 	100
649 	649 	Genesect 	71 	120 	95 	120 	95 	99 	600 	100
650 	650 	Marisson 	56 	64 	66 	50 	45 	38 	319 	53,17
651 	651 	Boguerisse 	54 	79 	101 	50 	50 	52 	386 	64,33
652 	652 	Blindepique 	88 	107 	122 	74 	75 	64 	530 	88,33
653 	653 	Feunnec 	40 	45 	40 	62 	60 	60 	307 	51,17
654 	654 	Roussil 	59 	59 	58 	90 	70 	73 	409 	68,17
655 	655 	Goupelin 	75 	69 	72 	114 	100 	104 	534 	89
656 	656 	Grenousse 	37 	53 	49 	66 	50 	70 	325 	54,17
657 	657 	Croaporal 	54 	63 	52 	83 	56 	97 	405 	67,5
658 	658 	Amphinobi 	72 	95 	67 	103 	71 	122 	530 	88,33
659 	659 	Sapereau 	38 	36 	38 	32 	36 	57 	237 	39,5
660 	660 	Excavarenne 	85 	56 	77 	50 	77 	78 	423 	70,5
661 	661 	Passerouge 	45 	50 	43 	40 	38 	62 	278 	46,33
662 	662 	Braisillon 	62 	73 	55 	56 	52 	84 	382 	63,67
663 	663 	Flambusard 	78 	81 	71 	74 	69 	126 	499 	83,17
664 	664 	Lepidonille 	38 	35 	40 	27 	25 	35 	200 	33,33
665 	665 	Peregrain 	45 	22 	60 	37 	30 	29 	223 	37,17
666 	666 	Prismillon 	80 	52 	50 	90 	50 	89 	411 	68,5
667 	667 	Helionceau 	62 	50 	58 	73 	54 	72 	369 	61,5
668 	668 	Nemelios 	86 	68 	72 	109 	66 	106 	507 	84,5
669 	669 	Flabebe 	44 	38 	39 	61 	79 	42 	303 	50,5
670 	670 	Floette 	58 	54 	52 	90 	116 	63 	433 	72,17
671 	671 	Florges 	78 	65 	68 	112 	154 	75 	552 	92
672 	672 	Cabriolaine 	66 	65 	48 	62 	57 	52 	350 	58,33
673 	673 	Chevroum 	123 	100 	62 	97 	81 	68 	531 	88,5
674 	674 	Pandespiegle 	67 	82 	62 	46 	48 	43 	348 	58
675 	675 	Pandarbare 	95 	124 	78 	69 	71 	58 	495 	82,5
676 	676 	Couafarel 	75 	80 	60 	65 	90 	102 	472 	78,67
677 	677 	Psystigri 	60 	22 	62 	72 	72 	95 	383 	63,83
678 	678 	Mistigrix 	74 	48 	76 	83 	81 	104 	466 	77,67
679 	679 	Monorpale 	40 	90 	130 	35 	30 	10 	335 	55,83
680 	680 	Dimocles 	59 	110 	150 	45 	49 	35 	448 	74,67
681 	681 	Exagide (Forme Assaut) 	60 	150 	50 	150 	50 	60 	520 	86,67
681 	681 	Exagide (Forme Parade) 	60 	50 	150 	50 	150 	60 	520 	86,67
682 	682 	Fluvetin 	78 	52 	60 	63 	65 	23 	341 	56,83
683 	683 	Cocotine 	100 	65 	75 	95 	90 	30 	455 	75,83
684 	684 	Sucroquin 	62 	48 	66 	59 	57 	49 	455 	56,83
685 	685 	Cupcanaille 	82 	80 	86 	85 	75 	72 	480 	80
686 	686 	Sepiatop 	53 	54 	53 	37 	46 	45 	288 	48
687 	687 	Sepiatroce 	86 	92 	88 	68 	73 	75 	482 	80,33
688 	688 	Opermine 	50 	95 	95 	30 	80 	60 	410 	68,33
689 	689 	Golgopathe 	70 	115 	115 	50 	100 	80 	530 	88,33
690 	690 	Venalgue 	50 	60 	60 	60 	60 	30 	320 	53,33
691 	691 	Kravarech 	65 	75 	90 	97 	123 	44 	494 	82,33
692 	692 	Flingouste 	50 	53 	62 	58 	63 	44 	330 	55
693 	693 	Gamblast 	71 	73 	88 	120 	89 	59 	500 	83,33
694 	694 	Galvaran 	44 	38 	33 	61 	43 	70 	289 	48,17
695 	695 	Iguolta 	62 	55 	52 	109 	94 	109 	481 	80,17
696 	696 	Ptyranidur 	58 	89 	77 	45 	45 	48 	362 	60,33
697 	697 	Rexillius 	82 	121 	119 	69 	59 	71 	521 	86,83
698 	698 	Amagara 	77 	59 	50 	67 	63 	46 	362 	60,33
699 	699 	Dragmara 	123 	77 	72 	99 	92 	58 	521 	86,83
700 	700 	Nymphali 	95 	65 	65 	110 	130 	60 	525 	87,5
701 	701 	Brutalibre 	70 	95 	80 	65 	70 	110 	490 	81,67
702 	702 	Dedenne 	67 	58 	57 	81 	67 	101 	431 	71,83
703 	703 	Strassie 	50 	50 	150 	50 	150 	50 	500 	83,33
704 	704 	Mucuscule 	40 	50 	30 	70 	100 	45 	335 	55,83
705 	705 	Colimucus 	50 	70 	50 	90 	120 	65 	455 	75,83
706 	706 	Muplodocus 	90 	100 	70 	110 	150 	80 	600 	100
707 	707 	Trousselin 	57 	80 	91 	80 	87 	75 	470 	78,33
708 	708 	Brocelome 	43 	70 	48 	50 	60 	38 	309 	51,5
709 	709 	Desseliande 	85 	110 	76 	65 	82 	56 	474 	79
710 	710 	Pitrouille (Taille Mini) 	44 	66 	70 	44 	55 	56 	335 	55,83
710 	710 	Pitrouille (Taille Normale) 	49 	66 	70 	44 	55 	51 	335 	55,83
710 	710 	Pitrouille (Taille Maxi) 	54 	66 	70 	44 	55 	51 	335 	55,83
710 	710 	Pitrouille (Taille Ultra) 	59 	66 	70 	44 	55 	41 	335 	55,83
711 	711 	Banshitrouye (Taille Mini) 	55 	85 	122 	58 	75 	99 	494 	82,33
711 	711 	Banshitrouye (Taille Normale) 	65 	90 	122 	58 	75 	84 	494 	82,33
711 	711 	Banshitrouye (Taille Maxi) 	75 	95 	122 	58 	75 	69 	494 	82,33
711 	711 	Banshitrouye (Taille Ultra) 	85 	100 	122 	58 	75 	54 	494 	82,33
712 	712 	Grelacon 	55 	69 	85 	32 	35 	28 	304 	50,67
713 	713 	Seracrawl 	95 	117 	184 	44 	46 	28 	514 	85,67
714 	714 	Sonistrelle 	70 	60 	60 	82 	60 	97 	429 	71,5
715 	715 	Bruyverne 	85 	70 	80 	97 	80 	123 	535 	89,17
716 	716 	Xerneas 	126 	131 	95 	131 	98 	99 	680 	113,33
717 	717 	Yveltal 	126 	131 	95 	131 	98 	99 	680 	113,33
718 	718 	Zygarde 	108 	100 	121 	81 	95 	95 	600 	100 """

megatypes = """3	Mega-Florizarre	PLANTE/POISON	Isograisse
6	Mega-Dracaufeu X	FEU/DRAGON	Griffe Dure
6	Mega-Dracaufeu Y	FEU/VOL	Secheresse
9	Mega-Tortank	EAU/	Mega Blaster
65	Mega-Alakazam	PSY/	Calque
94	Mega-Ectoplasma	SPECTRE/POISON	Marque Ombre
115	Mega-Kangourex	NORMAL/	Amour Filial
127	Mega-Scarabrute	INSECTE/VOL	Peau Celeste
130	Mega-Leviator	EAU/TENEBRE	Brise Moule
142	Mega-Ptera	ROCHE/VOL	Griffe Dure
150	Mega-Mewtwo X	PSY/COMBAT	Impassible
150	Mega-Mewtwo Y	PSY/	Insomnia
181	Mega-Pharamp	ELECTRIQUE/DRAGON	Brise Moule
212	Mega-Cizayox	INSECTE/ACIER	Technicien
214	Mega-Scarhino	INSECTE/COMBAT	Multi-Coups
229	Mega-Demolosse	TENEBRE/FEU	Force Soleil
248	Mega-Tyranocif	ROCHE/TENEBRE	Sable Volant
257	Mega-Brasegali	FEU/COMBAT	Turbo
282	Mega-Gardevoir	PSY/FEE	Peau Feerique
303	Mega-Mysdibule	ACIER/FEE	Coloforce
306	Mega-Galeking	ACIER/	Filtre
308	Mega-Charmina	COMBAT/PSY	Force Pure
310	Mega-Elecsprint	ELECTRIQUE/	Intimidation
354	Mega-Branette	SPECTRE/	Farceur
359	Mega-Absol	TENEBRE/	Miroir Magik
445	Mega-Carchacrok	DRAGON/SOL	Force Sable
448	Mega-Lucario	ACIER/COMBAT	Adaptabilite
460	Mega-Blizzaroi	GLACE/PLANTE	Alerte Neige"""

talents = {
"Rattatac":
[u'Cran', u'Fuite', u'Agitation'],
"Porygon-Z":
[u'Telecharge', u'Adaptabilite', u'Analyste'],
"Baggiguane":
[u'Mue', u'Impudence', u'Intimidation'],
"Noadkoko":
[u'Chlorophyle', u'Recolte'],
"Gueriaigle":
[u'Regard Vif', u'Sans Limite', u'Acharne'],
"Polichombr":
[u'Insomnia', u'Fouille', u'Corps Maudit'],
"Gaulet":
[u'Pose Spore', u'Rege-Force'],
"Hyporoi":
[u'Glissade', u'Sniper', u'Moiteur'],
"Elekable":
[u'Motorise', u'Esprit Vital'],
"Roussil":
[u'Brasier', u'Magicien'],
"Pashmilla":
[u'Joli Sourire', u'Technicien', u'Multi-Coups'],
"Emolga":
[u'Statik', u'Motorise'],
"Grolem":
[u'Tete de Roc', u'Fermete'],
"Cresselia":
[u'Levitation'],
"Flotoutan":
[u'Gloutonnerie', u'Torrent'],
"Bekipan":
[u'Regard Vif', u'Cuvette'],
"Mateloutre":
[u'Torrent', u'Coque Armure'],
"Dinoclier":
[u'Fermete', u'Anti-Bruit'],
"Absol":
[u'Pression', u'Chanceux', u'Coeur Noble'],
"Azurill":
[u'Isograisse', u'Coloforce', u'Herbivore'],
"Apireine":
[u'Pression', u'Tension'],
"Dracaufeu":
[u'Brasier', u'Force Soleil'],
"Solochi":
[u'Agitation'],
"Volcaropod":
[u'Armumagma', u'Corps Ardent', u'Armurouillee'],
"Snubbull":
[u'Fuite', u'Intimidation', u'Phobique'],
"Sharpedo":
[u'Peau Dure'],
"Tutafeh":
[u'Momie'],
"Noctunoir":
[u'Pression'],
"Melodelfe":
[u'Joli Sourire', u'Garde Magik', u'Inconscient'],
"Celebi":
[u'Medic nature'],
"Cocotine":
[u'Coeur Soin', u'Aroma-Voile'],
"Cheniselle":
[u'Anticipation', u'Envelocape'],
"Zorua":
[u'Illusion'],
"Carabing":
[u'Essaim', u'Mue', u'Annule Garde'],
"Okeoke":
[u'Marque Ombre', u'Telepathe'],
"Hypotrempe":
[u'Glissade', u'Sniper', u'Moiteur'],
"Nymphali":
[u'Joli Sourire', u'Peau Feerique'],
"Venalgue":
[u'Point Poison', u'Toxitouche'],
"Maraiste":
[u'Absorb Eau', u'Moiteur', u'Inconscient'],
"Papilusion":
[u'Oeil Compose', u'Lentiteintee'],
"Charpenti":
[u'Cran', u'Sans Limite', u'Poing de Fer'],
"Doduo":
[u'Fuite', u'Matinal', u'Pied Confus'],
"Coatox":
[u'Anticipation', u'Peau Seche', u'Toxitouche'],
"Charmina":
[u'Force pure', u'Telepathe'],
"Voltali":
[u'Absorb Volt', u'Pied Veloce'],
"Joliflor":
[u'Chlorophyle', u'Coeur Soin'],
"Tarsal":
[u'Synchro', u'Calque', u'Telepathe'],
"Scalpion":
[u'Attention', u'Acharne', u'Pression'],
"Galegon":
[u'Fermete', u'Tete de Roc', u'Heavy Metal'],
"Smogogo":
[u'Levitation'],
"Baudrive":
[u'Boom Final', u'Delestage', u'Rage Brulure'],
"Libegon":
[u'Levitation'],
"Pomdepik":
[u'Fermete', u'Envelocape'],
"Korillon":
[u'Levitation'],
"Boguerisse":
[u'Engrais', u'Pare-balles'],
"Mime Jr.":
[u'Anti-Bruit', u'Filtre', u'Technicien'],
"Queulorior":
[u'Technicien', u'Tempo Perso', u'Lunatique'],
"Ecremeuh":
[u'Isograisse', u'Querelleur', u'Herbivore'],
"Lineon":
[u'Ramassage', u'Gloutonnerie', u'Pied Veloce'],
"Osselait":
[u'Tete de Roc', u'Paratonnerre', u'Armurbaston'],
"Castorno":
[u'Inconscient', u'Simple', u'Lunatique'],
"Hypnomade":
[u'Insomnia', u'Prediction', u'Attention'],
"Lilia":
[u'Ventouse', u'Lavabo'],
"Kranidos":
[u'Brise Moule', u'Sans Limite'],
"Mammochon":
[u'Benet', u'Rideau Neige', u'Isograisse'],
"Moufouette":
[u'Puanteur', u'Boom Final'],
"Miasmax":
[u'Puanteur', u'Armurouillee', u'Boom Final'],
"Aflamanoir":
[u'Gloutonnerie', u'Torche', u'Ecran Fumee'],
"Makuhita":
[u'Isograisse', u'Cran', u'Sans Limite'],
"Cerfrousse":
[u'Intimidation', u'Fouille', u'Herbivore'],
"Alakazam":
[u'Synchro', u'Attention', u'Garde Magik'],
"Reptincel":
[u'Brasier', u'Force Soleil'],
"Carapagos":
[u'Solide Roc', u'Fermete', u'Glissade'],
"Hypocean":
[u'Point Poison', u'Sniper', u'Moiteur'],
"Tortipouss":
[u'Engrais', u'Coque Armure'],
"Stalgamin":
[u'Attention', u'Corps Gel', u'Lunatique'],
"Lancargot":
[u'Essaim', u'Coque Armure', u'Envelocape'],
"Chuchmur":
[u'Anti-Bruit', u'Phobique'],
"Nidoran F":
[u'Point Poison', u'Rivalite', u'Agitation'],
"Nidoran M":
[u'Point Poison', u'Rivalite', u'Agitation'],
"Maganon":
[u'Corps Ardent', u'Esprit Vital'],
"Parecool":
[u'Absenteisme'],
"Wattouat":
[u'Statik'],
"Opermine":
[u'Sniper', u'Griffe Dure', u'Pickpocket'],
"Prinplouf":
[u'Torrent', u'Acharne'],
"Anchwatt":
[u'Levitation'],
"Posipi":
[u'Plus', u'Paratonnerre'],
"Elekid":
[u'Statik', u'Esprit Vital'],
"Flambusard":
[u'Corps Ardent', u'Ailes Bourrasque'],
"Balbuto":
[u'Levitation'],
"Yanma":
[u'Oeil Compose', u'Turbo', u'Fouille'],
"Poichigeon":
[u'Coeur de Coq', u'Chanceux', u'Rivalite'],
"Lamperoie":
[u'Levitation'],
"Kirlia":
[u'Synchro', u'Calque', u'Telepathe'],
"Couaneton":
[u'Regard Vif', u'Coeur de Coq', u'Hydratation'],
"Mystherbe":
[u'Chlorophyle', u'Fuite'],
"Metang":
[u'Corps Sain', u'Light Metal'],
"Tritosor":
[u'Glue', u'Lavabo', u'Force Sable'],
"Dracolosse":
[u'Attention', u'Multiecaille'],
"Fragilady":
[u'Chlorophyle', u'Tempo Perso', u'Feuil. Garde'],
"Genesect":
[u'Telecharge'],
"Nidorino":
[u'Point Poison', u'Rivalite', u'Agitation'],
"Branette":
[u'Insomnia', u'Fouille', u'Corps Maudit'],
"Nidorina":
[u'Point Poison', u'Rivalite', u'Agitation'],
"Rhinoferos":
[u'Paratonnerre', u'Tete de Roc', u'Temeraire'],
"Regigigas":
[u'Debut calme'],
"Tentacruel":
[u'Corps Sain', u'Suintement', u'Cuvette'],
"Chlorobule":
[u'Chlorophyle', u'Tempo Perso', u'Feuil. Garde'],
"Ferosinge":
[u'Esprit Vital', u'Colerique', u'Acharne'],
"Flagadoss":
[u'Benet', u'Tempo Perso', u'Rege-Force'],
"Crikzik":
[u'Mue', u'Fuite'],
"Florges":
[u'Flora-Voile', u'Symbiosis'],
"Scarabrute":
[u'Hyper Cutter', u'Brise Moule', u'Impudence'],
"Mimigal":
[u'Essaim', u'Insomnia', u'Sniper'],
"Dodrio":
[u'Fuite', u'Matinal', u'Pied Confus'],
"Pijako":
[u'Oeil Compose', u'Pied Confus', u'Coeur de Coq'],
"Lepidonille":
[u'Oeil Compose', u'Ecran Poudre', u'Garde Amie'],
"Bargantua":
[u'Temeraire', u'Adaptabilite', u'Brise Moule'],
"Chrysacier":
[u'Mue'],
"Electrode":
[u'Anti-Bruit', u'Statik', u'Boom Final'],
"Sorbebe":
[u'Corps Gel', u'Armurouillee'],
"Givrali":
[u'Rideau Neige', u'Corps Gel'],
"Gloupti":
[u'Suintement', u'Glue', u'Gloutonnerie'],
"Gringolem":
[u'Poing de Fer', u'Maladresse', u'Annule Garde'],
"Miamiasme":
[u'Puanteur', u'Glue', u'Boom Final'],
"Togepi":
[u'Serenite', u'Agitation', u'Chanceux'],
"Corboss":
[u'Insomnia', u'Chanceux', u'Impudence'],
"Flamajou":
[u'Gloutonnerie', u'Brasier'],
"Etourvol":
[u'Intimidation', u'Temeraire'],
"Abo":
[u'Intimidation', u'Mue', u'Tension'],
"Obalie":
[u'Isograisse', u'Corps Gel', u'Benet'],
"Octillery":
[u'Ventouse', u'Sniper', u'Lunatique'],
"Feuillajou":
[u'Gloutonnerie', u'Engrais'],
"Zygarde":
[u'Aura Inversee'],
"Pikachu":
[u'Statik'],
"Zoroark":
[u'Illusion'],
"Nodulithe":
[u'Fermete', u'Force Sable'],
"Rhinastoc":
[u'Paratonnerre', u'Solide Roc', u'Temeraire'],
"Grainipiot":
[u'Chlorophyle', u'Matinal', u'Pickpocket'],
"Qwilfish":
[u'Glissade', u'Point Poison', u'Intimidation'],
"Carchacrok":
[u'Voile Sable', u'Peau Dure'],
"Latios":
[u'Levitation'],
"Groret":
[u'Isograisse', u'Tempo Perso', u'Gloutonnerie'],
"Oniglali":
[u'Attention', u'Corps Gel', u'Lunatique'],
"Steelix":
[u'Tete de roc', u'Fermete', u'Sans Limite'],
"Crefollet":
[u'Levitation'],
"Electhor":
[u'Pression'],
"Phanpy":
[u'Ramassage', u'Voile Sable'],
"Crehelf":
[u'Levitation'],
"Ortide":
[u'Chlorophyle'],
"Metalosse":
[u'Corps Sain', u'Light Metal'],
"Azumarill":
[u'Isograisse', u'Coloforce', u'Herbivore'],
"Kyogre":
[u'Crachin'],
"Scorplane":
[u'Voile sable', u'Hyper Cutter', u'Vaccin'],
"Chenipotte":
[u'Ecran Poudre', u'Fuite'],
"Elektek":
[u'Statik', u'Esprit Vital'],
"Vigoroth":
[u'Esprit Vital'],
"Leveinard":
[u'Medic Nature', u'Serenite', u'Coeur Soin'],
"Fouinar":
[u'Fuite', u'Regard Vif', u'Fouille'],
"Simularbre":
[u'Fermete', u'Tete de Roc', u'Phobique'],
"Polagriffe":
[u'Rideau Neige', u'Glissade'],
"Demeteros":
[u'Force Sable', u'Sans Limite'],
"Maracachi":
[u'Absorb Eau', u'Chlorophyle', u'Lavabo'],
"Dragmara":
[u'Peau Gelee', u'Alerte Neige'],
"Insecateur":
[u'Essaim', u'Technicien', u'Impassible'],
"Laporeille":
[u'Fuite', u'Maladresse', u'Echauffement'],
"Hoot-hoot":
[u'Insomnia', u'Regard Vif', u'Lentiteintee'],
"Lokhlass":
[u'Absorb Eau', u'Coque Armure', u'Hydratation'],
"Spiritomb":
[u'Pression', u'Infiltration'],
"Limagma":
[u'Armumagma', u'Corps Ardent', u'Armurouillee'],
"Paras":
[u'Pose Spore', u'Peau Seche'],
"Pyronille":
[u'Corps Ardent', u'Essaim'],
"Symbios":
[u'Envelocape', u'Garde Magik', u'Rege-Force'],
"Melo":
[u'Joli Sourire', u'Garde Magik', u'Garde Amie'],
"Lianaja":
[u'Engrais', u'Contestation'],
"Arcko":
[u'Engrais', u'Delestage'],
"Archeomire":
[u'Levitation', u'Ignifuge', u'Heavy Metal'],
"Feuforeve":
[u'Levitation'],
"Venipatte":
[u'Point Poison', u'Essaim', u'Pied Veloce'],
"Doudouvet":
[u'Farceur', u'Infiltration', u'Chlorophyle'],
"Lamantine":
[u'Isograisse', u'Hydratation', u'Corps Gel'],
"Parasect":
[u'Pose Spore', u'Peau Seche'],
"Avaltout":
[u'Suintement', u'Glue', u'Gloutonnerie'],
"Motisma":
[u'Levitation'],
"Voltorbe":
[u'Anti-Bruit', u'Statik', u'Boom Final'],
"Magicarpe":
[u'Glissade', u'Phobique'],
"Heledelle":
[u'Cran', u'Querelleur'],
"Noacier":
[u'Epine de Fer'],
"Laggron":
[u'Torrent', u'Moiteur'],
"Gobou":
[u'Torrent', u'Moiteur'],
"Canarticho":
[u'Attention', u'Regard Vif', u'Acharne'],
"Kyurem":
[u'Pression'],
"Groudon":
[u'Secheresse'],
"Blizzaroi":
[u'Alerte Neige', u'Anti-Bruit'],
"Tournegrin":
[u'Chlorophyle', u'Force Soleil', u'Matinal'],
"Nidoqueen":
[u'Point Poison', u'Rivalite', u'Sans Limite'],
"Altaria":
[u'Medic Nature', u'Ciel Gris'],
"Roucool":
[u'Regard vif', u'Pied confus', u'Coeur de Coq'],
"Cradopaud":
[u'Anticipation', u'Peau Seche', u'Toxitouche'],
"Malosse":
[u'Torche', u'Matinal', u'Tension'],
"Vaututrice":
[u'Coeur de Coq', u'Envelocape', u'Armurouillee'],
"Deoxys":
[u'Pression'],
"Meloetta":
[u'Serenite'],
"Togekiss":
[u'Serenite', u'Agitation', u'Chanceux'],
"Tritonde":
[u'Glissade', u'Hydratation', u'Absorb Eau'],
"Moufflair":
[u'Puanteur', u'Boom Final'],
"Tiplouf":
[u'Torrent', u'Acharne'],
"Lumivole":
[u'Benet', u'Lentiteintee', u'Farceur'],
"Carmache":
[u'Voile sable'],
"Cliticlic":
[u'Plus', u'Minus', u'Corps Sain'],
"Poussifeu":
[u'Brasier', u'Turbo'],
"Limaspeed":
[u'Hydratation', u'Glue', u'Delestage'],
"Iguolta":
[u'Peau Seche', u'Voile Sable', u'Force Soleil'],
"Cheniti":
[u'Mue', u'Envelocape'],
"Kapoera":
[u'Intimidation', u'Technicien', u'Impassible'],
"Pachirisu":
[u'Fuite', u'Ramassage', u'Absorb Volt'],
"Marill":
[u'Isograisse', u'Coloforce', u'Herbivore'],
"Skitty":
[u'Joli Sourire', u'Normalise'],
"Abra":
[u'Synchro', u'Attention', u'Garde Magik'],
"Couverdure":
[u'Feuil. Garde', u'Chlorophyle', u'Envelocape'],
"Grodoudou":
[u'Joli Sourire', u'Battant', u'Fouille'],
"Ptyranidur":
[u'Prognathe'],
"Kecleon":
[u'Deguisement', u'Proteen'],
"Crustabri":
[u'Coque Armure', u'Multi-Coups', u'Envelocape'],
"Galvaran":
[u'Peau Seche', u'Voile Sable', u'Force Soleil'],
"Fluvetin":
[u'Coeur Soin', u'Aroma-Voile'],
"Haydaim":
[u'Chlorophyle', u'Herbivore', u'Serenite'],
"Hippopotas":
[u'Sable Volant', u'Force Sable'],
"Coconfort":
[u'Mue'],
"Noeunoeuf":
[u'Chlorophyle', u'Recolte'],
"Zigzaton":
[u'Ramassage', u'Gloutonnerie', u'Pied Veloce'],
"Rattata":
[u'Cran', u'Fuite', u'Agitation'],
"Girafarig":
[u'Attention', u'Matinal', u'Herbivore'],
"Otaria":
[u'Isograisse', u'Hydratation', u'Corps Gel'],
"Granbull":
[u'Pied Veloce', u'Intimidation', u'Phobique'],
"Kabutops":
[u'Glissade', u'Armurbaston', u'Armurouillee'],
"Ratentif":
[u'Fuite', u'Regard Vif', u'Analyste'],
"Bulbizarre":
[u'Engrais', u'Chlorophyle'],
"Couafarel":
[u'Toison Epaisse'],
"Siderella":
[u'Fouille', u'Marque Ombre'],
"Dedenne":
[u'Ramassage', u'Bajoues', u'Plus'],
"Herbizarre":
[u'Engrais', u'Chlorophyle'],
"Lixy":
[u'Intimidation', u'Rivalite', u'Cran'],
"Roucarnage":
[u'Regard Vif', u'Pied Confus', u'Coeur de Coq'],
"Tarinor":
[u'Fermete', u'Magnepiege', u'Force Sable'],
"Rapasdepic":
[u'Regard Vif', u'Sniper'],
"Embrylex":
[u'Cran'],
"Togetic":
[u'Serenite', u'Agitation', u'Chanceux'],
"Brouhabam":
[u'Anti-Bruit', u'Querelleur'],
"Babimanta":
[u'Glissade', u'Absorb Eau'],
"Rhinolove":
[u'Inconscient', u'Maladresse', u'Simple'],
"Florizarre":
[u'Engrais', u'Chlorophyle'],
"Clamiral":
[u'Torrent', u'Coque Armure'],
"Ronflex":
[u'Vaccin', u'Isograisse', u'Gloutonnerie'],
"Grotadmorv":
[u'Puanteur', u'Glue', u'Toxitouche'],
"Ptitard":
[u'Absorb Eau', u'Moiteur', u'Glissade'],
"Mentali":
[u'Synchro', u'Miroir Magik'],
"Betochef":
[u'Cran', u'Sans Limite', u'Poing de Fer'],
"Stari":
[u'Medic Nature', u'Lumiattirance', u'Analyste'],
"Arkeapti":
[u'Defaitiste'],
"Crocorible":
[u'Intimidation', u'Impudence', u'Colerique'],
"Heatran":
[u'Torche', u'Corps Ardent'],
"Ponyta":
[u'Fuite', u'Torche', u'Corps Ardent'],
"Crefadet":
[u'Levitation'],
"Escroco":
[u'Intimidation', u'Impudence', u'Colerique'],
"Hariyama":
[u'Isograisse', u'Cran', u'Sans Limite'],
"Qulbutoke":
[u'Marque Ombre', u'Telepathe'],
"Staross":
[u'Medic Nature', u'Lumiattirance', u'Analyste'],
"Hexagel":
[u'Levitation'],
"Lippouti":
[u'Benet', u'Prediction', u'Hydratation'],
"Exagide":
[u'Declic Tactique'],
"Bastiodon":
[u'Fermete', u'Anti-Bruit'],
"Peregrain":
[u'Mue', u'Garde Amie'],
"Carvanha":
[u'Peau Dure'],
"Pharamp":
[u'Statik'],
"Bouldeneu":
[u'Chlorophyle', u'Feuil. Garde', u'Rege-Force'],
"Heliatronc":
[u'Chlorophyle', u'Force Soleil', u'Matinal'],
"Gamblast":
[u'Mega Blaster'],
"Eoko":
[u'Levitation'],
"Brutalibre":
[u'Echauffement', u'Delestage', u'Brise Moule'],
"Furaiglon":
[u'Regard Vif', u'Sans Limite', u'Agitation'],
"Chevroum":
[u'Herbivore'],
"Flamoutan":
[u'Gloutonnerie', u'Brasier'],
"Prismillon":
[u'Oeil Compose', u'Ecran Poudre', u'Garde Amie'],
"Sonistrelle":
[u'Fouille', u'Infiltration', u'Telepathe'],
"Goupix":
[u'Torche', u'Secheresse'],
"Gravalanch":
[u'Tete de Roc', u'Fermete'],
"Nostenfer":
[u'Attention', u'Infiltration'],
"Chetiflor":
[u'Chlorophyle', u'Gloutonnerie'],
"Lumineon":
[u'Lavabo'],
"Croaporal":
[u'Torrent', u'Proteen'],
"Rhinocorne":
[u'Paratonnerre', u'Tete de Roc', u'Temeraire'],
"Leviator":
[u'Intimidation', u'Impudence'],
"Cryptero":
[u'Peau Miracle', u'Garde Magik', u'Lentiteintee'],
"Spoink":
[u'Isograisse', u'Tempo Perso'],
"Dialga":
[u'Pression', u'Telepathe'],
"Sabelette":
[u'Voile Sable', u'Baigne Sable'],
"Dynavolt":
[u'Paratonnerre', u'Statik'],
"Pichu":
[u'Statik', u'Paratonnerre'],
"Terrakium":
[u'Coeur Noble'],
"Amagara":
[u'Peau Gelee'],
"Poissirene":
[u'Glissade', u'Ignifu-Voile'],
"Magby":
[u'Corps Ardent', u'Esprit Vital'],
"Farfaduvet":
[u'Farceur', u'Infiltration', u'Chlorophyle'],
"Lockpin":
[u'Joli Sourire', u'Maladresse', u'Echauffement'],
"Loupio":
[u'Absorb Volt', u'Lumiattirance', u'Absorb Eau'],
"Elecsprint":
[u'Paratonnerre', u'Statik', u'Minus'],
"Keldeo":
[u'Coeur Noble'],
"Jungko":
[u'Engrais', u'Delestage'],
"Registeel":
[u'Corps Sain', u'Light Metal'],
"Xatu":
[u'Synchro', u'Matinal', u'Miroir Magik'],
"Skelenox":
[u'Levitation'],
"Etourmi":
[u'Regard Vif'],
"Aeromite":
[u'Ecran Poudre', u'Lentiteintee'],
"Tortank":
[u'Torrent', u'Cuvette'],
"Minidraco":
[u'Mue', u'Ecaille Speciale'],
"Trioxhydre":
[u'Levitation'],
"Melofee":
[u'Joli Sourire', u'Garde Magik', u'Garde Amie'],
"Crabicoque":
[u'Fermete', u'Coque Armure', u'Armurouillee'],
"Torterra":
[u'Engrais', u'Coque Armure'],
"Rototaupe":
[u'Baigne Sable', u'Force Sable', u'Brise Moule'],
"Ceribou":
[u'Chlorophyle'],
"Keunotor":
[u'Simple', u'Inconscient', u'Lunatique'],
"Helionceau":
[u'Tension', u'Rivalite', u'Impudence'],
"Entei":
[u'Pression', u'Torche'],
"Moustillon":
[u'Torrent', u'Coque Armure'],
"Mygavolt":
[u'Oeil compose', u'Tension', u'Essaim'],
"Soporifik":
[u'Insomnia', u'Prediction', u'Attention'],
"Dimocles":
[u'Annule Garde'],
"Riolu":
[u'Attention', u'Impassible', u'Farceur'],
"Fulguris":
[u'Farceur', u'Acharne'],
"Aspicot":
[u'Ecran Poudre', u'Fuite'],
"Marcacrin":
[u'Rideau Neige'],
"Mysdibule":
[u'Hyper Cutter', u'Intimidation', u'Sans Limite'],
"Chartor":
[u'Ecran Fumee', u'Coque Armure'],
"Minotaupe":
[u'Baigne Sable', u'Force Sable', u'Brise Moule'],
"Maskadra":
[u'Intimidation', u'Tension'],
"Yanmega":
[u'Turbo', u'Lentiteintee', u'Fouille'],
"Melokrik":
[u'Essaim', u'Technicien'],
"Scobolide":
[u'Point Poison', u'Essaim', u'Turbo'],
"Massko":
[u'Engrais', u'Delestage'],
"Brasegali":
[u'Brasier', u'Turbo'],
"Sepiatroce":
[u'Ventouse', u'Contestation'],
"Vostourno":
[u'Coeur de Coq', u'Envelocape', u'Armurouillee'],
"Ossatueur":
[u'Tete de Roc', u'Paratonnerre', u'Armurbaston'],
"Cabriolaine":
[u'Herbivore'],
"Lombre":
[u'Glissade', u'Cuvette'],
"Apitrini":
[u'Cherche Miel', u'Agitation'],
"Nirondelle":
[u'Cran', u'Querelleur'],
"Chinchidou":
[u'Joli Sourire', u'Technicien', u'Multi-Coups'],
"Arceus":
[u'Multitype'],
"Kadabra":
[u'Synchro', u'Attention', u'Garde Magik'],
"Regirock":
[u'Corps Sain', u'Fermete'],
"Tarpaud":
[u'Absorb Eau', u'Moiteur', u'Crachin'],
"Sapereau":
[u'Ramassage', u'Bajoues', u'Coloforce'],
"Cacturne":
[u'Voile Sable', u'Absorb Eau'],
"Raichu":
[u'Statik', u'Paratonnerre'],
"Poissoroy":
[u'Glissade', u'Ignifu-Voile', u'Paratonnerre'],
"Vibraninf":
[u'Levitation'],
"Vacilys":
[u'Ventouse', u'Lavabo'],
"Vivaldaim":
[u'Chlorophyle', u'Herbivore', u'Serenite'],
"Tadmorv":
[u'Puanteur', u'Glue', u'Toxitouche'],
"Zarbi":
[u'Levitation'],
"Galifeu":
[u'Brasier', u'Turbo'],
"Dardargnan":
[u'Essaim', u'Sniper'],
"Polarhume":
[u'Rideau Neige', u'Phobique'],
"Tylton":
[u'Medic Nature', u'Ciel Gris'],
"Roitiflam":
[u'Brasier', u'Temeraire'],
"Manternel":
[u'Essaim', u'Chlorophyle', u'Envelocape'],
"Cornebre":
[u'Insomnia', u'Chanceux', u'Farceur'],
"Terhal":
[u'Corps Sain', u'Light Metal'],
"Shaofouine":
[u'Rege-Force', u'Attention', u'Temeraire'],
"Papilord":
[u'Essaim', u'Lentiteintee'],
"Boreas":
[u'Farceur', u'Acharne'],
"Fantominus":
[u'Levitation'],
"Lakmecygne":
[u'Regard Vif', u'Coeur de Coq', u'Hydratation'],
"Banshitrouye":
[u'Ramassage', u'Fouille', u'Insomnia'],
"Kraknoix":
[u'Hyper Cutter', u'Piege', u'Sans Limite'],
"Leuphorie":
[u'Medic nature', u'Serenite', u'Coeur Soin'],
"Boskara":
[u'Engrais', u'Coque Armure'],
"Charkos":
[u'Brise Moule', u'Sans Limite'],
"Gigalithe":
[u'Fermete', u'Force Sable'],
"Roucoups":
[u'Regard Vif', u'Pied Confus', u'Coeur de Coq'],
"Ecayon":
[u'Lavabo', u'Glissade', u'Ignifu-voile'],
"Statitik":
[u'Oeil Compose', u'Tension', u'Essaim'],
"Teraclope":
[u'Pression'],
"Aquali":
[u'Absorb Eau', u'Hydratation'],
"Geolithe":
[u'Fermete', u'Force Sable'],
"Draco":
[u'Mue', u'Ecaille Speciale'],
"Magnezone":
[u'Fermete', u'Magnepiege', u'Analyste'],
"Roselia":
[u'Medic Nature', u'Point Poison', u'Feuil. Garde'],
"Monaflemit":
[u'Absenteisme'],
"Spinda":
[u'Tempo Perso', u'Pied Confus', u'Contestation'],
"Tartard":
[u'Absorb Eau', u'Moiteur', u'Glissade'],
"Palkia":
[u'Pression', u'Telepathe'],
"Darumarond":
[u'Agitation', u'Attention'],
"Munna":
[u'Prediction', u'Synchro', u'Telepathe'],
"Tauros":
[u'Intimidation', u'Colerique', u'Sans Limite'],
"Etouraptor":
[u'Intimidation', u'Temeraire'],
"Frison":
[u'Temeraire', u'Herbivore', u'Anti-Bruit'],
"Raikou":
[u'Pression', u'Absorb Volt'],
"Pingoleon":
[u'Torrent', u'Acharne'],
"Hericendre":
[u'Brasier', u'Torche'],
"Arbok":
[u'Intimidation', u'Mue', u'Tension'],
"Mesmerella":
[u'Fouille', u'Battant', u'Marque Ombre'],
"Chimpenfeu":
[u'Brasier', u'Poing de Fer'],
"Psykokwak":
[u'Moiteur', u'Ciel Gris', u'Glissade'],
"Boustiflor":
[u'Chlorophyle', u'Gloutonnerie'],
"Porygon2":
[u'Calque', u'Telecharge', u'Analyste'],
"Kaimorse":
[u'Isograisse', u'Corps Gel', u'Benet'],
"Akwakwak":
[u'Moiteur', u'Ciel Gris', u'Glissade'],
"Tygnon":
[u'Regard Vif', u'Poing de Fer', u'Attention'],
"Goinfrex":
[u'Ramassage', u'Isograisse', u'Gloutonnerie'],
"Griknot":
[u'Voile sable'],
"Sucroquin":
[u'Gluco-Voile', u'Delestage'],
"Escargaume":
[u'Hydratation', u'Coque Armure', u'Envelocape'],
"Monorpale":
[u'Annule Garde'],
"Goupelin":
[u'Brasier', u'Magicien'],
"Tenefix":
[u'Regard Vif', u'Frein', u'Farceur'],
"Mustebouee":
[u'Glissade'],
"Nosferalto":
[u'Attention', u'Infiltration'],
"Judokrak":
[u'Cran', u'Attention', u'Brise Moule'],
"Relicanth":
[u'Glissade', u'Tete de Roc', u'Fermete'],
"Mushana":
[u'Prediction', u'Synchro', u'Telepathe'],
"Ptiravi":
[u'Medic Nature', u'Serenite', u'Garde Amie'],
"Coquiperl":
[u'Coque Armure', u'Phobique'],
"Ohmassacre":
[u'Levitation'],
"Brocelome":
[u'Medic Nature', u'Fouille', u'Recolte'],
"Rozbouton":
[u'Medic Nature', u'Point Poison', u'Feuil. Garde'],
"Scalproie":
[u'Attention', u'Acharne', u'Pression'],
"Phogleur":
[u'Isograisse', u'Corps Gel', u'Benet'],
"Neitram":
[u'Telepathe', u'Synchro', u'Analyste'],
"Chovsourir":
[u'Inconscient', u'Maladresse', u'Simple'],
"Musteflott":
[u'Glissade'],
"Insolourdo":
[u'Serenite', u'Fuite', u'Phobique'],
"Munja":
[u'Garde Mystik'],
"Drakkarmin":
[u'Peau Dure', u'Sans Limite', u'Brise Moule'],
"Sorbouboul":
[u'Corps Gel', u'Armurouillee'],
"Zekrom":
[u'Tera-Voltage'],
"Remoraid":
[u'Agitation', u'Sniper', u'Lunatique'],
"Mamanbo":
[u'Hydratation', u'Coeur Soin', u'Rege-Force'],
"Meios":
[u'Envelocape', u'Garde Magik', u'Rege-Force'],
"Noctali":
[u'Synchro', u'Attention'],
"Ramoloss":
[u'Benet', u'Tempo Perso', u'Rege-Force'],
"Cupcanaille":
[u'Gluco-Voile', u'Delestage'],
"Carabaffe":
[u'Torrent', u'Cuvette'],
"Barbicha":
[u'Benet', u'Anticipation', u'Hydratation'],
"Colombeau":
[u'Coeur de Coq', u'Chanceux', u'Rivalite'],
"Baggaid":
[u'Mue', u'Impudence', u'Intimidation'],
"Pitrouille":
[u'Ramassage', u'Fouille', u'Insomnia'],
"Ramboum":
[u'Anti-Bruit', u'Querelleur'],
"Kicklee":
[u'Echauffement', u'Temeraire', u'Delestage'],
"Teddiursa":
[u'Ramassage', u'Pied Veloce', u'Cherche Miel'],
"Karaclee":
[u'Fermete', u'Attention', u'Brise Moule'],
"Serpang":
[u'Glissade', u'Ignifu-Voile'],
"Porygon":
[u'Calque', u'Telecharge', u'Analyste'],
"Mastouffe":
[u'Intimidation', u'Baigne Sable', u'Querelleur'],
"Pyrax":
[u'Corps Ardent', u'Essaim'],
"Majaspic":
[u'Engrais', u'Contestation'],
"Blindalys":
[u'Mue'],
"Nenupiot":
[u'Glissade', u'Cuvette'],
"Foretress":
[u'Fermete', u'Envelocape'],
"Mimitoss":
[u'Oeil Compose', u'Lentiteintee', u'Fuite'],
"Lippoutou":
[u'Benet', u'Prediction', u'Peau Seche'],
"Negapi":
[u'Minus'],
"Colimucus":
[u'Hydratation', u'Herbivore', u'Poisseux'],
"Ouisticram":
[u'Brasier', u'Poing de Fer'],
"Gruikui":
[u'Brasier', u'Isograisse'],
"Gallame":
[u'Impassible'],
"Flotajou":
[u'Gloutonnerie', u'Torrent'],
"Pandespiegle":
[u'Brise Moule', u'Poing de Fer', u'Querelleur'],
"Muplodocus":
[u'Hydratation', u'Herbivore', u'Poisseux'],
"Blindepique":
[u'Engrais', u'Pare-balles'],
"Melancolux":
[u'Torche', u'Corps Ardent', u'Infiltration'],
"Viridium":
[u'Coeur Noble'],
"Fouinette":
[u'Fuite', u'Regard Vif', u'Fouille'],
"Desseliande":
[u'Medic Nature', u'Fouille', u'Recolte'],
"Seviper":
[u'Mue', u'Infiltration'],
"Germignon":
[u'Engrais', u'Feuil. Garde'],
"Ponchiot":
[u'Esprit Vital', u'Ramassage', u'Fuite'],
"Typhlosion":
[u'Brasier', u'Torche'],
"Feunard":
[u'Torche', u'Secheresse'],
"Magneti":
[u'Magnepiege', u'Fermete', u'Analyste'],
"Cobaltium":
[u'Coeur Noble'],
"Persian":
[u'Echauffement', u'Technicien', u'Tension'],
"Nidoking":
[u'Point Poison', u'Rivalite', u'Sans Limite'],
"Ninjask":
[u'Turbo', u'Infiltration'],
"Amphinobi":
[u'Torrent', u'Proteen'],
"Nemelios":
[u'Rivalite', u'Tension', u'Impudence'],
"Medhyena":
[u'Fuite', u'Pied Veloce', u'Phobique'],
"Evoli":
[u'Fuite', u'Adaptabilite', u'Anticipation'],
"Barloche":
[u'Benet', u'Anticipation', u'Hydratation'],
"Kabuto":
[u'Glissade', u'Armurbaston', u'Armurouillee'],
"Grenousse":
[u'Torrent', u'Proteen'],
"Kaorine":
[u'Levitation'],
"Debugant":
[u'Cran', u'Impassible', u'Esprit Vital'],
"Ningale":
[u'Oeil Compose'],
"Capidextre":
[u'Ramassage', u'Technicien', u'Multi-Coups'],
"Tic":
[u'Plus', u'Minus', u'Corps Sain'],
"Piafabec":
[u'Regard Vif', u'Sniper'],
"Camerupt":
[u'Armumagma', u'Solide Roc', u'Colerique'],
"Goelise":
[u'Regard Vif', u'Cuvette'],
"Funecire":
[u'Torche', u'Corps Ardent', u'Marque Ombre'],
"Golgopathe":
[u'Sniper', u'Griffe Dure', u'Pickpocket'],
"Reshiram":
[u'TurboBrasier'],
"Excelangue":
[u'Benet', u'Tempo Perso', u'Ciel Gris'],
"Tetarte":
[u'Absorb Eau', u'Moiteur', u'Glissade'],
"Flingouste":
[u'Mega Blaster'],
"Aligatueur":
[u'Torrent', u'Sans Limite'],
"Magireve":
[u'Levitation'],
"Luxray":
[u'Rivalite', u'Intimidation', u'Cran'],
"Rosabyss":
[u'Glissade', u'Hydratation'],
"Galekid":
[u'Fermete', u'Tete de Roc', u'Heavy Metal'],
"Ptera":
[u'Tete de Roc', u'Pression', u'Tension'],
"Galopa":
[u'Fuite', u'Torche', u'Corps Ardent'],
"Roigada":
[u'Benet', u'Tempo Perso', u'Rege-Force'],
"Jirachi":
[u'Serenite'],
"Marisson":
[u'Engrais', u'Pare-balles'],
"Mascaiman":
[u'Intimidation', u'Impudence', u'Colerique'],
"Carapuce":
[u'Torrent', u'Cuvette'],
"Mangriff":
[u'Vaccin', u'Rage Poison'],
"Latias":
[u'Levitation'],
"Grahyena":
[u'Intimidation', u'Pied Veloce', u'Impudence'],
"Lugia":
[u'Pression', u'Multiecaille'],
"Onix":
[u'Tete de Roc', u'Fermete', u'Armurouillee'],
"Pyroli":
[u'Torche', u'Cran'],
"Magneton":
[u'Magnepiege', u'Fermete', u'Analyste'],
"Incisache":
[u'Rivalite', u'Brise Moule', u'Tension'],
"Kokiyas":
[u'Coque Armure', u'Multi-Coups', u'Envelocape'],
"Racaillou":
[u'Tete de Roc', u'Fermete', u'Voile Sable'],
"Colhomard":
[u'Hyper Cutter', u'Coque Armure', u'Adaptabilite'],
"Papinox":
[u'Ecran Poudre'],
"Manaphy":
[u'Hydratation'],
"Crocrodil":
[u'Torrent', u'Sans Limite'],
"Ectoplasma":
[u'Levitation'],
"Nucleos":
[u'Envelocape', u'Garde Magik', u'Rege-Force'],
"Vortente":
[u'Levitation'],
"Ecrapince":
[u'Hyper Cutter', u'Coque Armure', u'Adaptabilite'],
"Coxyclaque":
[u'Essaim', u'Matinal', u'Poing de Fer'],
"Lugulabre":
[u'Torche', u'Corps Ardent', u'Marque Ombre'],
"Moyade":
[u'Absorb Eau', u'Corps Maudit', u'Moiteur'],
"Delcatty":
[u'Joli Sourire', u'Normalise'],
"Floette":
[u'Flora-Voile', u'Symbiosis'],
"Tutankafer":
[u'Momie'],
"Meditikka":
[u'Force Pure', u'Telepathe'],
"Nanmeouie":
[u'Coeur Soin', u'Rege-Force', u'Maladresse'],
"Feunnec":
[u'Brasier', u'Magicien'],
"Archeodong":
[u'Levitation', u'Ignifuge', u'Heavy Metal'],
"Axoloto":
[u'Absorb Eau', u'Moiteur', u'Inconscient'],
"Macronium":
[u'Engrais', u'Feuil. Garde'],
"Rafflesia":
[u'Chlorophyle'],
"Caratroc":
[u'Fermete', u'Gloutonnerie', u'Contestation'],
"Ponchien":
[u'Intimidation', u'Baigne Sable', u'Querelleur'],
"Pifeuil":
[u'Chlorophyle', u'Matinal', u'Pickpocket'],
"Toudoudou":
[u'Joli sourire', u'Battant', u'Garde Amie'],
"Sablaireau":
[u'Voile Sable', u'Baigne Sable'],
"Draby":
[u'Tete de Roc', u'Sans Limite'],
"Rayquaza":
[u'Air Lock'],
"Granivol":
[u'Chlorophyle', u'Feuil. Garde', u'Infiltration'],
"Luxio":
[u'Intimidation', u'Rivalite', u'Cran'],
"Ceriflor":
[u'Don Floral'],
"Dimoret":
[u'Pression', u'Pickpocket'],
"Amonita":
[u'Glissade', u'Coque Armure', u'Armurouillee'],
"Larveyette":
[u'Essaim', u'Chlorophyle', u'Envelocape'],
"Krabboss":
[u'Hyper Cutter', u'Coque Armure', u'Sans Limite'],
"Batracne":
[u'Glissade', u'Hydratation', u'Absorb Eau'],
"Tentacool":
[u'Corps Sain', u'Suintement', u'Cuvette'],
"Hippodocus":
[u'Sable Volant', u'Force Sable'],
"Wailmer":
[u'Ignifu-Voile', u'Benet'],
"Magmar":
[u'Corps Ardent', u'Esprit Vital'],
"Caninos":
[u'Torche', u'Intimidation'],
"Seleroc":
[u'Levitation'],
"Lucario":
[u'Attention', u'Impassible', u'Coeur Noble'],
"Machopeur":
[u'Cran', u'Annule Garde', u'Impassible'],
"Barpau":
[u'Glissade', u'Benet', u'Adaptabilite'],
"Armulys":
[u'Mue'],
"Drascore":
[u'Armurbaston', u'Sniper', u'Regard Vif'],
"Darumacho":
[u'Sans Limite', u'Mode Transe'],
"Coudlangue":
[u'Benet', u'Tempo Perso', u'Ciel Gris'],
"Tarinorme":
[u'Fermete', u'Magnepiege', u'Force Sable'],
"Lovdisc":
[u'Glissade', u'Hydratation'],
"Saquedeneu":
[u'Chlorophyle', u'Feuil. Garde', u'Rege-Force'],
"Tengalice":
[u'Chlorophyle', u'Matinal', u'Pickpocket'],
"Golemastoc":
[u'Poing de Fer', u'Maladresse', u'Annule Garde'],
"Diamat":
[u'Agitation'],
"Phyllali":
[u'Feuil. Garde', u'Chlorophyle'],
"Mistigrix":
[u'Regard Vif', u'Infiltration', u'Farceur', u'Battant'],
# [u'Regard Vif', u'Infiltration', u'Farceur(M)/Battant(F)'],
"Grotichon":
[u'Brasier', u'Isograisse'],
"Tropius":
[u'Chlorophyle', u'Force Soleil', u'Recolte'],
"Chapignon":
[u'Pose Spore', u'Soin Poison', u'Technicien'],
"Victini":
[u'Victorieux'],
"Ymphect":
[u'Mue'],
"Artikodin":
[u'Pression', u'Rideau Neige'],
"Phione":
[u'Hydratation'],
"Miaouss":
[u'Ramassage', u'Technicien', u'Tension'],
"Braisillon":
[u'Corps Ardent', u'Ailes Bourrasque'],
"Giratina":
[u'Levitation', u'Pression', u'Telepathe'],
"Migalos":
[u'Essaim', u'Insomnia', u'Sniper'],
"Manzai":
[u'Tete de roc', u'Fermete', u'Phobique'],
"Nosferapti":
[u'Attention', u'Infiltration'],
"Arakdo":
[u'Glissade', u'Cuvette'],
"Kaiminus":
[u'Torrent', u'Sans Limite'],
"Charmillon":
[u'Essaim', u'Rivalite'],
"Zebibron":
[u'Paratonnerre', u'Motorise', u'Herbivore'],
"Coupenotte":
[u'Rivalite', u'Brise Moule', u'Tension'],
"Muciole":
[u'Lumiattirance', u'Essaim', u'Farceur'],
"Cizayox":
[u'Essaim', u'Technicien', u'Light Metal'],
"Triopikeur":
[u'Voile Sable', u'Piege', u'Force Sable'],
"Floravol":
[u'Chlorophyle', u'Feuil. Garde', u'Infiltration'],
"Ouvrifier":
[u'Cran', u'Sans Limite', u'Poing de Fer'],
"Darkrai":
[u'Mauvais Reve'],
"Mew":
[u'Synchro'],
"Grindur":
[u'Epine de Fer'],
"Balignon":
[u'Pose Spore', u'Soin Poison', u'Pied Veloce'],
"Kravarech":
[u'Point Poison', u'Toxitouche'],
"Chaglam":
[u'Echauffement', u'Tempo perso', u'Regard Vif'],
"Xerneas":
[u'Aura Feerique'],
"Cadoizo":
[u'Esprit Vital', u'Agitation'],
"Salameche":
[u'Brasier', u'Force Soleil'],
"Lanturn":
[u'Absorb Volt', u'Lumiattirance', u'Absorb Eau'],
"Simiabraz":
[u'Brasier', u'Poing de Fer'],
"Bruyverne":
[u'Fouille', u'Infiltration', u'Telepathe'],
"Mucuscule":
[u'Hydratation', u'Herbivore', u'Poisseux'],
"Chaffreux":
[u'Isograisse', u'Tempo perso', u'Acharne'],
"Aeropteryx":
[u'Defaitiste'],
"Farfuret":
[u'Attention', u'Regard Vif', u'Pickpocket'],
"Cotovol":
[u'Chlorophyle', u'Feuil. Garde', u'Infiltration'],
"Rondoudou":
[u'Joli Sourire', u'Battant', u'Garde Amie'],
"Sorboul":
[u'Corps Gel', u'Armurouillee'],
"Amonistar":
[u'Glissade', u'Coque Armure', u'Armurouillee'],
"Clic":
[u'Plus', u'Minus', u'Corps Sain'],
"Meganium":
[u'Engrais', u'Feuil. Garde'],
"Viskuse":
[u'Absorb Eau', u'Corps Maudit', u'Moiteur'],
"Metamorph":
[u'Echauffement', u'Imposteur'],
"Kangourex":
[u'Matinal', u'Querelleur', u'Attention'],
"Wailord":
[u'Ignifu-Voile', u'Benet'],
"Colossinge":
[u'Esprit Vital', u'Colerique', u'Acharne'],
"Yveltal":
[u'Aura Tenebreuse'],
"Corayon":
[u'Agitation', u'Medic Nature'],
"Mackogneur":
[u'Cran', u'Annule Garde', u'Impassible'],
"Rapion":
[u'Armurbaston', u'Sniper', u'Regard Vif'],
"Feuiloutan":
[u'Gloutonnerie', u'Engrais'],
"Ursaring":
[u'Cran', u'Pied Veloce', u'Tension'],
"Anorith":
[u'Armurbaston', u'Glissade'],
"Vipelierre":
[u'Engrais', u'Contestation'],
"Gardevoir":
[u'Synchro', u'Calque', u'Telepathe'],
"Scarhino":
[u'Cran', u'Essaim', u'Impudence'],
"Demolosse":
[u'Torche', u'Matinal', u'Tension'],
"Crapustule":
[u'Glissade', u'Toxitouche', u'Absorb Eau'],
"Crabaraque":
[u'Fermete', u'Coque Armure', u'Armurouillee'],
"Tranchodon":
[u'Rivalite', u'Brise Moule', u'Tension'],
"Mewtwo":
[u'Pression', u'Tension'],
"Feurisson":
[u'Brasier', u'Torche'],
"Galeking":
[u'Fermete', u'Tete de Roc', u'Heavy Metal'],
"Miradar":
[u'Lumiattirance', u'Regard Vif', u'Analyste'],
"Tyranocif":
[u'Sable Volant', u'Tension'],
"Scorvol":
[u'Hyper Cutter', u'Voile Sable', u'Soin Poison'],
"Demanta":
[u'Glissade', u'Absorb Eau'],
"Solaroc":
[u'Levitation'],
"Passerouge":
[u'Coeur de Coq', u'Ailes Bourrasque'],
"Flobio":
[u'Torrent', u'Moiteur'],
"Cochignon":
[u'Rideau Neige'],
"Roserade":
[u'Medic Nature', u'Point Poison', u'Technicien'],
"Chamallot":
[u'Benet', u'Simple'],
"Chacripan":
[u'Echauffement', u'Delestage', u'Farceur'],
"Psystigri":
[u'Infiltration', u'Regard Vif', u'Tempo Perso'],
"Scrutella":
[u'Fouille', u'Battant', u'Marque Ombre'],
"Kungfouine":
[u'Rege-Force', u'Attention', u'Temeraire'],
"Momartik":
[u'Rideau Neige', u'Corps Maudit'],
"Leopardus":
[u'Echauffement', u'Delestage', u'Farceur'],
"Ho-Oh":
[u'Pression', u'Rege-Force'],
"Krabby":
[u'Hyper Cutter', u'Coque Armure', u'Sans Limite'],
"Suicune":
[u'Pression', u'Absorb Eau'],
"Zeblitz":
[u'Paratonnerre', u'Motorise', u'Herbivore'],
"Excavarenne":
[u'Bajoues', u'Ramassage', u'Coloforce'],
"Donphan":
[u'Fermete', u'Voile Sable'],
"Grelacon":
[u'Tempo Perso', u'Corps Gel', u'Fermete'],
"Blizzi":
[u'Alerte Neige', u'Anti-Bruit'],
"Strassie":
[u'Corps Sain', u'Fermete'],
"Trousselin":
[u'Farceur', u'Magicien'],
"Morpheo":
[u'Meteo'],
"Airmure":
[u'Fermete', u'Regard Vif', u'Armurouillee'],
"M. Mime":
[u'Anti-Bruit', u'Filtre', u'Technicien'],
"Natu":
[u'Synchro', u'Matinal', u'Miroir Magik'],
"Shaymin":
[u'Medic Nature'],
"Lainergie":
[u'Statik'],
"Coxy":
[u'Essaim', u'Matinal', u'Phobique'],
"Cacnea":
[u'Voile Sable', u'Absorb Eau'],
"Smogo":
[u'Levitation'],
"Arcanin":
[u'Intimidation', u'Torche', u'Coeur Noble'],
"Milobellus":
[u'Ecaille Speciale', u'Battant', u'Joli Sourire'],
"Taupiqueur":
[u'Voile Sable', u'Piege', u'Force Sable'],
"Capumain":
[u'Fuite', u'Ramassage', u'Multi-Coups'],
"Machoc":
[u'Cran', u'Annule Garde', u'Impassible'],
"Ludicolo":
[u'Glissade', u'Cuvette'],
"Noarfang":
[u'Insomnia', u'Regard Vif', u'Lentiteintee'],
"Sepiatop":
[u'Ventouse', u'Contestation', u'Infiltration'],
"Fermite":
[u'Essaim', u'Agitation', u'Absenteisme'],
"Regice":
[u'Corps Sain', u'Corps Gel'],
"Armaldo":
[u'Armurbaston', u'Glissade'],
"Lewsor":
[u'Telepathe', u'Synchro', u'Analyste'],
"Sancoki":
[u'Glue', u'Lavabo', u'Force Sable'],
"Trompignon":
[u'Pose Spore', u'Rege-Force'],
"Empiflor":
[u'Chlorophyle', u'Gloutonnerie'],
"Drackhaus":
[u'Tete de Roc', u'Envelocape'],
"Chenipan":
[u'Ecran Poudre', u'Fuite'],
"Limonde":
[u'Statik', u'Echauffement', u'Voile Sable'],
"Grodrive":
[u'Boom Final', u'Delestage', u'Rage Brulure'],
"Flabebe":
[u'Flora-Voile', u'Symbiosis'],
"Brutapode":
[u'Point Poison', u'Essaim', u'Pied Veloce'],
"Deflaisan":
[u'Chanceux', u'Coeur de Coq', u'Rivalite'],
"Spectrum":
[u'Levitation'],
"Pandarbare":
[u'Poing de Fer', u'Brise Moule', u'Querelleur'],
"Rexillius":
[u'Prognathe'],
"Sulfura":
[u'Pression', u'Corps Ardent'],
"Drattak":
[u'Intimidation', u'Impudence'],
"Seracrawl":
[u'Tempo Perso', u'Corps Gel', u'Fermete'],
"Megapagos":
[u'Solide Roc', u'Fermete', u'Glissade'],
}


main(types, megatypes, caracs, talents)
# -*- coding: utf-8 -*- 

def main():
    mapping = []
    even = False
    es_name = ""
    for row in data.split("\n"):
        if not even:
            es_name = row
            even = True
            continue
        
        even = False
        
        name = row.split("\t")[0].strip()
        desc = row.split("\t")[1].strip()
        
        std_name = name.strip()\
        .lower()\
        .replace(" ", "_")\
        .replace("-", "_")\
        .replace("(", "")\
        .replace(")", "")\
        .replace("'", "")\
        .replace(".", "")\
        .replace("é", "e")\
        .replace("è", "e")\
        .replace("ê", "e")\
        .replace("à", "a")\
        .replace("â", "a")\
        .replace("î", "i")\
        .replace("ô", "o")\
        .replace("ç", "c")\
        .replace("œ", "oe")\
        .replace("É", "e")
        
        if std_name in existing_names:
            mapping.append((std_name, name.replace("'", "\\'"), desc.replace("'", "\\'")))
        else:
            print std_name
            
    print len(existing_names)
    print len(mapping)
    # for m in mapping:
        # print """
    # <string name="ability_name_{0}">{1}</string>
    # <string name="ability_infight_{0}">{2}</string>
    # <string name="ability_outfight_{0}"></string>""".format(*m)
    

existing_names = [u'guts', u'run_away', u'hustle', u'download', u'adaptability', u'analytic', u'shed_skin', u'moxie', u'intimidate', u'chlorophyll', u'harvest', u'keen_eye', u'sheer_force', u'defiant', u'insomnia', u'frisk', u'cursed_body', u'effect_spore', u'regenerator', u'swift_swim', u'sniper', u'damp', u'motor_drive', u'vital_spirit', u'blaze', u'magician', u'cute_charm', u'technician', u'skill_link', u'static', u'rock_head', u'sturdy', u'levitate', u'gluttony', u'torrent', u'rain_dish', u'shell_armor', u'soundproof', u'pressure', u'super_luck', u'justified', u'thick_fat', u'huge_power', u'sap_sipper', u'unnerve', u'solar_power', u'magma_armor', u'flame_body', u'weak_armor', u'prankster', u'serene_grace', u'rattled', u'rough_skin', u'mummy', u'magic_guard', u'unaware', u'steadfast', u'natural_cure', u'healer', u'aroma_veil', u'illusion', u'swarm', u'no_guard', u'shadow_tag', u'telepathy', u'pixilate', u'poison_point', u'poison_touch', u'aerilate', u'water_absorb', u'compoundeye', u'tinted_lens', u'iron_fist', u'early_bird', u'tangled_feet', u'anticipation', u'dry_skin', u'pure_power', u'volt_absorb', u'quick_feet', u'pickup', u'overcoat', u'stance_change', u'synchronize', u'trace', u'inner_focus', u'heavy_metal', u'aftermath', u'unburden', u'flare_boost', u'overgrow', u'bulletproof', u'filter', u'own_tempo', u'moody', u'scrappy', u'lightningrod', u'battle_armor', u'simple', u'forewarn', u'suction_cups', u'storm_drain', u'mold_breaker', u'oblivious', u'snow_cloak', u'stench', u'flash_fire', u'white_smoke', u'tough_claws', u'solid_rock', u'ice_body', u'truant', u'pickpocket', u'plus', u'gale_wings', u'speed_boost', u'big_pecks', u'rivalry', u'hydration', u'clear_body', u'light_metal', u'sticky_hold', u'sand_force', u'multiscale', u'leaf_guard', u'reckless', u'slow_start', u'liquid_ooze', u'zen_mode', u'anger_point', u'flower_veil', u'symbiosis', u'hyper_cutter', u'shield_dust', u'friend_guard', u'klutz', u'aura_break', u'sand_veil', u'drizzle', u'immunity', u'refrigerate', u'snow_warning', u'limber', u'infiltrator', u'contrary', u'heatproof', u'mega_launcher', u'iron_barbs', u'drought', u'cloud_nine', u'minus', u'normalize', u'competitive', u'strong_jaw', u'color_change', u'protean', u'sand_stream', u'fur_coat', u'cheek_pouch', u'magnet_pull', u'magic_bounce', u'illuminate', u'defeatist', u'wonder_skin', u'sand_rush', u'water_veil', u'marvel_scale', u'honey_gather', u'multitype', u'arena_trap', u'sweet_veil', u'stall', u'wonder_guard', u'teravolt', u'gooey', u'turboblaze', u'toxic_boost', u'air_lock', u'flower_gift', u'poison_heal', u'victory_star', u'bad_dreams', u'fairy_aura', u'parental_bond', u'imposter', u'dark_aura', u'forecast']


data = """Absor. agua
Water Absorb 	Convierte agua en PS. 	Vaporeon, Volcanion 	Poliwag, Poliwhirl, Poliwrath, Politoed, Lapras, Wooper, Quagsire, Mantyke, Mantine, Maractus, Frillish, Jellicent 	Chinchou, Lanturn, Suicune, Cacnea, Cacturne, Tympole, Palpitoad, Seismitoad 	-
Absor. elec.
Volt Absorb 	Convierte electricidad en PS. 	Jolteon, ThundurusT 	Chinchou, Lanturn 	Raikou, Pachirisu 	-
Absor. fuego
Flash Fire 	Aumenta la fuerza de los movimientos tipo fuego si el Pokémon recibe uno en vez de daño. 	Vulpix, Ninetales, Flareon, Heatran 	Growlithe, Arcanine, Ponyta, Rapidash, Houndour, Houndoom, Litwick, Lampent, Chandelure, Heatmor 	Cyndaquil, Quilava, Typhlosion, Entei 	-
Aclimatación
Cloud Nine 	Anula los efectos del clima. 	- 	Psyduck, Golduck 	Lickitung, Swablu, Altaria, Lickilicky 	-
Agallas
Guts 	Sube el ataque si el Pokémon sufre un cambio de estado. 	Larvitar, Taillow, Swellow 	Rattata, Raticate, Machop1, Machoke1, Machamp1, Heracross, Ursaring1, Tyrogue1, Makuhita, Hariyama, Timburr, Gurdurr, Conkeldurr 	Flareon, Shinx, Luxio, Luxray 	-
Armad. bat.
Battle Armor	Bloquea golpes críticos. 	Anorith, Armaldo 	Kabuto, Kabutops, Skorupi, Drapion 	Cubone, Marowak 	-
Ausente
Truant 	Interviene cada dos rondas. 	Slakoth, Slaking 	- 	Durant 	-
Bucle aire
Air Lock 	Anula los efectos del clima. 	Rayquaza 	- 	- 	-
Cabeza roca
Rock Head 	Evita el daño colateral causado por movimientos del usuario. 	Bagon, Shelgon 	Geodude, Graveler, Golem, Onix, Steelix, Cubone, Marowak, Aerodactyl, Rhyhorn, Rhydon, Bonsly, Sudowoodo, Aron, Lairon, Aggron, Relicanth, Basculin 	Tyrunt, Tyrantrum 	-
Cambio color
Color Change 	Toma el tipo del movimiento rival. 	Kecleon 	- 	- 	-
Caparazón
Shell Armor 	Bloquea golpes críticos. 	Clamperl 	Shellder2Cloyster2, Krabby, Kingler, Lapras, Omanyte, Omastar, Corphish, Crawdaunt, Dwebble, Crustle, Escavalier, Shelmet 	Torkoal, Turtwig, Grotle, Torterra, Oshawott, Dewott, Samurott 	Mega-Slowbro
Chorro arena
Sand Stream 	Crea una tormenta de arena. 	Tyranitar, Hippopotas, Hippowdon 	- 	- 	Mega-Tyranitar
Clorofila
Chlorophyll 	Con sol, sube la velocidad. 	Oddish, Gloom, Vileplume, Bellossom, Cherubi, Bellsprout, Weepinbell, Victreebel, Exeggcute, Exeggutor 	Tangela3, Tangrowth, Hoppip3, Skiploom3, Jumpluff3, Sunkern3, Sunflora3, Seedot, Nuzleaf, Shiftry, Tropius3, Sewaddle, Swadloon, Leavanny, Cottonee, Whimsicott, Maractus, Deerling, Sawsbuck 	Bulbasaur, Ivysaur, Venusaur, Leafeon, Cottonee, Whimsicott 	-
Corte fuerte
Hyper Cutter 	Evita que baje el ataque. 	- 	Krabby, Kingler, Pinsir4, Gligar, Gliscor, Mawile, Corphish, Crawdaunt, Trapinch 	- 	-
Cuerpo llama
Flame Body 	Quema al mínimo contacto. 	Magby, Magmar, Magmortar, Larvesta, Volcarona, Fletchinder, Talonflame 	Slugma, Magcargo, Litwick, Lampent, Chandelure 	Ponyta, Rapidash, Moltres, Heatran 	-
Cuerpo puro
Clear Body 	Evita que bajen las estadísticas. 	Beldum, Metang, Metagross, Regirock, Regice, Registeel, Carbink, Diancie 	Tentacool, Tentacruel 	Klink, Klang, Klinklang 	-
Cura lluvia
Rain Dish 	Sube PS cuando llueve. 	- 	Lotad, Lombre, Ludicolo 	Squirtle, Wartortle, Blastoise, Tentacool, Tentacruel, Wingull, Pelipper, Surskit 	-
Cura natural
Natural Cure 	Se cura al salir a la batalla. 	Celebi, Swablu, Altaria, Shaymin 	Happiny, Chansey, Blissey, Staryu, Starmie, Corsola, Budew, Roselia, Roserade, Phantump, Trevenant 	- 	-
Despiste
Oblivious 	Evita la atracción. 	- 	Slowpoke, Slowbro, Slowking, Lickitung, Lickilicky, Smoochum5, Jynx5, Illumise5, Swinub5, Piloswine5, Mamoswine, Wailmer, Wailord, Numel5, Barboach5, Whiscash5 	Spheal, Sealeo, Walrein 	-
Dicha
Serene Grace 	Promueve efectos secundarios. 	Jirachi, Meloetta 	Happiny, Chansey, Blissey, Togepi, Togetic, Togekiss, Dunsparce, Shaymin 	Deerling, Sawsbuck 	-
Efec. espora
Effect Spore 	Duerme, paraliza o envenena al contacto. 	Foongus, Amoonguss 	Paras6, Parasect6, Shroomish6, Breloom6 	Vileplume 	-
Elec. estát.
Static 	Paraliza al mínimo contacto. 	Pichu, Pikachu, Raichu, Elekid, Electabuzz, Mareep, Flaaffy, Ampharos, Emolga 	Voltorb, Electrode, Electrike, Manectric, Stunfisk 	- 	-
Energía pura
Pure Power 	Sube el ataque. 	Meditite, Medicham 	- 	- 	Mega-Medicham
Enjambre
Swarm 	Incrementa el poder de ataques tipo bicho. 	Beedrill, Beautifly, Kricketune, Mothim 	Scyther7, Scizor7, Ledyba, Ledian, Spinarak, Ariados, Heracross, Volbeat, Sewaddle, Swadloon, Leavanny, Venipede, Whirlipede, Scolipede, Karrablast, Escavalier, Durant 	Joltik, Galvantula, Larvesta, Volcarona 	-
Entusiasmo
Hustle 	Cambia precisión por Ataque. 	Deino, Zweilous 	Togepi, Togetic, Togekiss, Corsola, Remoraid8, Delibird, Durant 	Rattata, Raticate, Nidoran?, Nidorina, Nidoran?, Nidorino, Combee, Rufflet 	-
Escama esp.
Marvel Scale 	Sube la defensa si sufre. 	Milotic 	- 	Dratini, Dragonair 	-
Escudo magma
Magma Armor 	Evita el congelamiento. 	- 	Slugma, Magcargo, Camerupt9 	- 	-
Espesura
Overgrow 	Sube ataques tipo planta. 	Bulbasaur, Ivysaur, Venusaur, Chikorita, Bayleef, Meganium, Treecko, Grovyle, Sceptile, Turtwig, Grotle, Torterra, Snivy, Servine, Serperior, Chespin, Quilladin, Chesnaught 	- 	Pansage, Simisage 	-
Espír. vital
Vital Spirit 	Evita el quedarse dormido. 	Vigoroth 	Mankey10, Primeape10, Delibird, Lillipup 	Electabuzz, Magmar, Tyrogue, Elekid, Magby, Electivire, Magmortar 	-
Flexibilidad
Limber 	Evita la parálisis. 	Ditto 	Persian11, Hitmonlee11, Glameow, Purrloin, Liepard, Stunfisk, Hawlucha 	Buneary, Lopunny 	-
Foco interno
Inner Focus 	Evita el retroceso. 	Zubat, Golbat, Crobat, Dragonite 	Abra, Kadabra, Alakazam, Farfetch'd, Girafarig, Sneasel, Snorunt12, Glalie12, Riolu, Lucario, Throh, Sawk, Mienfoo, Mienshao, Pawniard, Bisharp 	Drowzee, Hypno, Hitmonchan, Kangaskhan, Umbreon, Darumaka 	Mega-Gallade
Fuga
Run Away 	Facilita la huida. 	- 	Rattata, Raticate, Ponyta, Rapidash, Doduo, Dodrio, Eevee13, Sentret, Furret, Aipom, Dunsparce, Snubbull, Poochyena13, Pachirisu, Buneary, Patrat 	Caterpie, Weedle, Oddish, Venonat, Wurmple, Nincada, Kricketot, Lillipup 	-
Gran encanto
Cute Charm 	enamora al mínimo contacto. 	Igglybuff, Jigglypuff, Wigglytuff, Sylveon 	Cleffa14, Clefairy14, Clefable14, Skitty14, Delcatty14, Lopunny, Minccino, Cinccino 	Milotic 	-
Hedor
Stench 	Aleja a Pokémon salvajes. 	- 	Grimer, Muk, Stunky, Skuntank, Trubbish, Garbodor 	Gloom 	-
Humedad
Damp 	Evita la autodestrucción. 	- 	Poliwag, Poliwhirl, Poliwrath, Politoed, Psyduck, Golduck, Wooper, Quagsire 	Paras, Parasect, Horsea, Seadra, Kingdra, Mudkip, Marshtomp, Swampert, Frillish, Jellicent 	-
Humo blanco
White Smoke 	Evita que bajen las estadísticas. 	Torkoal 	- 	Heatmor 	-
Iluminación
Illuminate 	Facilita el encuentro con Pokémon salvajes. 	- 	Staryu, Starmie, Chinchou, Lanturn, Volbeat, Watchog 	- 	-
Impulso
Speed Boost 	Aumenta la velocidad en cada turno. 	Ninjask 	Yanma, Yanmega 	Torchic, Combusken, Blaziken, Carvanha, Sharpedo 	Mega-Blaziken
Imán
Magnet Pull 	Atrapa Pokémon de acero. 	- 	Magnemite, Magneton, Magnezone, Nosepass, Probopass 	- 	-
Inmunidad
Immunity 	Evita el envenenamiento. 	Zangoose 	Snorlax 	Gligar 	-
Insomnio
Insomnia 	Evita el quedarse dormido. 	- 	Drowzee15, Hypno15, Hoothoot, Noctowl, Spinarak, Ariados, Murkrow15, Honchkrow, Shuppet15, Banette15 	Delibird, Pumpkaboo, Gourgeist 	Mega-Mewtwo Y
Insonorizar
Soundproof 	Evita ataques de sonido. 	Whismur, Loudred, Exploud 	Voltorb, Electrode, Mime Jr., Mr. Mime16 	Shieldon, Bastiodon, Snover, Abomasnow, Bouffalant 	-
Intimidación
Intimidate 	Baja el ataque del rival. 	Gyarados, Masquerain, Salamence, Staravia, Staraptor 	Ekans, Arbok, Growlithe, Arcanine, Tauros17, Snubbull, Granbull17, Stantler17, Hitmontop17, Mightyena17, Mawile, Shinx, Luxio, Luxray, Herdier, Stoutland, Sandile, Krokorok, Krookodile 	Qwilfish, Scraggy, Scrafty 	Mega-Manectric
Levitación
Levitate 	No sufre ataques tipo tierra. 	Gastly, Haunter, Gengar, Koffing, Weezing, Misdreavus, Mismagius, Unown, Vibrava, Flygon, Lunatone, Solrock, Baltoy, Claydol, Duskull, Chingling, Chimecho, Latias, Latios, Carnivine, Rotom, Uxie, Mesprit, Azelf, Cresselia, Giratina, Tynamo, Eelektross, Eelektrik, Cryogonal, Hydreigon 	Bronzor, Bronzong 	- 	Mega-Latias, Mega-Latios
Llovizna
Drizzle 	Cambia el clima a lluvioso. 	Kyogre 	- 	Politoed 	-
Lodo líquido
Liquid Ooze 	Al robar PS, hiere. 	- 	Tentacool, Tentacruel, Gulpin, Swalot 	- 	-
Madrugar
Early Bird 	Despierta rápido al Pokémon. 	- 	Doduo, Dodrio, Kangaskhan18, Ledyba, Ledian, Natu, Xatu, Girafarig, Houndour, Houndoom, Seedot, Nuzleaf, Shiftry 	Sunkern, Sunflora 	-
Mar llamas
Blaze 	Sube ataques tipo fuego. 	Charmander, Charmeleon, Charizard, Cyndaquil, Quilava, Typhlosion, Torchic, Combusken, Blaziken, Chimchar, Monferno, Infernape, Tepig, Pignite, Emboar, Fennekin, Braixen, Delphox 	- 	Pansear, Simisear 	-
Más
Plus 	Mejora con la habilidad Menos. 	Plusle 	Klink, Klang, Klinklang 	Mareep, Flaaffy, Ampharos, Dedenne 	-
Menos
Minus 	Mejora con la habilidad Más. 	Minun 	Klink, Klang, Klinklang 	Electrike, Manectric 	-
Mudar
Shed Skin 	Se cura mudando la piel. 	Metapod, Kakuna, Dratini, Dragonair, Pupitar, Silcoon, Cascoon, Seviper, Kricketot, Burmy, Spewpa 	Ekans, Arbok, Scraggy, Scrafty, Karrablast 	- 	-
Nado rápido
Swift Swim 	Con lluvia, sube la velocidad. 	Magikarp, Surskit, Feebas, Huntail, Gorebyss, Luvdisc, Buizel, Floatzel 	Horsea19, Kingdra19, Goldeen, Seaking, Omanyte, Omastar, Kabuto, Kabutops, Qwilfish, Mantyke, Mantine, Lotad, Lombre, Ludicolo, Relicanth, Finneon, Lumineon, Tympole, Palpitoad, Seismitoad 	Psyduck, Golduck, Poliwag, Poliwhirl, Poliwrath, Anorith, Armaldo, Tirtouga, Carracosta, Beartic 	Mega-Swampert
Ojocompuesto
Compoundeye 	Aumenta la precisión de los ataques. 	Butterfree, Nincada 	Venonat20, Yanma, Joltik, Galvantula, Scatterbug, Vivillon 	Dustox 	-
Pararrayos
Lightningrod 	Atrae ataques de tipo eléctrico. 	- 	Cubone, Marowak, Rhyhorn, Rhydon, Rhyperior, Electrike, Manectric, Blitzle, Zebstrika 	Pichu, Pikachu, Raichu, Goldeen, Seaking, Zapdos 	Mega-Sceptile
Piel tosca
Rough Skin 	Hiere al tacto. 	Carvanha, Sharpedo 	Druddigon 	Gible, Gabite, Garchomp 	-
Polvo escudo
Shield Dust 	Evita efectos secundarios. 	Caterpie, Weedle, Wurmple, Dustox 	Venomoth21, Scatterbug, Vivillon 	- 	-
Potencia
Huge Power 	Aumenta el ataque. 	- 	Azurill, Marill, Azumarill 	Bunnelby, Diggersby 	Mega-Mawile
Predicción
Forecast 	Cambia de forma con el clima. 	Castform 	- 	- 	-
Presión
Pressure 	Baja los PP del enemigo. 	Articuno, Zapdos, Moltres, Mewtwo, Raikou, Entei, Suicune, Lugia, Ho-Oh, Dusclops, Dusknoir, Deoxys, Vespiquen, Spiritomb, Weavile, Dialga, Palkia, Giratina, Kyurem 	Aerodactyl, Absol22 	Wailmer, Wailord, Pawniard, Bisharp 	-
Punto tóxico
Poison Point 	Envenena al mínimo contacto. 	- 	Nidoran?23, Nidorina23, Nidoqueen23, Nidoran?23, Nidorino23, Nidoking23, Seadra23,Qwilfish, Budew, Roselia, Roserade, Venipede, Whirlipede, Scolipede, Skrelp, Dragalge 	- 	-
Rastro
Trace 	Copia la habilidad especial. 	- 	Porygon24, Porygon224, Ralts, Kirlia, Gardevoir 	- 	Mega-Alakazam
Recogida
Pickup 	Puede tomar objetos. 	Phanpy 	Meowth25, Aipom, Ambipom, Teddiursa25, Zigzagoon25, Linoone25, Pachirisu, Munchlax, Lillipup, Bunnelby, Diggersby, Dedenne, Pumpkaboo, Gourgeist 	- 	-
Ritmo propio
Own Tempo 	Evita la confusión. 	- 	Slowpoke, Slowbro, Slowking, Lickitung, Lickilicky, Smeargle26, Spoink, Grumpig, Spinda26, Glameow, Purugly, Petilil, Lilligant, Bergmite, Avalugg 	Lotad, Lombre, Ludicolo, Numel, Espurr 	-
Robustez
Sturdy 	Anula golpes fulminantes. 	Pineco, Forretress, Donphan, Shieldon, Bastiodon, Roggenrola, Boldore, Gigalith 	Geodude, Graveler, Golem, Magnemite, Magneton, Magnezone, Onix, Steelix, Bonsly, Sudowoodo, Shuckle27, Skarmory, Nosepass, Probopass, Aron, Lairon, Aggron, Dwebble, Crustle, Tirtouga, Carracosta 	Relicanth, Regirock, Bergmite, Avalugg 	-
Sebo
Thick Fat 	Protege del frío y calor. 	- 	Seel28, Dewgong28, Munchlax, Snorlax, Azurill, Marill, Azumarill, Miltank28, Makuhita, Hariyama, Spoink, Grumpig, Spheal28, Sealeo28, Walrein28, Purugly 	Swinub, Piloswine, Mamoswine, Tepig, Pignite 	Mega-Venusaur
Sequía
Drought 	Cambia el clima a soleado en batalla. 	Groudon 	- 	Vulpix, Ninetales 	Mega-Charizard Y
Sincronía
Synchronize 	Transmite problemas de estado. 	Mew, Espeon, Umbreon 	Abra, Kadabra, Alakazam, Natu, Xatu, Ralts, Kirlia, Gardevoir, Munna, Musharna, Elgyem, Beheeyem 	- 	-
Sombratrampa
Shadow Tag 	Evita que el enemigo huya. 	Wynaut, Wobbuffet 	- 	Gothita, Gothorita, Gothitelle, Litwick, Lampent, Chandelure 	Mega-Gengar
Superguarda
Wonder Guard 	Solo afectan golpes super efectivos. 	Shedinja 	- 	- 	-
Torrente
Torrent 	Sube ataques tipo agua. 	Squirtle, Wartortle, Blastoise, Totodile, Croconaw, Feraligatr, Mudkip, Marshtomp, Swampert, Piplup, Prinplup, Empoleon, Oshawott, Dewott, Samurott, Froakie, Frogadier,Greninja 	- 	Panpour, Simipour 	-
Trampa arena
Arena Trap 	Evita la huida. 	- 	Diglett, Dugtrio, Trapinch 	- 	-
Velo agua
Water Veil 	Evita las quemaduras. 	- 	Goldeen, Seaking, Wailmer, Wailord 	Mantine, Huntail, Buizel, Floatzel, Finneon, Lumineon, Mantyke 	-
Velo arena
Sand Veil 	Aumenta evasión con Tormenta Arena. 	Sandshrew, Sandslash, Cacnea, Cacturne, Gible, Gabite, Garchomp 	Diglett, Dugtrio, Gligar, Gliscor, Helioptile, Heliolisk 	Geodude, Graveler, Golem, Phanpy, Donphan, Larvitar, Stunfisk 	-
Ventosas
Suction Cups 	Fija el cuerpo con firmeza. 	Lileep, Cradily 	Octillery29, Inkay, Malamar 	- 	-
Viscosidad
Sticky Hold 	Evita el robo de objetos. 	- 	Grimer, Muk, Gulpin, Swalot, Shellos, Gastrodon, Trubbish, Accelgor 	- 	-
Vista lince
Keen Eye 	Evita que baje la precisión. 	Spearow, Fearow, Wingull, Pelipper, Starly 	Pidgey30, Pidgeotto30, Pidgeot30, Farfetch'd, Hitmonchan30, Sentret, Furret, Hoothoot, Noctowl, Sneasel, Skarmory, Sableye30, Chatot, Patrat, Watchog, Ducklett, Swanna, Rufflet, Braviary, Espurr, Meowstic 	Glameow, Stunky, Skuntank, Skorupi, Drapion 	-
Adaptable
Adaptability 	Potencia los movimientos del mismo tipo. 	- 	Eevee, Porygon-Z, Basculin 	Corphish, Crawdaunt, Feebas, Dragalge 	Mega-Lucario, Mega-Beedrill
Afortunado
Super Luck 	Aumenta la posibilidad de producir un ataque crítico. 	- 	Murkrow, Honchkrow, Absol, Pidove, Tranquill, Unfezant 	Togepi, Togetic, Togekiss 	-
Alerta
Forewarn 	Determina el ataque más potente del Pokémon rival. 	- 	Drowzee, Hypno, Smoochum, Jynx, Munna, Musharna 	- 	-
Anticipación
Anticipation 	Siente los ataques peligrosos del rival. 	Wormadam 	Barboach, Whiscash, Croagunk, Toxicroak 	Eevee 	-
Antídoto
Poison Heal 	Sube PS si el Pokémon está envenenado. 	- 	Shroomish, Breloom 	Gliscor 	-
Audaz
Reckless 	Aumenta el poder de los ataques que causan retroceso. 	- 	Hitmonlee, Basculin, Bouffalant 	Emboar, Staravia, Staraptor, Mienfoo, Mienshao, Rhyhorn, Rhydon, Rhyperior 	-
Cacheo
Frisk 	El Pokémon puede ver el objeto equipado del rival. 	Gothita, Gothorita, Gothitelle 	Stantler, Shuppet, Banette, Phantump, Trevenant, Pumpkaboo, Gourgeist, Noibat, Noivern 	Sentret, Furret, Yanma, Yanmega, Wigglytuff 	-
Colector
Storm Drain 	Atrae ataques de tipo agua lanzados a un Pokémon. 	- 	Shellos, Gastrodon, Finneon, Lumineon 	Lileep, Cradily, Maractus 	-
Cromolente
Tinted Lens 	Potencia los movimientos "poco eficaces". 	- 	Venonat, Venomoth, Illumise, Yanmega 	Butterfree, Hoothoot, Noctowl, Sigilyph, Mothim 	-
Defensa hoja
Leaf Guard 	Previene problemas de estado con día soleado. 	Leafeon 	Tangela, Tangrowth, Hoppip, Skiploom, Jumpluff 	Chikorita, Bayleef, Meganium, Budew, Roselia, Petilil, Lilligant 	-
Descarga
Download 	Ajusta el poder acorde con la habilidad del rival. 	Genesect 	Porygon, Porygon2, Porygon-Z 	- 	-
Don floral
Flower Gift 	Aumenta el poder con día soleado. 	Cherrim 	- 	- 	-
Electromotor
Motor Drive 	Aumenta la rapidez si es golpeado con un ataque tipo eléctrico. 	Electivire 	Blitzle, Zebstrika 	Emolga 	-
Encadenado
Skill Link 	Incrementa la frecuencia de golpes en los ataques de golpeo múltiple. 	- 	Shellder, Cloyster 	Aipom, Ambipom, Minccino, Cinccino 	Mega-Heracross
Experto
Technician 	Aumenta el poder de los ataques débiles. 	- 	Meowth, Persian, Scyther, Scizor, Smeargle, Hitmontop, Ambipom, Minccino, Cinccino 	Mr. Mime, Breloom, Kricketune, Roserade, Mime Jr. 	Mega-Scizor
Filtro
Filter 	Mitiga los movimientos super efectivos. 	- 	Mime Jr., Mr. Mime 	- 	Mega-Aggron
Francotirador
Sniper 	Potencia los movimientos que se vuelven críticos. 	- 	Horsea, Seadra, Kingdra, Remoraid, Octillery, Skorupi, Drapion, Binacle, Barbaracle 	Beedrill, Spearow, Fearow, Spinarak, Ariados 	-
Gula
Gluttony 	Aumenta la rapidez del uso de las bayas equipadas. 	Pansage, Simisage, Pansear, Simisear, Panpour, Simipour 	Shuckle, Zigzagoon, Linoone, Heatmor 	Bellsprout, Weepinbell, Victreebel, Munchlax, Snorlax, Spoink, Grumpig, Gulpin, Swalot 	-
Gélido
Ice Body 	Sube PS con Granizo. 	Vanillite, Vanilluxe, Vanillish 	Snorunt, Glalie, Spheal, Sealeo, Walrein, Bergmite, Avalugg 	Seel, Dewgong, Regice, Glaceon 	-
Hidratación
Hydration 	Cura los problemas de estado si está lloviendo. 	Phione, Manaphy 	Seel, Dewgong, Tympole, Palpitoad, Alomomola, Shelmet, Accelgor, Goomy, Sliggoo, Goodra 	Lapras, Vaporeon, Smoochum, Barboach, Whiscash, Ducklett, Swanna, Gorebyss, Luvdisc 	-
Ignífugo
Heatproof 	Reduce el poder de los ataques tipo fuego. 	- 	Bronzor, Bronzong 	- 	-
Ignorante
Unaware 	Ignora cualquier cambio en la habilidad del enemigo. 	- 	Bidoof, Bibarel, Woobat, Swoobat 	Clefable, Wooper, Quagsire 	-
Impasible
Steadfast 	Sube la velocidad cada vez que el Pokémon retrocede. 	Gallade 	Tyrogue, Riolu, Lucario 	Machop, Machoke, Machamp, Scyther, Hitmontop 	Mega-Mewtwo X
Indefenso
No Guard 	El ataque del Pokémon y el del rival acertarán. 	Honedge, Doublade 	Machop, Machoke, Machamp 	Karrablast, Golett, Golurk 	Mega-Pidgeot
Inicio lento
Slow Start 	Reduce el ataque y la velocidad. 	Regigigas 	- 	- 	-
Intrépido
Scrappy 	Permite golpear a los Pokémon de tipo fantasma. 	- 	Kangaskhan, Miltank 	Taillow, Swellow, Loudred, Exploud, Herdier, Stoutland, Pancham 	Mega-Lopunny
Irascible
Anger Point 	Potencia el ataque tras recibir un golpe crítico. 	- 	Mankey, Primeape, Tauros 	Sandile, Krokorok, Krookodile, Camerupt 	-
Liviano
Unburden 	Sube la velocidad al perder un objeto equipado. 	- 	Drifloon, Drifblim, Purrloin, Liepard, Hawlucha 	Hitmonlee, Treecko, Grovyle, Sceptile, Accelgor, Swirlix, Slurpuff 	-
Mal sueño
Bad dreams 	Reduce los PS del enemigo cuando duerme. 	Darkrai 	- 	- 	-
Manto níveo
Snow Cloak 	Más evasión con Granizo. 	Glaceon, Froslass, Cubchoo, Beartic 	Swinub, Piloswine, Mamoswine 	Articuno 	-
Multitipo
Multitype 	Cambia con la tabla equipada. 	Arceus 	- 	- 	-
Muro mágico
Magic Guard 	Al Pokémon solo le afectan ataques directos. 	- 	Cleffa, Clefairy, Clefable, Sigilyph, Solosis, Duosion, Reuniclus 	Abra, Kadabra, Alakazam 	-
Nevada
Snow Warning 	El Pokémon invoca una tormenta de granizo. 	Snover, Abomasnow 	- 	Amaura, Aurorus 	Mega-Abomasnow
Normalidad
Normalize 	Todos los movimientos de este Pokémon son de tipo normal. 	- 	Skitty, Delcatty 	- 	-
Piel seca
Dry Skin 	Pierde PS si hace calor. Los recupera con agua. 	- 	Paras, Parasect, Croagunk, Toxicroak, Helioptile, Heliolisk 	Jynx 	-
Pies rápidos
Quick Feet 	Potencia la velocidad si hay problemas de estado. 	- 	Granbull, Teddiursa, Ursaring, Poochyena, Mightyena 	Jolteon, Zigzagoon, Linoone, Shroomish, Venipede, Whirlipede, Scolipede 	-
Poder solar
Solar Power 	Aumenta el ataque esp. y baja PS con sol. 	- 	Sunkern, Sunflora, Tropius 	Charmander, Charmeleon, Charizard, Helioptile 	Mega-Houndoom
Puño férreo
Iron Fist 	Aumenta el poder de los puños. 	- 	Hitmonchan, Golett, Golurk, Pancham, Pangoro 	Ledian, Chimchar, Monferno, Infernape, Timburr, Gurdurr, Conkeldurr 	-
Recogemiel
Honey Gather 	El Pokémon recoge miel de donde puede. 	Combee 	- 	Teddiursa 	-
Resquicio
Aftermath 	Daña al rival que le ha dado el golpe de gracia. 	- 	Drifloon, Drifblim, Stunky, Skuntank 	Voltorb, Electrode, Trubbish, Garbodor 	-
Rezagado
Stall 	El Pokémon se moverá en segundo lugar. 	- 	Sableye 	- 	-
Rivalidad
Rivalry 	Sube el ataque si el rival es del mismo sexo. 	- 	Nidoran?, Nidorina, Nidoqueen, Nidoran?, Nidorino, Nidoking, Shinx, Luxio, Luxray, Axew, Fraxure, Haxorus, Litleo, Pyroar 	Pidove, Tranquill, Unfezant 	-
Roca sólida
Solid Rock 	Reduce el poder de los ataques super efectivos del rival. 	- 	Camerupt, Rhyperior, Tirtouga, Carracosta 	- 	-
Rompemoldes
Mold Breaker 	No importan las habilidades para usar movimientos. 	Cranidos, Rampardos 	Pinsir, Axew, Fraxure, Haxorus, Pancham, Pangoro 	Drilbur, Excadrill, Throh, Sawk, Basculin, Druddigon, Hawlucha 	Mega-Ampharos, Mega-Gyarados
Simple
Simple 	Cambia las características de la forma más audaz. 	- 	Numel, Bidoof, Bibarel 	Woobat, Swoobat 	-
Tumbos
Tangled Feet 	Sube la evasión si el Pokémon está confuso. 	- 	Pidgey, Pidgeotto, Pidgeot, Spinda, Chatot 	Doduo, Dodrio 	-
Zoquete
Klutz 	El Pokémon no puede usar ningún objeto equipado. 	- 	Buneary, Lopunny, Woobat, Swoobat, Golett, Golurk 	Audino 	-
Allanamiento
Infiltrator 	Los ataques del usuario no se ven afectados por ataques como Protección o Detección. 	- 	Cottonee, Whimsicott, Espurr, Meowstic, Noibat, Noivern 	Zubat, Golbat, Crobat, Hoppip, Skiploom, Jumpluff, Ninjask, Seviper, Spiritomb 	-
Alma cura
Healer 	Esta habilidad permite eliminar todos los problemas de estado de un compañero Pokémon en plena batalla. 	Spritzee, Aromatisse 	Audino, Alomomola 	Chansey, Bellossom, Blissey 	Mega-Audino
Armadura frágil
Weak Armor 	Cuando el Pokémon es golpeado con ataques físicos, su Defensa se reduce un nivel pero su Velocidad aumenta un nivel. 	- 	Garbodor 	Onix, Omanyte, Omastar, Kabuto, Kabutops, Slugma, Magcargo, Skarmory, Dwebble, Crustle, Vanillite, Vanillish, Vanilluxe, Vullaby, Mandibuzz 	-
Autoestima
Moxie 	Consiste en subir el ataque cuando debilitas a un rival. 	- 	Sandile, Krokorok, Krookodile, Scraggy, Scrafty 	Pinsir, Gyarados, Heracross, Mightyena, Salamence, Honchkrow, Pyroar 	-
Bromista
Prankster 	Hace que los ataques de efectos tengan prioridad. 	Tornadus, Thundurus, Klefki 	Cottonee, Whimsicott 	Murkrow, Sableye, Volbeat, Illumise, Riolu, Purrloin, Liepard, Meowstic31 	Mega-Banette
Cálculo final
Analytic 	Hace que los movimientos sean mas poderosos si son utilizados al último. 	- 	- 	Magnemite, Magneton, Magnezone, Staryu, Starmie, Porygon, Porygon2, PorygonZ, Patrat, Watchog, Elgyem, Beheeyem 	-
Cobardía
Rattled 	Incrementa la Velocidad del Pokémon al enfrentarse a determinados tipos de Pokémon contra los que presenta debilidad. 	- 	- 	Magikarp, Ledyba, Sudowoodo, Dunsparce, Snubbul, Granbull, Poochyena, Whismur, Clamperl, Bonsly, Cubchoo 	-
Compensación
Multiscale 	Cuando el Pokémon tiene su PS al máximo, esta habilidad reduce el daño recibido del ataque rival. 	- 	- 	Dragonite, Lugia 	-
Competitivo
Defiant 	Los efectos de esta habilidad hacen que si al usuario le reducen una característica, sube dos puntos de ataque. 	- 	Pawniard, Bisharp 	Mankey, Primeape, Farfetch'd, Piplup, Prinplup, Empoleon, Purugly, Braviary, Tornadus, Thundurus 	-
Compiescolta
Friend Guard 	Esta habilidad le brinda un poco de protección ante ataques de aliados haciendo que el poseedor de esta habilidad reciba menos daño del normal. 	- 	- 	Cleffa, Clefairy, Igglybuff, Jigglypuff, Happiny, Vivillon 	-
Cosecha
Harvest 	El Pokémon puede utilizar la misma Baya de manera indefinida en batalla. 	- 	- 	Exeggcute, Exeggutor, Tropius, Phantump, Trevenant 	-
Cuerpo maldito
Cursed Body 	Todo aquel rival que golpee a un Pokémon con esta habilidad tiene un 30% de probabilidad de ver anulado temporalmente el uso del movimiento utilizado. 	- 	Frillish, Jellicent 	Shuppet, Banette, Froslass 	-
Espejo mágico
Magic Bounce 	Refleja el efecto de determinados movimientos modificadores. 	- 	- 	Natu, Xatu, Espeon 	Mega-Absol, Mega-Sableye, Mega-Diancie
Flaqueza
Defeatist 	Si los PS restantes del Pokémon son inferiores al 50% de sus PS máximos, sus estadísticas se reducen. 	Archen, Archeops 	- 	- 	-
Funda
Overcoat 	Esta habilidad hace que el usuario sea invulnerable a los cambios del clima. 	- 	Solosis, Duosion, Reuniclus, Vullaby, Mandibuzz 	Shellder, Cloyster, Pineco, Forretress, Shelgon, Burmy, Wormadam, Sewaddle, Swadloon, Leavanny, Escavalier, Shelmet 	-
Herbívoro
Sap Sipper 	Esta habilidad anula los posibles daños que el Pokémon que la tenga pueda sufrir al recibir ataques de tipo planta y aumenta su ataque cuando son golpeados por movimientos de dicho tipo. 	Skiddo, Gogoat 	Deerling, Sawsbuck, Bouffalant, Goomy, Sliggoo, Goodra 	Marill, Azumarill, Girafarig, Stantler, Miltank, Azurill, Blitzle, Zebstrika 	-
Hurto
Pickpocket 	Hace que el usuario robe el objeto del rival al mínimo contacto. 	- 	- 	Sneasel, Seedot, Nuzleaf, Shiftry, Weavile, Binacle, Barbaracle 	-
Ilusión
Illusion 	Permite transformarse en otros Pokémon. 	Zorua, Zoroark 	- 	- 	-
Ímpetu ardiente
Flare Boost 	Incrementa el poder de sus ataques especiales cuando el Pokémon está quemado. 	- 	- 	Drifloon, Drifblim 	-
Ímpetu arena
Sand Rush 	Esta habilidad aumenta la velocidad del Pokémon que la tiene cuando hay una tormenta de arena en plena batalla. 	- 	Herdier, Stoutland, Drilbur, Excadrill 	Sandshrew, Sandslash 	-
Ímpetu tóxico
Toxic Boost 	Incrementa el poder los ataques físicos cuando el usuario está envenenado. 	- 	- 	Zangoose 	-
Impostor
Imposter 	El Pokémon se transforma automáticamente en el Pokémon rival al salir a la batalla. En batallas múltiples se transforma en uno de sus rivales al azar. 	- 	- 	Ditto 	-
Justiciero
Justified 	Es una habilidad que da inmunidad ante los ataques de tipo siniestro y sube el ataque al recibir uno. 	Cobalion, Terrakion, Virizion, Keldeo 	- 	Growlithe, Arcanine, Absol, Lucario, Gallade 	-
Metal liviano
Light Metal 	Hace que el Pokémon pese la mitad 	- 	- 	Scizor, Beldum, Metang, Metagross, Registeel 	-
Metal pesado
Heavy Metal 	Hace que el Pokémon pese el doble. 	- 	- 	Aron, Lairon, Aggron, Bronzor, Bronzong 	-
Modo Daruma
Zen Mode 	Permite al pokemon usuario cambiar de forma cuando tenga menos del 50 % de PS, revirtiendo el Ataque por el Ataque especial. 	- 	Darmanitan 	- 	-
Momia
Mummy 	Su efecto consiste en transformar la habilidad del oponente en Momia cuando el usuario es atacado por un ataque físico o de contacto, lo que da como resultado que el Pokémon pierda su habilidad y le sea inútil la de momia pues no tiene alguna otra característica especial. 	Yamask, Cofagrigus 	- 	- 	-
Nerviosismo
Unnerve 	Esta habilidad anula el uso de las bayas. 	- 	Joltik, Galvantula, Litleo, Pyroar 	Ekans, Arbok, Meowth, Persian, Aerodactyl, Mewtwo, Ursaring, Houndour, Houndoom, Tyranitar, Masquerain, Vespiquen, Axew, Fraxure, Haxorus 	-
Piel milagro
Wonder Skin 	Esta habilidad evita que el pokémon sea afectado por ataques que no hagan daño. 	- 	Sigilyph 	Venomoth, Skitty, Delcatty 	-
Poder arena
Sand Force 	Esta habilidad aumenta el poder de los ataques de tipo tierra, roca y acero cuando hay una tormenta de arena en plena batalla. 	Landorus 	Drilbur, Excadrill 	Diglett, Dugtrio, Nosepass, Probopass, Shellos, Gastrodon, Hippopotas, Hippowdon, Roggenrola, Boldore, Gigalith 	Mega-Garchomp, Mega-Steelix
Potencia bruta
Sheer Force 	Los efectos secundarios de los ataques no se cumplen, pero se hacen más fuertes. 	- 	Timburr, Gurdurr, Conkeldurr, Darmanitan, Druddigon, Rufflet, Braviary 	Nidoqueen, Nidoking, Krabby, Kingler, Tauros, Totodile, Croconaw, Feraligatr, Steelix, Makuhita, Hariyama, Mawile, Trapinch, Bagon, Cranidos, Rampardos, Landorus 	Mega-Camerupt
Punta acero
Iron Barbs 	Provoca daño al rival que haga contacto con este Pokémon. 	Ferroseed, Ferrothorn 	- 	- 	-
Regeneración
Regenerator 	Recupera un tercio de sus PS (HP) cuando lo regresas a su Pokeball en batalla. 	- 	Audino, Mienfoo, Mienshao 	Slowpoke, Slowbro, Slowking, Tangela, Tangrowth, Corsola,Ho-Oh, Solosis, Duosion, Reuniclus, Foongus, Amoonguss, Alomomola 	-
Respondón
Contrary 	Los movimientos que suben estadísticas las bajan, y viceversa. 	- 	Inkay, Malamar 	Shuckle, Spinda, Snivy, Servine, Serperior 	-
Sacapecho
Big Pecks 	Evita que le bajen la defensa al Pokémon usuario. 	Fletchling 	Pidove, Tranquill, Unfezant, Ducklett, Swanna, Vullaby, Mandibuzz 	Pidgey, Pidgeotto, Pidgeot, Chatot 	-
Telepatía
Telepathy 	Con esta habilidad, ataques como terremoto o explosión no afectaran al Pokémon. 	- 	Elgyem, Beheeyem 	Wynaut, Wobbuffet, Ralts, Kirlia, Gardevoir, Meditite, Medicham, Dialga, Palkia, Giratina, Munna, Noibat, Noivern 	-
Terravoltaje
Teravolt 	Hace que las otras habilidades no tengan efecto. 	Zekrom, Kyurem Negro 	- 	- 	-
Tinovictoria
Victory Star 	Aumenta la precisión del Pokemon. 	Victini 	- 	- 	-
Toque tóxico
Poison Touch 	Los movimientos de contacto del poseedor tienen una probabilidad del 30% de envenenar al oponente 	- 	Seismitoad, Skrelp, Dragalge 	Grimer, Muk, Croagunk, Toxicroak 	-
Turbollama
Turboblaze 	Hace que las otras habilidades no tengan efecto. 	Reshiram, Kyurem Blanco 	- 	- 	-
Veleta
Moody 	Provoca que una de las estadísticas del Pokémon se incremente en dos niveles mientras otra se reduce en uno. 	- 	- 	Remoraid, Octillery, Smeargle, Snorunt, Glalie, Bidoof, Bibarel 	-
Alas vendaval
Gale Wings 	Otorga prioridad +1 a los movimientos de tipo volador. 	- 	- 	Fletchling, Fletchinder, Talonflame 	-
Antibalas
Bulletproof 	Hace al usuario inmune a los siguientes movimientos
Amor filial
Parental Bond 	Permite atacar dos veces en un mismo turno, un ataque de su cría y otro del propio Pokémon. 	- 	- 	- 	Mega-Kangaskhan
Aura feérica
Fairy Aura 	Potencia los movimientos de tipo Hada de todos los Pokémon en el combate. 	Xerneas 	- 	- 	-
Aura oscura
Dark Aura 	Potencia los movimientos de tipo Siniestro de todos los Pokémon en el combate. 	Yveltal 	- 	- 	-
Baba
Gooey 	Baja en un nivel la velocidad del Pokémon que use un movimiento de contacto contra el poseedor de la habilidad. 	- 	- 	Goomy, Sliggoo, Goodra 	-
Cambio táctico
Stance Change 	Cambia la forma y las estadísticas del Pokémon dependiendo de sus movimientos. 	Aegislash 	- 	- 	-
Carrillo
Cheek Pouch 	Cuando un Pokémon con esta habilidad se come una baya en combate, además de obtener el efecto habitual de esa baya, recuperará PS. 	- 	Bunnelby, Diggersby, Dedenne 	- 	-
Garra dura
Tough Claws 	Aumenta el poder de los ataques físicos de contacto. 	- 	Binacle, Barbaracle 	- 	Mega-Charizard X, Mega-Aerodactyl, Mega-Metagross
Megadisparador
Mega Launcher 	Aumenta la potencia de movimientos de pulsos, como hidropulso y pulso umbrío, haciéndolos aún más devastadores. 	Clauncher, Clawitzer 	- 	- 	Mega-Blastoise
Mandíbula fuerte
Strong Jaw 	Aumenta la potencia de movimientos en los que se requiere morder, como triturar o mordisco. 	Tyrunt, Tyrantrum 	- 	- 	Mega-Sharpedo
Mutatipo
Protean 	Cambia el tipo del Pokémon al del movimiento que va a usar. 	- 	- 	Froakie, Frogadier, Greninja 	-
Pelaje recio
Fur Coat 	Reduce a la mitad el daño recibido por ataques físicos. 	Furfrou 	- 	- 	-
Piel celeste
Aerilate 	Cambia el tipo de los movimientos de tipo normal por tipo volador. 	- 	- 	- 	Mega-Pinsir, Mega-Salamence
Piel feérica
Pixilate 	Cambia el tipo de los movimientos de tipo normal por tipo hada. 	- 	- 	Sylveon 	Mega-Gardevoir, Mega-Altaria
Piel helada
Refrigerate 	Convierte los movimientos de tipo normal en tipo hielo. 	Amaura, Aurorus 	- 	- 	Mega-Glalie
Prestidigitador
Magician 	Permite al usuario robar el objeto del oponente. 	Hoopa 	- 	Fennekin, Braixen, Delphox, Klefki 	-
Rompeaura
Aura break 	Invierte todas las habilidades de aura. 	Zygarde 	- 	- 	-
Simbiosis
Symbiosis	Hace que el usuario sea capaz de pasar un objeto a un aliado. 	- 	- 	Flabébé, Floette, Florges 	-
Tenacidad
Competitive 	Si al usuario le reducen una característica, sube dos puntos de ataque especial. 	- 	Gothita, Gothorita, Gothitelle 	Meowstic32 	-
Velo aroma
Aroma Veil 	Protege a los aliados de movimientos que afecten a su mente, como atracción. 	- 	- 	Spritzee, Aromatisse 	-
Velo dulce
Sweet Veil 	Evita que los Pokémon aliados se duerman durante el combate. 	Swirlix, Slurpuff 	- 	- 	-
Velo flor
Flower Veil 	Evita que bajen las características de los Pokémon de tipo planta aliados. 	Flabébé, Floette, Florges 	- 	- 	- """

main()
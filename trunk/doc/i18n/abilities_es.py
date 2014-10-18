# -*- coding: utf-8 -*- 

def main():
    mapping = []
    for row in data.split("\n"):
        name = row.split("\t")[1].strip()
        
        std_name = "name_"+name.strip()\
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
            mapping.append((std_name, name.replace("'", "\\'")))
        else:
            print std_name
    
    # for m in mapping:
        # print "    <string name=\"{}\">{}</string>".format(*m)
    

existing_names = ['name_raticate','name_porygon_z','name_scraggy','name_exeggutor','name_braviary','name_shuppet','name_amoonguss','name_kingdra','name_electivire','name_braixen','name_cinccino','name_emolga','name_golem','name_cresselia','name_simipour','name_pelipper','name_dewott','name_shieldon','name_absol','name_azurill','name_vespiquen','name_charizard','name_deino','name_rotom_fan_rotom','name_magcargo','name_tornadus_therian_forme','name_meloetta_aria_forme','name_snubbull','name_sharpedo','name_rotom_frost_rotom','name_mega_mewtwo_y','name_yamask','name_dusknoir','name_clefable','name_mega_mewtwo_x','name_celebi','name_aromatisse','name_zorua','name_mega_manectric','name_karrablast','name_wynaut','name_horsea','name_sylveon','name_skrelp','name_mega_pinsir','name_quagsire','name_mega_venusaur','name_butterfree','name_timburr','name_doduo','name_toxicroak','name_medicham','name_jolteon','name_pumpkaboo_large_size','name_wormadam_trash_cloak','name_aegislash_blade_forme','name_bellossom','name_ralts','name_pawniard','name_lairon','name_weezing','name_drifloon','name_flygon','name_pineco','name_chingling','name_quilladin','name_mime_jr','name_smeargle','name_miltank','name_linoone','name_cubone','name_bibarel','name_hypno','name_lileep','name_rotom_mow_rotom','name_cranidos','name_mamoswine','name_stunky','name_garbodor','name_heatmor','name_makuhita','name_stantler','name_alakazam','name_mega_charizard_x','name_charmeleon','name_tirtouga','name_seadra','name_turtwig','name_snorunt','name_escavalier','name_whismur','name_rotom_normal_rotom','name_magmortar','name_slakoth','name_mareep','name_binacle','name_prinplup','name_tynamo','name_plusle','name_aegislash_shield_forme','name_elekid','name_talonflame','name_baltoy','name_yanma','name_pidove','name_eelektrik','name_kirlia','name_ducklett','name_oddish','name_metang','name_gastrodon','name_dragonite','name_lilligant','name_genesect','name_nidorino','name_banette','name_nidorina','name_rhydon','name_regigigas','name_tentacruel','name_petilil','name_darmanitan_zen_mode','name_mankey','name_slowbro','name_kricketot','name_florges','name_pinsir','name_spinarak','name_dodrio','name_chatot','name_scatterbug','name_basculin','name_metapod','name_electrode','name_vanillite','name_glaceon','name_gulpin','name_golett','name_trubbish','name_togepi','name_honchkrow','name_pansear','name_staravia','name_ekans','name_spheal','name_octillery','name_pansage','name_zygarde','name_pikachu','name_zoroark','name_mega_mawile','name_roggenrola','name_rhyperior','name_mega_gardevoir','name_mega_blaziken','name_seedot','name_qwilfish','name_garchomp','name_latios','name_grumpig','name_wormadam_plant_cloak','name_glalie','name_steelix','name_mesprit','name_zapdos','name_phanpy','name_uxie','name_gloom','name_metagross','name_azumarill','name_kyogre','name_mega_banette','name_gligar','name_wurmple','name_electabuzz','name_vigoroth','name_chansey','name_furret','name_sudowoodo','name_beartic','name_maractus','name_aurorus','name_scyther','name_buneary','name_hoot_hoot','name_lapras','name_spiritomb','name_slugma','name_paras','name_larvesta','name_reuniclus','name_cleffa','name_servine','name_treecko','name_bronzor','name_gourgeist_average_size','name_misdreavus','name_mega_blastoise','name_venipede','name_cottonee','name_dewgong','name_parasect','name_swalot','name_voltorb','name_magikarp','name_darmanitan_standard_mode','name_swellow','name_ferrothorn','name_swampert','name_mudkip','name_farfetchd','name_groudon','name_abomasnow','name_sunkern','name_nidoqueen','name_altaria','name_pidgey','name_croagunk','name_houndour','name_mandibuzz','name_togekiss','name_tympole','name_skuntank','name_piplup','name_illumise','name_gabite','name_klinklang','name_giratina_origin_forme','name_torchic','name_accelgor','name_heliolisk','name_burmy','name_hitmontop','name_pachirisu','name_marill','name_mega_lucario','name_skitty','name_abra','name_swadloon','name_wigglytuff','name_tyrunt','name_kecleon','name_deoxys_speed_forme','name_cloyster','name_rotom_heat_rotom','name_helioptile','name_spritzee','name_sawsbuck','name_kyurem_black_kyurem','name_hippopotas','name_giratina_altered_forme','name_kakuna','name_exeggcute','name_zigzagoon','name_rattata','name_girafarig','name_seel','name_granbull','name_kabutops','name_patrat','name_wormadam_sandy_cloak','name_bulbasaur','name_furfrou','name_mega_houndoom','name_gothitelle','name_dedenne','name_ivysaur','name_shinx','name_pidgeot','name_nosepass','name_fearow','name_larvitar','name_togetic','name_mega_aggron','name_exploud','name_mantyke','name_swoobat','name_venusaur','name_samurott','name_snorlax','name_kyurem_white_kyurem','name_muk','name_poliwag','name_espeon','name_conkeldurr','name_staryu','name_archen','name_krookodile','name_heatran','name_ponyta','name_azelf','name_krokorok','name_hariyama','name_wobbuffet','name_starmie','name_cryogonal','name_smoochum','name_bastiodon','name_spewpa','name_carvanha','name_ampharos','name_mega_medicham','name_tangrowth','name_sunflora','name_clawitzer','name_chimecho','name_hawlucha','name_rufflet','name_gogoat','name_simisear','name_vivillon','name_noibat','name_vulpix','name_graveler','name_crobat','name_bellsprout','name_rotom_wash_rotom','name_lumineon','name_frogadier','name_rhyhorn','name_gyarados','name_sigilyph','name_spoink','name_dialga','name_sandshrew','name_electrike','name_pichu','name_terrakion','name_amaura','name_goldeen','name_magby','name_whimsicott','name_lopunny','name_chinchou','name_manectric','name_gourgeist_super_size','name_keldeo','name_sceptile','name_tornadus_incarnate_forme','name_registeel','name_xatu','name_duskull','name_starly','name_venomoth','name_blastoise','name_mega_scizor','name_dratini','name_hydreigon','name_clefairy','name_dwebble','name_torterra','name_drilbur','name_cherubi','name_bidoof','name_nidoran_f','name_litleo','name_entei','name_nidoran_m','name_oshawott','name_galvantula','name_drowzee','name_doublade','name_riolu','name_weedle','name_swinub','name_mawile','name_torkoal','name_excadrill','name_masquerain','name_yanmega','name_kricketune','name_whirlipede','name_grovyle','name_blaziken','name_malamar','name_vullaby','name_marowak','name_skiddo','name_lombre','name_combee','name_taillow','name_minccino','name_arceus','name_mega_aerodactyl','name_kadabra','name_regirock','name_deoxys_attack_forme','name_politoed','name_bunnelby','name_cacturne','name_raichu','name_seaking','name_vibrava','name_cradily','name_deerling','name_grimer','name_unown','name_combusken','name_beedrill','name_cubchoo','name_swablu','name_emboar','name_leavanny','name_murkrow','name_beldum','name_mienshao','name_mothim','name_gastly','name_swanna','name_trapinch','name_blissey','name_grotle','name_rampardos','name_gigalith','name_pidgeotto','name_finneon','name_joltik','name_dusclops','name_vaporeon','name_boldore','name_dragonair','name_magnezone','name_roselia','name_slaking','name_spinda','name_poliwrath','name_palkia','name_darumaka','name_munna','name_tauros','name_staraptor','name_bouffalant','name_raikou','name_empoleon','name_cyndaquil','name_arbok','name_gothorita','name_monferno','name_psyduck','name_weepinbell','name_porygon2','name_walrein','name_golduck','name_hitmonchan','name_munchlax','name_gible','name_swirlix','name_shelmet','name_honedge','name_delphox','name_sableye','name_buizel','name_golbat','name_throh','name_relicanth','name_musharna','name_happiny','name_clamperl','name_eelektross','name_phantump','name_budew','name_bisharp','name_sealeo','name_beheeyem','name_woobat','name_floatzel','name_dunsparce','name_mega_tyranitar','name_shedinja','name_druddigon','name_vanilluxe','name_mega_abomasnow','name_zekrom','name_remoraid','name_alomomola','name_duosion','name_umbreon','name_mega_ampharos','name_slowpoke','name_slurpuff','name_wartortle','name_whiscash','name_tranquill','name_scrafty','name_loudred','name_hitmonlee','name_teddiursa','name_sawk','name_huntail','name_porygon','name_stoutland','name_volcarona','name_serperior','name_cascoon','name_lotad','name_forretress','name_venonat','name_jynx','name_minun','name_mega_gyarados','name_mega_charizard_y','name_sliggoo','name_chimchar','name_tepig','name_gallade','name_panpour','name_pancham','name_goodra','name_chesnaught','name_lampent','name_virizion','name_sentret','name_trevenant','name_seviper','name_chikorita','name_lillipup','name_typhlosion','name_landorus_incarnate_forme','name_ninetales','name_magnemite','name_cobalion','name_persian','name_nidoking','name_ninjask','name_greninja','name_pyroar','name_poochyena','name_eevee','name_barboach','name_kabuto','name_froakie','name_claydol','name_tyrogue','name_nincada','name_ambipom','name_klink','name_spearow','name_camerupt','name_wingull','name_litwick','name_barbaracle','name_reshiram','name_lickitung','name_poliwhirl','name_mega_gengar','name_clauncher','name_feraligatr','name_mismagius','name_luxray','name_gorebyss','name_aron','name_aerodactyl','name_rapidash','name_slowking','name_jirachi','name_pumpkaboo_small_size','name_chespin','name_sandile','name_squirtle','name_zangoose','name_latias','name_mightyena','name_lugia','name_onix','name_flareon','name_magneton','name_fraxure','name_shellder','name_geodude','name_crawdaunt','name_dustox','name_manaphy','name_croconaw','name_gengar','name_solosis','name_carnivine','name_corphish','name_ledian','name_chandelure','name_jellicent','name_delcatty','name_floette','name_cofagrigus','name_meditite','name_audino','name_fennekin','name_bronzong','name_wooper','name_bayleef','name_vileplume','name_shuckle','name_shaymin_sky_forme','name_herdier','name_nuzleaf','name_igglybuff','name_sandslash','name_gourgeist_small_size','name_bagon','name_rayquaza','name_hoppip','name_luxio','name_cherrim','name_weavile','name_omanyte','name_sewaddle','name_kingler','name_palpitoad','name_tentacool','name_hippowdon','name_wailmer','name_magmar','name_growlithe','name_lunatone','name_lucario','name_machoke','name_feebas','name_silcoon','name_drapion','name_lickilicky','name_probopass','name_luvdisc','name_tangela','name_shiftry','name_golurk','name_zweilous','name_leafeon','name_meowstic','name_pignite','name_tropius','name_breloom','name_victini','name_pupitar','name_articuno','name_phione','name_meowth','name_fletchinder','name_ariados','name_bonsly','name_zubat','name_surskit','name_totodile','name_beautifly','name_blitzle','name_axew','name_volbeat','name_scizor','name_dugtrio','name_skiploom','name_gurdurr','name_darkrai','name_mew','name_ferroseed','name_shroomish','name_dragalge','name_glameow','name_xerneas','name_delibird','name_mega_kangaskhan','name_charmander','name_lanturn','name_infernape','name_noivern','name_goomy','name_purugly','name_archeops','name_sneasel','name_jumpluff','name_jigglypuff','name_vanillish','name_omastar','name_klang','name_meganium','name_deoxys_defense_forme','name_frillish','name_ditto','name_kangaskhan','name_pumpkaboo_average_size','name_wailord','name_primeape','name_yveltal','name_thundurus_therian_forme','name_corsola','name_machamp','name_skorupi','name_simisage','name_ursaring','name_anorith','name_snivy','name_gardevoir','name_heracross','name_houndoom','name_seismitoad','name_crustle','name_haxorus','name_mewtwo','name_quilava','name_aggron','name_watchog','name_tyranitar','name_gliscor','name_mantine','name_solrock','name_fletchling','name_mega_heracross','name_marshtomp','name_piloswine','name_roserade','name_numel','name_purrloin','name_espurr','name_gothita','name_mienfoo','name_froslass','name_liepard','name_ho_oh','name_krabby','name_suicune','name_zebstrika','name_diggersby','name_donphan','name_bergmite','name_pumpkaboo_super_size','name_snover','name_mega_absol','name_carbink','name_klefki','name_castform','name_skarmory','name_mr_mime','name_natu','name_flaaffy','name_mega_garchomp','name_ledyba','name_shaymin_land_forme','name_gourgeist_large_size','name_cacnea','name_koffing','name_arcanine','name_milotic','name_diglett','name_aipom','name_thundurus_incarnate_forme','name_machop','name_ludicolo','name_noctowl','name_meloetta_pirouette_forme','name_inkay','name_durant','name_regice','name_armaldo','name_elgyem','name_shellos','name_landorus_therian_forme','name_foongus','name_victreebel','name_shelgon','name_caterpie','name_stunfisk','name_drifblim','name_flabebe','name_mega_alakazam','name_scolipede','name_deoxys_normal_forme','name_carracosta','name_unfezant','name_haunter','name_pangoro','name_tyrantrum','name_moltres','name_salamence','name_avalugg','name_kyurem']

data = """001 	Bulbasaur 	Tipo planta 	Tipo veneno 	????? 	Fushigidane 	Fushigidane 	Monstruo 	Planta 	226 				080CE
002 	Ivysaur 	Tipo planta 	Tipo veneno 	????? 	Fushigiso 	Fushigisou 	Monstruo 	Planta 	227 				081CE
003 	Venusaur 	Tipo planta 	Tipo veneno 	????? 	Fushigibana 	Fushigibana 	Monstruo 	Planta 	228 				082CE
004 	Charmander 	Tipo fuego 		???? 	Hitokage 	Hitokage 	Monstruo 	Dragón 	229 				083CE
005 	Charmeleon 	Tipo fuego 		???? 	Rizado 	Lizardo 	Monstruo 	Dragón 	230 				084CE
006 	Charizard 	Tipo fuego 	Tipo volador 	????? 	Rizadon 	Lizardon 	Monstruo 	Dragón 	231 				085CE
007 	Squirtle 	Tipo agua 		???? 	Zenigame 	Zenigame 	Monstruo 	Agua 1 	232 				086CE
008 	Wartortle 	Tipo agua 		???? 	Kameru 	Kameil 	Monstruo 	Agua 1 	233 				087CE
009 	Blastoise 	Tipo agua 		????? 	Kamekkusu 	Kamex 	Monstruo 	Agua 1 	234 				088CE
010 	Caterpie 	Tipo bicho 		????? 	Kyatapi 	Caterpie 	Bicho 		024 				023CE
011 	Metapod 	Tipo bicho 		????? 	Toranseru 	Trancell 	Bicho 		025 				024CE
012 	Butterfree 	Tipo bicho 	Tipo volador 	????? 	Batafuri 	Butterfree 	Bicho 		026 				025CE
013 	Weedle 	Tipo bicho 	Tipo veneno 	???? 	Bidoru 	Beedle 	Bicho 		027 				026CE
014 	Kakuna 	Tipo bicho 	Tipo veneno 	???? 	Kokun 	Cocoon 	Bicho 		028 				027CE
015 	Beedrill 	Tipo bicho 	Tipo veneno 	???? 	Supia 	Spear 	Bicho 		029 				028CE
016 	Pidgey 	Tipo normal 	Tipo volador 	??? 	Poppo 	Poppo 	Volador 		010 				017CE
017 	Pidgeotto 	Tipo normal 	Tipo volador 	???? 	Pijon 	Pigeon 	Volador 		011 				018CE
018 	Pidgeot 	Tipo normal 	Tipo volador 	????? 	Pijotto 	Pigeot 	Volador 		012 				019CE
019 	Rattata 	Tipo normal 		???? 	Koratta 	Koratta 	Campo 		017 			059 	
020 	Raticate 	Tipo normal 		??? 	Ratta 	Ratta 	Campo 		018 			060 	
021 	Spearow 	Tipo normal 	Tipo volador 	????? 	Onisuzume 	Onisuzume 	Volador 		013 				109MO
022 	Fearow 	Tipo normal 	Tipo volador 	????? 	Onidoriru 	Onidrill 	Volador 		014 				110MO
023 	Ekans 	Tipo veneno 		??? 	Abo 	Arbo 	Campo 	Dragón 	050 				037MO
024 	Arbok 	Tipo veneno 		????? 	Abokku 	Arbok 	Campo 	Dragón 	051 				038MO
025 	Pikachu 	Tipo eléctrico 		????? 	Pikachu 	Pikachu 	Campo 	Hada 	022 	156 	104 		036CE
026 	Raichu 	Tipo eléctrico 		????? 	Raichu 	Raichu 	Campo 	Hada 	023 	157 	105 		037CE
027 	Sandshrew 	Tipo tierra 		??? 	Sando 	Sand 	Campo 		048 	112 		113 	097MO
028 	Sandslash 	Tipo tierra 		????? 	Sandopan 	Sandpan 	Campo 		049 	113 		114 	098MO
029 	Nidoran H 	Tipo veneno 		????? 	Nidoran? 	Nidoran? 	Monstruo 	Campo 	095 				104CO
030 	Nidorina 	Tipo veneno 		????? 	Nidorina 	Nidorina 	Ninguno 		096 				105CO
031 	Nidoqueen 	Tipo veneno 	Tipo tierra 	????? 	Nidokuin 	Nidoqueen 	Ninguno 		097 				106CO
032 	Nidoran M 	Tipo veneno 		????? 	Nidoran? 	Nidoran? 	Monstruo 	Campo 	098 				107CO
033 	Nidorino 	Tipo veneno 		????? 	Nidorino 	Nidorino 	Monstruo 	Campo 	099 				108CO
034 	Nidoking 	Tipo veneno 	Tipo tierra 	????? 	Nidokingu 	Nidoking 	Monstruo 	Campo 	100 				109CO
035 	Clefairy 	Tipo hada2 		??? 	Pippi 	Pippi 	Hada 		041 		100 	089 	
036 	Clefable 	Tipo hada3 		???? 	Pikushi 	Pixy 	Hada 		042 		101 	090 	
037 	Vulpix 	Tipo fuego 		??? 	Rokon 	Rokon 	Campo 		125 	153 		248 	
038 	Ninetales 	Tipo fuego 		????? 	Kyukon 	Kyukon 	Campo 		126 	154 		249 	
039 	Jigglypuff 	Tipo normal 	Tipo hada4 	??? 	Purin 	Purin 	Hada 		044 	138 		282 	120MO
040 	Wigglytuff 	Tipo normal 	Tipo hada5 	???? 	Pukurin 	Pukurin 	Hada 		045 	139 		283 	121MO
041 	Zubat 	Tipo veneno 	Tipo volador 	???? 	Zubatto 	Zubat 	Volador 		037 	063 	028 	061 	145CE
042 	Golbat 	Tipo veneno 	Tipo volador 	????? 	Gorubatto 	Golbat 	Volador 		038 	064 	029 	062 	146CE
043 	Oddish 	Tipo planta 	Tipo veneno 	????? 	Nazonokusa 	Nazonokusa 	Planta 		083 	088 			106CE
044 	Gloom 	Tipo planta 	Tipo veneno 	????? 	Kusaihana 	Kusaihana 	Planta 		084 	089 			107CE
045 	Vileplume 	Tipo planta 	Tipo veneno 	????? 	Rafureshia 	Ruffresia 	Planta 		085 	090 			108CE
046 	Paras 	Tipo bicho 	Tipo planta 	??? 	Parasu 	Paras 	Bicho 	Planta 	070 				
047 	Parasect 	Tipo bicho 	Tipo planta 	????? 	Parasekuto 	Parasect 	Bicho 	Planta 	071 				
048 	Venonat 	Tipo bicho 	Tipo veneno 	???? 	Konpan 	Kongpang 	Bicho 		108 				
049 	Venomoth 	Tipo bicho 	Tipo veneno 	????? 	Morufon 	Morphon 	Bicho 		109 				
050 	Diglett 	Tipo tierra 		???? 	Diguda 	Digda 	Campo 		132 				001MO
051 	Dugtrio 	Tipo tierra 		????? 	Dagutorio 	Dugtrio 	Campo 		133 				002MO
052 	Meowth 	Tipo normal 		???? 	Nyasu 	Nyarth 	Campo 		136 				
053 	Persian 	Tipo normal 		????? 	Perushian 	Persian 	Campo 		137 				
054 	Psyduck 	Tipo agua 		???? 	Kodakku 	Koduck 	Agua 1 	Campo 	138 	158 	043 	028 	059CE
055 	Golduck 	Tipo agua 		????? 	Gorudakku 	Golduck 	Agua 1 	Campo 	139 	159 	044 	029 	060CE
056 	Mankey 	Tipo lucha 		???? 	Manki 	Mankey 	Campo 		134 				
057 	Primeape 	Tipo lucha 		????? 	Okorizaru 	Okorizaru 	Campo 		135 				
058 	Growlithe 	Tipo fuego 		???? 	Gadi 	Gardie 	Campo 		127 			051 	
059 	Arcanine 	Tipo fuego 		????? 	Uindi 	Windie 	Campo 		128 			052 	
060 	Poliwag 	Tipo agua 		???? 	Nyoromo 	Nyoromo 	Agua 1 		072 				033MO
061 	Poliwhirl 	Tipo agua 		???? 	Nyorozo 	Nyorozo 	Agua 1 		073 				034MO
062 	Poliwrath 	Tipo agua 	Tipo lucha 	????? 	Nyorobon 	Nyorobon 	Agua 1 		074 				035MO
063 	Abra 	Tipo psíquico 		???? 	Keshii 	Casey 	Humanoide 		089 	039 	020 		102CE
064 	Kadabra 	Tipo psíquico 		????? 	Yungera 	Yungerer 	Humanoide 		090 	040 	021 		103CE
065 	Alakazam 	Tipo psíquico 		????? 	Fudin 	Foodin 	Humanoide 		091 	041 	022 		104CE
066 	Machop 	Tipo lucha 		????? 	Wanriki 	Wanriky 	Humanoide 		140 	073 	040 		057CO
067 	Machoke 	Tipo lucha 		????? 	Goriki 	Goriky 	Humanoide 		141 	074 	041 		058CO
068 	Machamp 	Tipo lucha 		????? 	Kairiki 	Kairiky 	Humanoide 		142 	075 	042 		059CO
069 	Bellsprout 	Tipo planta 	Tipo veneno 	????? 	Madatsubomi 	Madatsubomi 	Planta 		064 				026MO
070 	Weepinbell 	Tipo planta 	Tipo veneno 	???? 	Utsudon 	Utsudon 	Planta 		065 				027MO
071 	Victreebel 	Tipo planta 	Tipo veneno 	????? 	Utsubotto 	Utsubot 	Planta 		066 				028MO
072 	Tentacool 	Tipo agua 	Tipo veneno 	????? 	Menokurage 	Menokurage 	Agua 3 		162 	066 	136 		025CO
073 	Tentacruel 	Tipo agua 	Tipo veneno 	????? 	Dokukurage 	Dokukurage 	Agua 3 		163 	067 	137 		026CO
074 	Geodude 	Tipo roca 	Tipo tierra 	????? 	Ishitsubute 	Ishitsubute 	Mineral 		034 	057 	031 		009MO
075 	Graveler 	Tipo roca 	Tipo tierra 	???? 	Goron 	Golone 	Mineral 		035 	058 	032 		010MO
076 	Golem 	Tipo roca 	Tipo tierra 	????? 	Goronya 	Golonya 	Mineral 		036 	059 	033 		011MO
077 	Ponyta 	Tipo fuego 		???? 	Ponita 	Ponyta 	Campo 		201 		090 		
078 	Rapidash 	Tipo fuego 		????? 	Gyaroppu 	Gallop 	Campo 		202 		091 		
079 	Slowpoke 	Tipo agua 	Tipo psíquico 	??? 	Yadon 	Yadon 	Monstruo 	Agua 1 	080 				133CO
080 	Slowbro 	Tipo agua 	Tipo psíquico 	???? 	Yadoran 	Yadoran 	Monstruo 	Agua 1 	081 				134CO
081 	Magnemite 	Tipo eléctrico 	Tipo acero6 	??? 	Koiru 	Coil 	Mineral 		118 	082 	178 	048 	069MO
082 	Magneton 	Tipo eléctrico 	Tipo acero6 	????? 	Reakoiru 	Rarecoil 	Mineral 		119 	083 	179 	049 	070MO
083 	Farfetch'd 	Tipo normal 	Tipo volador 	???? 	Kamonegi 	Kamonegi 	Volador 	Campo 	158 				061CE
084 	Doduo 	Tipo normal 	Tipo volador 	???? 	Dodo 	Dodo 	Volador 		199 	092 			094CE
085 	Dodrio 	Tipo normal 	Tipo volador 	????? 	Dodorio 	Dodorio 	Volador 		200 	093 			095CE
086 	Seel 	Tipo agua 		???? 	Pauwau 	Pawou 	Agua 1 	Campo 	176 			265 	
087 	Dewgong 	Tipo agua 	Tipo hielo 	???? 	Jugon 	Jugon 	Agua 1 	Campo 	177 			266 	
088 	Grimer 	Tipo veneno 		????? 	Betobeta 	Betbeter 	Amorfo 		116 	106 		064 	
089 	Muk 	Tipo veneno 		????? 	Betobeton 	Betbeton 	Amorfo 		117 	107 		065 	
090 	Shellder 	Tipo agua 		????? 	Sheruda 	Shellder 	Agua 3 		169 				036CO
091 	Cloyster 	Tipo agua 	Tipo hielo 	????? 	Parushen 	Parshen 	Agua 3 		170 				037CO
092 	Gastly 	Tipo fantasma 	Tipo veneno 	??? 	Gosu 	Ghos 	Amorfo 		058 		069 		030MO
093 	Haunter 	Tipo fantasma 	Tipo veneno 	???? 	Gosuto 	Ghost 	Amorfo 		059 		070 		031MO
094 	Gengar 	Tipo fantasma 	Tipo veneno 	???? 	Genga 	Gangar 	Amorfo 		060 		071 		032MO
095 	Onix 	Tipo roca 	Tipo tierra 	???? 	Iwaku 	Iwark 	Mineral 		062 		034 	071 	053CO
096 	Drowzee 	Tipo psíquico 		???? 	Suripu 	Sleep 	Humanoide 		087 				
097 	Hypno 	Tipo psíquico 		????? 	Suripa 	Sleeper 	Humanoide 		088 				
098 	Krabby 	Tipo agua 		??? 	Kurabu 	Crab 	Agua 3 		164 				
099 	Kingler 	Tipo agua 		????? 	Kingura 	Kingler 	Agua 3 		165 				
100 	Voltorb 	Tipo eléctrico 		????? 	Biriridama 	Biriridama 	Mineral 		120 	084 			072MO
101 	Electrode 	Tipo eléctrico 		????? 	Marumain 	Marumine 	Mineral 		121 	085 			073MO
102 	Exeggcute 	Tipo planta 	Tipo psíquico 	???? 	Tamatama 	Tamatama 	Planta 		104 				136CO
103 	Exeggutor 	Tipo planta 	Tipo psíquico 	???? 	Nasshi 	Nassy 	Planta 		105 				137CO
104 	Cubone 	Tipo tierra 		???? 	Karakara 	Karakara 	Monstruo 		203 				060CO
105 	Marowak 	Tipo tierra 		???? 	Garagara 	Garagara 	Monstruo 		204 				061CO
106 	Hitmonlee 	Tipo lucha 		????? 	Sawamura 	Sawamular 	Humanoide 		144 				
107 	Hitmonchan 	Tipo lucha 		????? 	Ebiwara 	Ebiwalar 	Humanoide 		145 				
108 	Lickitung 	Tipo normal 		????? 	Beroringa 	Beroringa 	Monstruo 		178 		161 	284 	134MO
109 	Koffing 	Tipo veneno 		???? 	Dogasu 	Dogars 	Amorfo 		114 	108 		046 	
110 	Weezing 	Tipo veneno 		????? 	Matadogasu 	Matadogas 	Amorfo 		115 	109 		047 	
111 	Rhyhorn 	Tipo tierra 	Tipo roca 	????? 	Saihon 	Sihorn 	Monstruo 	Campo 	206 	169 	186 		050CO
112 	Rhydon 	Tipo tierra 	Tipo roca 	???? 	Saidon 	Sidon 	Monstruo 	Campo 	207 	170 	187 		051CO
113 	Chansey 	Tipo normal 		???? 	Rakki 	Lucky 	Hada 		217 		097 		
114 	Tangela 	Tipo planta 		????? 	Monjara 	Monjara 	Planta 		179 		181 	216 	
115 	Kangaskhan 	Tipo normal 		???? 	Garura 	Garura 	Monstruo 		205 				062CO
116 	Horsea 	Tipo agua 		???? 	Tattsu 	Tattu 	Agua 1 	Dragón 	186 	184 			039CO
117 	Seadra 	Tipo agua 		???? 	Shidora 	Seadra 	Agua 1 	Dragón 	187 	185 			040CO
118 	Goldeen 	Tipo agua 		????? 	Tosakinto 	Tosakinto 	Agua 2 		078 	050 	078 		053CE
119 	Seaking 	Tipo agua 		????? 	Azumao 	Azumao 	Agua 2 		079 	051 	079 		054CE
120 	Staryu 	Tipo agua 		????? 	Hitodeman 	Hitodeman 	Agua 3 		167 	143 		238 	034CO
121 	Starmie 	Tipo agua 	Tipo psíquico 	????? 	Sutami 	Starmie 	Agua 3 		168 	144 		239 	035CO
122 	Mr. Mime 	Tipo psíquico 	Tipo hada7 	????? 	Bariyado 	Barrierd 	Humanoide 		156 		095 		114CO
123 	Scyther 	Tipo bicho 	Tipo volador 	????? 	Sutoraiku 	Strike 	Bicho 		110 		195 		136MO
124 	Jynx 	Tipo hielo 	Tipo psíquico 	????? 	Rujura 	Rougela 	Humanoide 		153 				084MO
125 	Electabuzz 	Tipo eléctrico 		???? 	Erebu 	Eleboo 	Humanoide 		155 		198 	057 	
126 	Magmar 	Tipo fuego 		???? 	Buba 	Boober 	Humanoide 		151 		201 	054 	
127 	Pinsir 	Tipo bicho 		???? 	Kairosu 	Kailios 	Bicho 		112 	167 		146 	130CO
128 	Tauros 	Tipo normal 		????? 	Kentarosu 	Kentauros 	Campo 		148 				125CO
129 	Magikarp 	Tipo agua 		????? 	Koikingu 	Koiking 	Agua 2 	Dragón 	076 	052 	023 		049CE
130 	Gyarados 	Tipo agua 	Tipo volador 	????? 	Gyaradosu 	Gyarados 	Agua 2 	Dragón 	077 	053 	024 		050CE
131 	Lapras 	Tipo agua 	Tipo hielo 	???? 	Rapurasu 	Laplace 	Monstruo 	Agua 1 	219 			242 	150CO
132 	Ditto 	Tipo normal 		???? 	Metamon 	Metamon 	Ditto 		092 			261 	138MO
133 	Eevee 	Tipo normal 		???? 	Ibui 	Eievui 	Campo 		180 		163 	091 	077CO
134 	Vaporeon 	Tipo agua 		????? 	Shawazu 	Showers 	Campo 		181 		164 	092 	078CO
135 	Jolteon 	Tipo eléctrico 		????? 	Sandasu 	Thunders 	Campo 		182 		165 	093 	079CO
136 	Flareon 	Tipo fuego 		????? 	Busuta 	Booster 	Campo 		183 		166 	094 	080CO
137 	Porygon 	Tipo normal 		???? 	Porigon 	Porygon 	Mineral 		215 		192 		
138 	Omanyte 	Tipo roca 	Tipo agua 	????? 	Omunaito 	Omnite 	Agua 1 	Agua 3 	220 				
139 	Omastar 	Tipo roca 	Tipo agua 	????? 	Omusuta 	Omstar 	Agua 1 	Agua 3 	221 				
140 	Kabuto 	Tipo roca 	Tipo agua 	??? 	Kabuto 	Kabuto 	Agua 1 	Agua 3 	222 				
141 	Kabutops 	Tipo roca 	Tipo agua 	????? 	Kabutopusu 	Kabutops 	Agua 1 	Agua 3 	223 				
142 	Aerodactyl 	Tipo roca 	Tipo volador 	??? 	Putera 	Ptera 	Volador 		224 				068CO
143 	Snorlax 	Tipo normal 		???? 	Kabigon 	Kabigon 	Monstruo 		225 		113 		139CE
144 	Articuno 	Tipo hielo 	Tipo volador 	????? 	Furiza 	Freezer 	Ninguno 		235 				151CO
145 	Zapdos 	Tipo eléctrico 	Tipo volador 	???? 	Sanda 	Thunder 	Ninguno 		236 				152CO
146 	Moltres 	Tipo fuego 	Tipo volador 	????? 	Faiya 	Fire 	Ninguno 		237 				153CO
147 	Dratini 	Tipo dragón 		????? 	Miniryu 	Miniryu 	Agua 1 	Dragón 	241 				145MO
148 	Dragonair 	Tipo dragón 		????? 	Hakuryu 	Hakuryu 	Agua 1 	Dragón 	242 				146MO
149 	Dragonite 	Tipo dragón 	Tipo volador 	????? 	Kairyu 	Kairyu 	Agua 1 	Dragón 	243 				147MO
150 	Mewtwo 	Tipo psíquico 		????? 	Myutsu 	Mewtwo 	Ninguno 		249 				151MO
151 	Mew 	Tipo psíquico 		??? 	Myu 	Mew 	Ninguno 		250 				
152 	Chikorita 	Tipo planta 		????? 	Chikorita 	Chicorita 	Monstruo 	Planta 	001 				
153 	Bayleef 	Tipo planta 		????? 	Beirifu 	Bayleaf 	Monstruo 	Planta 	002 				
154 	Meganium 	Tipo planta 		????? 	Meganiumu 	Meganium 	Monstruo 	Planta 	003 				
155 	Cyndaquil 	Tipo fuego 		????? 	Hinoarashi 	Hinoarashi 	Campo 		004 				
156 	Quilava 	Tipo fuego 		????? 	Magumarashi 	Magmarashi 	Campo 		005 				
157 	Typhlosion 	Tipo fuego 		????? 	Bakufun 	Bakphoon 	Campo 		006 				
158 	Totodile 	Tipo agua 		???? 	Waninoko 	Waninoko 	Monstruo 	Agua 1 	007 				
159 	Croconaw 	Tipo agua 		????? 	Arigeitsu 	Alligates 	Monstruo 	Agua 1 	008 				
160 	Feraligatr 	Tipo agua 		????? 	Odairu 	Ordile 	Monstruo 	Agua 1 	009 				
161 	Sentret 	Tipo normal 		??? 	Otachi 	Otachi 	Campo 		019 				109CE
162 	Furret 	Tipo normal 		???? 	Otachi 	Ootachi 	Campo 		020 				110CE
163 	Hoot hoot 	Tipo normal 	Tipo volador 	???? 	Hoho 	Hoho 	Volador 		015 		106 		117MO
164 	Noctowl 	Tipo normal 	Tipo volador 	????? 	Yorunozuku 	Yorunozuku 	Volador 		016 		107 		118MO
165 	Ledyba 	Tipo bicho 	Tipo volador 	???? 	Rediba 	Rediba 	Bicho 		030 				074CE
166 	Ledian 	Tipo bicho 	Tipo volador 	????? 	Redian 	Redian 	Bicho 		031 				075CE
167 	Spinarak 	Tipo bicho 	Tipo veneno 	???? 	Itomaru 	Itomaru 	Bicho 		032 				107MO
168 	Ariados 	Tipo bicho 	Tipo veneno 	????? 	Ariadosu 	Ariados 	Bicho 		033 				108MO
169 	Crobat 	Tipo veneno 	Tipo volador 	????? 	Kurobatto 	Crobat 	Volador 		039 	065 	030 	063 	147CE
170 	Chinchou 	Tipo agua 	Tipo eléctrico 	????? 	Chonchi 	Chonchie 	Agua 2 		174 	181 			147CO
171 	Lanturn 	Tipo agua 	Tipo eléctrico 	????? 	Rantan 	Lantern 	Agua 2 		175 	182 			148CO
172 	Pichu 	Tipo eléctrico 		???? 	Pichu 	Pichu 	Ninguno 		021 	155 	103 		035CE
173 	Cleffa 	Tipo hada8 		?? 	Pii 	Py 	Ninguno 		040 		099 	088 	
174 	Igglybuff 	Tipo normal 	Tipo hada9 	???? 	Pupurin 	Pupurin 	Ninguno 		043 	137 		281 	119MO
175 	Togepi 	Tipo hada10 		???? 	Togepi 	Togepy 	Ninguno 		046 		173 		
176 	Togetic 	Tipo hada11 	Tipo volador 	????? 	Togechikku 	Togechick 	Volador 	Hada 	047 		174 		
177 	Natu 	Tipo psíquico 	Tipo volador 	???? 	Neiti 	Naty 	Volador 		159 	162 			
178 	Xatu 	Tipo psíquico 	Tipo volador 	????? 	Neitio 	Natio 	Volador 		160 	163 			
179 	Mareep 	Tipo eléctrico 		???? 	Meripu 	Merriep 	Monstruo 	Campo 	053 			025 	127CO
180 	Flaaffy 	Tipo eléctrico 		??? 	Mokoko 	Mokoko 	Monstruo 	Campo 	054 			026 	128CO
181 	Ampharos 	Tipo eléctrico 		????? 	Denryu 	Denryu 	Monstruo 	Campo 	055 			027 	129CO
182 	Bellossom 	Tipo planta 		????? 	Kireihana 	Kireihana 	Planta 		086 	091 			108CE
183 	Marill 	Tipo agua 	Tipo hada 12 	??? 	Mariru 	Maril 	Agua 1 	Hada 	130 	055 	125 	031 	042CE
184 	Azumarill 	Tipo agua 	Tipo hada 13 	???? 	Mariruri 	Marilli 	Agua 1 	Hada 	131 	056 	126 	032 	043CE
185 	Sudowoodo 	Tipo roca 		????? 	Usokki 	Usokkie 	Mineral 		106 		093 		130MO
186 	Politoed 	Tipo agua 		????? 	Nyorotono 	Nyorotono 	Agua 1 		075 				036MO
187 	Hoppip 	Tipo planta 	Tipo volador 	???? 	Hanekko 	Hanecco 	Hada 	Planta 	067 				135CE
188 	Skiploom 	Tipo planta 	Tipo volador 	???? 	Popokko 	Popocco 	Hada 	Planta 	068 				136CE
189 	Jumpluff 	Tipo planta 	Tipo volador 	???? 	Watakko 	Watacco 	Hada 	Planta 	069 				137CE
190 	Aipom 	Tipo normal 		???? 	Eipamu 	Eipam 	Campo 		122 		063 		
191 	Sunkern 	Tipo planta 		????? 	Himanattsu 	Himanuts 	Planta 		102 			020 	
192 	Sunflora 	Tipo planta 		???? 	Kimawari 	Kimawari 	Planta 		103 			021 	
193 	Yanma 	Tipo bicho 	Tipo volador 	????? 	Yanyanma 	Yanyanma 	Bicho 		101 		183 	216 	087CO
194 	Wooper 	Tipo agua 	Tipo tierra 	??? 	Upa 	Upah 	Agua 1 	Campo 	056 		117 		017MO
195 	Quagsire 	Tipo agua 	Tipo tierra 	??? 	Nuo 	Nuoh 	Agua 1 	Campo 	057 		118 		018MO
196 	Espeon 	Tipo psíquico 		???? 	Efi 	Eifie 	Campo 		184 		167 	095 	081CO
197 	Umbreon 	Tipo siniestro 		????? 	Burakki 	Blacky 	Campo 		185 		168 	096 	082CO
198 	Murkrow 	Tipo siniestro 	Tipo volador 	????? 	Yamikarasu 	Yamikarasu 	Volador 		208 		074 		051MO
199 	Slowking 	Tipo agua 	Tipo psíquico 	????? 	Yadokingu 	Yadoking 	Monstruo 	Agua 1 	082 				135CO
200 	Misdreavus 	Tipo fantasma 		??? 	Muma 	Muma 	Amorfo 		214 		072 		
201 	Unown 	Tipo psíquico 		????? 	Annon 	Unknown 	Ninguno 		061 		114 		
202 	Wobbuffet 	Tipo psíquico 		????? 	Sonansu 	Sonans 	Amorfo 		107 	161 			119CO
203 	Girafarig 	Tipo normal 	Tipo psíquico 	????? 	Kirinriki 	Kirinriki 	Campo 		147 	164 	121 		
204 	Pineco 	Tipo bicho 		????? 	Kunugidama 	Kunugidama 	Bicho 		093 				
205 	Forretress 	Tipo bicho 	Tipo acero 	????? 	Foretosu 	Foretos 	Bicho 		094 				
206 	Dunsparce 	Tipo normal 		???? 	Nokocchi 	Nokotchi 	Campo 		052 			035 	040CE
207 	Gligar 	Tipo tierra 	Tipo volador 	????? 	Guraiga 	Gliger 	Bicho 		189 		153 	221 	115MO
208 	Steelix 	Tipo acero 	Tipo tierra 	????? 	Haganeru 	Haganeil 	Mineral 		063 		035 	072 	054CO
209 	Snubbull 	Tipo hada14 		??? 	Buru 	Bulu 	Campo 	Hada 	123 				071CO
210 	Granbull 	Tipo hada15 		????? 	Guranburu 	Granbulu 	Campo 	Hada 	124 				072CO
211 	Qwilfish 	Tipo agua 	Tipo veneno 	????? 	Harisen 	Harysen 	Agua 2 		161 				038CO
212 	Scizor 	Tipo bicho 	Tipo acero 	???? 	Hassamu 	Hassam 	Bicho 		111 		196 		137MO
213 	Shuckle 	Tipo bicho 	Tipo roca 	???? 	Tsubotsubo 	Tsubotsubo 	Bicho 		166 			232 	014MO
214 	Heracross 	Tipo bicho 	Tipo lucha 	????? 	Herakurosu 	Heracros 	Bicho 		113 	168 	062 	145 	131CO
215 	Sneasel 	Tipo siniestro 	Tipo hielo 	???? 	Nyura 	Nyula 	Campo 		213 		144 	252 	091MO
216 	Teddiursa 	Tipo normal 		???? 	Himeguma 	Himeguma 	Campo 		193 				132MO
217 	Ursaring 	Tipo normal 		???? 	Ringuma 	Ringuma 	Campo 		194 				133MO
218 	Slugma 	Tipo fuego 		????? 	Magumaggu 	Magmag 	Amorfo 		211 	103 			012MO
219 	Magcargo 	Tipo fuego 	Tipo roca 	????? 	Magukarugo 	Magcargot 	Amorfo 		212 	104 			013MO
220 	Swinub 	Tipo hielo 	Tipo tierra 	???? 	Urimu 	Urimoo 	Campo 		191 		203 	258 	076MO
221 	Piloswine 	Tipo hielo 	Tipo tierra 	???? 	Inomu 	Inomoo 	Campo 		192 		204 	259 	077MO
222 	Corsola 	Tipo agua 	Tipo roca 	???? 	Sanigo 	Sunnygo 	Agua 1 	Agua 3 	171 	180 		237 	146CO
223 	Remoraid 	Tipo agua 		????? 	Teppo'o 	Teppouo 	Agua 1 	Agua 2 	172 		132 	235 	144CO
224 	Octillery 	Tipo agua 		???? 	Okutan 	Okutank 	Agua 1 	Agua 2 	173 		133 	236 	145CO
225 	Delibird 	Tipo hielo 	Tipo volador 	????? 	Deribado 	Delibird 	Agua 1 	Campo 	190 			254 	090MO
226 	Mantine 	Tipo agua 	Tipo volador 	????? 	Mantain 	Mantain 	Agua 1 		197 		141 	234 	140CO
227 	Skarmory 	Tipo acero 	Tipo volador 	????? 	Eamudo 	Airmd 	Volador 		198 	115 		203 	112MO
228 	Houndour 	Tipo siniestro 	Tipo fuego 	???? 	Derubiru 	Delvil 	Campo 		209 		176 		075CO
229 	Houndoom 	Tipo siniestro 	Tipo fuego 	???? 	Heruga 	Hellgar 	Campo 		210 		177 		076CO
230 	Kingdra 	Tipo agua 	Tipo dragón 	????? 	Kingudora 	Kingdra 	Agua 1 	Dragón 	188 	186 			041CO
231 	Phanpy 	Tipo tierra 		???? 	Gomazo 	Gomazou 	Campo 		195 	165 			
232 	Donphan 	Tipo tierra 		????? 	Donfan 	Donfan 	Campo 		196 	166 			
233 	Porygon2 	Tipo normal 		????2 	Porigon2 	Porygon2 	Mineral 		216 		193 		
234 	Stantler 	Tipo normal 		???? 	Odoshishi 	Odoshishi 	Campo 		129 				
235 	Smeargle 	Tipo normal 		???? 	Doburu 	Doble 	Campo 		157 				124CE
236 	Tyrogue 	Tipo lucha 		???? 	Baruki 	Balkie 	Ninguno 		143 				
237 	Hitmontop 	Tipo lucha 		????? 	Kapoera 	Kapoerer 	Humanoide 		146 				
238 	Smoochum 	Tipo hielo 	Tipo psíquico 	????? 	Muchuru 	Muchul 	Ninguno 		152 				083MO
239 	Elekid 	Tipo eléctrico 		????? 	Erekiddo 	Elekid 	Ninguno 		154 		197 	056 	
240 	Magby 	Tipo fuego 		??? 	Bubii 	Buby 	Ninguno 		150 		200 	053 	
241 	Miltank 	Tipo normal 		????? 	Mirutanku 	Miltank 	Campo 		149 				126CO
242 	Blissey 	Tipo normal 		???? 	Hapinasu 	Happinas 	Hada 		218 		098 		
243 	Raikou 	Tipo eléctrico 		???? 	Raiko 	Raikou 	Ninguno 		238 				
244 	Entei 	Tipo fuego 		???? 	Entei 	Entei 	Ninguno 		239 				
245 	Suicune 	Tipo agua 		???? 	Suikun 	Suikun 	Ninguno 		240 				
246 	Larvitar 	Tipo roca 	Tipo tierra 	????? 	Yogirasu 	Yogiras 	Monstruo 		244 			292 	102MO
247 	Pupitar 	Tipo roca 	Tipo tierra 	????? 	Sanagirasu 	Sanagiras 	Monstruo 		245 			293 	103MO
248 	Tyranitar 	Tipo roca 	Tipo siniestro 	????? 	Bangirasu 	Bangiras 	Monstruo 		246 			294 	104MO
249 	Lugia 	Tipo psíquico 	Tipo volador 	??? 	Rugia 	Lugia 	Ninguno 		247 				
250 	Ho-Oh 	Tipo fuego 	Tipo volador 	???? 	Ho'o 	Houou 	Ninguno 		248 				
251 	Celebi 	Tipo psíquico 	Tipo planta 	???? 	Serebii 	Cerebi 	Ninguno 		251 				
252 	Treecko 	Tipo planta 		??? 	Kimori 	Kimori 	Monstruo 	Dragón 		001 			
253 	Grovyle 	Tipo planta 		????? 	Juputoru 	Juptile 	Monstruo 	Dragón 		002 			
254 	Sceptile 	Tipo planta 		????? 	Jukain 	Jukain 	Monstruo 	Dragón 		003 			
255 	Torchic 	Tipo fuego 		???? 	Achamo 	Achamo 	Campo 			004 			
256 	Combusken 	Tipo fuego 	Tipo lucha 	????? 	Wakashamo 	Wakasyamo 	Campo 			005 			
257 	Blaziken 	Tipo fuego 	Tipo lucha 	????? 	Bashamo 	Bursyamo 	Campo 			006 			
258 	Mudkip 	Tipo agua 		????? 	Mizugoro 	Mizugorou 	Monstruo 	Agua 1 		007 			
259 	Marshtomp 	Tipo agua 	Tipo tierra 	????? 	Numakuro 	Numacraw 	Monstruo 	Agua 1 		008 			
260 	Swampert 	Tipo agua 	Tipo tierra 	????? 	Raguraji 	Laglarge 	Monstruo 	Agua 1 		009 			
261 	Poochyena 	Tipo siniestro 		???? 	Pochiena 	Pochiena 	Campo 			010 			044MO
262 	Mightyena 	Tipo siniestro 		???? 	Guraena 	Guraena 	Campo 			011 			045MO
263 	Zigzagoon 	Tipo normal 		????? 	Jiguzaguma 	Ziguzaguma 	Campo 			012 			012CE
264 	Linoone 	Tipo normal 		????? 	Massuguma 	Massuguma 	Campo 			013 			013CE
265 	Wurmple 	Tipo bicho 		???? 	Kemusso 	Kemusso 	Bicho 			014 	048 		
266 	Silcoon 	Tipo bicho 		????? 	Karasarisu 	Karasalis 	Bicho 			015 	049 		
267 	Beautifly 	Tipo bicho 	Tipo volador 	????? 	Agehanto 	Agehunt 	Bicho 			016 	050 		
268 	Cascoon 	Tipo bicho 		???? 	Mayurudo 	Mayuld 	Bicho 			017 	051 		
269 	Dustox 	Tipo bicho 	Tipo veneno 	????? 	Dokukeiru 	Dokucale 	Bicho 			018 	052 		
270 	Lotad 	Tipo agua 	Tipo planta 	???? 	Hasubo 	Hassboh 	Agua 1 	Planta 		019 			055MO
271 	Lombre 	Tipo agua 	Tipo planta 	????? 	Hasuburero 	Hasubrero 	Agua 1 	Planta 		020 			056MO
272 	Ludicolo 	Tipo agua 	Tipo planta 	????? 	Runpappa 	Runpappa 	Agua 1 	Planta 		021 			057MO
273 	Seedot 	Tipo planta 		???? 	Tanebo 	Taneboh 	Campo 	Planta 		022 			
274 	Nuzleaf 	Tipo planta 	Tipo siniestro 	???? 	Konohana 	Konohana 	Campo 	Planta 		023 			
275 	Shiftry 	Tipo planta 	Tipo siniestro 	????? 	Datengu 	Dirteng 	Campo 	Planta 		024 			
276 	Taillow 	Tipo normal 	Tipo volador 	??? 	Subame 	Subame 	Volador 			025 			019CO
277 	Swellow 	Tipo normal 	Tipo volador 	????? 	Osubame 	Ohsubame 	Volador 			026 			020CO
278 	Wingull 	Tipo agua 	Tipo volador 	???? 	Kyamome 	Camome 	Agua 1 	Volador 		027 	119 	212 	017CO
279 	Pelipper 	Tipo agua 	Tipo volador 	????? 	Perippa 	Pelipper 	Agua 1 	Volador 		028 	120 	213 	018CO
280 	Ralts 	Tipo psíquico 	Tipo hada16 	???? 	Rarutosu 	Ralts 	Amorfo 			029 	157 		064CE
281 	Kirlia 	Tipo psíquico 	Tipo hada17 	???? 	Kiruria 	Kirlia 	Amorfo 			030 	158 		065CE
282 	Gardevoir 	Tipo psíquico 	Tipo hada18 	????? 	Sanaito 	Sirnight 	Amorfo 			031 	159 		066CE
283 	Surskit 	Tipo bicho 	Tipo agua 	???? 	Ametama 	Ametama 	Agua 1 	Bicho 		032 			047CE
284 	Masquerain 	Tipo bicho 	Tipo volador 	????? 	Amemosu 	Amemoth 	Agua 1 	Bicho 		033 			048CE
285 	Shroomish 	Tipo planta 		???? 	Kinokoko 	Kinococo 	Hada 	Planta 		034 			
286 	Breloom 	Tipo planta 	Tipo lucha 	????? 	Kinogassa 	Kinogassa 	Hada 	Planta 		035 			
287 	Slakoth 	Tipo normal 		???? 	Namakero 	Namakero 	Campo 			036 		276 	
288 	Vigoroth 	Tipo normal 		????? 	Yarukimono 	Yarukimono 	Campo 			037 		277 	
289 	Slaking 	Tipo normal 		????? 	Kekkingu 	Kekking 	Campo 			038 		278 	
290 	Nincada 	Tipo bicho 	Tipo tierra 	???? 	Tsuchinin 	Tutinin 	Bicho 			042 			111CE
291 	Ninjask 	Tipo bicho 	Tipo volador 	????? 	Tekkanin 	Tekkanin 	Bicho 			043 			112CE
292 	Shedinja 	Tipo bicho 	Tipo fantasma 	???? 	Nukenin 	Nukenin 	Mineral 			044 			113CE
293 	Whismur 	Tipo normal 		????? 	Gonyonyo 	Gonyonyo 	Monstruo 	Campo 		045 			140CE
294 	Loudred 	Tipo normal 		???? 	Dogomu 	Dogohmb 	Monstruo 	Campo 		046 			141CE
295 	Exploud 	Tipo normal 		????? 	Bakuongu 	Bakuong 	Monstruo 	Campo 		047 			142CE
296 	Makuhita 	Tipo lucha 		????? 	Makunoshita 	Makunoshita 	Humanoide 			048 			095CO
297 	Hariyama 	Tipo lucha 		????? 	Hariteyama 	Hariteyama 	Humanoide 			049 			096CO
298 	Azurill 	Tipo normal 	Tipo hada19 	??? 	Ruriri 	Ruriri 	Ninguno 			054 	124 	030 	041CE
299 	Nosepass 	Tipo roca 		???? 	Nozupasu 	Nosepass 	Mineral 			060 	155 	164 	093CO
300 	Skitty 	Tipo normal 		??? 	Eneko 	Eneco 	Campo 	Hada 		061 		078 	078CE
301 	Delcatty 	Tipo normal 		????? 	Enekororo 	Enekororo 	Campo 	Hada 		062 		079 	079CE
302 	Sableye 	Tipo siniestro 	Tipo fantasma 	???? 	Yamirami 	Yamirami 	Humanoide 			068 			123CO
303 	Mawile 	Tipo acero 	Tipo hada 20 	???? 	Kuchito 	Kucheat 	Campo 	Hada 		069 			063CO
304 	Aron 	Tipo acero 	Tipo roca 	???? 	Kokodora 	Cokodora 	Monstruo 			070 		166 	099MO
305 	Lairon 	Tipo acero 	Tipo roca 	??? 	Kodora 	Kodora 	Monstruo 			071 		167 	100MO
306 	Aggron 	Tipo acero 	Tipo roca 	????? 	Bosugodora 	Bossgodora 	Monstruo 			072 		168 	101MO
307 	Meditite 	Tipo lucha 	Tipo psíquico 	???? 	Asanan 	Asanan 	Humanoide 			076 	086 		143CE
308 	Medicham 	Tipo lucha 	Tipo psíquico 	????? 	Charemu 	Charem 	Humanoide 			077 	087 		144CE
309 	Electrike 	Tipo eléctrico 		???? 	Rakurai 	Rakurai 	Campo 			078 			073CO
310 	Manectric 	Tipo eléctrico 		????? 	Raiboruto 	Livolt 	Campo 			079 			074CO
311 	Plusle 	Tipo eléctrico 		???? 	Purasuru 	Prasle 	Hada 			080 			096CE
312 	Minun 	Tipo eléctrico 		???? 	Mainan 	Minun 	Hada 			081 			097CE
313 	Volbeat 	Tipo bicho 		????? 	Barubito 	Barubeat 	Bicho 	Humanoide 		086 			133CE
314 	Illumise 	Tipo bicho 		????? 	Irumize 	Illumise 	Bicho 	Humanoide 		087 			134CE
315 	Roselia 	Tipo planta 	Tipo veneno 	???? 	Rozeria 	Roselia 	Hada 	Planta 		094 	026 	134 	072CE
316 	Gulpin 	Tipo veneno 		???? 	Gokurin 	Gokulin 	Amorfo 			095 			098CE
317 	Swalot 	Tipo veneno 		????? 	Marunomu 	Marunoom 	Amorfo 			096 			099CE
318 	Carvanha 	Tipo agua 	Tipo siniestro 	???? 	Kibania 	Kibanha 	Agua 2 			097 			055CE
319 	Sharpedo 	Tipo agua 	Tipo siniestro 	????? 	Samehada 	Samehader 	Agua 2 			098 			056CE
320 	Wailmer 	Tipo agua 		???? 	Hoeruko 	Hoeruko 	Campo 	Agua 2 		099 		240 	027CO
321 	Wailord 	Tipo agua 		????? 	Hoeruo 	Whaloh 	Campo 	Agua 2 		100 		241 	028CO
322 	Numel 	Tipo fuego 	Tipo tierra 	???? 	Donmeru 	Donmel 	Campo 			101 		204 	
323 	Camerupt 	Tipo fuego 	Tipo tierra 	???? 	Bakuda 	Bakuuda 	Campo 			102 		205 	
324 	Torkoal 	Tipo fuego 		???? 	Kotasu 	Cotoise 	Campo 			105 			096MO
325 	Spoink 	Tipo psíquico 		???? 	Banebu 	Baneboo 	Campo 			110 		206 	007CO
326 	Grumpig 	Tipo psíquico 		????? 	Bupiggu 	Boopig 	Campo 			111 		207 	008CO
327 	Spinda 	Tipo normal 		????? 	Patchiru 	Patcheel 	Campo 	Humanoide 		114 			131MO
328 	Trapinch 	Tipo tierra 		????? 	Nakkura 	Nuckrar 	Bicho 			116 		121 	003MO
329 	Vibrava 	Tipo tierra 	Tipo dragón 	????? 	Biburaba 	Vibrava 	Bicho 			117 		122 	004MO
330 	Flygon 	Tipo tierra 	Tipo dragón 	????? 	Furaigon 	Flygon 	Bicho 			118 		123 	005MO
331 	Cacnea 	Tipo planta 		???? 	Sabonea 	Sabonea 	Planta 	Humanoide 		119 			
332 	Cacturne 	Tipo planta 	Tipo siniestro 	???? 	Nokutasu 	Noctus 	Planta 	Humanoide 		120 			
333 	Swablu 	Tipo normal 	Tipo volador 	???? 	Chirutto 	Tyltto 	Volador 	Dragón 		121 	171 	246 	139MO
334 	Altaria 	Tipo dragón 	Tipo volador 	????? 	Chirutarisu 	Tyltalis 	Volador 	Dragón 		122 	172 	247 	140MO
335 	Zangoose 	Tipo normal 		????? 	Zangusu 	Zangoose 	Campo 			123 		186 	005CO
336 	Seviper 	Tipo veneno 		????? 	Habuneku 	Habunake 	Campo 	Dragón 		124 		187 	006CO
337 	Lunatone 	Tipo roca 	Tipo psíquico 	????? 	Runaton 	Lunatone 	Mineral 			125 		214 	012CO
338 	Solrock 	Tipo roca 	Tipo psíquico 	????? 	Sorurokku 	Solrock 	Mineral 			126 		215 	013CO
339 	Barboach 	Tipo agua 	Tipo tierra 	????? 	Dojotchi 	Dojoach 	Agua 2 			127 	080 		040MO
340 	Whiscash 	Tipo agua 	Tipo tierra 	???? 	Namazun 	Namazun 	Agua 2 			128 	081 		041MO
341 	Corphish 	Tipo agua 		???? 	Heigani 	Heigani 	Agua 1 	Agua 3 		129 		279 	051CE
342 	Crawdaunt 	Tipo agua 	Tipo siniestro 	????? 	Shizariga 	Shizariger 	Agua 1 	Agua 3 		130 		280 	052CE
343 	Baltoy 	Tipo tierra 	Tipo psíquico 	???? 	Yajiron 	Yajilon 	Mineral 			131 		169 	
344 	Claydol 	Tipo tierra 	Tipo psíquico 	????? 	Nendoru 	Nendoll 	Mineral 			132 		170 	
345 	Lileep 	Tipo roca 	Tipo planta 	???? 	Ririra 	Lilyla 	Agua 3 			133 			
346 	Cradily 	Tipo roca 	Tipo planta 	????? 	Yureidoru 	Yuradle 	Agua 3 			134 			
347 	Anorith 	Tipo roca 	Tipo bicho 	???? 	Anopusu 	Anopth 	Agua 3 			135 			
348 	Armaldo 	Tipo roca 	Tipo bicho 	????? 	Amarudo 	Armaldo 	Agua 3 			136 			
349 	Feebas 	Tipo agua 		???? 	Hinbasu 	Hinbass 	Agua 1 	Dragón 		140 	138 		
350 	Milotic 	Tipo agua 		????? 	Mirokarosu 	Milokaross 	Agua 1 	Dragón 		141 	139 		
351 	Castform 	Tipo normal 		???? 	Powarun 	Powalen 	Hada 	Amorfo 		142 		163 	
352 	Kecleon 	Tipo normal 		????? 	Kakureon 	Kakureon 	Campo 			145 			116CE
353 	Shuppet 	Tipo fantasma 		????? 	Kagebozu 	Kagebouzu 	Amorfo 			146 		210 	122MO
354 	Banette 	Tipo fantasma 		????? 	Jupetta 	Juppeta 	Amorfo 			147 		211 	123MO
355 	Duskull 	Tipo fantasma 		???? 	Yomawaru 	Yomawaru 	Amorfo 			148 	189 		
356 	Dusclops 	Tipo fantasma 		????? 	Samayoru 	Samayouru 	Amorfo 			149 	190 		
357 	Tropius 	Tipo planta 	Tipo volador 	????? 	Toropiusu 	Tropius 	Monstruo 	Planta 		150 	185 	288 	
358 	Chimecho 	Tipo psíquico 		???? 	Chirin 	Chirean 	Amorfo 			151 	083 		112CO
359 	Absol 	Tipo siniestro 		???? 	Abusoru 	Absol 	Campo 			152 	209 	216 	009CO
360 	Wynaut 	Tipo psíquico 		???? 	Sonano 	Sohnano 	Ninguno 			160 			118CO
361 	Snorunt 	Tipo hielo 		????? 	Yukiwarashi 	Yukiwarashi 	Hada 	Mineral 		171 	206 		
362 	Glalie 	Tipo hielo 		????? 	Onigori 	Onigohri 	Hada 	Mineral 		172 	207 		
363 	Spheal 	Tipo hielo 	Tipo agua 	????? 	Tamazarashi 	Tamazarashi 	Agua 1 	Campo 		173 		243 	
364 	Sealeo 	Tipo hielo 	Tipo agua 	????? 	Todogura 	Todoggler 	Agua 1 	Campo 		174 		244 	
365 	Walrein 	Tipo hielo 	Tipo agua 	????? 	Todozeruga 	Todoseruga 	Agua 1 	Campo 		175 		245 	
366 	Clamperl 	Tipo agua 		???? 	Paruru 	Pearlulu 	Agua 1 			176 			141CO
367 	Huntail 	Tipo agua 		????? 	Hanteru 	Huntail 	Agua 1 			177 			142CO
368 	Gorebyss 	Tipo agua 		????? 	Sakurabisu 	Sakurabyss 	Agua 1 			178 			143CO
369 	Relicanth 	Tipo agua 	Tipo roca 	????? 	Jiransu 	Glanth 	Agua 1 	Agua 2 		179 			042CO
370 	Luvdisc 	Tipo agua 		???? 	Rabukasu 	Lovecus 	Agua 2 			183 			029CO
371 	Bagon 	Tipo dragón 		???? 	Tatsubei 	Tatsubay 	Dragón 			187 			014CO
372 	Shelgon 	Tipo dragón 		???? 	Komoru 	Komoruu 	Dragón 			188 			015CO
373 	Salamence 	Tipo dragón 	Tipo volador 	????? 	Bomanda 	Bohmander 	Dragón 			189 			016CO
374 	Beldum 	Tipo acero 	Tipo psíquico 	???? 	Danbaru 	Dumbber 	Mineral 			190 		262 	
375 	Metang 	Tipo acero 	Tipo psíquico 	???? 	Metangu 	Metang 	Mineral 			191 		263 	
376 	Metagross 	Tipo acero 	Tipo psíquico 	????? 	Metagurosu 	Metagross 	Mineral 			192 		264 	
377 	Regirock 	Tipo roca 		????? 	Rejirokku 	Regirock 	Ninguno 			193 			
378 	Regice 	Tipo hielo 		????? 	Rejiaisu 	Regice 	Ninguno 			194 			
379 	Registeel 	Tipo acero 		????? 	Rejisuchiru 	Registeel 	Ninguno 			195 			
380 	Latias 	Tipo dragón 	Tipo psíquico 	????? 	Ratiasu 	Latias 	Ninguno 			196 			
381 	Latios 	Tipo dragón 	Tipo psíquico 	????? 	Ratiosu 	Latios 	Ninguno 			197 			
382 	Kyogre 	Tipo agua 		????? 	Kaioga 	Kyogre 	Ninguno 			198 			
383 	Groudon 	Tipo tierra 		????? 	Guradon 	Groudon 	Ninguno 			199 			
384 	Rayquaza 	Tipo dragón 	Tipo volador 	????? 	Rekkuza 	Rayquaza 	Ninguno 			200 			
385 	Jirachi 	Tipo acero 	Tipo psíquico 	???? 	Jirachi 	Jirachi 	Ninguno 			201 			
386 	Deoxys 	Tipo psíquico 		????? 	Deokishisu 	Deoxys 	Ninguno 			202 			
387 	Turtwig 	Tipo planta 		???? 	Naetoru 	Naetle 	Monstruo 	Planta 			001 		
388 	Grotle 	Tipo planta 		????? 	Hayashigame 	Hayashigame 	Monstruo 	Planta 			002 		
389 	Torterra 	Tipo planta 	Tipo tierra 	????? 	Dodaitosu 	Dodaitose 	Monstruo 	Planta 			003 		
390 	Chimchar 	Tipo fuego 		???? 	Hikozaru 	Hikozaru 	Campo 	Humanoide 			004 		
391 	Monferno 	Tipo fuego 	Tipo lucha 	????? 	Mokazaru 	Moukazaru 	Campo 	Humanoide 			005 		
392 	Infernape 	Tipo fuego 	Tipo lucha 	????? 	Gokazaru 	Goukazaru 	Campo 	Humanoide 			006 		
393 	Piplup 	Tipo agua 		????? 	Pocchama 	Pochama 	Agua 1 	Campo 			007 		
394 	Prinplup 	Tipo agua 		????? 	Pottaishi 	Pottaishi 	Agua 1 	Campo 			008 		
395 	Empoleon 	Tipo agua 	Tipo acero 	????? 	Enperuto 	Emperte 	Agua 1 	Campo 			009 		
396 	Starly 	Tipo normal 	Tipo volador 	???? 	Mukkuru 	Mukkuru 	Volador 				010 		099CO
397 	Staravia 	Tipo normal 	Tipo volador 	????? 	Mukubado 	Mukubird 	Volador 				011 		100CO
398 	Staraptor 	Tipo normal 	Tipo volador 	????? 	Mukuhoku 	Mukuhawk 	Volador 				012 		101CO
399 	Bidoof 	Tipo normal 		??? 	Bippa 	Bipper 	Agua 1 	Campo 			013 		038CE
400 	Bibarel 	Tipo normal 	Tipo agua 	???? 	Bidaru 	Beadull 	Agua 1 	Campo 			014 		039CE
401 	Kricketot 	Tipo bicho 		????? 	Koroboshi 	Korobooshi 	Bicho 				015 		
402 	Kricketune 	Tipo bicho 		????? 	Korotokku 	Korotok 	Bicho 				016 		
403 	Shinx 	Tipo eléctrico 		???? 	Korinku 	Kolink 	Campo 				017 		
404 	Luxio 	Tipo eléctrico 		???? 	Rukushio 	Luxio 	Campo 				018 		
405 	Luxray 	Tipo eléctrico 		????? 	Rentora 	Rentorer 	Campo 				019 		
406 	Budew 	Tipo planta 	Tipo veneno 	???? 	Subomi 	Subomie 	Ninguno 				025 	133 	071CE
407 	Roserade 	Tipo planta 	Tipo veneno 	????? 	Rozureido 	Roserade 	Hada 	Planta 			027 	135 	073CE
408 	Cranidos 	Tipo roca 		????? 	Zugaidosu 	Zugaidos 	Monstruo 				036 		
409 	Rampardos 	Tipo roca 		????? 	Ramuparudo 	Rampard 	Monstruo 				037 		
410 	Shieldon 	Tipo roca 	Tipo acero 	????? 	Tatetopusu 	Tatetops 	Monstruo 				038 		
411 	Bastiodon 	Tipo roca 	Tipo acero 	????? 	Toridepusu 	Trideps 	Monstruo 				039 		
412 	Burmy 	Tipo bicho 		????? 	Minomucchi 	Minomutchi 	Bicho 				045 		044CE
413 	Wormadam 	Tipo bicho 	Tipo planta
414 	Mothim 	Tipo bicho 	Tipo volador 	????? 	Gameiru 	Garmeil 	Bicho 				047 		046CE
415 	Combee 	Tipo bicho 	Tipo volador 	????? 	Mitsuhani 	Mitsuhoney 	Bicho 				053 	142 	076CE
416 	Vespiquen 	Tipo bicho 	Tipo volador 	????? 	Bikuin 	Beequeen 	Bicho 				054 	143 	077CE
417 	Pachirisu 	Tipo eléctrico 		???? 	Pachirisu 	Pachirisu 	Campo 	Hada 			055 		132CO
418 	Buizel 	Tipo agua 		???? 	Buizeru 	Buoysel 	Agua 1 	Campo 			056 	149 	058MO
419 	Floatzel 	Tipo agua 		????? 	Furozeru 	Flowsel 	Agua 1 	Campo 			057 	150 	059MO
420 	Cherubi 	Tipo planta 		????? 	Cherinbo 	Cherinbo 	Hada 	Planta 			058 		
421 	Cherrim 	Tipo planta 		???? 	Cherimu 	Cherrim 	Hada 	Planta 			059 		
422 	Shellos 	Tipo agua 		????? 	Karanakushi 	Karanakushi 	Agua 1 	Amorfo 			060 		
423 	Gastrodon 	Tipo agua 	Tipo tierra 	????? 	Toritodon 	Toritodon 	Agua 1 	Amorfo 			061 		
424 	Ambipom 	Tipo normal 		????? 	Etebosu 	Eteboth 	Campo 				064 		
425 	Drifloon 	Tipo fantasma 	Tipo volador 	???? 	Fuwante 	Fuwante 	Amorfo 				065 	208 	001CO
426 	Drifblim 	Tipo fantasma 	Tipo volador 	????? 	Fuwaraido 	Fuwaride 	Amorfo 				066 	209 	002CO
427 	Buneary 	Tipo normal 		???? 	Mimiroru 	Mimirol 	Campo 	Humanoide 			067 	080 	
428 	Lopunny 	Tipo normal 		????? 	Mimiroppu 	Mimilop 	Campo 	Humanoide 			068 	081 	
429 	Mismagius 	Tipo fantasma 		????? 	Mumaji 	Mumage 	Amorfo 				073 		
430 	Honchkrow 	Tipo siniestro 	Tipo volador 	????? 	Donkarasu 	Donkarasu 	Volador 				075 		052MO
431 	Glameow 	Tipo normal 		????? 	Nyaruma 	Nyarmar 	Campo 				076 		
432 	Purugly 	Tipo normal 		????? 	Bunyatto 	Bunyat 	Campo 				077 		
433 	Chingling 	Tipo psíquico 		????? 	Rishan 	Lisyan 	Ninguno 				082 		111CO
434 	Stunky 	Tipo veneno 	Tipo siniestro 	????? 	Sukanpu 	Skunpoo 	Campo 				084 		102CO
435 	Skuntank 	Tipo veneno 	Tipo siniestro 	????? 	Sukatanku 	Skutank 	Campo 				085 		103CO
436 	Bronzor 	Tipo acero 	Tipo psíquico 	????? 	Domira 	Domirror 	Mineral 				088 	250 	
437 	Bronzong 	Tipo acero 	Tipo psíquico 	????? 	Dotakun 	Dootakun 	Mineral 				089 	251 	
438 	Bonsly 	Tipo roca 		???? 	Usohachi 	Usohachi 	Ninguno 				092 		129MO
439 	Mime Jr. 	Tipo psíquico 	Tipo hada 21 	??? 	Manene 	Manene 	Ninguno 				094 		113CO
440 	Happiny 	Tipo normal 		???? 	Pinpuku 	Pinpuku 	Ninguno 				096 		
441 	Chatot 	Tipo normal 	Tipo volador 	???? 	Perappu 	Perap 	Volador 				102 		138CO
442 	Spiritomb 	Tipo fantasma 	Tipo siniestro 	???? 	Mikaruge 	Mikaruge 	Amorfo 				108 		
443 	Gible 	Tipo dragón 	Tipo tierra 	???? 	Fukamaru 	Fukamaru 	Monstruo 	Dragón 			109 		006MO
444 	Gabite 	Tipo dragón 	Tipo tierra 	???? 	Gabaito 	Gabite 	Monstruo 	Dragón 			110 		007MO
445 	Garchomp 	Tipo dragón 	Tipo tierra 	????? 	Gaburiasu 	Gaburias 	Monstruo 	Dragón 			111 		008MO
446 	Munchlax 	Tipo normal 		??? 	Gonbe 	Gonbe 	Ninguno 				112 		138CE
447 	Riolu 	Tipo lucha 		??? 	Rioru 	Riolu 	Ninguno 				115 	033 	062CE
448 	Lucario 	Tipo lucha 	Tipo acero 	???? 	Rukario 	Lucario 	Campo 	Humanoide 			116 	034 	063CE
449 	Hippopotas 	Tipo tierra 		????? 	Hipopotasu 	Hippopotas 	Campo 				122 		048CO
450 	Hippowdon 	Tipo tierra 		????? 	Kabarudon 	Kabarudon 	Campo 				123 		049CO
451 	Skorupi 	Tipo veneno 	Tipo bicho 	???? 	Sukorupi 	Scorpi 	Bicho 	Agua 3 			127 	201 	015MO
452 	Drapion 	Tipo veneno 	Tipo siniestro 	????? 	Dorapion 	Dorapion 	Bicho 	Agua 3 			128 	202 	016MO
453 	Croagunk 	Tipo veneno 	Tipo lucha 	????? 	Guregguru 	Gureggru 	Humanoide 				129 	290 	125CE
454 	Toxicroak 	Tipo veneno 	Tipo lucha 	????? 	Dokuroggu 	Dokurog 	Humanoide 				130 	291 	126CE
455 	Carnivine 	Tipo planta 		????? 	Masukippa 	Muskippa 	Planta 				131 	289 	029MO
456 	Finneon 	Tipo agua 		????? 	Keiko'o 	Keikouo 	Agua 2 				134 		
457 	Lumineon 	Tipo agua 		????? 	Neoranto 	Neorant 	Agua 2 				135 		
458 	Mantyke 	Tipo agua 	Tipo volador 	???? 	Tamanta 	Tamanta 	Ninguno 				140 	233 	139CO
459 	Snover 	Tipo planta 	Tipo hielo 	????? 	Yukikaburi 	Yukikabli 	Monstruo 	Planta 			142 		088MO
460 	Abomasnow 	Tipo planta 	Tipo hielo 	????? 	Yukinoo 	Yukinooh 	Monstruo 	Planta 			143 		089MO
461 	Weavile 	Tipo siniestro 	Tipo hielo 	????? 	Manyura 	Manyula 	Campo 				145 	253 	092MO
462 	Magnezone 	Tipo eléctrico 	Tipo acero 	????? 	Jibakoiru 	Jibacoil 	Mineral 				18022 	050 	071MO
463 	Lickilicky 	Tipo normal 		????? 	Beroberuto 	Berobelt 	Monstruo 				16222 	285 	135MO
464 	Rhyperior 	Tipo tierra 	Tipo roca 	????? 	Dosaidon 	Dosidon 	Monstruo 	Campo 			18822 		052CO
465 	Tangrowth 	Tipo planta 		????? 	Mojanbo 	Mojanbo 	Planta 				18222 	217 	
466 	Electivire 	Tipo eléctrico 		????? 	Erekiburu 	Elekible 	Humanoide 				19922 	058 	
467 	Magmortar 	Tipo fuego 		????? 	Buban 	Booburn 	Humanoide 				20222 	055 	
468 	Togekiss 	Tipo hada 	Tipo volador 23 	????? 	Togekissu 	Togekiss 	Volador 	Hada 			17522 		
469 	Yanmega 	Tipo bicho 	Tipo volador 	????? 	Megayanma 	Megayanma 	Bicho 				18422 	217 	088CO
470 	Leafeon 	Tipo planta 		????? 	Rifia 	Leafia 	Campo 				16922 	097 	083CO
471 	Glaceon 	Tipo hielo 		????? 	Gureishia 	Glacia 	Campo 				17022 	098 	084CO
472 	Gliscor 	Tipo tierra 	Tipo volador 	????? 	Guraion 	Glion 	Bicho 				15422 	222 	116MO
473 	Mamoswine 	Tipo hielo 	Tipo tierra 	???? 	Manmu 	Manmoo 	Campo 				20522 	260 	078MO
474 	Porygon-Z 	Tipo normal 		????Z 	PorigonZ 	PorygonZ 	Mineral 				19422 		
475 	Gallade 	Tipo psíquico 	Tipo lucha 	????? 	Erureido 	Erureido 	Amorfo 				16022 		067CE
476 	Probopass 	Tipo roca 	Tipo acero 	????? 	Dainozu 	Dainose 	Mineral 				15622 	165 	094CO
477 	Dusknoir 	Tipo fantasma 		????? 	Yonowaru 	Yonoir 	Amorfo 				19122 		
478 	Froslass 	Tipo hielo 	Tipo fantasma 	????? 	Yukimenoko 	Yukimenoko 	Hada 	Mineral 			20822 		
479 	Rotom 	Tipo eléctrico 	Tipo fantasma 	??? 	Rotomu 	Rotom 	Amorfo 				15222 		068MO
480 	Uxie 	Tipo psíquico 		???? 	Yukushi 	Yuxie 	Ninguno 				146 		
481 	Mesprit 	Tipo psíquico 		????? 	Emuritto 	Emrit 	Ninguno 				147 		
482 	Azelf 	Tipo psíquico 		???? 	Agunomu 	Agnome 	Ninguno 				148 		
483 	Dialga 	Tipo acero 	Tipo dragón 	????? 	Diaruga 	Dialga 	Ninguno 				149 		
484 	Palkia 	Tipo agua 	Tipo dragón 	???? 	Parukia 	Palkia 	Ninguno 				150 		
485 	Heatran 	Tipo fuego 	Tipo acero 	????? 	Hidoran 	Heatran 	Ninguno 						
486 	Regigigas 	Tipo normal 		????? 	Rejigigasu 	Regigigas 	Ninguno 						
487 	Giratina 	Tipo fantasma 	Tipo dragón 	????? 	Giratina 	Giratina 	Ninguno 				21022 		
488 	Cresselia 	Tipo psíquico 		????? 	Kureseria 	Crecelia 	Ninguno 						
489 	Phione 	Tipo agua 		???? 	Fione 	Phione 	Agua 1 	Hada 					
490 	Manaphy 	Tipo agua 		???? 	Manafi 	Manaphy 	Agua 1 	Hada 			151 		
491 	Darkrai 	Tipo siniestro 		????? 	Dakurai 	Darkrai 	Ninguno 						
492 	Shaymin 	Tipo planta 		???? 	Sheimi 	Sheimi 	Ninguno 						
493 	Arceus 	Tipo normal 		????? 	Aruseusu 	Arseus 	Ninguno 						
494 	Victini 	Tipo psíquico 	Tipo fuego 	????? 	Bikutini 	Victini 	Ninguno 					000 	
495 	Snivy 	Tipo planta 		????? 	Tsutaja 	Tsutarja 	Campo 	Planta 				001 	
496 	Servine 	Tipo planta 		????? 	Janobi 	Janovy 	Campo 	Planta 				002 	
497 	Serperior 	Tipo planta 		????? 	Jaroda 	Jalorda 	Campo 	Planta 				003 	
498 	Tepig 	Tipo fuego 		??? 	Pokabu 	Pokabu 	Campo 					004 	
499 	Pignite 	Tipo fuego 	Tipo lucha 	????? 	Chaobu 	Chaoboo 	Campo 					005 	
500 	Emboar 	Tipo fuego 	Tipo lucha 	????? 	Enbuo 	Enbuoh 	Campo 					006 	
501 	Oshawott 	Tipo agua 		????? 	Mijumaru 	Mijumaru 	Campo 					007 	
502 	Dewott 	Tipo agua 		????? 	Futachimaru 	Futachimaru 	Campo 					008 	
503 	Samurott 	Tipo agua 		????? 	Daikenki 	Daikenki 	Campo 					009 	
504 	Patrat 	Tipo normal 		???? 	Minezumi 	Minezumi 	Campo 					010 	046MO
505 	Watchog 	Tipo normal 		????? 	Miruhoggu 	Miruhog 	Campo 					011 	047MO
506 	Lillipup 	Tipo normal 		????? 	Yoteri 	Yorterrie 	Campo 					012 	
507 	Herdier 	Tipo normal 		????? 	Harderia 	Herderrie 	Campo 					013 	
508 	Stoutland 	Tipo normal 		????? 	Murando 	Mooland 	Campo 					014 	
509 	Purrloin 	Tipo siniestro 		????? 	Choroneko 	Choroneko 	Campo 					015 	042MO
510 	Liepard 	Tipo siniestro 		????? 	Reparudasu 	Lepardas 	Campo 					016 	043MO
511 	Pansage 	Tipo planta 		???? 	Yanappu 	Yanappu 	Campo 					017 	029CE
512 	Simisage 	Tipo planta 		????? 	Yanakki 	Yanakkie 	Campo 					018 	030CE
513 	Pansear 	Tipo fuego 		???? 	Baoppu 	Baoppu 	Campo 					019 	031CE
514 	Simisear 	Tipo fuego 		????? 	Baokki 	Baokkie 	Campo 					020 	032CE
515 	Panpour 	Tipo agua 		???? 	Hiyappu 	Hiyappu 	Campo 					021 	033CE
516 	Simipour 	Tipo agua 		????? 	Hiyakki 	Hiyakkie 	Campo 					022 	034CE
517 	Munna 	Tipo psíquico 		??? 	Munna 	Munna 	Campo 					023 	
518 	Musharna 	Tipo psíquico 		????? 	Mushana 	Musharna 	Campo 					024 	
519 	Pidove 	Tipo normal 	Tipo volador 	???? 	Mamepato 	Mamepato 	Volador 					025 	
520 	Tranquill 	Tipo normal 	Tipo volador 	????? 	Hatopo 	Hatoboh 	Volador 					026 	
521 	Unfezant 	Tipo normal 	Tipo volador 	????? 	Kenhorou 	Kenhallow 	Volador 					027 	
522 	Blitzle 	Tipo eléctrico 		??? 	Shimama 	Shimama 	Campo 					028 	
523 	Zebstrika 	Tipo eléctrico 		????? 	Zeburaika 	Zebraika 	Campo 					029 	
524 	Roggenrola 	Tipo roca 		???? 	Dangoro 	Dangoro 	Mineral 					030 	120CO
525 	Boldore 	Tipo roca 		???? 	Gantoru 	Gantle 	Mineral 					031 	121CO
526 	Gigalith 	Tipo roca 		????? 	Gigaiasu 	Gigaiath 	Mineral 					032 	122CO
527 	Woobat 	Tipo psíquico 	Tipo volador 	???? 	Koromori 	Koromori 	Campo 	Volador 				033 	055CO
528 	Swoobat 	Tipo psíquico 	Tipo volador 	????? 	Kokoromori 	Kokoromori 	Campo 	Volador 				034 	056CO
529 	Drilbur 	Tipo tierra 		????? 	Moguryu 	Mogurew 	Campo 					035 	
530 	Excadrill 	Tipo tierra 	Tipo acero 	????? 	Doryuzu 	Doryuzu 	Campo 					036 	
531 	Audino 	Tipo normal 		???? 	Tabunne 	Tabunne 	Hada 					037 	123CE
532 	Timburr 	Tipo lucha 		????? 	Dokkora 	Dokkoraa 	Humanoide 					038 	093MO
533 	Gurdurr 	Tipo lucha 		????? 	Dotekkotsu 	Dotekkotsu 	Humanoide 					039 	094MO
534 	Conkeldurr 	Tipo lucha 		????? 	Robushin 	Roobushin 	Humanoide 					040 	095MO
535 	Tympole 	Tipo agua 		???? 	Otamaro 	Otamaro 	Agua 1 					041 	
536 	Palpitoad 	Tipo agua 	Tipo tierra 	???? 	Gamagaru 	Gamagaru 	Agua 1 					042 	
537 	Seismitoad 	Tipo agua 	Tipo tierra 	????? 	Gamageroge 	Gamageroge 	Agua 1 					043 	
538 	Throh 	Tipo lucha 		??? 	Nageki 	Nageki 	Humanoide 					044 	097CO
539 	Sawk 	Tipo lucha 		??? 	Dageki 	Dageki 	Humanoide 					045 	098CO
540 	Sewaddle 	Tipo bicho 	Tipo planta 	???? 	Kurumiru 	Kurumiru 	Bicho 					046 	
541 	Swadloon 	Tipo bicho 	Tipo planta 	???? 	Kurumayu 	Kurumayu 	Bicho 					047 	
542 	Leavanny 	Tipo bicho 	Tipo planta 	????? 	Hahakomori 	Hahakomori 	Bicho 					048 	
543 	Venipede 	Tipo bicho 	Tipo veneno 	??? 	Fushide 	Fushide 	Bicho 					049 	120CE
544 	Whirlipede 	Tipo bicho 	Tipo veneno 	???? 	Hoiga 	Hoiiga 	Bicho 					050 	121CE
545 	Scolipede 	Tipo bicho 	Tipo veneno 	????? 	Pendora 	Pendror 	Bicho 					051 	122CE
546 	Cottonee 	Tipo planta 		???? 	Monmen 	Monmen 	Planta 	Hada 				052 	
547 	Whimsicott 	Tipo planta 	Tipo hada 24 	????? 	Erufun 	Elfuun 	Planta 	Hada 				053 	
548 	Petilil 	Tipo planta 		???? 	Churine 	Churine 	Planta 					054 	
549 	Lilligant 	Tipo planta 		????? 	Doredia 	Dredear 	Planta 					055 	
550 	Basculin 	Tipo agua 		???? 	Basurao 	Bassrao 	Agua 2 					056 	060MO
551 	Sandile 	Tipo tierra 	Tipo siniestro 	???? 	Meguroko 	Meguroco 	Campo 					057 	043CO
552 	Krokorok 	Tipo tierra 	Tipo siniestro 	???? 	Warubiru 	Waruvile 	Campo 					058 	044CO
553 	Krookodile 	Tipo tierra 	Tipo siniestro 	????? 	Warubiaru 	Waruvial 	Campo 					059 	045CO
554 	Darumaka 	Tipo fuego 		????? 	Darumakka 	Darumakka 	Campo 					060 	
555 	Darmanitan 	Tipo fuego 		????? 	Hihidaruma 	Hihidaruma 	Campo 					061 	
556 	Maractus 	Tipo planta 		????? 	Marakacchi 	Maracacchi 	Planta 					062 	
557 	Dwebble 	Tipo bicho 	Tipo roca 	????? 	Ishizumai 	Ishizumai 	Bicho 	Mineral 				063 	023CO
558 	Crustle 	Tipo bicho 	Tipo roca 	????? 	Iwaparesu 	Iwaparesu 	Bicho 	Mineral 				064 	024CO
559 	Scraggy 	Tipo siniestro 	Tipo lucha 	???? 	Zuruggu 	Zuruggu 	Campo 	Dragón 				065 	100CE
560 	Scrafty 	Tipo siniestro 	Tipo lucha 	????? 	Zuruzukin 	Zuruzukin 	Campo 	Dragón 				066 	101CE
561 	Sigilyph 	Tipo psíquico 	Tipo volador 	????? 	Shinbora 	Symboler 	Volador 					067 	090CO
562 	Yamask 	Tipo fantasma 		???? 	Desumasu 	Deathmas 	Mineral 	Amorfo 				068 	
563 	Cofagrigus 	Tipo fantasma 		????? 	Desukan 	Desukarn 	Mineral 	Amorfo 				069 	
564 	Tirtouga 	Tipo agua 	Tipo roca 	????? 	Purotoga 	Purotoga 	Agua 1 	Agua 3 				070 	
565 	Carracosta 	Tipo agua 	Tipo roca 	????? 	Abagora 	Abagoura 	Agua 1 	Agua 3 				071 	
566 	Archen 	Tipo roca 	Tipo volador 	???? 	Aken 	Archen 	Volador 	Agua 3 				072 	
567 	Archeops 	Tipo roca 	Tipo volador 	????? 	Akeosu 	Archeos 	Volador 	Agua 3 				073 	
568 	Trubbish 	Tipo veneno 		????? 	Yabukuron 	Yabukuron 	Mineral 					074 	074MO
569 	Garbodor 	Tipo veneno 		????? 	Dasutodasu 	Dasutodasu 	Mineral 					075 	075MO
570 	Zorua 	Tipo siniestro 		??? 	Zoroa 	Zorua 	Campo 					076 	124MO
571 	Zoroark 	Tipo siniestro 		????? 	Zoroaku 	Zoroark 	Campo 					077 	125MO
572 	Minccino 	Tipo normal 		????? 	Chirami 	Chillarmy 	Campo 					078 	
573 	Cinccino 	Tipo normal 		????? 	Chirachino 	Chillaccino 	Campo 					079 	
574 	Gothita 	Tipo psíquico 		??? 	Gochimu 	Gothimu 	Humanoide 					080 	126MO
575 	Gothorita 	Tipo psíquico 		???? 	Gochimiru 	Gothimiru 	Humanoide 					081 	127MO
576 	Gothitelle 	Tipo psíquico 		????? 	Gochiruzeru 	Gothiruselle 	Humanoide 					082 	128MO
577 	Solosis 	Tipo psíquico 		???? 	Yuniran 	Uniran 	Amorfo 					083 	115CO
578 	Duosion 	Tipo psíquico 		???? 	Daburan 	Daburan 	Amorfo 					084 	116CO
579 	Reuniclus 	Tipo psíquico 		????? 	Rankurusu 	Lanculus 	Amorfo 					085 	117CO
580 	Ducklett 	Tipo agua 	Tipo volador 	????? 	Koaruhi 	Koaruhie 	Agua 1 	Volador 				086 	127CE
581 	Swanna 	Tipo agua 	Tipo volador 	???? 	Swanna 	Swanna 	Agua 1 	Volador 				087 	128CE
582 	Vanillite 	Tipo hielo 		????? 	Banipucchi 	Vanipeti 	Mineral 					088 	085MO
583 	Vanillish 	Tipo hielo 		????? 	Baniricchi 	Vaniricchi 	Mineral 					089 	086MO
584 	Vanilluxe 	Tipo hielo 		????? 	Baibanira 	Vaivanilla 	Mineral 					090 	087MO
585 	Deerling 	Tipo normal 	Tipo planta 	???? 	Shikijika 	Shikijika 	Campo 					091 	
586 	Sawsbuck 	Tipo normal 	Tipo planta 	????? 	Mebukijika 	Mebukijika 	Campo 					092 	
587 	Emolga 	Tipo eléctrico 	Tipo volador 	???? 	Emonga 	Emonga 	Campo 					093 	086CO
588 	Karrablast 	Tipo bicho 		???? 	Kaburumo 	Kaburumo 	Bicho 					094 	022MO
589 	Escavalier 	Tipo bicho 	Tipo acero 	????? 	Shubarugo 	Chevargo 	Bicho 					095 	023MO
590 	Foongus 	Tipo planta 	Tipo veneno 	????? 	Tamagetake 	Tamagetake 	Planta 					096 	053MO
591 	Amoonguss 	Tipo planta 	Tipo veneno 	????? 	Morobareru 	Morobareru 	Planta 					097 	054MO
592 	Frillish 	Tipo agua 	Tipo fantasma 	???? 	Pururiru 	Pururill 	Amorfo 					098 	
593 	Jellicent 	Tipo agua 	Tipo fantasma 	????? 	Burunkeru 	Burungel 	Amorfo 					099 	
594 	Alomomola 	Tipo agua 		????? 	Mamanbou 	Mamanbou 	Agua 1 	Agua 2 				100 	149CO
595 	Joltik 	Tipo bicho 	Tipo eléctrico 	???? 	Bachuru 	Bachuru 	Bicho 					101 	
596 	Galvantula 	Tipo bicho 	Tipo eléctrico 	????? 	Denchura 	Dentula 	Bicho 					102 	
597 	Ferroseed 	Tipo planta 	Tipo acero 	????? 	Tessihdo 	Tesseed 	Planta 	Mineral 				103 	069CO
598 	Ferrothorn 	Tipo planta 	Tipo acero 	????? 	Nattorei 	Nutrey 	Planta 	Mineral 				104 	070CO
599 	Klink 	Tipo acero 		??? 	Giaru 	Gear 	Mineral 					105 	
600 	Klang 	Tipo acero 		???? 	Gigiaru 	Gigiaru 	Mineral 					106 	
601 	Klinklang 	Tipo acero 		????? 	Gigigiaru 	Gigigiaru 	Mineral 					107 	
602 	Tynamo 	Tipo eléctrico 		????? 	Shibishirasu 	Shibishirasu 	Amorfo 					108 	
603 	Eelektrik 	Tipo eléctrico 		????? 	Shibibiiru 	Shibibiiru 	Amorfo 					109 	
604 	Eelektross 	Tipo eléctrico 		????? 	Shibirudon 	Shibirudon 	Amorfo 					110 	
605 	Elgyem 	Tipo psíquico 		???? 	Rigure 	Ligray 	Humanoide 					111 	
606 	Beheeyem 	Tipo psíquico 		???? 	Obemu 	Ohbem 	Humanoide 					112 	
607 	Litwick 	Tipo fantasma 	Tipo fuego 	???? 	Hitomoshi 	Hitomoshi 	Amorfo 					113 	065MO
608 	Lampent 	Tipo fantasma 	Tipo fuego 	????? 	Ranpura 	Ranpuraa 	Amorfo 					114 	066MO
609 	Chandelure 	Tipo fantasma 	Tipo fuego 	????? 	Shandera 	Shandera 	Amorfo 					115 	067MO
610 	Axew 	Tipo dragón 		??? 	Kibago 	Kibago 	Monstruo 	Dragón 				116 	148CE
611 	Fraxure 	Tipo dragón 		???? 	Onondo 	Onondo 	Monstruo 	Dragón 				117 	149CE
612 	Haxorus 	Tipo dragón 		????? 	Ononokusu 	Ononokus 	Monstruo 	Dragón 				118 	150CE
613 	Cubchoo 	Tipo hielo 		????? 	Kumashun 	Kumasyun 	Campo 					119 	081MO
614 	Beartic 	Tipo hielo 		????? 	Tsunbea 	Tunbear 	Campo 					120 	082MO
615 	Cryogonal 	Tipo hielo 		????? 	Furijio 	Freegeo 	Mineral 					121 	111MO
616 	Shelmet 	Tipo bicho 		????? 	Chobomaki 	Chobomaki 	Bicho 					122 	024MO
617 	Accelgor 	Tipo bicho 		????? 	Agiruda 	Agilder 	Bicho 					123 	025MO
618 	Stunfisk 	Tipo tierra 	Tipo eléctrico 	???? 	Maggyo 	Maggyo 	Agua 1 	Amorfo 				124 	039MO
619 	Mienfoo 	Tipo lucha 		????? 	Kojofu 	Kojofu 	Campo 	Humanoide 				125 	003CO
620 	Mienshao 	Tipo lucha 		????? 	Kojondo 	Kojondo 	Campo 	Humanoide 				126 	004CO
621 	Druddigon 	Tipo dragón 		????? 	Kurimugan 	Crimgan 	Dragón 	Monstruo 				127 	141MO
622 	Golett 	Tipo tierra 	Tipo fantasma 	???? 	Gobitto 	Golbit 	Mineral 					128 	091CO
623 	Golurk 	Tipo tierra 	Tipo fantasma 	???? 	Gorugu 	Gorog 	Mineral 					129 	092CO
624 	Pawniard 	Tipo siniestro 	Tipo acero 	???? 	Komatana 	Komatana 	Humanoide 					130 	048MO
625 	Bisharp 	Tipo siniestro 	Tipo acero 	????? 	Kirikizan 	Kirikizan 	Humanoide 					131 	049MO
626 	Bouffalant 	Tipo normal 		????? 	Baffuron 	Buffron 	Campo 					132 	
627 	Rufflet 	Tipo normal 	Tipo volador 	???? 	Washibon 	Washibon 	Volador 					133 	
628 	Braviary 	Tipo normal 	Tipo volador 	????? 	Woguru 	Warrgle 	Volador 					134 	
629 	Vullaby 	Tipo siniestro 	Tipo volador 	????? 	Baruchai 	Valchai 	Volador 					135 	
630 	Mandibuzz 	Tipo siniestro 	Tipo volador 	????? 	Barujina 	Vulgina 	Volador 					136 	
631 	Heatmor 	Tipo fuego 		????? 	Kuitaran 	Kuitaran 	Campo 					137 	105MO
632 	Durant 	Tipo bicho 	Tipo acero 	????? 	Aianto 	Aiant 	Bicho 					138 	106MO
633 	Deino 	Tipo siniestro 	Tipo dragón 	??? 	Monozu 	Monozu 	Dragón 					139 	142MO
634 	Zweilous 	Tipo siniestro 	Tipo dragón 	???? 	Jiheddo 	Jihead 	Dragón 					140 	143MO
635 	Hydreigon 	Tipo siniestro 	Tipo dragón 	????? 	Sazandora 	Sazandora 	Dragón 					141 	144MO
636 	Larvesta 	Tipo bicho 	Tipo fuego 	???? 	Meraruba 	Meraruda 	Bicho 					142 	
637 	Volcarona 	Tipo bicho 	Tipo fuego 	????? 	Urugamosu 	Urgamoth 	Bicho 					143 	
638 	Cobalion 	Tipo acero 	Tipo lucha 	????? 	Kobaruon 	Cobalon 	Ninguno 					144 	
639 	Terrakion 	Tipo roca 	Tipo lucha 	????? 	Terakion 	Terrakion 	Ninguno 					145 	
640 	Virizion 	Tipo planta 	Tipo lucha 	????? 	Birijion 	Virizion 	Ninguno 					146 	
641 	Tornadus 	Tipo volador 		????? 	Torunerosu 	Tornelos 	Ninguno 					147 	
642 	Thundurus 	Tipo eléctrico 	Tipo volador 	????? 	Borutorosu 	Voltolos 	Ninguno 					148 	
643 	Reshiram 	Tipo dragón 	Tipo fuego 	???? 	Reshiramu 	Reshiram 	Ninguno 					149 	
644 	Zekrom 	Tipo dragón 	Tipo eléctrico 	???? 	Zekuromu 	Zekrom 	Ninguno 					150 	
645 	Landorus 	Tipo tierra 	Tipo volador 	????? 	Randorosu 	Landlos 	Ninguno 					151 	
646 	Kyurem 	Tipo dragón 	Tipo hielo 	???? 	Kyuremu 	Kyurem 	Ninguno 					152 	
647 	Keldeo 	Tipo agua 	Tipo lucha 	????? 	Kerudio 	Keldeo 	Ninguno 					153 	
648 	Meloetta 	Tipo normal 	Tipo psíquico 	????? 	Meroetta 	Meloia 	Ninguno 					154 	
649 	Genesect 	Tipo bicho 	Tipo acero 	????? 	Genosekuto 	Genosect 	Ninguno 					155 	
650 	Chespin 	Tipo planta 		????? 	Harimaron 	Harimaron 	Campo 						001CE
651 	Quilladin 	Tipo planta 		????? 	Haribogu 	Hariboogu 	Campo 						002CE
652 	Chesnaught 	Tipo planta 	Tipo lucha 	????? 	Burigaron 	Brigarron 	Campo 						003CE
653 	Fennekin 	Tipo fuego 		???? 	Fokko 	Fokko 	Campo 						004CE
654 	Braixen 	Tipo fuego 		????? 	Teruna 	Teerunaa 	Campo 						005CE
655 	Delphox 	Tipo fuego 	Tipo psíquico 	?????? 	Mafokushi 	Mahoxy 	Campo 						006CE
656 	Froakie 	Tipo agua 		???? 	Keromatsu 	Keromatsu 	Agua 1 						007CE
657 	Frogadier 	Tipo agua 		????? 	Gekogashira 	Gekogashira 	Agua 1 						008CE
658 	Greninja 	Tipo agua 	Tipo siniestro 	????? 	Gekkouga 	Gekkouga 	Agua 1 						009CE
659 	Bunnelby 	Tipo normal 		???? 	Horubi 		Campo 						010CE
660 	Diggersby 	Tipo normal 	Tipo tierra 	???? 	Horudo 		Campo 						011CE
661 	Fletchling 	Tipo normal 	Tipo volador 	???? 	Yayakoma 	Yayakoma 	Volador 						014CE
662 	Fletchinder 	Tipo fuego 	Tipo volador 	????? 	Hinoyakoma 	Hinoyakoma 	Volador 						015CE
663 	Talonflame 	Tipo fuego 	Tipo volador 	?????? 	Faiaro 	Firearrow 	Volador 						016CE
664 	Scatterbug 	Tipo bicho 		????? 	Kofukimushi 	Kofukimushi 	Bicho 						020CE
665 	Spewpa 	Tipo bicho 		????? 	Kofurai 		Bicho 						021CE
666 	Vivillon 	Tipo bicho 	Tipo volador 	???? 	Bibiyon 	Viviyon 	Bicho 						022CE
667 	Litleo 	Tipo fuego 	Tipo normal 	??? 	Shishiko 	Shishiko 	Campo 						057CE
668 	Pyroar 	Tipo fuego 	Tipo normal 	????? 	Kaenjishi 	Kaenjishi 	Campo 						058CE
669 	Flabébé 	Tipo hada 		???? 	Furabebe 	Flabebe 	Hada 						068CE
670 	Floette 	Tipo hada 		????? 	Furaette 	Flaette 	Hada 						069CE
671 	Florges 	Tipo hada 		?????? 	Furajesu 	Florges 	Hada 						070CE
672 	Skiddo 	Tipo planta 		????? 	Meekuru 		Campo 						089CE
673 	Gogoat 	Tipo planta 		????? 	Gogoto 	Gogoat 	Campo 						090CE
674 	Pancham 	Tipo lucha 		????? 	Yanchamu 	Yancham 	Campo 	Humanoide 					091CE
675 	Pangoro 	Tipo lucha 	Tipo siniestro 	???? 	Goronda 	Goronda 	Campo 	Humanoide 					092CE
676 	Furfrou 	Tipo normal 		????? 	Torimian 		Campo 						093CE
677 	Espurr 	Tipo psíquico 		????? 	Nyasupa 	Nyasper 	Campo 						114CE
678 	Meowstic 	Tipo psíquico 		?????? 	Nyaonikusu 	Nyaonix 	Campo 						115CE
679 	Honedge 	Tipo acero 	Tipo fantasma 	???? 	Hitotsuki 	Hitotsuki 	Mineral 						117CE
680 	Doublade 	Tipo acero 	Tipo fantasma 	????? 	Nidangiru 		Mineral 						118CE
681 	Aegislash 	Tipo acero 	Tipo fantasma 	????? 	Girogarudo 		Mineral 						118CE
682 	Spritzee 	Tipo hada 		????? 	Shushuppu 	Shushupu 	Hada 						129CE
683 	Aromatisse 	Tipo hada 		????? 	Furefuwan 		Hada 						130CE
684 	Swirlix 	Tipo hada 		????? 	Peroppafu 	Peroppafu 	Hada 						131CE
685 	Slurpuff 	Tipo hada 		????? 	Perorimu 	Peroream 	Hada 						132CE
686 	Inkay 	Tipo siniestro 	Tipo psíquico 	????? 	Maika 	Maaiika 	Agua 1 	Agua 2 					010CO
687 	Malamar 	Tipo siniestro 	Tipo psíquico 	????? 	Karamanero 	Calamanero 	Agua 1 	Agua 2 					011CO
688 	Binacle 	Tipo roca 	Tipo agua 	???? 	Kametete 	Kametete 	Agua 3 						021CO
689 	Barbaracle 	Tipo roca 	Tipo agua 	????? 	Gamenodesu 	Gamenodesu 	Agua 3 						022CO
690 	Skrelp 	Tipo veneno 	Tipo agua 	???? 	Kuzumo 		Agua 1 	Dragón 					030CO
691 	Dragalge 	Tipo veneno 	Tipo dragón 	????? 	Doramidoro 	Doramidoro 	Agua 1 	Dragón 					031CO
692 	Clauncher 	Tipo agua 		????? 	Udeppou 		Agua 1 	Agua 3 					032CO
693 	Clawitzer 	Tipo agua 		????? 	Burosuta 		Agua 1 	Agua 3 					033CO
694 	Helioptile 	Tipo eléctrico 	Tipo normal 	????? 	Erikiteru 	Erikiteru 	Monstruo 	Dragón 					046CO
695 	Heliolisk 	Tipo eléctrico 	Tipo normal 	????? 	Erezado 	Elezard 	Monstruo 	Dragón 					047CO
696 	Tyrunt 	Tipo roca 	Tipo dragón 	???? 	Chigorasu 		Monstruo 	Dragón 					064CO
697 	Tyrantrum 	Tipo roca 	Tipo dragón 	????? 	Gachigorasu 		Monstruo 	Dragón 					065CO
698 	Amaura 	Tipo roca 	Tipo hielo 	???? 	Amarusu 	Amarus 	Monstruo 						066CO
699 	Aurorus 	Tipo roca 	Tipo hielo 	????? 	Amaruruga 		Monstruo 						067CO
700 	Sylveon 	Tipo hada 		????? 	Ninfia 	Nymphia 	Campo 						085CO
701 	Hawlucha 	Tipo lucha 	Tipo volador 	????? 	Ruchaburu 		Humanoide 						089CO
702 	Dedenne 	Tipo eléctrico 	Tipo hada 	???? 	Dedenne 	Dedenne 	Campo 	Hada 					110CO
703 	Carbink 	Tipo roca 	Tipo hada 	???? 	Mereshi 	Melecie 	Hada 	Mineral 					124CO
704 	Goomy 	Tipo dragón 		??? 	Numera 	Numera 	Dragón 						019MO
705 	Sliggoo 	Tipo dragón 		???? 	Numeiru 	Numeiru 	Dragón 						020MO
706 	Goodra 	Tipo dragón 		????? 	Numerugon 	Numerugon 	Dragón 						021MO
707 	Klefki 	Tipo acero 	Tipo hada 	????? 	Kureffi 	Cleffy 	Mineral 						050MO
708 	Phantump 	Tipo fantasma 	Tipo planta 	???? 	Bokure 		Planta 	Amorfo 					061MO
709 	Trevenant 	Tipo fantasma 	Tipo planta 	????? 	Orotto 		Planta 	Amorfo 					062MO
710 	Pumpkaboo 	Tipo fantasma 	Tipo planta 	????? 	Baketcha 		Amorfo 						063MO
711 	Gourgeist 	Tipo fantasma 	Tipo planta 	????? 	Panpujin 	Panpujin 	Amorfo 						064MO
712 	Bergmite 	Tipo hielo 		????? 	Kachikoru 		Monstruo 						079MO
713 	Avalugg 	Tipo hielo 		????? 	Kurebesu 		Monstruo 						080MO
714 	Noibat 	Tipo volador 	Tipo dragón 	????? 	Onbatto 	Onbat 	Volador 						113MO
715 	Noivern 	Tipo volador 	Tipo dragón 	????? 	Onban 	Onvern 	Volador 						114MO
716 	Xerneas 	Tipo hada 		????? 	Zeruneasu 	Xerneas 	Ninguno 						148MO
717 	Yveltal 	Tipo siniestro 	Tipo volador 	????? 	Iberutaru 	Yveltal 	Ninguno 						149MO
718 	Zygarde 	Tipo dragón 	Tipo tierra 	???? 	Jigarude 	Zygarde 	Ninguno 						150MO
719 	Diancie 	Tipo roca 	Tipo hada 	?????? 	Dianshi 	Diancie 	Ninguno 						151CE
720 	Hoopa 	Tipo psíquico 	Tipo fantasma 	??? 	Fuupa 		Ninguno 						152CE
721 	Volcanion 	Tipo fuego 	Tipo agua 	?????? 	Borukenion 		Ninguno 						153CE"""

main()
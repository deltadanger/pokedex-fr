# -*- coding: utf-8 -*- 

def main():
    mapping = []
    for row in data.split("\n"):
        name = row.split("\t")[2].strip()
        
        std_name = "name_"+name.strip()\
        .lower()\
        .replace(" ", "_")\
        .replace("-", "_")\
        .replace("(", "")\
        .replace(")", "")\
        .replace("'", "")\
        .replace(".", "")\
        .replace("�", "e")\
        .replace("�", "e")\
        .replace("�", "e")\
        .replace("�", "a")\
        .replace("�", "a")\
        .replace("�", "i")\
        .replace("�", "o")\
        .replace("�", "c")\
        .replace("�", "oe")\
        .replace("�", "e")
        
        if std_name in existing_names:
            mapping.append((std_name, name.replace("'", "\\'")))
        else:
            print std_name
    
    for m in mapping:
        print "    <string name=\"{}\">{}</string>".format(*m)
    

existing_names = ['name_raticate','name_porygon_z','name_scraggy','name_exeggutor','name_braviary','name_shuppet','name_amoonguss','name_kingdra','name_electivire','name_braixen','name_cinccino','name_emolga','name_golem','name_cresselia','name_simipour','name_pelipper','name_dewott','name_shieldon','name_absol','name_azurill','name_vespiquen','name_charizard','name_deino','name_rotom_fan_rotom','name_magcargo','name_tornadus_therian_forme','name_meloetta_aria_forme','name_snubbull','name_sharpedo','name_rotom_frost_rotom','name_mega_mewtwo_y','name_yamask','name_dusknoir','name_clefable','name_mega_mewtwo_x','name_celebi','name_aromatisse','name_zorua','name_mega_manectric','name_karrablast','name_wynaut','name_horsea','name_sylveon','name_skrelp','name_mega_pinsir','name_quagsire','name_mega_venusaur','name_butterfree','name_timburr','name_doduo','name_toxicroak','name_medicham','name_jolteon','name_pumpkaboo_large_size','name_wormadam_trash_cloak','name_aegislash_blade_forme','name_bellossom','name_ralts','name_pawniard','name_lairon','name_weezing','name_drifloon','name_flygon','name_pineco','name_chingling','name_quilladin','name_mime_jr','name_smeargle','name_miltank','name_linoone','name_cubone','name_bibarel','name_hypno','name_lileep','name_rotom_mow_rotom','name_cranidos','name_mamoswine','name_stunky','name_garbodor','name_heatmor','name_makuhita','name_stantler','name_alakazam','name_mega_charizard_x','name_charmeleon','name_tirtouga','name_seadra','name_turtwig','name_snorunt','name_escavalier','name_whismur','name_rotom_normal_rotom','name_magmortar','name_slakoth','name_mareep','name_binacle','name_prinplup','name_tynamo','name_plusle','name_aegislash_shield_forme','name_elekid','name_talonflame','name_baltoy','name_yanma','name_pidove','name_eelektrik','name_kirlia','name_ducklett','name_oddish','name_metang','name_gastrodon','name_dragonite','name_lilligant','name_genesect','name_nidorino','name_banette','name_nidorina','name_rhydon','name_regigigas','name_tentacruel','name_petilil','name_darmanitan_zen_mode','name_mankey','name_slowbro','name_kricketot','name_florges','name_pinsir','name_spinarak','name_dodrio','name_chatot','name_scatterbug','name_basculin','name_metapod','name_electrode','name_vanillite','name_glaceon','name_gulpin','name_golett','name_trubbish','name_togepi','name_honchkrow','name_pansear','name_staravia','name_ekans','name_spheal','name_octillery','name_pansage','name_zygarde','name_pikachu','name_zoroark','name_mega_mawile','name_roggenrola','name_rhyperior','name_mega_gardevoir','name_mega_blaziken','name_seedot','name_qwilfish','name_garchomp','name_latios','name_grumpig','name_wormadam_plant_cloak','name_glalie','name_steelix','name_mesprit','name_zapdos','name_phanpy','name_uxie','name_gloom','name_metagross','name_azumarill','name_kyogre','name_mega_banette','name_gligar','name_wurmple','name_electabuzz','name_vigoroth','name_chansey','name_furret','name_sudowoodo','name_beartic','name_maractus','name_aurorus','name_scyther','name_buneary','name_hoot_hoot','name_lapras','name_spiritomb','name_slugma','name_paras','name_larvesta','name_reuniclus','name_cleffa','name_servine','name_treecko','name_bronzor','name_gourgeist_average_size','name_misdreavus','name_mega_blastoise','name_venipede','name_cottonee','name_dewgong','name_parasect','name_swalot','name_voltorb','name_magikarp','name_darmanitan_standard_mode','name_swellow','name_ferrothorn','name_swampert','name_mudkip','name_farfetchd','name_groudon','name_abomasnow','name_sunkern','name_nidoqueen','name_altaria','name_pidgey','name_croagunk','name_houndour','name_mandibuzz','name_togekiss','name_tympole','name_skuntank','name_piplup','name_illumise','name_gabite','name_klinklang','name_giratina_origin_forme','name_torchic','name_accelgor','name_heliolisk','name_burmy','name_hitmontop','name_pachirisu','name_marill','name_mega_lucario','name_skitty','name_abra','name_swadloon','name_wigglytuff','name_tyrunt','name_kecleon','name_deoxys_speed_forme','name_cloyster','name_rotom_heat_rotom','name_helioptile','name_spritzee','name_sawsbuck','name_kyurem_black_kyurem','name_hippopotas','name_giratina_altered_forme','name_kakuna','name_exeggcute','name_zigzagoon','name_rattata','name_girafarig','name_seel','name_granbull','name_kabutops','name_patrat','name_wormadam_sandy_cloak','name_bulbasaur','name_furfrou','name_mega_houndoom','name_gothitelle','name_dedenne','name_ivysaur','name_shinx','name_pidgeot','name_nosepass','name_fearow','name_larvitar','name_togetic','name_mega_aggron','name_exploud','name_mantyke','name_swoobat','name_venusaur','name_samurott','name_snorlax','name_kyurem_white_kyurem','name_muk','name_poliwag','name_espeon','name_conkeldurr','name_staryu','name_archen','name_krookodile','name_heatran','name_ponyta','name_azelf','name_krokorok','name_hariyama','name_wobbuffet','name_starmie','name_cryogonal','name_smoochum','name_bastiodon','name_spewpa','name_carvanha','name_ampharos','name_mega_medicham','name_tangrowth','name_sunflora','name_clawitzer','name_chimecho','name_hawlucha','name_rufflet','name_gogoat','name_simisear','name_vivillon','name_noibat','name_vulpix','name_graveler','name_crobat','name_bellsprout','name_rotom_wash_rotom','name_lumineon','name_frogadier','name_rhyhorn','name_gyarados','name_sigilyph','name_spoink','name_dialga','name_sandshrew','name_electrike','name_pichu','name_terrakion','name_amaura','name_goldeen','name_magby','name_whimsicott','name_lopunny','name_chinchou','name_manectric','name_gourgeist_super_size','name_keldeo','name_sceptile','name_tornadus_incarnate_forme','name_registeel','name_xatu','name_duskull','name_starly','name_venomoth','name_blastoise','name_mega_scizor','name_dratini','name_hydreigon','name_clefairy','name_dwebble','name_torterra','name_drilbur','name_cherubi','name_bidoof','name_nidoran_f','name_litleo','name_entei','name_nidoran_m','name_oshawott','name_galvantula','name_drowzee','name_doublade','name_riolu','name_weedle','name_swinub','name_mawile','name_torkoal','name_excadrill','name_masquerain','name_yanmega','name_kricketune','name_whirlipede','name_grovyle','name_blaziken','name_malamar','name_vullaby','name_marowak','name_skiddo','name_lombre','name_combee','name_taillow','name_minccino','name_arceus','name_mega_aerodactyl','name_kadabra','name_regirock','name_deoxys_attack_forme','name_politoed','name_bunnelby','name_cacturne','name_raichu','name_seaking','name_vibrava','name_cradily','name_deerling','name_grimer','name_unown','name_combusken','name_beedrill','name_cubchoo','name_swablu','name_emboar','name_leavanny','name_murkrow','name_beldum','name_mienshao','name_mothim','name_gastly','name_swanna','name_trapinch','name_blissey','name_grotle','name_rampardos','name_gigalith','name_pidgeotto','name_finneon','name_joltik','name_dusclops','name_vaporeon','name_boldore','name_dragonair','name_magnezone','name_roselia','name_slaking','name_spinda','name_poliwrath','name_palkia','name_darumaka','name_munna','name_tauros','name_staraptor','name_bouffalant','name_raikou','name_empoleon','name_cyndaquil','name_arbok','name_gothorita','name_monferno','name_psyduck','name_weepinbell','name_porygon2','name_walrein','name_golduck','name_hitmonchan','name_munchlax','name_gible','name_swirlix','name_shelmet','name_honedge','name_delphox','name_sableye','name_buizel','name_golbat','name_throh','name_relicanth','name_musharna','name_happiny','name_clamperl','name_eelektross','name_phantump','name_budew','name_bisharp','name_sealeo','name_beheeyem','name_woobat','name_floatzel','name_dunsparce','name_mega_tyranitar','name_shedinja','name_druddigon','name_vanilluxe','name_mega_abomasnow','name_zekrom','name_remoraid','name_alomomola','name_duosion','name_umbreon','name_mega_ampharos','name_slowpoke','name_slurpuff','name_wartortle','name_whiscash','name_tranquill','name_scrafty','name_loudred','name_hitmonlee','name_teddiursa','name_sawk','name_huntail','name_porygon','name_stoutland','name_volcarona','name_serperior','name_cascoon','name_lotad','name_forretress','name_venonat','name_jynx','name_minun','name_mega_gyarados','name_mega_charizard_y','name_sliggoo','name_chimchar','name_tepig','name_gallade','name_panpour','name_pancham','name_goodra','name_chesnaught','name_lampent','name_virizion','name_sentret','name_trevenant','name_seviper','name_chikorita','name_lillipup','name_typhlosion','name_landorus_incarnate_forme','name_ninetales','name_magnemite','name_cobalion','name_persian','name_nidoking','name_ninjask','name_greninja','name_pyroar','name_poochyena','name_eevee','name_barboach','name_kabuto','name_froakie','name_claydol','name_tyrogue','name_nincada','name_ambipom','name_klink','name_spearow','name_camerupt','name_wingull','name_litwick','name_barbaracle','name_reshiram','name_lickitung','name_poliwhirl','name_mega_gengar','name_clauncher','name_feraligatr','name_mismagius','name_luxray','name_gorebyss','name_aron','name_aerodactyl','name_rapidash','name_slowking','name_jirachi','name_pumpkaboo_small_size','name_chespin','name_sandile','name_squirtle','name_zangoose','name_latias','name_mightyena','name_lugia','name_onix','name_flareon','name_magneton','name_fraxure','name_shellder','name_geodude','name_crawdaunt','name_dustox','name_manaphy','name_croconaw','name_gengar','name_solosis','name_carnivine','name_corphish','name_ledian','name_chandelure','name_jellicent','name_delcatty','name_floette','name_cofagrigus','name_meditite','name_audino','name_fennekin','name_bronzong','name_wooper','name_bayleef','name_vileplume','name_shuckle','name_shaymin_sky_forme','name_herdier','name_nuzleaf','name_igglybuff','name_sandslash','name_gourgeist_small_size','name_bagon','name_rayquaza','name_hoppip','name_luxio','name_cherrim','name_weavile','name_omanyte','name_sewaddle','name_kingler','name_palpitoad','name_tentacool','name_hippowdon','name_wailmer','name_magmar','name_growlithe','name_lunatone','name_lucario','name_machoke','name_feebas','name_silcoon','name_drapion','name_lickilicky','name_probopass','name_luvdisc','name_tangela','name_shiftry','name_golurk','name_zweilous','name_leafeon','name_meowstic','name_pignite','name_tropius','name_breloom','name_victini','name_pupitar','name_articuno','name_phione','name_meowth','name_fletchinder','name_ariados','name_bonsly','name_zubat','name_surskit','name_totodile','name_beautifly','name_blitzle','name_axew','name_volbeat','name_scizor','name_dugtrio','name_skiploom','name_gurdurr','name_darkrai','name_mew','name_ferroseed','name_shroomish','name_dragalge','name_glameow','name_xerneas','name_delibird','name_mega_kangaskhan','name_charmander','name_lanturn','name_infernape','name_noivern','name_goomy','name_purugly','name_archeops','name_sneasel','name_jumpluff','name_jigglypuff','name_vanillish','name_omastar','name_klang','name_meganium','name_deoxys_defense_forme','name_frillish','name_ditto','name_kangaskhan','name_pumpkaboo_average_size','name_wailord','name_primeape','name_yveltal','name_thundurus_therian_forme','name_corsola','name_machamp','name_skorupi','name_simisage','name_ursaring','name_anorith','name_snivy','name_gardevoir','name_heracross','name_houndoom','name_seismitoad','name_crustle','name_haxorus','name_mewtwo','name_quilava','name_aggron','name_watchog','name_tyranitar','name_gliscor','name_mantine','name_solrock','name_fletchling','name_mega_heracross','name_marshtomp','name_piloswine','name_roserade','name_numel','name_purrloin','name_espurr','name_gothita','name_mienfoo','name_froslass','name_liepard','name_ho_oh','name_krabby','name_suicune','name_zebstrika','name_diggersby','name_donphan','name_bergmite','name_pumpkaboo_super_size','name_snover','name_mega_absol','name_carbink','name_klefki','name_castform','name_skarmory','name_mr_mime','name_natu','name_flaaffy','name_mega_garchomp','name_ledyba','name_shaymin_land_forme','name_gourgeist_large_size','name_cacnea','name_koffing','name_arcanine','name_milotic','name_diglett','name_aipom','name_thundurus_incarnate_forme','name_machop','name_ludicolo','name_noctowl','name_meloetta_pirouette_forme','name_inkay','name_durant','name_regice','name_armaldo','name_elgyem','name_shellos','name_landorus_therian_forme','name_foongus','name_victreebel','name_shelgon','name_caterpie','name_stunfisk','name_drifblim','name_flabebe','name_mega_alakazam','name_scolipede','name_deoxys_normal_forme','name_carracosta','name_unfezant','name_haunter','name_pangoro','name_tyrantrum','name_moltres','name_salamence','name_avalugg','name_kyurem']

data = """001 	001 	Bulbasaur 	45 	49 	49 	65 	65 	45 	318 	53
002 	002 	Ivysaur 	60 	62 	63 	80 	80 	60 	405 	67.5
003 	003 	Venusaur 	80 	82 	83 	100 	100 	80 	525 	87.5
		Mega Venusaur
004 	004 	Charmander 	39 	52 	43 	60 	50 	65 	309 	51.5
005 	005 	Charmeleon 	58 	64 	58 	80 	65 	80 	405 	67.5
006 	006 	Charizard 	78 	84 	78 	109 	85 	100 	534 	89
		Mega Charizard X
		Mega Charizard Y
007 	007 	Squirtle 	44 	48 	65 	50 	64 	43 	314 	52.33
008 	008 	Wartortle 	59 	63 	80 	65 	80 	58 	405 	67.5
009 	009 	Blastoise 	79 	83 	100 	85 	105 	78 	530 	88.33
		Mega Blastoise
010 	010 	Caterpie 	45 	30 	35 	20 	20 	45 	195 	32.5
011 	011 	Metapod 	50 	20 	55 	25 	25 	30 	205 	34.17
012 	012 	Butterfree 	60 	45 	50 	90 	80 	70 	395 	65.83
013 	013 	Weedle 	40 	35 	30 	20 	20 	50 	195 	32.5
014 	014 	Kakuna 	45 	25 	50 	25 	25 	35 	205 	34.17
015 	015 	Beedrill 	65 	90 	40 	45 	80 	75 	395 	65.83
016 	016 	Pidgey 	40 	45 	40 	35 	35 	56 	251 	41.83
017 	017 	Pidgeotto 	63 	60 	55 	50 	50 	71 	349 	58.17
018 	018 	Pidgeot 	83 	80 	75 	70 	70 	101 	479 	79.83
019 	019 	Rattata 	30 	56 	35 	25 	35 	72 	253 	42.17
020 	020 	Raticate 	55 	81 	60 	50 	70 	97 	413 	68.83
021 	021 	Spearow 	40 	60 	30 	31 	31 	70 	262 	43.67
022 	022 	Fearow 	65 	90 	65 	61 	61 	100 	442 	73.67
023 	023 	Ekans 	35 	60 	44 	40 	54 	55 	288 	48
024 	024 	Arbok 	60 	85 	69 	65 	79 	80 	438 	73
025 	025 	Pikachu 	35 	55 	40 	50 	50 	90 	320 	53.33
026 	026 	Raichu 	60 	90 	55 	90 	80 	110 	485 	80.83
027 	027 	Sandshrew 	50 	75 	85 	20 	30 	40 	300 	50
028 	028 	Sandslash 	75 	100 	110 	45 	55 	65 	450 	75
029 	029 	Nidoran m 	55 	47 	52 	40 	40 	41 	275 	45.83
030 	030 	Nidorina 	70 	62 	67 	55 	55 	56 	365 	60.83
031 	031 	Nidoqueen 	90 	92 	87 	75 	85 	76 	505 	84.17
032 	032 	Nidoran f 	46 	57 	40 	40 	40 	50 	273 	45.5
033 	033 	Nidorino 	61 	72 	57 	55 	55 	65 	365 	60.83
034 	034 	Nidoking 	81 	102 	77 	85 	75 	85 	505 	84.17
035 	035 	Clefairy 	70 	45 	48 	60 	65 	35 	323 	53.83
036 	036 	Clefable 	95 	70 	73 	95 	90 	60 	483 	80.5
037 	037 	Vulpix 	38 	41 	40 	50 	65 	65 	299 	49.83
038 	038 	Ninetales 	73 	76 	75 	81 	100 	100 	505 	84.17
039 	039 	Jigglypuff 	115 	45 	20 	45 	25 	20 	270 	45
040 	040 	Wigglytuff 	140 	70 	45 	85 	50 	45 	435 	72.5
041 	041 	Zubat 	40 	45 	35 	30 	40 	55 	245 	40.83
042 	042 	Golbat 	75 	80 	70 	65 	75 	90 	455 	75.83
043 	043 	Oddish 	45 	50 	55 	75 	65 	30 	320 	53.33
044 	044 	Gloom 	60 	65 	70 	85 	75 	40 	395 	65.83
045 	045 	Vileplume 	75 	80 	85 	110 	90 	50 	490 	81.67
046 	046 	Paras 	35 	70 	55 	45 	55 	25 	285 	47.5
047 	047 	Parasect 	60 	95 	80 	60 	80 	30 	405 	67.5
048 	048 	Venonat 	60 	55 	50 	40 	55 	45 	305 	50.83
049 	049 	Venomoth 	70 	65 	60 	90 	75 	90 	450 	75
050 	050 	Diglett 	10 	55 	25 	35 	45 	95 	265 	44.17
051 	051 	Dugtrio 	35 	80 	50 	50 	70 	120 	405 	67.5
052 	052 	Meowth 	40 	45 	35 	40 	40 	90 	290 	48.33
053 	053 	Persian 	65 	70 	60 	65 	65 	115 	440 	73.33
054 	054 	Psyduck 	50 	52 	48 	65 	50 	55 	320 	53.33
055 	055 	Golduck 	80 	82 	78 	95 	80 	85 	500 	83.33
056 	056 	Mankey 	40 	80 	35 	35 	45 	70 	305 	50.83
057 	057 	Primeape 	65 	105 	60 	60 	70 	95 	455 	75.83
058 	058 	Growlithe 	55 	70 	45 	70 	50 	60 	350 	58.33
059 	059 	Arcanine 	90 	110 	80 	100 	80 	95 	555 	92.5
060 	060 	Poliwag 	40 	50 	40 	40 	40 	90 	300 	50
061 	061 	Poliwhirl 	65 	65 	65 	50 	50 	90 	385 	64.17
062 	062 	Poliwrath 	90 	95 	95 	70 	90 	70 	510 	85
063 	063 	Abra 	25 	20 	15 	105 	55 	90 	310 	51.67
064 	064 	Kadabra 	40 	35 	30 	120 	70 	105 	400 	66.67
065 	065 	Alakazam 	55 	50 	45 	135 	95 	120 	500 	83.33
		Mega Alakazam
066 	066 	Machop 	70 	80 	50 	35 	35 	35 	305 	50.83
067 	067 	Machoke 	80 	100 	70 	50 	60 	45 	405 	67.5
068 	068 	Machamp 	90 	130 	80 	65 	85 	55 	505 	84.17
069 	069 	Bellsprout 	50 	75 	35 	70 	30 	40 	300 	50
070 	070 	Weepinbell 	65 	90 	50 	85 	45 	55 	390 	65
071 	071 	Victreebel 	80 	105 	65 	100 	70 	70 	490 	81.67
072 	072 	Tentacool 	40 	40 	35 	50 	100 	70 	335 	55.83
073 	073 	Tentacruel 	80 	70 	65 	80 	120 	100 	515 	85.83
074 	074 	Geodude 	40 	80 	100 	30 	30 	20 	300 	50
075 	075 	Graveler 	55 	95 	115 	45 	45 	35 	390 	65
076 	076 	Golem 	80 	120 	130 	55 	65 	45 	495 	82.5
077 	077 	Ponyta 	50 	85 	55 	65 	65 	90 	410 	68.33
078 	078 	Rapidash 	65 	100 	70 	80 	80 	105 	500 	83.33
079 	079 	Slowpoke 	90 	65 	65 	40 	40 	15 	315 	52.5
080 	080 	Slowbro 	95 	75 	110 	100 	80 	30 	490 	81.67
081 	081 	Magnemite 	25 	35 	70 	95 	55 	45 	325 	54.17
082 	082 	Magneton 	50 	60 	95 	120 	70 	70 	465 	77.5
083 	083 	Farfetch'd 	52 	65 	55 	58 	62 	60 	352 	58.67
084 	084 	Doduo 	35 	85 	45 	35 	35 	75 	310 	51.67
085 	085 	Dodrio 	60 	110 	70 	60 	60 	100 	460 	76.67
086 	086 	Seel 	65 	45 	55 	45 	70 	45 	325 	54.17
087 	087 	Dewgong 	90 	70 	80 	70 	95 	70 	475 	79.17
088 	088 	Grimer 	80 	80 	50 	40 	50 	25 	325 	54.17
089 	089 	Muk 	105 	105 	75 	65 	100 	50 	500 	83.33
090 	090 	Shellder 	30 	65 	100 	45 	25 	40 	305 	50.83
091 	091 	Cloyster 	50 	95 	180 	85 	45 	70 	525 	87.5
092 	092 	Gastly 	30 	35 	30 	100 	35 	80 	310 	51.67
093 	093 	Haunter 	45 	50 	45 	115 	55 	95 	405 	67.5
094 	094 	Gengar 	60 	65 	60 	130 	75 	110 	500 	83.33
		Mega Gengar
095 	095 	Onix 	35 	45 	160 	30 	45 	70 	385 	64.17
096 	096 	Drowzee 	60 	48 	45 	43 	90 	42 	328 	54.67
097 	097 	Hypno 	85 	73 	70 	73 	115 	67 	483 	80.5
098 	098 	Krabby 	30 	105 	90 	25 	25 	50 	325 	54.17
099 	099 	Kingler 	55 	130 	115 	50 	50 	75 	475 	79.17
100 	100 	Voltorb 	40 	30 	50 	55 	55 	100 	330 	55
101 	101 	Electrode 	60 	50 	70 	80 	80 	140 	480 	80
102 	102 	Exeggcute 	60 	40 	80 	60 	45 	40 	325 	54.17
103 	103 	Exeggutor 	95 	95 	85 	125 	65 	55 	520 	86.67
104 	104 	Cubone 	50 	50 	95 	40 	50 	35 	320 	53.33
105 	105 	Marowak 	60 	80 	110 	50 	80 	45 	425 	70.83
106 	106 	Hitmonlee 	50 	120 	53 	35 	110 	87 	455 	75.83
107 	107 	Hitmonchan 	50 	105 	79 	35 	110 	76 	455 	75.83
108 	108 	Lickitung 	90 	55 	75 	60 	75 	30 	385 	64.17
109 	109 	Koffing 	40 	65 	95 	60 	45 	35 	340 	56.67
110 	110 	Weezing 	65 	90 	120 	85 	70 	60 	490 	81.67
111 	111 	Rhyhorn 	80 	85 	95 	30 	30 	25 	345 	57.5
112 	112 	Rhydon 	105 	130 	120 	45 	45 	40 	485 	80.83
113 	113 	Chansey 	250 	5 	5 	35 	105 	50 	450 	75
114 	114 	Tangela 	65 	55 	115 	100 	40 	60 	435 	72.5
115 	115 	Kangaskhan 	105 	95 	80 	40 	80 	90 	490 	81.67
		Mega Kangaskhan
116 	116 	Horsea 	30 	40 	70 	70 	25 	60 	295 	49.17
117 	117 	Seadra 	55 	65 	95 	95 	45 	85 	440 	73.33
118 	118 	Goldeen 	45 	67 	60 	35 	50 	63 	320 	53.33
119 	119 	Seaking 	80 	92 	65 	65 	80 	68 	450 	75
120 	120 	Staryu 	30 	45 	55 	70 	55 	85 	340 	56.67
121 	121 	Starmie 	60 	75 	85 	100 	85 	115 	520 	86.67
122 	122 	Mr. Mime 	40 	45 	65 	100 	120 	90 	460 	76.67
123 	123 	Scyther 	70 	110 	80 	55 	80 	105 	500 	83.33
124 	124 	Jynx 	65 	50 	35 	115 	95 	95 	455 	75.83
125 	125 	Electabuzz 	65 	83 	57 	95 	85 	105 	490 	81.67
126 	126 	Magmar 	65 	95 	57 	100 	85 	93 	495 	82.5
127 	127 	Pinsir 	65 	125 	100 	55 	70 	85 	500 	83.33
		Mega Pinsir
128 	128 	Tauros 	75 	100 	95 	40 	70 	110 	490 	81.67
129 	129 	Magikarp 	20 	10 	55 	15 	20 	80 	200 	33.33
130 	130 	Gyarados 	95 	125 	79 	60 	100 	81 	540 	90
		Mega Gyarados
131 	131 	Lapras 	130 	85 	80 	85 	95 	60 	535 	89.17
132 	132 	Ditto 	48 	48 	48 	48 	48 	48 	288 	48
133 	133 	Eevee 	55 	55 	50 	45 	65 	55 	325 	54.17
134 	134 	Vaporeon 	130 	65 	60 	110 	95 	65 	525 	87.5
135 	135 	Jolteon 	65 	65 	60 	110 	95 	130 	525 	87.5
136 	136 	Flareon 	65 	130 	60 	95 	110 	65 	525 	87.5
137 	137 	Porygon 	65 	60 	70 	85 	75 	40 	395 	65.83
138 	138 	Omanyte 	35 	40 	100 	90 	55 	35 	355 	59.17
139 	139 	Omastar 	70 	60 	125 	115 	70 	55 	495 	82.5
140 	140 	Kabuto 	30 	80 	90 	55 	45 	55 	355 	59.17
141 	141 	Kabutops 	60 	115 	105 	65 	70 	80 	495 	82.5
142 	142 	Aerodactyl 	80 	105 	65 	60 	75 	130 	515 	85.83
		Mega Aerodactyl
143 	143 	Snorlax 	160 	110 	65 	65 	110 	30 	540 	90
144 	144 	Articuno 	90 	85 	100 	95 	125 	85 	580 	96.67
145 	145 	Zapdos 	90 	90 	85 	125 	90 	100 	580 	96.67
146 	146 	Moltres 	90 	100 	90 	125 	85 	90 	580 	96.67
147 	147 	Dratini 	41 	64 	45 	50 	50 	50 	300 	50
148 	148 	Dragonair 	61 	84 	65 	70 	70 	70 	420 	70
149 	149 	Dragonite 	91 	134 	95 	100 	100 	80 	600 	100
150 	150 	Mewtwo 	106 	110 	90 	154 	90 	130 	680 	113.33
		Mega Mewtwo X
		Mega Mewtwo Y
151 	151 	Mew 	100 	100 	100 	100 	100 	100 	600 	100
152 	152 	Chikorita 	45 	49 	65 	49 	65 	45 	318 	53
153 	153 	Bayleef 	60 	62 	80 	63 	80 	60 	405 	67.5
154 	154 	Meganium 	80 	82 	100 	83 	100 	80 	525 	87.5
155 	155 	Cyndaquil 	39 	52 	43 	60 	50 	65 	309 	51.5
156 	156 	Quilava 	58 	64 	58 	80 	65 	80 	405 	67.5
157 	157 	Typhlosion 	78 	84 	78 	109 	85 	100 	534 	89
158 	158 	Totodile 	50 	65 	64 	44 	48 	43 	314 	52.33
159 	159 	Croconaw 	65 	80 	80 	59 	63 	58 	405 	67.5
160 	160 	Feraligatr 	85 	105 	100 	79 	83 	78 	530 	88.33
161 	161 	Sentret 	35 	46 	34 	35 	45 	20 	215 	35.83
162 	162 	Furret 	85 	76 	64 	45 	55 	90 	415 	69.17
163 	163 	Hoot hoot 	60 	30 	30 	36 	56 	50 	262 	43.67
164 	164 	Noctowl 	100 	50 	50 	76 	96 	70 	442 	73.67
165 	165 	Ledyba 	40 	20 	30 	40 	80 	55 	265 	44.17
166 	166 	Ledian 	55 	35 	50 	55 	110 	85 	390 	65
167 	167 	Spinarak 	40 	60 	40 	40 	40 	30 	250 	41.67
168 	168 	Ariados 	70 	90 	70 	60 	60 	40 	390 	65
169 	169 	Crobat 	85 	90 	80 	70 	80 	130 	535 	89.17
170 	170 	Chinchou 	75 	38 	38 	56 	56 	67 	330 	55
171 	171 	Lanturn 	125 	58 	58 	76 	76 	67 	460 	76.67
172 	172 	Pichu 	20 	40 	15 	35 	35 	60 	205 	34.17
173 	173 	Cleffa 	50 	25 	28 	45 	55 	15 	218 	36.33
174 	174 	Igglybuff 	90 	30 	15 	40 	20 	15 	210 	35
175 	175 	Togepi 	35 	20 	65 	40 	65 	20 	245 	40.83
176 	176 	Togetic 	55 	40 	85 	80 	105 	40 	405 	67.5
177 	177 	Natu 	40 	50 	45 	70 	45 	70 	320 	53.33
178 	178 	Xatu 	65 	75 	70 	95 	70 	95 	470 	78.33
179 	179 	Mareep 	55 	40 	40 	65 	45 	35 	280 	46.67
180 	180 	Flaaffy 	70 	55 	55 	80 	60 	45 	365 	60.83
181 	181 	Ampharos 	90 	75 	85 	115 	90 	55 	510 	85
		Mega Ampharos
182 	182 	Bellossom 	75 	80 	95 	90 	100 	50 	490 	81.67
183 	183 	Marill 	70 	20 	50 	20 	50 	40 	250 	41.67
184 	184 	Azumarill 	100 	50 	80 	60 	80 	50 	420 	70
185 	185 	Sudowoodo 	70 	100 	115 	30 	65 	30 	410 	68.33
186 	186 	Politoed 	90 	75 	75 	90 	100 	70 	500 	83.33
187 	187 	Hoppip 	35 	35 	40 	35 	55 	50 	250 	41.67
188 	188 	Skiploom 	55 	45 	50 	45 	65 	80 	340 	56.67
189 	189 	Jumpluff 	75 	55 	70 	55 	95 	110 	460 	76.67
190 	190 	Aipom 	55 	70 	55 	40 	55 	85 	360 	60
191 	191 	Sunkern 	30 	30 	30 	30 	30 	30 	180 	30
192 	192 	Sunflora 	75 	75 	55 	105 	85 	30 	425 	70.83
193 	193 	Yanma 	65 	65 	45 	75 	45 	95 	390 	65
194 	194 	Wooper 	55 	45 	45 	25 	25 	15 	210 	35
195 	195 	Quagsire 	95 	85 	85 	65 	65 	35 	430 	71.67
196 	196 	Espeon 	65 	65 	60 	130 	95 	110 	525 	87.5
197 	197 	Umbreon 	95 	65 	110 	60 	130 	65 	525 	87.5
198 	198 	Murkrow 	60 	85 	42 	85 	42 	91 	405 	67.5
199 	199 	Slowking 	95 	75 	80 	100 	110 	30 	490 	81.67
200 	200 	Misdreavus 	60 	60 	60 	85 	85 	85 	435 	72.5
201 	201 	Unown 	48 	72 	48 	72 	48 	48 	336 	56
202 	202 	Wobbuffet 	190 	33 	58 	33 	58 	33 	405 	67.5
203 	203 	Girafarig 	70 	80 	65 	90 	65 	85 	455 	75.83
204 	204 	Pineco 	50 	65 	90 	35 	35 	15 	290 	48.33
205 	205 	Forretress 	75 	90 	140 	60 	60 	40 	465 	77.5
206 	206 	Dunsparce 	100 	70 	70 	65 	65 	45 	415 	69.17
207 	207 	Gligar 	65 	75 	105 	35 	65 	85 	430 	71.67
208 	208 	Steelix 	75 	85 	200 	55 	65 	30 	510 	85
209 	209 	Snubbull 	60 	80 	50 	40 	40 	30 	300 	50
210 	210 	Granbull 	90 	120 	75 	60 	60 	45 	450 	75
211 	211 	Qwilfish 	65 	95 	75 	55 	55 	85 	430 	71.67
212 	212 	Scizor 	70 	130 	100 	55 	80 	65 	500 	83.33
		Mega Scizor
213 	213 	Shuckle 	20 	10 	230 	10 	230 	5 	505 	84.17
214 	214 	Heracross 	80 	125 	75 	40 	95 	85 	500 	83.33
		Mega Heracross
215 	215 	Sneasel 	55 	95 	55 	35 	75 	115 	430 	71.67
216 	216 	Teddiursa 	60 	80 	50 	50 	50 	40 	330 	55
217 	217 	Ursaring 	90 	130 	75 	75 	75 	55 	500 	83.33
218 	218 	Slugma 	40 	40 	40 	70 	40 	20 	250 	41.67
219 	219 	Magcargo 	50 	50 	120 	80 	80 	30 	410 	68.33
220 	220 	Swinub 	50 	50 	40 	30 	30 	50 	250 	41.67
221 	221 	Piloswine 	100 	100 	80 	60 	60 	50 	450 	75
222 	222 	Corsola 	55 	55 	85 	65 	85 	35 	380 	63.33
223 	223 	Remoraid 	35 	65 	35 	65 	35 	65 	300 	50
224 	224 	Octillery 	75 	105 	75 	105 	75 	45 	480 	80
225 	225 	Delibird 	45 	55 	45 	65 	45 	75 	330 	55
226 	226 	Mantine 	65 	40 	70 	80 	140 	70 	465 	77.5
227 	227 	Skarmory 	65 	80 	140 	40 	70 	70 	465 	77.5
228 	228 	Houndour 	45 	60 	30 	80 	50 	65 	330 	55
229 	229 	Houndoom 	75 	90 	50 	110 	80 	95 	500 	83.33
		Mega Houndoom
230 	230 	Kingdra 	75 	95 	95 	95 	95 	85 	540 	90
231 	231 	Phanpy 	90 	60 	60 	40 	40 	40 	330 	55
232 	232 	Donphan 	90 	120 	120 	60 	60 	50 	500 	83.33
233 	233 	Porygon2 	85 	80 	90 	105 	95 	60 	515 	85.83
234 	234 	Stantler 	73 	95 	62 	85 	65 	85 	465 	77.5
235 	235 	Smeargle 	55 	20 	35 	20 	45 	75 	250 	41.67
236 	236 	Tyrogue 	35 	35 	35 	35 	35 	35 	210 	35
237 	237 	Hitmontop 	50 	95 	95 	35 	110 	70 	455 	75.83
238 	238 	Smoochum 	45 	30 	15 	85 	65 	65 	305 	50.83
239 	239 	Elekid 	45 	63 	37 	65 	55 	95 	360 	60
240 	240 	Magby 	45 	75 	37 	70 	55 	83 	365 	60.83
241 	241 	Miltank 	95 	80 	105 	40 	70 	100 	490 	81.67
242 	242 	Blissey 	255 	10 	10 	75 	135 	55 	540 	90
243 	243 	Raikou 	90 	85 	75 	115 	100 	115 	580 	96.67
244 	244 	Entei 	115 	115 	85 	90 	75 	100 	580 	96.67
245 	245 	Suicune 	100 	75 	115 	90 	115 	85 	580 	96.67
246 	246 	Larvitar 	50 	64 	50 	45 	50 	41 	300 	50
247 	247 	Pupitar 	70 	84 	70 	65 	70 	51 	410 	68.33
248 	248 	Tyranitar 	100 	134 	110 	95 	100 	61 	600 	100
		Mega Tyranitar
249 	249 	Lugia 	106 	90 	130 	90 	154 	110 	680 	113.33
250 	250 	Ho-Oh 	106 	130 	90 	110 	154 	90 	680 	113.33
251 	251 	Celebi 	100 	100 	100 	100 	100 	100 	600 	100
252 	252 	Treecko 	40 	45 	35 	65 	55 	70 	310 	51.67
253 	253 	Grovyle 	50 	65 	45 	85 	65 	95 	405 	67.5
254 	254 	Sceptile 	70 	85 	65 	105 	85 	120 	530 	88.33
255 	255 	Torchic 	45 	60 	40 	70 	50 	45 	310 	51.67
256 	256 	Combusken 	60 	85 	60 	85 	60 	55 	405 	67.5
257 	257 	Blaziken 	80 	120 	70 	110 	70 	80 	530 	88.33
		Mega Blaziken
258 	258 	Mudkip 	50 	70 	50 	50 	50 	40 	310 	51.67
259 	259 	Marshtomp 	70 	85 	70 	60 	70 	50 	405 	67.5
260 	260 	Swampert 	100 	110 	90 	85 	90 	60 	535 	89.17
261 	261 	Poochyena 	35 	55 	35 	30 	30 	35 	220 	36.67
262 	262 	Mightyena 	70 	90 	70 	60 	60 	70 	420 	70
263 	263 	Zigzagoon 	38 	30 	41 	30 	41 	60 	240 	40
264 	264 	Linoone 	78 	70 	61 	50 	61 	100 	420 	70
265 	265 	Wurmple 	45 	45 	35 	20 	30 	20 	195 	32.5
266 	266 	Silcoon 	50 	35 	55 	25 	25 	15 	205 	34.17
267 	267 	Beautifly 	60 	70 	50 	100 	50 	65 	395 	65.83
268 	268 	Cascoon 	50 	35 	55 	25 	25 	15 	205 	34.17
269 	269 	Dustox 	60 	50 	70 	50 	90 	65 	385 	64.17
270 	270 	Lotad 	40 	30 	30 	40 	50 	30 	220 	36.67
271 	271 	Lombre 	60 	50 	50 	60 	70 	50 	340 	56.67
272 	272 	Ludicolo 	80 	70 	70 	90 	100 	70 	480 	80
273 	273 	Seedot 	40 	40 	50 	30 	30 	30 	220 	36.67
274 	274 	Nuzleaf 	70 	70 	40 	60 	40 	60 	340 	56.67
275 	275 	Shiftry 	90 	100 	60 	90 	60 	80 	480 	80
276 	276 	Taillow 	40 	55 	30 	30 	30 	85 	270 	45
277 	277 	Swellow 	60 	85 	60 	50 	50 	125 	430 	71.67
278 	278 	Wingull 	40 	30 	30 	55 	30 	85 	270 	45
279 	279 	Pelipper 	60 	50 	100 	85 	70 	65 	430 	71.67
280 	280 	Ralts 	28 	25 	25 	45 	35 	40 	198 	33
281 	281 	Kirlia 	38 	35 	35 	65 	55 	50 	278 	46.33
282 	282 	Gardevoir 	68 	65 	65 	125 	115 	80 	518 	86.33
		Mega Gardevoir
283 	283 	Surskit 	40 	30 	32 	50 	52 	65 	269 	44.83
284 	284 	Masquerain 	70 	60 	62 	80 	82 	60 	414 	69
285 	285 	Shroomish 	60 	40 	60 	40 	60 	35 	295 	49.17
286 	286 	Breloom 	60 	130 	80 	60 	60 	70 	460 	76.67
287 	287 	Slakoth 	60 	60 	60 	35 	35 	30 	280 	46.67
288 	288 	Vigoroth 	80 	80 	80 	55 	55 	90 	440 	73.33
289 	289 	Slaking 	150 	160 	100 	95 	65 	100 	670 	111.67
290 	290 	Nincada 	31 	45 	90 	30 	30 	40 	266 	44.33
291 	291 	Ninjask 	61 	90 	45 	50 	50 	160 	456 	76
292 	292 	Shedinja 	1 	90 	45 	30 	30 	40 	236 	39.33
293 	293 	Whismur 	64 	51 	23 	51 	23 	28 	240 	40
294 	294 	Loudred 	84 	71 	43 	71 	43 	48 	360 	60
295 	295 	Exploud 	104 	91 	63 	91 	73 	68 	490 	81.67
296 	296 	Makuhita 	72 	60 	30 	20 	30 	25 	237 	39.5
297 	297 	Hariyama 	144 	120 	60 	40 	60 	50 	474 	79
298 	298 	Azurill 	50 	20 	40 	20 	40 	20 	190 	31.67
299 	299 	Nosepass 	30 	45 	135 	45 	90 	30 	375 	62.5
300 	300 	Skitty 	50 	45 	45 	35 	35 	50 	260 	43.33
301 	301 	Delcatty 	70 	65 	65 	55 	55 	70 	380 	63.33
302 	302 	Sableye 	50 	75 	75 	65 	65 	50 	380 	63.33
303 	303 	Mawile 	50 	85 	85 	55 	55 	50 	380 	63.33
		Mega Mawile
304 	304 	Aron 	50 	70 	100 	40 	40 	30 	330 	55
305 	305 	Lairon 	60 	90 	140 	50 	50 	40 	430 	71.67
306 	306 	Aggron 	70 	110 	180 	60 	60 	50 	530 	88.33
		Mega Aggron
307 	307 	Meditite 	30 	40 	55 	40 	55 	60 	280 	46.67
308 	308 	Medicham 	60 	60 	75 	60 	75 	80 	410 	68.33
		Mega Medicham
309 	309 	Electrike 	40 	45 	40 	65 	40 	65 	295 	49.17
310 	310 	Manectric 	70 	75 	60 	105 	60 	105 	475 	79.17
		Mega Manectric
311 	311 	Plusle 	60 	50 	40 	85 	75 	95 	405 	67.5
312 	312 	Minun 	60 	40 	50 	75 	85 	95 	405 	67.5
313 	313 	Volbeat 	65 	73 	55 	47 	75 	85 	400 	66.67
314 	314 	Illumise 	65 	47 	55 	73 	75 	85 	400 	66.67
315 	315 	Roselia 	50 	60 	45 	100 	80 	65 	400 	66.67
316 	316 	Gulpin 	70 	43 	53 	43 	53 	40 	302 	50.33
317 	317 	Swalot 	100 	73 	83 	73 	83 	55 	467 	77.83
318 	318 	Carvanha 	45 	90 	20 	65 	20 	65 	305 	50.83
319 	319 	Sharpedo 	70 	120 	40 	95 	40 	95 	460 	76.67
320 	320 	Wailmer 	130 	70 	35 	70 	35 	60 	400 	66.67
321 	321 	Wailord 	170 	90 	45 	90 	45 	60 	500 	83.33
322 	322 	Numel 	60 	60 	40 	65 	45 	35 	305 	50.83
323 	323 	Camerupt 	70 	100 	70 	105 	75 	40 	460 	76.67
324 	324 	Torkoal 	70 	85 	140 	85 	70 	20 	470 	78.33
325 	325 	Spoink 	60 	25 	35 	70 	80 	60 	330 	55
326 	326 	Grumpig 	80 	45 	65 	90 	110 	80 	470 	78.33
327 	327 	Spinda 	60 	60 	60 	60 	60 	60 	360 	60
328 	328 	Trapinch 	45 	100 	45 	45 	45 	10 	290 	48.33
329 	329 	Vibrava 	50 	70 	50 	50 	50 	70 	340 	56.67
330 	330 	Flygon 	80 	100 	80 	80 	80 	100 	520 	86.67
331 	331 	Cacnea 	50 	85 	40 	85 	40 	35 	335 	55.83
332 	332 	Cacturne 	70 	115 	60 	115 	60 	55 	475 	79.17
333 	333 	Swablu 	45 	40 	60 	40 	75 	50 	310 	51.67
334 	334 	Altaria 	75 	70 	90 	70 	105 	80 	490 	81.67
335 	335 	Zangoose 	73 	115 	60 	60 	60 	90 	458 	76.33
336 	336 	Seviper 	73 	100 	60 	100 	60 	65 	458 	76.33
337 	337 	Lunatone 	70 	55 	65 	95 	85 	70 	440 	73.33
338 	338 	Solrock 	70 	95 	85 	55 	65 	70 	440 	73.33
339 	339 	Barboach 	50 	48 	43 	46 	41 	60 	288 	48
340 	340 	Whiscash 	110 	78 	73 	76 	71 	60 	468 	78
341 	341 	Corphish 	43 	80 	65 	50 	35 	35 	308 	51.33
342 	342 	Crawdaunt 	63 	120 	85 	90 	55 	55 	468 	78
343 	343 	Baltoy 	40 	40 	55 	40 	70 	55 	300 	50
344 	344 	Claydol 	60 	70 	105 	70 	120 	75 	500 	83.33
345 	345 	Lileep 	66 	41 	77 	61 	87 	23 	355 	59.17
346 	346 	Cradily 	86 	81 	97 	81 	107 	43 	495 	82.5
347 	347 	Anorith 	45 	95 	50 	40 	50 	75 	355 	59.17
348 	348 	Armaldo 	75 	125 	100 	70 	80 	45 	495 	82.5
349 	349 	Feebas 	20 	15 	20 	10 	55 	80 	200 	33.33
350 	350 	Milotic 	95 	60 	79 	100 	125 	81 	540 	90
351 	351 	Castform 	70 	70 	70 	70 	70 	70 	420 	70
352 	352 	Kecleon 	60 	90 	70 	60 	120 	40 	440 	73.33
353 	353 	Shuppet 	44 	75 	35 	63 	33 	45 	295 	49.17
354 	354 	Banette 	64 	115 	65 	83 	63 	65 	455 	75.83
		Mega Banette
355 	355 	Duskull 	20 	40 	90 	30 	90 	25 	295 	49.17
356 	356 	Dusclops 	40 	70 	130 	60 	130 	25 	455 	75.83
357 	357 	Tropius 	99 	68 	83 	72 	87 	51 	460 	76.67
358 	358 	Chimecho 	65 	50 	70 	95 	80 	65 	425 	70.83
359 	359 	Absol 	65 	130 	60 	75 	60 	75 	465 	77.5
		Mega Absol
360 	360 	Wynaut 	95 	23 	48 	23 	48 	23 	260 	43.33
361 	361 	Snorunt 	50 	50 	50 	50 	50 	50 	300 	50
362 	362 	Glalie 	80 	80 	80 	80 	80 	80 	480 	80
363 	363 	Spheal 	70 	40 	50 	55 	50 	25 	290 	48.33
364 	364 	Sealeo 	90 	60 	70 	75 	70 	45 	410 	68.33
365 	365 	Walrein 	110 	80 	90 	95 	90 	65 	530 	88.33
366 	366 	Clamperl 	35 	64 	85 	74 	55 	32 	345 	57.5
367 	367 	Huntail 	55 	104 	105 	94 	75 	52 	485 	80.83
368 	368 	Gorebyss 	55 	84 	105 	114 	75 	52 	485 	80.83
369 	369 	Relicanth 	100 	90 	130 	45 	65 	55 	485 	80.83
370 	370 	Luvdisc 	43 	30 	55 	40 	65 	97 	330 	55
371 	371 	Bagon 	45 	75 	60 	40 	30 	50 	300 	50
372 	372 	Shelgon 	65 	95 	100 	60 	50 	50 	420 	70
373 	373 	Salamence 	95 	135 	80 	110 	80 	100 	600 	100
374 	374 	Beldum 	40 	55 	80 	35 	60 	30 	300 	50
375 	375 	Metang 	60 	75 	100 	55 	80 	50 	420 	70
376 	376 	Metagross 	80 	135 	130 	95 	90 	70 	600 	100
377 	377 	Regirock 	80 	100 	200 	50 	100 	50 	580 	96.67
378 	378 	Regice 	80 	50 	100 	100 	200 	50 	580 	96.67
379 	379 	Registeel 	80 	75 	150 	75 	150 	50 	580 	96.67
380 	380 	Latias 	80 	80 	90 	110 	130 	110 	600 	100
381 	381 	Latios 	80 	90 	80 	130 	110 	110 	600 	100
382 	382 	Kyogre 	100 	100 	90 	150 	140 	90 	670 	111.67
383 	383 	Groudon 	100 	150 	140 	100 	90 	90 	670 	111.67
384 	384 	Rayquaza 	105 	150 	90 	150 	90 	95 	680 	113.33
385 	385 	Jirachi 	100 	100 	100 	100 	100 	100 	600 	100
386 	386 	Deoxys (Normal Forme) 	50 	150 	50 	150 	50 	150 	600 	100
386 	386A 	Deoxys (Attack Forme) 	50 	180 	20 	180 	20 	150 	600 	100
386 	386D 	Deoxys (Defense Forme) 	50 	70 	160 	70 	160 	90 	600 	100
386 	386S 	Deoxys (Speed Forme) 	50 	95 	90 	95 	90 	180 	600 	100
387 	387 	Turtwig 	55 	68 	64 	45 	55 	31 	318 	53
388 	388 	Grotle 	75 	89 	85 	55 	65 	36 	405 	67.5
389 	389 	Torterra 	95 	109 	105 	75 	85 	56 	525 	87.5
390 	390 	Chimchar 	44 	58 	44 	58 	44 	61 	309 	51.5
391 	391 	Monferno 	64 	78 	52 	78 	52 	81 	405 	67.5
392 	392 	Infernape 	76 	104 	71 	104 	71 	108 	534 	89
393 	393 	Piplup 	53 	51 	53 	61 	56 	40 	314 	52.33
394 	394 	Prinplup 	64 	66 	68 	81 	76 	50 	405 	67.5
395 	395 	Empoleon 	84 	86 	88 	111 	101 	60 	530 	88.33
396 	396 	Starly 	40 	55 	30 	30 	30 	60 	245 	40.83
397 	397 	Staravia 	55 	75 	50 	40 	40 	80 	340 	56.67
398 	398 	Staraptor 	85 	120 	70 	50 	60 	100 	485 	80.83
399 	399 	Bidoof 	59 	45 	40 	35 	40 	31 	250 	41.67
400 	400 	Bibarel 	79 	85 	60 	55 	60 	71 	410 	68.33
401 	401 	Kricketot 	37 	25 	41 	25 	41 	25 	194 	32.33
402 	402 	Kricketune 	77 	85 	51 	55 	51 	65 	384 	64
403 	403 	Shinx 	45 	65 	34 	40 	34 	45 	263 	43.83
404 	404 	Luxio 	60 	85 	49 	60 	49 	60 	363 	60.5
405 	405 	Luxray 	80 	120 	79 	95 	79 	70 	523 	87.17
406 	406 	Budew 	40 	30 	35 	50 	70 	55 	280 	46.67
407 	407 	Roserade 	60 	70 	65 	125 	105 	90 	515 	85.83
408 	408 	Cranidos 	67 	125 	40 	30 	30 	58 	350 	58.33
409 	409 	Rampardos 	97 	165 	60 	65 	50 	58 	495 	82.5
410 	410 	Shieldon 	30 	42 	118 	42 	88 	30 	350 	58.33
411 	411 	Bastiodon 	60 	52 	168 	47 	138 	30 	495 	82.5
412 	412 	Burmy 	40 	29 	45 	29 	45 	36 	224 	37.33
413 	413 	Wormadam (Plant Cloak) 	60 	59 	85 	79 	105 	36 	424 	70.67
413 	413G 	Wormadam (Sandy Cloak) 	60 	79 	105 	59 	85 	36 	424 	70.67
413 	413S 	Wormadam (Trash Cloak) 	60 	69 	95 	69 	95 	36 	424 	70.67
414 	414 	Mothim 	70 	94 	50 	94 	50 	66 	424 	70.67
415 	415 	Combee 	30 	30 	42 	30 	42 	70 	244 	40.67
416 	416 	Vespiquen 	70 	80 	102 	80 	102 	40 	474 	79
417 	417 	Pachirisu 	60 	45 	70 	45 	90 	95 	405 	67.5
418 	418 	Buizel 	55 	65 	35 	60 	30 	85 	330 	55
419 	419 	Floatzel 	85 	105 	55 	85 	50 	115 	495 	82.5
420 	420 	Cherubi 	45 	35 	45 	62 	53 	35 	275 	45.83
421 	421 	Cherrim 	70 	60 	70 	87 	78 	85 	450 	75
422 	422 	Shellos 	76 	48 	48 	57 	62 	34 	325 	54.17
423 	423 	Gastrodon 	111 	83 	68 	92 	82 	39 	475 	79.17
424 	424 	Ambipom 	75 	100 	66 	60 	66 	115 	482 	80.33
425 	425 	Drifloon 	90 	50 	34 	60 	44 	70 	348 	58
426 	426 	Drifblim 	150 	80 	44 	90 	54 	80 	498 	83
427 	427 	Buneary 	55 	66 	44 	44 	56 	85 	350 	58.33
428 	428 	Lopunny 	65 	76 	84 	54 	96 	105 	480 	80
429 	429 	Mismagius 	60 	60 	60 	105 	105 	105 	495 	82.5
430 	430 	Honchkrow 	100 	125 	52 	105 	52 	71 	505 	84.17
431 	431 	Glameow 	49 	55 	42 	42 	37 	85 	310 	51.67
432 	432 	Purugly 	71 	82 	64 	64 	59 	112 	452 	75.33
433 	433 	Chingling 	45 	30 	50 	65 	50 	45 	285 	47.5
434 	434 	Stunky 	63 	63 	47 	41 	41 	74 	329 	54.83
435 	435 	Skuntank 	103 	93 	67 	71 	61 	84 	479 	79.83
436 	436 	Bronzor 	57 	24 	86 	24 	86 	23 	300 	50
437 	437 	Bronzong 	67 	89 	116 	79 	116 	33 	500 	83.33
438 	438 	Bonsly 	50 	80 	95 	10 	45 	10 	290 	48.33
439 	439 	Mime Jr. 	20 	25 	45 	70 	90 	60 	310 	51.67
440 	440 	Happiny 	100 	5 	5 	15 	65 	30 	220 	36.67
441 	441 	Chatot 	76 	65 	45 	92 	42 	91 	411 	68.5
442 	442 	Spiritomb 	50 	92 	108 	92 	108 	35 	485 	80.83
443 	443 	Gible 	58 	70 	45 	40 	45 	42 	300 	50
444 	444 	Gabite 	68 	90 	65 	50 	55 	82 	410 	68.33
445 	445 	Garchomp 	108 	130 	95 	80 	85 	102 	600 	100
		Mega Garchomp
446 	446 	Munchlax 	135 	85 	40 	40 	85 	5 	390 	65
447 	447 	Riolu 	40 	70 	40 	35 	40 	60 	285 	47.5
448 	448 	Lucario 	70 	110 	70 	115 	70 	90 	525 	87.5
		Mega Lucario
449 	449 	Hippopotas 	68 	72 	78 	38 	42 	32 	330 	55
450 	450 	Hippowdon 	108 	112 	118 	68 	72 	47 	525 	87.5
451 	451 	Skorupi 	40 	50 	90 	30 	55 	65 	330 	55
452 	452 	Drapion 	70 	90 	110 	60 	75 	95 	500 	83.33
453 	453 	Croagunk 	48 	61 	40 	61 	40 	50 	300 	50
454 	454 	Toxicroak 	83 	106 	65 	86 	65 	85 	490 	81.67
455 	455 	Carnivine 	74 	100 	72 	90 	72 	46 	454 	75.67
456 	456 	Finneon 	49 	49 	56 	49 	61 	66 	330 	55
457 	457 	Lumineon 	69 	69 	76 	69 	86 	91 	460 	76.67
458 	458 	Mantyke 	45 	20 	50 	60 	120 	50 	345 	57.5
459 	459 	Snover 	60 	62 	50 	62 	60 	40 	334 	55.67
460 	460 	Abomasnow 	90 	92 	75 	92 	85 	60 	494 	82.33
		Mega Abomasnow
461 	461 	Weavile 	70 	120 	65 	45 	85 	125 	510 	85
462 	462 	Magnezone 	70 	70 	115 	130 	90 	60 	535 	89.17
463 	463 	Lickilicky 	110 	85 	95 	80 	95 	50 	515 	85.83
464 	464 	Rhyperior 	115 	140 	130 	55 	55 	40 	535 	89.17
465 	465 	Tangrowth 	100 	100 	125 	110 	50 	50 	535 	89.17
466 	466 	Electivire 	75 	123 	67 	95 	85 	95 	540 	90
467 	467 	Magmortar 	75 	95 	67 	125 	95 	83 	540 	90
468 	468 	Togekiss 	85 	50 	95 	120 	115 	80 	545 	90.83
469 	469 	Yanmega 	86 	76 	86 	116 	56 	95 	515 	85.83
470 	470 	Leafeon 	65 	110 	130 	60 	65 	95 	525 	87.5
471 	471 	Glaceon 	65 	60 	110 	130 	95 	65 	525 	87.5
472 	472 	Gliscor 	75 	95 	125 	45 	75 	95 	510 	85
473 	473 	Mamoswine 	110 	130 	80 	70 	60 	80 	530 	88.33
474 	474 	Porygon-Z 	85 	80 	70 	135 	75 	90 	535 	89.17
475 	475 	Gallade 	68 	125 	65 	65 	115 	80 	518 	86.33
476 	476 	Probopass 	60 	55 	145 	75 	150 	40 	525 	87.5
477 	477 	Dusknoir 	45 	100 	135 	65 	135 	45 	525 	87.5
478 	478 	Froslass 	70 	80 	70 	80 	70 	110 	480 	80
479 	479 	Rotom (Normal Rotom) 	50 	50 	77 	95 	77 	91 	440 	73.33
479 	479O 	Rotom (Heat Rotom) 	50 	65 	107 	105 	107 	86 	520 	86.67
479 	479W 	Rotom (Wash Rotom) 	50 	65 	107 	105 	107 	86 	520 	86.67
479 	479R 	Rotom (Frost Rotom) 	50 	65 	107 	105 	107 	86 	520 	86.67
479 	479F 	Rotom (Fan Rotom) 	50 	65 	107 	105 	107 	86 	520 	86.67
479 	479L 	Rotom (Mow Rotom) 	50 	65 	107 	105 	107 	86 	520 	86.67
480 	480 	Uxie 	75 	75 	130 	75 	130 	95 	580 	96.67
481 	481 	Mesprit 	80 	105 	105 	105 	105 	80 	580 	96.67
482 	482 	Azelf 	75 	125 	70 	125 	70 	115 	580 	96.67
483 	483 	Dialga 	100 	120 	120 	150 	100 	90 	680 	113.33
484 	484 	Palkia 	90 	120 	100 	150 	120 	100 	680 	113.33
485 	485 	Heatran 	91 	90 	106 	130 	106 	77 	600 	100
486 	486 	Regigigas 	110 	160 	110 	80 	110 	100 	670 	111.67
487 	487 	Giratina (Altered Forme) 	150 	100 	120 	100 	120 	90 	680 	113.33
487 	487O 	Giratina (Origin Forme) 	150 	120 	100 	120 	100 	90 	680 	113.33
488 	488 	Cresselia 	120 	70 	120 	75 	130 	85 	600 	100
489 	489 	Phione 	80 	80 	80 	80 	80 	80 	480 	80
490 	490 	Manaphy 	100 	100 	100 	100 	100 	100 	600 	100
491 	491 	Darkrai 	70 	90 	90 	135 	90 	125 	600 	100
492 	492 	Shaymin (Land Forme) 	100 	100 	100 	100 	100 	100 	600 	100
492 	492S 	Shaymin (Sky Forme) 	100 	103 	75 	120 	75 	127 	600 	100
493 	493 	Arceus 	120 	120 	120 	120 	120 	120 	720 	120
494 	494 	Victini 	100 	100 	100 	100 	100 	100 	600 	100
495 	495 	Snivy 	45 	45 	55 	45 	55 	63 	308 	51.33
496 	496 	Servine 	60 	60 	75 	60 	75 	83 	413 	68.83
497 	497 	Serperior 	75 	75 	95 	75 	95 	113 	528 	88
498 	498 	Tepig 	65 	63 	45 	45 	45 	45 	308 	51.33
499 	499 	Pignite 	90 	93 	55 	70 	55 	55 	418 	69.67
500 	500 	Emboar 	110 	123 	65 	100 	65 	65 	528 	88
501 	501 	Oshawott 	55 	55 	45 	63 	45 	45 	308 	51.33
502 	502 	Dewott 	75 	75 	60 	83 	60 	60 	413 	68.83
503 	503 	Samurott 	95 	100 	85 	108 	70 	70 	528 	88
504 	504 	Patrat 	45 	55 	39 	35 	39 	42 	255 	42.5
505 	505 	Watchog 	60 	85 	69 	60 	69 	77 	420 	70
506 	506 	Lillipup 	45 	60 	45 	25 	45 	55 	275 	45.83
507 	507 	Herdier 	65 	80 	65 	35 	65 	60 	370 	61.67
508 	508 	Stoutland 	85 	110 	90 	45 	90 	80 	500 	83.33
509 	509 	Purrloin 	41 	50 	37 	50 	37 	66 	281 	46.83
510 	510 	Liepard 	64 	88 	50 	88 	50 	106 	446 	74.33
511 	511 	Pansage 	50 	53 	48 	53 	48 	64 	316 	52.67
512 	512 	Simisage 	75 	98 	63 	98 	63 	101 	498 	83
513 	513 	Pansear 	50 	53 	48 	53 	48 	64 	316 	52.67
514 	514 	Simisear 	75 	98 	63 	98 	63 	101 	498 	83
515 	515 	Panpour 	50 	53 	48 	53 	48 	64 	316 	52.67
516 	516 	Simipour 	75 	98 	63 	98 	63 	101 	498 	83
517 	517 	Munna 	76 	25 	45 	67 	55 	24 	292 	48.67
518 	518 	Musharna 	116 	55 	85 	107 	95 	29 	487 	81.17
519 	519 	Pidove 	50 	55 	50 	36 	30 	43 	264 	44
520 	520 	Tranquill 	62 	77 	62 	50 	42 	65 	358 	59.67
521 	521 	Unfezant 	80 	115 	80 	65 	55 	93 	488 	81.33
522 	522 	Blitzle 	45 	60 	32 	50 	32 	76 	295 	49.17
523 	523 	Zebstrika 	75 	100 	63 	80 	63 	116 	497 	82.83
524 	524 	Roggenrola 	55 	75 	85 	25 	25 	15 	280 	46.67
525 	525 	Boldore 	70 	105 	105 	50 	40 	20 	390 	65
526 	526 	Gigalith 	85 	135 	130 	60 	80 	25 	515 	85.83
527 	527 	Woobat 	55 	45 	43 	55 	43 	72 	313 	52.17
528 	528 	Swoobat 	67 	57 	55 	77 	55 	114 	425 	70.83
529 	529 	Drilbur 	60 	85 	40 	30 	45 	68 	328 	54.67
530 	530 	Excadrill 	110 	135 	60 	50 	65 	88 	508 	84.67
531 	531 	Audino 	103 	60 	86 	60 	86 	50 	445 	74.17
532 	532 	Timburr 	75 	80 	55 	25 	35 	35 	305 	50.83
533 	533 	Gurdurr 	85 	105 	85 	40 	50 	40 	405 	67.5
534 	534 	Conkeldurr 	105 	140 	95 	55 	65 	45 	505 	84.17
535 	535 	Tympole 	50 	50 	40 	50 	40 	64 	294 	49
536 	536 	Palpitoad 	75 	65 	55 	65 	55 	69 	384 	64
537 	537 	Seismitoad 	105 	95 	75 	85 	75 	74 	509 	84.83
538 	538 	Throh 	120 	100 	85 	30 	85 	45 	465 	77.5
539 	539 	Sawk 	75 	125 	75 	30 	75 	85 	465 	77.5
540 	540 	Sewaddle 	45 	53 	70 	40 	60 	42 	310 	51.67
541 	541 	Swadloon 	55 	63 	90 	50 	80 	42 	380 	63.33
542 	542 	Leavanny 	75 	103 	80 	70 	80 	92 	500 	83.33
543 	543 	Venipede 	30 	45 	59 	30 	39 	57 	260 	43.33
544 	544 	Whirlipede 	40 	55 	99 	40 	79 	47 	360 	60
545 	545 	Scolipede 	60 	100 	89 	55 	69 	112 	485 	80.83
546 	546 	Cottonee 	40 	27 	60 	37 	50 	66 	280 	46.67
547 	547 	Whimsicott 	60 	67 	85 	77 	75 	116 	480 	80
548 	548 	Petilil 	45 	35 	50 	70 	50 	30 	280 	46.67
549 	549 	Lilligant 	70 	60 	75 	110 	75 	90 	480 	80
550 	550 	Basculin 	70 	92 	65 	80 	55 	98 	460 	76.67
551 	551 	Sandile 	50 	72 	35 	35 	35 	65 	292 	48.67
552 	552 	Krokorok 	60 	82 	45 	45 	45 	74 	351 	58.5
553 	553 	Krookodile 	95 	117 	80 	65 	70 	92 	519 	86.5
554 	554 	Darumaka 	70 	90 	45 	15 	45 	50 	315 	52.5
555 	555 	Darmanitan (Standard Mode) 	105 	140 	55 	30 	55 	95 	480 	80
555 	555Z 	Darmanitan (Zen Mode) 	105 	30 	105 	140 	105 	55 	540 	90
556 	556 	Maractus 	75 	86 	67 	106 	67 	60 	461 	76.83
557 	557 	Dwebble 	50 	65 	85 	35 	35 	55 	325 	54.17
558 	558 	Crustle 	70 	95 	125 	65 	75 	45 	475 	79.17
559 	559 	Scraggy 	50 	75 	70 	35 	70 	48 	348 	58
560 	560 	Scrafty 	65 	90 	115 	45 	115 	58 	488 	81.33
561 	561 	Sigilyph 	72 	58 	80 	103 	80 	97 	490 	81.67
562 	562 	Yamask 	38 	30 	85 	55 	65 	30 	303 	50.5
563 	563 	Cofagrigus 	58 	50 	145 	95 	105 	30 	483 	80.5
564 	564 	Tirtouga 	54 	78 	103 	53 	45 	22 	355 	59.17
565 	565 	Carracosta 	74 	108 	133 	83 	65 	32 	495 	82.5
566 	566 	Archen 	55 	112 	45 	74 	45 	70 	401 	66.83
567 	567 	Archeops 	75 	140 	65 	112 	65 	110 	567 	94.5
568 	568 	Trubbish 	50 	50 	62 	40 	62 	65 	329 	54.83
569 	569 	Garbodor 	80 	95 	82 	60 	82 	75 	474 	79
570 	570 	Zorua 	40 	65 	40 	80 	40 	65 	330 	55
571 	571 	Zoroark 	60 	105 	60 	120 	60 	105 	510 	85
572 	572 	Minccino 	55 	50 	40 	40 	40 	75 	300 	50
573 	573 	Cinccino 	75 	95 	60 	65 	60 	115 	470 	78.33
574 	574 	Gothita 	45 	30 	50 	55 	65 	45 	290 	48.33
575 	575 	Gothorita 	60 	45 	70 	75 	85 	55 	390 	65
576 	576 	Gothitelle 	70 	55 	95 	95 	110 	65 	490 	81.67
577 	577 	Solosis 	45 	30 	40 	105 	50 	20 	290 	48.33
578 	578 	Duosion 	65 	40 	50 	125 	60 	30 	370 	61.67
579 	579 	Reuniclus 	110 	65 	75 	125 	85 	30 	490 	81.67
580 	580 	Ducklett 	62 	44 	50 	44 	50 	55 	305 	50.83
581 	581 	Swanna 	75 	87 	63 	87 	63 	98 	473 	78.83
582 	582 	Vanillite 	36 	50 	50 	65 	60 	44 	305 	50.83
583 	583 	Vanillish 	51 	65 	65 	80 	75 	59 	395 	65.83
584 	584 	Vanilluxe 	71 	95 	85 	110 	95 	79 	535 	89.17
585 	585 	Deerling 	60 	60 	50 	40 	50 	75 	335 	55.83
586 	586 	Sawsbuck 	80 	100 	70 	60 	70 	95 	475 	79.17
587 	587 	Emolga 	55 	75 	60 	75 	60 	103 	428 	71.33
588 	588 	Karrablast 	50 	75 	45 	40 	45 	60 	315 	52.5
589 	589 	Escavalier 	70 	135 	105 	60 	105 	20 	495 	82.5
590 	590 	Foongus 	69 	55 	45 	55 	55 	15 	294 	49
591 	591 	Amoonguss 	114 	85 	70 	85 	80 	30 	464 	77.33
592 	592 	Frillish 	55 	40 	50 	65 	85 	40 	335 	55.83
593 	593 	Jellicent 	100 	60 	70 	85 	105 	60 	480 	80
594 	594 	Alomomola 	165 	75 	80 	40 	45 	65 	470 	78.33
595 	595 	Joltik 	50 	47 	50 	57 	50 	65 	319 	53.17
596 	596 	Galvantula 	70 	77 	60 	97 	60 	108 	472 	78.67
597 	597 	Ferroseed 	44 	50 	91 	24 	86 	10 	305 	50.83
598 	598 	Ferrothorn 	74 	94 	131 	54 	116 	20 	489 	81.5
599 	599 	Klink 	40 	55 	70 	45 	60 	30 	300 	50
600 	600 	Klang 	60 	80 	95 	70 	85 	50 	440 	73.33
601 	601 	Klinklang 	60 	100 	115 	70 	85 	90 	520 	86.67
602 	602 	Tynamo 	35 	55 	40 	45 	40 	60 	275 	45.83
603 	603 	Eelektrik 	65 	85 	70 	75 	70 	40 	405 	67.5
604 	604 	Eelektross 	85 	115 	80 	105 	80 	50 	515 	85.83
605 	605 	Elgyem 	55 	55 	55 	85 	55 	30 	335 	55.83
606 	606 	Beheeyem 	75 	75 	75 	125 	95 	40 	485 	80.83
607 	607 	Litwick 	50 	30 	55 	65 	55 	20 	275 	45.83
608 	608 	Lampent 	60 	40 	60 	95 	60 	55 	370 	61.67
609 	609 	Chandelure 	60 	55 	90 	145 	90 	80 	520 	86.67
610 	610 	Axew 	46 	87 	60 	30 	40 	57 	320 	53.33
611 	611 	Fraxure 	66 	117 	70 	40 	50 	67 	410 	68.33
612 	612 	Haxorus 	76 	147 	90 	60 	70 	97 	540 	90
613 	613 	Cubchoo 	55 	70 	40 	60 	40 	40 	305 	50.83
614 	614 	Beartic 	95 	110 	80 	70 	80 	50 	485 	80.83
615 	615 	Cryogonal 	70 	50 	30 	95 	135 	105 	485 	80.83
616 	616 	Shelmet 	50 	40 	85 	40 	65 	25 	305 	50.83
617 	617 	Accelgor 	80 	70 	40 	100 	60 	145 	495 	82.5
618 	618 	Stunfisk 	109 	66 	84 	81 	99 	32 	471 	78.5
619 	619 	Mienfoo 	45 	85 	50 	55 	50 	65 	350 	58.33
620 	620 	Mienshao 	65 	125 	60 	95 	60 	105 	510 	85
621 	621 	Druddigon 	77 	120 	90 	60 	90 	48 	485 	80.83
622 	622 	Golett 	59 	74 	50 	35 	50 	35 	303 	50.5
623 	623 	Golurk 	89 	124 	80 	55 	80 	55 	483 	80.5
624 	624 	Pawniard 	45 	85 	70 	40 	40 	60 	340 	56.67
625 	625 	Bisharp 	65 	125 	100 	60 	70 	70 	490 	81.67
626 	626 	Bouffalant 	95 	110 	95 	40 	95 	55 	490 	81.67
627 	627 	Rufflet 	70 	83 	50 	37 	50 	60 	350 	58.33
628 	628 	Braviary 	100 	123 	75 	57 	75 	80 	510 	85
629 	629 	Vullaby 	70 	55 	75 	45 	65 	60 	370 	61.67
630 	630 	Mandibuzz 	110 	65 	105 	55 	95 	80 	510 	85
631 	631 	Heatmor 	85 	97 	66 	105 	66 	65 	484 	80.67
632 	632 	Durant 	58 	109 	112 	48 	48 	109 	484 	80.67
633 	633 	Deino 	52 	65 	50 	45 	50 	38 	300 	50
634 	634 	Zweilous 	72 	85 	70 	65 	70 	58 	420 	70
635 	635 	Hydreigon 	92 	105 	90 	125 	90 	98 	600 	100
636 	636 	Larvesta 	55 	85 	55 	50 	55 	60 	360 	60
637 	637 	Volcarona 	85 	60 	65 	135 	105 	100 	550 	91.67
638 	638 	Cobalion 	91 	90 	129 	90 	72 	108 	580 	96.67
639 	639 	Terrakion 	91 	129 	90 	72 	90 	108 	580 	96.67
640 	640 	Virizion 	91 	90 	72 	90 	129 	108 	580 	96.67
641 	641 	Tornadus (Incarnate Forme) 	79 	115 	70 	125 	80 	111 	580 	96.67
641 	641T 	Tornadus (Therian Forme) 	79 	100 	80 	110 	90 	121 	580 	96.67
642 	642 	Thundurus (Incarnate Forme) 	79 	115 	70 	125 	80 	111 	580 	96.67
642 	642T 	Thundurus (Therian Forme) 	79 	105 	70 	145 	80 	101 	580 	96.67
643 	643 	Reshiram 	100 	120 	100 	150 	120 	90 	680 	113.33
644 	644 	Zekrom 	100 	150 	120 	120 	100 	90 	680 	113.33
645 	645 	Landorus (Incarnate Forme) 	89 	125 	90 	115 	80 	101 	600 	100
645 	645T 	Landorus (Therian Forme) 	89 	145 	90 	105 	80 	91 	600 	100
646 	646 	Kyurem 	125 	130 	90 	130 	90 	95 	660 	110
646 	646B 	Kyurem (Black Kyurem) 	125 	170 	100 	120 	90 	95 	700 	116.67
646 	646W 	Kyurem (White Kyurem) 	125 	120 	90 	170 	100 	95 	700 	116.67
647 	647 	Keldeo 	91 	72 	90 	129 	90 	108 	580 	96.67
648 	648 	Meloetta (Aria Forme) 	100 	77 	77 	128 	128 	90 	600 	100
648 	648P 	Meloetta (Pirouette Forme) 	100 	128 	90 	77 	77 	128 	600 	100
649 	649 	Genesect 	71 	120 	95 	120 	95 	99 	600 	100
650 	650 	Chespin 	56 	61 	65 	48 	45 	38 	313 	52.17
651 	651 	Quilladin 	61 	78 	95 	56 	58 	57 	405 	67.5
652 	652 	Chesnaught 	88 	107 	122 	74 	75 	64 	530 	88.33
653 	653 	Fennekin 	40 	45 	40 	62 	60 	60 	307 	51.17
654 	654 	Braixen 	59 	59 	58 	90 	70 	73 	409 	68.17
655 	655 	Delphox 	75 	69 	72 	114 	100 	104 	534 	89
656 	656 	Froakie 	41 	56 	40 	62 	44 	71 	314 	52.33
657 	657 	Frogadier 	54 	63 	52 	83 	56 	97 	405 	67.5
658 	658 	Greninja 	72 	95 	67 	103 	71 	122 	530 	88.33
659 	659 	Bunnelby 	38 	36 	38 	32 	36 	57 	237 	39.5
660 	660 	Diggersby 	85 	56 	77 	50 	77 	78 	423 	70.5
661 	661 	Fletchling 	45 	50 	43 	40 	38 	62 	278 	46.33
662 	662 	Fletchinder 	62 	73 	55 	56 	52 	84 	382 	63.67
663 	663 	Talonflame 	78 	81 	71 	74 	69 	126 	499 	83.17
664 	664 	Scatterbug 	38 	35 	40 	27 	25 	35 	200 	33.33
665 	665 	Spewpa 	45 	22 	60 	27 	30 	29 	213 	35.5
666 	666 	Vivillon 	80 	52 	50 	90 	50 	89 	411 	68.5
667 	667 	Litleo 	62 	50 	58 	73 	54 	72 	369 	61.5
668 	668 	Pyroar 	86 	68 	72 	109 	66 	106 	507 	84.5
669 	669 	Flab�b� 	44 	38 	39 	61 	79 	42 	303 	50.5
670 	670 	Floette 	54 	45 	47 	75 	98 	52 	371 	61.83
671 	671 	Florges 	78 	65 	68 	112 	154 	75 	552 	92
672 	672 	Skiddo 	66 	65 	48 	62 	57 	52 	350 	58.33
673 	673 	Gogoat 	123 	100 	62 	97 	81 	68 	531 	88.5
674 	674 	Pancham 	67 	82 	62 	46 	48 	43 	348 	58
675 	675 	Pangoro 	95 	124 	78 	69 	71 	58 	495 	82.5
676 	676 	Furfrou 	75 	80 	60 	65 	90 	102 	472 	78.67
677 	677 	Espurr 	62 	48 	54 	63 	60 	68 	355 	59.17
678 	678 	Meowstic 	74 	48 	76 	83 	81 	104 	466 	77.67
679 	679 	Honedge 	45 	80 	100 	35 	37 	28 	325 	54.17
680 	680 	Doublade 	59 	110 	150 	45 	49 	35 	448 	74.67
681 	681 	Aegislash (Shield Forme) 	60 	50 	150 	50 	150 	60 	520 	86.67
681 	681 	Aegislash (Blade Forme) 	60 	150 	50 	150 	50 	60 	520 	86.67
682 	682 	Spritzee 	78 	52 	60 	63 	65 	23 	341 	56.83
683 	683 	Aromatisse 	101 	72 	72 	99 	89 	29 	462 	77
684 	684 	Swirlix 	62 	48 	66 	59 	57 	49 	341 	56.83
685 	685 	Slurpuff 	82 	80 	86 	85 	75 	72 	480 	80
686 	686 	Inkay 	53 	54 	53 	37 	46 	45 	288 	48
687 	687 	Malamar 	86 	92 	88 	68 	75 	73 	482 	80.33
688 	688 	Binacle 	42 	52 	67 	39 	56 	50 	306 	51
689 	689 	Barbaracle 	72 	105 	115 	54 	86 	68 	500 	83.33
690 	690 	Skrelp 	50 	60 	60 	60 	60 	30 	320 	53.33
691 	691 	Dragalge 	65 	75 	90 	97 	123 	44 	494 	82.33
692 	692 	Clauncher 	50 	53 	62 	58 	63 	44 	330 	55
693 	693 	Clawitzer 	71 	73 	88 	120 	89 	59 	500 	83.33
694 	694 	Helioptile 	44 	38 	33 	61 	43 	70 	289 	48.17
695 	695 	Heliolisk 	62 	55 	52 	109 	94 	109 	481 	80.17
696 	696 	Tyrunt 	58 	89 	77 	45 	45 	48 	362 	60.33
697 	697 	Tyrantrum 	82 	121 	119 	69 	59 	71 	521 	86.83
698 	698 	Amaura 	77 	59 	50 	67 	63 	46 	362 	60.33
699 	699 	Aurorus 	123 	77 	72 	99 	92 	58 	521 	86.83
700 	700 	Sylveon 	95 	65 	65 	110 	130 	60 	525 	87.5
701 	701 	Hawlucha 	78 	92 	75 	74 	63 	118 	500 	83.33
702 	702 	Dedenne 	67 	58 	57 	81 	67 	101 	431 	71.83
703 	703 	Carbink 	50 	50 	150 	50 	150 	50 	500 	83.33
704 	704 	Goomy 	45 	50 	35 	55 	75 	40 	300 	50
705 	705 	Sliggoo 	68 	75 	53 	83 	113 	60 	452 	75.33
706 	706 	Goodra 	90 	100 	70 	110 	150 	80 	600 	100
707 	707 	Klefki 	57 	80 	91 	80 	87 	75 	470 	78.33
708 	708 	Phantump 	43 	70 	48 	50 	60 	38 	309 	51.5
709 	709 	Trevenant 	85 	110 	76 	65 	82 	56 	474 	79
710 	710 	Pumpkaboo (Small Size) 	44 	66 	70 	44 	55 	56 	335 	55.83
710 	710 	Pumpkaboo (Average Size) 	49 	66 	70 	44 	55 	51 	335 	55.83
710 	710 	Pumpkaboo (Large Size) 	54 	66 	70 	44 	55 	46 	335 	55.83
710 	710 	Pumpkaboo (Super Size) 	59 	66 	70 	44 	55 	41 	335 	55.83
711 	711 	Gourgeist (Small Size) 	55 	85 	122 	58 	75 	99 	494 	82.33
711 	711 	Gourgeist (Average Size) 	65 	90 	122 	58 	75 	84 	494 	82.33
711 	711 	Gourgeist (Large Size) 	75 	95 	122 	58 	75 	69 	494 	82.33
711 	711 	Gourgeist (Super Size) 	85 	100 	122 	58 	75 	54 	494 	82.33
712 	712 	Bergmite 	55 	69 	85 	32 	35 	28 	304 	50.67
713 	713 	Avalugg 	95 	117 	184 	44 	46 	28 	514 	85.67
714 	714 	Noibat 	40 	30 	35 	45 	40 	55 	245 	40.83
715 	715 	Noivern 	85 	70 	80 	97 	80 	123 	535 	89.17
716 	716 	Xerneas 	126 	131 	95 	131 	98 	99 	680 	113.33
717 	717 	Yveltal 	126 	131 	95 	131 	98 	99 	680 	113.33
718 	718 	Zygarde 	108 	100 	121 	81 	95 	95 	600 	100"""

main()
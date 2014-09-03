from app.models import Pokemon, PokemonType, EggGroup, EVBonus, Ability
import re
from pprint import pprint

def main(data):
#     generate_pokemons(data)
#     generate_evolutions(data)
    print_xml_evolution_path_names()
    
def generate_pokemons(data):
    for block in data.split("\n\n"):
        rows = block.split("\n")
        row2 = rows[1].split(",")
        name = re.match(".*R\.string\.([a-z0-9_]+)\)", rows[2]).group(1)
        p = Pokemon.objects.get_if_exist(name=name)
        if not p:
            p = Pokemon()
            p.name = name
        p.number = row2[2].strip()
        p.ancestor = None # Ancestor to be set after the first round, when all Pokemons are created
        p.evolution_path = None
        p.type1 = PokemonType.objects.get(name=row2[4].split(".")[1].strip())
        p.type2 = PokemonType.objects.get(name=row2[5].split(".")[1].strip())
        p.life = row2[7].strip()
        p.attack = row2[8].strip()
        p.defense = row2[9].strip()
        p.sp_attack = row2[10].strip()
        p.sp_defense = row2[11].strip()
        p.speed = row2[12].strip()[:-3]
        
        p.size = rows[10].split(" = ")[1].strip()[:-2]
        p.weight = rows[5].split(" = ")[1].strip()[:-2]
        p.catch_rate = rows[4].split(" = ")[1].strip()[:-1]
        p.gender = rows[7].split(" = ")[1].strip()[:-2]
        p.hatch = rows[6].split(" = ")[1].strip()[:-1]
        
        ev_names_map = {
            "life": "life",
            "att": "attack",
            "def": "defense",
            "spatt": "sp_attack",
            "spdef": "sp_defense",
            "speed": "speed"
        }
         
        ev_values = {
            "life": 0,
            "attack": 0,
            "defense": 0,
            "sp_attack": 0,
            "sp_defense": 0,
            "speed": 0
        }
        ev_content = re.match(".*\{\{(.*)\}\}.*", rows[8]).group(1).split(";")
        for ev in ev_content:
            m = re.match("this.append((\d+), R.string.([a-z]+)_short)", ev)
            if m:
                ev_values[ev_names_map[m.group(2)]] = m.group(1)
        p.ev, _created = EVBonus.objects.get_or_create(**ev_values)
        
        p.save()

        egg_group_content = re.match(".*\{(.*)\}.*", rows[9]).group(1).split(",")
        for egg_group_str in egg_group_content:
            if egg_group_str.startswith("EggGroup."):
                egg_group_name = "egg_group_" + egg_group_str[9:].strip().lower()
                p.egg_group.add(EggGroup.objects.get(name=egg_group_name))
        p.save()
        
        abilities_content = re.match(".*\{\{(.*)\}\}.*", rows[0]).group(1).split(";")
        for ability_str in abilities_content:
            m = re.match(".*Ability\.([A-Z_]+)\).*", ability_str)
            if m:
                ability_identifier = m.group(1).lower()
                ability, _created = Ability.objects.get_or_create(identifier=ability_identifier)
                p.abilities.add(ability)
        p.save()

        print p
    

def generate_evolutions(data):
    for block in data.split("\n\n"):
        rows = block.split("\n")
        name = re.match(".*R\.string\.([a-z0-9_]+)\)", rows[2]).group(1)
        p = Pokemon.objects.get(name=name)
        
        name = re.match(".*R\.string\.([a-z0-9_]+)\)", rows[2]).group(1)
        evolutions = []
        for row in rows[3].split("new HashMap<String, EvolutionNode>(){{"):
            if row.startswith("this.put("):
                row = row[9:]
            evolutions.append(row.split("this.put("))
        
        for i, row in enumerate(evolutions):
            for evol in row:
                if name in evol:
                    if evol.startswith("p.evolutions"):
                        p.ancestor = None
                        p.evolution_path = None
                        
                    else:
                        p.evolution_path = re.match(".*\"(.*)\"", evol).group(1)
                        try:
                            int(p.evolution_path)
                        except ValueError:
#                             evolution_paths_mapping[p.evolution_path] = ""
                            p.evolution_path = evolution_paths_mapping[p.evolution_path];
                        ancestor_name = re.match(".*perName\.get\(ctx\.getString\(R\.string\.([a-z0-9_]+)\).*", evolutions[i-1][0]).group(1)
                        p.ancestor = Pokemon.objects.get(name=ancestor_name)
        p.save()
        print p
    
    Pokemon.objects.filter(name="name_mega_gardevoir").update(ancestor=Pokemon.objects.get(name="name_gardevoir"))
    

def print_xml_evolution_path_names():
    uniques = {}
    for k,v in evolution_paths_mapping.items():
        try:
            int(v)
        except ValueError:
            uniques[v] = k
    
    for k,v in uniques.items():
        print '    <string name="{}">{}</string>'.format(k, v)

evolution_paths_mapping = {"2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee": 'evo_sylveon',
 '20, Attaque > Defense': 'evo_20_att_gt_def',
 '20, Attaque < Defense': 'evo_20_att_lt_def',
 '20, Attaque et Defense identiques': 'evo_20_att_eq_def',
 "20, emplacement libre et Poke Ball dans l'inventaire": 'evo_shedinja',
 '30, en retournant la 3DS': 'evo_malamar',
 "32, avec un Pokemon dans l'equipe": 'evo_pangoro',
 '39 pendant la journee': 'evo_39_day',
 '39 pendant la nuit': 'evo_39_night',
 '50, quand il pleut': 'evo_50_rain',
 '7, au hasard': 'evo_cascoon',
 'Absolite': 'evo_mega',
 'Alakazamite': 'evo_mega',
 'Avec une Pierre Eau': 'evo_water_stone',
 'Avec une Pierre Eclat': 'evo_shiny_stone',
 'Avec une Pierre Feu': 'evo_fire_stone',
 'Avec une Pierre Foudre': 'evo_lightning_stone',
 'Avec une Pierre Lune': 'evo_moon_stone',
 'Avec une Pierre Nuit': 'evo_night_stone',
 'Avec une Pierre Plante': 'evo_herb_stone',
 'Avec une Pierresoleil': 'evo_sun_stone',
 'Blizzarite': 'evo_mega',
 'Bonheur': 'evo_happyness',
 'Bonheur + gagne un niveau de jour': 'evo_happyness_day',
 'Bonheur , Jour': 'evo_happyness_day',
 'Bonheur , Nuit': 'evo_happyness_night',
 'Branettite': 'evo_mega',
 'Brasegalite': 'evo_mega',
 'Carchacrokite': 'evo_mega',
 'Charminite': 'evo_mega',
 'Cizayoxite': 'evo_mega',
 'Demolossite': 'evo_mega',
 'Dracaufite X': 'evo_mega',
 'Dracaufite Y': 'evo_mega',
 'Echange': 'evo_exchange',
 'Echange avec Carabing': 'evo_exchange_karrablast',
 'Echange avec Escargaume': 'evo_exchange_escavalier',
 'Echange en tenant Ameliorator': 'evo_exchange_holding_upgrade',
 'Echange en tenant CD Douteux': 'evo_exchange_holding_dubious_disc',
 'Echange en tenant Chantibonbon': 'evo_exchange_holding_whipped_dream',
 'Echange en tenant Magmariseur': 'evo_exchange_holding_magmarizer',
 'Echange en tenant Peau Metal': 'evo_exchange_holding_metal_coat',
 'Echange en tenant Roche Royale': 'evo_exchange_holding_kings_rock',
 'Echange en tenant Sachet Senteur': 'evo_exchange_holding_sachet',
 "Echange en tenant l'objet Ecaille Draco": 'evo_exchange_holding_dragon_scale',
 "Echange en tenant l'objet Protecteur": 'evo_exchange_holding_protector',
 "Echange en tenant l'objet Tissu Fauche": 'evo_exchange_holding_reaper_cloth',
 'Echange en tenant un Electiriseur': 'evo_exchange_holding_electirizer',
 'Echange en tenant une Dent Ocean': 'evo_exchange_holding_deep_sea_tooth',
 'Echange en tenant une Ecaille Ocean': 'evo_exchange_holding_deep_sea_scale',
 'Ectoplasmite': 'evo_mega',
 'Elecsprintite': 'evo_mega',
 "En apprenant l'attaque Copie": 'evo_attack_mimic',
 "En apprenant l'attaque Pouv.Antique": 'evo_attack_ancientpower',
 "En connaissant l'attaque Coup Double + passer un niveau": 'evo_attack_double_hit ',
 "En connaissant l'attaque Pouv.Antique et lui faire monter d'un niveau": 'evo_attack_ancientpower',
 "En connaissant l'attaque Roulade": 'evo_attack_rollout',
 'Femelle + Pierre Aube': 'evo_dawn_stone_female',
 'Male + Pierre Aube': 'evo_dawn_stone_male',
 'Florizarrite': 'evo_mega',
 'Gagne un niveau de nuit en tenant un Croc Rasoir': 'evo_night_holding_razor_fang',
 'Gagne un niveau de nuit en tenant une Griffe Rasoir': 'evo_night_holding_razor_claw',
 "Gain de niveau avec Remoraid dans l'equipe": 'evo_mantine',
 'Gain de niveau dans un lieu indique': 'evo_place',
 'Gain de niveau en tenant une Pierre Ovale': 'evo_oval_stone',
 'Galekingite': 'evo_mega',
 'Gardevoirite': 'evo_mega',
 'Kangourexite': 'evo_mega',
 'Leviatorite': 'evo_mega',
 'Lucarite': 'evo_mega',
 'Mega': 'evo_mega',
 'Mewtwoite X': 'evo_mega',
 'Mewtwoite Y': 'evo_mega',
 'Mysdibulite': 'evo_mega',
 'Niv 30': '30',
 'Pharampite': 'evo_mega',
 'Pierre Eau': 'evo_water_stone',
 "Pres d'une Pierre Glacee + gagne un niveau": 'evo_glaceon',
 "Pres d'une Pierre Mousse + gagne un niveau": 'evo_leafeon',
 'Scarabruite': 'evo_mega',
 'Scarhinoite': 'evo_mega',
 'Si Femelle, Niveau 20': 'evo_20_female',
 'Si Femelle, Niveau 21': 'evo_21_female',
 'Si Male, Niveau 20': 'evo_20_male',
 'Tortankite': 'evo_mega',
 'Tyranocivite': 'evo_mega',
 "de Beaute superieur ou egal a 170 (3eme et 4eme generations) ou Echange en tenant l'objet Bel'Ecaille (5eme et 6eme generations) ou Tenir le Voile Venus (Pokemon Donjon Mystere)": 'evo_exchange_holding_prism_scale',
 'niveau 26': '26',
 'niveau 30': '30',
 'niveau 33': '33',
 'niveau 34': '34',
 'niveau 37': '37',
 'niveau 38': '38'
}

data = """abilities = new ArrayList<Ability>(){{this.add(Ability.GUTS);this.add(Ability.RUN_AWAY);this.add(Ability.HUSTLE);}};
perName.put(ctx.getString(R.string.name_raticate), new Pokemon(ctx.getString(R.string.name_raticate), 20, 24, Type.NORMAL, Type.NONE, abilities, 55, 81, 60, 50, 70, 97));
p = perName.get(ctx.getString(R.string.name_raticate));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_rattata)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_raticate)), null));}});
p.catchRate = 127;
p.weight = 18.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.DOWNLOAD);this.add(Ability.ADAPTABILITY);this.add(Ability.ANALYTIC);}};
perName.put(ctx.getString(R.string.name_porygon_z), new Pokemon(ctx.getString(R.string.name_porygon_z), 474, 507, Type.PSYCHIC, Type.NONE, abilities, 85, 80, 70, 135, 75, 90));
p = perName.get(ctx.getString(R.string.name_porygon_z));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_porygon)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Ameliorator", new EvolutionNode(perName.get(ctx.getString(R.string.name_porygon2)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant CD Douteux", new EvolutionNode(perName.get(ctx.getString(R.string.name_porygon_z)), null));}}));}});
p.catchRate = 30;
p.weight = 34.0f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHED_SKIN);this.add(Ability.MOXIE);this.add(Ability.INTIMIDATE);}};
perName.put(ctx.getString(R.string.name_scraggy), new Pokemon(ctx.getString(R.string.name_scraggy), 559, 600, Type.DARK, Type.FIGHTING, abilities, 50, 75, 70, 35, 70, 48));
p = perName.get(ctx.getString(R.string.name_scraggy));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_scraggy)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "39", new EvolutionNode(perName.get(ctx.getString(R.string.name_scrafty)), null));}});
p.catchRate = 180;
p.weight = 11.8f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON,EggGroup.FIELD};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.HARVEST);}};
perName.put(ctx.getString(R.string.name_exeggutor), new Pokemon(ctx.getString(R.string.name_exeggutor), 103, 109, Type.GRASS, Type.PSYCHIC, abilities, 95, 95, 85, 125, 65, 55));
p = perName.get(ctx.getString(R.string.name_exeggutor));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_exeggcute)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get(ctx.getString(R.string.name_exeggutor)), null));}});
p.catchRate = 45;
p.weight = 120.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.KEEN_EYE);this.add(Ability.SHEER_FORCE);this.add(Ability.DEFIANT);}};
perName.put(ctx.getString(R.string.name_braviary), new Pokemon(ctx.getString(R.string.name_braviary), 628, 669, Type.NORMAL, Type.FLYING, abilities, 100, 123, 75, 57, 75, 80));
p = perName.get(ctx.getString(R.string.name_braviary));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_rufflet)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "54", new EvolutionNode(perName.get(ctx.getString(R.string.name_braviary)), null));}});
p.catchRate = 60;
p.weight = 41f;
p.hatch = 5355;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INSOMNIA);this.add(Ability.FRISK);this.add(Ability.CURSED_BODY);}};
perName.put(ctx.getString(R.string.name_shuppet), new Pokemon(ctx.getString(R.string.name_shuppet), 353, 376, Type.GHOST, Type.NONE, abilities, 44, 75, 35, 63, 33, 45));
p = perName.get(ctx.getString(R.string.name_shuppet));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_shuppet)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_banette)), new HashMap<String, EvolutionNode>(){{this.put("Branettite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_banette)), null));}}));}});
p.catchRate = 225;
p.weight = 2.3f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.EFFECT_SPORE);this.add(Ability.REGENERATOR);}};
perName.put(ctx.getString(R.string.name_amoonguss), new Pokemon(ctx.getString(R.string.name_amoonguss), 591, 632, Type.GRASS, Type.POISON, abilities, 114, 85, 70, 85, 80, 30));
p = perName.get(ctx.getString(R.string.name_amoonguss));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_foongus)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "39", new EvolutionNode(perName.get(ctx.getString(R.string.name_amoonguss)), null));}});
p.catchRate = 75;
p.weight = 10.5f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.SNIPER);this.add(Ability.DAMP);}};
perName.put(ctx.getString(R.string.name_kingdra), new Pokemon(ctx.getString(R.string.name_kingdra), 230, 246, Type.WATER, Type.DRAGON, abilities, 75, 95, 95, 95, 95, 85));
p = perName.get(ctx.getString(R.string.name_kingdra));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_horsea)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_seadra)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Ecaille Draco", new EvolutionNode(perName.get(ctx.getString(R.string.name_kingdra)), null));}}));}});
p.catchRate = 45;
p.weight = 152.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.DRAGON};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MOTOR_DRIVE);this.add(Ability.VITAL_SPIRIT);}};
perName.put(ctx.getString(R.string.name_electivire), new Pokemon(ctx.getString(R.string.name_electivire), 466, 499, Type.ELECTRIC, Type.NONE, abilities, 75, 123, 67, 95, 85, 95));
p = perName.get(ctx.getString(R.string.name_electivire));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_elekid)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_electabuzz)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant un Electiriseur", new EvolutionNode(perName.get(ctx.getString(R.string.name_electivire)), null));}}));}});
p.catchRate = 30;
p.weight = 140.0f;
p.hatch = 6400;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.MAGICIAN);}};
perName.put(ctx.getString(R.string.name_braixen), new Pokemon(ctx.getString(R.string.name_braixen), 654, 700, Type.FIRE, Type.NONE, abilities, 59, 59, 58, 90, 70, 73));
p = perName.get(ctx.getString(R.string.name_braixen));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_fennekin)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_braixen)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_delphox)), null));}}));}});
p.catchRate = 45;
p.weight = 14.5f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CUTE_CHARM);this.add(Ability.TECHNICIAN);this.add(Ability.SKILL_LINK);}};
perName.put(ctx.getString(R.string.name_cinccino), new Pokemon(ctx.getString(R.string.name_cinccino), 573, 614, Type.NORMAL, Type.NONE, abilities, 75, 95, 60, 65, 60, 115));
p = perName.get(ctx.getString(R.string.name_cinccino));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_minccino)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get(ctx.getString(R.string.name_cinccino)), null));}});
p.catchRate = 255;
p.weight = 7.5f;
p.hatch = 4080;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STATIC);this.add(Ability.MOTOR_DRIVE);}};
perName.put(ctx.getString(R.string.name_emolga), new Pokemon(ctx.getString(R.string.name_emolga), 587, 628, Type.ELECTRIC, Type.FLYING, abilities, 55, 75, 60, 75, 60, 103));
p = perName.get(ctx.getString(R.string.name_emolga));
p.evolutions = null;
p.catchRate = 200;
p.weight = 5.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ROCK_HEAD);this.add(Ability.STURDY);}};
perName.put(ctx.getString(R.string.name_golem), new Pokemon(ctx.getString(R.string.name_golem), 76, 81, Type.ROCK, Type.GROUND, abilities, 80, 110, 130, 55, 65, 45));
p = perName.get(ctx.getString(R.string.name_golem));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_geodude)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_graveler)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_golem)), null));}}));}});
p.catchRate = 45;
p.weight = 300.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_cresselia), new Pokemon(ctx.getString(R.string.name_cresselia), 488, 527, Type.PSYCHIC, Type.NONE, abilities, 120, 70, 120, 75, 130, 85));
p = perName.get(ctx.getString(R.string.name_cresselia));
p.evolutions = null;
p.catchRate = 3;
p.weight = 85.6f;
p.hatch = 30720;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(3, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GLUTTONY);this.add(Ability.TORRENT);}};
perName.put(ctx.getString(R.string.name_simipour), new Pokemon(ctx.getString(R.string.name_simipour), 516, 556, Type.WATER, Type.NONE, abilities, 75, 98, 63, 98, 63, 101));
p = perName.get(ctx.getString(R.string.name_simipour));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_panpour)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_simipour)), null));}});
p.catchRate = 75;
p.weight = 29.0f;
p.hatch = 5355;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.KEEN_EYE);this.add(Ability.RAIN_DISH);}};
perName.put(ctx.getString(R.string.name_pelipper), new Pokemon(ctx.getString(R.string.name_pelipper), 279, 297, Type.WATER, Type.FLYING, abilities, 60, 50, 100, 85, 70, 65));
p = perName.get(ctx.getString(R.string.name_pelipper));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_wingull)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_pelipper)), null));}});
p.catchRate = 45;
p.weight = 28.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FLYING};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.SHELL_ARMOR);}};
perName.put(ctx.getString(R.string.name_dewott), new Pokemon(ctx.getString(R.string.name_dewott), 502, 542, Type.WATER, Type.NONE, abilities, 75, 75, 60, 83, 60, 60));
p = perName.get(ctx.getString(R.string.name_dewott));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_oshawott)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "17", new EvolutionNode(perName.get(ctx.getString(R.string.name_dewott)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_samurott)), null));}}));}});
p.catchRate = 45;
p.weight = 24.5f;
p.hatch = 5355;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.SOUNDPROOF);}};
perName.put(ctx.getString(R.string.name_shieldon), new Pokemon(ctx.getString(R.string.name_shieldon), 410, 438, Type.ROCK, Type.STEEL, abilities, 30, 42, 118, 42, 88, 30));
p = perName.get(ctx.getString(R.string.name_shieldon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_shieldon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_bastiodon)), null));}});
p.catchRate = 45;
p.weight = 57.0f;
p.hatch = 7680;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);this.add(Ability.SUPER_LUCK);this.add(Ability.JUSTIFIED);}};
perName.put(ctx.getString(R.string.name_absol), new Pokemon(ctx.getString(R.string.name_absol), 359, 383, Type.DARK, Type.NONE, abilities, 65, 130, 60, 75, 60, 75));
p = perName.get(ctx.getString(R.string.name_absol));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_absol)), new HashMap<String, EvolutionNode>(){{this.put("Absolite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_absol)), null));}});
p.catchRate = 30;
p.weight = 47.0f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.THICK_FAT);this.add(Ability.HUGE_POWER);this.add(Ability.SAP_SIPPER);}};
perName.put(ctx.getString(R.string.name_azurill), new Pokemon(ctx.getString(R.string.name_azurill), 298, 317, Type.NORMAL, Type.NONE, abilities, 50, 20, 40, 20, 40, 20));
p = perName.get(ctx.getString(R.string.name_azurill));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_azurill)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_marill)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_azumarill)), null));}}));}});
p.catchRate = 60;
p.weight = 2.0f;
p.hatch = 2560;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);this.add(Ability.UNNERVE);}};
perName.put(ctx.getString(R.string.name_vespiquen), new Pokemon(ctx.getString(R.string.name_vespiquen), 416, 446, Type.BUG, Type.FLYING, abilities, 70, 80, 102, 80, 102, 40));
p = perName.get(ctx.getString(R.string.name_vespiquen));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_combee)), new HashMap<String, EvolutionNode>(){{this.put("Si Femelle, Niveau 21", new EvolutionNode(perName.get(ctx.getString(R.string.name_vespiquen)), null));}});
p.catchRate = 45;
p.weight = 38.5f;
p.hatch = 3840;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.SOLAR_POWER);}};
perName.put(ctx.getString(R.string.name_charizard), new Pokemon(ctx.getString(R.string.name_charizard), 6, 7, Type.FIRE, Type.FLYING, abilities, 78, 84, 78, 109, 85, 100));
p = perName.get(ctx.getString(R.string.name_charizard));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_charmander)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_charmeleon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_charizard)), new HashMap<String, EvolutionNode>(){{this.put("Dracaufite X", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_charizard_x)), null));this.put("Dracaufite Y", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_charizard_y)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 90.5f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON,EggGroup.MONSTER};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HUSTLE);}};
perName.put(ctx.getString(R.string.name_deino), new Pokemon(ctx.getString(R.string.name_deino), 633, 674, Type.DARK, Type.DRAGON, abilities, 52, 65, 50, 45, 50, 38));
p = perName.get(ctx.getString(R.string.name_deino));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_deino)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "50", new EvolutionNode(perName.get(ctx.getString(R.string.name_zweilous)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "64", new EvolutionNode(perName.get(ctx.getString(R.string.name_hydreigon)), null));}}));}});
p.catchRate = 45;
p.weight = 17.3f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_rotom_fan_rotom), new Pokemon(ctx.getString(R.string.name_rotom_fan_rotom), 479, 516, Type.ELECTRIC, Type.GHOST, abilities, 50, 65, 107, 105, 107, 86));
p = perName.get(ctx.getString(R.string.name_rotom_fan_rotom));
p.evolutions = null;
p.catchRate = 45;
p.weight = 0.3f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MAGMA_ARMOR);this.add(Ability.FLAME_BODY);this.add(Ability.WEAK_ARMOR);}};
perName.put(ctx.getString(R.string.name_magcargo), new Pokemon(ctx.getString(R.string.name_magcargo), 219, 234, Type.FIRE, Type.ROCK, abilities, 50, 50, 120, 80, 80, 30));
p = perName.get(ctx.getString(R.string.name_magcargo));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_slugma)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "38", new EvolutionNode(perName.get(ctx.getString(R.string.name_magcargo)), null));}});
p.catchRate = 75;
p.weight = 55.0f;
p.hatch = 5610;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRANKSTER);this.add(Ability.DEFIANT);}};
perName.put(ctx.getString(R.string.name_tornadus_therian_forme), new Pokemon(ctx.getString(R.string.name_tornadus_therian_forme), 641, 683, Type.FLYING, Type.NONE, abilities, 79, 100, 80, 110, 90, 121));
p = perName.get(ctx.getString(R.string.name_tornadus_therian_forme));
p.evolutions = null;
p.catchRate = 3;
p.weight = 63.0f;
p.hatch = 30855;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SERENE_GRACE);}};
perName.put(ctx.getString(R.string.name_meloetta_aria_forme), new Pokemon(ctx.getString(R.string.name_meloetta_aria_forme), 648, 693, Type.NORMAL, Type.PSYCHIC, abilities, 100, 77, 77, 128, 128, 90));
p = perName.get(ctx.getString(R.string.name_meloetta_aria_forme));
p.evolutions = null;
p.catchRate = 5;
p.weight = 6.5f;
p.hatch = 5355;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RUN_AWAY);this.add(Ability.INTIMIDATE);this.add(Ability.RATTLED);}};
perName.put(ctx.getString(R.string.name_snubbull), new Pokemon(ctx.getString(R.string.name_snubbull), 209, 222, Type.NORMAL, Type.NONE, abilities, 60, 80, 50, 40, 40, 30));
p = perName.get(ctx.getString(R.string.name_snubbull));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_snubbull)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "23", new EvolutionNode(perName.get(ctx.getString(R.string.name_granbull)), null));}});
p.catchRate = 190;
p.weight = 7.8f;
p.hatch = 5120;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.FAIRY};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ROUGH_SKIN);}};
perName.put(ctx.getString(R.string.name_sharpedo), new Pokemon(ctx.getString(R.string.name_sharpedo), 319, 342, Type.WATER, Type.DARK, abilities, 70, 120, 40, 95, 40, 95));
p = perName.get(ctx.getString(R.string.name_sharpedo));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_carvanha)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_sharpedo)), null));}});
p.catchRate = 60;
p.weight = 88.8f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER2};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_rotom_frost_rotom), new Pokemon(ctx.getString(R.string.name_rotom_frost_rotom), 479, 515, Type.ELECTRIC, Type.GHOST, abilities, 50, 65, 107, 105, 107, 86));
p = perName.get(ctx.getString(R.string.name_rotom_frost_rotom));
p.evolutions = null;
p.catchRate = 45;
p.weight = 0.3f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INSOMNIA);}};
perName.put(ctx.getString(R.string.name_mega_mewtwo_y), new Pokemon(ctx.getString(R.string.name_mega_mewtwo_y), 150, 162, Type.PSYCHIC, Type.NONE, abilities, 106, 150, 70, 194, 120, 140));
p = perName.get(ctx.getString(R.string.name_mega_mewtwo_y));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mewtwo)), new HashMap<String, EvolutionNode>(){{this.put("Mewtwoite X", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_mewtwo_x)), null));this.put("Mewtwoite Y", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_mewtwo_y)), null));}});
p.catchRate = -1;
p.weight = 33.0f;
p.hatch = -1;
p.gender = -1f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MUMMY);}};
perName.put(ctx.getString(R.string.name_yamask), new Pokemon(ctx.getString(R.string.name_yamask), 562, 603, Type.GHOST, Type.NONE, abilities, 38, 30, 85, 55, 65, 30));
p = perName.get(ctx.getString(R.string.name_yamask));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_yamask)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "34", new EvolutionNode(perName.get(ctx.getString(R.string.name_cofagrigus)), null));}});
p.catchRate = 190;
p.weight = 1.5f;
p.hatch = 6630;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL,EggGroup.UNKNOWN};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);}};
perName.put(ctx.getString(R.string.name_dusknoir), new Pokemon(ctx.getString(R.string.name_dusknoir), 477, 510, Type.GHOST, Type.NONE, abilities, 45, 100, 135, 65, 135, 45));
p = perName.get(ctx.getString(R.string.name_dusknoir));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_duskull)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_dusclops)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Tissu Fauche", new EvolutionNode(perName.get(ctx.getString(R.string.name_dusknoir)), null));}}));}});
p.catchRate = 45;
p.weight = 106.6f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 2.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CUTE_CHARM);this.add(Ability.MAGIC_GUARD);this.add(Ability.UNAWARE);}};
perName.put(ctx.getString(R.string.name_clefable), new Pokemon(ctx.getString(R.string.name_clefable), 36, 40, Type.NORMAL, Type.NONE, abilities, 95, 70, 73, 85, 90, 60));
p = perName.get(ctx.getString(R.string.name_clefable));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cleffa)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_clefairy)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get(ctx.getString(R.string.name_clefable)), null));}}));}});
p.catchRate = 25;
p.weight = 40.0f;
p.hatch = 2560;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STEADFAST);}};
perName.put(ctx.getString(R.string.name_mega_mewtwo_x), new Pokemon(ctx.getString(R.string.name_mega_mewtwo_x), 150, 161, Type.PSYCHIC, Type.FIGHTING, abilities, 106, 190, 100, 154, 100, 130));
p = perName.get(ctx.getString(R.string.name_mega_mewtwo_x));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mewtwo)), new HashMap<String, EvolutionNode>(){{this.put("Mewtwoite X", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_mewtwo_x)), null));this.put("Mewtwoite Y", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_mewtwo_y)), null));}});
p.catchRate = -1;
p.weight = 127.0f;
p.hatch = -1;
p.gender = -1f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NATURAL_CURE);}};
perName.put(ctx.getString(R.string.name_celebi), new Pokemon(ctx.getString(R.string.name_celebi), 251, 268, Type.PSYCHIC, Type.GRASS, abilities, 100, 100, 100, 100, 100, 100));
p = perName.get(ctx.getString(R.string.name_celebi));
p.evolutions = null;
p.catchRate = 45;
p.weight = 5.0f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HEALER);this.add(Ability.AROMA_VEIL);}};
perName.put(ctx.getString(R.string.name_aromatisse), new Pokemon(ctx.getString(R.string.name_aromatisse), 683, 730, Type.FAIRY, Type.NONE, abilities, 100, 65, 75, 95, 90, 30));
p = perName.get(ctx.getString(R.string.name_aromatisse));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_spritzee)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Sachet Senteur", new EvolutionNode(perName.get(ctx.getString(R.string.name_aromatisse)), null));}});
p.catchRate = -1;
p.weight = 15.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ILLUSION);}};
perName.put(ctx.getString(R.string.name_zorua), new Pokemon(ctx.getString(R.string.name_zorua), 570, 611, Type.DARK, Type.NONE, abilities, 40, 65, 40, 80, 40, 65));
p = perName.get(ctx.getString(R.string.name_zorua));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_zorua)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_zoroark)), null));}});
p.catchRate = 75;
p.weight = 12.5f;
p.hatch = 6630;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);}};
perName.put(ctx.getString(R.string.name_mega_manectric), new Pokemon(ctx.getString(R.string.name_mega_manectric), 310, 333, Type.ELECTRIC, Type.NONE, abilities, 70, 75, 80, 135, 80, 135));
p = perName.get(ctx.getString(R.string.name_mega_manectric));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_electrike)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "26", new EvolutionNode(perName.get(ctx.getString(R.string.name_manectric)), new HashMap<String, EvolutionNode>(){{this.put("Elecsprintite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_manectric)), null));}}));}});
p.catchRate = -1;
p.weight = 44f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWARM);this.add(Ability.SHED_SKIN);this.add(Ability.NO_GUARD);}};
perName.put(ctx.getString(R.string.name_karrablast), new Pokemon(ctx.getString(R.string.name_karrablast), 588, 629, Type.BUG, Type.NONE, abilities, 50, 75, 45, 40, 45, 60));
p = perName.get(ctx.getString(R.string.name_karrablast));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_karrablast)), new HashMap<String, EvolutionNode>(){{this.put("Echange avec Escargaume", new EvolutionNode(perName.get(ctx.getString(R.string.name_escavalier)), null));}});
p.catchRate = 200;
p.weight = 5.9f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHADOW_TAG);this.add(Ability.TELEPATHY);}};
perName.put(ctx.getString(R.string.name_wynaut), new Pokemon(ctx.getString(R.string.name_wynaut), 360, 385, Type.PSYCHIC, Type.NONE, abilities, 95, 23, 48, 23, 48, 23));
p = perName.get(ctx.getString(R.string.name_wynaut));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_wynaut)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "15", new EvolutionNode(perName.get(ctx.getString(R.string.name_wobbuffet)), null));}});
p.catchRate = 125;
p.weight = 14.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.SNIPER);this.add(Ability.DAMP);}};
perName.put(ctx.getString(R.string.name_horsea), new Pokemon(ctx.getString(R.string.name_horsea), 116, 123, Type.WATER, Type.NONE, abilities, 30, 40, 70, 70, 25, 60));
p = perName.get(ctx.getString(R.string.name_horsea));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_horsea)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_seadra)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Ecaille Draco", new EvolutionNode(perName.get(ctx.getString(R.string.name_kingdra)), null));}}));}});
p.catchRate = 225;
p.weight = 8.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.DRAGON};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CUTE_CHARM);this.add(Ability.PIXILATE);}};
perName.put(ctx.getString(R.string.name_sylveon), new Pokemon(ctx.getString(R.string.name_sylveon), 700, 747, Type.FAIRY, Type.NONE, abilities, 95, 65, 65, 110, 130, 60));
p = perName.get(ctx.getString(R.string.name_sylveon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_eevee)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get(ctx.getString(R.string.name_jolteon)), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_leafeon)), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get(ctx.getString(R.string.name_espeon)), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get(ctx.getString(R.string.name_sylveon)), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_vaporeon)), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_glaceon)), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get(ctx.getString(R.string.name_flareon)), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_umbreon)), null));}});
p.catchRate = 45;
p.weight = 23.5f;
p.hatch = 8960;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.POISON_POINT);this.add(Ability.POISON_TOUCH);}};
perName.put(ctx.getString(R.string.name_skrelp), new Pokemon(ctx.getString(R.string.name_skrelp), 690, 737, Type.POISON, Type.WATER, abilities, 50, 60, 60, 60, 60, 30));
p = perName.get(ctx.getString(R.string.name_skrelp));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_skrelp)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "48", new EvolutionNode(perName.get(ctx.getString(R.string.name_dragalge)), null));}});
p.catchRate = -1;
p.weight = 7.3f;
p.hatch = -1;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.DRAGON};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.AERILATE);}};
perName.put(ctx.getString(R.string.name_mega_pinsir), new Pokemon(ctx.getString(R.string.name_mega_pinsir), 127, 135, Type.BUG, Type.FLYING, abilities, 65, 155, 120, 65, 90, 105));
p = perName.get(ctx.getString(R.string.name_mega_pinsir));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pinsir)), new HashMap<String, EvolutionNode>(){{this.put("Scarabruite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_pinsir)), null));}});
p.catchRate = -1;
p.weight = 59f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.WATER_ABSORB);this.add(Ability.DAMP);this.add(Ability.UNAWARE);}};
perName.put(ctx.getString(R.string.name_quagsire), new Pokemon(ctx.getString(R.string.name_quagsire), 195, 208, Type.WATER, Type.GROUND, abilities, 95, 85, 85, 65, 65, 35));
p = perName.get(ctx.getString(R.string.name_quagsire));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_wooper)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_quagsire)), null));}});
p.catchRate = 90;
p.weight = 75.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.THICK_FAT);}};
perName.put(ctx.getString(R.string.name_mega_venusaur), new Pokemon(ctx.getString(R.string.name_mega_venusaur), 3, 4, Type.GRASS, Type.POISON, abilities, 80, 100, 123, 122, 120, 80));
p = perName.get(ctx.getString(R.string.name_mega_venusaur));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bulbasaur)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_ivysaur)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_venusaur)), new HashMap<String, EvolutionNode>(){{this.put("Florizarrite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_venusaur)), null));}}));}}));}});
p.catchRate = -1;
p.weight = 155.5f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.COMPOUNDEYE);this.add(Ability.TINTED_LENS);}};
perName.put(ctx.getString(R.string.name_butterfree), new Pokemon(ctx.getString(R.string.name_butterfree), 12, 16, Type.BUG, Type.FLYING, abilities, 60, 45, 50, 80, 80, 70));
p = perName.get(ctx.getString(R.string.name_butterfree));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_caterpie)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "7", new EvolutionNode(perName.get(ctx.getString(R.string.name_metapod)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "10", new EvolutionNode(perName.get(ctx.getString(R.string.name_butterfree)), null));}}));}});
p.catchRate = 45;
p.weight = 32.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GUTS);this.add(Ability.SHEER_FORCE);this.add(Ability.IRON_FIST);}};
perName.put(ctx.getString(R.string.name_timburr), new Pokemon(ctx.getString(R.string.name_timburr), 532, 572, Type.FIGHTING, Type.NONE, abilities, 75, 80, 55, 25, 35, 35));
p = perName.get(ctx.getString(R.string.name_timburr));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_timburr)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_gurdurr)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_conkeldurr)), null));}}));}});
p.catchRate = 190;
p.weight = 12.5f;
p.hatch = 5355;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RUN_AWAY);this.add(Ability.EARLY_BIRD);this.add(Ability.TANGLED_FEET);}};
perName.put(ctx.getString(R.string.name_doduo), new Pokemon(ctx.getString(R.string.name_doduo), 84, 89, Type.NORMAL, Type.FLYING, abilities, 35, 85, 45, 35, 35, 75));
p = perName.get(ctx.getString(R.string.name_doduo));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_doduo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "31", new EvolutionNode(perName.get(ctx.getString(R.string.name_dodrio)), null));}});
p.catchRate = 190;
p.weight = 39.2f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ANTICIPATION);this.add(Ability.DRY_SKIN);this.add(Ability.POISON_TOUCH);}};
perName.put(ctx.getString(R.string.name_toxicroak), new Pokemon(ctx.getString(R.string.name_toxicroak), 454, 486, Type.POISON, Type.FIGHTING, abilities, 83, 106, 65, 86, 65, 85));
p = perName.get(ctx.getString(R.string.name_toxicroak));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_croagunk)), new HashMap<String, EvolutionNode>(){{this.put("niveau 37", new EvolutionNode(perName.get(ctx.getString(R.string.name_toxicroak)), null));}});
p.catchRate = 75;
p.weight = 44.4f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PURE_POWER);this.add(Ability.TELEPATHY);}};
perName.put(ctx.getString(R.string.name_medicham), new Pokemon(ctx.getString(R.string.name_medicham), 308, 329, Type.FIGHTING, Type.PSYCHIC, abilities, 60, 60, 75, 60, 75, 80));
p = perName.get(ctx.getString(R.string.name_medicham));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_meditite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_medicham)), new HashMap<String, EvolutionNode>(){{this.put("Charminite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_medicham)), null));}}));}});
p.catchRate = 90;
p.weight = 31.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.VOLT_ABSORB);this.add(Ability.QUICK_FEET);}};
perName.put(ctx.getString(R.string.name_jolteon), new Pokemon(ctx.getString(R.string.name_jolteon), 135, 144, Type.ELECTRIC, Type.NONE, abilities, 65, 65, 60, 110, 95, 130));
p = perName.get(ctx.getString(R.string.name_jolteon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_eevee)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get(ctx.getString(R.string.name_jolteon)), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_leafeon)), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get(ctx.getString(R.string.name_espeon)), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get(ctx.getString(R.string.name_sylveon)), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_vaporeon)), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_glaceon)), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get(ctx.getString(R.string.name_flareon)), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_umbreon)), null));}});
p.catchRate = 45;
p.weight = 24.5f;
p.hatch = 8960;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.FRISK);this.add(Ability.INSOMNIA);}};
perName.put(ctx.getString(R.string.name_pumpkaboo_large_size), new Pokemon(ctx.getString(R.string.name_pumpkaboo_large_size), 710, 759, Type.GHOST, Type.GRASS, abilities, 54, 66, 70, 44, 55, 51));
p = perName.get(ctx.getString(R.string.name_pumpkaboo_large_size));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pumpkaboo_large_size)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_gourgeist_large_size)), null));}});
p.catchRate = -1;
p.weight = 3.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ANTICIPATION);this.add(Ability.OVERCOAT);}};
perName.put(ctx.getString(R.string.name_wormadam_trash_cloak), new Pokemon(ctx.getString(R.string.name_wormadam_trash_cloak), 413, 443, Type.BUG, Type.NONE, abilities, 60, 69, 95, 69, 95, 36));
p = perName.get(ctx.getString(R.string.name_wormadam_trash_cloak));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_burmy)), new HashMap<String, EvolutionNode>(){{this.put("Si Male, Niveau 20", new EvolutionNode(perName.get(ctx.getString(R.string.name_mothim)), null));this.put("Si Femelle, Niveau 20", new EvolutionNode(perName.get(ctx.getString(R.string.name_wormadam_trash_cloak)), null));}});
p.catchRate = 45;
p.weight = 6.5f;
p.hatch = 3840;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STANCE_CHANGE);}};
perName.put(ctx.getString(R.string.name_aegislash_shield_forme), new Pokemon(ctx.getString(R.string.name_aegislash_shield_forme), 681, 727, Type.STEEL, Type.GHOST, abilities, 60, 150, 50, 150, 50, 60));
p = perName.get(ctx.getString(R.string.name_aegislash_shield_forme));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_honedge)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_doublade)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_aegislash_shield_forme)), null));}}));}});
p.catchRate = -1;
p.weight = 53.0f;
p.hatch = 4845;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.HEALER);}};
perName.put(ctx.getString(R.string.name_bellossom), new Pokemon(ctx.getString(R.string.name_bellossom), 182, 195, Type.GRASS, Type.NONE, abilities, 75, 80, 85, 90, 100, 50));
p = perName.get(ctx.getString(R.string.name_bellossom));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_oddish)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "21", new EvolutionNode(perName.get(ctx.getString(R.string.name_gloom)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get(ctx.getString(R.string.name_vileplume)), null));this.put("Avec une Pierresoleil", new EvolutionNode(perName.get(ctx.getString(R.string.name_bellossom)), null));}}));}});
p.catchRate = 45;
p.weight = 5.8f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SYNCHRONIZE);this.add(Ability.TRACE);this.add(Ability.TELEPATHY);}};
perName.put(ctx.getString(R.string.name_ralts), new Pokemon(ctx.getString(R.string.name_ralts), 280, 298, Type.PSYCHIC, Type.NONE, abilities, 28, 25, 25, 45, 35, 40));
p = perName.get(ctx.getString(R.string.name_ralts));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_ralts)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_kirlia)), new HashMap<String, EvolutionNode>(){{this.put("Male + Pierre Aube", new EvolutionNode(perName.get(ctx.getString(R.string.name_gallade)), null));this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_gardevoir)), new HashMap<String, EvolutionNode>(){{this.put("Gardevoirite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_gardevoir)), null));}}));}}));}});
p.catchRate = 235;
p.weight = 6.6f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INNER_FOCUS);this.add(Ability.DEFIANT);this.add(Ability.PRESSURE);}};
perName.put(ctx.getString(R.string.name_pawniard), new Pokemon(ctx.getString(R.string.name_pawniard), 624, 665, Type.STEEL, Type.DARK, abilities, 45, 85, 70, 40, 40, 60));
p = perName.get(ctx.getString(R.string.name_pawniard));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pawniard)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "52", new EvolutionNode(perName.get(ctx.getString(R.string.name_bisharp)), null));}});
p.catchRate = 120;
p.weight = 10.2f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.ROCK_HEAD);this.add(Ability.HEAVY_METAL);}};
perName.put(ctx.getString(R.string.name_lairon), new Pokemon(ctx.getString(R.string.name_lairon), 305, 325, Type.STEEL, Type.ROCK, abilities, 60, 90, 140, 50, 50, 40));
p = perName.get(ctx.getString(R.string.name_lairon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_aron)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_lairon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "42", new EvolutionNode(perName.get(ctx.getString(R.string.name_aggron)), new HashMap<String, EvolutionNode>(){{this.put("Galekingite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_aggron)), null));}}));}}));}});
p.catchRate = 90;
p.weight = 120.0f;
p.hatch = 8960;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_weezing), new Pokemon(ctx.getString(R.string.name_weezing), 110, 116, Type.POISON, Type.NONE, abilities, 65, 90, 120, 85, 70, 60));
p = perName.get(ctx.getString(R.string.name_weezing));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_koffing)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_weezing)), null));}});
p.catchRate = 60;
p.weight = 9.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.AFTERMATH);this.add(Ability.UNBURDEN);this.add(Ability.FLARE_BOOST);}};
perName.put(ctx.getString(R.string.name_drifloon), new Pokemon(ctx.getString(R.string.name_drifloon), 425, 455, Type.GHOST, Type.FLYING, abilities, 90, 50, 34, 60, 44, 70));
p = perName.get(ctx.getString(R.string.name_drifloon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_drifloon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "28", new EvolutionNode(perName.get(ctx.getString(R.string.name_drifblim)), null));}});
p.catchRate = 125;
p.weight = 1.2f;
p.hatch = 7680;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_flygon), new Pokemon(ctx.getString(R.string.name_flygon), 330, 353, Type.GROUND, Type.DRAGON, abilities, 80, 100, 80, 80, 80, 100));
p = perName.get(ctx.getString(R.string.name_flygon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_trapinch)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_vibrava)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "45", new EvolutionNode(perName.get(ctx.getString(R.string.name_flygon)), null));}}));}});
p.catchRate = 45;
p.weight = 82.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.OVERCOAT);}};
perName.put(ctx.getString(R.string.name_pineco), new Pokemon(ctx.getString(R.string.name_pineco), 204, 217, Type.BUG, Type.NONE, abilities, 50, 65, 90, 35, 35, 15));
p = perName.get(ctx.getString(R.string.name_pineco));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pineco)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "31", new EvolutionNode(perName.get(ctx.getString(R.string.name_forretress)), null));}});
p.catchRate = 190;
p.weight = 7.2f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_chingling), new Pokemon(ctx.getString(R.string.name_chingling), 433, 463, Type.PSYCHIC, Type.NONE, abilities, 45, 30, 50, 65, 50, 45));
p = perName.get(ctx.getString(R.string.name_chingling));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_chingling)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur , Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_chimecho)), null));}});
p.catchRate = 120;
p.weight = 0.6f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.BULLETPROOF);}};
perName.put(ctx.getString(R.string.name_quilladin), new Pokemon(ctx.getString(R.string.name_quilladin), 651, 697, Type.GRASS, Type.NONE, abilities, 54, 79, 101, 50, 50, 52));
p = perName.get(ctx.getString(R.string.name_quilladin));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_chespin)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_quilladin)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_chesnaught)), null));}}));}});
p.catchRate = 45;
p.weight = 29.0f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SOUNDPROOF);this.add(Ability.FILTER);this.add(Ability.TECHNICIAN);}};
perName.put(ctx.getString(R.string.name_mime_jr), new Pokemon(ctx.getString(R.string.name_mime_jr), 439, 469, Type.PSYCHIC, Type.NONE, abilities, 20, 25, 45, 70, 90, 60));
p = perName.get(ctx.getString(R.string.name_mime_jr));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mime_jr)), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l'attaque Copie", new EvolutionNode(perName.get(ctx.getString(R.string.name_mr_mime)), null));}});
p.catchRate = 145;
p.weight = 13.0f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TECHNICIAN);this.add(Ability.OWN_TEMPO);this.add(Ability.MOODY);}};
perName.put(ctx.getString(R.string.name_smeargle), new Pokemon(ctx.getString(R.string.name_smeargle), 235, 251, Type.NORMAL, Type.NONE, abilities, 55, 20, 35, 20, 45, 75));
p = perName.get(ctx.getString(R.string.name_smeargle));
p.evolutions = null;
p.catchRate = 45;
p.weight = 58.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.THICK_FAT);this.add(Ability.SCRAPPY);this.add(Ability.SAP_SIPPER);}};
perName.put(ctx.getString(R.string.name_miltank), new Pokemon(ctx.getString(R.string.name_miltank), 241, 257, Type.NORMAL, Type.NONE, abilities, 95, 80, 105, 40, 70, 100));
p = perName.get(ctx.getString(R.string.name_miltank));
p.evolutions = null;
p.catchRate = 45;
p.weight = 75.5f;
p.hatch = 5120;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.GLUTTONY);this.add(Ability.QUICK_FEET);}};
perName.put(ctx.getString(R.string.name_linoone), new Pokemon(ctx.getString(R.string.name_linoone), 264, 282, Type.NORMAL, Type.NONE, abilities, 78, 70, 61, 50, 61, 100));
p = perName.get(ctx.getString(R.string.name_linoone));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_zigzagoon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_linoone)), null));}});
p.catchRate = 90;
p.weight = 32.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ROCK_HEAD);this.add(Ability.LIGHTNINGROD);this.add(Ability.BATTLE_ARMOR);}};
perName.put(ctx.getString(R.string.name_cubone), new Pokemon(ctx.getString(R.string.name_cubone), 104, 110, Type.GROUND, Type.NONE, abilities, 50, 50, 95, 40, 50, 35));
p = perName.get(ctx.getString(R.string.name_cubone));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cubone)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "28", new EvolutionNode(perName.get(ctx.getString(R.string.name_marowak)), null));}});
p.catchRate = 190;
p.weight = 6.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.UNAWARE);this.add(Ability.SIMPLE);this.add(Ability.MOODY);}};
perName.put(ctx.getString(R.string.name_bibarel), new Pokemon(ctx.getString(R.string.name_bibarel), 400, 428, Type.NORMAL, Type.WATER, abilities, 79, 85, 60, 55, 60, 71));
p = perName.get(ctx.getString(R.string.name_bibarel));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bidoof)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "15", new EvolutionNode(perName.get(ctx.getString(R.string.name_bibarel)), null));}});
p.catchRate = 127;
p.weight = 31.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INSOMNIA);this.add(Ability.FOREWARN);this.add(Ability.INNER_FOCUS);}};
perName.put(ctx.getString(R.string.name_hypno), new Pokemon(ctx.getString(R.string.name_hypno), 97, 103, Type.PSYCHIC, Type.NONE, abilities, 85, 73, 70, 73, 115, 67));
p = perName.get(ctx.getString(R.string.name_hypno));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_drowzee)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "26", new EvolutionNode(perName.get(ctx.getString(R.string.name_hypno)), null));}});
p.catchRate = 75;
p.weight = 75.6f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SUCTION_CUPS);this.add(Ability.STORM_DRAIN);}};
perName.put(ctx.getString(R.string.name_lileep), new Pokemon(ctx.getString(R.string.name_lileep), 345, 368, Type.ROCK, Type.GRASS, abilities, 66, 41, 77, 61, 87, 23));
p = perName.get(ctx.getString(R.string.name_lileep));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_lileep)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_cradily)), null));}});
p.catchRate = 45;
p.weight = 23.8f;
p.hatch = 7680;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER3};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_rotom_mow_rotom), new Pokemon(ctx.getString(R.string.name_rotom_mow_rotom), 479, 517, Type.ELECTRIC, Type.GHOST, abilities, 50, 65, 107, 105, 107, 86));
p = perName.get(ctx.getString(R.string.name_rotom_mow_rotom));
p.evolutions = null;
p.catchRate = 45;
p.weight = 0.3f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MOLD_BREAKER);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_cranidos), new Pokemon(ctx.getString(R.string.name_cranidos), 408, 436, Type.ROCK, Type.NONE, abilities, 67, 125, 40, 30, 30, 58));
p = perName.get(ctx.getString(R.string.name_cranidos));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cranidos)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_rampardos)), null));}});
p.catchRate = 45;
p.weight = 31.5f;
p.hatch = 7680;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OBLIVIOUS);this.add(Ability.SNOW_CLOAK);this.add(Ability.THICK_FAT);}};
perName.put(ctx.getString(R.string.name_mamoswine), new Pokemon(ctx.getString(R.string.name_mamoswine), 473, 506, Type.ICE, Type.GROUND, abilities, 110, 130, 80, 70, 60, 80));
p = perName.get(ctx.getString(R.string.name_mamoswine));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_swinub)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "33", new EvolutionNode(perName.get(ctx.getString(R.string.name_piloswine)), new HashMap<String, EvolutionNode>(){{this.put("En connaissant l'attaque Pouv.Antique et lui faire monter d'un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_mamoswine)), null));}}));}});
p.catchRate = 50;
p.weight = 291.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 2.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STENCH);this.add(Ability.AFTERMATH);}};
perName.put(ctx.getString(R.string.name_stunky), new Pokemon(ctx.getString(R.string.name_stunky), 434, 464, Type.POISON, Type.DARK, abilities, 63, 63, 47, 41, 41, 74));
p = perName.get(ctx.getString(R.string.name_stunky));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_stunky)), new HashMap<String, EvolutionNode>(){{this.put("niveau 34", new EvolutionNode(perName.get(ctx.getString(R.string.name_skuntank)), null));}});
p.catchRate = 225;
p.weight = 19.2f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STENCH);this.add(Ability.WEAK_ARMOR);this.add(Ability.AFTERMATH);}};
perName.put(ctx.getString(R.string.name_garbodor), new Pokemon(ctx.getString(R.string.name_garbodor), 569, 610, Type.POISON, Type.NONE, abilities, 80, 95, 82, 60, 82, 75));
p = perName.get(ctx.getString(R.string.name_garbodor));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_trubbish)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_garbodor)), null));}});
p.catchRate = 60;
p.weight = 107.3f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GLUTTONY);this.add(Ability.FLASH_FIRE);this.add(Ability.WHITE_SMOKE);}};
perName.put(ctx.getString(R.string.name_heatmor), new Pokemon(ctx.getString(R.string.name_heatmor), 631, 672, Type.FIRE, Type.NONE, abilities, 85, 97, 66, 105, 66, 65));
p = perName.get(ctx.getString(R.string.name_heatmor));
p.evolutions = null;
p.catchRate = 90;
p.weight = 58.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.THICK_FAT);this.add(Ability.GUTS);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_makuhita), new Pokemon(ctx.getString(R.string.name_makuhita), 296, 315, Type.FIGHTING, Type.NONE, abilities, 72, 60, 30, 20, 30, 25));
p = perName.get(ctx.getString(R.string.name_makuhita));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_makuhita)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "24", new EvolutionNode(perName.get(ctx.getString(R.string.name_hariyama)), null));}});
p.catchRate = 180;
p.weight = 86.4f;
p.hatch = 5120;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.FRISK);this.add(Ability.SAP_SIPPER);}};
perName.put(ctx.getString(R.string.name_stantler), new Pokemon(ctx.getString(R.string.name_stantler), 234, 250, Type.NORMAL, Type.NONE, abilities, 73, 95, 62, 85, 65, 85));
p = perName.get(ctx.getString(R.string.name_stantler));
p.evolutions = null;
p.catchRate = 45;
p.weight = 71.2f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SYNCHRONIZE);this.add(Ability.INNER_FOCUS);this.add(Ability.MAGIC_GUARD);}};
perName.put(ctx.getString(R.string.name_alakazam), new Pokemon(ctx.getString(R.string.name_alakazam), 65, 69, Type.PSYCHIC, Type.NONE, abilities, 55, 50, 45, 135, 85, 120));
p = perName.get(ctx.getString(R.string.name_alakazam));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_abra)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_kadabra)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_alakazam)), new HashMap<String, EvolutionNode>(){{this.put("Alakazamite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_alakazam)), null));}}));}}));}});
p.catchRate = 50;
p.weight = 48.0f;
p.hatch = 5120;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TOUGH_CLAWS);}};
perName.put(ctx.getString(R.string.name_mega_charizard_x), new Pokemon(ctx.getString(R.string.name_mega_charizard_x), 6, 8, Type.FIRE, Type.DRAGON, abilities, 78, 130, 111, 130, 85, 100));
p = perName.get(ctx.getString(R.string.name_mega_charizard_x));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_charmander)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_charmeleon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_charizard)), new HashMap<String, EvolutionNode>(){{this.put("Dracaufite X", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_charizard_x)), null));this.put("Dracaufite Y", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_charizard_y)), null));}}));}}));}});
p.catchRate = -1;
p.weight = 110.5f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.SOLAR_POWER);}};
perName.put(ctx.getString(R.string.name_charmeleon), new Pokemon(ctx.getString(R.string.name_charmeleon), 5, 6, Type.FIRE, Type.NONE, abilities, 58, 64, 58, 80, 65, 80));
p = perName.get(ctx.getString(R.string.name_charmeleon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_charmander)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_charmeleon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_charizard)), new HashMap<String, EvolutionNode>(){{this.put("Dracaufite X", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_charizard_x)), null));this.put("Dracaufite Y", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_charizard_y)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 19.0f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.DRAGON};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SOLID_ROCK);this.add(Ability.STURDY);this.add(Ability.SWIFT_SWIM);}};
perName.put(ctx.getString(R.string.name_tirtouga), new Pokemon(ctx.getString(R.string.name_tirtouga), 564, 605, Type.WATER, Type.ROCK, abilities, 54, 78, 103, 53, 45, 22));
p = perName.get(ctx.getString(R.string.name_tirtouga));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tirtouga)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_carracosta)), null));}});
p.catchRate = 45;
p.weight = 16.5f;
p.hatch = 7905;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER3};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.POISON_POINT);this.add(Ability.SNIPER);this.add(Ability.DAMP);}};
perName.put(ctx.getString(R.string.name_seadra), new Pokemon(ctx.getString(R.string.name_seadra), 117, 124, Type.WATER, Type.NONE, abilities, 55, 65, 95, 95, 45, 85));
p = perName.get(ctx.getString(R.string.name_seadra));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_horsea)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_seadra)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Ecaille Draco", new EvolutionNode(perName.get(ctx.getString(R.string.name_kingdra)), null));}}));}});
p.catchRate = 75;
p.weight = 25.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.DRAGON};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.SHELL_ARMOR);}};
perName.put(ctx.getString(R.string.name_turtwig), new Pokemon(ctx.getString(R.string.name_turtwig), 387, 415, Type.GRASS, Type.NONE, abilities, 55, 68, 64, 45, 55, 31));
p = perName.get(ctx.getString(R.string.name_turtwig));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_turtwig)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_grotle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_torterra)), null));}}));}});
p.catchRate = 45;
p.weight = 10.2f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.GRASS};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INNER_FOCUS);this.add(Ability.ICE_BODY);this.add(Ability.MOODY);}};
perName.put(ctx.getString(R.string.name_snorunt), new Pokemon(ctx.getString(R.string.name_snorunt), 361, 386, Type.ICE, Type.NONE, abilities, 50, 50, 50, 50, 50, 50));
p = perName.get(ctx.getString(R.string.name_snorunt));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_snorunt)), new HashMap<String, EvolutionNode>(){{this.put("Femelle + Pierre Aube", new EvolutionNode(perName.get(ctx.getString(R.string.name_froslass)), null));this.put(ctx.getString(R.string.level) + "42", new EvolutionNode(perName.get(ctx.getString(R.string.name_glalie)), null));}});
p.catchRate = 190;
p.weight = 16.8f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY,EggGroup.MINERAL};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWARM);this.add(Ability.SHELL_ARMOR);this.add(Ability.OVERCOAT);}};
perName.put(ctx.getString(R.string.name_escavalier), new Pokemon(ctx.getString(R.string.name_escavalier), 589, 630, Type.BUG, Type.STEEL, abilities, 70, 135, 105, 60, 105, 20));
p = perName.get(ctx.getString(R.string.name_escavalier));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_karrablast)), new HashMap<String, EvolutionNode>(){{this.put("Echange avec Escargaume", new EvolutionNode(perName.get(ctx.getString(R.string.name_escavalier)), null));}});
p.catchRate = 75;
p.weight = 33.0f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SOUNDPROOF);this.add(Ability.RATTLED);}};
perName.put(ctx.getString(R.string.name_whismur), new Pokemon(ctx.getString(R.string.name_whismur), 293, 312, Type.NORMAL, Type.NONE, abilities, 64, 51, 23, 51, 23, 28));
p = perName.get(ctx.getString(R.string.name_whismur));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_whismur)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_loudred)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_exploud)), null));}}));}});
p.catchRate = 190;
p.weight = 16.3f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.FIELD};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_rotom_normal_rotom), new Pokemon(ctx.getString(R.string.name_rotom_normal_rotom), 479, 512, Type.ELECTRIC, Type.GHOST, abilities, 50, 50, 77, 95, 77, 91));
p = perName.get(ctx.getString(R.string.name_rotom_normal_rotom));
p.evolutions = null;
p.catchRate = 45;
p.weight = 0.3f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLAME_BODY);this.add(Ability.VITAL_SPIRIT);}};
perName.put(ctx.getString(R.string.name_magmortar), new Pokemon(ctx.getString(R.string.name_magmortar), 467, 500, Type.FIRE, Type.NONE, abilities, 75, 95, 67, 125, 95, 83));
p = perName.get(ctx.getString(R.string.name_magmortar));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_magby)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_magmar)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Magmariseur", new EvolutionNode(perName.get(ctx.getString(R.string.name_magmortar)), null));}}));}});
p.catchRate = 30;
p.weight = 68.0f;
p.hatch = 6400;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TRUANT);}};
perName.put(ctx.getString(R.string.name_slakoth), new Pokemon(ctx.getString(R.string.name_slakoth), 287, 306, Type.NORMAL, Type.NONE, abilities, 60, 60, 60, 35, 35, 30));
p = perName.get(ctx.getString(R.string.name_slakoth));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_slakoth)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_vigoroth)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_slaking)), null));}}));}});
p.catchRate = 255;
p.weight = 24.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STATIC);}};
perName.put(ctx.getString(R.string.name_mareep), new Pokemon(ctx.getString(R.string.name_mareep), 179, 191, Type.ELECTRIC, Type.NONE, abilities, 55, 40, 40, 65, 45, 35));
p = perName.get(ctx.getString(R.string.name_mareep));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mareep)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "15", new EvolutionNode(perName.get(ctx.getString(R.string.name_flaaffy)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_ampharos)), new HashMap<String, EvolutionNode>(){{this.put("Pharampite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_ampharos)), null));}}));}}));}});
p.catchRate = 235;
p.weight = 7.8f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.MONSTER};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SNIPER);this.add(Ability.TOUGH_CLAWS);this.add(Ability.PICKPOCKET);}};
perName.put(ctx.getString(R.string.name_binacle), new Pokemon(ctx.getString(R.string.name_binacle), 688, 735, Type.ROCK, Type.WATER, abilities, 50, 95, 95, 30, 80, 60));
p = perName.get(ctx.getString(R.string.name_binacle));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_binacle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "39", new EvolutionNode(perName.get(ctx.getString(R.string.name_barbaracle)), null));}});
p.catchRate = -1;
p.weight = 31.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER3};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.DEFIANT);}};
perName.put(ctx.getString(R.string.name_prinplup), new Pokemon(ctx.getString(R.string.name_prinplup), 394, 422, Type.WATER, Type.NONE, abilities, 64, 66, 68, 81, 76, 50));
p = perName.get(ctx.getString(R.string.name_prinplup));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_piplup)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_prinplup)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_empoleon)), null));}}));}});
p.catchRate = 45;
p.weight = 23.0f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_tynamo), new Pokemon(ctx.getString(R.string.name_tynamo), 602, 643, Type.ELECTRIC, Type.NONE, abilities, 35, 55, 40, 45, 40, 60));
p = perName.get(ctx.getString(R.string.name_tynamo));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tynamo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "39", new EvolutionNode(perName.get(ctx.getString(R.string.name_eelektrik)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get(ctx.getString(R.string.name_eelektross)), null));}}));}});
p.catchRate = 190;
p.weight = 0.3f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PLUS);this.add(Ability.LIGHTNINGROD);}};
perName.put(ctx.getString(R.string.name_plusle), new Pokemon(ctx.getString(R.string.name_plusle), 311, 334, Type.ELECTRIC, Type.NONE, abilities, 60, 50, 40, 85, 75, 95));
p = perName.get(ctx.getString(R.string.name_plusle));
p.evolutions = null;
p.catchRate = 200;
p.weight = 4.2f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STANCE_CHANGE);}};
perName.put(ctx.getString(R.string.name_aegislash_blade_forme), new Pokemon(ctx.getString(R.string.name_aegislash_blade_forme), 681, 728, Type.STEEL, Type.GHOST, abilities, 60, 50, 150, 50, 150, 60));
p = perName.get(ctx.getString(R.string.name_aegislash_blade_forme));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_honedge)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_doublade)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_aegislash_blade_forme)), null));}}));}});
p.catchRate = -1;
p.weight = 53.0f;
p.hatch = 4845;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STATIC);this.add(Ability.VITAL_SPIRIT);}};
perName.put(ctx.getString(R.string.name_elekid), new Pokemon(ctx.getString(R.string.name_elekid), 239, 255, Type.ELECTRIC, Type.NONE, abilities, 45, 63, 37, 65, 55, 95));
p = perName.get(ctx.getString(R.string.name_elekid));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_elekid)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_electabuzz)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Electiriseur", new EvolutionNode(perName.get(ctx.getString(R.string.name_electivire)), null));}}));}});
p.catchRate = 45;
p.weight = 23.5f;
p.hatch = 6400;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLAME_BODY);this.add(Ability.GALE_WINGS);}};
perName.put(ctx.getString(R.string.name_talonflame), new Pokemon(ctx.getString(R.string.name_talonflame), 663, 709, Type.FIRE, Type.FLYING, abilities, 78, 81, 71, 74, 69, 126));
p = perName.get(ctx.getString(R.string.name_talonflame));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_fletchling)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "17", new EvolutionNode(perName.get(ctx.getString(R.string.name_fletchinder)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_talonflame)), null));}}));}});
p.catchRate = -1;
p.weight = 24.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_baltoy), new Pokemon(ctx.getString(R.string.name_baltoy), 343, 366, Type.GROUND, Type.PSYCHIC, abilities, 40, 40, 55, 40, 70, 55));
p = perName.get(ctx.getString(R.string.name_baltoy));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_baltoy)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_claydol)), null));}});
p.catchRate = 255;
p.weight = 21.5f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.COMPOUNDEYE);this.add(Ability.SPEED_BOOST);this.add(Ability.FRISK);}};
perName.put(ctx.getString(R.string.name_yanma), new Pokemon(ctx.getString(R.string.name_yanma), 193, 206, Type.BUG, Type.FLYING, abilities, 65, 65, 45, 75, 45, 95));
p = perName.get(ctx.getString(R.string.name_yanma));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_yanma)), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l' attaque  Pouv.Antique", new EvolutionNode(perName.get(ctx.getString(R.string.name_yanmega)), null));}});
p.catchRate = 75;
p.weight = 38.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BIG_PECKS);this.add(Ability.SUPER_LUCK);this.add(Ability.RIVALRY);}};
perName.put(ctx.getString(R.string.name_pidove), new Pokemon(ctx.getString(R.string.name_pidove), 519, 559, Type.NORMAL, Type.FLYING, abilities, 50, 55, 50, 36, 30, 43));
p = perName.get(ctx.getString(R.string.name_pidove));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pidove)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "21", new EvolutionNode(perName.get(ctx.getString(R.string.name_tranquill)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_unfezant)), null));}}));}});
p.catchRate = 255;
p.weight = 2.1f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_eelektrik), new Pokemon(ctx.getString(R.string.name_eelektrik), 603, 644, Type.ELECTRIC, Type.NONE, abilities, 65, 85, 70, 75, 70, 40));
p = perName.get(ctx.getString(R.string.name_eelektrik));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tynamo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "39", new EvolutionNode(perName.get(ctx.getString(R.string.name_eelektrik)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get(ctx.getString(R.string.name_eelektross)), null));}}));}});
p.catchRate = 60;
p.weight = 22.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SYNCHRONIZE);this.add(Ability.TRACE);this.add(Ability.TELEPATHY);}};
perName.put(ctx.getString(R.string.name_kirlia), new Pokemon(ctx.getString(R.string.name_kirlia), 281, 299, Type.PSYCHIC, Type.NONE, abilities, 38, 35, 35, 65, 55, 50));
p = perName.get(ctx.getString(R.string.name_kirlia));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_ralts)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_kirlia)), new HashMap<String, EvolutionNode>(){{this.put("Male + Pierre Aube", new EvolutionNode(perName.get(ctx.getString(R.string.name_gallade)), null));this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_gardevoir)), new HashMap<String, EvolutionNode>(){{this.put("Gardevoirite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_gardevoir)), null));}}));}}));}});
p.catchRate = 120;
p.weight = 20.2f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.KEEN_EYE);this.add(Ability.BIG_PECKS);this.add(Ability.HYDRATION);}};
perName.put(ctx.getString(R.string.name_ducklett), new Pokemon(ctx.getString(R.string.name_ducklett), 580, 621, Type.WATER, Type.FLYING, abilities, 62, 44, 50, 44, 50, 55));
p = perName.get(ctx.getString(R.string.name_ducklett));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_ducklett)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_swanna)), null));}});
p.catchRate = 190;
p.weight = 5.5f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FLYING};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.RUN_AWAY);}};
perName.put(ctx.getString(R.string.name_oddish), new Pokemon(ctx.getString(R.string.name_oddish), 43, 47, Type.GRASS, Type.POISON, abilities, 45, 50, 55, 75, 65, 30));
p = perName.get(ctx.getString(R.string.name_oddish));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_oddish)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "21", new EvolutionNode(perName.get(ctx.getString(R.string.name_gloom)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get(ctx.getString(R.string.name_vileplume)), null));this.put("Avec une Pierresoleil", new EvolutionNode(perName.get(ctx.getString(R.string.name_bellossom)), null));}}));}});
p.catchRate = 255;
p.weight = 5.4f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CLEAR_BODY);this.add(Ability.LIGHT_METAL);}};
perName.put(ctx.getString(R.string.name_metang), new Pokemon(ctx.getString(R.string.name_metang), 375, 400, Type.STEEL, Type.PSYCHIC, abilities, 60, 75, 100, 55, 80, 50));
p = perName.get(ctx.getString(R.string.name_metang));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_beldum)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_metang)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "45", new EvolutionNode(perName.get(ctx.getString(R.string.name_metagross)), null));}}));}});
p.catchRate = 3;
p.weight = 202.5f;
p.hatch = 10240;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STICKY_HOLD);this.add(Ability.STORM_DRAIN);this.add(Ability.SAND_FORCE);}};
perName.put(ctx.getString(R.string.name_gastrodon), new Pokemon(ctx.getString(R.string.name_gastrodon), 423, 453, Type.WATER, Type.GROUND, abilities, 111, 83, 68, 92, 82, 39));
p = perName.get(ctx.getString(R.string.name_gastrodon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_shellos)), new HashMap<String, EvolutionNode>(){{this.put("niveau 30", new EvolutionNode(perName.get(ctx.getString(R.string.name_gastrodon)), null));}});
p.catchRate = 75;
p.weight = 29.9f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.UNKNOWN};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INNER_FOCUS);this.add(Ability.MULTISCALE);}};
perName.put(ctx.getString(R.string.name_dragonite), new Pokemon(ctx.getString(R.string.name_dragonite), 149, 159, Type.DRAGON, Type.FLYING, abilities, 91, 134, 95, 100, 100, 80));
p = perName.get(ctx.getString(R.string.name_dragonite));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_dratini)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_dragonair)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "55", new EvolutionNode(perName.get(ctx.getString(R.string.name_dragonite)), null));}}));}});
p.catchRate = 45;
p.weight = 210.0f;
p.hatch = 10240;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON,EggGroup.WATER1};
p.size = 2.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.OWN_TEMPO);this.add(Ability.LEAF_GUARD);}};
perName.put(ctx.getString(R.string.name_lilligant), new Pokemon(ctx.getString(R.string.name_lilligant), 549, 589, Type.GRASS, Type.NONE, abilities, 70, 60, 75, 110, 75, 90));
p = perName.get(ctx.getString(R.string.name_lilligant));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_petilil)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierresoleil", new EvolutionNode(perName.get(ctx.getString(R.string.name_lilligant)), null));}});
p.catchRate = 75;
p.weight = 16.3f;
p.hatch = 5355;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.DOWNLOAD);}};
perName.put(ctx.getString(R.string.name_genesect), new Pokemon(ctx.getString(R.string.name_genesect), 649, 695, Type.BUG, Type.STEEL, abilities, 71, 120, 95, 120, 95, 99));
p = perName.get(ctx.getString(R.string.name_genesect));
p.evolutions = null;
p.catchRate = 3;
p.weight = 82.5f;
p.hatch = 30855;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.POISON_POINT);this.add(Ability.RIVALRY);this.add(Ability.HUSTLE);}};
perName.put(ctx.getString(R.string.name_nidorino), new Pokemon(ctx.getString(R.string.name_nidorino), 33, 37, Type.POISON, Type.NONE, abilities, 61, 72, 57, 55, 55, 65));
p = perName.get(ctx.getString(R.string.name_nidorino));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_nidoran_m)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_nidorino)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get(ctx.getString(R.string.name_nidoking)), null));}}));}});
p.catchRate = 120;
p.weight = 19.5f;
p.hatch = 5120;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.FIELD};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INSOMNIA);this.add(Ability.FRISK);this.add(Ability.CURSED_BODY);}};
perName.put(ctx.getString(R.string.name_banette), new Pokemon(ctx.getString(R.string.name_banette), 354, 377, Type.GHOST, Type.NONE, abilities, 64, 115, 65, 83, 63, 65));
p = perName.get(ctx.getString(R.string.name_banette));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_shuppet)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_banette)), new HashMap<String, EvolutionNode>(){{this.put("Branettite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_banette)), null));}}));}});
p.catchRate = 45;
p.weight = 12.5f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.POISON_POINT);this.add(Ability.RIVALRY);this.add(Ability.HUSTLE);}};
perName.put(ctx.getString(R.string.name_nidorina), new Pokemon(ctx.getString(R.string.name_nidorina), 30, 34, Type.POISON, Type.NONE, abilities, 70, 62, 67, 55, 55, 56));
p = perName.get(ctx.getString(R.string.name_nidorina));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_nidoran_f)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_nidorina)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get(ctx.getString(R.string.name_nidoqueen)), null));}}));}});
p.catchRate = 120;
p.weight = 20.0f;
p.hatch = 5120;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LIGHTNINGROD);this.add(Ability.ROCK_HEAD);this.add(Ability.RECKLESS);}};
perName.put(ctx.getString(R.string.name_rhydon), new Pokemon(ctx.getString(R.string.name_rhydon), 112, 118, Type.GROUND, Type.ROCK, abilities, 105, 130, 120, 45, 45, 40));
p = perName.get(ctx.getString(R.string.name_rhydon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_rhyhorn)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "42", new EvolutionNode(perName.get(ctx.getString(R.string.name_rhydon)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Protecteur", new EvolutionNode(perName.get(ctx.getString(R.string.name_rhyperior)), null));}}));}});
p.catchRate = 60;
p.weight = 120.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.FIELD};
p.size = 1.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SLOW_START);}};
perName.put(ctx.getString(R.string.name_regigigas), new Pokemon(ctx.getString(R.string.name_regigigas), 486, 524, Type.NORMAL, Type.NONE, abilities, 110, 160, 110, 80, 110, 100));
p = perName.get(ctx.getString(R.string.name_regigigas));
p.evolutions = null;
p.catchRate = 3;
p.weight = 420.0f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 3.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CLEAR_BODY);this.add(Ability.LIQUID_OOZE);this.add(Ability.RAIN_DISH);}};
perName.put(ctx.getString(R.string.name_tentacruel), new Pokemon(ctx.getString(R.string.name_tentacruel), 73, 78, Type.WATER, Type.POISON, abilities, 80, 70, 65, 80, 120, 100));
p = perName.get(ctx.getString(R.string.name_tentacruel));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tentacool)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_tentacruel)), null));}});
p.catchRate = 60;
p.weight = 55.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER3};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.OWN_TEMPO);this.add(Ability.LEAF_GUARD);}};
perName.put(ctx.getString(R.string.name_petilil), new Pokemon(ctx.getString(R.string.name_petilil), 548, 588, Type.GRASS, Type.NONE, abilities, 45, 35, 50, 70, 50, 30));
p = perName.get(ctx.getString(R.string.name_petilil));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_petilil)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierresoleil", new EvolutionNode(perName.get(ctx.getString(R.string.name_lilligant)), null));}});
p.catchRate = 190;
p.weight = 6.6f;
p.hatch = 5355;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHEER_FORCE);this.add(Ability.ZEN_MODE);}};
perName.put(ctx.getString(R.string.name_darmanitan_zen_mode), new Pokemon(ctx.getString(R.string.name_darmanitan_zen_mode), 555, 596, Type.FIRE, Type.NONE, abilities, 105, 30, 105, 140, 105, 55));
p = perName.get(ctx.getString(R.string.name_darmanitan_zen_mode));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_darumaka)), null);
p.catchRate = 60;
p.weight = 92.9f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.VITAL_SPIRIT);this.add(Ability.ANGER_POINT);this.add(Ability.DEFIANT);}};
perName.put(ctx.getString(R.string.name_mankey), new Pokemon(ctx.getString(R.string.name_mankey), 56, 60, Type.FIGHTING, Type.NONE, abilities, 40, 80, 35, 35, 45, 70));
p = perName.get(ctx.getString(R.string.name_mankey));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mankey)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "28", new EvolutionNode(perName.get(ctx.getString(R.string.name_primeape)), null));}});
p.catchRate = 190;
p.weight = 28.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OBLIVIOUS);this.add(Ability.OWN_TEMPO);this.add(Ability.REGENERATOR);}};
perName.put(ctx.getString(R.string.name_slowbro), new Pokemon(ctx.getString(R.string.name_slowbro), 80, 85, Type.WATER, Type.PSYCHIC, abilities, 95, 75, 110, 100, 80, 30));
p = perName.get(ctx.getString(R.string.name_slowbro));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_slowpoke)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_slowbro)), null));this.put("Echange en tenant Roche Royale", new EvolutionNode(perName.get(ctx.getString(R.string.name_slowking)), null));}});
p.catchRate = 75;
p.weight = 78.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.WATER1};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHED_SKIN);this.add(Ability.RUN_AWAY);}};
perName.put(ctx.getString(R.string.name_kricketot), new Pokemon(ctx.getString(R.string.name_kricketot), 401, 429, Type.BUG, Type.NONE, abilities, 37, 25, 41, 25, 41, 25));
p = perName.get(ctx.getString(R.string.name_kricketot));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_kricketot)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "10", new EvolutionNode(perName.get(ctx.getString(R.string.name_kricketune)), null));}});
p.catchRate = 255;
p.weight = 2.2f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLOWER_VEIL);this.add(Ability.SYMBIOSIS);}};
perName.put(ctx.getString(R.string.name_florges), new Pokemon(ctx.getString(R.string.name_florges), 671, 717, Type.FAIRY, Type.NONE, abilities, 78, 65, 68, 112, 154, 75));
p = perName.get(ctx.getString(R.string.name_florges));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_flabebe)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "19", new EvolutionNode(perName.get(ctx.getString(R.string.name_floette)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get(ctx.getString(R.string.name_florges)), null));}}));}});
p.catchRate = -1;
p.weight = 10.0f;
p.hatch = -1;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HYPER_CUTTER);this.add(Ability.MOLD_BREAKER);this.add(Ability.MOXIE);}};
perName.put(ctx.getString(R.string.name_pinsir), new Pokemon(ctx.getString(R.string.name_pinsir), 127, 134, Type.BUG, Type.NONE, abilities, 65, 125, 100, 55, 70, 85));
p = perName.get(ctx.getString(R.string.name_pinsir));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pinsir)), new HashMap<String, EvolutionNode>(){{this.put("Scarabruite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_pinsir)), null));}});
p.catchRate = 45;
p.weight = 55.0f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWARM);this.add(Ability.INSOMNIA);this.add(Ability.SNIPER);}};
perName.put(ctx.getString(R.string.name_spinarak), new Pokemon(ctx.getString(R.string.name_spinarak), 167, 179, Type.BUG, Type.POISON, abilities, 40, 60, 40, 40, 40, 30));
p = perName.get(ctx.getString(R.string.name_spinarak));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_spinarak)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "22", new EvolutionNode(perName.get(ctx.getString(R.string.name_ariados)), null));}});
p.catchRate = 255;
p.weight = 8.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RUN_AWAY);this.add(Ability.EARLY_BIRD);this.add(Ability.TANGLED_FEET);}};
perName.put(ctx.getString(R.string.name_dodrio), new Pokemon(ctx.getString(R.string.name_dodrio), 85, 90, Type.NORMAL, Type.FLYING, abilities, 60, 110, 70, 60, 60, 100));
p = perName.get(ctx.getString(R.string.name_dodrio));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_doduo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "31", new EvolutionNode(perName.get(ctx.getString(R.string.name_dodrio)), null));}});
p.catchRate = 45;
p.weight = 85.2f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.COMPOUNDEYE);this.add(Ability.TANGLED_FEET);this.add(Ability.BIG_PECKS);}};
perName.put(ctx.getString(R.string.name_chatot), new Pokemon(ctx.getString(R.string.name_chatot), 441, 471, Type.NORMAL, Type.FLYING, abilities, 76, 65, 45, 92, 42, 91));
p = perName.get(ctx.getString(R.string.name_chatot));
p.evolutions = null;
p.catchRate = 30;
p.weight = 1.9f;
p.hatch = 2560;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.COMPOUNDEYE);this.add(Ability.SHIELD_DUST);this.add(Ability.FRIEND_GUARD);}};
perName.put(ctx.getString(R.string.name_scatterbug), new Pokemon(ctx.getString(R.string.name_scatterbug), 664, 710, Type.BUG, Type.NONE, abilities, 38, 35, 40, 27, 25, 35));
p = perName.get(ctx.getString(R.string.name_scatterbug));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_scatterbug)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "9", new EvolutionNode(perName.get(ctx.getString(R.string.name_spewpa)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "12", new EvolutionNode(perName.get(ctx.getString(R.string.name_vivillon)), null));}}));}});
p.catchRate = -1;
p.weight = 2.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RECKLESS);this.add(Ability.ADAPTABILITY);this.add(Ability.MOLD_BREAKER);}};
perName.put(ctx.getString(R.string.name_basculin), new Pokemon(ctx.getString(R.string.name_basculin), 550, 590, Type.WATER, Type.NONE, abilities, 70, 92, 65, 80, 55, 98));
p = perName.get(ctx.getString(R.string.name_basculin));
p.evolutions = null;
p.catchRate = 25;
p.weight = 18.0f;
p.hatch = 10455;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER2};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHED_SKIN);}};
perName.put(ctx.getString(R.string.name_metapod), new Pokemon(ctx.getString(R.string.name_metapod), 11, 15, Type.BUG, Type.NONE, abilities, 50, 20, 55, 25, 25, 30));
p = perName.get(ctx.getString(R.string.name_metapod));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_caterpie)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "7", new EvolutionNode(perName.get(ctx.getString(R.string.name_metapod)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "10", new EvolutionNode(perName.get(ctx.getString(R.string.name_butterfree)), null));}}));}});
p.catchRate = 120;
p.weight = 9.9f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SOUNDPROOF);this.add(Ability.STATIC);this.add(Ability.AFTERMATH);}};
perName.put(ctx.getString(R.string.name_electrode), new Pokemon(ctx.getString(R.string.name_electrode), 101, 107, Type.ELECTRIC, Type.NONE, abilities, 60, 50, 70, 80, 80, 140));
p = perName.get(ctx.getString(R.string.name_electrode));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_voltorb)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_electrode)), null));}});
p.catchRate = 60;
p.weight = 66.6f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ICE_BODY);this.add(Ability.WEAK_ARMOR);}};
perName.put(ctx.getString(R.string.name_vanillite), new Pokemon(ctx.getString(R.string.name_vanillite), 582, 623, Type.ICE, Type.NONE, abilities, 36, 50, 50, 65, 60, 44));
p = perName.get(ctx.getString(R.string.name_vanillite));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_vanillite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_vanillish)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "47", new EvolutionNode(perName.get(ctx.getString(R.string.name_vanilluxe)), null));}}));}});
p.catchRate = 255;
p.weight = 5.7f;
p.hatch = 3533;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SNOW_CLOAK);this.add(Ability.ICE_BODY);}};
perName.put(ctx.getString(R.string.name_glaceon), new Pokemon(ctx.getString(R.string.name_glaceon), 471, 504, Type.ICE, Type.NONE, abilities, 65, 60, 110, 130, 95, 65));
p = perName.get(ctx.getString(R.string.name_glaceon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_eevee)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get(ctx.getString(R.string.name_jolteon)), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_leafeon)), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get(ctx.getString(R.string.name_espeon)), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get(ctx.getString(R.string.name_sylveon)), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_vaporeon)), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_glaceon)), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get(ctx.getString(R.string.name_flareon)), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_umbreon)), null));}});
p.catchRate = 45;
p.weight = 25.9f;
p.hatch = 8960;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LIQUID_OOZE);this.add(Ability.STICKY_HOLD);this.add(Ability.GLUTTONY);}};
perName.put(ctx.getString(R.string.name_gulpin), new Pokemon(ctx.getString(R.string.name_gulpin), 316, 339, Type.POISON, Type.NONE, abilities, 70, 43, 53, 43, 53, 40));
p = perName.get(ctx.getString(R.string.name_gulpin));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_gulpin)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "26", new EvolutionNode(perName.get(ctx.getString(R.string.name_swalot)), null));}});
p.catchRate = 225;
p.weight = 10.3f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.IRON_FIST);this.add(Ability.KLUTZ);this.add(Ability.NO_GUARD);}};
perName.put(ctx.getString(R.string.name_golett), new Pokemon(ctx.getString(R.string.name_golett), 622, 663, Type.GROUND, Type.GHOST, abilities, 59, 74, 50, 35, 50, 35));
p = perName.get(ctx.getString(R.string.name_golett));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_golett)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "43", new EvolutionNode(perName.get(ctx.getString(R.string.name_golurk)), null));}});
p.catchRate = 190;
p.weight = 92.0f;
p.hatch = 6630;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STENCH);this.add(Ability.STICKY_HOLD);this.add(Ability.AFTERMATH);}};
perName.put(ctx.getString(R.string.name_trubbish), new Pokemon(ctx.getString(R.string.name_trubbish), 568, 609, Type.POISON, Type.NONE, abilities, 50, 50, 62, 40, 62, 65));
p = perName.get(ctx.getString(R.string.name_trubbish));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_trubbish)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_garbodor)), null));}});
p.catchRate = 190;
p.weight = 31.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SERENE_GRACE);this.add(Ability.HUSTLE);this.add(Ability.SUPER_LUCK);}};
perName.put(ctx.getString(R.string.name_togepi), new Pokemon(ctx.getString(R.string.name_togepi), 175, 187, Type.NORMAL, Type.NONE, abilities, 35, 20, 65, 40, 65, 20));
p = perName.get(ctx.getString(R.string.name_togepi));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_togepi)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_togetic)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get(ctx.getString(R.string.name_togekiss)), null));}}));}});
p.catchRate = 190;
p.weight = 1.5f;
p.hatch = 2560;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INSOMNIA);this.add(Ability.SUPER_LUCK);this.add(Ability.MOXIE);}};
perName.put(ctx.getString(R.string.name_honchkrow), new Pokemon(ctx.getString(R.string.name_honchkrow), 430, 460, Type.DARK, Type.FLYING, abilities, 100, 125, 52, 105, 52, 71));
p = perName.get(ctx.getString(R.string.name_honchkrow));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_murkrow)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_honchkrow)), null));}});
p.catchRate = 30;
p.weight = 27.3f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GLUTTONY);this.add(Ability.BLAZE);}};
perName.put(ctx.getString(R.string.name_pansear), new Pokemon(ctx.getString(R.string.name_pansear), 513, 553, Type.FIRE, Type.NONE, abilities, 50, 53, 48, 53, 48, 64));
p = perName.get(ctx.getString(R.string.name_pansear));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pansear)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Feu", new EvolutionNode(perName.get(ctx.getString(R.string.name_simisear)), null));}});
p.catchRate = 190;
p.weight = 11.0f;
p.hatch = 5355;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.RECKLESS);}};
perName.put(ctx.getString(R.string.name_staravia), new Pokemon(ctx.getString(R.string.name_staravia), 397, 425, Type.NORMAL, Type.FLYING, abilities, 55, 75, 50, 40, 40, 80));
p = perName.get(ctx.getString(R.string.name_staravia));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_starly)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "14", new EvolutionNode(perName.get(ctx.getString(R.string.name_staravia)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "34", new EvolutionNode(perName.get(ctx.getString(R.string.name_staraptor)), null));}}));}});
p.catchRate = 120;
p.weight = 15.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.SHED_SKIN);this.add(Ability.UNNERVE);}};
perName.put(ctx.getString(R.string.name_ekans), new Pokemon(ctx.getString(R.string.name_ekans), 23, 27, Type.POISON, Type.NONE, abilities, 35, 60, 44, 40, 54, 55));
p = perName.get(ctx.getString(R.string.name_ekans));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_ekans)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "22", new EvolutionNode(perName.get(ctx.getString(R.string.name_arbok)), null));}});
p.catchRate = 255;
p.weight = 6.9f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.DRAGON};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.THICK_FAT);this.add(Ability.ICE_BODY);this.add(Ability.OBLIVIOUS);}};
perName.put(ctx.getString(R.string.name_spheal), new Pokemon(ctx.getString(R.string.name_spheal), 363, 388, Type.ICE, Type.WATER, abilities, 70, 40, 50, 55, 50, 25));
p = perName.get(ctx.getString(R.string.name_spheal));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_spheal)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_sealeo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "44", new EvolutionNode(perName.get(ctx.getString(R.string.name_walrein)), null));}}));}});
p.catchRate = 255;
p.weight = 39.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SUCTION_CUPS);this.add(Ability.SNIPER);this.add(Ability.MOODY);}};
perName.put(ctx.getString(R.string.name_octillery), new Pokemon(ctx.getString(R.string.name_octillery), 224, 239, Type.WATER, Type.NONE, abilities, 75, 105, 75, 105, 75, 45));
p = perName.get(ctx.getString(R.string.name_octillery));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_remoraid)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_octillery)), null));}});
p.catchRate = 75;
p.weight = 28.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER2};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GLUTTONY);this.add(Ability.OVERGROW);}};
perName.put(ctx.getString(R.string.name_pansage), new Pokemon(ctx.getString(R.string.name_pansage), 511, 551, Type.GRASS, Type.NONE, abilities, 50, 53, 48, 53, 48, 64));
p = perName.get(ctx.getString(R.string.name_pansage));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pansage)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get(ctx.getString(R.string.name_simisage)), null));}});
p.catchRate = 190;
p.weight = 10.5f;
p.hatch = 5355;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.AURA_BREAK);}};
perName.put(ctx.getString(R.string.name_zygarde), new Pokemon(ctx.getString(R.string.name_zygarde), 718, 771, Type.DRAGON, Type.GROUND, abilities, 108, 100, 121, 81, 95, 95));
p = perName.get(ctx.getString(R.string.name_zygarde));
p.evolutions = null;
p.catchRate = -1;
p.weight = 305.0f;
p.hatch = -1;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 5.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STATIC);}};
perName.put(ctx.getString(R.string.name_pikachu), new Pokemon(ctx.getString(R.string.name_pikachu), 25, 29, Type.ELECTRIC, Type.NONE, abilities, 35, 55, 30, 50, 40, 90));
p = perName.get(ctx.getString(R.string.name_pikachu));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pichu)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_pikachu)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get(ctx.getString(R.string.name_raichu)), null));}}));}});
p.catchRate = 190;
p.weight = 6.0f;
p.hatch = 2560;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.FAIRY};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ILLUSION);}};
perName.put(ctx.getString(R.string.name_zoroark), new Pokemon(ctx.getString(R.string.name_zoroark), 571, 612, Type.DARK, Type.NONE, abilities, 60, 105, 60, 120, 60, 105));
p = perName.get(ctx.getString(R.string.name_zoroark));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_zorua)), new HashMap<String, EvolutionNode>(){{this.put("Niv 30", new EvolutionNode(perName.get(ctx.getString(R.string.name_zoroark)), null));}});
p.catchRate = 45;
p.weight = 81.1f;
p.hatch = 5535;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HUGE_POWER);}};
perName.put(ctx.getString(R.string.name_mega_mawile), new Pokemon(ctx.getString(R.string.name_mega_mawile), 303, 323, Type.STEEL, Type.FAIRY, abilities, 50, 105, 125, 55, 95, 50));
p = perName.get(ctx.getString(R.string.name_mega_mawile));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mawile)), new HashMap<String, EvolutionNode>(){{this.put("Mysdibulite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_mawile)), null));}});
p.catchRate = -1;
p.weight = 23.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.SAND_FORCE);}};
perName.put(ctx.getString(R.string.name_roggenrola), new Pokemon(ctx.getString(R.string.name_roggenrola), 524, 564, Type.ROCK, Type.NONE, abilities, 55, 75, 85, 25, 25, 15));
p = perName.get(ctx.getString(R.string.name_roggenrola));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_roggenrola)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_boldore)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_gigalith)), null));}}));}});
p.catchRate = 255;
p.weight = 18.0f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LIGHTNINGROD);this.add(Ability.SOLID_ROCK);this.add(Ability.RECKLESS);}};
perName.put(ctx.getString(R.string.name_rhyperior), new Pokemon(ctx.getString(R.string.name_rhyperior), 464, 497, Type.GROUND, Type.ROCK, abilities, 115, 140, 130, 55, 55, 40));
p = perName.get(ctx.getString(R.string.name_rhyperior));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_rhyhorn)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "42", new EvolutionNode(perName.get(ctx.getString(R.string.name_rhydon)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Protecteur", new EvolutionNode(perName.get(ctx.getString(R.string.name_rhyperior)), null));}}));}});
p.catchRate = 30;
p.weight = 282.8f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.FIELD};
p.size = 2.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PIXILATE);}};
perName.put(ctx.getString(R.string.name_mega_gardevoir), new Pokemon(ctx.getString(R.string.name_mega_gardevoir), 282, 301, Type.PSYCHIC, Type.FAIRY, abilities, 68, 85, 65, 165, 135, 100));
p = perName.get(ctx.getString(R.string.name_mega_gardevoir));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_ralts)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_kirlia)), new HashMap<String, EvolutionNode>(){{this.put("Male + Pierre Aube", new EvolutionNode(perName.get(ctx.getString(R.string.name_gallade)), null));this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_gardevoir)), new HashMap<String, EvolutionNode>(){{this.put("Gardevoirite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_gardevoir)), null));}}));}}));}});
p.catchRate = -1;
p.weight = 48.4f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SPEED_BOOST);}};
perName.put(ctx.getString(R.string.name_mega_blaziken), new Pokemon(ctx.getString(R.string.name_mega_blaziken), 257, 275, Type.FIRE, Type.FIGHTING, abilities, 80, 160, 80, 130, 80, 100));
p = perName.get(ctx.getString(R.string.name_mega_blaziken));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_torchic)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_combusken)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_blaziken)), new HashMap<String, EvolutionNode>(){{this.put("Brasegalite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_blaziken)), null));}}));}}));}});
p.catchRate = -1;
p.weight = 52f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.EARLY_BIRD);this.add(Ability.PICKPOCKET);}};
perName.put(ctx.getString(R.string.name_seedot), new Pokemon(ctx.getString(R.string.name_seedot), 273, 291, Type.GRASS, Type.NONE, abilities, 40, 40, 50, 30, 30, 30));
p = perName.get(ctx.getString(R.string.name_seedot));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_seedot)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "14", new EvolutionNode(perName.get(ctx.getString(R.string.name_nuzleaf)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get(ctx.getString(R.string.name_shiftry)), null));}}));}});
p.catchRate = 255;
p.weight = 4.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.GRASS};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.POISON_POINT);this.add(Ability.INTIMIDATE);}};
perName.put(ctx.getString(R.string.name_qwilfish), new Pokemon(ctx.getString(R.string.name_qwilfish), 211, 224, Type.WATER, Type.POISON, abilities, 65, 95, 75, 55, 55, 85));
p = perName.get(ctx.getString(R.string.name_qwilfish));
p.evolutions = null;
p.catchRate = 45;
p.weight = 3.9f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER2};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_VEIL);this.add(Ability.ROUGH_SKIN);}};
perName.put(ctx.getString(R.string.name_garchomp), new Pokemon(ctx.getString(R.string.name_garchomp), 445, 475, Type.DRAGON, Type.GROUND, abilities, 108, 130, 95, 80, 85, 102));
p = perName.get(ctx.getString(R.string.name_garchomp));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_gible)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "24", new EvolutionNode(perName.get(ctx.getString(R.string.name_gabite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "48", new EvolutionNode(perName.get(ctx.getString(R.string.name_garchomp)), new HashMap<String, EvolutionNode>(){{this.put("Carchacrokite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_garchomp)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 95.0f;
p.hatch = 10240;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON,EggGroup.MONSTER};
p.size = 1.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_latios), new Pokemon(ctx.getString(R.string.name_latios), 381, 406, Type.DRAGON, Type.PSYCHIC, abilities, 80, 90, 80, 130, 110, 110));
p = perName.get(ctx.getString(R.string.name_latios));
p.evolutions = null;
p.catchRate = 3;
p.weight = 60.0f;
p.hatch = 30720;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.THICK_FAT);this.add(Ability.OWN_TEMPO);this.add(Ability.GLUTTONY);}};
perName.put(ctx.getString(R.string.name_grumpig), new Pokemon(ctx.getString(R.string.name_grumpig), 326, 349, Type.PSYCHIC, Type.NONE, abilities, 80, 45, 65, 90, 110, 80));
p = perName.get(ctx.getString(R.string.name_grumpig));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_spoink)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_grumpig)), null));}});
p.catchRate = 60;
p.weight = 71.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ANTICIPATION);this.add(Ability.OVERCOAT);}};
perName.put(ctx.getString(R.string.name_wormadam_plant_cloak), new Pokemon(ctx.getString(R.string.name_wormadam_plant_cloak), 413, 441, Type.BUG, Type.NONE, abilities, 60, 59, 85, 79, 105, 36));
p = perName.get(ctx.getString(R.string.name_wormadam_plant_cloak));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_burmy)), new HashMap<String, EvolutionNode>(){{this.put("Si Male, Niveau 20", new EvolutionNode(perName.get(ctx.getString(R.string.name_mothim)), null));this.put("Si Femelle, Niveau 20", new EvolutionNode(perName.get(ctx.getString(R.string.name_wormadam_plant_cloak)), null));}});
p.catchRate = 45;
p.weight = 6.5f;
p.hatch = 3840;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INNER_FOCUS);this.add(Ability.ICE_BODY);this.add(Ability.MOODY);}};
perName.put(ctx.getString(R.string.name_glalie), new Pokemon(ctx.getString(R.string.name_glalie), 362, 387, Type.ICE, Type.NONE, abilities, 80, 80, 80, 80, 80, 80));
p = perName.get(ctx.getString(R.string.name_glalie));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_snorunt)), new HashMap<String, EvolutionNode>(){{this.put("Femelle + Pierre Aube", new EvolutionNode(perName.get(ctx.getString(R.string.name_froslass)), null));this.put(ctx.getString(R.string.level) + "42", new EvolutionNode(perName.get(ctx.getString(R.string.name_glalie)), null));}});
p.catchRate = 75;
p.weight = 256.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY,EggGroup.MINERAL};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ROCK_HEAD);this.add(Ability.STURDY);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_steelix), new Pokemon(ctx.getString(R.string.name_steelix), 208, 221, Type.STEEL, Type.GROUND, abilities, 75, 85, 200, 55, 65, 30));
p = perName.get(ctx.getString(R.string.name_steelix));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_onix)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Peau Metal", new EvolutionNode(perName.get(ctx.getString(R.string.name_steelix)), null));}});
p.catchRate = 25;
p.weight = 400.0f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 9.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_mesprit), new Pokemon(ctx.getString(R.string.name_mesprit), 481, 519, Type.PSYCHIC, Type.NONE, abilities, 80, 105, 105, 105, 105, 80));
p = perName.get(ctx.getString(R.string.name_mesprit));
p.evolutions = null;
p.catchRate = 3;
p.weight = 0.3f;
p.hatch = 20480;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);}};
perName.put(ctx.getString(R.string.name_zapdos), new Pokemon(ctx.getString(R.string.name_zapdos), 145, 155, Type.ELECTRIC, Type.FLYING, abilities, 90, 90, 85, 125, 90, 100));
p = perName.get(ctx.getString(R.string.name_zapdos));
p.evolutions = null;
p.catchRate = 3;
p.weight = 52.6f;
p.hatch = 20480;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.SAND_VEIL);}};
perName.put(ctx.getString(R.string.name_phanpy), new Pokemon(ctx.getString(R.string.name_phanpy), 231, 247, Type.GROUND, Type.NONE, abilities, 90, 60, 60, 40, 40, 40));
p = perName.get(ctx.getString(R.string.name_phanpy));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_phanpy)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_donphan)), null));}});
p.catchRate = 120;
p.weight = 33.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_uxie), new Pokemon(ctx.getString(R.string.name_uxie), 480, 518, Type.PSYCHIC, Type.NONE, abilities, 75, 75, 130, 75, 130, 95));
p = perName.get(ctx.getString(R.string.name_uxie));
p.evolutions = null;
p.catchRate = 3;
p.weight = 0.3f;
p.hatch = 20480;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);}};
perName.put(ctx.getString(R.string.name_gloom), new Pokemon(ctx.getString(R.string.name_gloom), 44, 48, Type.GRASS, Type.POISON, abilities, 60, 65, 70, 85, 75, 40));
p = perName.get(ctx.getString(R.string.name_gloom));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_oddish)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "21", new EvolutionNode(perName.get(ctx.getString(R.string.name_gloom)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get(ctx.getString(R.string.name_vileplume)), null));this.put("Avec une Pierresoleil", new EvolutionNode(perName.get(ctx.getString(R.string.name_bellossom)), null));}}));}});
p.catchRate = 120;
p.weight = 8.6f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CLEAR_BODY);this.add(Ability.LIGHT_METAL);}};
perName.put(ctx.getString(R.string.name_metagross), new Pokemon(ctx.getString(R.string.name_metagross), 376, 401, Type.STEEL, Type.PSYCHIC, abilities, 80, 135, 130, 95, 90, 70));
p = perName.get(ctx.getString(R.string.name_metagross));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_beldum)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_metang)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "45", new EvolutionNode(perName.get(ctx.getString(R.string.name_metagross)), null));}}));}});
p.catchRate = 3;
p.weight = 550.0f;
p.hatch = 10240;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.THICK_FAT);this.add(Ability.HUGE_POWER);this.add(Ability.SAP_SIPPER);}};
perName.put(ctx.getString(R.string.name_azumarill), new Pokemon(ctx.getString(R.string.name_azumarill), 184, 197, Type.WATER, Type.NONE, abilities, 100, 50, 80, 50, 80, 50));
p = perName.get(ctx.getString(R.string.name_azumarill));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_azurill)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_marill)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_azumarill)), null));}}));}});
p.catchRate = 75;
p.weight = 28.5f;
p.hatch = 2560;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FAIRY};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.DRIZZLE);}};
perName.put(ctx.getString(R.string.name_kyogre), new Pokemon(ctx.getString(R.string.name_kyogre), 382, 407, Type.WATER, Type.NONE, abilities, 100, 100, 90, 150, 140, 90));
p = perName.get(ctx.getString(R.string.name_kyogre));
p.evolutions = null;
p.catchRate = 5;
p.weight = 352.0f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 4.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRANKSTER);}};
perName.put(ctx.getString(R.string.name_mega_banette), new Pokemon(ctx.getString(R.string.name_mega_banette), 354, 378, Type.GHOST, Type.NONE, abilities, 64, 165, 75, 93, 83, 75));
p = perName.get(ctx.getString(R.string.name_mega_banette));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_shuppet)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_banette)), new HashMap<String, EvolutionNode>(){{this.put("Branettite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_banette)), null));}}));}});
p.catchRate = -1;
p.weight = 13f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_VEIL);this.add(Ability.HYPER_CUTTER);this.add(Ability.IMMUNITY);}};
perName.put(ctx.getString(R.string.name_gligar), new Pokemon(ctx.getString(R.string.name_gligar), 207, 220, Type.GROUND, Type.FLYING, abilities, 65, 75, 105, 35, 65, 85));
p = perName.get(ctx.getString(R.string.name_gligar));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_gligar)), new HashMap<String, EvolutionNode>(){{this.put("Gagne un niveau de nuit en tenant un Croc Rasoir", new EvolutionNode(perName.get(ctx.getString(R.string.name_gliscor)), null));}});
p.catchRate = 60;
p.weight = 64.8f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHIELD_DUST);this.add(Ability.RUN_AWAY);}};
perName.put(ctx.getString(R.string.name_wurmple), new Pokemon(ctx.getString(R.string.name_wurmple), 265, 283, Type.BUG, Type.NONE, abilities, 45, 45, 35, 20, 30, 20));
p = perName.get(ctx.getString(R.string.name_wurmple));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_wurmple)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "10", new EvolutionNode(perName.get(ctx.getString(R.string.name_dustox)), null));this.put(ctx.getString(R.string.level) + "7, au hasard", new EvolutionNode(perName.get(ctx.getString(R.string.name_cascoon)), null));}});
p.catchRate = 255;
p.weight = 3.6f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STATIC);this.add(Ability.VITAL_SPIRIT);}};
perName.put(ctx.getString(R.string.name_electabuzz), new Pokemon(ctx.getString(R.string.name_electabuzz), 125, 132, Type.ELECTRIC, Type.NONE, abilities, 65, 83, 57, 95, 85, 105));
p = perName.get(ctx.getString(R.string.name_electabuzz));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_elekid)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_electabuzz)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Electiriseur", new EvolutionNode(perName.get(ctx.getString(R.string.name_electivire)), null));}}));}});
p.catchRate = 45;
p.weight = 30.0f;
p.hatch = 6400;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.VITAL_SPIRIT);}};
perName.put(ctx.getString(R.string.name_vigoroth), new Pokemon(ctx.getString(R.string.name_vigoroth), 288, 307, Type.NORMAL, Type.NONE, abilities, 80, 80, 80, 55, 55, 90));
p = perName.get(ctx.getString(R.string.name_vigoroth));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_slakoth)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_vigoroth)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_slaking)), null));}}));}});
p.catchRate = 120;
p.weight = 46.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NATURAL_CURE);this.add(Ability.SERENE_GRACE);this.add(Ability.HEALER);}};
perName.put(ctx.getString(R.string.name_chansey), new Pokemon(ctx.getString(R.string.name_chansey), 113, 119, Type.NORMAL, Type.NONE, abilities, 250, 5, 5, 35, 105, 50));
p = perName.get(ctx.getString(R.string.name_chansey));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_happiny)), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau en tenant une Pierre Ovale", new EvolutionNode(perName.get(ctx.getString(R.string.name_chansey)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_blissey)), null));}}));}});
p.catchRate = 30;
p.weight = 34.6f;
p.hatch = 10240;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RUN_AWAY);this.add(Ability.KEEN_EYE);this.add(Ability.FRISK);}};
perName.put(ctx.getString(R.string.name_furret), new Pokemon(ctx.getString(R.string.name_furret), 162, 174, Type.NORMAL, Type.NONE, abilities, 85, 76, 64, 45, 55, 90));
p = perName.get(ctx.getString(R.string.name_furret));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_sentret)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "15", new EvolutionNode(perName.get(ctx.getString(R.string.name_furret)), null));}});
p.catchRate = 90;
p.weight = 32.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.ROCK_HEAD);this.add(Ability.RATTLED);}};
perName.put(ctx.getString(R.string.name_sudowoodo), new Pokemon(ctx.getString(R.string.name_sudowoodo), 185, 198, Type.ROCK, Type.NONE, abilities, 70, 100, 115, 30, 65, 30));
p = perName.get(ctx.getString(R.string.name_sudowoodo));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bonsly)), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l'attaque Copie", new EvolutionNode(perName.get(ctx.getString(R.string.name_sudowoodo)), null));}});
p.catchRate = 65;
p.weight = 61.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SNOW_CLOAK);this.add(Ability.SWIFT_SWIM);}};
perName.put(ctx.getString(R.string.name_beartic), new Pokemon(ctx.getString(R.string.name_beartic), 614, 655, Type.ICE, Type.NONE, abilities, 95, 110, 80, 70, 80, 50));
p = perName.get(ctx.getString(R.string.name_beartic));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cubchoo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_beartic)), null));}});
p.catchRate = 60;
p.weight = 260.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 2.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.WATER_ABSORB);this.add(Ability.CHLOROPHYLL);this.add(Ability.STORM_DRAIN);}};
perName.put(ctx.getString(R.string.name_maractus), new Pokemon(ctx.getString(R.string.name_maractus), 556, 597, Type.GRASS, Type.NONE, abilities, 75, 86, 67, 106, 67, 60));
p = perName.get(ctx.getString(R.string.name_maractus));
p.evolutions = null;
p.catchRate = 255;
p.weight = 28.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.REFRIGERATE);this.add(Ability.SNOW_WARNING);}};
perName.put(ctx.getString(R.string.name_aurorus), new Pokemon(ctx.getString(R.string.name_aurorus), 699, 746, Type.ROCK, Type.ICE, abilities, 123, 77, 72, 99, 92, 58));
p = perName.get(ctx.getString(R.string.name_aurorus));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_amaura)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "39 pendant la nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_aurorus)), null));}});
p.catchRate = 45;
p.weight = 225.0f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 2.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWARM);this.add(Ability.TECHNICIAN);this.add(Ability.STEADFAST);}};
perName.put(ctx.getString(R.string.name_scyther), new Pokemon(ctx.getString(R.string.name_scyther), 123, 130, Type.BUG, Type.FLYING, abilities, 70, 110, 80, 55, 80, 105));
p = perName.get(ctx.getString(R.string.name_scyther));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_scyther)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Peau Metal", new EvolutionNode(perName.get(ctx.getString(R.string.name_scizor)), new HashMap<String, EvolutionNode>(){{this.put("Mega-Evolution", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_scizor)), null));}}));}});
p.catchRate = 45;
p.weight = 56.0f;
p.hatch = 6400;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RUN_AWAY);this.add(Ability.KLUTZ);this.add(Ability.LIMBER);}};
perName.put(ctx.getString(R.string.name_buneary), new Pokemon(ctx.getString(R.string.name_buneary), 427, 457, Type.NORMAL, Type.NONE, abilities, 55, 66, 44, 44, 56, 85));
p = perName.get(ctx.getString(R.string.name_buneary));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_buneary)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_lopunny)), null));}});
p.catchRate = 190;
p.weight = 5.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.HUMANLIKE};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INSOMNIA);this.add(Ability.KEEN_EYE);this.add(Ability.TINTED_LENS);}};
perName.put(ctx.getString(R.string.name_hoot_hoot), new Pokemon(ctx.getString(R.string.name_hoot_hoot), 163, 175, Type.NORMAL, Type.FLYING, abilities, 60, 30, 30, 36, 56, 50));
p = perName.get(ctx.getString(R.string.name_hoot_hoot));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_hoot_hoot)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_noctowl)), null));}});
p.catchRate = 255;
p.weight = 21.2f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.WATER_ABSORB);this.add(Ability.SHELL_ARMOR);this.add(Ability.HYDRATION);}};
perName.put(ctx.getString(R.string.name_lapras), new Pokemon(ctx.getString(R.string.name_lapras), 131, 140, Type.WATER, Type.ICE, abilities, 130, 85, 80, 85, 95, 60));
p = perName.get(ctx.getString(R.string.name_lapras));
p.evolutions = null;
p.catchRate = 45;
p.weight = 220.0f;
p.hatch = 10240;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.WATER1};
p.size = 2.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);this.add(Ability.INFILTRATOR);}};
perName.put(ctx.getString(R.string.name_spiritomb), new Pokemon(ctx.getString(R.string.name_spiritomb), 442, 472, Type.GHOST, Type.DARK, abilities, 50, 92, 108, 92, 108, 35));
p = perName.get(ctx.getString(R.string.name_spiritomb));
p.evolutions = null;
p.catchRate = 100;
p.weight = 108f;
p.hatch = 7680;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MAGMA_ARMOR);this.add(Ability.FLAME_BODY);this.add(Ability.WEAK_ARMOR);}};
perName.put(ctx.getString(R.string.name_slugma), new Pokemon(ctx.getString(R.string.name_slugma), 218, 233, Type.FIRE, Type.NONE, abilities, 40, 40, 40, 70, 40, 20));
p = perName.get(ctx.getString(R.string.name_slugma));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_slugma)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "38", new EvolutionNode(perName.get(ctx.getString(R.string.name_magcargo)), null));}});
p.catchRate = 190;
p.weight = 35.0f;
p.hatch = 5610;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.EFFECT_SPORE);this.add(Ability.DRY_SKIN);}};
perName.put(ctx.getString(R.string.name_paras), new Pokemon(ctx.getString(R.string.name_paras), 46, 50, Type.BUG, Type.GRASS, abilities, 35, 70, 55, 45, 55, 25));
p = perName.get(ctx.getString(R.string.name_paras));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_paras)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "24", new EvolutionNode(perName.get(ctx.getString(R.string.name_parasect)), null));}});
p.catchRate = 190;
p.weight = 5.4f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG,EggGroup.GRASS};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLAME_BODY);this.add(Ability.SWARM);}};
perName.put(ctx.getString(R.string.name_larvesta), new Pokemon(ctx.getString(R.string.name_larvesta), 636, 677, Type.BUG, Type.FIRE, abilities, 55, 85, 55, 50, 55, 60));
p = perName.get(ctx.getString(R.string.name_larvesta));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_larvesta)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "59", new EvolutionNode(perName.get(ctx.getString(R.string.name_volcarona)), null));}});
p.catchRate = 45;
p.weight = 28.8f;
p.hatch = 10455;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERCOAT);this.add(Ability.MAGIC_GUARD);this.add(Ability.REGENERATOR);}};
perName.put(ctx.getString(R.string.name_reuniclus), new Pokemon(ctx.getString(R.string.name_reuniclus), 579, 620, Type.PSYCHIC, Type.NONE, abilities, 110, 65, 75, 125, 85, 30));
p = perName.get(ctx.getString(R.string.name_reuniclus));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_solosis)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_duosion)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "41", new EvolutionNode(perName.get(ctx.getString(R.string.name_reuniclus)), null));}}));}});
p.catchRate = 50;
p.weight = 20.1f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CUTE_CHARM);this.add(Ability.MAGIC_GUARD);this.add(Ability.FRIEND_GUARD);}};
perName.put(ctx.getString(R.string.name_cleffa), new Pokemon(ctx.getString(R.string.name_cleffa), 173, 185, Type.NORMAL, Type.NONE, abilities, 50, 25, 28, 45, 55, 15));
p = perName.get(ctx.getString(R.string.name_cleffa));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cleffa)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_clefairy)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get(ctx.getString(R.string.name_clefable)), null));}}));}});
p.catchRate = 150;
p.weight = 3.0f;
p.hatch = 2560;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.CONTRARY);}};
perName.put(ctx.getString(R.string.name_servine), new Pokemon(ctx.getString(R.string.name_servine), 496, 536, Type.GRASS, Type.NONE, abilities, 60, 60, 75, 60, 75, 83));
p = perName.get(ctx.getString(R.string.name_servine));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_snivy)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "17", new EvolutionNode(perName.get(ctx.getString(R.string.name_servine)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_serperior)), null));}}));}});
p.catchRate = 45;
p.weight = 16f;
p.hatch = 5355;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.GRASS};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.UNBURDEN);}};
perName.put(ctx.getString(R.string.name_treecko), new Pokemon(ctx.getString(R.string.name_treecko), 252, 269, Type.GRASS, Type.NONE, abilities, 40, 45, 35, 65, 55, 70));
p = perName.get(ctx.getString(R.string.name_treecko));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_treecko)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_grovyle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_sceptile)), null));}}));}});
p.catchRate = 45;
p.weight = 5.0f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.DRAGON};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);this.add(Ability.HEATPROOF);this.add(Ability.HEAVY_METAL);}};
perName.put(ctx.getString(R.string.name_bronzor), new Pokemon(ctx.getString(R.string.name_bronzor), 436, 466, Type.STEEL, Type.PSYCHIC, abilities, 57, 24, 86, 24, 86, 23));
p = perName.get(ctx.getString(R.string.name_bronzor));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bronzor)), new HashMap<String, EvolutionNode>(){{this.put("niveau 33", new EvolutionNode(perName.get(ctx.getString(R.string.name_bronzong)), null));}});
p.catchRate = 255;
p.weight = 60.5f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.FRISK);this.add(Ability.INSOMNIA);}};
perName.put(ctx.getString(R.string.name_gourgeist_average_size), new Pokemon(ctx.getString(R.string.name_gourgeist_average_size), 711, 762, Type.GHOST, Type.GRASS, abilities, 65, 90, 122, 58, 75, 84));
p = perName.get(ctx.getString(R.string.name_gourgeist_average_size));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pumpkaboo_average_size)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_gourgeist_average_size)), null));}});
p.catchRate = -1;
p.weight = 9.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_misdreavus), new Pokemon(ctx.getString(R.string.name_misdreavus), 200, 213, Type.GHOST, Type.NONE, abilities, 60, 60, 60, 85, 85, 85));
p = perName.get(ctx.getString(R.string.name_misdreavus));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_misdreavus)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_mismagius)), null));}});
p.catchRate = 45;
p.weight = 1.0f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MEGA_LAUNCHER);}};
perName.put(ctx.getString(R.string.name_mega_blastoise), new Pokemon(ctx.getString(R.string.name_mega_blastoise), 9, 13, Type.WATER, Type.NONE, abilities, 79, 103, 120, 135, 115, 78));
p = perName.get(ctx.getString(R.string.name_mega_blastoise));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_squirtle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_wartortle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_blastoise)), new HashMap<String, EvolutionNode>(){{this.put("Tortankite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_blastoise)), null));}}));}}));}});
p.catchRate = -1;
p.weight = 101.1f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.POISON_POINT);this.add(Ability.SWARM);this.add(Ability.QUICK_FEET);}};
perName.put(ctx.getString(R.string.name_venipede), new Pokemon(ctx.getString(R.string.name_venipede), 543, 583, Type.BUG, Type.POISON, abilities, 30, 45, 59, 30, 39, 57));
p = perName.get(ctx.getString(R.string.name_venipede));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_venipede)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "22", new EvolutionNode(perName.get(ctx.getString(R.string.name_whirlipede)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_scolipede)), null));}}));}});
p.catchRate = 255;
p.weight = 5.3f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRANKSTER);this.add(Ability.INFILTRATOR);this.add(Ability.CHLOROPHYLL);}};
perName.put(ctx.getString(R.string.name_cottonee), new Pokemon(ctx.getString(R.string.name_cottonee), 546, 586, Type.GRASS, Type.NONE, abilities, 40, 27, 60, 37, 50, 66));
p = perName.get(ctx.getString(R.string.name_cottonee));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cottonee)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierresoleil", new EvolutionNode(perName.get(ctx.getString(R.string.name_whimsicott)), null));}});
p.catchRate = 190;
p.weight = 0.6f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS,EggGroup.FAIRY};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.THICK_FAT);this.add(Ability.HYDRATION);this.add(Ability.ICE_BODY);}};
perName.put(ctx.getString(R.string.name_dewgong), new Pokemon(ctx.getString(R.string.name_dewgong), 87, 92, Type.WATER, Type.ICE, abilities, 90, 70, 80, 70, 95, 70));
p = perName.get(ctx.getString(R.string.name_dewgong));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_seel)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "34", new EvolutionNode(perName.get(ctx.getString(R.string.name_dewgong)), null));}});
p.catchRate = 75;
p.weight = 120.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.EFFECT_SPORE);this.add(Ability.DRY_SKIN);}};
perName.put(ctx.getString(R.string.name_parasect), new Pokemon(ctx.getString(R.string.name_parasect), 47, 51, Type.BUG, Type.GRASS, abilities, 60, 95, 80, 60, 80, 30));
p = perName.get(ctx.getString(R.string.name_parasect));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_paras)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "24", new EvolutionNode(perName.get(ctx.getString(R.string.name_parasect)), null));}});
p.catchRate = 75;
p.weight = 29.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG,EggGroup.GRASS};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LIQUID_OOZE);this.add(Ability.STICKY_HOLD);this.add(Ability.GLUTTONY);}};
perName.put(ctx.getString(R.string.name_swalot), new Pokemon(ctx.getString(R.string.name_swalot), 317, 340, Type.POISON, Type.NONE, abilities, 100, 73, 83, 73, 83, 55));
p = perName.get(ctx.getString(R.string.name_swalot));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_gulpin)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "26", new EvolutionNode(perName.get(ctx.getString(R.string.name_swalot)), null));}});
p.catchRate = 75;
p.weight = 80.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SOUNDPROOF);this.add(Ability.STATIC);this.add(Ability.AFTERMATH);}};
perName.put(ctx.getString(R.string.name_voltorb), new Pokemon(ctx.getString(R.string.name_voltorb), 100, 106, Type.ELECTRIC, Type.NONE, abilities, 40, 30, 50, 55, 55, 100));
p = perName.get(ctx.getString(R.string.name_voltorb));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_voltorb)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_electrode)), null));}});
p.catchRate = 190;
p.weight = 10.4f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.RATTLED);}};
perName.put(ctx.getString(R.string.name_magikarp), new Pokemon(ctx.getString(R.string.name_magikarp), 129, 137, Type.WATER, Type.NONE, abilities, 20, 10, 55, 15, 20, 80));
p = perName.get(ctx.getString(R.string.name_magikarp));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_magikarp)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_gyarados)), new HashMap<String, EvolutionNode>(){{this.put("Leviatorite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_gyarados)), null));}}));}});
p.catchRate = 255;
p.weight = 10.0f;
p.hatch = 1280;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER2,EggGroup.DRAGON};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHEER_FORCE);this.add(Ability.ZEN_MODE);}};
perName.put(ctx.getString(R.string.name_darmanitan_standard_mode), new Pokemon(ctx.getString(R.string.name_darmanitan_standard_mode), 555, 595, Type.FIRE, Type.NONE, abilities, 105, 140, 55, 30, 55, 95));
p = perName.get(ctx.getString(R.string.name_darmanitan_standard_mode));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_darumaka)), null);
p.catchRate = 60;
p.weight = 92.9f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GUTS);this.add(Ability.SCRAPPY);}};
perName.put(ctx.getString(R.string.name_swellow), new Pokemon(ctx.getString(R.string.name_swellow), 277, 295, Type.NORMAL, Type.FLYING, abilities, 60, 85, 60, 50, 50, 125));
p = perName.get(ctx.getString(R.string.name_swellow));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_taillow)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "22", new EvolutionNode(perName.get(ctx.getString(R.string.name_swellow)), null));}});
p.catchRate = 45;
p.weight = 19.8f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.IRON_BARBS);}};
perName.put(ctx.getString(R.string.name_ferrothorn), new Pokemon(ctx.getString(R.string.name_ferrothorn), 598, 639, Type.GRASS, Type.STEEL, abilities, 74, 94, 131, 54, 116, 20));
p = perName.get(ctx.getString(R.string.name_ferrothorn));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_ferroseed)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_ferrothorn)), null));}});
p.catchRate = 90;
p.weight = 110f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS,EggGroup.MINERAL};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.DAMP);}};
perName.put(ctx.getString(R.string.name_swampert), new Pokemon(ctx.getString(R.string.name_swampert), 260, 278, Type.WATER, Type.GROUND, abilities, 100, 110, 90, 85, 90, 60));
p = perName.get(ctx.getString(R.string.name_swampert));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mudkip)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_marshtomp)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_swampert)), null));}}));}});
p.catchRate = 45;
p.weight = 81.9f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.WATER1};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.DAMP);}};
perName.put(ctx.getString(R.string.name_mudkip), new Pokemon(ctx.getString(R.string.name_mudkip), 258, 276, Type.WATER, Type.NONE, abilities, 50, 70, 50, 50, 50, 40));
p = perName.get(ctx.getString(R.string.name_mudkip));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mudkip)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_marshtomp)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_swampert)), null));}}));}});
p.catchRate = 45;
p.weight = 7.6f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.WATER1};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INNER_FOCUS);this.add(Ability.KEEN_EYE);this.add(Ability.DEFIANT);}};
perName.put(ctx.getString(R.string.name_farfetchd), new Pokemon(ctx.getString(R.string.name_farfetchd), 83, 88, Type.NORMAL, Type.FLYING, abilities, 52, 65, 55, 58, 62, 60));
p = perName.get(ctx.getString(R.string.name_farfetchd));
p.evolutions = null;
p.catchRate = 45;
p.weight = 15.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING,EggGroup.FIELD};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.DROUGHT);}};
perName.put(ctx.getString(R.string.name_groudon), new Pokemon(ctx.getString(R.string.name_groudon), 383, 408, Type.GROUND, Type.NONE, abilities, 100, 150, 140, 100, 90, 90));
p = perName.get(ctx.getString(R.string.name_groudon));
p.evolutions = null;
p.catchRate = 5;
p.weight = 950.0f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 3.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SNOW_WARNING);this.add(Ability.SOUNDPROOF);}};
perName.put(ctx.getString(R.string.name_abomasnow), new Pokemon(ctx.getString(R.string.name_abomasnow), 460, 492, Type.GRASS, Type.ICE, abilities, 90, 92, 75, 92, 85, 60));
p = perName.get(ctx.getString(R.string.name_abomasnow));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_snover)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_abomasnow)), new HashMap<String, EvolutionNode>(){{this.put("Blizzarite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_abomasnow)), null));}}));}});
p.catchRate = 60;
p.weight = 135.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.GRASS};
p.size = 2.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.SOLAR_POWER);this.add(Ability.EARLY_BIRD);}};
perName.put(ctx.getString(R.string.name_sunkern), new Pokemon(ctx.getString(R.string.name_sunkern), 191, 204, Type.GRASS, Type.NONE, abilities, 30, 30, 30, 30, 30, 30));
p = perName.get(ctx.getString(R.string.name_sunkern));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_sunkern)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierresoleil", new EvolutionNode(perName.get(ctx.getString(R.string.name_sunflora)), null));}});
p.catchRate = 235;
p.weight = 1.8f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.POISON_POINT);this.add(Ability.RIVALRY);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_nidoqueen), new Pokemon(ctx.getString(R.string.name_nidoqueen), 31, 35, Type.POISON, Type.GROUND, abilities, 90, 82, 87, 75, 85, 76));
p = perName.get(ctx.getString(R.string.name_nidoqueen));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_nidoran_f)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_nidorina)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get(ctx.getString(R.string.name_nidoqueen)), null));}}));}});
p.catchRate = 45;
p.weight = 60.0f;
p.hatch = 5120;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NATURAL_CURE);this.add(Ability.CLOUD_NINE);}};
perName.put(ctx.getString(R.string.name_altaria), new Pokemon(ctx.getString(R.string.name_altaria), 334, 357, Type.DRAGON, Type.FLYING, abilities, 75, 70, 90, 70, 105, 80));
p = perName.get(ctx.getString(R.string.name_altaria));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_swablu)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_altaria)), null));}});
p.catchRate = 45;
p.weight = 20.6f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING,EggGroup.DRAGON};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.KEEN_EYE);this.add(Ability.TANGLED_FEET);this.add(Ability.BIG_PECKS);}};
perName.put(ctx.getString(R.string.name_pidgey), new Pokemon(ctx.getString(R.string.name_pidgey), 16, 20, Type.NORMAL, Type.FLYING, abilities, 40, 45, 40, 35, 35, 56));
p = perName.get(ctx.getString(R.string.name_pidgey));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pidgey)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_pidgeotto)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_pidgeot)), null));}}));}});
p.catchRate = 255;
p.weight = 1.8f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ANTICIPATION);this.add(Ability.DRY_SKIN);this.add(Ability.POISON_TOUCH);}};
perName.put(ctx.getString(R.string.name_croagunk), new Pokemon(ctx.getString(R.string.name_croagunk), 453, 485, Type.POISON, Type.FIGHTING, abilities, 48, 61, 40, 61, 40, 50));
p = perName.get(ctx.getString(R.string.name_croagunk));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_croagunk)), new HashMap<String, EvolutionNode>(){{this.put("niveau 37", new EvolutionNode(perName.get(ctx.getString(R.string.name_toxicroak)), null));}});
p.catchRate = 140;
p.weight = 23.0f;
p.hatch = 2560;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLASH_FIRE);this.add(Ability.EARLY_BIRD);this.add(Ability.UNNERVE);}};
perName.put(ctx.getString(R.string.name_houndour), new Pokemon(ctx.getString(R.string.name_houndour), 228, 243, Type.DARK, Type.FIRE, abilities, 45, 60, 30, 80, 50, 65));
p = perName.get(ctx.getString(R.string.name_houndour));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_houndour)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "24", new EvolutionNode(perName.get(ctx.getString(R.string.name_houndoom)), new HashMap<String, EvolutionNode>(){{this.put("Demolossite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_houndoom)), null));}}));}});
p.catchRate = 120;
p.weight = 10.8f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BIG_PECKS);this.add(Ability.OVERCOAT);this.add(Ability.WEAK_ARMOR);}};
perName.put(ctx.getString(R.string.name_mandibuzz), new Pokemon(ctx.getString(R.string.name_mandibuzz), 630, 671, Type.DARK, Type.FLYING, abilities, 110, 65, 105, 55, 95, 80));
p = perName.get(ctx.getString(R.string.name_mandibuzz));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_vullaby)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "54", new EvolutionNode(perName.get(ctx.getString(R.string.name_mandibuzz)), null));}});
p.catchRate = 60;
p.weight = 39.5f;
p.hatch = 5355;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SERENE_GRACE);this.add(Ability.HUSTLE);this.add(Ability.SUPER_LUCK);}};
perName.put(ctx.getString(R.string.name_togekiss), new Pokemon(ctx.getString(R.string.name_togekiss), 468, 501, Type.NORMAL, Type.FLYING, abilities, 85, 50, 95, 120, 115, 80));
p = perName.get(ctx.getString(R.string.name_togekiss));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_togepi)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_togetic)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get(ctx.getString(R.string.name_togekiss)), null));}}));}});
p.catchRate = 30;
p.weight = 38.0f;
p.hatch = 2560;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING,EggGroup.FAIRY};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.HYDRATION);this.add(Ability.WATER_ABSORB);}};
perName.put(ctx.getString(R.string.name_tympole), new Pokemon(ctx.getString(R.string.name_tympole), 535, 575, Type.WATER, Type.NONE, abilities, 50, 50, 40, 50, 40, 64));
p = perName.get(ctx.getString(R.string.name_tympole));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tympole)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_palpitoad)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_seismitoad)), null));}}));}});
p.catchRate = 255;
p.weight = 4.5f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STENCH);this.add(Ability.AFTERMATH);}};
perName.put(ctx.getString(R.string.name_skuntank), new Pokemon(ctx.getString(R.string.name_skuntank), 435, 465, Type.POISON, Type.DARK, abilities, 103, 93, 67, 71, 61, 84));
p = perName.get(ctx.getString(R.string.name_skuntank));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_stunky)), new HashMap<String, EvolutionNode>(){{this.put("niveau 34", new EvolutionNode(perName.get(ctx.getString(R.string.name_skuntank)), null));}});
p.catchRate = 60;
p.weight = 38.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.DEFIANT);}};
perName.put(ctx.getString(R.string.name_piplup), new Pokemon(ctx.getString(R.string.name_piplup), 393, 421, Type.WATER, Type.NONE, abilities, 53, 51, 53, 61, 56, 40));
p = perName.get(ctx.getString(R.string.name_piplup));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_piplup)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_prinplup)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_empoleon)), null));}}));}});
p.catchRate = 45;
p.weight = 5.2f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OBLIVIOUS);this.add(Ability.TINTED_LENS);this.add(Ability.PRANKSTER);}};
perName.put(ctx.getString(R.string.name_illumise), new Pokemon(ctx.getString(R.string.name_illumise), 314, 337, Type.BUG, Type.NONE, abilities, 65, 47, 55, 73, 75, 85));
p = perName.get(ctx.getString(R.string.name_illumise));
p.evolutions = null;
p.catchRate = 150;
p.weight = 17.7f;
p.hatch = 3840;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG,EggGroup.HUMANLIKE};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_VEIL);}};
perName.put(ctx.getString(R.string.name_gabite), new Pokemon(ctx.getString(R.string.name_gabite), 444, 474, Type.DRAGON, Type.GROUND, abilities, 68, 90, 65, 50, 55, 82));
p = perName.get(ctx.getString(R.string.name_gabite));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_gible)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "24", new EvolutionNode(perName.get(ctx.getString(R.string.name_gabite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "48", new EvolutionNode(perName.get(ctx.getString(R.string.name_garchomp)), new HashMap<String, EvolutionNode>(){{this.put("Carchacrokite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_garchomp)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 56.0f;
p.hatch = 10240;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON,EggGroup.MONSTER};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PLUS);this.add(Ability.MINUS);this.add(Ability.CLEAR_BODY);}};
perName.put(ctx.getString(R.string.name_klinklang), new Pokemon(ctx.getString(R.string.name_klinklang), 601, 642, Type.STEEL, Type.NONE, abilities, 60, 100, 115, 70, 85, 90));
p = perName.get(ctx.getString(R.string.name_klinklang));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_klink)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "38", new EvolutionNode(perName.get(ctx.getString(R.string.name_klang)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "49", new EvolutionNode(perName.get(ctx.getString(R.string.name_klinklang)), null));}}));}});
p.catchRate = 30;
p.weight = 81.0f;
p.hatch = 5355;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);this.add(Ability.PRESSURE);this.add(Ability.TELEPATHY);}};
perName.put(ctx.getString(R.string.name_giratina_origin_forme), new Pokemon(ctx.getString(R.string.name_giratina_origin_forme), 487, 526, Type.GHOST, Type.DRAGON, abilities, 150, 120, 100, 120, 100, 90));
p = perName.get(ctx.getString(R.string.name_giratina_origin_forme));
p.evolutions = null;
p.catchRate = 3;
p.weight = 750f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 4.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.SPEED_BOOST);}};
perName.put(ctx.getString(R.string.name_torchic), new Pokemon(ctx.getString(R.string.name_torchic), 255, 272, Type.FIRE, Type.NONE, abilities, 45, 60, 40, 70, 50, 45));
p = perName.get(ctx.getString(R.string.name_torchic));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_torchic)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_combusken)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_blaziken)), new HashMap<String, EvolutionNode>(){{this.put("Brasegalite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_blaziken)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 2.5f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HYDRATION);this.add(Ability.STICKY_HOLD);this.add(Ability.UNBURDEN);}};
perName.put(ctx.getString(R.string.name_accelgor), new Pokemon(ctx.getString(R.string.name_accelgor), 617, 658, Type.BUG, Type.NONE, abilities, 80, 70, 40, 100, 60, 145));
p = perName.get(ctx.getString(R.string.name_accelgor));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_shelmet)), new HashMap<String, EvolutionNode>(){{this.put("Echange avec Carabing", new EvolutionNode(perName.get(ctx.getString(R.string.name_accelgor)), null));}});
p.catchRate = 75;
p.weight = 23.5f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.DRY_SKIN);this.add(Ability.SAND_VEIL);this.add(Ability.SOLAR_POWER);}};
perName.put(ctx.getString(R.string.name_heliolisk), new Pokemon(ctx.getString(R.string.name_heliolisk), 695, 742, Type.ELECTRIC, Type.NORMAL, abilities, 62, 55, 52, 109, 94, 109));
p = perName.get(ctx.getString(R.string.name_heliolisk));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_helioptile)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierresoleil", new EvolutionNode(perName.get(ctx.getString(R.string.name_heliolisk)), null));}});
p.catchRate = -1;
p.weight = 21.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.DRAGON};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHED_SKIN);this.add(Ability.OVERCOAT);}};
perName.put(ctx.getString(R.string.name_burmy), new Pokemon(ctx.getString(R.string.name_burmy), 412, 440, Type.BUG, Type.NONE, abilities, 40, 29, 45, 29, 45, 36));
p = perName.get(ctx.getString(R.string.name_burmy));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_burmy)), new HashMap<String, EvolutionNode>(){{this.put("Si Male, Niveau 20", new EvolutionNode(perName.get(ctx.getString(R.string.name_mothim)), null));this.put("Si Femelle, Niveau 20", new EvolutionNode(perName.get(ctx.getString(R.string.name_wormadam_plant_cloak)), null));}});
p.catchRate = 120;
p.weight = 3.4f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.TECHNICIAN);this.add(Ability.STEADFAST);}};
perName.put(ctx.getString(R.string.name_hitmontop), new Pokemon(ctx.getString(R.string.name_hitmontop), 237, 253, Type.FIGHTING, Type.NONE, abilities, 50, 95, 95, 35, 110, 70));
p = perName.get(ctx.getString(R.string.name_hitmontop));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tyrogue)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20, Attaque < Defense", new EvolutionNode(perName.get(ctx.getString(R.string.name_hitmonchan)), null));this.put(ctx.getString(R.string.level) + "20, Attaque > Defense", new EvolutionNode(perName.get(ctx.getString(R.string.name_hitmonlee)), null));this.put(ctx.getString(R.string.level) + "20, Attaque et Defense identiques", new EvolutionNode(perName.get(ctx.getString(R.string.name_hitmontop)), null));}});
p.catchRate = 45;
p.weight = 48.0f;
p.hatch = 6400;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RUN_AWAY);this.add(Ability.PICKUP);this.add(Ability.VOLT_ABSORB);}};
perName.put(ctx.getString(R.string.name_pachirisu), new Pokemon(ctx.getString(R.string.name_pachirisu), 417, 447, Type.ELECTRIC, Type.NONE, abilities, 60, 45, 70, 45, 90, 95));
p = perName.get(ctx.getString(R.string.name_pachirisu));
p.evolutions = null;
p.catchRate = 200;
p.weight = 3.9f;
p.hatch = 2560;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY,EggGroup.FIELD};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.THICK_FAT);this.add(Ability.HUGE_POWER);this.add(Ability.SAP_SIPPER);}};
perName.put(ctx.getString(R.string.name_marill), new Pokemon(ctx.getString(R.string.name_marill), 183, 196, Type.WATER, Type.NONE, abilities, 70, 20, 50, 20, 50, 40));
p = perName.get(ctx.getString(R.string.name_marill));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_azurill)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_marill)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_azumarill)), null));}}));}});
p.catchRate = 190;
p.weight = 8.5f;
p.hatch = 2560;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FAIRY};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ADAPTABILITY);}};
perName.put(ctx.getString(R.string.name_mega_lucario), new Pokemon(ctx.getString(R.string.name_mega_lucario), 448, 480, Type.STEEL, Type.FIGHTING, abilities, 70, 145, 88, 140, 70, 112));
p = perName.get(ctx.getString(R.string.name_mega_lucario));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_riolu)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur + gagne un niveau de jour", new EvolutionNode(perName.get(ctx.getString(R.string.name_lucario)), new HashMap<String, EvolutionNode>(){{this.put("Lucarite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_lucario)), null));}}));}});
p.catchRate = -1;
p.weight = 57.5f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CUTE_CHARM);this.add(Ability.NORMALIZE);}};
perName.put(ctx.getString(R.string.name_skitty), new Pokemon(ctx.getString(R.string.name_skitty), 300, 319, Type.NORMAL, Type.NONE, abilities, 50, 45, 45, 35, 35, 50));
p = perName.get(ctx.getString(R.string.name_skitty));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_skitty)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get(ctx.getString(R.string.name_delcatty)), null));}});
p.catchRate = 255;
p.weight = 11.0f;
p.hatch = 3840;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.FAIRY};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SYNCHRONIZE);this.add(Ability.INNER_FOCUS);this.add(Ability.MAGIC_GUARD);}};
perName.put(ctx.getString(R.string.name_abra), new Pokemon(ctx.getString(R.string.name_abra), 63, 67, Type.PSYCHIC, Type.NONE, abilities, 25, 20, 15, 105, 55, 90));
p = perName.get(ctx.getString(R.string.name_abra));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_abra)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_kadabra)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_alakazam)), new HashMap<String, EvolutionNode>(){{this.put("Alakazamite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_alakazam)), null));}}));}}));}});
p.catchRate = 200;
p.weight = 19.5f;
p.hatch = 5120;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEAF_GUARD);this.add(Ability.CHLOROPHYLL);this.add(Ability.OVERCOAT);}};
perName.put(ctx.getString(R.string.name_swadloon), new Pokemon(ctx.getString(R.string.name_swadloon), 541, 581, Type.BUG, Type.GRASS, abilities, 55, 63, 90, 50, 80, 42));
p = perName.get(ctx.getString(R.string.name_swadloon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_sewaddle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_swadloon)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_leavanny)), null));}}));}});
p.catchRate = 120;
p.weight = 7.3f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CUTE_CHARM);this.add(Ability.COMPETITIVE);this.add(Ability.FRISK);}};
perName.put(ctx.getString(R.string.name_wigglytuff), new Pokemon(ctx.getString(R.string.name_wigglytuff), 40, 44, Type.NORMAL, Type.NONE, abilities, 140, 70, 45, 75, 50, 45));
p = perName.get(ctx.getString(R.string.name_wigglytuff));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_igglybuff)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_jigglypuff)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get(ctx.getString(R.string.name_wigglytuff)), null));}}));}});
p.catchRate = 50;
p.weight = 12.0f;
p.hatch = 2560;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STRONG_JAW);}};
perName.put(ctx.getString(R.string.name_tyrunt), new Pokemon(ctx.getString(R.string.name_tyrunt), 696, 743, Type.ROCK, Type.DRAGON, abilities, 58, 89, 77, 45, 45, 48));
p = perName.get(ctx.getString(R.string.name_tyrunt));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tyrunt)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "39 pendant la journee", new EvolutionNode(perName.get(ctx.getString(R.string.name_tyrantrum)), null));}});
p.catchRate = -1;
p.weight = 26.0f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.COLOR_CHANGE);this.add(Ability.PROTEAN);}};
perName.put(ctx.getString(R.string.name_kecleon), new Pokemon(ctx.getString(R.string.name_kecleon), 352, 375, Type.NORMAL, Type.NONE, abilities, 60, 90, 70, 60, 120, 40));
p = perName.get(ctx.getString(R.string.name_kecleon));
p.evolutions = null;
p.catchRate = 45;
p.weight = 22.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);}};
perName.put(ctx.getString(R.string.name_deoxys_speed_forme), new Pokemon(ctx.getString(R.string.name_deoxys_speed_forme), 386, 414, Type.PSYCHIC, Type.NONE, abilities, 50, 95, 90, 95, 90, 180));
p = perName.get(ctx.getString(R.string.name_deoxys_speed_forme));
p.evolutions = null;
p.catchRate = 3;
p.weight = 60.8f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHELL_ARMOR);this.add(Ability.SKILL_LINK);this.add(Ability.OVERCOAT);}};
perName.put(ctx.getString(R.string.name_cloyster), new Pokemon(ctx.getString(R.string.name_cloyster), 91, 96, Type.WATER, Type.ICE, abilities, 50, 95, 180, 85, 45, 70));
p = perName.get(ctx.getString(R.string.name_cloyster));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_shellder)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_cloyster)), null));}});
p.catchRate = 60;
p.weight = 132.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER3};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_rotom_heat_rotom), new Pokemon(ctx.getString(R.string.name_rotom_heat_rotom), 479, 513, Type.ELECTRIC, Type.GHOST, abilities, 50, 65, 107, 105, 107, 86));
p = perName.get(ctx.getString(R.string.name_rotom_heat_rotom));
p.evolutions = null;
p.catchRate = 45;
p.weight = 0.3f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.DRY_SKIN);this.add(Ability.SAND_VEIL);this.add(Ability.SOLAR_POWER);}};
perName.put(ctx.getString(R.string.name_helioptile), new Pokemon(ctx.getString(R.string.name_helioptile), 694, 741, Type.ELECTRIC, Type.NORMAL, abilities, 44, 38, 33, 61, 43, 70));
p = perName.get(ctx.getString(R.string.name_helioptile));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_helioptile)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierresoleil", new EvolutionNode(perName.get(ctx.getString(R.string.name_heliolisk)), null));}});
p.catchRate = -1;
p.weight = 6.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.DRAGON};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HEALER);this.add(Ability.AROMA_VEIL);}};
perName.put(ctx.getString(R.string.name_spritzee), new Pokemon(ctx.getString(R.string.name_spritzee), 682, 729, Type.FAIRY, Type.NONE, abilities, 78, 52, 60, 63, 65, 23));
p = perName.get(ctx.getString(R.string.name_spritzee));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_spritzee)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Sachet Senteur", new EvolutionNode(perName.get(ctx.getString(R.string.name_aromatisse)), null));}});
p.catchRate = -1;
p.weight = 0.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY};
p.size = 0.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.SAP_SIPPER);this.add(Ability.SERENE_GRACE);}};
perName.put(ctx.getString(R.string.name_sawsbuck), new Pokemon(ctx.getString(R.string.name_sawsbuck), 586, 627, Type.NORMAL, Type.GRASS, abilities, 80, 100, 70, 60, 70, 95));
p = perName.get(ctx.getString(R.string.name_sawsbuck));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_deerling)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "34", new EvolutionNode(perName.get(ctx.getString(R.string.name_sawsbuck)), null));}});
p.catchRate = 75;
p.weight = 92.5f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);}};
perName.put(ctx.getString(R.string.name_kyurem_black_kyurem), new Pokemon(ctx.getString(R.string.name_kyurem_black_kyurem), 646, 690, Type.DRAGON, Type.ICE, abilities, 125, 170, 100, 120, 90, 95));
p = perName.get(ctx.getString(R.string.name_kyurem_black_kyurem));
p.evolutions = null;
p.catchRate = 3;
p.weight = 325f;
p.hatch = 30855;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 3.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_STREAM);this.add(Ability.SAND_FORCE);}};
perName.put(ctx.getString(R.string.name_hippopotas), new Pokemon(ctx.getString(R.string.name_hippopotas), 449, 481, Type.GROUND, Type.NONE, abilities, 68, 72, 78, 38, 42, 32));
p = perName.get(ctx.getString(R.string.name_hippopotas));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_hippopotas)), new HashMap<String, EvolutionNode>(){{this.put("niveau 34", new EvolutionNode(perName.get(ctx.getString(R.string.name_hippowdon)), null));}});
p.catchRate = 140;
p.weight = 49.5f;
p.hatch = 7680;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);this.add(Ability.PRESSURE);this.add(Ability.TELEPATHY);}};
perName.put(ctx.getString(R.string.name_giratina_altered_forme), new Pokemon(ctx.getString(R.string.name_giratina_altered_forme), 487, 525, Type.GHOST, Type.DRAGON, abilities, 150, 100, 120, 100, 120, 90));
p = perName.get(ctx.getString(R.string.name_giratina_altered_forme));
p.evolutions = null;
p.catchRate = 3;
p.weight = 750f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 4.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHED_SKIN);}};
perName.put(ctx.getString(R.string.name_kakuna), new Pokemon(ctx.getString(R.string.name_kakuna), 14, 18, Type.BUG, Type.POISON, abilities, 45, 25, 50, 25, 25, 35));
p = perName.get(ctx.getString(R.string.name_kakuna));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_weedle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "7", new EvolutionNode(perName.get(ctx.getString(R.string.name_kakuna)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "10", new EvolutionNode(perName.get(ctx.getString(R.string.name_beedrill)), null));}}));}});
p.catchRate = 120;
p.weight = 10.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.HARVEST);}};
perName.put(ctx.getString(R.string.name_exeggcute), new Pokemon(ctx.getString(R.string.name_exeggcute), 102, 108, Type.GRASS, Type.PSYCHIC, abilities, 60, 40, 80, 60, 45, 40));
p = perName.get(ctx.getString(R.string.name_exeggcute));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_exeggcute)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get(ctx.getString(R.string.name_exeggutor)), null));}});
p.catchRate = 90;
p.weight = 2.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.GLUTTONY);this.add(Ability.QUICK_FEET);}};
perName.put(ctx.getString(R.string.name_zigzagoon), new Pokemon(ctx.getString(R.string.name_zigzagoon), 263, 281, Type.NORMAL, Type.NONE, abilities, 38, 30, 41, 30, 41, 60));
p = perName.get(ctx.getString(R.string.name_zigzagoon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_zigzagoon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_linoone)), null));}});
p.catchRate = 255;
p.weight = 17.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GUTS);this.add(Ability.RUN_AWAY);this.add(Ability.HUSTLE);}};
perName.put(ctx.getString(R.string.name_rattata), new Pokemon(ctx.getString(R.string.name_rattata), 19, 23, Type.NORMAL, Type.NONE, abilities, 30, 56, 35, 25, 35, 72));
p = perName.get(ctx.getString(R.string.name_rattata));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_rattata)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_raticate)), null));}});
p.catchRate = 255;
p.weight = 3.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INNER_FOCUS);this.add(Ability.EARLY_BIRD);this.add(Ability.SAP_SIPPER);}};
perName.put(ctx.getString(R.string.name_girafarig), new Pokemon(ctx.getString(R.string.name_girafarig), 203, 216, Type.NORMAL, Type.PSYCHIC, abilities, 70, 80, 65, 90, 65, 85));
p = perName.get(ctx.getString(R.string.name_girafarig));
p.evolutions = null;
p.catchRate = 60;
p.weight = 41.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.THICK_FAT);this.add(Ability.HYDRATION);this.add(Ability.ICE_BODY);}};
perName.put(ctx.getString(R.string.name_seel), new Pokemon(ctx.getString(R.string.name_seel), 86, 91, Type.WATER, Type.NONE, abilities, 65, 45, 55, 45, 70, 45));
p = perName.get(ctx.getString(R.string.name_seel));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_seel)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "34", new EvolutionNode(perName.get(ctx.getString(R.string.name_dewgong)), null));}});
p.catchRate = 190;
p.weight = 90.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.QUICK_FEET);this.add(Ability.INTIMIDATE);this.add(Ability.RATTLED);}};
perName.put(ctx.getString(R.string.name_granbull), new Pokemon(ctx.getString(R.string.name_granbull), 210, 223, Type.NORMAL, Type.NONE, abilities, 90, 120, 75, 60, 60, 45));
p = perName.get(ctx.getString(R.string.name_granbull));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_snubbull)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "23", new EvolutionNode(perName.get(ctx.getString(R.string.name_granbull)), null));}});
p.catchRate = 75;
p.weight = 48.7f;
p.hatch = 5120;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.FAIRY};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.BATTLE_ARMOR);this.add(Ability.WEAK_ARMOR);}};
perName.put(ctx.getString(R.string.name_kabutops), new Pokemon(ctx.getString(R.string.name_kabutops), 141, 150, Type.ROCK, Type.WATER, abilities, 60, 115, 105, 65, 70, 80));
p = perName.get(ctx.getString(R.string.name_kabutops));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_kabuto)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_kabutops)), null));}});
p.catchRate = 45;
p.weight = 40.5f;
p.hatch = 7680;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER3};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RUN_AWAY);this.add(Ability.KEEN_EYE);this.add(Ability.ANALYTIC);}};
perName.put(ctx.getString(R.string.name_patrat), new Pokemon(ctx.getString(R.string.name_patrat), 504, 544, Type.NORMAL, Type.NONE, abilities, 45, 55, 39, 35, 39, 42));
p = perName.get(ctx.getString(R.string.name_patrat));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_patrat)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_watchog)), null));}});
p.catchRate = 255;
p.weight = 11.6f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ANTICIPATION);this.add(Ability.OVERCOAT);}};
perName.put(ctx.getString(R.string.name_wormadam_sandy_cloak), new Pokemon(ctx.getString(R.string.name_wormadam_sandy_cloak), 413, 442, Type.BUG, Type.NONE, abilities, 60, 79, 105, 59, 85, 36));
p = perName.get(ctx.getString(R.string.name_wormadam_sandy_cloak));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_burmy)), new HashMap<String, EvolutionNode>(){{this.put("Si Male, Niveau 20", new EvolutionNode(perName.get(ctx.getString(R.string.name_mothim)), null));this.put("Si Femelle, Niveau 20", new EvolutionNode(perName.get(ctx.getString(R.string.name_wormadam_sandy_cloak)), null));}});
p.catchRate = 45;
p.weight = 6.5f;
p.hatch = 3840;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.CHLOROPHYLL);}};
perName.put(ctx.getString(R.string.name_bulbasaur), new Pokemon(ctx.getString(R.string.name_bulbasaur), 1, 1, Type.GRASS, Type.POISON, abilities, 45, 49, 49, 65, 65, 45));
p = perName.get(ctx.getString(R.string.name_bulbasaur));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bulbasaur)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_ivysaur)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_venusaur)), new HashMap<String, EvolutionNode>(){{this.put("Florizarrite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_venusaur)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 6.9f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.GRASS};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FUR_COAT);}};
perName.put(ctx.getString(R.string.name_furfrou), new Pokemon(ctx.getString(R.string.name_furfrou), 676, 722, Type.NORMAL, Type.NONE, abilities, 75, 80, 60, 65, 90, 102));
p = perName.get(ctx.getString(R.string.name_furfrou));
p.evolutions = null;
p.catchRate = -1;
p.weight = 28.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.HUMANLIKE};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SOLAR_POWER);}};
perName.put(ctx.getString(R.string.name_mega_houndoom), new Pokemon(ctx.getString(R.string.name_mega_houndoom), 229, 245, Type.DARK, Type.FIRE, abilities, 75, 90, 90, 140, 90, 115));
p = perName.get(ctx.getString(R.string.name_mega_houndoom));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_houndour)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "24", new EvolutionNode(perName.get(ctx.getString(R.string.name_houndoom)), new HashMap<String, EvolutionNode>(){{this.put("Demolossite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_houndoom)), null));}}));}});
p.catchRate = -1;
p.weight = 35f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FRISK);this.add(Ability.SHADOW_TAG);}};
perName.put(ctx.getString(R.string.name_gothitelle), new Pokemon(ctx.getString(R.string.name_gothitelle), 576, 617, Type.PSYCHIC, Type.NONE, abilities, 70, 55, 95, 95, 110, 65));
p = perName.get(ctx.getString(R.string.name_gothitelle));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_gothita)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_gothorita)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "41", new EvolutionNode(perName.get(ctx.getString(R.string.name_gothitelle)), null));}}));}});
p.catchRate = 50;
p.weight = 44f;
p.hatch = 5355;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.CHEEK_POUCH);this.add(Ability.PLUS);}};
perName.put(ctx.getString(R.string.name_dedenne), new Pokemon(ctx.getString(R.string.name_dedenne), 702, 749, Type.ELECTRIC, Type.FAIRY, abilities, 67, 58, 57, 81, 67, 101));
p = perName.get(ctx.getString(R.string.name_dedenne));
p.evolutions = null;
p.catchRate = -1;
p.weight = 2.2f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.FAIRY};
p.size = 0.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.CHLOROPHYLL);}};
perName.put(ctx.getString(R.string.name_ivysaur), new Pokemon(ctx.getString(R.string.name_ivysaur), 2, 2, Type.GRASS, Type.POISON, abilities, 62, 62, 63, 80, 80, 60));
p = perName.get(ctx.getString(R.string.name_ivysaur));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bulbasaur)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_ivysaur)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_venusaur)), new HashMap<String, EvolutionNode>(){{this.put("Florizarrite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_venusaur)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 13.0f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.GRASS};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.RIVALRY);this.add(Ability.GUTS);}};
perName.put(ctx.getString(R.string.name_shinx), new Pokemon(ctx.getString(R.string.name_shinx), 403, 431, Type.ELECTRIC, Type.NONE, abilities, 45, 65, 34, 40, 34, 45));
p = perName.get(ctx.getString(R.string.name_shinx));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_shinx)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "15", new EvolutionNode(perName.get(ctx.getString(R.string.name_luxio)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_luxray)), null));}}));}});
p.catchRate = 235;
p.weight = 9.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.KEEN_EYE);this.add(Ability.TANGLED_FEET);this.add(Ability.BIG_PECKS);}};
perName.put(ctx.getString(R.string.name_pidgeot), new Pokemon(ctx.getString(R.string.name_pidgeot), 18, 22, Type.NORMAL, Type.FLYING, abilities, 83, 80, 75, 70, 70, 91));
p = perName.get(ctx.getString(R.string.name_pidgeot));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pidgey)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_pidgeotto)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_pidgeot)), null));}}));}});
p.catchRate = 45;
p.weight = 39.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.MAGNET_PULL);this.add(Ability.SAND_FORCE);}};
perName.put(ctx.getString(R.string.name_nosepass), new Pokemon(ctx.getString(R.string.name_nosepass), 299, 318, Type.ROCK, Type.NONE, abilities, 30, 45, 135, 45, 90, 30));
p = perName.get(ctx.getString(R.string.name_nosepass));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_nosepass)), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau dans un lieu indique", new EvolutionNode(perName.get(ctx.getString(R.string.name_probopass)), null));}});
p.catchRate = 255;
p.weight = 97.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.KEEN_EYE);this.add(Ability.SNIPER);}};
perName.put(ctx.getString(R.string.name_fearow), new Pokemon(ctx.getString(R.string.name_fearow), 22, 26, Type.NORMAL, Type.FLYING, abilities, 65, 90, 65, 61, 61, 100));
p = perName.get(ctx.getString(R.string.name_fearow));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_spearow)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_fearow)), null));}});
p.catchRate = 90;
p.weight = 38.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GUTS);}};
perName.put(ctx.getString(R.string.name_larvitar), new Pokemon(ctx.getString(R.string.name_larvitar), 246, 262, Type.ROCK, Type.GROUND, abilities, 50, 64, 50, 45, 50, 41));
p = perName.get(ctx.getString(R.string.name_larvitar));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_larvitar)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_pupitar)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "55", new EvolutionNode(perName.get(ctx.getString(R.string.name_tyranitar)), new HashMap<String, EvolutionNode>(){{this.put("Tyranocivite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_tyranitar)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 72.0f;
p.hatch = 10240;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SERENE_GRACE);this.add(Ability.HUSTLE);this.add(Ability.SUPER_LUCK);}};
perName.put(ctx.getString(R.string.name_togetic), new Pokemon(ctx.getString(R.string.name_togetic), 176, 188, Type.NORMAL, Type.FLYING, abilities, 55, 40, 85, 80, 105, 40));
p = perName.get(ctx.getString(R.string.name_togetic));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_togepi)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_togetic)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get(ctx.getString(R.string.name_togekiss)), null));}}));}});
p.catchRate = 75;
p.weight = 3.2f;
p.hatch = 2560;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING,EggGroup.FAIRY};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FILTER);}};
perName.put(ctx.getString(R.string.name_mega_aggron), new Pokemon(ctx.getString(R.string.name_mega_aggron), 306, 327, Type.STEEL, Type.NONE, abilities, 70, 140, 230, 60, 80, 50));
p = perName.get(ctx.getString(R.string.name_mega_aggron));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_aron)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_lairon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "42", new EvolutionNode(perName.get(ctx.getString(R.string.name_aggron)), new HashMap<String, EvolutionNode>(){{this.put("Galekingite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_aggron)), null));}}));}}));}});
p.catchRate = -1;
p.weight = 395f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SOUNDPROOF);this.add(Ability.SCRAPPY);}};
perName.put(ctx.getString(R.string.name_exploud), new Pokemon(ctx.getString(R.string.name_exploud), 295, 314, Type.NORMAL, Type.NONE, abilities, 104, 91, 63, 91, 63, 68));
p = perName.get(ctx.getString(R.string.name_exploud));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_whismur)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_loudred)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_exploud)), null));}}));}});
p.catchRate = 45;
p.weight = 84.0f;
p.hatch = 5120;
p.gender = 45f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.FIELD};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.WATER_ABSORB);}};
perName.put(ctx.getString(R.string.name_mantyke), new Pokemon(ctx.getString(R.string.name_mantyke), 458, 490, Type.WATER, Type.FLYING, abilities, 45, 20, 50, 60, 120, 50));
p = perName.get(ctx.getString(R.string.name_mantyke));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mantyke)), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau avec Remoraid dans l'equipe", new EvolutionNode(perName.get(ctx.getString(R.string.name_mantine)), null));}});
p.catchRate = 25;
p.weight = 65.0f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.UNAWARE);this.add(Ability.KLUTZ);this.add(Ability.SIMPLE);}};
perName.put(ctx.getString(R.string.name_swoobat), new Pokemon(ctx.getString(R.string.name_swoobat), 528, 568, Type.PSYCHIC, Type.FLYING, abilities, 67, 57, 55, 77, 55, 114));
p = perName.get(ctx.getString(R.string.name_swoobat));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_woobat)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_swoobat)), null));}});
p.catchRate = 45;
p.weight = 10.5f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.FLYING};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.CHLOROPHYLL);}};
perName.put(ctx.getString(R.string.name_venusaur), new Pokemon(ctx.getString(R.string.name_venusaur), 3, 3, Type.GRASS, Type.POISON, abilities, 80, 82, 83, 100, 100, 80));
p = perName.get(ctx.getString(R.string.name_venusaur));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bulbasaur)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_ivysaur)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_venusaur)), new HashMap<String, EvolutionNode>(){{this.put("Florizarrite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_venusaur)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 100.0f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.GRASS};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.SHELL_ARMOR);}};
perName.put(ctx.getString(R.string.name_samurott), new Pokemon(ctx.getString(R.string.name_samurott), 503, 543, Type.WATER, Type.NONE, abilities, 95, 100, 85, 108, 70, 70));
p = perName.get(ctx.getString(R.string.name_samurott));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_oshawott)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "17", new EvolutionNode(perName.get(ctx.getString(R.string.name_dewott)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_samurott)), null));}}));}});
p.catchRate = 45;
p.weight = 94.6f;
p.hatch = 5355;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.IMMUNITY);this.add(Ability.THICK_FAT);this.add(Ability.GLUTTONY);}};
perName.put(ctx.getString(R.string.name_snorlax), new Pokemon(ctx.getString(R.string.name_snorlax), 143, 153, Type.NORMAL, Type.NONE, abilities, 160, 110, 65, 65, 110, 30));
p = perName.get(ctx.getString(R.string.name_snorlax));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_munchlax)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_snorlax)), null));}});
p.catchRate = 25;
p.weight = 460.0f;
p.hatch = 10240;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 2.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);}};
perName.put(ctx.getString(R.string.name_kyurem_white_kyurem), new Pokemon(ctx.getString(R.string.name_kyurem_white_kyurem), 646, 691, Type.DRAGON, Type.ICE, abilities, 125, 120, 90, 170, 100, 95));
p = perName.get(ctx.getString(R.string.name_kyurem_white_kyurem));
p.evolutions = null;
p.catchRate = 3;
p.weight = 325f;
p.hatch = 30855;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 3.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STENCH);this.add(Ability.STICKY_HOLD);this.add(Ability.POISON_TOUCH);}};
perName.put(ctx.getString(R.string.name_muk), new Pokemon(ctx.getString(R.string.name_muk), 89, 94, Type.POISON, Type.NONE, abilities, 105, 105, 75, 65, 100, 50));
p = perName.get(ctx.getString(R.string.name_muk));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_grimer)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "38", new EvolutionNode(perName.get(ctx.getString(R.string.name_muk)), null));}});
p.catchRate = 75;
p.weight = 30.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.WATER_ABSORB);this.add(Ability.DAMP);this.add(Ability.SWIFT_SWIM);}};
perName.put(ctx.getString(R.string.name_poliwag), new Pokemon(ctx.getString(R.string.name_poliwag), 60, 64, Type.WATER, Type.NONE, abilities, 40, 50, 40, 40, 40, 90));
p = perName.get(ctx.getString(R.string.name_poliwag));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_poliwag)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_poliwhirl)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Roche Royale", new EvolutionNode(perName.get(ctx.getString(R.string.name_politoed)), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_poliwrath)), null));}}));}});
p.catchRate = 255;
p.weight = 12.4f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SYNCHRONIZE);this.add(Ability.MAGIC_BOUNCE);}};
perName.put(ctx.getString(R.string.name_espeon), new Pokemon(ctx.getString(R.string.name_espeon), 196, 209, Type.PSYCHIC, Type.NONE, abilities, 65, 65, 60, 130, 95, 110));
p = perName.get(ctx.getString(R.string.name_espeon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_eevee)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get(ctx.getString(R.string.name_jolteon)), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_leafeon)), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get(ctx.getString(R.string.name_espeon)), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get(ctx.getString(R.string.name_sylveon)), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_vaporeon)), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_glaceon)), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get(ctx.getString(R.string.name_flareon)), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_umbreon)), null));}});
p.catchRate = 45;
p.weight = 26.5f;
p.hatch = 8960;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GUTS);this.add(Ability.SHEER_FORCE);this.add(Ability.IRON_FIST);}};
perName.put(ctx.getString(R.string.name_conkeldurr), new Pokemon(ctx.getString(R.string.name_conkeldurr), 534, 574, Type.FIGHTING, Type.NONE, abilities, 105, 140, 95, 55, 65, 45));
p = perName.get(ctx.getString(R.string.name_conkeldurr));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_timburr)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_gurdurr)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_conkeldurr)), null));}}));}});
p.catchRate = 45;
p.weight = 87.0f;
p.hatch = 5355;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NATURAL_CURE);this.add(Ability.ILLUMINATE);this.add(Ability.ANALYTIC);}};
perName.put(ctx.getString(R.string.name_staryu), new Pokemon(ctx.getString(R.string.name_staryu), 120, 127, Type.WATER, Type.NONE, abilities, 30, 45, 55, 70, 55, 85));
p = perName.get(ctx.getString(R.string.name_staryu));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_staryu)), new HashMap<String, EvolutionNode>(){{this.put("Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_starmie)), null));}});
p.catchRate = 225;
p.weight = 34.5f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER3};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.DEFEATIST);}};
perName.put(ctx.getString(R.string.name_archen), new Pokemon(ctx.getString(R.string.name_archen), 566, 607, Type.ROCK, Type.FLYING, abilities, 55, 112, 45, 74, 45, 70));
p = perName.get(ctx.getString(R.string.name_archen));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_archen)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_archeops)), null));}});
p.catchRate = 45;
p.weight = 9.5f;
p.hatch = 7905;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.MOXIE);this.add(Ability.ANGER_POINT);}};
perName.put(ctx.getString(R.string.name_krookodile), new Pokemon(ctx.getString(R.string.name_krookodile), 553, 593, Type.GROUND, Type.DARK, abilities, 95, 117, 70, 65, 70, 92));
p = perName.get(ctx.getString(R.string.name_krookodile));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_sandile)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "29", new EvolutionNode(perName.get(ctx.getString(R.string.name_krokorok)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_krookodile)), null));}}));}});
p.catchRate = 45;
p.weight = 96.3f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLASH_FIRE);this.add(Ability.FLAME_BODY);}};
perName.put(ctx.getString(R.string.name_heatran), new Pokemon(ctx.getString(R.string.name_heatran), 485, 523, Type.FIRE, Type.STEEL, abilities, 91, 90, 106, 130, 106, 77));
p = perName.get(ctx.getString(R.string.name_heatran));
p.evolutions = null;
p.catchRate = 3;
p.weight = 430.0f;
p.hatch = 2560;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RUN_AWAY);this.add(Ability.FLASH_FIRE);this.add(Ability.FLAME_BODY);}};
perName.put(ctx.getString(R.string.name_ponyta), new Pokemon(ctx.getString(R.string.name_ponyta), 77, 82, Type.FIRE, Type.NONE, abilities, 50, 85, 55, 65, 65, 90));
p = perName.get(ctx.getString(R.string.name_ponyta));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_ponyta)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_rapidash)), null));}});
p.catchRate = 190;
p.weight = 30.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_azelf), new Pokemon(ctx.getString(R.string.name_azelf), 482, 520, Type.PSYCHIC, Type.NONE, abilities, 75, 125, 70, 125, 70, 115));
p = perName.get(ctx.getString(R.string.name_azelf));
p.evolutions = null;
p.catchRate = 3;
p.weight = 0.3f;
p.hatch = 20480;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.MOXIE);this.add(Ability.ANGER_POINT);}};
perName.put(ctx.getString(R.string.name_krokorok), new Pokemon(ctx.getString(R.string.name_krokorok), 552, 592, Type.GROUND, Type.DARK, abilities, 60, 82, 45, 45, 45, 74));
p = perName.get(ctx.getString(R.string.name_krokorok));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_sandile)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "29", new EvolutionNode(perName.get(ctx.getString(R.string.name_krokorok)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_krookodile)), null));}}));}});
p.catchRate = 90;
p.weight = 33.4f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.THICK_FAT);this.add(Ability.GUTS);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_hariyama), new Pokemon(ctx.getString(R.string.name_hariyama), 297, 316, Type.FIGHTING, Type.NONE, abilities, 144, 120, 60, 40, 60, 50));
p = perName.get(ctx.getString(R.string.name_hariyama));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_makuhita)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "24", new EvolutionNode(perName.get(ctx.getString(R.string.name_hariyama)), null));}});
p.catchRate = 200;
p.weight = 253.8f;
p.hatch = 5120;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 2.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHADOW_TAG);this.add(Ability.TELEPATHY);}};
perName.put(ctx.getString(R.string.name_wobbuffet), new Pokemon(ctx.getString(R.string.name_wobbuffet), 202, 215, Type.PSYCHIC, Type.NONE, abilities, 190, 33, 58, 33, 58, 33));
p = perName.get(ctx.getString(R.string.name_wobbuffet));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_wynaut)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "15", new EvolutionNode(perName.get(ctx.getString(R.string.name_wobbuffet)), null));}});
p.catchRate = 45;
p.weight = 28.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NATURAL_CURE);this.add(Ability.ILLUMINATE);this.add(Ability.ANALYTIC);}};
perName.put(ctx.getString(R.string.name_starmie), new Pokemon(ctx.getString(R.string.name_starmie), 121, 128, Type.WATER, Type.PSYCHIC, abilities, 60, 75, 85, 100, 85, 115));
p = perName.get(ctx.getString(R.string.name_starmie));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_staryu)), new HashMap<String, EvolutionNode>(){{this.put("Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_starmie)), null));}});
p.catchRate = 60;
p.weight = 80.0f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER3};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_cryogonal), new Pokemon(ctx.getString(R.string.name_cryogonal), 615, 656, Type.ICE, Type.NONE, abilities, 70, 50, 30, 95, 135, 105));
p = perName.get(ctx.getString(R.string.name_cryogonal));
p.evolutions = null;
p.catchRate = 25;
p.weight = 148.0f;
p.hatch = 6630;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OBLIVIOUS);this.add(Ability.FOREWARN);this.add(Ability.HYDRATION);}};
perName.put(ctx.getString(R.string.name_smoochum), new Pokemon(ctx.getString(R.string.name_smoochum), 238, 254, Type.ICE, Type.PSYCHIC, abilities, 45, 30, 15, 85, 65, 65));
p = perName.get(ctx.getString(R.string.name_smoochum));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_smoochum)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_jynx)), null));}});
p.catchRate = 45;
p.weight = 6.0f;
p.hatch = 6400;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.SOUNDPROOF);}};
perName.put(ctx.getString(R.string.name_bastiodon), new Pokemon(ctx.getString(R.string.name_bastiodon), 411, 439, Type.ROCK, Type.STEEL, abilities, 60, 52, 168, 47, 138, 30));
p = perName.get(ctx.getString(R.string.name_bastiodon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_shieldon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_bastiodon)), null));}});
p.catchRate = 45;
p.weight = 149.5f;
p.hatch = 7680;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHED_SKIN);this.add(Ability.FRIEND_GUARD);}};
perName.put(ctx.getString(R.string.name_spewpa), new Pokemon(ctx.getString(R.string.name_spewpa), 665, 711, Type.BUG, Type.NONE, abilities, 45, 22, 60, 37, 30, 29));
p = perName.get(ctx.getString(R.string.name_spewpa));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_scatterbug)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "9", new EvolutionNode(perName.get(ctx.getString(R.string.name_spewpa)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "12", new EvolutionNode(perName.get(ctx.getString(R.string.name_vivillon)), null));}}));}});
p.catchRate = -1;
p.weight = 8.4f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ROUGH_SKIN);}};
perName.put(ctx.getString(R.string.name_carvanha), new Pokemon(ctx.getString(R.string.name_carvanha), 318, 341, Type.WATER, Type.DARK, abilities, 45, 90, 20, 65, 20, 65));
p = perName.get(ctx.getString(R.string.name_carvanha));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_carvanha)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_sharpedo)), null));}});
p.catchRate = 225;
p.weight = 20.8f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER2};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STATIC);}};
perName.put(ctx.getString(R.string.name_ampharos), new Pokemon(ctx.getString(R.string.name_ampharos), 181, 193, Type.ELECTRIC, Type.NONE, abilities, 90, 75, 75, 115, 90, 55));
p = perName.get(ctx.getString(R.string.name_ampharos));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mareep)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "15", new EvolutionNode(perName.get(ctx.getString(R.string.name_flaaffy)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_ampharos)), new HashMap<String, EvolutionNode>(){{this.put("Pharampite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_ampharos)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 61.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.FIELD};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PURE_POWER);}};
perName.put(ctx.getString(R.string.name_mega_medicham), new Pokemon(ctx.getString(R.string.name_mega_medicham), 308, 330, Type.FIGHTING, Type.PSYCHIC, abilities, 60, 100, 85, 80, 85, 100));
p = perName.get(ctx.getString(R.string.name_mega_medicham));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_meditite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_medicham)), new HashMap<String, EvolutionNode>(){{this.put("Charminite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_medicham)), null));}}));}});
p.catchRate = -1;
p.weight = 31.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.LEAF_GUARD);this.add(Ability.REGENERATOR);}};
perName.put(ctx.getString(R.string.name_tangrowth), new Pokemon(ctx.getString(R.string.name_tangrowth), 465, 498, Type.GRASS, Type.NONE, abilities, 100, 100, 125, 110, 50, 50));
p = perName.get(ctx.getString(R.string.name_tangrowth));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tangela)), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l'attaque Pouv.Antique", new EvolutionNode(perName.get(ctx.getString(R.string.name_tangrowth)), null));}});
p.catchRate = 30;
p.weight = 128.6f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.SOLAR_POWER);this.add(Ability.EARLY_BIRD);}};
perName.put(ctx.getString(R.string.name_sunflora), new Pokemon(ctx.getString(R.string.name_sunflora), 192, 205, Type.GRASS, Type.NONE, abilities, 75, 75, 55, 105, 85, 30));
p = perName.get(ctx.getString(R.string.name_sunflora));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_sunkern)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierresoleil", new EvolutionNode(perName.get(ctx.getString(R.string.name_sunflora)), null));}});
p.catchRate = 120;
p.weight = 8.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MEGA_LAUNCHER);}};
perName.put(ctx.getString(R.string.name_clawitzer), new Pokemon(ctx.getString(R.string.name_clawitzer), 693, 740, Type.WATER, Type.NONE, abilities, 71, 73, 88, 120, 89, 59));
p = perName.get(ctx.getString(R.string.name_clawitzer));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_clauncher)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_clawitzer)), null));}});
p.catchRate = -1;
p.weight = 35.3f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER3};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_chimecho), new Pokemon(ctx.getString(R.string.name_chimecho), 358, 382, Type.PSYCHIC, Type.NONE, abilities, 65, 50, 70, 95, 80, 65));
p = perName.get(ctx.getString(R.string.name_chimecho));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_chingling)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur , Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_chimecho)), null));}});
p.catchRate = 45;
p.weight = 1.0f;
p.hatch = 6655;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LIMBER);this.add(Ability.UNBURDEN);this.add(Ability.MOLD_BREAKER);}};
perName.put(ctx.getString(R.string.name_hawlucha), new Pokemon(ctx.getString(R.string.name_hawlucha), 701, 748, Type.FIGHTING, Type.FLYING, abilities, 70, 95, 80, 65, 70, 110));
p = perName.get(ctx.getString(R.string.name_hawlucha));
p.evolutions = null;
p.catchRate = -1;
p.weight = 21.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.KEEN_EYE);this.add(Ability.SHEER_FORCE);this.add(Ability.HUSTLE);}};
perName.put(ctx.getString(R.string.name_rufflet), new Pokemon(ctx.getString(R.string.name_rufflet), 627, 668, Type.NORMAL, Type.FLYING, abilities, 70, 83, 50, 37, 50, 60));
p = perName.get(ctx.getString(R.string.name_rufflet));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_rufflet)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "54", new EvolutionNode(perName.get(ctx.getString(R.string.name_braviary)), null));}});
p.catchRate = 190;
p.weight = 10.5f;
p.hatch = 5355;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAP_SIPPER);}};
perName.put(ctx.getString(R.string.name_gogoat), new Pokemon(ctx.getString(R.string.name_gogoat), 673, 719, Type.GRASS, Type.NONE, abilities, 123, 100, 62, 97, 81, 68));
p = perName.get(ctx.getString(R.string.name_gogoat));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_skiddo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_gogoat)), null));}});
p.catchRate = -1;
p.weight = 91.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GLUTTONY);this.add(Ability.BLAZE);}};
perName.put(ctx.getString(R.string.name_simisear), new Pokemon(ctx.getString(R.string.name_simisear), 514, 554, Type.FIRE, Type.NONE, abilities, 75, 98, 63, 98, 63, 101));
p = perName.get(ctx.getString(R.string.name_simisear));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pansear)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Feu", new EvolutionNode(perName.get(ctx.getString(R.string.name_simisear)), null));}});
p.catchRate = 75;
p.weight = 28.0f;
p.hatch = 5355;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.COMPOUNDEYE);this.add(Ability.SHIELD_DUST);this.add(Ability.FRIEND_GUARD);}};
perName.put(ctx.getString(R.string.name_vivillon), new Pokemon(ctx.getString(R.string.name_vivillon), 666, 712, Type.BUG, Type.FLYING, abilities, 80, 52, 50, 90, 50, 89));
p = perName.get(ctx.getString(R.string.name_vivillon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_scatterbug)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "9", new EvolutionNode(perName.get(ctx.getString(R.string.name_spewpa)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "12", new EvolutionNode(perName.get(ctx.getString(R.string.name_vivillon)), null));}}));}});
p.catchRate = -1;
p.weight = 17.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FRISK);this.add(Ability.INFILTRATOR);this.add(Ability.TELEPATHY);}};
perName.put(ctx.getString(R.string.name_noibat), new Pokemon(ctx.getString(R.string.name_noibat), 714, 767, Type.FLYING, Type.DRAGON, abilities, 70, 60, 60, 82, 60, 97));
p = perName.get(ctx.getString(R.string.name_noibat));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_noibat)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "48", new EvolutionNode(perName.get(ctx.getString(R.string.name_noivern)), null));}});
p.catchRate = -1;
p.weight = 8.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLASH_FIRE);this.add(Ability.DROUGHT);}};
perName.put(ctx.getString(R.string.name_vulpix), new Pokemon(ctx.getString(R.string.name_vulpix), 37, 41, Type.FIRE, Type.NONE, abilities, 38, 41, 40, 50, 65, 65));
p = perName.get(ctx.getString(R.string.name_vulpix));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_vulpix)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Feu", new EvolutionNode(perName.get(ctx.getString(R.string.name_ninetales)), null));}});
p.catchRate = 190;
p.weight = 9.9f;
p.hatch = 5120;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ROCK_HEAD);this.add(Ability.STURDY);}};
perName.put(ctx.getString(R.string.name_graveler), new Pokemon(ctx.getString(R.string.name_graveler), 75, 80, Type.ROCK, Type.GROUND, abilities, 55, 95, 115, 45, 45, 35));
p = perName.get(ctx.getString(R.string.name_graveler));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_geodude)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_graveler)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_golem)), null));}}));}});
p.catchRate = 120;
p.weight = 105.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INNER_FOCUS);this.add(Ability.INFILTRATOR);}};
perName.put(ctx.getString(R.string.name_crobat), new Pokemon(ctx.getString(R.string.name_crobat), 169, 181, Type.POISON, Type.FLYING, abilities, 85, 90, 80, 70, 80, 130));
p = perName.get(ctx.getString(R.string.name_crobat));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_zubat)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "22", new EvolutionNode(perName.get(ctx.getString(R.string.name_golbat)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_crobat)), null));}}));}});
p.catchRate = 90;
p.weight = 75.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.GLUTTONY);}};
perName.put(ctx.getString(R.string.name_bellsprout), new Pokemon(ctx.getString(R.string.name_bellsprout), 69, 74, Type.GRASS, Type.POISON, abilities, 50, 75, 35, 70, 30, 40));
p = perName.get(ctx.getString(R.string.name_bellsprout));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bellsprout)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "21", new EvolutionNode(perName.get(ctx.getString(R.string.name_weepinbell)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get(ctx.getString(R.string.name_victreebel)), null));}}));}});
p.catchRate = 255;
p.weight = 4.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_rotom_wash_rotom), new Pokemon(ctx.getString(R.string.name_rotom_wash_rotom), 479, 514, Type.ELECTRIC, Type.GHOST, abilities, 50, 65, 107, 105, 107, 86));
p = perName.get(ctx.getString(R.string.name_rotom_wash_rotom));
p.evolutions = null;
p.catchRate = 45;
p.weight = 0.3f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STORM_DRAIN);}};
perName.put(ctx.getString(R.string.name_lumineon), new Pokemon(ctx.getString(R.string.name_lumineon), 457, 489, Type.WATER, Type.NONE, abilities, 69, 69, 76, 69, 86, 91));
p = perName.get(ctx.getString(R.string.name_lumineon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_finneon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "31", new EvolutionNode(perName.get(ctx.getString(R.string.name_lumineon)), null));}});
p.catchRate = 75;
p.weight = 24.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER2};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.PROTEAN);}};
perName.put(ctx.getString(R.string.name_frogadier), new Pokemon(ctx.getString(R.string.name_frogadier), 657, 703, Type.WATER, Type.NONE, abilities, 54, 63, 52, 83, 56, 97));
p = perName.get(ctx.getString(R.string.name_frogadier));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_froakie)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_frogadier)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_greninja)), null));}}));}});
p.catchRate = 45;
p.weight = 10.9f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LIGHTNINGROD);this.add(Ability.ROCK_HEAD);this.add(Ability.RECKLESS);}};
perName.put(ctx.getString(R.string.name_rhyhorn), new Pokemon(ctx.getString(R.string.name_rhyhorn), 111, 117, Type.GROUND, Type.ROCK, abilities, 80, 85, 95, 30, 30, 25));
p = perName.get(ctx.getString(R.string.name_rhyhorn));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_rhyhorn)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "42", new EvolutionNode(perName.get(ctx.getString(R.string.name_rhydon)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Protecteur", new EvolutionNode(perName.get(ctx.getString(R.string.name_rhyperior)), null));}}));}});
p.catchRate = 120;
p.weight = 115.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.MOXIE);}};
perName.put(ctx.getString(R.string.name_gyarados), new Pokemon(ctx.getString(R.string.name_gyarados), 130, 138, Type.WATER, Type.FLYING, abilities, 95, 125, 79, 60, 100, 81));
p = perName.get(ctx.getString(R.string.name_gyarados));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_magikarp)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_gyarados)), new HashMap<String, EvolutionNode>(){{this.put("Leviatorite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_gyarados)), null));}}));}});
p.catchRate = 45;
p.weight = 235.0f;
p.hatch = 1280;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER2,EggGroup.DRAGON};
p.size = 6.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.WONDER_SKIN);this.add(Ability.MAGIC_GUARD);this.add(Ability.TINTED_LENS);}};
perName.put(ctx.getString(R.string.name_sigilyph), new Pokemon(ctx.getString(R.string.name_sigilyph), 561, 602, Type.PSYCHIC, Type.FLYING, abilities, 72, 58, 80, 103, 80, 97));
p = perName.get(ctx.getString(R.string.name_sigilyph));
p.evolutions = null;
p.catchRate = 45;
p.weight = 14.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.THICK_FAT);this.add(Ability.OWN_TEMPO);}};
perName.put(ctx.getString(R.string.name_spoink), new Pokemon(ctx.getString(R.string.name_spoink), 325, 348, Type.PSYCHIC, Type.NONE, abilities, 60, 25, 35, 70, 80, 60));
p = perName.get(ctx.getString(R.string.name_spoink));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_spoink)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_grumpig)), null));}});
p.catchRate = 255;
p.weight = 30.6f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);this.add(Ability.TELEPATHY);}};
perName.put(ctx.getString(R.string.name_dialga), new Pokemon(ctx.getString(R.string.name_dialga), 483, 521, Type.STEEL, Type.DRAGON, abilities, 100, 120, 120, 150, 100, 90));
p = perName.get(ctx.getString(R.string.name_dialga));
p.evolutions = null;
p.catchRate = 30;
p.weight = 683f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 5.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_VEIL);this.add(Ability.SAND_RUSH);}};
perName.put(ctx.getString(R.string.name_sandshrew), new Pokemon(ctx.getString(R.string.name_sandshrew), 27, 31, Type.GROUND, Type.NONE, abilities, 50, 75, 85, 20, 30, 40));
p = perName.get(ctx.getString(R.string.name_sandshrew));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_sandshrew)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "22", new EvolutionNode(perName.get(ctx.getString(R.string.name_sandslash)), null));}});
p.catchRate = 255;
p.weight = 12.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LIGHTNINGROD);this.add(Ability.STATIC);}};
perName.put(ctx.getString(R.string.name_electrike), new Pokemon(ctx.getString(R.string.name_electrike), 309, 331, Type.ELECTRIC, Type.NONE, abilities, 40, 45, 40, 65, 40, 65));
p = perName.get(ctx.getString(R.string.name_electrike));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_electrike)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "26", new EvolutionNode(perName.get(ctx.getString(R.string.name_manectric)), new HashMap<String, EvolutionNode>(){{this.put("Mega-Evolution", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_manectric)), null));}}));}});
p.catchRate = 120;
p.weight = 15.2f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STATIC);this.add(Ability.LIGHTNINGROD);}};
perName.put(ctx.getString(R.string.name_pichu), new Pokemon(ctx.getString(R.string.name_pichu), 172, 184, Type.ELECTRIC, Type.NONE, abilities, 20, 40, 15, 35, 35, 60));
p = perName.get(ctx.getString(R.string.name_pichu));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pichu)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_pikachu)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get(ctx.getString(R.string.name_raichu)), null));}}));}});
p.catchRate = 190;
p.weight = 2.0f;
p.hatch = 2560;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.JUSTIFIED);}};
perName.put(ctx.getString(R.string.name_terrakion), new Pokemon(ctx.getString(R.string.name_terrakion), 639, 680, Type.ROCK, Type.FIGHTING, abilities, 91, 129, 90, 72, 90, 108));
p = perName.get(ctx.getString(R.string.name_terrakion));
p.evolutions = null;
p.catchRate = 3;
p.weight = 260f;
p.hatch = 20655;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.REFRIGERATE);}};
perName.put(ctx.getString(R.string.name_amaura), new Pokemon(ctx.getString(R.string.name_amaura), 698, 745, Type.ROCK, Type.ICE, abilities, 77, 59, 50, 67, 63, 46));
p = perName.get(ctx.getString(R.string.name_amaura));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_amaura)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "39 pendant la nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_aurorus)), null));}});
p.catchRate = 45;
p.weight = 25.2f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.WATER_VEIL);}};
perName.put(ctx.getString(R.string.name_goldeen), new Pokemon(ctx.getString(R.string.name_goldeen), 118, 125, Type.WATER, Type.NONE, abilities, 45, 67, 60, 35, 50, 63));
p = perName.get(ctx.getString(R.string.name_goldeen));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_goldeen)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "33", new EvolutionNode(perName.get(ctx.getString(R.string.name_seaking)), null));}});
p.catchRate = 225;
p.weight = 15.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER2};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLAME_BODY);this.add(Ability.VITAL_SPIRIT);}};
perName.put(ctx.getString(R.string.name_magby), new Pokemon(ctx.getString(R.string.name_magby), 240, 256, Type.FIRE, Type.NONE, abilities, 45, 75, 37, 70, 55, 83));
p = perName.get(ctx.getString(R.string.name_magby));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_magby)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_magmar)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Magmariseur", new EvolutionNode(perName.get(ctx.getString(R.string.name_magmortar)), null));}}));}});
p.catchRate = 45;
p.weight = 21.4f;
p.hatch = 6400;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRANKSTER);this.add(Ability.INFILTRATOR);this.add(Ability.CHLOROPHYLL);}};
perName.put(ctx.getString(R.string.name_whimsicott), new Pokemon(ctx.getString(R.string.name_whimsicott), 547, 587, Type.GRASS, Type.NONE, abilities, 60, 67, 85, 77, 75, 116));
p = perName.get(ctx.getString(R.string.name_whimsicott));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cottonee)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierresoleil", new EvolutionNode(perName.get(ctx.getString(R.string.name_whimsicott)), null));}});
p.catchRate = 75;
p.weight = 6.6f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS,EggGroup.FAIRY};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CUTE_CHARM);this.add(Ability.KLUTZ);this.add(Ability.LIMBER);}};
perName.put(ctx.getString(R.string.name_lopunny), new Pokemon(ctx.getString(R.string.name_lopunny), 428, 458, Type.NORMAL, Type.NONE, abilities, 65, 76, 84, 54, 96, 105));
p = perName.get(ctx.getString(R.string.name_lopunny));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_buneary)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_lopunny)), null));}});
p.catchRate = 60;
p.weight = 33.3f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.HUMANLIKE};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.VOLT_ABSORB);this.add(Ability.ILLUMINATE);this.add(Ability.WATER_ABSORB);}};
perName.put(ctx.getString(R.string.name_chinchou), new Pokemon(ctx.getString(R.string.name_chinchou), 170, 182, Type.WATER, Type.ELECTRIC, abilities, 75, 38, 38, 56, 56, 67));
p = perName.get(ctx.getString(R.string.name_chinchou));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_chinchou)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "27", new EvolutionNode(perName.get(ctx.getString(R.string.name_lanturn)), null));}});
p.catchRate = 190;
p.weight = 12.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER2};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LIGHTNINGROD);this.add(Ability.STATIC);this.add(Ability.MINUS);}};
perName.put(ctx.getString(R.string.name_manectric), new Pokemon(ctx.getString(R.string.name_manectric), 310, 332, Type.ELECTRIC, Type.NONE, abilities, 70, 75, 60, 105, 60, 105));
p = perName.get(ctx.getString(R.string.name_manectric));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_electrike)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "26", new EvolutionNode(perName.get(ctx.getString(R.string.name_manectric)), new HashMap<String, EvolutionNode>(){{this.put("Mega-Evolution", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_manectric)), null));}}));}});
p.catchRate = 45;
p.weight = 40.2f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.FRISK);this.add(Ability.INSOMNIA);}};
perName.put(ctx.getString(R.string.name_gourgeist_super_size), new Pokemon(ctx.getString(R.string.name_gourgeist_super_size), 711, 764, Type.GHOST, Type.GRASS, abilities, 85, 100, 122, 58, 75, 54));
p = perName.get(ctx.getString(R.string.name_gourgeist_super_size));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pumpkaboo_super_size)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_gourgeist_super_size)), null));}});
p.catchRate = -1;
p.weight = 9.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.JUSTIFIED);}};
perName.put(ctx.getString(R.string.name_keldeo), new Pokemon(ctx.getString(R.string.name_keldeo), 647, 692, Type.WATER, Type.FIGHTING, abilities, 91, 72, 90, 129, 90, 108));
p = perName.get(ctx.getString(R.string.name_keldeo));
p.evolutions = null;
p.catchRate = 3;
p.weight = 48.5f;
p.hatch = 20655;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.UNBURDEN);}};
perName.put(ctx.getString(R.string.name_sceptile), new Pokemon(ctx.getString(R.string.name_sceptile), 254, 271, Type.GRASS, Type.NONE, abilities, 70, 85, 65, 105, 85, 120));
p = perName.get(ctx.getString(R.string.name_sceptile));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_treecko)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_grovyle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_sceptile)), null));}}));}});
p.catchRate = 45;
p.weight = 52.2f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(3, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.DRAGON};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRANKSTER);this.add(Ability.DEFIANT);}};
perName.put(ctx.getString(R.string.name_tornadus_incarnate_forme), new Pokemon(ctx.getString(R.string.name_tornadus_incarnate_forme), 641, 682, Type.FLYING, Type.NONE, abilities, 79, 115, 70, 125, 80, 111));
p = perName.get(ctx.getString(R.string.name_tornadus_incarnate_forme));
p.evolutions = null;
p.catchRate = 3;
p.weight = 63.0f;
p.hatch = 30855;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CLEAR_BODY);this.add(Ability.LIGHT_METAL);}};
perName.put(ctx.getString(R.string.name_registeel), new Pokemon(ctx.getString(R.string.name_registeel), 379, 404, Type.STEEL, Type.NONE, abilities, 80, 75, 150, 75, 150, 50));
p = perName.get(ctx.getString(R.string.name_registeel));
p.evolutions = null;
p.catchRate = 3;
p.weight = 205.0f;
p.hatch = 20480;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SYNCHRONIZE);this.add(Ability.EARLY_BIRD);this.add(Ability.MAGIC_BOUNCE);}};
perName.put(ctx.getString(R.string.name_xatu), new Pokemon(ctx.getString(R.string.name_xatu), 178, 190, Type.PSYCHIC, Type.FLYING, abilities, 65, 75, 70, 95, 70, 95));
p = perName.get(ctx.getString(R.string.name_xatu));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_natu)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_xatu)), null));}});
p.catchRate = 75;
p.weight = 15.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_duskull), new Pokemon(ctx.getString(R.string.name_duskull), 355, 379, Type.GHOST, Type.NONE, abilities, 20, 40, 90, 30, 90, 25));
p = perName.get(ctx.getString(R.string.name_duskull));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_duskull)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_dusclops)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Tissu Fauche", new EvolutionNode(perName.get(ctx.getString(R.string.name_dusknoir)), null));}}));}});
p.catchRate = 190;
p.weight = 15.0f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.KEEN_EYE);}};
perName.put(ctx.getString(R.string.name_starly), new Pokemon(ctx.getString(R.string.name_starly), 396, 424, Type.NORMAL, Type.FLYING, abilities, 40, 55, 30, 30, 30, 60));
p = perName.get(ctx.getString(R.string.name_starly));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_starly)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "14", new EvolutionNode(perName.get(ctx.getString(R.string.name_staravia)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "34", new EvolutionNode(perName.get(ctx.getString(R.string.name_staraptor)), null));}}));}});
p.catchRate = 255;
p.weight = 2.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHIELD_DUST);this.add(Ability.TINTED_LENS);}};
perName.put(ctx.getString(R.string.name_venomoth), new Pokemon(ctx.getString(R.string.name_venomoth), 49, 53, Type.BUG, Type.POISON, abilities, 70, 65, 60, 90, 75, 90));
p = perName.get(ctx.getString(R.string.name_venomoth));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_venonat)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "31", new EvolutionNode(perName.get(ctx.getString(R.string.name_venomoth)), null));}});
p.catchRate = 75;
p.weight = 12.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.RAIN_DISH);}};
perName.put(ctx.getString(R.string.name_blastoise), new Pokemon(ctx.getString(R.string.name_blastoise), 9, 12, Type.WATER, Type.NONE, abilities, 79, 83, 100, 85, 105, 78));
p = perName.get(ctx.getString(R.string.name_blastoise));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_squirtle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_wartortle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_blastoise)), new HashMap<String, EvolutionNode>(){{this.put("Tortankite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_blastoise)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 85.5f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.MONSTER};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TECHNICIAN);}};
perName.put(ctx.getString(R.string.name_mega_scizor), new Pokemon(ctx.getString(R.string.name_mega_scizor), 212, 226, Type.BUG, Type.STEEL, abilities, 70, 150, 140, 65, 100, 75));
p = perName.get(ctx.getString(R.string.name_mega_scizor));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_scyther)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Peau Metal", new EvolutionNode(perName.get(ctx.getString(R.string.name_scizor)), new HashMap<String, EvolutionNode>(){{this.put("Cizayoxite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_scizor)), null));}}));}});
p.catchRate = -1;
p.weight = 125f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHED_SKIN);this.add(Ability.MARVEL_SCALE);}};
perName.put(ctx.getString(R.string.name_dratini), new Pokemon(ctx.getString(R.string.name_dratini), 147, 157, Type.DRAGON, Type.NONE, abilities, 41, 64, 45, 50, 50, 50));
p = perName.get(ctx.getString(R.string.name_dratini));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_dratini)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_dragonair)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "55", new EvolutionNode(perName.get(ctx.getString(R.string.name_dragonite)), null));}}));}});
p.catchRate = 45;
p.weight = 3.3f;
p.hatch = 10240;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON,EggGroup.WATER1};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_hydreigon), new Pokemon(ctx.getString(R.string.name_hydreigon), 635, 676, Type.DARK, Type.DRAGON, abilities, 92, 105, 90, 125, 90, 98));
p = perName.get(ctx.getString(R.string.name_hydreigon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_deino)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "50", new EvolutionNode(perName.get(ctx.getString(R.string.name_zweilous)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "64", new EvolutionNode(perName.get(ctx.getString(R.string.name_hydreigon)), null));}}));}});
p.catchRate = 30;
p.weight = 160.0f;
p.hatch = 10455;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CUTE_CHARM);this.add(Ability.MAGIC_GUARD);this.add(Ability.FRIEND_GUARD);}};
perName.put(ctx.getString(R.string.name_clefairy), new Pokemon(ctx.getString(R.string.name_clefairy), 35, 39, Type.NORMAL, Type.NONE, abilities, 70, 45, 48, 60, 65, 35));
p = perName.get(ctx.getString(R.string.name_clefairy));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cleffa)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_clefairy)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get(ctx.getString(R.string.name_clefable)), null));}}));}});
p.catchRate = 150;
p.weight = 7.5f;
p.hatch = 2560;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.SHELL_ARMOR);this.add(Ability.WEAK_ARMOR);}};
perName.put(ctx.getString(R.string.name_dwebble), new Pokemon(ctx.getString(R.string.name_dwebble), 557, 598, Type.BUG, Type.ROCK, abilities, 50, 65, 85, 35, 35, 55));
p = perName.get(ctx.getString(R.string.name_dwebble));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_dwebble)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "34", new EvolutionNode(perName.get(ctx.getString(R.string.name_crustle)), null));}});
p.catchRate = 190;
p.weight = 14.5f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG,EggGroup.MINERAL};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.SHELL_ARMOR);}};
perName.put(ctx.getString(R.string.name_torterra), new Pokemon(ctx.getString(R.string.name_torterra), 389, 417, Type.GRASS, Type.GROUND, abilities, 95, 109, 105, 75, 85, 56));
p = perName.get(ctx.getString(R.string.name_torterra));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_turtwig)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_grotle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_torterra)), null));}}));}});
p.catchRate = 45;
p.weight = 310.0f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.GRASS};
p.size = 2.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_RUSH);this.add(Ability.SAND_FORCE);this.add(Ability.MOLD_BREAKER);}};
perName.put(ctx.getString(R.string.name_drilbur), new Pokemon(ctx.getString(R.string.name_drilbur), 529, 569, Type.GROUND, Type.NONE, abilities, 60, 85, 40, 30, 45, 68));
p = perName.get(ctx.getString(R.string.name_drilbur));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_drilbur)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "31", new EvolutionNode(perName.get(ctx.getString(R.string.name_excadrill)), null));}});
p.catchRate = 120;
p.weight = 8.5f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);}};
perName.put(ctx.getString(R.string.name_cherubi), new Pokemon(ctx.getString(R.string.name_cherubi), 420, 450, Type.GRASS, Type.NONE, abilities, 45, 35, 45, 62, 53, 35));
p = perName.get(ctx.getString(R.string.name_cherubi));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cherubi)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_cherrim)), null));}});
p.catchRate = 190;
p.weight = 3.3f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY,EggGroup.GRASS};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SIMPLE);this.add(Ability.UNAWARE);this.add(Ability.MOODY);}};
perName.put(ctx.getString(R.string.name_bidoof), new Pokemon(ctx.getString(R.string.name_bidoof), 399, 427, Type.NORMAL, Type.NONE, abilities, 59, 45, 40, 35, 40, 31));
p = perName.get(ctx.getString(R.string.name_bidoof));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bidoof)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "15", new EvolutionNode(perName.get(ctx.getString(R.string.name_bibarel)), null));}});
p.catchRate = 255;
p.weight = 20.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.POISON_POINT);this.add(Ability.RIVALRY);this.add(Ability.HUSTLE);}};
perName.put(ctx.getString(R.string.name_nidoran_f), new Pokemon(ctx.getString(R.string.name_nidoran_f), 29, 33, Type.POISON, Type.NONE, abilities, 55, 47, 52, 40, 40, 41));
p = perName.get(ctx.getString(R.string.name_nidoran_f));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_nidoran_f)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_nidorina)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get(ctx.getString(R.string.name_nidoqueen)), null));}}));}});
p.catchRate = 235;
p.weight = 7.0f;
p.hatch = 5120;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.FIELD};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.UNNERVE);this.add(Ability.RIVALRY);this.add(Ability.MOXIE);}};
perName.put(ctx.getString(R.string.name_litleo), new Pokemon(ctx.getString(R.string.name_litleo), 667, 713, Type.FIRE, Type.NORMAL, abilities, 62, 50, 58, 73, 54, 72));
p = perName.get(ctx.getString(R.string.name_litleo));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_litleo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_pyroar)), null));}});
p.catchRate = -1;
p.weight = 13.5f;
p.hatch = -1;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);this.add(Ability.FLASH_FIRE);}};
perName.put(ctx.getString(R.string.name_entei), new Pokemon(ctx.getString(R.string.name_entei), 244, 260, Type.FIRE, Type.NONE, abilities, 115, 115, 85, 90, 75, 100));
p = perName.get(ctx.getString(R.string.name_entei));
p.evolutions = null;
p.catchRate = 3;
p.weight = 198.0f;
p.hatch = 20480;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.POISON_POINT);this.add(Ability.RIVALRY);this.add(Ability.HUSTLE);}};
perName.put(ctx.getString(R.string.name_nidoran_m), new Pokemon(ctx.getString(R.string.name_nidoran_m), 32, 36, Type.POISON, Type.NONE, abilities, 46, 57, 40, 40, 40, 50));
p = perName.get(ctx.getString(R.string.name_nidoran_m));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_nidoran_m)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_nidorino)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get(ctx.getString(R.string.name_nidoking)), null));}}));}});
p.catchRate = 235;
p.weight = 9.0f;
p.hatch = 5120;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.FIELD};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.SHELL_ARMOR);}};
perName.put(ctx.getString(R.string.name_oshawott), new Pokemon(ctx.getString(R.string.name_oshawott), 501, 541, Type.WATER, Type.NONE, abilities, 55, 55, 45, 63, 45, 45));
p = perName.get(ctx.getString(R.string.name_oshawott));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_oshawott)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "17", new EvolutionNode(perName.get(ctx.getString(R.string.name_dewott)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_samurott)), null));}}));}});
p.catchRate = 45;
p.weight = 5.9f;
p.hatch = 5355;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.COMPOUNDEYE);this.add(Ability.UNNERVE);this.add(Ability.SWARM);}};
perName.put(ctx.getString(R.string.name_galvantula), new Pokemon(ctx.getString(R.string.name_galvantula), 596, 637, Type.BUG, Type.ELECTRIC, abilities, 70, 77, 60, 97, 60, 108));
p = perName.get(ctx.getString(R.string.name_galvantula));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_joltik)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_galvantula)), null));}});
p.catchRate = 75;
p.weight = 14.3f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INSOMNIA);this.add(Ability.FOREWARN);this.add(Ability.INNER_FOCUS);}};
perName.put(ctx.getString(R.string.name_drowzee), new Pokemon(ctx.getString(R.string.name_drowzee), 96, 102, Type.PSYCHIC, Type.NONE, abilities, 60, 48, 45, 43, 90, 42));
p = perName.get(ctx.getString(R.string.name_drowzee));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_drowzee)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "26", new EvolutionNode(perName.get(ctx.getString(R.string.name_hypno)), null));}});
p.catchRate = 190;
p.weight = 32.4f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NO_GUARD);}};
perName.put(ctx.getString(R.string.name_doublade), new Pokemon(ctx.getString(R.string.name_doublade), 680, 726, Type.STEEL, Type.GHOST, abilities, 59, 110, 150, 45, 49, 35));
p = perName.get(ctx.getString(R.string.name_doublade));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_honedge)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_doublade)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_aegislash_blade_forme)), null));}}));}});
p.catchRate = -1;
p.weight = 4.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INNER_FOCUS);this.add(Ability.STEADFAST);this.add(Ability.PRANKSTER);}};
perName.put(ctx.getString(R.string.name_riolu), new Pokemon(ctx.getString(R.string.name_riolu), 447, 478, Type.FIGHTING, Type.NONE, abilities, 40, 70, 40, 35, 40, 60));
p = perName.get(ctx.getString(R.string.name_riolu));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_riolu)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur + gagne un niveau de jour", new EvolutionNode(perName.get(ctx.getString(R.string.name_lucario)), new HashMap<String, EvolutionNode>(){{this.put("Lucarite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_lucario)), null));}}));}});
p.catchRate = 75;
p.weight = 20.2f;
p.hatch = 6400;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHIELD_DUST);this.add(Ability.RUN_AWAY);}};
perName.put(ctx.getString(R.string.name_weedle), new Pokemon(ctx.getString(R.string.name_weedle), 13, 17, Type.BUG, Type.POISON, abilities, 40, 35, 30, 20, 20, 50));
p = perName.get(ctx.getString(R.string.name_weedle));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_weedle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "7", new EvolutionNode(perName.get(ctx.getString(R.string.name_kakuna)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "10", new EvolutionNode(perName.get(ctx.getString(R.string.name_beedrill)), null));}}));}});
p.catchRate = 255;
p.weight = 3.2f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SNOW_CLOAK);}};
perName.put(ctx.getString(R.string.name_swinub), new Pokemon(ctx.getString(R.string.name_swinub), 220, 235, Type.ICE, Type.GROUND, abilities, 50, 50, 40, 30, 30, 50));
p = perName.get(ctx.getString(R.string.name_swinub));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_swinub)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "33", new EvolutionNode(perName.get(ctx.getString(R.string.name_piloswine)), new HashMap<String, EvolutionNode>(){{this.put("En connaissant l'attaque Pouv.Antique", new EvolutionNode(perName.get(ctx.getString(R.string.name_mamoswine)), null));}}));}});
p.catchRate = 225;
p.weight = 6.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HYPER_CUTTER);this.add(Ability.INTIMIDATE);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_mawile), new Pokemon(ctx.getString(R.string.name_mawile), 303, 322, Type.STEEL, Type.NONE, abilities, 50, 85, 85, 55, 55, 50));
p = perName.get(ctx.getString(R.string.name_mawile));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mawile)), new HashMap<String, EvolutionNode>(){{this.put("Mysdibulite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_mawile)), null));}});
p.catchRate = 45;
p.weight = 11.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.FAIRY};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.WHITE_SMOKE);this.add(Ability.SHELL_ARMOR);}};
perName.put(ctx.getString(R.string.name_torkoal), new Pokemon(ctx.getString(R.string.name_torkoal), 324, 347, Type.FIRE, Type.NONE, abilities, 70, 85, 140, 85, 70, 20));
p = perName.get(ctx.getString(R.string.name_torkoal));
p.evolutions = null;
p.catchRate = 90;
p.weight = 80.4f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_RUSH);this.add(Ability.SAND_FORCE);this.add(Ability.MOLD_BREAKER);}};
perName.put(ctx.getString(R.string.name_excadrill), new Pokemon(ctx.getString(R.string.name_excadrill), 530, 570, Type.GROUND, Type.STEEL, abilities, 110, 135, 60, 50, 65, 88));
p = perName.get(ctx.getString(R.string.name_excadrill));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_drilbur)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "31", new EvolutionNode(perName.get(ctx.getString(R.string.name_excadrill)), null));}});
p.catchRate = 60;
p.weight = 40.4f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.UNNERVE);}};
perName.put(ctx.getString(R.string.name_masquerain), new Pokemon(ctx.getString(R.string.name_masquerain), 284, 303, Type.BUG, Type.FLYING, abilities, 70, 60, 62, 80, 82, 60));
p = perName.get(ctx.getString(R.string.name_masquerain));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_surskit)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "22", new EvolutionNode(perName.get(ctx.getString(R.string.name_masquerain)), null));}});
p.catchRate = 75;
p.weight = 3.6f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.BUG};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SPEED_BOOST);this.add(Ability.TINTED_LENS);this.add(Ability.FRISK);}};
perName.put(ctx.getString(R.string.name_yanmega), new Pokemon(ctx.getString(R.string.name_yanmega), 469, 502, Type.BUG, Type.FLYING, abilities, 86, 76, 86, 116, 56, 95));
p = perName.get(ctx.getString(R.string.name_yanmega));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_yanma)), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l'attaque Pouv.Antique", new EvolutionNode(perName.get(ctx.getString(R.string.name_yanmega)), null));}});
p.catchRate = 30;
p.weight = 51.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWARM);this.add(Ability.TECHNICIAN);}};
perName.put(ctx.getString(R.string.name_kricketune), new Pokemon(ctx.getString(R.string.name_kricketune), 402, 430, Type.BUG, Type.NONE, abilities, 77, 85, 51, 55, 51, 65));
p = perName.get(ctx.getString(R.string.name_kricketune));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_kricketot)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "10", new EvolutionNode(perName.get(ctx.getString(R.string.name_kricketune)), null));}});
p.catchRate = 45;
p.weight = 25.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.POISON_POINT);this.add(Ability.SWARM);this.add(Ability.SPEED_BOOST);}};
perName.put(ctx.getString(R.string.name_whirlipede), new Pokemon(ctx.getString(R.string.name_whirlipede), 544, 584, Type.BUG, Type.POISON, abilities, 40, 55, 99, 40, 79, 47));
p = perName.get(ctx.getString(R.string.name_whirlipede));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_venipede)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "22", new EvolutionNode(perName.get(ctx.getString(R.string.name_whirlipede)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_scolipede)), null));}}));}});
p.catchRate = 120;
p.weight = 58.5f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.UNBURDEN);}};
perName.put(ctx.getString(R.string.name_grovyle), new Pokemon(ctx.getString(R.string.name_grovyle), 253, 270, Type.GRASS, Type.NONE, abilities, 50, 65, 45, 85, 65, 95));
p = perName.get(ctx.getString(R.string.name_grovyle));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_treecko)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_grovyle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_sceptile)), null));}}));}});
p.catchRate = 45;
p.weight = 21.6f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.DRAGON};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.SPEED_BOOST);}};
perName.put(ctx.getString(R.string.name_blaziken), new Pokemon(ctx.getString(R.string.name_blaziken), 257, 274, Type.FIRE, Type.FIGHTING, abilities, 80, 120, 70, 110, 70, 80));
p = perName.get(ctx.getString(R.string.name_blaziken));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_torchic)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_combusken)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_blaziken)), new HashMap<String, EvolutionNode>(){{this.put("Brasegalite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_blaziken)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 52.0f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SUCTION_CUPS);this.add(Ability.CONTRARY);}};
perName.put(ctx.getString(R.string.name_malamar), new Pokemon(ctx.getString(R.string.name_malamar), 687, 734, Type.DARK, Type.PSYCHIC, abilities, 86, 92, 88, 68, 73, 75));
p = perName.get(ctx.getString(R.string.name_malamar));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_inkay)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30, en retournant la 3DS", new EvolutionNode(perName.get(ctx.getString(R.string.name_malamar)), null));}});
p.catchRate = -1;
p.weight = 47.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER2};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BIG_PECKS);this.add(Ability.OVERCOAT);this.add(Ability.WEAK_ARMOR);}};
perName.put(ctx.getString(R.string.name_vullaby), new Pokemon(ctx.getString(R.string.name_vullaby), 629, 670, Type.DARK, Type.FLYING, abilities, 70, 55, 75, 45, 65, 60));
p = perName.get(ctx.getString(R.string.name_vullaby));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_vullaby)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "54", new EvolutionNode(perName.get(ctx.getString(R.string.name_mandibuzz)), null));}});
p.catchRate = 190;
p.weight = 9.0f;
p.hatch = 5355;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ROCK_HEAD);this.add(Ability.LIGHTNINGROD);this.add(Ability.BATTLE_ARMOR);}};
perName.put(ctx.getString(R.string.name_marowak), new Pokemon(ctx.getString(R.string.name_marowak), 105, 111, Type.GROUND, Type.NONE, abilities, 60, 80, 110, 50, 80, 45));
p = perName.get(ctx.getString(R.string.name_marowak));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cubone)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "28", new EvolutionNode(perName.get(ctx.getString(R.string.name_marowak)), null));}});
p.catchRate = 75;
p.weight = 45.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAP_SIPPER);}};
perName.put(ctx.getString(R.string.name_skiddo), new Pokemon(ctx.getString(R.string.name_skiddo), 672, 718, Type.GRASS, Type.NONE, abilities, 66, 65, 48, 62, 57, 52));
p = perName.get(ctx.getString(R.string.name_skiddo));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_skiddo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_gogoat)), null));}});
p.catchRate = -1;
p.weight = 31.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.RAIN_DISH);}};
perName.put(ctx.getString(R.string.name_lombre), new Pokemon(ctx.getString(R.string.name_lombre), 271, 289, Type.WATER, Type.GRASS, abilities, 60, 50, 50, 60, 70, 50));
p = perName.get(ctx.getString(R.string.name_lombre));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_lotad)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "14", new EvolutionNode(perName.get(ctx.getString(R.string.name_lombre)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_ludicolo)), null));}}));}});
p.catchRate = 120;
p.weight = 32.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.GRASS};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HONEY_GATHER);this.add(Ability.HUSTLE);}};
perName.put(ctx.getString(R.string.name_combee), new Pokemon(ctx.getString(R.string.name_combee), 415, 445, Type.BUG, Type.FLYING, abilities, 30, 30, 42, 30, 42, 70));
p = perName.get(ctx.getString(R.string.name_combee));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_combee)), new HashMap<String, EvolutionNode>(){{this.put("Si Femelle, Niveau 21", new EvolutionNode(perName.get(ctx.getString(R.string.name_vespiquen)), null));}});
p.catchRate = 120;
p.weight = 5.5f;
p.hatch = 3840;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GUTS);this.add(Ability.SCRAPPY);}};
perName.put(ctx.getString(R.string.name_taillow), new Pokemon(ctx.getString(R.string.name_taillow), 276, 294, Type.NORMAL, Type.FLYING, abilities, 40, 55, 30, 30, 30, 85));
p = perName.get(ctx.getString(R.string.name_taillow));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_taillow)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "22", new EvolutionNode(perName.get(ctx.getString(R.string.name_swellow)), null));}});
p.catchRate = 200;
p.weight = 2.3f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CUTE_CHARM);this.add(Ability.TECHNICIAN);this.add(Ability.SKILL_LINK);}};
perName.put(ctx.getString(R.string.name_minccino), new Pokemon(ctx.getString(R.string.name_minccino), 572, 613, Type.NORMAL, Type.NONE, abilities, 55, 50, 40, 40, 40, 75));
p = perName.get(ctx.getString(R.string.name_minccino));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_minccino)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get(ctx.getString(R.string.name_cinccino)), null));}});
p.catchRate = 255;
p.weight = 5.8f;
p.hatch = 4080;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MULTITYPE);}};
perName.put(ctx.getString(R.string.name_arceus), new Pokemon(ctx.getString(R.string.name_arceus), 493, 533, Type.NORMAL, Type.NONE, abilities, 120, 120, 120, 120, 120, 120));
p = perName.get(ctx.getString(R.string.name_arceus));
p.evolutions = null;
p.catchRate = 3;
p.weight = 320.0f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 3.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TOUGH_CLAWS);}};
perName.put(ctx.getString(R.string.name_mega_aerodactyl), new Pokemon(ctx.getString(R.string.name_mega_aerodactyl), 142, 152, Type.ROCK, Type.FLYING, abilities, 80, 135, 85, 70, 95, 150));
p = perName.get(ctx.getString(R.string.name_mega_aerodactyl));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_aerodactyl)), new HashMap<String, EvolutionNode>(){{this.put("Mega", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_aerodactyl)), null));}});
p.catchRate = -1;
p.weight = 79.0f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SYNCHRONIZE);this.add(Ability.INNER_FOCUS);this.add(Ability.MAGIC_GUARD);}};
perName.put(ctx.getString(R.string.name_kadabra), new Pokemon(ctx.getString(R.string.name_kadabra), 64, 68, Type.PSYCHIC, Type.NONE, abilities, 40, 35, 30, 120, 70, 105));
p = perName.get(ctx.getString(R.string.name_kadabra));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_abra)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_kadabra)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_alakazam)), new HashMap<String, EvolutionNode>(){{this.put("Alakazamite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_alakazam)), null));}}));}}));}});
p.catchRate = 100;
p.weight = 56.5f;
p.hatch = 5120;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CLEAR_BODY);this.add(Ability.STURDY);}};
perName.put(ctx.getString(R.string.name_regirock), new Pokemon(ctx.getString(R.string.name_regirock), 377, 402, Type.ROCK, Type.NONE, abilities, 80, 100, 200, 50, 100, 50));
p = perName.get(ctx.getString(R.string.name_regirock));
p.evolutions = null;
p.catchRate = 3;
p.weight = 230.0f;
p.hatch = 20480;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);}};
perName.put(ctx.getString(R.string.name_deoxys_attack_forme), new Pokemon(ctx.getString(R.string.name_deoxys_attack_forme), 386, 412, Type.PSYCHIC, Type.NONE, abilities, 50, 180, 20, 180, 20, 150));
p = perName.get(ctx.getString(R.string.name_deoxys_attack_forme));
p.evolutions = null;
p.catchRate = 3;
p.weight = 60.8f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.WATER_ABSORB);this.add(Ability.DAMP);this.add(Ability.DRIZZLE);}};
perName.put(ctx.getString(R.string.name_politoed), new Pokemon(ctx.getString(R.string.name_politoed), 186, 199, Type.WATER, Type.NONE, abilities, 90, 75, 75, 90, 100, 70));
p = perName.get(ctx.getString(R.string.name_politoed));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_poliwag)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_poliwhirl)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Roche Royale", new EvolutionNode(perName.get(ctx.getString(R.string.name_politoed)), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_poliwrath)), null));}}));}});
p.catchRate = 45;
p.weight = 33.9f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.CHEEK_POUCH);this.add(Ability.HUGE_POWER);}};
perName.put(ctx.getString(R.string.name_bunnelby), new Pokemon(ctx.getString(R.string.name_bunnelby), 659, 705, Type.NORMAL, Type.NONE, abilities, 38, 36, 38, 32, 36, 57));
p = perName.get(ctx.getString(R.string.name_bunnelby));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bunnelby)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_diggersby)), null));}});
p.catchRate = -1;
p.weight = 5.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_VEIL);this.add(Ability.WATER_ABSORB);}};
perName.put(ctx.getString(R.string.name_cacturne), new Pokemon(ctx.getString(R.string.name_cacturne), 332, 355, Type.GRASS, Type.DARK, abilities, 70, 115, 60, 115, 60, 55));
p = perName.get(ctx.getString(R.string.name_cacturne));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cacnea)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_cacturne)), null));}});
p.catchRate = 60;
p.weight = 77.4f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS,EggGroup.HUMANLIKE};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STATIC);this.add(Ability.LIGHTNINGROD);}};
perName.put(ctx.getString(R.string.name_raichu), new Pokemon(ctx.getString(R.string.name_raichu), 26, 30, Type.ELECTRIC, Type.NONE, abilities, 60, 90, 55, 90, 80, 100));
p = perName.get(ctx.getString(R.string.name_raichu));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pichu)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_pikachu)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get(ctx.getString(R.string.name_raichu)), null));}}));}});
p.catchRate = 75;
p.weight = 30.0f;
p.hatch = 2560;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.FAIRY};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.WATER_VEIL);this.add(Ability.LIGHTNINGROD);}};
perName.put(ctx.getString(R.string.name_seaking), new Pokemon(ctx.getString(R.string.name_seaking), 119, 126, Type.WATER, Type.NONE, abilities, 80, 92, 65, 65, 80, 68));
p = perName.get(ctx.getString(R.string.name_seaking));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_goldeen)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "33", new EvolutionNode(perName.get(ctx.getString(R.string.name_seaking)), null));}});
p.catchRate = 60;
p.weight = 39.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER2};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_vibrava), new Pokemon(ctx.getString(R.string.name_vibrava), 329, 352, Type.GROUND, Type.DRAGON, abilities, 50, 70, 50, 50, 50, 70));
p = perName.get(ctx.getString(R.string.name_vibrava));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_trapinch)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_vibrava)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "45", new EvolutionNode(perName.get(ctx.getString(R.string.name_flygon)), null));}}));}});
p.catchRate = 120;
p.weight = 15.3f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SUCTION_CUPS);this.add(Ability.STORM_DRAIN);}};
perName.put(ctx.getString(R.string.name_cradily), new Pokemon(ctx.getString(R.string.name_cradily), 346, 369, Type.ROCK, Type.GRASS, abilities, 86, 81, 97, 81, 107, 43));
p = perName.get(ctx.getString(R.string.name_cradily));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_lileep)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_cradily)), null));}});
p.catchRate = 45;
p.weight = 60.4f;
p.hatch = 7680;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER3};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.SAP_SIPPER);this.add(Ability.SERENE_GRACE);}};
perName.put(ctx.getString(R.string.name_deerling), new Pokemon(ctx.getString(R.string.name_deerling), 585, 626, Type.NORMAL, Type.GRASS, abilities, 60, 60, 50, 40, 50, 75));
p = perName.get(ctx.getString(R.string.name_deerling));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_deerling)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "34", new EvolutionNode(perName.get(ctx.getString(R.string.name_sawsbuck)), null));}});
p.catchRate = 190;
p.weight = 19.5f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STENCH);this.add(Ability.STICKY_HOLD);this.add(Ability.POISON_TOUCH);}};
perName.put(ctx.getString(R.string.name_grimer), new Pokemon(ctx.getString(R.string.name_grimer), 88, 93, Type.POISON, Type.NONE, abilities, 80, 80, 50, 40, 50, 25));
p = perName.get(ctx.getString(R.string.name_grimer));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_grimer)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "38", new EvolutionNode(perName.get(ctx.getString(R.string.name_muk)), null));}});
p.catchRate = 190;
p.weight = 30.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_unown), new Pokemon(ctx.getString(R.string.name_unown), 201, 214, Type.PSYCHIC, Type.NONE, abilities, 48, 72, 48, 72, 48, 48));
p = perName.get(ctx.getString(R.string.name_unown));
p.evolutions = null;
p.catchRate = 225;
p.weight = 5.0f;
p.hatch = 10240;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.SPEED_BOOST);}};
perName.put(ctx.getString(R.string.name_combusken), new Pokemon(ctx.getString(R.string.name_combusken), 256, 273, Type.FIRE, Type.FIGHTING, abilities, 60, 85, 60, 85, 60, 55));
p = perName.get(ctx.getString(R.string.name_combusken));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_torchic)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_combusken)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_blaziken)), new HashMap<String, EvolutionNode>(){{this.put("Brasegalite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_blaziken)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 19.5f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWARM);this.add(Ability.SNIPER);}};
perName.put(ctx.getString(R.string.name_beedrill), new Pokemon(ctx.getString(R.string.name_beedrill), 15, 19, Type.BUG, Type.POISON, abilities, 65, 80, 40, 45, 80, 75));
p = perName.get(ctx.getString(R.string.name_beedrill));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_weedle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "7", new EvolutionNode(perName.get(ctx.getString(R.string.name_kakuna)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "10", new EvolutionNode(perName.get(ctx.getString(R.string.name_beedrill)), null));}}));}});
p.catchRate = 45;
p.weight = 29.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SNOW_CLOAK);this.add(Ability.RATTLED);}};
perName.put(ctx.getString(R.string.name_cubchoo), new Pokemon(ctx.getString(R.string.name_cubchoo), 613, 654, Type.ICE, Type.NONE, abilities, 55, 70, 40, 60, 40, 40));
p = perName.get(ctx.getString(R.string.name_cubchoo));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cubchoo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_beartic)), null));}});
p.catchRate = 120;
p.weight = 8.5f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NATURAL_CURE);this.add(Ability.CLOUD_NINE);}};
perName.put(ctx.getString(R.string.name_swablu), new Pokemon(ctx.getString(R.string.name_swablu), 333, 356, Type.NORMAL, Type.FLYING, abilities, 45, 40, 60, 40, 75, 50));
p = perName.get(ctx.getString(R.string.name_swablu));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_swablu)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_altaria)), null));}});
p.catchRate = 255;
p.weight = 1.2f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING,EggGroup.DRAGON};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.RECKLESS);}};
perName.put(ctx.getString(R.string.name_emboar), new Pokemon(ctx.getString(R.string.name_emboar), 500, 540, Type.FIRE, Type.FIGHTING, abilities, 110, 123, 65, 100, 65, 65));
p = perName.get(ctx.getString(R.string.name_emboar));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tepig)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "17", new EvolutionNode(perName.get(ctx.getString(R.string.name_pignite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_emboar)), null));}}));}});
p.catchRate = 45;
p.weight = 150f;
p.hatch = 5355;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWARM);this.add(Ability.CHLOROPHYLL);this.add(Ability.OVERCOAT);}};
perName.put(ctx.getString(R.string.name_leavanny), new Pokemon(ctx.getString(R.string.name_leavanny), 542, 582, Type.BUG, Type.GRASS, abilities, 75, 103, 80, 70, 70, 92));
p = perName.get(ctx.getString(R.string.name_leavanny));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_sewaddle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_swadloon)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_leavanny)), null));}}));}});
p.catchRate = 45;
p.weight = 20.5f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INSOMNIA);this.add(Ability.SUPER_LUCK);this.add(Ability.PRANKSTER);}};
perName.put(ctx.getString(R.string.name_murkrow), new Pokemon(ctx.getString(R.string.name_murkrow), 198, 211, Type.DARK, Type.FLYING, abilities, 60, 85, 42, 85, 42, 91));
p = perName.get(ctx.getString(R.string.name_murkrow));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_murkrow)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_honchkrow)), null));}});
p.catchRate = 30;
p.weight = 2.1f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CLEAR_BODY);this.add(Ability.LIGHT_METAL);}};
perName.put(ctx.getString(R.string.name_beldum), new Pokemon(ctx.getString(R.string.name_beldum), 374, 399, Type.STEEL, Type.PSYCHIC, abilities, 40, 55, 80, 35, 60, 30));
p = perName.get(ctx.getString(R.string.name_beldum));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_beldum)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_metang)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "45", new EvolutionNode(perName.get(ctx.getString(R.string.name_metagross)), null));}}));}});
p.catchRate = 3;
p.weight = 95.2f;
p.hatch = 10240;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.REGENERATOR);this.add(Ability.INNER_FOCUS);this.add(Ability.RECKLESS);}};
perName.put(ctx.getString(R.string.name_mienshao), new Pokemon(ctx.getString(R.string.name_mienshao), 620, 661, Type.FIGHTING, Type.NONE, abilities, 65, 125, 60, 95, 60, 105));
p = perName.get(ctx.getString(R.string.name_mienshao));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mienfoo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "50", new EvolutionNode(perName.get(ctx.getString(R.string.name_mienshao)), null));}});
p.catchRate = 45;
p.weight = 35.5f;
p.hatch = 6630;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.HUMANLIKE};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWARM);this.add(Ability.TINTED_LENS);}};
perName.put(ctx.getString(R.string.name_mothim), new Pokemon(ctx.getString(R.string.name_mothim), 414, 444, Type.BUG, Type.FLYING, abilities, 70, 94, 50, 94, 50, 66));
p = perName.get(ctx.getString(R.string.name_mothim));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_burmy)), new HashMap<String, EvolutionNode>(){{this.put("Si Male, Niveau 20", new EvolutionNode(perName.get(ctx.getString(R.string.name_mothim)), null));this.put("Si Femelle, Niveau 20", new EvolutionNode(perName.get(ctx.getString(R.string.name_wormadam_plant_cloak)), null));}});
p.catchRate = 45;
p.weight = 23.3f;
p.hatch = 3840;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_gastly), new Pokemon(ctx.getString(R.string.name_gastly), 92, 97, Type.GHOST, Type.POISON, abilities, 30, 35, 30, 100, 35, 80));
p = perName.get(ctx.getString(R.string.name_gastly));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_gastly)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_haunter)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_gengar)), new HashMap<String, EvolutionNode>(){{this.put("Ectoplasmite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_gengar)), null));}}));}}));}});
p.catchRate = 190;
p.weight = 0.1f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.KEEN_EYE);this.add(Ability.BIG_PECKS);this.add(Ability.HYDRATION);}};
perName.put(ctx.getString(R.string.name_swanna), new Pokemon(ctx.getString(R.string.name_swanna), 581, 622, Type.WATER, Type.FLYING, abilities, 75, 87, 63, 87, 63, 98));
p = perName.get(ctx.getString(R.string.name_swanna));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_ducklett)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_swanna)), null));}});
p.catchRate = 45;
p.weight = 24.2f;
p.hatch = 7905;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FLYING};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HYPER_CUTTER);this.add(Ability.ARENA_TRAP);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_trapinch), new Pokemon(ctx.getString(R.string.name_trapinch), 328, 351, Type.GROUND, Type.NONE, abilities, 45, 100, 45, 45, 45, 10));
p = perName.get(ctx.getString(R.string.name_trapinch));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_trapinch)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_vibrava)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "45", new EvolutionNode(perName.get(ctx.getString(R.string.name_flygon)), null));}}));}});
p.catchRate = 255;
p.weight = 15.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NATURAL_CURE);this.add(Ability.SERENE_GRACE);this.add(Ability.HEALER);}};
perName.put(ctx.getString(R.string.name_blissey), new Pokemon(ctx.getString(R.string.name_blissey), 242, 258, Type.NORMAL, Type.NONE, abilities, 255, 10, 10, 75, 135, 55));
p = perName.get(ctx.getString(R.string.name_blissey));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_happiny)), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau en tenant une Pierre Ovale", new EvolutionNode(perName.get(ctx.getString(R.string.name_chansey)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_blissey)), null));}}));}});
p.catchRate = 30;
p.weight = 46.8f;
p.hatch = 10240;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.SHELL_ARMOR);}};
perName.put(ctx.getString(R.string.name_grotle), new Pokemon(ctx.getString(R.string.name_grotle), 388, 416, Type.GRASS, Type.NONE, abilities, 75, 89, 85, 55, 65, 36));
p = perName.get(ctx.getString(R.string.name_grotle));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_turtwig)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_grotle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_torterra)), null));}}));}});
p.catchRate = 45;
p.weight = 97.0f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.GRASS};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MOLD_BREAKER);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_rampardos), new Pokemon(ctx.getString(R.string.name_rampardos), 409, 437, Type.ROCK, Type.NONE, abilities, 97, 165, 60, 65, 50, 58));
p = perName.get(ctx.getString(R.string.name_rampardos));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cranidos)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_rampardos)), null));}});
p.catchRate = 45;
p.weight = 102.5f;
p.hatch = 7680;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.SAND_FORCE);}};
perName.put(ctx.getString(R.string.name_gigalith), new Pokemon(ctx.getString(R.string.name_gigalith), 526, 566, Type.ROCK, Type.NONE, abilities, 85, 135, 130, 60, 70, 25));
p = perName.get(ctx.getString(R.string.name_gigalith));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_roggenrola)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_boldore)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_gigalith)), null));}}));}});
p.catchRate = 45;
p.weight = 260.0f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.KEEN_EYE);this.add(Ability.TANGLED_FEET);this.add(Ability.BIG_PECKS);}};
perName.put(ctx.getString(R.string.name_pidgeotto), new Pokemon(ctx.getString(R.string.name_pidgeotto), 17, 21, Type.NORMAL, Type.FLYING, abilities, 63, 60, 55, 50, 50, 71));
p = perName.get(ctx.getString(R.string.name_pidgeotto));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pidgey)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_pidgeotto)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_pidgeot)), null));}}));}});
p.catchRate = 120;
p.weight = 30.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STORM_DRAIN);this.add(Ability.SWIFT_SWIM);this.add(Ability.WATER_VEIL);}};
perName.put(ctx.getString(R.string.name_finneon), new Pokemon(ctx.getString(R.string.name_finneon), 456, 488, Type.WATER, Type.NONE, abilities, 49, 49, 56, 49, 61, 66));
p = perName.get(ctx.getString(R.string.name_finneon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_finneon)), new HashMap<String, EvolutionNode>(){{this.put("niveau 31", new EvolutionNode(perName.get(ctx.getString(R.string.name_lumineon)), null));}});
p.catchRate = 190;
p.weight = 7.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER2};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.COMPOUNDEYE);this.add(Ability.UNNERVE);this.add(Ability.SWARM);}};
perName.put(ctx.getString(R.string.name_joltik), new Pokemon(ctx.getString(R.string.name_joltik), 595, 636, Type.BUG, Type.ELECTRIC, abilities, 50, 47, 50, 57, 50, 65));
p = perName.get(ctx.getString(R.string.name_joltik));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_joltik)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_galvantula)), null));}});
p.catchRate = 190;
p.weight = 0.6f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);}};
perName.put(ctx.getString(R.string.name_dusclops), new Pokemon(ctx.getString(R.string.name_dusclops), 356, 380, Type.GHOST, Type.NONE, abilities, 40, 70, 130, 60, 130, 25));
p = perName.get(ctx.getString(R.string.name_dusclops));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_duskull)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_dusclops)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Tissu Fauche", new EvolutionNode(perName.get(ctx.getString(R.string.name_dusknoir)), null));}}));}});
p.catchRate = 90;
p.weight = 30.6f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.WATER_ABSORB);this.add(Ability.HYDRATION);}};
perName.put(ctx.getString(R.string.name_vaporeon), new Pokemon(ctx.getString(R.string.name_vaporeon), 134, 143, Type.WATER, Type.NONE, abilities, 130, 65, 60, 110, 95, 65));
p = perName.get(ctx.getString(R.string.name_vaporeon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_eevee)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get(ctx.getString(R.string.name_jolteon)), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_leafeon)), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get(ctx.getString(R.string.name_espeon)), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get(ctx.getString(R.string.name_sylveon)), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_vaporeon)), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_glaceon)), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get(ctx.getString(R.string.name_flareon)), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_umbreon)), null));}});
p.catchRate = 45;
p.weight = 29.0f;
p.hatch = 8960;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.SAND_FORCE);}};
perName.put(ctx.getString(R.string.name_boldore), new Pokemon(ctx.getString(R.string.name_boldore), 525, 565, Type.ROCK, Type.NONE, abilities, 70, 105, 105, 50, 40, 20));
p = perName.get(ctx.getString(R.string.name_boldore));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_roggenrola)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_boldore)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_gigalith)), null));}}));}});
p.catchRate = 120;
p.weight = 102.0f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHED_SKIN);this.add(Ability.MARVEL_SCALE);}};
perName.put(ctx.getString(R.string.name_dragonair), new Pokemon(ctx.getString(R.string.name_dragonair), 148, 158, Type.DRAGON, Type.NONE, abilities, 61, 84, 65, 70, 70, 70));
p = perName.get(ctx.getString(R.string.name_dragonair));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_dratini)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_dragonair)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "55", new EvolutionNode(perName.get(ctx.getString(R.string.name_dragonite)), null));}}));}});
p.catchRate = 45;
p.weight = 16.5f;
p.hatch = 10240;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON,EggGroup.WATER1};
p.size = 4.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.MAGNET_PULL);this.add(Ability.ANALYTIC);}};
perName.put(ctx.getString(R.string.name_magnezone), new Pokemon(ctx.getString(R.string.name_magnezone), 462, 495, Type.ELECTRIC, Type.STEEL, abilities, 70, 70, 115, 130, 90, 60));
p = perName.get(ctx.getString(R.string.name_magnezone));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_magnemite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_magneton)), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau dans un lieu indique", new EvolutionNode(perName.get(ctx.getString(R.string.name_magnezone)), null));}}));}});
p.catchRate = 30;
p.weight = 180.0f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NATURAL_CURE);this.add(Ability.POISON_POINT);this.add(Ability.LEAF_GUARD);}};
perName.put(ctx.getString(R.string.name_roselia), new Pokemon(ctx.getString(R.string.name_roselia), 315, 338, Type.GRASS, Type.POISON, abilities, 50, 60, 45, 100, 80, 65));
p = perName.get(ctx.getString(R.string.name_roselia));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_budew)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur , Jour", new EvolutionNode(perName.get(ctx.getString(R.string.name_roselia)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get(ctx.getString(R.string.name_roserade)), null));}}));}});
p.catchRate = 150;
p.weight = 2.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY,EggGroup.GRASS};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TRUANT);}};
perName.put(ctx.getString(R.string.name_slaking), new Pokemon(ctx.getString(R.string.name_slaking), 289, 308, Type.NORMAL, Type.NONE, abilities, 150, 160, 100, 95, 65, 100));
p = perName.get(ctx.getString(R.string.name_slaking));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_slakoth)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_vigoroth)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_slaking)), null));}}));}});
p.catchRate = 45;
p.weight = 130.5f;
p.hatch = 4095;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OWN_TEMPO);this.add(Ability.TANGLED_FEET);this.add(Ability.CONTRARY);}};
perName.put(ctx.getString(R.string.name_spinda), new Pokemon(ctx.getString(R.string.name_spinda), 327, 350, Type.NORMAL, Type.NONE, abilities, 60, 60, 60, 60, 60, 60));
p = perName.get(ctx.getString(R.string.name_spinda));
p.evolutions = null;
p.catchRate = 255;
p.weight = 5.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.HUMANLIKE};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.WATER_ABSORB);this.add(Ability.DAMP);this.add(Ability.SWIFT_SWIM);}};
perName.put(ctx.getString(R.string.name_poliwrath), new Pokemon(ctx.getString(R.string.name_poliwrath), 62, 66, Type.WATER, Type.FIGHTING, abilities, 90, 85, 95, 70, 90, 70));
p = perName.get(ctx.getString(R.string.name_poliwrath));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_poliwag)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_poliwhirl)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Roche Royale", new EvolutionNode(perName.get(ctx.getString(R.string.name_politoed)), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_poliwrath)), null));}}));}});
p.catchRate = 45;
p.weight = 54.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);this.add(Ability.TELEPATHY);}};
perName.put(ctx.getString(R.string.name_palkia), new Pokemon(ctx.getString(R.string.name_palkia), 484, 522, Type.WATER, Type.DRAGON, abilities, 90, 120, 100, 150, 120, 100));
p = perName.get(ctx.getString(R.string.name_palkia));
p.evolutions = null;
p.catchRate = 30;
p.weight = 336.0f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 4.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HUSTLE);this.add(Ability.INNER_FOCUS);}};
perName.put(ctx.getString(R.string.name_darumaka), new Pokemon(ctx.getString(R.string.name_darumaka), 554, 594, Type.FIRE, Type.NONE, abilities, 70, 90, 45, 15, 45, 50));
p = perName.get(ctx.getString(R.string.name_darumaka));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_darumaka)), null);
p.catchRate = 120;
p.weight = 37.5f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FOREWARN);this.add(Ability.SYNCHRONIZE);this.add(Ability.TELEPATHY);}};
perName.put(ctx.getString(R.string.name_munna), new Pokemon(ctx.getString(R.string.name_munna), 517, 557, Type.PSYCHIC, Type.NONE, abilities, 76, 25, 45, 67, 55, 24));
p = perName.get(ctx.getString(R.string.name_munna));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_munna)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get(ctx.getString(R.string.name_musharna)), null));}});
p.catchRate = 190;
p.weight = 23.3f;
p.hatch = 2805;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.ANGER_POINT);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_tauros), new Pokemon(ctx.getString(R.string.name_tauros), 128, 136, Type.NORMAL, Type.NONE, abilities, 75, 100, 95, 40, 70, 110));
p = perName.get(ctx.getString(R.string.name_tauros));
p.evolutions = null;
p.catchRate = 45;
p.weight = 88.4f;
p.hatch = 5120;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.RECKLESS);}};
perName.put(ctx.getString(R.string.name_staraptor), new Pokemon(ctx.getString(R.string.name_staraptor), 398, 426, Type.NORMAL, Type.FLYING, abilities, 85, 120, 70, 50, 50, 100));
p = perName.get(ctx.getString(R.string.name_staraptor));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_starly)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "14", new EvolutionNode(perName.get(ctx.getString(R.string.name_staravia)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "34", new EvolutionNode(perName.get(ctx.getString(R.string.name_staraptor)), null));}}));}});
p.catchRate = 45;
p.weight = 24.9f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RECKLESS);this.add(Ability.SAP_SIPPER);this.add(Ability.SOUNDPROOF);}};
perName.put(ctx.getString(R.string.name_bouffalant), new Pokemon(ctx.getString(R.string.name_bouffalant), 626, 667, Type.NORMAL, Type.NONE, abilities, 95, 110, 95, 40, 95, 55));
p = perName.get(ctx.getString(R.string.name_bouffalant));
p.evolutions = null;
p.catchRate = 45;
p.weight = 94.5f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);this.add(Ability.VOLT_ABSORB);}};
perName.put(ctx.getString(R.string.name_raikou), new Pokemon(ctx.getString(R.string.name_raikou), 243, 259, Type.ELECTRIC, Type.NONE, abilities, 90, 85, 75, 115, 100, 115));
p = perName.get(ctx.getString(R.string.name_raikou));
p.evolutions = null;
p.catchRate = 3;
p.weight = 178.0f;
p.hatch = 20480;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.DEFIANT);}};
perName.put(ctx.getString(R.string.name_empoleon), new Pokemon(ctx.getString(R.string.name_empoleon), 395, 423, Type.WATER, Type.STEEL, abilities, 84, 86, 88, 111, 101, 60));
p = perName.get(ctx.getString(R.string.name_empoleon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_piplup)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_prinplup)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_empoleon)), null));}}));}});
p.catchRate = 45;
p.weight = 84.5f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.FLASH_FIRE);}};
perName.put(ctx.getString(R.string.name_cyndaquil), new Pokemon(ctx.getString(R.string.name_cyndaquil), 155, 167, Type.FIRE, Type.NONE, abilities, 39, 52, 43, 60, 50, 65));
p = perName.get(ctx.getString(R.string.name_cyndaquil));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cyndaquil)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "14", new EvolutionNode(perName.get(ctx.getString(R.string.name_quilava)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_typhlosion)), null));}}));}});
p.catchRate = 45;
p.weight = 7.9f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.SHED_SKIN);this.add(Ability.UNNERVE);}};
perName.put(ctx.getString(R.string.name_arbok), new Pokemon(ctx.getString(R.string.name_arbok), 24, 28, Type.POISON, Type.NONE, abilities, 60, 85, 69, 65, 79, 80));
p = perName.get(ctx.getString(R.string.name_arbok));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_ekans)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "22", new EvolutionNode(perName.get(ctx.getString(R.string.name_arbok)), null));}});
p.catchRate = 90;
p.weight = 65.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.DRAGON};
p.size = 3.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FRISK);this.add(Ability.COMPETITIVE);this.add(Ability.SHADOW_TAG);}};
perName.put(ctx.getString(R.string.name_gothorita), new Pokemon(ctx.getString(R.string.name_gothorita), 575, 616, Type.PSYCHIC, Type.NONE, abilities, 60, 45, 70, 75, 85, 55));
p = perName.get(ctx.getString(R.string.name_gothorita));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_gothita)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_gothorita)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "41", new EvolutionNode(perName.get(ctx.getString(R.string.name_gothitelle)), null));}}));}});
p.catchRate = 100;
p.weight = 18.0f;
p.hatch = 5355;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.IRON_FIST);}};
perName.put(ctx.getString(R.string.name_monferno), new Pokemon(ctx.getString(R.string.name_monferno), 391, 419, Type.FIRE, Type.FIGHTING, abilities, 64, 78, 52, 78, 52, 81));
p = perName.get(ctx.getString(R.string.name_monferno));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_chimchar)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "14", new EvolutionNode(perName.get(ctx.getString(R.string.name_monferno)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_infernape)), null));}}));}});
p.catchRate = 45;
p.weight = 22.0f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.HUMANLIKE};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.DAMP);this.add(Ability.CLOUD_NINE);this.add(Ability.SWIFT_SWIM);}};
perName.put(ctx.getString(R.string.name_psyduck), new Pokemon(ctx.getString(R.string.name_psyduck), 54, 58, Type.WATER, Type.NONE, abilities, 50, 52, 48, 65, 50, 55));
p = perName.get(ctx.getString(R.string.name_psyduck));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_psyduck)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "33", new EvolutionNode(perName.get(ctx.getString(R.string.name_golduck)), null));}});
p.catchRate = 190;
p.weight = 19.6f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.GLUTTONY);}};
perName.put(ctx.getString(R.string.name_weepinbell), new Pokemon(ctx.getString(R.string.name_weepinbell), 70, 75, Type.GRASS, Type.POISON, abilities, 65, 90, 50, 85, 45, 55));
p = perName.get(ctx.getString(R.string.name_weepinbell));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bellsprout)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "21", new EvolutionNode(perName.get(ctx.getString(R.string.name_weepinbell)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get(ctx.getString(R.string.name_victreebel)), null));}}));}});
p.catchRate = 120;
p.weight = 6.4f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TRACE);this.add(Ability.DOWNLOAD);this.add(Ability.ANALYTIC);}};
perName.put(ctx.getString(R.string.name_porygon2), new Pokemon(ctx.getString(R.string.name_porygon2), 233, 249, Type.NORMAL, Type.NONE, abilities, 85, 80, 90, 105, 95, 60));
p = perName.get(ctx.getString(R.string.name_porygon2));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_porygon)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Ameliorator", new EvolutionNode(perName.get(ctx.getString(R.string.name_porygon2)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant CD Douteux", new EvolutionNode(perName.get(ctx.getString(R.string.name_porygon_z)), null));}}));}});
p.catchRate = 45;
p.weight = 36.5f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.THICK_FAT);this.add(Ability.ICE_BODY);this.add(Ability.OBLIVIOUS);}};
perName.put(ctx.getString(R.string.name_walrein), new Pokemon(ctx.getString(R.string.name_walrein), 365, 390, Type.ICE, Type.WATER, abilities, 110, 80, 90, 95, 90, 65));
p = perName.get(ctx.getString(R.string.name_walrein));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_spheal)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_sealeo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "44", new EvolutionNode(perName.get(ctx.getString(R.string.name_walrein)), null));}}));}});
p.catchRate = 45;
p.weight = 150.6f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.DAMP);this.add(Ability.CLOUD_NINE);this.add(Ability.SWIFT_SWIM);}};
perName.put(ctx.getString(R.string.name_golduck), new Pokemon(ctx.getString(R.string.name_golduck), 55, 59, Type.WATER, Type.NONE, abilities, 80, 82, 78, 95, 80, 85));
p = perName.get(ctx.getString(R.string.name_golduck));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_psyduck)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "33", new EvolutionNode(perName.get(ctx.getString(R.string.name_golduck)), null));}});
p.catchRate = 75;
p.weight = 76.6f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.KEEN_EYE);this.add(Ability.IRON_FIST);this.add(Ability.INNER_FOCUS);}};
perName.put(ctx.getString(R.string.name_hitmonchan), new Pokemon(ctx.getString(R.string.name_hitmonchan), 107, 113, Type.FIGHTING, Type.NONE, abilities, 50, 105, 79, 35, 110, 76));
p = perName.get(ctx.getString(R.string.name_hitmonchan));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tyrogue)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20, Attaque < Defense", new EvolutionNode(perName.get(ctx.getString(R.string.name_hitmonchan)), null));this.put(ctx.getString(R.string.level) + "20, Attaque > Defense", new EvolutionNode(perName.get(ctx.getString(R.string.name_hitmonlee)), null));this.put(ctx.getString(R.string.level) + "20, Attaque et Defense identiques", new EvolutionNode(perName.get(ctx.getString(R.string.name_hitmontop)), null));}});
p.catchRate = 45;
p.weight = 50.2f;
p.hatch = 6400;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.THICK_FAT);this.add(Ability.GLUTTONY);}};
perName.put(ctx.getString(R.string.name_munchlax), new Pokemon(ctx.getString(R.string.name_munchlax), 446, 477, Type.NORMAL, Type.NONE, abilities, 135, 85, 40, 40, 85, 5));
p = perName.get(ctx.getString(R.string.name_munchlax));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_munchlax)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_snorlax)), null));}});
p.catchRate = 50;
p.weight = 105.0f;
p.hatch = 10240;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_VEIL);}};
perName.put(ctx.getString(R.string.name_gible), new Pokemon(ctx.getString(R.string.name_gible), 443, 473, Type.DRAGON, Type.GROUND, abilities, 58, 70, 45, 40, 45, 42));
p = perName.get(ctx.getString(R.string.name_gible));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_gible)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "24", new EvolutionNode(perName.get(ctx.getString(R.string.name_gabite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "48", new EvolutionNode(perName.get(ctx.getString(R.string.name_garchomp)), new HashMap<String, EvolutionNode>(){{this.put("Carchacrokite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_garchomp)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 20.5f;
p.hatch = 10240;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON,EggGroup.MONSTER};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWEET_VEIL);this.add(Ability.UNBURDEN);}};
perName.put(ctx.getString(R.string.name_swirlix), new Pokemon(ctx.getString(R.string.name_swirlix), 684, 731, Type.FAIRY, Type.NONE, abilities, 62, 48, 66, 59, 57, 49));
p = perName.get(ctx.getString(R.string.name_swirlix));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_swirlix)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Chantibonbon", new EvolutionNode(perName.get(ctx.getString(R.string.name_slurpuff)), null));}});
p.catchRate = -1;
p.weight = 3.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HYDRATION);this.add(Ability.SHELL_ARMOR);this.add(Ability.OVERCOAT);}};
perName.put(ctx.getString(R.string.name_shelmet), new Pokemon(ctx.getString(R.string.name_shelmet), 616, 657, Type.BUG, Type.NONE, abilities, 50, 40, 85, 40, 65, 25));
p = perName.get(ctx.getString(R.string.name_shelmet));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_shelmet)), new HashMap<String, EvolutionNode>(){{this.put("Echange avec Carabing", new EvolutionNode(perName.get(ctx.getString(R.string.name_accelgor)), null));}});
p.catchRate = 200;
p.weight = 7.7f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NO_GUARD);}};
perName.put(ctx.getString(R.string.name_honedge), new Pokemon(ctx.getString(R.string.name_honedge), 679, 725, Type.STEEL, Type.GHOST, abilities, 40, 90, 130, 35, 30, 10));
p = perName.get(ctx.getString(R.string.name_honedge));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_honedge)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_doublade)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_aegislash_blade_forme)), null));}}));}});
p.catchRate = -1;
p.weight = 2.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.MAGICIAN);}};
perName.put(ctx.getString(R.string.name_delphox), new Pokemon(ctx.getString(R.string.name_delphox), 655, 701, Type.FIRE, Type.PSYCHIC, abilities, 75, 69, 72, 114, 100, 104));
p = perName.get(ctx.getString(R.string.name_delphox));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_fennekin)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_braixen)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_delphox)), null));}}));}});
p.catchRate = 45;
p.weight = 39.0f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.KEEN_EYE);this.add(Ability.STALL);this.add(Ability.PRANKSTER);}};
perName.put(ctx.getString(R.string.name_sableye), new Pokemon(ctx.getString(R.string.name_sableye), 302, 321, Type.DARK, Type.GHOST, abilities, 50, 75, 75, 65, 65, 50));
p = perName.get(ctx.getString(R.string.name_sableye));
p.evolutions = null;
p.catchRate = 45;
p.weight = 11.0f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);}};
perName.put(ctx.getString(R.string.name_buizel), new Pokemon(ctx.getString(R.string.name_buizel), 418, 448, Type.WATER, Type.NONE, abilities, 55, 65, 35, 60, 30, 85));
p = perName.get(ctx.getString(R.string.name_buizel));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_buizel)), new HashMap<String, EvolutionNode>(){{this.put("niveau 26", new EvolutionNode(perName.get(ctx.getString(R.string.name_floatzel)), null));}});
p.catchRate = 190;
p.weight = 29.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INNER_FOCUS);this.add(Ability.INFILTRATOR);}};
perName.put(ctx.getString(R.string.name_golbat), new Pokemon(ctx.getString(R.string.name_golbat), 42, 46, Type.POISON, Type.FLYING, abilities, 75, 80, 70, 65, 75, 90));
p = perName.get(ctx.getString(R.string.name_golbat));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_zubat)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "22", new EvolutionNode(perName.get(ctx.getString(R.string.name_golbat)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_crobat)), null));}}));}});
p.catchRate = 90;
p.weight = 55.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GUTS);this.add(Ability.INNER_FOCUS);this.add(Ability.MOLD_BREAKER);}};
perName.put(ctx.getString(R.string.name_throh), new Pokemon(ctx.getString(R.string.name_throh), 538, 578, Type.FIGHTING, Type.NONE, abilities, 120, 100, 85, 30, 85, 45));
p = perName.get(ctx.getString(R.string.name_throh));
p.evolutions = null;
p.catchRate = 45;
p.weight = 55.5f;
p.hatch = 5355;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.ROCK_HEAD);this.add(Ability.STURDY);}};
perName.put(ctx.getString(R.string.name_relicanth), new Pokemon(ctx.getString(R.string.name_relicanth), 369, 394, Type.WATER, Type.ROCK, abilities, 100, 90, 130, 45, 65, 55));
p = perName.get(ctx.getString(R.string.name_relicanth));
p.evolutions = null;
p.catchRate = 25;
p.weight = 23.4f;
p.hatch = 10240;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER2};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FOREWARN);this.add(Ability.SYNCHRONIZE);this.add(Ability.TELEPATHY);}};
perName.put(ctx.getString(R.string.name_musharna), new Pokemon(ctx.getString(R.string.name_musharna), 518, 558, Type.PSYCHIC, Type.NONE, abilities, 116, 55, 85, 107, 95, 29));
p = perName.get(ctx.getString(R.string.name_musharna));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_munna)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get(ctx.getString(R.string.name_musharna)), null));}});
p.catchRate = 75;
p.weight = 60.5f;
p.hatch = 2805;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NATURAL_CURE);this.add(Ability.SERENE_GRACE);this.add(Ability.FRIEND_GUARD);}};
perName.put(ctx.getString(R.string.name_happiny), new Pokemon(ctx.getString(R.string.name_happiny), 440, 470, Type.NORMAL, Type.NONE, abilities, 100, 5, 5, 15, 65, 30));
p = perName.get(ctx.getString(R.string.name_happiny));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_happiny)), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau en journee en tenant une Pierre Ovale", new EvolutionNode(perName.get(ctx.getString(R.string.name_chansey)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_blissey)), null));}}));}});
p.catchRate = 130;
p.weight = 24.4f;
p.hatch = 10240;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHELL_ARMOR);this.add(Ability.RATTLED);}};
perName.put(ctx.getString(R.string.name_clamperl), new Pokemon(ctx.getString(R.string.name_clamperl), 366, 391, Type.WATER, Type.NONE, abilities, 35, 64, 85, 74, 55, 32));
p = perName.get(ctx.getString(R.string.name_clamperl));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_clamperl)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant une Ecaille Ocean", new EvolutionNode(perName.get(ctx.getString(R.string.name_gorebyss)), null));this.put("Echange en tenant une Dent Ocean", new EvolutionNode(perName.get(ctx.getString(R.string.name_huntail)), null));}});
p.catchRate = 255;
p.weight = 52.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_eelektross), new Pokemon(ctx.getString(R.string.name_eelektross), 604, 645, Type.ELECTRIC, Type.NONE, abilities, 85, 115, 80, 105, 80, 50));
p = perName.get(ctx.getString(R.string.name_eelektross));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tynamo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "39", new EvolutionNode(perName.get(ctx.getString(R.string.name_eelektrik)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get(ctx.getString(R.string.name_eelektross)), null));}}));}});
p.catchRate = 30;
p.weight = 80.5f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 2.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NATURAL_CURE);this.add(Ability.FRISK);this.add(Ability.HARVEST);}};
perName.put(ctx.getString(R.string.name_phantump), new Pokemon(ctx.getString(R.string.name_phantump), 708, 755, Type.GHOST, Type.GRASS, abilities, 43, 70, 48, 50, 60, 38));
p = perName.get(ctx.getString(R.string.name_phantump));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_phantump)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_trevenant)), null));}});
p.catchRate = -1;
p.weight = 7.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS,EggGroup.UNKNOWN};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NATURAL_CURE);this.add(Ability.POISON_POINT);this.add(Ability.LEAF_GUARD);}};
perName.put(ctx.getString(R.string.name_budew), new Pokemon(ctx.getString(R.string.name_budew), 406, 434, Type.GRASS, Type.NONE, abilities, 40, 30, 35, 50, 70, 55));
p = perName.get(ctx.getString(R.string.name_budew));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_budew)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur , Jour", new EvolutionNode(perName.get(ctx.getString(R.string.name_roselia)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get(ctx.getString(R.string.name_roserade)), null));}}));}});
p.catchRate = 255;
p.weight = 1.2f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INNER_FOCUS);this.add(Ability.DEFIANT);this.add(Ability.PRESSURE);}};
perName.put(ctx.getString(R.string.name_bisharp), new Pokemon(ctx.getString(R.string.name_bisharp), 625, 666, Type.STEEL, Type.DARK, abilities, 65, 125, 100, 60, 70, 70));
p = perName.get(ctx.getString(R.string.name_bisharp));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pawniard)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "52", new EvolutionNode(perName.get(ctx.getString(R.string.name_bisharp)), null));}});
p.catchRate = 45;
p.weight = 70.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.THICK_FAT);this.add(Ability.ICE_BODY);this.add(Ability.OBLIVIOUS);}};
perName.put(ctx.getString(R.string.name_sealeo), new Pokemon(ctx.getString(R.string.name_sealeo), 364, 389, Type.ICE, Type.WATER, abilities, 90, 60, 70, 75, 70, 45));
p = perName.get(ctx.getString(R.string.name_sealeo));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_spheal)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_sealeo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "44", new EvolutionNode(perName.get(ctx.getString(R.string.name_walrein)), null));}}));}});
p.catchRate = 120;
p.weight = 87.6f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TELEPATHY);this.add(Ability.SYNCHRONIZE);this.add(Ability.ANALYTIC);}};
perName.put(ctx.getString(R.string.name_beheeyem), new Pokemon(ctx.getString(R.string.name_beheeyem), 606, 647, Type.PSYCHIC, Type.NONE, abilities, 75, 75, 75, 125, 95, 40));
p = perName.get(ctx.getString(R.string.name_beheeyem));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_elgyem)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "42", new EvolutionNode(perName.get(ctx.getString(R.string.name_beheeyem)), null));}});
p.catchRate = 90;
p.weight = 34.5f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.UNAWARE);this.add(Ability.KLUTZ);this.add(Ability.SIMPLE);}};
perName.put(ctx.getString(R.string.name_woobat), new Pokemon(ctx.getString(R.string.name_woobat), 527, 567, Type.PSYCHIC, Type.FLYING, abilities, 55, 45, 43, 55, 43, 72));
p = perName.get(ctx.getString(R.string.name_woobat));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_woobat)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_swoobat)), null));}});
p.catchRate = 190;
p.weight = 2.1f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.FLYING};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);}};
perName.put(ctx.getString(R.string.name_floatzel), new Pokemon(ctx.getString(R.string.name_floatzel), 419, 449, Type.WATER, Type.NONE, abilities, 85, 105, 55, 85, 50, 115));
p = perName.get(ctx.getString(R.string.name_floatzel));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_buizel)), new HashMap<String, EvolutionNode>(){{this.put("niveau 26", new EvolutionNode(perName.get(ctx.getString(R.string.name_floatzel)), null));}});
p.catchRate = 75;
p.weight = 33.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SERENE_GRACE);this.add(Ability.RUN_AWAY);this.add(Ability.RATTLED);}};
perName.put(ctx.getString(R.string.name_dunsparce), new Pokemon(ctx.getString(R.string.name_dunsparce), 206, 219, Type.NORMAL, Type.NONE, abilities, 100, 70, 70, 65, 65, 45));
p = perName.get(ctx.getString(R.string.name_dunsparce));
p.evolutions = null;
p.catchRate = 190;
p.weight = 14.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_STREAM);}};
perName.put(ctx.getString(R.string.name_mega_tyranitar), new Pokemon(ctx.getString(R.string.name_mega_tyranitar), 248, 265, Type.ROCK, Type.DARK, abilities, 100, 164, 150, 95, 120, 71));
p = perName.get(ctx.getString(R.string.name_mega_tyranitar));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_larvitar)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_pupitar)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "55", new EvolutionNode(perName.get(ctx.getString(R.string.name_tyranitar)), new HashMap<String, EvolutionNode>(){{this.put("Tyranocivite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_tyranitar)), null));}}));}}));}});
p.catchRate = -1;
p.weight = 255.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.WONDER_GUARD);}};
perName.put(ctx.getString(R.string.name_shedinja), new Pokemon(ctx.getString(R.string.name_shedinja), 292, 311, Type.BUG, Type.GHOST, abilities, 1, 90, 45, 30, 30, 40));
p = perName.get(ctx.getString(R.string.name_shedinja));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_nincada)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_ninjask)), null));this.put(ctx.getString(R.string.level) + "20, emplacement libre et Poke Ball dans l'inventaire", new EvolutionNode(perName.get(ctx.getString(R.string.name_shedinja)), null));}});
p.catchRate = 45;
p.weight = 1.2f;
p.hatch = 3840;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ROUGH_SKIN);this.add(Ability.SHEER_FORCE);this.add(Ability.MOLD_BREAKER);}};
perName.put(ctx.getString(R.string.name_druddigon), new Pokemon(ctx.getString(R.string.name_druddigon), 621, 662, Type.DRAGON, Type.NONE, abilities, 77, 120, 90, 60, 90, 48));
p = perName.get(ctx.getString(R.string.name_druddigon));
p.evolutions = null;
p.catchRate = 45;
p.weight = 139.0f;
p.hatch = 7905;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON,EggGroup.MONSTER};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ICE_BODY);this.add(Ability.WEAK_ARMOR);}};
perName.put(ctx.getString(R.string.name_vanilluxe), new Pokemon(ctx.getString(R.string.name_vanilluxe), 584, 625, Type.ICE, Type.NONE, abilities, 71, 95, 85, 110, 95, 79));
p = perName.get(ctx.getString(R.string.name_vanilluxe));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_vanillite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_vanillish)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "47", new EvolutionNode(perName.get(ctx.getString(R.string.name_vanilluxe)), null));}}));}});
p.catchRate = 45;
p.weight = 57.5f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SNOW_WARNING);}};
perName.put(ctx.getString(R.string.name_mega_abomasnow), new Pokemon(ctx.getString(R.string.name_mega_abomasnow), 460, 493, Type.ICE, Type.GRASS, abilities, 90, 132, 105, 132, 105, 30));
p = perName.get(ctx.getString(R.string.name_mega_abomasnow));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_snover)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_abomasnow)), new HashMap<String, EvolutionNode>(){{this.put("Blizzarite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_abomasnow)), null));}}));}});
p.catchRate = -1;
p.weight = 135.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TERAVOLT);}};
perName.put(ctx.getString(R.string.name_zekrom), new Pokemon(ctx.getString(R.string.name_zekrom), 644, 687, Type.DRAGON, Type.ELECTRIC, abilities, 100, 150, 120, 120, 100, 90));
p = perName.get(ctx.getString(R.string.name_zekrom));
p.evolutions = null;
p.catchRate = 45;
p.weight = 345f;
p.hatch = 30855;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HUSTLE);this.add(Ability.SNIPER);this.add(Ability.MOODY);}};
perName.put(ctx.getString(R.string.name_remoraid), new Pokemon(ctx.getString(R.string.name_remoraid), 223, 238, Type.WATER, Type.NONE, abilities, 35, 65, 35, 65, 35, 65));
p = perName.get(ctx.getString(R.string.name_remoraid));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_remoraid)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_octillery)), null));}});
p.catchRate = 190;
p.weight = 12.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER2};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HYDRATION);this.add(Ability.HEALER);this.add(Ability.REGENERATOR);}};
perName.put(ctx.getString(R.string.name_alomomola), new Pokemon(ctx.getString(R.string.name_alomomola), 594, 635, Type.WATER, Type.NONE, abilities, 165, 75, 80, 40, 45, 65));
p = perName.get(ctx.getString(R.string.name_alomomola));
p.evolutions = null;
p.catchRate = 75;
p.weight = 31.6f;
p.hatch = 10455;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER2};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERCOAT);this.add(Ability.MAGIC_GUARD);this.add(Ability.REGENERATOR);}};
perName.put(ctx.getString(R.string.name_duosion), new Pokemon(ctx.getString(R.string.name_duosion), 578, 619, Type.PSYCHIC, Type.NONE, abilities, 65, 40, 50, 125, 60, 30));
p = perName.get(ctx.getString(R.string.name_duosion));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_solosis)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_duosion)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "41", new EvolutionNode(perName.get(ctx.getString(R.string.name_reuniclus)), null));}}));}});
p.catchRate = 100;
p.weight = 8.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SYNCHRONIZE);this.add(Ability.INNER_FOCUS);}};
perName.put(ctx.getString(R.string.name_umbreon), new Pokemon(ctx.getString(R.string.name_umbreon), 197, 210, Type.DARK, Type.NONE, abilities, 95, 65, 110, 60, 130, 65));
p = perName.get(ctx.getString(R.string.name_umbreon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_eevee)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get(ctx.getString(R.string.name_jolteon)), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_leafeon)), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get(ctx.getString(R.string.name_espeon)), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get(ctx.getString(R.string.name_sylveon)), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_vaporeon)), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_glaceon)), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get(ctx.getString(R.string.name_flareon)), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_umbreon)), null));}});
p.catchRate = 45;
p.weight = 27.0f;
p.hatch = 8960;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MOLD_BREAKER);}};
perName.put(ctx.getString(R.string.name_mega_ampharos), new Pokemon(ctx.getString(R.string.name_mega_ampharos), 181, 194, Type.ELECTRIC, Type.DRAGON, abilities, 90, 95, 105, 165, 110, 45));
p = perName.get(ctx.getString(R.string.name_mega_ampharos));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mareep)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "15", new EvolutionNode(perName.get(ctx.getString(R.string.name_flaaffy)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_ampharos)), new HashMap<String, EvolutionNode>(){{this.put("Pharampite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_ampharos)), null));}}));}}));}});
p.catchRate = -1;
p.weight = 61.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OBLIVIOUS);this.add(Ability.OWN_TEMPO);this.add(Ability.REGENERATOR);}};
perName.put(ctx.getString(R.string.name_slowpoke), new Pokemon(ctx.getString(R.string.name_slowpoke), 79, 84, Type.WATER, Type.PSYCHIC, abilities, 90, 65, 65, 40, 40, 15));
p = perName.get(ctx.getString(R.string.name_slowpoke));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_slowpoke)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_slowbro)), null));this.put("Echange en tenant Roche Royale", new EvolutionNode(perName.get(ctx.getString(R.string.name_slowking)), null));}});
p.catchRate = 190;
p.weight = 36.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.WATER1};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWEET_VEIL);this.add(Ability.UNBURDEN);}};
perName.put(ctx.getString(R.string.name_slurpuff), new Pokemon(ctx.getString(R.string.name_slurpuff), 685, 732, Type.FAIRY, Type.NONE, abilities, 82, 80, 86, 85, 75, 72));
p = perName.get(ctx.getString(R.string.name_slurpuff));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_swirlix)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Chantibonbon", new EvolutionNode(perName.get(ctx.getString(R.string.name_slurpuff)), null));}});
p.catchRate = -1;
p.weight = 5.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.RAIN_DISH);}};
perName.put(ctx.getString(R.string.name_wartortle), new Pokemon(ctx.getString(R.string.name_wartortle), 8, 11, Type.WATER, Type.NONE, abilities, 59, 63, 80, 65, 80, 58));
p = perName.get(ctx.getString(R.string.name_wartortle));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_squirtle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_wartortle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_blastoise)), new HashMap<String, EvolutionNode>(){{this.put("Tortankite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_blastoise)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 22.5f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.MONSTER};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OBLIVIOUS);this.add(Ability.ANTICIPATION);this.add(Ability.HYDRATION);}};
perName.put(ctx.getString(R.string.name_whiscash), new Pokemon(ctx.getString(R.string.name_whiscash), 340, 363, Type.WATER, Type.GROUND, abilities, 110, 78, 73, 76, 71, 60));
p = perName.get(ctx.getString(R.string.name_whiscash));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_barboach)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_whiscash)), null));}});
p.catchRate = 75;
p.weight = 23.6f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER2};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BIG_PECKS);this.add(Ability.SUPER_LUCK);this.add(Ability.RIVALRY);}};
perName.put(ctx.getString(R.string.name_tranquill), new Pokemon(ctx.getString(R.string.name_tranquill), 520, 560, Type.NORMAL, Type.FLYING, abilities, 62, 77, 62, 50, 42, 65));
p = perName.get(ctx.getString(R.string.name_tranquill));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pidove)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "21", new EvolutionNode(perName.get(ctx.getString(R.string.name_tranquill)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_unfezant)), null));}}));}});
p.catchRate = 120;
p.weight = 15.0f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHED_SKIN);this.add(Ability.MOXIE);this.add(Ability.INTIMIDATE);}};
perName.put(ctx.getString(R.string.name_scrafty), new Pokemon(ctx.getString(R.string.name_scrafty), 560, 601, Type.DARK, Type.FIGHTING, abilities, 65, 90, 115, 45, 115, 58));
p = perName.get(ctx.getString(R.string.name_scrafty));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_scraggy)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "39", new EvolutionNode(perName.get(ctx.getString(R.string.name_scrafty)), null));}});
p.catchRate = 90;
p.weight = 30.0f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.DRAGON};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SOUNDPROOF);this.add(Ability.SCRAPPY);}};
perName.put(ctx.getString(R.string.name_loudred), new Pokemon(ctx.getString(R.string.name_loudred), 294, 313, Type.NORMAL, Type.NONE, abilities, 84, 71, 43, 71, 43, 48));
p = perName.get(ctx.getString(R.string.name_loudred));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_whismur)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_loudred)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_exploud)), null));}}));}});
p.catchRate = 120;
p.weight = 40.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LIMBER);this.add(Ability.RECKLESS);this.add(Ability.UNBURDEN);}};
perName.put(ctx.getString(R.string.name_hitmonlee), new Pokemon(ctx.getString(R.string.name_hitmonlee), 106, 112, Type.FIGHTING, Type.NONE, abilities, 50, 120, 53, 35, 110, 87));
p = perName.get(ctx.getString(R.string.name_hitmonlee));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tyrogue)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20, Attaque < Defense", new EvolutionNode(perName.get(ctx.getString(R.string.name_hitmonchan)), null));this.put(ctx.getString(R.string.level) + "20, Attaque > Defense", new EvolutionNode(perName.get(ctx.getString(R.string.name_hitmonlee)), null));this.put(ctx.getString(R.string.level) + "20, Attaque et Defense identiques", new EvolutionNode(perName.get(ctx.getString(R.string.name_hitmontop)), null));}});
p.catchRate = 45;
p.weight = 49.8f;
p.hatch = 6400;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.QUICK_FEET);this.add(Ability.HONEY_GATHER);}};
perName.put(ctx.getString(R.string.name_teddiursa), new Pokemon(ctx.getString(R.string.name_teddiursa), 216, 231, Type.NORMAL, Type.NONE, abilities, 60, 80, 50, 50, 50, 40));
p = perName.get(ctx.getString(R.string.name_teddiursa));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_teddiursa)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_ursaring)), null));}});
p.catchRate = 120;
p.weight = 8.8f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.INNER_FOCUS);this.add(Ability.MOLD_BREAKER);}};
perName.put(ctx.getString(R.string.name_sawk), new Pokemon(ctx.getString(R.string.name_sawk), 539, 579, Type.FIGHTING, Type.NONE, abilities, 75, 125, 75, 30, 75, 85));
p = perName.get(ctx.getString(R.string.name_sawk));
p.evolutions = null;
p.catchRate = 45;
p.weight = 51.0f;
p.hatch = 5355;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.WATER_VEIL);}};
perName.put(ctx.getString(R.string.name_huntail), new Pokemon(ctx.getString(R.string.name_huntail), 367, 392, Type.WATER, Type.NONE, abilities, 55, 104, 105, 94, 75, 52));
p = perName.get(ctx.getString(R.string.name_huntail));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_clamperl)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant une Ecaille Ocean", new EvolutionNode(perName.get(ctx.getString(R.string.name_gorebyss)), null));this.put("Echange en tenant une Dent Ocean", new EvolutionNode(perName.get(ctx.getString(R.string.name_huntail)), null));}});
p.catchRate = 60;
p.weight = 27.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TRACE);this.add(Ability.DOWNLOAD);this.add(Ability.ANALYTIC);}};
perName.put(ctx.getString(R.string.name_porygon), new Pokemon(ctx.getString(R.string.name_porygon), 137, 146, Type.NORMAL, Type.NONE, abilities, 65, 60, 70, 85, 75, 40));
p = perName.get(ctx.getString(R.string.name_porygon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_porygon)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Ameliorator", new EvolutionNode(perName.get(ctx.getString(R.string.name_porygon2)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant CD Douteux", new EvolutionNode(perName.get(ctx.getString(R.string.name_porygon_z)), null));}}));}});
p.catchRate = 45;
p.weight = 36.5f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.SAND_RUSH);this.add(Ability.SCRAPPY);}};
perName.put(ctx.getString(R.string.name_stoutland), new Pokemon(ctx.getString(R.string.name_stoutland), 508, 548, Type.NORMAL, Type.NONE, abilities, 85, 100, 90, 45, 90, 80));
p = perName.get(ctx.getString(R.string.name_stoutland));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_lillipup)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_herdier)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_stoutland)), null));}}));}});
p.catchRate = 45;
p.weight = 61.0f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLAME_BODY);this.add(Ability.SWARM);}};
perName.put(ctx.getString(R.string.name_volcarona), new Pokemon(ctx.getString(R.string.name_volcarona), 637, 678, Type.BUG, Type.FIRE, abilities, 85, 60, 65, 135, 105, 100));
p = perName.get(ctx.getString(R.string.name_volcarona));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_larvesta)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "59", new EvolutionNode(perName.get(ctx.getString(R.string.name_volcarona)), null));}});
p.catchRate = 15;
p.weight = 46f;
p.hatch = 10240;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.CONTRARY);}};
perName.put(ctx.getString(R.string.name_serperior), new Pokemon(ctx.getString(R.string.name_serperior), 497, 537, Type.GRASS, Type.NONE, abilities, 75, 75, 95, 75, 95, 113));
p = perName.get(ctx.getString(R.string.name_serperior));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_snivy)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "17", new EvolutionNode(perName.get(ctx.getString(R.string.name_servine)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_serperior)), null));}}));}});
p.catchRate = 45;
p.weight = 63f;
p.hatch = 5355;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(3, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.GRASS};
p.size = 3.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHED_SKIN);}};
perName.put(ctx.getString(R.string.name_cascoon), new Pokemon(ctx.getString(R.string.name_cascoon), 268, 286, Type.BUG, Type.NONE, abilities, 50, 35, 55, 25, 25, 15));
p = perName.get(ctx.getString(R.string.name_cascoon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_wurmple)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "10", new EvolutionNode(perName.get(ctx.getString(R.string.name_dustox)), null));this.put(ctx.getString(R.string.level) + "7, au hasard", new EvolutionNode(perName.get(ctx.getString(R.string.name_cascoon)), null));}});
p.catchRate = 120;
p.weight = 11.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.RAIN_DISH);}};
perName.put(ctx.getString(R.string.name_lotad), new Pokemon(ctx.getString(R.string.name_lotad), 270, 288, Type.WATER, Type.GRASS, abilities, 40, 30, 30, 40, 50, 30));
p = perName.get(ctx.getString(R.string.name_lotad));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_lotad)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "14", new EvolutionNode(perName.get(ctx.getString(R.string.name_lombre)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_ludicolo)), null));}}));}});
p.catchRate = 255;
p.weight = 2.6f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.GRASS};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.OVERCOAT);}};
perName.put(ctx.getString(R.string.name_forretress), new Pokemon(ctx.getString(R.string.name_forretress), 205, 218, Type.BUG, Type.STEEL, abilities, 75, 90, 140, 60, 60, 40));
p = perName.get(ctx.getString(R.string.name_forretress));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pineco)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "31", new EvolutionNode(perName.get(ctx.getString(R.string.name_forretress)), null));}});
p.catchRate = 75;
p.weight = 125.8f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.COMPOUNDEYE);this.add(Ability.TINTED_LENS);this.add(Ability.RUN_AWAY);}};
perName.put(ctx.getString(R.string.name_venonat), new Pokemon(ctx.getString(R.string.name_venonat), 48, 52, Type.BUG, Type.POISON, abilities, 60, 55, 50, 40, 55, 45));
p = perName.get(ctx.getString(R.string.name_venonat));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_venonat)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "31", new EvolutionNode(perName.get(ctx.getString(R.string.name_venomoth)), null));}});
p.catchRate = 190;
p.weight = 30.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OBLIVIOUS);this.add(Ability.FOREWARN);this.add(Ability.DRY_SKIN);}};
perName.put(ctx.getString(R.string.name_jynx), new Pokemon(ctx.getString(R.string.name_jynx), 124, 131, Type.ICE, Type.PSYCHIC, abilities, 65, 50, 35, 115, 95, 95));
p = perName.get(ctx.getString(R.string.name_jynx));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_smoochum)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_jynx)), null));}});
p.catchRate = 45;
p.weight = 40.6f;
p.hatch = 6400;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MINUS);}};
perName.put(ctx.getString(R.string.name_minun), new Pokemon(ctx.getString(R.string.name_minun), 312, 335, Type.ELECTRIC, Type.NONE, abilities, 60, 40, 50, 75, 85, 95));
p = perName.get(ctx.getString(R.string.name_minun));
p.evolutions = null;
p.catchRate = 200;
p.weight = 4.2f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MOLD_BREAKER);}};
perName.put(ctx.getString(R.string.name_mega_gyarados), new Pokemon(ctx.getString(R.string.name_mega_gyarados), 130, 139, Type.WATER, Type.DARK, abilities, 95, 155, 109, 70, 130, 81));
p = perName.get(ctx.getString(R.string.name_mega_gyarados));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_magikarp)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_gyarados)), new HashMap<String, EvolutionNode>(){{this.put("Leviatorite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_gyarados)), null));}}));}});
p.catchRate = -1;
p.weight = 305.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 6.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.DROUGHT);}};
perName.put(ctx.getString(R.string.name_mega_charizard_y), new Pokemon(ctx.getString(R.string.name_mega_charizard_y), 6, 9, Type.FIRE, Type.FLYING, abilities, 78, 104, 78, 159, 115, 100));
p = perName.get(ctx.getString(R.string.name_mega_charizard_y));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_charmander)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_charmeleon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_charizard)), new HashMap<String, EvolutionNode>(){{this.put("Dracaufite X", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_charizard_x)), null));this.put("Dracaufite Y", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_charizard_y)), null));}}));}}));}});
p.catchRate = -1;
p.weight = 100.5f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HYDRATION);this.add(Ability.SAP_SIPPER);this.add(Ability.GOOEY);}};
perName.put(ctx.getString(R.string.name_sliggoo), new Pokemon(ctx.getString(R.string.name_sliggoo), 705, 752, Type.DRAGON, Type.NONE, abilities, 50, 70, 50, 90, 120, 65));
p = perName.get(ctx.getString(R.string.name_sliggoo));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_goomy)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_sliggoo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "50, quand il pleut", new EvolutionNode(perName.get(ctx.getString(R.string.name_goodra)), null));}}));}});
p.catchRate = -1;
p.weight = 17.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.IRON_FIST);}};
perName.put(ctx.getString(R.string.name_chimchar), new Pokemon(ctx.getString(R.string.name_chimchar), 390, 418, Type.FIRE, Type.NONE, abilities, 44, 58, 44, 58, 44, 61));
p = perName.get(ctx.getString(R.string.name_chimchar));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_chimchar)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "14", new EvolutionNode(perName.get(ctx.getString(R.string.name_monferno)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_infernape)), null));}}));}});
p.catchRate = 45;
p.weight = 6.2f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.HUMANLIKE};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.THICK_FAT);}};
perName.put(ctx.getString(R.string.name_tepig), new Pokemon(ctx.getString(R.string.name_tepig), 498, 538, Type.FIRE, Type.NONE, abilities, 65, 63, 45, 45, 45, 45));
p = perName.get(ctx.getString(R.string.name_tepig));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tepig)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "17", new EvolutionNode(perName.get(ctx.getString(R.string.name_pignite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_emboar)), null));}}));}});
p.catchRate = 45;
p.weight = 9.9f;
p.hatch = 5355;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STEADFAST);}};
perName.put(ctx.getString(R.string.name_gallade), new Pokemon(ctx.getString(R.string.name_gallade), 475, 508, Type.PSYCHIC, Type.FIGHTING, abilities, 68, 125, 65, 65, 115, 80));
p = perName.get(ctx.getString(R.string.name_gallade));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_ralts)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_kirlia)), new HashMap<String, EvolutionNode>(){{this.put("Male + Pierre Aube", new EvolutionNode(perName.get(ctx.getString(R.string.name_gallade)), null));this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_gardevoir)), new HashMap<String, EvolutionNode>(){{this.put("Gardevoirite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_gardevoir)), null));}}));}}));}});
p.catchRate = 60;
p.weight = 52.0f;
p.hatch = 5120;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GLUTTONY);this.add(Ability.TORRENT);}};
perName.put(ctx.getString(R.string.name_panpour), new Pokemon(ctx.getString(R.string.name_panpour), 515, 555, Type.WATER, Type.NONE, abilities, 50, 53, 48, 53, 48, 64));
p = perName.get(ctx.getString(R.string.name_panpour));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_panpour)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_simipour)), null));}});
p.catchRate = 190;
p.weight = 13.5f;
p.hatch = 5355;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MOLD_BREAKER);this.add(Ability.IRON_FIST);this.add(Ability.SCRAPPY);}};
perName.put(ctx.getString(R.string.name_pancham), new Pokemon(ctx.getString(R.string.name_pancham), 674, 720, Type.FIGHTING, Type.NONE, abilities, 67, 82, 62, 46, 48, 43));
p = perName.get(ctx.getString(R.string.name_pancham));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pancham)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32, en ayant un Pokemon dans l'equipe", new EvolutionNode(perName.get(ctx.getString(R.string.name_pangoro)), null));}});
p.catchRate = -1;
p.weight = 8.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.HUMANLIKE};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HYDRATION);this.add(Ability.SAP_SIPPER);this.add(Ability.GOOEY);}};
perName.put(ctx.getString(R.string.name_goodra), new Pokemon(ctx.getString(R.string.name_goodra), 706, 753, Type.DRAGON, Type.NONE, abilities, 90, 100, 70, 110, 150, 80));
p = perName.get(ctx.getString(R.string.name_goodra));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_goomy)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_sliggoo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "50, quand il pleut", new EvolutionNode(perName.get(ctx.getString(R.string.name_goodra)), null));}}));}});
p.catchRate = -1;
p.weight = 150.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.BULLETPROOF);}};
perName.put(ctx.getString(R.string.name_chesnaught), new Pokemon(ctx.getString(R.string.name_chesnaught), 652, 698, Type.GRASS, Type.FIGHTING, abilities, 88, 107, 122, 74, 75, 64));
p = perName.get(ctx.getString(R.string.name_chesnaught));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_chespin)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_quilladin)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_chesnaught)), null));}}));}});
p.catchRate = 45;
p.weight = 90.0f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(3, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLASH_FIRE);this.add(Ability.FLAME_BODY);this.add(Ability.INFILTRATOR);}};
perName.put(ctx.getString(R.string.name_lampent), new Pokemon(ctx.getString(R.string.name_lampent), 608, 649, Type.GHOST, Type.FIRE, abilities, 60, 40, 60, 95, 60, 55));
p = perName.get(ctx.getString(R.string.name_lampent));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_litwick)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "41", new EvolutionNode(perName.get(ctx.getString(R.string.name_lampent)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_chandelure)), null));}}));}});
p.catchRate = 190;
p.weight = 13.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.JUSTIFIED);}};
perName.put(ctx.getString(R.string.name_virizion), new Pokemon(ctx.getString(R.string.name_virizion), 640, 681, Type.GRASS, Type.FIGHTING, abilities, 91, 90, 72, 90, 129, 108));
p = perName.get(ctx.getString(R.string.name_virizion));
p.evolutions = null;
p.catchRate = 5;
p.weight = 200.0f;
p.hatch = 5355;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RUN_AWAY);this.add(Ability.KEEN_EYE);this.add(Ability.FRISK);}};
perName.put(ctx.getString(R.string.name_sentret), new Pokemon(ctx.getString(R.string.name_sentret), 161, 173, Type.NORMAL, Type.NONE, abilities, 35, 46, 34, 35, 45, 20));
p = perName.get(ctx.getString(R.string.name_sentret));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_sentret)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "15", new EvolutionNode(perName.get(ctx.getString(R.string.name_furret)), null));}});
p.catchRate = 255;
p.weight = 6.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NATURAL_CURE);this.add(Ability.FRISK);this.add(Ability.HARVEST);}};
perName.put(ctx.getString(R.string.name_trevenant), new Pokemon(ctx.getString(R.string.name_trevenant), 709, 756, Type.GHOST, Type.GRASS, abilities, 85, 110, 76, 65, 82, 56));
p = perName.get(ctx.getString(R.string.name_trevenant));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_phantump)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_trevenant)), null));}});
p.catchRate = -1;
p.weight = 71f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS,EggGroup.UNKNOWN};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHED_SKIN);this.add(Ability.INFILTRATOR);}};
perName.put(ctx.getString(R.string.name_seviper), new Pokemon(ctx.getString(R.string.name_seviper), 336, 359, Type.POISON, Type.NONE, abilities, 73, 100, 60, 100, 60, 65));
p = perName.get(ctx.getString(R.string.name_seviper));
p.evolutions = null;
p.catchRate = 90;
p.weight = 52.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.DRAGON};
p.size = 2.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.LEAF_GUARD);}};
perName.put(ctx.getString(R.string.name_chikorita), new Pokemon(ctx.getString(R.string.name_chikorita), 152, 164, Type.GRASS, Type.NONE, abilities, 45, 49, 65, 49, 65, 45));
p = perName.get(ctx.getString(R.string.name_chikorita));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_chikorita)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_bayleef)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_meganium)), null));}}));}});
p.catchRate = 45;
p.weight = 6.4f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.GRASS};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.VITAL_SPIRIT);this.add(Ability.PICKUP);this.add(Ability.RUN_AWAY);}};
perName.put(ctx.getString(R.string.name_lillipup), new Pokemon(ctx.getString(R.string.name_lillipup), 506, 546, Type.NORMAL, Type.NONE, abilities, 45, 60, 45, 25, 45, 55));
p = perName.get(ctx.getString(R.string.name_lillipup));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_lillipup)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_herdier)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_stoutland)), null));}}));}});
p.catchRate = 255;
p.weight = 4.1f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.FLASH_FIRE);}};
perName.put(ctx.getString(R.string.name_typhlosion), new Pokemon(ctx.getString(R.string.name_typhlosion), 157, 169, Type.FIRE, Type.NONE, abilities, 78, 84, 78, 109, 85, 100));
p = perName.get(ctx.getString(R.string.name_typhlosion));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cyndaquil)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "14", new EvolutionNode(perName.get(ctx.getString(R.string.name_quilava)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_typhlosion)), null));}}));}});
p.catchRate = 45;
p.weight = 79.5f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_FORCE);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_landorus_incarnate_forme), new Pokemon(ctx.getString(R.string.name_landorus_incarnate_forme), 645, 688, Type.GROUND, Type.FLYING, abilities, 89, 125, 90, 115, 80, 101));
p = perName.get(ctx.getString(R.string.name_landorus_incarnate_forme));
p.evolutions = null;
p.catchRate = 3;
p.weight = 68.0f;
p.hatch = 30855;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLASH_FIRE);this.add(Ability.DROUGHT);}};
perName.put(ctx.getString(R.string.name_ninetales), new Pokemon(ctx.getString(R.string.name_ninetales), 38, 42, Type.FIRE, Type.NONE, abilities, 73, 76, 75, 81, 100, 100));
p = perName.get(ctx.getString(R.string.name_ninetales));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_vulpix)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Feu", new EvolutionNode(perName.get(ctx.getString(R.string.name_ninetales)), null));}});
p.catchRate = 75;
p.weight = 19.9f;
p.hatch = 5120;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MAGNET_PULL);this.add(Ability.STURDY);this.add(Ability.ANALYTIC);}};
perName.put(ctx.getString(R.string.name_magnemite), new Pokemon(ctx.getString(R.string.name_magnemite), 81, 86, Type.ELECTRIC, Type.STEEL, abilities, 25, 35, 70, 95, 55, 45));
p = perName.get(ctx.getString(R.string.name_magnemite));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_magnemite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_magneton)), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau dans un lieu indique", new EvolutionNode(perName.get(ctx.getString(R.string.name_magnezone)), null));}}));}});
p.catchRate = 190;
p.weight = 6.0f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.JUSTIFIED);}};
perName.put(ctx.getString(R.string.name_cobalion), new Pokemon(ctx.getString(R.string.name_cobalion), 638, 679, Type.STEEL, Type.FIGHTING, abilities, 91, 90, 129, 90, 72, 108));
p = perName.get(ctx.getString(R.string.name_cobalion));
p.evolutions = null;
p.catchRate = 3;
p.weight = 250f;
p.hatch = 20655;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LIMBER);this.add(Ability.TECHNICIAN);this.add(Ability.UNNERVE);}};
perName.put(ctx.getString(R.string.name_persian), new Pokemon(ctx.getString(R.string.name_persian), 53, 57, Type.NORMAL, Type.NONE, abilities, 65, 70, 60, 65, 65, 115));
p = perName.get(ctx.getString(R.string.name_persian));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_meowth)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "28", new EvolutionNode(perName.get(ctx.getString(R.string.name_persian)), null));}});
p.catchRate = 90;
p.weight = 32.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.POISON_POINT);this.add(Ability.RIVALRY);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_nidoking), new Pokemon(ctx.getString(R.string.name_nidoking), 34, 38, Type.POISON, Type.GROUND, abilities, 81, 92, 77, 85, 75, 85));
p = perName.get(ctx.getString(R.string.name_nidoking));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_nidoran_m)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_nidorino)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get(ctx.getString(R.string.name_nidoking)), null));}}));}});
p.catchRate = 45;
p.weight = 62.0f;
p.hatch = 5120;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.FIELD};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SPEED_BOOST);this.add(Ability.INFILTRATOR);}};
perName.put(ctx.getString(R.string.name_ninjask), new Pokemon(ctx.getString(R.string.name_ninjask), 291, 310, Type.BUG, Type.FLYING, abilities, 61, 90, 45, 50, 50, 160));
p = perName.get(ctx.getString(R.string.name_ninjask));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_nincada)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_ninjask)), null));this.put(ctx.getString(R.string.level) + "20, emplacement libre et Poke Ball dans l'inventaire", new EvolutionNode(perName.get(ctx.getString(R.string.name_shedinja)), null));}});
p.catchRate = 120;
p.weight = 12.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.PROTEAN);}};
perName.put(ctx.getString(R.string.name_greninja), new Pokemon(ctx.getString(R.string.name_greninja), 658, 704, Type.WATER, Type.DARK, abilities, 72, 95, 67, 103, 71, 122));
p = perName.get(ctx.getString(R.string.name_greninja));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_froakie)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_frogadier)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_greninja)), null));}}));}});
p.catchRate = 45;
p.weight = 40.0f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(3, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RIVALRY);this.add(Ability.UNNERVE);this.add(Ability.MOXIE);}};
perName.put(ctx.getString(R.string.name_pyroar), new Pokemon(ctx.getString(R.string.name_pyroar), 668, 714, Type.FIRE, Type.NORMAL, abilities, 86, 68, 72, 109, 66, 106));
p = perName.get(ctx.getString(R.string.name_pyroar));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_litleo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_pyroar)), null));}});
p.catchRate = -1;
p.weight = 81.5f;
p.hatch = -1;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RUN_AWAY);this.add(Ability.QUICK_FEET);this.add(Ability.RATTLED);}};
perName.put(ctx.getString(R.string.name_poochyena), new Pokemon(ctx.getString(R.string.name_poochyena), 261, 279, Type.DARK, Type.NONE, abilities, 35, 55, 35, 30, 30, 35));
p = perName.get(ctx.getString(R.string.name_poochyena));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_poochyena)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_mightyena)), null));}});
p.catchRate = 255;
p.weight = 13.6f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RUN_AWAY);this.add(Ability.ADAPTABILITY);this.add(Ability.ANTICIPATION);}};
perName.put(ctx.getString(R.string.name_eevee), new Pokemon(ctx.getString(R.string.name_eevee), 133, 142, Type.NORMAL, Type.NONE, abilities, 55, 55, 50, 45, 65, 55));
p = perName.get(ctx.getString(R.string.name_eevee));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_eevee)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get(ctx.getString(R.string.name_jolteon)), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_leafeon)), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get(ctx.getString(R.string.name_espeon)), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get(ctx.getString(R.string.name_sylveon)), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_vaporeon)), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_glaceon)), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get(ctx.getString(R.string.name_flareon)), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_umbreon)), null));}});
p.catchRate = 45;
p.weight = 6.5f;
p.hatch = 8960;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OBLIVIOUS);this.add(Ability.ANTICIPATION);this.add(Ability.HYDRATION);}};
perName.put(ctx.getString(R.string.name_barboach), new Pokemon(ctx.getString(R.string.name_barboach), 339, 362, Type.WATER, Type.GROUND, abilities, 50, 48, 43, 46, 41, 60));
p = perName.get(ctx.getString(R.string.name_barboach));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_barboach)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_whiscash)), null));}});
p.catchRate = 190;
p.weight = 1.9f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER2};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.BATTLE_ARMOR);this.add(Ability.WEAK_ARMOR);}};
perName.put(ctx.getString(R.string.name_kabuto), new Pokemon(ctx.getString(R.string.name_kabuto), 140, 149, Type.ROCK, Type.WATER, abilities, 30, 80, 90, 55, 45, 55));
p = perName.get(ctx.getString(R.string.name_kabuto));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_kabuto)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_kabutops)), null));}});
p.catchRate = 45;
p.weight = 11.5f;
p.hatch = 7680;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER3};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.PROTEAN);}};
perName.put(ctx.getString(R.string.name_froakie), new Pokemon(ctx.getString(R.string.name_froakie), 656, 702, Type.WATER, Type.NONE, abilities, 37, 53, 49, 66, 50, 70));
p = perName.get(ctx.getString(R.string.name_froakie));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_froakie)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_frogadier)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_greninja)), null));}}));}});
p.catchRate = 45;
p.weight = 7.0f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_claydol), new Pokemon(ctx.getString(R.string.name_claydol), 344, 367, Type.GROUND, Type.PSYCHIC, abilities, 60, 70, 105, 70, 120, 75));
p = perName.get(ctx.getString(R.string.name_claydol));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_baltoy)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_claydol)), null));}});
p.catchRate = 90;
p.weight = 108.0f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GUTS);this.add(Ability.STEADFAST);this.add(Ability.VITAL_SPIRIT);}};
perName.put(ctx.getString(R.string.name_tyrogue), new Pokemon(ctx.getString(R.string.name_tyrogue), 236, 252, Type.FIGHTING, Type.NONE, abilities, 35, 35, 35, 35, 35, 35));
p = perName.get(ctx.getString(R.string.name_tyrogue));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tyrogue)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20, Attaque < Defense", new EvolutionNode(perName.get(ctx.getString(R.string.name_hitmonchan)), null));this.put(ctx.getString(R.string.level) + "20, Attaque > Defense", new EvolutionNode(perName.get(ctx.getString(R.string.name_hitmonlee)), null));this.put(ctx.getString(R.string.level) + "20, Attaque et Defense identiques", new EvolutionNode(perName.get(ctx.getString(R.string.name_hitmontop)), null));}});
p.catchRate = 75;
p.weight = 21.0f;
p.hatch = 6400;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.COMPOUNDEYE);}};
perName.put(ctx.getString(R.string.name_nincada), new Pokemon(ctx.getString(R.string.name_nincada), 290, 309, Type.BUG, Type.GROUND, abilities, 31, 45, 90, 30, 30, 40));
p = perName.get(ctx.getString(R.string.name_nincada));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_nincada)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_ninjask)), null));this.put(ctx.getString(R.string.level) + "20, emplacement libre et Poke Ball dans l'inventaire", new EvolutionNode(perName.get(ctx.getString(R.string.name_shedinja)), null));}});
p.catchRate = 255;
p.weight = 5.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.TECHNICIAN);this.add(Ability.SKILL_LINK);}};
perName.put(ctx.getString(R.string.name_ambipom), new Pokemon(ctx.getString(R.string.name_ambipom), 424, 454, Type.NORMAL, Type.NONE, abilities, 75, 100, 66, 60, 66, 115));
p = perName.get(ctx.getString(R.string.name_ambipom));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_aipom)), new HashMap<String, EvolutionNode>(){{this.put("En connaissant l'attaque Coup Double + passer un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_ambipom)), null));}});
p.catchRate = 45;
p.weight = 20.3f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PLUS);this.add(Ability.MINUS);this.add(Ability.CLEAR_BODY);}};
perName.put(ctx.getString(R.string.name_klink), new Pokemon(ctx.getString(R.string.name_klink), 599, 640, Type.STEEL, Type.NONE, abilities, 40, 55, 70, 45, 60, 30));
p = perName.get(ctx.getString(R.string.name_klink));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_klink)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "38", new EvolutionNode(perName.get(ctx.getString(R.string.name_klang)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "49", new EvolutionNode(perName.get(ctx.getString(R.string.name_klinklang)), null));}}));}});
p.catchRate = 130;
p.weight = 21.0f;
p.hatch = 5355;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.KEEN_EYE);this.add(Ability.SNIPER);}};
perName.put(ctx.getString(R.string.name_spearow), new Pokemon(ctx.getString(R.string.name_spearow), 21, 25, Type.NORMAL, Type.FLYING, abilities, 40, 60, 30, 31, 31, 70));
p = perName.get(ctx.getString(R.string.name_spearow));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_spearow)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_fearow)), null));}});
p.catchRate = 255;
p.weight = 2.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MAGMA_ARMOR);this.add(Ability.SOLID_ROCK);this.add(Ability.ANGER_POINT);}};
perName.put(ctx.getString(R.string.name_camerupt), new Pokemon(ctx.getString(R.string.name_camerupt), 323, 346, Type.FIRE, Type.GROUND, abilities, 70, 100, 70, 105, 75, 40));
p = perName.get(ctx.getString(R.string.name_camerupt));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_numel)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "33", new EvolutionNode(perName.get(ctx.getString(R.string.name_camerupt)), null));}});
p.catchRate = 150;
p.weight = 220.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.KEEN_EYE);this.add(Ability.RAIN_DISH);}};
perName.put(ctx.getString(R.string.name_wingull), new Pokemon(ctx.getString(R.string.name_wingull), 278, 296, Type.WATER, Type.FLYING, abilities, 40, 30, 30, 55, 30, 85));
p = perName.get(ctx.getString(R.string.name_wingull));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_wingull)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_pelipper)), null));}});
p.catchRate = 190;
p.weight = 9.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FLYING};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLASH_FIRE);this.add(Ability.FLAME_BODY);this.add(Ability.SHADOW_TAG);}};
perName.put(ctx.getString(R.string.name_litwick), new Pokemon(ctx.getString(R.string.name_litwick), 607, 648, Type.GHOST, Type.FIRE, abilities, 50, 30, 55, 65, 55, 20));
p = perName.get(ctx.getString(R.string.name_litwick));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_litwick)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "41", new EvolutionNode(perName.get(ctx.getString(R.string.name_lampent)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_chandelure)), null));}}));}});
p.catchRate = 190;
p.weight = 3.1f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SNIPER);this.add(Ability.TOUGH_CLAWS);this.add(Ability.PICKPOCKET);}};
perName.put(ctx.getString(R.string.name_barbaracle), new Pokemon(ctx.getString(R.string.name_barbaracle), 689, 736, Type.ROCK, Type.WATER, abilities, 70, 115, 115, 50, 100, 80));
p = perName.get(ctx.getString(R.string.name_barbaracle));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_binacle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "39", new EvolutionNode(perName.get(ctx.getString(R.string.name_barbaracle)), null));}});
p.catchRate = -1;
p.weight = 96.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER3,EggGroup.WATER1};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TURBOBLAZE);}};
perName.put(ctx.getString(R.string.name_reshiram), new Pokemon(ctx.getString(R.string.name_reshiram), 643, 686, Type.DRAGON, Type.FIRE, abilities, 100, 120, 100, 150, 120, 90));
p = perName.get(ctx.getString(R.string.name_reshiram));
p.evolutions = null;
p.catchRate = 45;
p.weight = 330f;
p.hatch = 30855;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 3.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OBLIVIOUS);this.add(Ability.OWN_TEMPO);this.add(Ability.CLOUD_NINE);}};
perName.put(ctx.getString(R.string.name_lickitung), new Pokemon(ctx.getString(R.string.name_lickitung), 108, 114, Type.NORMAL, Type.NONE, abilities, 90, 55, 75, 60, 75, 30));
p = perName.get(ctx.getString(R.string.name_lickitung));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_lickitung)), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l'attaque Roulade", new EvolutionNode(perName.get(ctx.getString(R.string.name_lickilicky)), null));}});
p.catchRate = 45;
p.weight = 65.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.WATER_ABSORB);this.add(Ability.DAMP);this.add(Ability.SWIFT_SWIM);}};
perName.put(ctx.getString(R.string.name_poliwhirl), new Pokemon(ctx.getString(R.string.name_poliwhirl), 61, 65, Type.WATER, Type.NONE, abilities, 65, 65, 65, 50, 50, 90));
p = perName.get(ctx.getString(R.string.name_poliwhirl));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_poliwag)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_poliwhirl)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Roche Royale", new EvolutionNode(perName.get(ctx.getString(R.string.name_politoed)), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_poliwrath)), null));}}));}});
p.catchRate = 120;
p.weight = 20.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHADOW_TAG);}};
perName.put(ctx.getString(R.string.name_mega_gengar), new Pokemon(ctx.getString(R.string.name_mega_gengar), 94, 100, Type.GHOST, Type.POISON, abilities, 60, 65, 80, 170, 95, 130));
p = perName.get(ctx.getString(R.string.name_mega_gengar));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_gastly)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_haunter)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_gengar)), new HashMap<String, EvolutionNode>(){{this.put("Ectoplasmite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_gengar)), null));}}));}}));}});
p.catchRate = -1;
p.weight = 40.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MEGA_LAUNCHER);}};
perName.put(ctx.getString(R.string.name_clauncher), new Pokemon(ctx.getString(R.string.name_clauncher), 692, 739, Type.WATER, Type.NONE, abilities, 50, 53, 62, 58, 63, 44));
p = perName.get(ctx.getString(R.string.name_clauncher));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_clauncher)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_clawitzer)), null));}});
p.catchRate = -1;
p.weight = 8.3f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER3};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_feraligatr), new Pokemon(ctx.getString(R.string.name_feraligatr), 160, 172, Type.WATER, Type.NONE, abilities, 85, 105, 100, 79, 83, 78));
p = perName.get(ctx.getString(R.string.name_feraligatr));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_totodile)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_croconaw)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_feraligatr)), null));}}));}});
p.catchRate = 45;
p.weight = 88.8f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.MONSTER};
p.size = 2.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_mismagius), new Pokemon(ctx.getString(R.string.name_mismagius), 429, 459, Type.GHOST, Type.NONE, abilities, 60, 60, 60, 105, 105, 105));
p = perName.get(ctx.getString(R.string.name_mismagius));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_misdreavus)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_mismagius)), null));}});
p.catchRate = 45;
p.weight = 4.4f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RIVALRY);this.add(Ability.INTIMIDATE);this.add(Ability.GUTS);}};
perName.put(ctx.getString(R.string.name_luxray), new Pokemon(ctx.getString(R.string.name_luxray), 405, 433, Type.ELECTRIC, Type.NONE, abilities, 80, 120, 79, 95, 79, 70));
p = perName.get(ctx.getString(R.string.name_luxray));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_shinx)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "15", new EvolutionNode(perName.get(ctx.getString(R.string.name_luxio)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_luxray)), null));}}));}});
p.catchRate = 45;
p.weight = 42.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.HYDRATION);}};
perName.put(ctx.getString(R.string.name_gorebyss), new Pokemon(ctx.getString(R.string.name_gorebyss), 368, 393, Type.WATER, Type.NONE, abilities, 55, 84, 105, 114, 75, 52));
p = perName.get(ctx.getString(R.string.name_gorebyss));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_clamperl)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant une Ecaille Ocean", new EvolutionNode(perName.get(ctx.getString(R.string.name_gorebyss)), null));this.put("Echange en tenant une Dent Ocean", new EvolutionNode(perName.get(ctx.getString(R.string.name_huntail)), null));}});
p.catchRate = 60;
p.weight = 22.6f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.ROCK_HEAD);this.add(Ability.HEAVY_METAL);}};
perName.put(ctx.getString(R.string.name_aron), new Pokemon(ctx.getString(R.string.name_aron), 304, 324, Type.STEEL, Type.ROCK, abilities, 50, 70, 100, 40, 40, 30));
p = perName.get(ctx.getString(R.string.name_aron));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_aron)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_lairon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "42", new EvolutionNode(perName.get(ctx.getString(R.string.name_aggron)), new HashMap<String, EvolutionNode>(){{this.put("Galekingite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_aggron)), null));}}));}}));}});
p.catchRate = 180;
p.weight = 60.0f;
p.hatch = 8960;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ROCK_HEAD);this.add(Ability.PRESSURE);this.add(Ability.UNNERVE);}};
perName.put(ctx.getString(R.string.name_aerodactyl), new Pokemon(ctx.getString(R.string.name_aerodactyl), 142, 151, Type.ROCK, Type.FLYING, abilities, 80, 105, 65, 60, 75, 130));
p = perName.get(ctx.getString(R.string.name_aerodactyl));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_aerodactyl)), null);
p.catchRate = 45;
p.weight = 59.0f;
p.hatch = 8960;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RUN_AWAY);this.add(Ability.FLASH_FIRE);this.add(Ability.FLAME_BODY);}};
perName.put(ctx.getString(R.string.name_rapidash), new Pokemon(ctx.getString(R.string.name_rapidash), 78, 83, Type.FIRE, Type.NONE, abilities, 65, 100, 70, 80, 80, 105));
p = perName.get(ctx.getString(R.string.name_rapidash));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_ponyta)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_rapidash)), null));}});
p.catchRate = 60;
p.weight = 95.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OBLIVIOUS);this.add(Ability.OWN_TEMPO);this.add(Ability.REGENERATOR);}};
perName.put(ctx.getString(R.string.name_slowking), new Pokemon(ctx.getString(R.string.name_slowking), 199, 212, Type.WATER, Type.PSYCHIC, abilities, 95, 75, 80, 100, 110, 30));
p = perName.get(ctx.getString(R.string.name_slowking));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_slowpoke)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_slowbro)), null));this.put("Echange en tenant Roche Royale", new EvolutionNode(perName.get(ctx.getString(R.string.name_slowking)), null));}});
p.catchRate = 70;
p.weight = 79.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.WATER1};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SERENE_GRACE);}};
perName.put(ctx.getString(R.string.name_jirachi), new Pokemon(ctx.getString(R.string.name_jirachi), 385, 410, Type.STEEL, Type.PSYCHIC, abilities, 100, 100, 100, 100, 100, 100));
p = perName.get(ctx.getString(R.string.name_jirachi));
p.evolutions = null;
p.catchRate = 3;
p.weight = 1.1f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.FRISK);this.add(Ability.INSOMNIA);}};
perName.put(ctx.getString(R.string.name_pumpkaboo_small_size), new Pokemon(ctx.getString(R.string.name_pumpkaboo_small_size), 710, 757, Type.GHOST, Type.GRASS, abilities, 44, 66, 70, 44, 55, 56));
p = perName.get(ctx.getString(R.string.name_pumpkaboo_small_size));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pumpkaboo_small_size)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_gourgeist_small_size)), null));}});
p.catchRate = -1;
p.weight = 3.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.BULLETPROOF);}};
perName.put(ctx.getString(R.string.name_chespin), new Pokemon(ctx.getString(R.string.name_chespin), 650, 696, Type.GRASS, Type.NONE, abilities, 56, 64, 66, 50, 45, 38));
p = perName.get(ctx.getString(R.string.name_chespin));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_chespin)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_quilladin)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_chesnaught)), null));}}));}});
p.catchRate = 45;
p.weight = 9.0f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.MOXIE);this.add(Ability.ANGER_POINT);}};
perName.put(ctx.getString(R.string.name_sandile), new Pokemon(ctx.getString(R.string.name_sandile), 551, 591, Type.GROUND, Type.DARK, abilities, 50, 72, 35, 35, 35, 65));
p = perName.get(ctx.getString(R.string.name_sandile));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_sandile)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "29", new EvolutionNode(perName.get(ctx.getString(R.string.name_krokorok)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_krookodile)), null));}}));}});
p.catchRate = 180;
p.weight = 15.2f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.RAIN_DISH);}};
perName.put(ctx.getString(R.string.name_squirtle), new Pokemon(ctx.getString(R.string.name_squirtle), 7, 10, Type.WATER, Type.NONE, abilities, 44, 48, 65, 50, 64, 43));
p = perName.get(ctx.getString(R.string.name_squirtle));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_squirtle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_wartortle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_blastoise)), new HashMap<String, EvolutionNode>(){{this.put("Tortankite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_blastoise)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 9.0f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.MONSTER};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.IMMUNITY);this.add(Ability.TOXIC_BOOST);}};
perName.put(ctx.getString(R.string.name_zangoose), new Pokemon(ctx.getString(R.string.name_zangoose), 335, 358, Type.NORMAL, Type.NONE, abilities, 73, 115, 60, 60, 60, 90));
p = perName.get(ctx.getString(R.string.name_zangoose));
p.evolutions = null;
p.catchRate = 90;
p.weight = 40.3f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_latias), new Pokemon(ctx.getString(R.string.name_latias), 380, 405, Type.DRAGON, Type.PSYCHIC, abilities, 80, 80, 90, 110, 130, 110));
p = perName.get(ctx.getString(R.string.name_latias));
p.evolutions = null;
p.catchRate = 3;
p.weight = 40.0f;
p.hatch = 30720;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.QUICK_FEET);this.add(Ability.MOXIE);}};
perName.put(ctx.getString(R.string.name_mightyena), new Pokemon(ctx.getString(R.string.name_mightyena), 262, 280, Type.DARK, Type.NONE, abilities, 70, 90, 70, 60, 60, 70));
p = perName.get(ctx.getString(R.string.name_mightyena));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_poochyena)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_mightyena)), null));}});
p.catchRate = 127;
p.weight = 37.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);this.add(Ability.MULTISCALE);}};
perName.put(ctx.getString(R.string.name_lugia), new Pokemon(ctx.getString(R.string.name_lugia), 249, 266, Type.PSYCHIC, Type.FLYING, abilities, 106, 90, 130, 90, 154, 110));
p = perName.get(ctx.getString(R.string.name_lugia));
p.evolutions = null;
p.catchRate = 3;
p.weight = 216.0f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 5.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ROCK_HEAD);this.add(Ability.STURDY);this.add(Ability.WEAK_ARMOR);}};
perName.put(ctx.getString(R.string.name_onix), new Pokemon(ctx.getString(R.string.name_onix), 95, 101, Type.ROCK, Type.GROUND, abilities, 35, 45, 160, 30, 45, 70));
p = perName.get(ctx.getString(R.string.name_onix));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_onix)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Peau Metal", new EvolutionNode(perName.get(ctx.getString(R.string.name_steelix)), null));}});
p.catchRate = 45;
p.weight = 210.0f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 8.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLASH_FIRE);this.add(Ability.GUTS);}};
perName.put(ctx.getString(R.string.name_flareon), new Pokemon(ctx.getString(R.string.name_flareon), 136, 145, Type.FIRE, Type.NONE, abilities, 65, 130, 60, 95, 110, 65));
p = perName.get(ctx.getString(R.string.name_flareon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_eevee)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get(ctx.getString(R.string.name_jolteon)), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_leafeon)), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get(ctx.getString(R.string.name_espeon)), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get(ctx.getString(R.string.name_sylveon)), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_vaporeon)), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_glaceon)), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get(ctx.getString(R.string.name_flareon)), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_umbreon)), null));}});
p.catchRate = 45;
p.weight = 25.9f;
p.hatch = 8960;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MAGNET_PULL);this.add(Ability.STURDY);this.add(Ability.ANALYTIC);}};
perName.put(ctx.getString(R.string.name_magneton), new Pokemon(ctx.getString(R.string.name_magneton), 82, 87, Type.ELECTRIC, Type.STEEL, abilities, 50, 60, 95, 120, 70, 70));
p = perName.get(ctx.getString(R.string.name_magneton));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_magnemite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_magneton)), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau dans un lieu indique", new EvolutionNode(perName.get(ctx.getString(R.string.name_magnezone)), null));}}));}});
p.catchRate = 60;
p.weight = 60.0f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RIVALRY);this.add(Ability.MOLD_BREAKER);this.add(Ability.UNNERVE);}};
perName.put(ctx.getString(R.string.name_fraxure), new Pokemon(ctx.getString(R.string.name_fraxure), 611, 652, Type.DRAGON, Type.DRAGON, abilities, 66, 117, 70, 40, 50, 67));
p = perName.get(ctx.getString(R.string.name_fraxure));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_axew)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "38", new EvolutionNode(perName.get(ctx.getString(R.string.name_fraxure)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "48", new EvolutionNode(perName.get(ctx.getString(R.string.name_haxorus)), null));}}));}});
p.catchRate = 60;
p.weight = 36.0f;
p.hatch = 10455;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.DRAGON};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHELL_ARMOR);this.add(Ability.SKILL_LINK);this.add(Ability.OVERCOAT);}};
perName.put(ctx.getString(R.string.name_shellder), new Pokemon(ctx.getString(R.string.name_shellder), 90, 95, Type.WATER, Type.NONE, abilities, 30, 65, 100, 45, 25, 40));
p = perName.get(ctx.getString(R.string.name_shellder));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_shellder)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_cloyster)), null));}});
p.catchRate = 190;
p.weight = 4.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER3};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ROCK_HEAD);this.add(Ability.STURDY);this.add(Ability.SAND_VEIL);}};
perName.put(ctx.getString(R.string.name_geodude), new Pokemon(ctx.getString(R.string.name_geodude), 74, 79, Type.ROCK, Type.GROUND, abilities, 40, 80, 100, 30, 30, 20));
p = perName.get(ctx.getString(R.string.name_geodude));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_geodude)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_graveler)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_golem)), null));}}));}});
p.catchRate = 255;
p.weight = 20.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HYPER_CUTTER);this.add(Ability.SHELL_ARMOR);this.add(Ability.ADAPTABILITY);}};
perName.put(ctx.getString(R.string.name_crawdaunt), new Pokemon(ctx.getString(R.string.name_crawdaunt), 342, 365, Type.WATER, Type.DARK, abilities, 63, 120, 85, 90, 55, 55));
p = perName.get(ctx.getString(R.string.name_crawdaunt));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_corphish)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_crawdaunt)), null));}});
p.catchRate = 255;
p.weight = 32.8f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER3};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHIELD_DUST);}};
perName.put(ctx.getString(R.string.name_dustox), new Pokemon(ctx.getString(R.string.name_dustox), 269, 287, Type.BUG, Type.POISON, abilities, 60, 50, 70, 50, 90, 65));
p = perName.get(ctx.getString(R.string.name_dustox));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_wurmple)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "10", new EvolutionNode(perName.get(ctx.getString(R.string.name_dustox)), null));this.put(ctx.getString(R.string.level) + "7, au hasard", new EvolutionNode(perName.get(ctx.getString(R.string.name_cascoon)), null));}});
p.catchRate = 45;
p.weight = 31.6f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HYDRATION);}};
perName.put(ctx.getString(R.string.name_manaphy), new Pokemon(ctx.getString(R.string.name_manaphy), 490, 529, Type.WATER, Type.NONE, abilities, 100, 100, 100, 100, 100, 100));
p = perName.get(ctx.getString(R.string.name_manaphy));
p.evolutions = null;
p.catchRate = 3;
p.weight = 1.4f;
p.hatch = 2560;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FAIRY};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_croconaw), new Pokemon(ctx.getString(R.string.name_croconaw), 159, 171, Type.WATER, Type.NONE, abilities, 65, 80, 80, 59, 63, 58));
p = perName.get(ctx.getString(R.string.name_croconaw));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_totodile)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_croconaw)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_feraligatr)), null));}}));}});
p.catchRate = 45;
p.weight = 25.0f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.WATER1};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_gengar), new Pokemon(ctx.getString(R.string.name_gengar), 94, 99, Type.GHOST, Type.POISON, abilities, 60, 65, 60, 130, 75, 110));
p = perName.get(ctx.getString(R.string.name_gengar));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_gastly)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_haunter)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_gengar)), new HashMap<String, EvolutionNode>(){{this.put("Ectoplasmite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_gengar)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 40.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERCOAT);this.add(Ability.MAGIC_GUARD);this.add(Ability.REGENERATOR);}};
perName.put(ctx.getString(R.string.name_solosis), new Pokemon(ctx.getString(R.string.name_solosis), 577, 618, Type.PSYCHIC, Type.NONE, abilities, 45, 30, 40, 105, 50, 20));
p = perName.get(ctx.getString(R.string.name_solosis));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_solosis)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_duosion)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "41", new EvolutionNode(perName.get(ctx.getString(R.string.name_reuniclus)), null));}}));}});
p.catchRate = 200;
p.weight = 1.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_carnivine), new Pokemon(ctx.getString(R.string.name_carnivine), 455, 487, Type.GRASS, Type.NONE, abilities, 74, 100, 72, 90, 72, 46));
p = perName.get(ctx.getString(R.string.name_carnivine));
p.evolutions = null;
p.catchRate = 200;
p.weight = 27.0f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HYPER_CUTTER);this.add(Ability.SHELL_ARMOR);this.add(Ability.ADAPTABILITY);}};
perName.put(ctx.getString(R.string.name_corphish), new Pokemon(ctx.getString(R.string.name_corphish), 341, 364, Type.WATER, Type.NONE, abilities, 43, 80, 65, 50, 35, 35));
p = perName.get(ctx.getString(R.string.name_corphish));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_corphish)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_crawdaunt)), null));}});
p.catchRate = 205;
p.weight = 11.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER3};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWARM);this.add(Ability.EARLY_BIRD);this.add(Ability.IRON_FIST);}};
perName.put(ctx.getString(R.string.name_ledian), new Pokemon(ctx.getString(R.string.name_ledian), 166, 178, Type.BUG, Type.FLYING, abilities, 55, 35, 50, 55, 110, 85));
p = perName.get(ctx.getString(R.string.name_ledian));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_ledyba)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_ledian)), null));}});
p.catchRate = 90;
p.weight = 35.6f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLASH_FIRE);this.add(Ability.FLAME_BODY);this.add(Ability.SHADOW_TAG);}};
perName.put(ctx.getString(R.string.name_chandelure), new Pokemon(ctx.getString(R.string.name_chandelure), 609, 650, Type.GHOST, Type.FIRE, abilities, 60, 55, 90, 145, 90, 80));
p = perName.get(ctx.getString(R.string.name_chandelure));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_litwick)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "41", new EvolutionNode(perName.get(ctx.getString(R.string.name_lampent)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_chandelure)), null));}}));}});
p.catchRate = 45;
p.weight = 34.3f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.WATER_ABSORB);this.add(Ability.CURSED_BODY);this.add(Ability.DAMP);}};
perName.put(ctx.getString(R.string.name_jellicent), new Pokemon(ctx.getString(R.string.name_jellicent), 593, 634, Type.WATER, Type.GHOST, abilities, 100, 60, 70, 85, 105, 60));
p = perName.get(ctx.getString(R.string.name_jellicent));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_frillish)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_jellicent)), null));}});
p.catchRate = 60;
p.weight = 135.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 2.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CUTE_CHARM);this.add(Ability.NORMALIZE);}};
perName.put(ctx.getString(R.string.name_delcatty), new Pokemon(ctx.getString(R.string.name_delcatty), 301, 320, Type.NORMAL, Type.NONE, abilities, 70, 65, 65, 55, 55, 70));
p = perName.get(ctx.getString(R.string.name_delcatty));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_skitty)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get(ctx.getString(R.string.name_delcatty)), null));}});
p.catchRate = 60;
p.weight = 32.6f;
p.hatch = 3840;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.FAIRY};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLOWER_VEIL);this.add(Ability.SYMBIOSIS);}};
perName.put(ctx.getString(R.string.name_floette), new Pokemon(ctx.getString(R.string.name_floette), 670, 716, Type.FAIRY, Type.NONE, abilities, 58, 54, 52, 90, 116, 63));
p = perName.get(ctx.getString(R.string.name_floette));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_flabebe)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "19", new EvolutionNode(perName.get(ctx.getString(R.string.name_floette)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get(ctx.getString(R.string.name_florges)), null));}}));}});
p.catchRate = -1;
p.weight = 0.9f;
p.hatch = -1;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY};
p.size = 0.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MUMMY);}};
perName.put(ctx.getString(R.string.name_cofagrigus), new Pokemon(ctx.getString(R.string.name_cofagrigus), 563, 604, Type.GHOST, Type.NONE, abilities, 58, 50, 145, 95, 105, 30));
p = perName.get(ctx.getString(R.string.name_cofagrigus));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_yamask)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "34", new EvolutionNode(perName.get(ctx.getString(R.string.name_cofagrigus)), null));}});
p.catchRate = 90;
p.weight = 76.5f;
p.hatch = 6630;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL,EggGroup.UNKNOWN};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PURE_POWER);this.add(Ability.TELEPATHY);}};
perName.put(ctx.getString(R.string.name_meditite), new Pokemon(ctx.getString(R.string.name_meditite), 307, 328, Type.FIGHTING, Type.PSYCHIC, abilities, 30, 40, 55, 40, 55, 60));
p = perName.get(ctx.getString(R.string.name_meditite));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_meditite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_medicham)), new HashMap<String, EvolutionNode>(){{this.put("Charminite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_medicham)), null));}}));}});
p.catchRate = 180;
p.weight = 11.2f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HEALER);this.add(Ability.REGENERATOR);this.add(Ability.KLUTZ);}};
perName.put(ctx.getString(R.string.name_audino), new Pokemon(ctx.getString(R.string.name_audino), 531, 571, Type.NORMAL, Type.NONE, abilities, 103, 60, 86, 60, 86, 50));
p = perName.get(ctx.getString(R.string.name_audino));
p.evolutions = null;
p.catchRate = 255;
p.weight = 31.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.MAGICIAN);}};
perName.put(ctx.getString(R.string.name_fennekin), new Pokemon(ctx.getString(R.string.name_fennekin), 653, 699, Type.FIRE, Type.NONE, abilities, 40, 45, 40, 62, 60, 60));
p = perName.get(ctx.getString(R.string.name_fennekin));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_fennekin)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_braixen)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_delphox)), null));}}));}});
p.catchRate = 45;
p.weight = 9.4f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);this.add(Ability.HEATPROOF);this.add(Ability.HEAVY_METAL);}};
perName.put(ctx.getString(R.string.name_bronzong), new Pokemon(ctx.getString(R.string.name_bronzong), 437, 467, Type.STEEL, Type.PSYCHIC, abilities, 67, 89, 116, 79, 116, 33));
p = perName.get(ctx.getString(R.string.name_bronzong));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bronzor)), new HashMap<String, EvolutionNode>(){{this.put("niveau 33", new EvolutionNode(perName.get(ctx.getString(R.string.name_bronzong)), null));}});
p.catchRate = 90;
p.weight = 187.0f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.WATER_ABSORB);this.add(Ability.DAMP);this.add(Ability.UNAWARE);}};
perName.put(ctx.getString(R.string.name_wooper), new Pokemon(ctx.getString(R.string.name_wooper), 194, 207, Type.WATER, Type.GROUND, abilities, 55, 45, 45, 25, 25, 15));
p = perName.get(ctx.getString(R.string.name_wooper));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_wooper)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_quagsire)), null));}});
p.catchRate = 255;
p.weight = 8.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.LEAF_GUARD);}};
perName.put(ctx.getString(R.string.name_bayleef), new Pokemon(ctx.getString(R.string.name_bayleef), 153, 165, Type.GRASS, Type.NONE, abilities, 60, 62, 80, 63, 80, 60));
p = perName.get(ctx.getString(R.string.name_bayleef));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_chikorita)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_bayleef)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_meganium)), null));}}));}});
p.catchRate = 45;
p.weight = 15.8f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.GRASS};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);}};
perName.put(ctx.getString(R.string.name_vileplume), new Pokemon(ctx.getString(R.string.name_vileplume), 45, 49, Type.GRASS, Type.POISON, abilities, 75, 80, 85, 100, 90, 50));
p = perName.get(ctx.getString(R.string.name_vileplume));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_oddish)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "21", new EvolutionNode(perName.get(ctx.getString(R.string.name_gloom)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get(ctx.getString(R.string.name_vileplume)), null));this.put("Avec une Pierresoleil", new EvolutionNode(perName.get(ctx.getString(R.string.name_bellossom)), null));}}));}});
p.catchRate = 45;
p.weight = 18.6f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.GLUTTONY);this.add(Ability.CONTRARY);}};
perName.put(ctx.getString(R.string.name_shuckle), new Pokemon(ctx.getString(R.string.name_shuckle), 213, 227, Type.BUG, Type.ROCK, abilities, 20, 10, 230, 10, 230, 5));
p = perName.get(ctx.getString(R.string.name_shuckle));
p.evolutions = null;
p.catchRate = 190;
p.weight = 20.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NATURAL_CURE);}};
perName.put(ctx.getString(R.string.name_shaymin_sky_forme), new Pokemon(ctx.getString(R.string.name_shaymin_sky_forme), 492, 532, Type.GRASS, Type.NONE, abilities, 100, 103, 75, 120, 75, 127));
p = perName.get(ctx.getString(R.string.name_shaymin_sky_forme));
p.evolutions = null;
p.catchRate = 45;
p.weight = 2.1f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.SAND_RUSH);this.add(Ability.SCRAPPY);}};
perName.put(ctx.getString(R.string.name_herdier), new Pokemon(ctx.getString(R.string.name_herdier), 507, 547, Type.NORMAL, Type.NONE, abilities, 65, 80, 65, 35, 65, 60));
p = perName.get(ctx.getString(R.string.name_herdier));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_lillipup)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_herdier)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_stoutland)), null));}}));}});
p.catchRate = 120;
p.weight = 14.7f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.EARLY_BIRD);this.add(Ability.PICKPOCKET);}};
perName.put(ctx.getString(R.string.name_nuzleaf), new Pokemon(ctx.getString(R.string.name_nuzleaf), 274, 292, Type.GRASS, Type.DARK, abilities, 70, 70, 40, 60, 40, 60));
p = perName.get(ctx.getString(R.string.name_nuzleaf));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_seedot)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "14", new EvolutionNode(perName.get(ctx.getString(R.string.name_nuzleaf)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get(ctx.getString(R.string.name_shiftry)), null));}}));}});
p.catchRate = 120;
p.weight = 28.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.GRASS};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CUTE_CHARM);this.add(Ability.COMPETITIVE);this.add(Ability.FRIEND_GUARD);}};
perName.put(ctx.getString(R.string.name_igglybuff), new Pokemon(ctx.getString(R.string.name_igglybuff), 174, 186, Type.NORMAL, Type.NONE, abilities, 90, 30, 15, 40, 20, 15));
p = perName.get(ctx.getString(R.string.name_igglybuff));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_igglybuff)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_jigglypuff)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get(ctx.getString(R.string.name_wigglytuff)), null));}}));}});
p.catchRate = 45;
p.weight = 1.0f;
p.hatch = 2560;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_VEIL);this.add(Ability.SAND_RUSH);}};
perName.put(ctx.getString(R.string.name_sandslash), new Pokemon(ctx.getString(R.string.name_sandslash), 28, 32, Type.GROUND, Type.NONE, abilities, 75, 100, 110, 45, 55, 65));
p = perName.get(ctx.getString(R.string.name_sandslash));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_sandshrew)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "22", new EvolutionNode(perName.get(ctx.getString(R.string.name_sandslash)), null));}});
p.catchRate = 90;
p.weight = 29.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.FRISK);this.add(Ability.INSOMNIA);}};
perName.put(ctx.getString(R.string.name_gourgeist_small_size), new Pokemon(ctx.getString(R.string.name_gourgeist_small_size), 711, 761, Type.GHOST, Type.GRASS, abilities, 55, 85, 122, 58, 75, 99));
p = perName.get(ctx.getString(R.string.name_gourgeist_small_size));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pumpkaboo_small_size)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_gourgeist_small_size)), null));}});
p.catchRate = -1;
p.weight = 9.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ROCK_HEAD);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_bagon), new Pokemon(ctx.getString(R.string.name_bagon), 371, 396, Type.DRAGON, Type.NONE, abilities, 45, 75, 60, 40, 30, 50));
p = perName.get(ctx.getString(R.string.name_bagon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bagon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_shelgon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "50", new EvolutionNode(perName.get(ctx.getString(R.string.name_salamence)), null));}}));}});
p.catchRate = 45;
p.weight = 42.1f;
p.hatch = 10240;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.AIR_LOCK);}};
perName.put(ctx.getString(R.string.name_rayquaza), new Pokemon(ctx.getString(R.string.name_rayquaza), 384, 409, Type.DRAGON, Type.FLYING, abilities, 105, 150, 90, 150, 90, 95));
p = perName.get(ctx.getString(R.string.name_rayquaza));
p.evolutions = null;
p.catchRate = 3;
p.weight = 206.5f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 7.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.LEAF_GUARD);this.add(Ability.INFILTRATOR);}};
perName.put(ctx.getString(R.string.name_hoppip), new Pokemon(ctx.getString(R.string.name_hoppip), 187, 200, Type.GRASS, Type.FLYING, abilities, 35, 35, 40, 35, 55, 50));
p = perName.get(ctx.getString(R.string.name_hoppip));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_hoppip)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_skiploom)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "27", new EvolutionNode(perName.get(ctx.getString(R.string.name_jumpluff)), null));}}));}});
p.catchRate = 255;
p.weight = 0.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY,EggGroup.GRASS};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.RIVALRY);this.add(Ability.GUTS);}};
perName.put(ctx.getString(R.string.name_luxio), new Pokemon(ctx.getString(R.string.name_luxio), 404, 432, Type.ELECTRIC, Type.NONE, abilities, 60, 85, 49, 60, 49, 60));
p = perName.get(ctx.getString(R.string.name_luxio));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_shinx)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "15", new EvolutionNode(perName.get(ctx.getString(R.string.name_luxio)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_luxray)), null));}}));}});
p.catchRate = 120;
p.weight = 30.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLOWER_GIFT);}};
perName.put(ctx.getString(R.string.name_cherrim), new Pokemon(ctx.getString(R.string.name_cherrim), 421, 451, Type.GRASS, Type.NONE, abilities, 70, 60, 70, 87, 78, 85));
p = perName.get(ctx.getString(R.string.name_cherrim));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cherubi)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_cherrim)), null));}});
p.catchRate = 75;
p.weight = 9.3f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY,EggGroup.GRASS};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);this.add(Ability.PICKPOCKET);}};
perName.put(ctx.getString(R.string.name_weavile), new Pokemon(ctx.getString(R.string.name_weavile), 461, 494, Type.DARK, Type.ICE, abilities, 70, 120, 65, 45, 85, 125));
p = perName.get(ctx.getString(R.string.name_weavile));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_sneasel)), new HashMap<String, EvolutionNode>(){{this.put("Gagne un niveau de nuit en tenant une Griffe Rasoir", new EvolutionNode(perName.get(ctx.getString(R.string.name_weavile)), null));}});
p.catchRate = 45;
p.weight = 34.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.SHELL_ARMOR);this.add(Ability.WEAK_ARMOR);}};
perName.put(ctx.getString(R.string.name_omanyte), new Pokemon(ctx.getString(R.string.name_omanyte), 138, 147, Type.ROCK, Type.WATER, abilities, 35, 40, 100, 90, 55, 35));
p = perName.get(ctx.getString(R.string.name_omanyte));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_omanyte)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_omastar)), null));}});
p.catchRate = 45;
p.weight = 7.5f;
p.hatch = 7680;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER3};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWARM);this.add(Ability.CHLOROPHYLL);this.add(Ability.OVERCOAT);}};
perName.put(ctx.getString(R.string.name_sewaddle), new Pokemon(ctx.getString(R.string.name_sewaddle), 540, 580, Type.BUG, Type.GRASS, abilities, 45, 53, 70, 40, 60, 42));
p = perName.get(ctx.getString(R.string.name_sewaddle));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_sewaddle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_swadloon)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_leavanny)), null));}}));}});
p.catchRate = 255;
p.weight = 2.5f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HYPER_CUTTER);this.add(Ability.SHELL_ARMOR);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_kingler), new Pokemon(ctx.getString(R.string.name_kingler), 99, 105, Type.WATER, Type.NONE, abilities, 55, 130, 115, 50, 50, 75));
p = perName.get(ctx.getString(R.string.name_kingler));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_krabby)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "28", new EvolutionNode(perName.get(ctx.getString(R.string.name_kingler)), null));}});
p.catchRate = 60;
p.weight = 60.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER3};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.HYDRATION);this.add(Ability.WATER_ABSORB);}};
perName.put(ctx.getString(R.string.name_palpitoad), new Pokemon(ctx.getString(R.string.name_palpitoad), 536, 576, Type.WATER, Type.GROUND, abilities, 75, 65, 55, 65, 55, 69));
p = perName.get(ctx.getString(R.string.name_palpitoad));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tympole)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_palpitoad)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_seismitoad)), null));}}));}});
p.catchRate = 120;
p.weight = 17.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CLEAR_BODY);this.add(Ability.LIQUID_OOZE);this.add(Ability.RAIN_DISH);}};
perName.put(ctx.getString(R.string.name_tentacool), new Pokemon(ctx.getString(R.string.name_tentacool), 72, 77, Type.WATER, Type.POISON, abilities, 40, 40, 35, 50, 100, 70));
p = perName.get(ctx.getString(R.string.name_tentacool));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tentacool)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_tentacruel)), null));}});
p.catchRate = 190;
p.weight = 45.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER3};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_STREAM);this.add(Ability.SAND_FORCE);}};
perName.put(ctx.getString(R.string.name_hippowdon), new Pokemon(ctx.getString(R.string.name_hippowdon), 450, 482, Type.GROUND, Type.NONE, abilities, 108, 112, 118, 68, 72, 47));
p = perName.get(ctx.getString(R.string.name_hippowdon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_hippopotas)), new HashMap<String, EvolutionNode>(){{this.put("niveau 34", new EvolutionNode(perName.get(ctx.getString(R.string.name_hippowdon)), null));}});
p.catchRate = 60;
p.weight = 300.0f;
p.hatch = 7680;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.WATER_VEIL);this.add(Ability.OBLIVIOUS);}};
perName.put(ctx.getString(R.string.name_wailmer), new Pokemon(ctx.getString(R.string.name_wailmer), 320, 343, Type.WATER, Type.NONE, abilities, 130, 70, 35, 70, 35, 60));
p = perName.get(ctx.getString(R.string.name_wailmer));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_wailmer)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_wailord)), null));}});
p.catchRate = 125;
p.weight = 130.0f;
p.hatch = 10240;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.WATER2};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLAME_BODY);this.add(Ability.VITAL_SPIRIT);}};
perName.put(ctx.getString(R.string.name_magmar), new Pokemon(ctx.getString(R.string.name_magmar), 126, 133, Type.FIRE, Type.NONE, abilities, 65, 95, 57, 100, 85, 93));
p = perName.get(ctx.getString(R.string.name_magmar));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_magby)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_magmar)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Magmariseur", new EvolutionNode(perName.get(ctx.getString(R.string.name_magmortar)), null));}}));}});
p.catchRate = 45;
p.weight = 44.5f;
p.hatch = 6400;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLASH_FIRE);this.add(Ability.INTIMIDATE);}};
perName.put(ctx.getString(R.string.name_growlithe), new Pokemon(ctx.getString(R.string.name_growlithe), 58, 62, Type.FIRE, Type.NONE, abilities, 55, 70, 45, 70, 50, 60));
p = perName.get(ctx.getString(R.string.name_growlithe));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_growlithe)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Feu", new EvolutionNode(perName.get(ctx.getString(R.string.name_arcanine)), null));}});
p.catchRate = 190;
p.weight = 19.0f;
p.hatch = 5120;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_lunatone), new Pokemon(ctx.getString(R.string.name_lunatone), 337, 360, Type.ROCK, Type.PSYCHIC, abilities, 70, 55, 65, 95, 85, 70));
p = perName.get(ctx.getString(R.string.name_lunatone));
p.evolutions = null;
p.catchRate = 45;
p.weight = 168.0f;
p.hatch = 6400;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INNER_FOCUS);this.add(Ability.STEADFAST);this.add(Ability.JUSTIFIED);}};
perName.put(ctx.getString(R.string.name_lucario), new Pokemon(ctx.getString(R.string.name_lucario), 448, 479, Type.FIGHTING, Type.STEEL, abilities, 70, 110, 70, 115, 70, 90));
p = perName.get(ctx.getString(R.string.name_lucario));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_riolu)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur + gagne un niveau de jour", new EvolutionNode(perName.get(ctx.getString(R.string.name_lucario)), new HashMap<String, EvolutionNode>(){{this.put("Lucarite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_lucario)), null));}}));}});
p.catchRate = 45;
p.weight = 54.0f;
p.hatch = 2560;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.HUMANLIKE};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GUTS);this.add(Ability.NO_GUARD);this.add(Ability.STEADFAST);}};
perName.put(ctx.getString(R.string.name_machoke), new Pokemon(ctx.getString(R.string.name_machoke), 67, 72, Type.FIGHTING, Type.NONE, abilities, 80, 100, 70, 50, 60, 45));
p = perName.get(ctx.getString(R.string.name_machoke));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_machop)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "28", new EvolutionNode(perName.get(ctx.getString(R.string.name_machoke)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_machamp)), null));}}));}});
p.catchRate = 90;
p.weight = 70.5f;
p.hatch = 5120;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.OBLIVIOUS);this.add(Ability.ADAPTABILITY);}};
perName.put(ctx.getString(R.string.name_feebas), new Pokemon(ctx.getString(R.string.name_feebas), 349, 372, Type.WATER, Type.NONE, abilities, 20, 15, 20, 10, 55, 80));
p = perName.get(ctx.getString(R.string.name_feebas));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_feebas)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "de Beaute superieur ou egal a 170 (3eme et 4eme generations) ou Echange en tenant l'objet Bel'Ecaille (5eme et 6eme generations) ou Tenir le Voile Venus (Pokemon Donjon Mystere)", new EvolutionNode(perName.get(ctx.getString(R.string.name_milotic)), null));}});
p.catchRate = 255;
p.weight = 7.4f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.DRAGON};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHED_SKIN);}};
perName.put(ctx.getString(R.string.name_silcoon), new Pokemon(ctx.getString(R.string.name_silcoon), 266, 284, Type.BUG, Type.NONE, abilities, 50, 35, 55, 25, 25, 15));
p = perName.get(ctx.getString(R.string.name_silcoon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_wurmple)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "10", new EvolutionNode(perName.get(ctx.getString(R.string.name_dustox)), null));this.put(ctx.getString(R.string.level) + "7, au hasard", new EvolutionNode(perName.get(ctx.getString(R.string.name_cascoon)), null));}});
p.catchRate = 120;
p.weight = 10.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BATTLE_ARMOR);this.add(Ability.SNIPER);this.add(Ability.KEEN_EYE);}};
perName.put(ctx.getString(R.string.name_drapion), new Pokemon(ctx.getString(R.string.name_drapion), 452, 484, Type.POISON, Type.DARK, abilities, 70, 90, 110, 60, 75, 95));
p = perName.get(ctx.getString(R.string.name_drapion));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_skorupi)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_drapion)), null));}});
p.catchRate = 45;
p.weight = 61.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG,EggGroup.WATER3};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OBLIVIOUS);this.add(Ability.OWN_TEMPO);this.add(Ability.CLOUD_NINE);}};
perName.put(ctx.getString(R.string.name_lickilicky), new Pokemon(ctx.getString(R.string.name_lickilicky), 463, 496, Type.NORMAL, Type.NONE, abilities, 110, 85, 95, 80, 95, 50));
p = perName.get(ctx.getString(R.string.name_lickilicky));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_lickitung)), new HashMap<String, EvolutionNode>(){{this.put("En connaissant l'attaque Roulade", new EvolutionNode(perName.get(ctx.getString(R.string.name_lickilicky)), null));}});
p.catchRate = 30;
p.weight = 140.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.MAGNET_PULL);this.add(Ability.SAND_FORCE);}};
perName.put(ctx.getString(R.string.name_probopass), new Pokemon(ctx.getString(R.string.name_probopass), 476, 509, Type.ROCK, Type.STEEL, abilities, 60, 55, 145, 75, 150, 40));
p = perName.get(ctx.getString(R.string.name_probopass));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_nosepass)), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau dans un lieu indique", new EvolutionNode(perName.get(ctx.getString(R.string.name_probopass)), null));}});
p.catchRate = 60;
p.weight = 340.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.HYDRATION);}};
perName.put(ctx.getString(R.string.name_luvdisc), new Pokemon(ctx.getString(R.string.name_luvdisc), 370, 395, Type.WATER, Type.NONE, abilities, 43, 30, 55, 40, 65, 97));
p = perName.get(ctx.getString(R.string.name_luvdisc));
p.evolutions = null;
p.catchRate = 225;
p.weight = 8.7f;
p.hatch = 5120;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER2};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.LEAF_GUARD);this.add(Ability.REGENERATOR);}};
perName.put(ctx.getString(R.string.name_tangela), new Pokemon(ctx.getString(R.string.name_tangela), 114, 120, Type.GRASS, Type.NONE, abilities, 65, 55, 115, 100, 40, 60));
p = perName.get(ctx.getString(R.string.name_tangela));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tangela)), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l'attaque Pouv.Antique", new EvolutionNode(perName.get(ctx.getString(R.string.name_tangrowth)), null));}});
p.catchRate = 45;
p.weight = 35.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.EARLY_BIRD);this.add(Ability.PICKPOCKET);}};
perName.put(ctx.getString(R.string.name_shiftry), new Pokemon(ctx.getString(R.string.name_shiftry), 275, 293, Type.GRASS, Type.DARK, abilities, 90, 100, 60, 90, 60, 80));
p = perName.get(ctx.getString(R.string.name_shiftry));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_seedot)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "14", new EvolutionNode(perName.get(ctx.getString(R.string.name_nuzleaf)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get(ctx.getString(R.string.name_shiftry)), null));}}));}});
p.catchRate = 45;
p.weight = 59.6f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.GRASS};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.IRON_FIST);this.add(Ability.KLUTZ);this.add(Ability.NO_GUARD);}};
perName.put(ctx.getString(R.string.name_golurk), new Pokemon(ctx.getString(R.string.name_golurk), 623, 664, Type.GROUND, Type.GHOST, abilities, 89, 124, 80, 55, 80, 55));
p = perName.get(ctx.getString(R.string.name_golurk));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_golett)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "43", new EvolutionNode(perName.get(ctx.getString(R.string.name_golurk)), null));}});
p.catchRate = 90;
p.weight = 330.0f;
p.hatch = 6630;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 2.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HUSTLE);}};
perName.put(ctx.getString(R.string.name_zweilous), new Pokemon(ctx.getString(R.string.name_zweilous), 634, 675, Type.DARK, Type.DRAGON, abilities, 72, 85, 70, 65, 70, 58));
p = perName.get(ctx.getString(R.string.name_zweilous));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_deino)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "50", new EvolutionNode(perName.get(ctx.getString(R.string.name_zweilous)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "64", new EvolutionNode(perName.get(ctx.getString(R.string.name_hydreigon)), null));}}));}});
p.catchRate = 190;
p.weight = 50.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEAF_GUARD);this.add(Ability.CHLOROPHYLL);}};
perName.put(ctx.getString(R.string.name_leafeon), new Pokemon(ctx.getString(R.string.name_leafeon), 470, 503, Type.GRASS, Type.NONE, abilities, 65, 110, 130, 60, 65, 95));
p = perName.get(ctx.getString(R.string.name_leafeon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_eevee)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get(ctx.getString(R.string.name_jolteon)), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_leafeon)), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get(ctx.getString(R.string.name_espeon)), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get(ctx.getString(R.string.name_sylveon)), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_vaporeon)), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get(ctx.getString(R.string.name_glaceon)), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get(ctx.getString(R.string.name_flareon)), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get(ctx.getString(R.string.name_umbreon)), null));}});
p.catchRate = 45;
p.weight = 25.5f;
p.hatch = 8960;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.KEEN_EYE);this.add(Ability.INFILTRATOR);this.add(Ability.PRANKSTER);this.add(Ability.COMPETITIVE);}};
perName.put(ctx.getString(R.string.name_meowstic), new Pokemon(ctx.getString(R.string.name_meowstic), 678, 724, Type.PSYCHIC, Type.NONE, abilities, 74, 48, 76, 83, 81, 104));
p = perName.get(ctx.getString(R.string.name_meowstic));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_espurr)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_meowstic)), null));}});
p.catchRate = -1;
p.weight = 8.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.THICK_FAT);}};
perName.put(ctx.getString(R.string.name_pignite), new Pokemon(ctx.getString(R.string.name_pignite), 499, 539, Type.FIRE, Type.FIGHTING, abilities, 90, 93, 55, 70, 55, 55));
p = perName.get(ctx.getString(R.string.name_pignite));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tepig)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "17", new EvolutionNode(perName.get(ctx.getString(R.string.name_pignite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_emboar)), null));}}));}});
p.catchRate = 45;
p.weight = 55.5f;
p.hatch = 5355;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.SOLAR_POWER);this.add(Ability.HARVEST);}};
perName.put(ctx.getString(R.string.name_tropius), new Pokemon(ctx.getString(R.string.name_tropius), 357, 381, Type.GRASS, Type.FLYING, abilities, 99, 68, 83, 72, 87, 51));
p = perName.get(ctx.getString(R.string.name_tropius));
p.evolutions = null;
p.catchRate = 200;
p.weight = 100.0f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.GRASS};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.EFFECT_SPORE);this.add(Ability.POISON_HEAL);this.add(Ability.TECHNICIAN);}};
perName.put(ctx.getString(R.string.name_breloom), new Pokemon(ctx.getString(R.string.name_breloom), 286, 305, Type.GRASS, Type.FIGHTING, abilities, 60, 130, 80, 60, 60, 70));
p = perName.get(ctx.getString(R.string.name_breloom));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_shroomish)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "23", new EvolutionNode(perName.get(ctx.getString(R.string.name_breloom)), null));}});
p.catchRate = 90;
p.weight = 39.2f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY,EggGroup.GRASS};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.VICTORY_STAR);}};
perName.put(ctx.getString(R.string.name_victini), new Pokemon(ctx.getString(R.string.name_victini), 494, 534, Type.PSYCHIC, Type.FIRE, abilities, 100, 100, 100, 100, 100, 100));
p = perName.get(ctx.getString(R.string.name_victini));
p.evolutions = null;
p.catchRate = 3;
p.weight = 4f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHED_SKIN);}};
perName.put(ctx.getString(R.string.name_pupitar), new Pokemon(ctx.getString(R.string.name_pupitar), 247, 263, Type.ROCK, Type.GROUND, abilities, 70, 84, 70, 65, 70, 51));
p = perName.get(ctx.getString(R.string.name_pupitar));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_larvitar)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_pupitar)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "55", new EvolutionNode(perName.get(ctx.getString(R.string.name_tyranitar)), new HashMap<String, EvolutionNode>(){{this.put("Tyranocivite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_tyranitar)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 152.0f;
p.hatch = 10240;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);this.add(Ability.SNOW_CLOAK);}};
perName.put(ctx.getString(R.string.name_articuno), new Pokemon(ctx.getString(R.string.name_articuno), 144, 154, Type.ICE, Type.FLYING, abilities, 90, 85, 100, 95, 125, 85));
p = perName.get(ctx.getString(R.string.name_articuno));
p.evolutions = null;
p.catchRate = 3;
p.weight = 55.4f;
p.hatch = 20480;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HYDRATION);}};
perName.put(ctx.getString(R.string.name_phione), new Pokemon(ctx.getString(R.string.name_phione), 489, 528, Type.WATER, Type.NONE, abilities, 80, 80, 80, 80, 80, 80));
p = perName.get(ctx.getString(R.string.name_phione));
p.evolutions = null;
p.catchRate = 30;
p.weight = 3.1f;
p.hatch = 10710;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FAIRY};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.TECHNICIAN);this.add(Ability.UNNERVE);}};
perName.put(ctx.getString(R.string.name_meowth), new Pokemon(ctx.getString(R.string.name_meowth), 52, 56, Type.NORMAL, Type.NONE, abilities, 40, 45, 35, 40, 40, 90));
p = perName.get(ctx.getString(R.string.name_meowth));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_meowth)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "28", new EvolutionNode(perName.get(ctx.getString(R.string.name_persian)), null));}});
p.catchRate = 255;
p.weight = 4.2f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLAME_BODY);this.add(Ability.GALE_WINGS);}};
perName.put(ctx.getString(R.string.name_fletchinder), new Pokemon(ctx.getString(R.string.name_fletchinder), 662, 708, Type.FIRE, Type.FLYING, abilities, 62, 73, 55, 56, 52, 84));
p = perName.get(ctx.getString(R.string.name_fletchinder));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_fletchling)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "17", new EvolutionNode(perName.get(ctx.getString(R.string.name_fletchinder)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_talonflame)), null));}}));}});
p.catchRate = -1;
p.weight = 16.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWARM);this.add(Ability.INSOMNIA);this.add(Ability.SNIPER);}};
perName.put(ctx.getString(R.string.name_ariados), new Pokemon(ctx.getString(R.string.name_ariados), 168, 180, Type.BUG, Type.POISON, abilities, 70, 90, 70, 60, 60, 40));
p = perName.get(ctx.getString(R.string.name_ariados));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_spinarak)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "22", new EvolutionNode(perName.get(ctx.getString(R.string.name_ariados)), null));}});
p.catchRate = 90;
p.weight = 33.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ROCK_HEAD);this.add(Ability.STURDY);this.add(Ability.RATTLED);}};
perName.put(ctx.getString(R.string.name_bonsly), new Pokemon(ctx.getString(R.string.name_bonsly), 438, 468, Type.ROCK, Type.NONE, abilities, 50, 80, 95, 10, 45, 10));
p = perName.get(ctx.getString(R.string.name_bonsly));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bonsly)), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l'attaque Copie", new EvolutionNode(perName.get(ctx.getString(R.string.name_sudowoodo)), null));}});
p.catchRate = 255;
p.weight = 15.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INNER_FOCUS);this.add(Ability.INFILTRATOR);}};
perName.put(ctx.getString(R.string.name_zubat), new Pokemon(ctx.getString(R.string.name_zubat), 41, 45, Type.POISON, Type.FLYING, abilities, 40, 45, 35, 30, 40, 55));
p = perName.get(ctx.getString(R.string.name_zubat));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_zubat)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "22", new EvolutionNode(perName.get(ctx.getString(R.string.name_golbat)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_crobat)), null));}}));}});
p.catchRate = 255;
p.weight = 7.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.RAIN_DISH);}};
perName.put(ctx.getString(R.string.name_surskit), new Pokemon(ctx.getString(R.string.name_surskit), 283, 302, Type.BUG, Type.WATER, abilities, 40, 30, 32, 50, 52, 65));
p = perName.get(ctx.getString(R.string.name_surskit));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_surskit)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "22", new EvolutionNode(perName.get(ctx.getString(R.string.name_masquerain)), null));}});
p.catchRate = 200;
p.weight = 1.7f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.BUG};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_totodile), new Pokemon(ctx.getString(R.string.name_totodile), 158, 170, Type.WATER, Type.NONE, abilities, 50, 65, 64, 44, 48, 43));
p = perName.get(ctx.getString(R.string.name_totodile));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_totodile)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_croconaw)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_feraligatr)), null));}}));}});
p.catchRate = 45;
p.weight = 9.5f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.WATER1};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWARM);this.add(Ability.RIVALRY);}};
perName.put(ctx.getString(R.string.name_beautifly), new Pokemon(ctx.getString(R.string.name_beautifly), 267, 285, Type.BUG, Type.FLYING, abilities, 60, 70, 50, 90, 50, 65));
p = perName.get(ctx.getString(R.string.name_beautifly));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_wurmple)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "10", new EvolutionNode(perName.get(ctx.getString(R.string.name_dustox)), null));this.put(ctx.getString(R.string.level) + "7, au hasard", new EvolutionNode(perName.get(ctx.getString(R.string.name_cascoon)), null));}});
p.catchRate = 45;
p.weight = 28.4f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LIGHTNINGROD);this.add(Ability.MOTOR_DRIVE);this.add(Ability.SAP_SIPPER);}};
perName.put(ctx.getString(R.string.name_blitzle), new Pokemon(ctx.getString(R.string.name_blitzle), 522, 562, Type.ELECTRIC, Type.NONE, abilities, 45, 60, 32, 50, 32, 76));
p = perName.get(ctx.getString(R.string.name_blitzle));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_blitzle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "27", new EvolutionNode(perName.get(ctx.getString(R.string.name_zebstrika)), null));}});
p.catchRate = 190;
p.weight = 29.8f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RIVALRY);this.add(Ability.MOLD_BREAKER);this.add(Ability.UNNERVE);}};
perName.put(ctx.getString(R.string.name_axew), new Pokemon(ctx.getString(R.string.name_axew), 610, 651, Type.DRAGON, Type.NONE, abilities, 46, 87, 60, 30, 40, 57));
p = perName.get(ctx.getString(R.string.name_axew));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_axew)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "38", new EvolutionNode(perName.get(ctx.getString(R.string.name_fraxure)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "48", new EvolutionNode(perName.get(ctx.getString(R.string.name_haxorus)), null));}}));}});
p.catchRate = 75;
p.weight = 18.0f;
p.hatch = 10455;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.DRAGON};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ILLUMINATE);this.add(Ability.SWARM);this.add(Ability.PRANKSTER);}};
perName.put(ctx.getString(R.string.name_volbeat), new Pokemon(ctx.getString(R.string.name_volbeat), 313, 336, Type.BUG, Type.NONE, abilities, 65, 73, 55, 47, 75, 85));
p = perName.get(ctx.getString(R.string.name_volbeat));
p.evolutions = null;
p.catchRate = 150;
p.weight = 17.7f;
p.hatch = 3840;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG,EggGroup.HUMANLIKE};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWARM);this.add(Ability.TECHNICIAN);this.add(Ability.LIGHT_METAL);}};
perName.put(ctx.getString(R.string.name_scizor), new Pokemon(ctx.getString(R.string.name_scizor), 212, 225, Type.BUG, Type.STEEL, abilities, 70, 130, 100, 55, 80, 65));
p = perName.get(ctx.getString(R.string.name_scizor));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_scyther)), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Peau Metal", new EvolutionNode(perName.get(ctx.getString(R.string.name_scizor)), new HashMap<String, EvolutionNode>(){{this.put("Mega-Evolution", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_scizor)), null));}}));}});
p.catchRate = 25;
p.weight = 118.0f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_VEIL);this.add(Ability.ARENA_TRAP);this.add(Ability.SAND_FORCE);}};
perName.put(ctx.getString(R.string.name_dugtrio), new Pokemon(ctx.getString(R.string.name_dugtrio), 51, 55, Type.GROUND, Type.NONE, abilities, 35, 80, 50, 50, 70, 120));
p = perName.get(ctx.getString(R.string.name_dugtrio));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_diglett)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "26", new EvolutionNode(perName.get(ctx.getString(R.string.name_dugtrio)), null));}});
p.catchRate = 50;
p.weight = 33.3f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.LEAF_GUARD);this.add(Ability.INFILTRATOR);}};
perName.put(ctx.getString(R.string.name_skiploom), new Pokemon(ctx.getString(R.string.name_skiploom), 188, 201, Type.GRASS, Type.FLYING, abilities, 55, 45, 50, 45, 65, 80));
p = perName.get(ctx.getString(R.string.name_skiploom));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_hoppip)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_skiploom)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "27", new EvolutionNode(perName.get(ctx.getString(R.string.name_jumpluff)), null));}}));}});
p.catchRate = 120;
p.weight = 1.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY,EggGroup.GRASS};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GUTS);this.add(Ability.SHEER_FORCE);this.add(Ability.IRON_FIST);}};
perName.put(ctx.getString(R.string.name_gurdurr), new Pokemon(ctx.getString(R.string.name_gurdurr), 533, 573, Type.FIGHTING, Type.NONE, abilities, 85, 105, 85, 40, 50, 40));
p = perName.get(ctx.getString(R.string.name_gurdurr));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_timburr)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_gurdurr)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_conkeldurr)), null));}}));}});
p.catchRate = 90;
p.weight = 40.0f;
p.hatch = 5355;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BAD_DREAMS);}};
perName.put(ctx.getString(R.string.name_darkrai), new Pokemon(ctx.getString(R.string.name_darkrai), 491, 530, Type.DARK, Type.NONE, abilities, 70, 90, 90, 135, 90, 125));
p = perName.get(ctx.getString(R.string.name_darkrai));
p.evolutions = null;
p.catchRate = 3;
p.weight = 50.5f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SYNCHRONIZE);}};
perName.put(ctx.getString(R.string.name_mew), new Pokemon(ctx.getString(R.string.name_mew), 151, 163, Type.PSYCHIC, Type.NONE, abilities, 100, 100, 100, 100, 100, 100));
p = perName.get(ctx.getString(R.string.name_mew));
p.evolutions = null;
p.catchRate = 45;
p.weight = 4.0f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.IRON_BARBS);}};
perName.put(ctx.getString(R.string.name_ferroseed), new Pokemon(ctx.getString(R.string.name_ferroseed), 597, 638, Type.GRASS, Type.STEEL, abilities, 44, 50, 91, 24, 86, 10));
p = perName.get(ctx.getString(R.string.name_ferroseed));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_ferroseed)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_ferrothorn)), null));}});
p.catchRate = 255;
p.weight = 18.8f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS,EggGroup.MINERAL};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.EFFECT_SPORE);this.add(Ability.POISON_HEAL);this.add(Ability.QUICK_FEET);}};
perName.put(ctx.getString(R.string.name_shroomish), new Pokemon(ctx.getString(R.string.name_shroomish), 285, 304, Type.GRASS, Type.NONE, abilities, 60, 40, 60, 40, 60, 35));
p = perName.get(ctx.getString(R.string.name_shroomish));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_shroomish)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "23", new EvolutionNode(perName.get(ctx.getString(R.string.name_breloom)), null));}});
p.catchRate = 255;
p.weight = 4.5f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY,EggGroup.GRASS};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.POISON_POINT);this.add(Ability.POISON_TOUCH);}};
perName.put(ctx.getString(R.string.name_dragalge), new Pokemon(ctx.getString(R.string.name_dragalge), 691, 738, Type.POISON, Type.DRAGON, abilities, 65, 75, 90, 97, 123, 44));
p = perName.get(ctx.getString(R.string.name_dragalge));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_skrelp)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "48", new EvolutionNode(perName.get(ctx.getString(R.string.name_dragalge)), null));}});
p.catchRate = -1;
p.weight = 81.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.DRAGON};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LIMBER);this.add(Ability.OWN_TEMPO);this.add(Ability.KEEN_EYE);}};
perName.put(ctx.getString(R.string.name_glameow), new Pokemon(ctx.getString(R.string.name_glameow), 431, 461, Type.NORMAL, Type.NONE, abilities, 49, 55, 42, 42, 37, 85));
p = perName.get(ctx.getString(R.string.name_glameow));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_glameow)), new HashMap<String, EvolutionNode>(){{this.put("niveau 38", new EvolutionNode(perName.get(ctx.getString(R.string.name_purugly)), null));}});
p.catchRate = 190;
p.weight = 3.9f;
p.hatch = 5120;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.75f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FAIRY_AURA);}};
perName.put(ctx.getString(R.string.name_xerneas), new Pokemon(ctx.getString(R.string.name_xerneas), 716, 769, Type.FAIRY, Type.NONE, abilities, 126, 131, 95, 131, 98, 99));
p = perName.get(ctx.getString(R.string.name_xerneas));
p.evolutions = null;
p.catchRate = 30;
p.weight = 215.0f;
p.hatch = -1;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 3.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.VITAL_SPIRIT);this.add(Ability.HUSTLE);}};
perName.put(ctx.getString(R.string.name_delibird), new Pokemon(ctx.getString(R.string.name_delibird), 225, 240, Type.ICE, Type.FLYING, abilities, 45, 55, 45, 65, 45, 75));
p = perName.get(ctx.getString(R.string.name_delibird));
p.evolutions = null;
p.catchRate = 45;
p.weight = 16.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.FIELD};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PARENTAL_BOND);}};
perName.put(ctx.getString(R.string.name_mega_kangaskhan), new Pokemon(ctx.getString(R.string.name_mega_kangaskhan), 115, 122, Type.NORMAL, Type.NONE, abilities, 105, 125, 100, 60, 100, 100));
p = perName.get(ctx.getString(R.string.name_mega_kangaskhan));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_kangaskhan)), new HashMap<String, EvolutionNode>(){{this.put("Kangourexite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_kangaskhan)), null));}});
p.catchRate = -1;
p.weight = 100.0f;
p.hatch = -1;
p.gender = 100f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.SOLAR_POWER);}};
perName.put(ctx.getString(R.string.name_charmander), new Pokemon(ctx.getString(R.string.name_charmander), 4, 5, Type.FIRE, Type.NONE, abilities, 39, 52, 43, 60, 40, 65));
p = perName.get(ctx.getString(R.string.name_charmander));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_charmander)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_charmeleon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_charizard)), new HashMap<String, EvolutionNode>(){{this.put("Dracaufite X", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_charizard_x)), null));this.put("Dracaufite Y", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_charizard_y)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 8.5f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON,EggGroup.MONSTER};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.VOLT_ABSORB);this.add(Ability.ILLUMINATE);this.add(Ability.WATER_ABSORB);}};
perName.put(ctx.getString(R.string.name_lanturn), new Pokemon(ctx.getString(R.string.name_lanturn), 171, 183, Type.WATER, Type.ELECTRIC, abilities, 125, 58, 58, 76, 76, 67));
p = perName.get(ctx.getString(R.string.name_lanturn));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_chinchou)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "27", new EvolutionNode(perName.get(ctx.getString(R.string.name_lanturn)), null));}});
p.catchRate = 75;
p.weight = 22.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER2};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.IRON_FIST);}};
perName.put(ctx.getString(R.string.name_infernape), new Pokemon(ctx.getString(R.string.name_infernape), 392, 420, Type.FIRE, Type.FIGHTING, abilities, 76, 104, 71, 104, 71, 108));
p = perName.get(ctx.getString(R.string.name_infernape));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_chimchar)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "14", new EvolutionNode(perName.get(ctx.getString(R.string.name_monferno)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_infernape)), null));}}));}});
p.catchRate = 45;
p.weight = 55f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.HUMANLIKE};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FRISK);this.add(Ability.INFILTRATOR);this.add(Ability.TELEPATHY);}};
perName.put(ctx.getString(R.string.name_noivern), new Pokemon(ctx.getString(R.string.name_noivern), 715, 768, Type.FLYING, Type.DRAGON, abilities, 85, 70, 80, 97, 80, 123));
p = perName.get(ctx.getString(R.string.name_noivern));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_noibat)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "48", new EvolutionNode(perName.get(ctx.getString(R.string.name_noivern)), null));}});
p.catchRate = -1;
p.weight = 85.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HYDRATION);this.add(Ability.SAP_SIPPER);this.add(Ability.GOOEY);}};
perName.put(ctx.getString(R.string.name_goomy), new Pokemon(ctx.getString(R.string.name_goomy), 704, 751, Type.DRAGON, Type.NONE, abilities, 40, 50, 30, 70, 100, 45));
p = perName.get(ctx.getString(R.string.name_goomy));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_goomy)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_sliggoo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "50, quand il pleut", new EvolutionNode(perName.get(ctx.getString(R.string.name_goodra)), null));}}));}});
p.catchRate = -1;
p.weight = 2.8f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.THICK_FAT);this.add(Ability.OWN_TEMPO);this.add(Ability.DEFIANT);}};
perName.put(ctx.getString(R.string.name_purugly), new Pokemon(ctx.getString(R.string.name_purugly), 432, 462, Type.NORMAL, Type.NONE, abilities, 71, 82, 64, 64, 59, 112));
p = perName.get(ctx.getString(R.string.name_purugly));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_glameow)), new HashMap<String, EvolutionNode>(){{this.put("niveau 38", new EvolutionNode(perName.get(ctx.getString(R.string.name_purugly)), null));}});
p.catchRate = 75;
p.weight = 43.8f;
p.hatch = 5120;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.DEFEATIST);}};
perName.put(ctx.getString(R.string.name_archeops), new Pokemon(ctx.getString(R.string.name_archeops), 567, 608, Type.ROCK, Type.FLYING, abilities, 75, 140, 65, 112, 65, 110));
p = perName.get(ctx.getString(R.string.name_archeops));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_archen)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_archeops)), null));}});
p.catchRate = 45;
p.weight = 32.0f;
p.hatch = 7905;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING,EggGroup.WATER3};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INNER_FOCUS);this.add(Ability.KEEN_EYE);this.add(Ability.PICKPOCKET);}};
perName.put(ctx.getString(R.string.name_sneasel), new Pokemon(ctx.getString(R.string.name_sneasel), 215, 230, Type.DARK, Type.ICE, abilities, 55, 95, 55, 35, 75, 115));
p = perName.get(ctx.getString(R.string.name_sneasel));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_sneasel)), new HashMap<String, EvolutionNode>(){{this.put("Gagne un niveau de nuit en tenant une Griffe Rasoir", new EvolutionNode(perName.get(ctx.getString(R.string.name_weavile)), null));}});
p.catchRate = 60;
p.weight = 28.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.LEAF_GUARD);this.add(Ability.INFILTRATOR);}};
perName.put(ctx.getString(R.string.name_jumpluff), new Pokemon(ctx.getString(R.string.name_jumpluff), 189, 202, Type.GRASS, Type.FLYING, abilities, 75, 55, 70, 55, 85, 110));
p = perName.get(ctx.getString(R.string.name_jumpluff));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_hoppip)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_skiploom)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "27", new EvolutionNode(perName.get(ctx.getString(R.string.name_jumpluff)), null));}}));}});
p.catchRate = 45;
p.weight = 3.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY,EggGroup.GRASS};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CUTE_CHARM);this.add(Ability.COMPETITIVE);this.add(Ability.FRIEND_GUARD);}};
perName.put(ctx.getString(R.string.name_jigglypuff), new Pokemon(ctx.getString(R.string.name_jigglypuff), 39, 43, Type.NORMAL, Type.NONE, abilities, 115, 45, 20, 45, 25, 20));
p = perName.get(ctx.getString(R.string.name_jigglypuff));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_igglybuff)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get(ctx.getString(R.string.name_jigglypuff)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get(ctx.getString(R.string.name_wigglytuff)), null));}}));}});
p.catchRate = 170;
p.weight = 5.5f;
p.hatch = 2560;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ICE_BODY);this.add(Ability.WEAK_ARMOR);}};
perName.put(ctx.getString(R.string.name_vanillish), new Pokemon(ctx.getString(R.string.name_vanillish), 583, 624, Type.ICE, Type.NONE, abilities, 51, 65, 65, 80, 75, 59));
p = perName.get(ctx.getString(R.string.name_vanillish));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_vanillite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_vanillish)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "47", new EvolutionNode(perName.get(ctx.getString(R.string.name_vanilluxe)), null));}}));}});
p.catchRate = 120;
p.weight = 41.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.SHELL_ARMOR);this.add(Ability.WEAK_ARMOR);}};
perName.put(ctx.getString(R.string.name_omastar), new Pokemon(ctx.getString(R.string.name_omastar), 139, 148, Type.ROCK, Type.WATER, abilities, 70, 60, 125, 115, 70, 55));
p = perName.get(ctx.getString(R.string.name_omastar));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_omanyte)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_omastar)), null));}});
p.catchRate = 45;
p.weight = 35.0f;
p.hatch = 7680;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER3};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PLUS);this.add(Ability.MINUS);this.add(Ability.CLEAR_BODY);}};
perName.put(ctx.getString(R.string.name_klang), new Pokemon(ctx.getString(R.string.name_klang), 600, 641, Type.STEEL, Type.NONE, abilities, 60, 80, 95, 70, 85, 50));
p = perName.get(ctx.getString(R.string.name_klang));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_klink)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "38", new EvolutionNode(perName.get(ctx.getString(R.string.name_klang)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "49", new EvolutionNode(perName.get(ctx.getString(R.string.name_klinklang)), null));}}));}});
p.catchRate = 60;
p.weight = 51.0f;
p.hatch = 5355;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.LEAF_GUARD);}};
perName.put(ctx.getString(R.string.name_meganium), new Pokemon(ctx.getString(R.string.name_meganium), 154, 166, Type.GRASS, Type.NONE, abilities, 80, 82, 100, 83, 100, 80));
p = perName.get(ctx.getString(R.string.name_meganium));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_chikorita)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_bayleef)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_meganium)), null));}}));}});
p.catchRate = 45;
p.weight = 100.5f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.GRASS};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);}};
perName.put(ctx.getString(R.string.name_deoxys_defense_forme), new Pokemon(ctx.getString(R.string.name_deoxys_defense_forme), 386, 413, Type.PSYCHIC, Type.NONE, abilities, 50, 70, 160, 70, 160, 90));
p = perName.get(ctx.getString(R.string.name_deoxys_defense_forme));
p.evolutions = null;
p.catchRate = 3;
p.weight = 60.8f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.WATER_ABSORB);this.add(Ability.CURSED_BODY);this.add(Ability.DAMP);}};
perName.put(ctx.getString(R.string.name_frillish), new Pokemon(ctx.getString(R.string.name_frillish), 592, 633, Type.WATER, Type.GHOST, abilities, 55, 40, 50, 65, 85, 40));
p = perName.get(ctx.getString(R.string.name_frillish));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_frillish)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_jellicent)), null));}});
p.catchRate = 190;
p.weight = 33.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LIMBER);this.add(Ability.IMPOSTER);}};
perName.put(ctx.getString(R.string.name_ditto), new Pokemon(ctx.getString(R.string.name_ditto), 132, 141, Type.NORMAL, Type.NONE, abilities, 48, 48, 48, 48, 48, 48));
p = perName.get(ctx.getString(R.string.name_ditto));
p.evolutions = null;
p.catchRate = 35;
p.weight = 4.0f;
p.hatch = 5120;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DITTO};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.EARLY_BIRD);this.add(Ability.SCRAPPY);this.add(Ability.INNER_FOCUS);}};
perName.put(ctx.getString(R.string.name_kangaskhan), new Pokemon(ctx.getString(R.string.name_kangaskhan), 115, 121, Type.NORMAL, Type.NONE, abilities, 105, 95, 80, 40, 80, 90));
p = perName.get(ctx.getString(R.string.name_kangaskhan));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_kangaskhan)), new HashMap<String, EvolutionNode>(){{this.put("Kangourexite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_kangaskhan)), null));}});
p.catchRate = 45;
p.weight = 80.0f;
p.hatch = 5120;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 2.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.FRISK);this.add(Ability.INSOMNIA);}};
perName.put(ctx.getString(R.string.name_pumpkaboo_average_size), new Pokemon(ctx.getString(R.string.name_pumpkaboo_average_size), 710, 758, Type.GHOST, Type.GRASS, abilities, 49, 66, 70, 44, 55, 51));
p = perName.get(ctx.getString(R.string.name_pumpkaboo_average_size));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pumpkaboo_average_size)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_gourgeist_average_size)), null));}});
p.catchRate = -1;
p.weight = 3.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.WATER_VEIL);this.add(Ability.OBLIVIOUS);}};
perName.put(ctx.getString(R.string.name_wailord), new Pokemon(ctx.getString(R.string.name_wailord), 321, 344, Type.WATER, Type.NONE, abilities, 170, 90, 45, 90, 45, 60));
p = perName.get(ctx.getString(R.string.name_wailord));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_wailmer)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_wailord)), null));}});
p.catchRate = 60;
p.weight = 398.0f;
p.hatch = 10240;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.WATER2};
p.size = 14.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.VITAL_SPIRIT);this.add(Ability.ANGER_POINT);this.add(Ability.DEFIANT);}};
perName.put(ctx.getString(R.string.name_primeape), new Pokemon(ctx.getString(R.string.name_primeape), 57, 61, Type.FIGHTING, Type.NONE, abilities, 65, 105, 60, 60, 70, 95));
p = perName.get(ctx.getString(R.string.name_primeape));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mankey)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "28", new EvolutionNode(perName.get(ctx.getString(R.string.name_primeape)), null));}});
p.catchRate = 75;
p.weight = 32.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.DARK_AURA);}};
perName.put(ctx.getString(R.string.name_yveltal), new Pokemon(ctx.getString(R.string.name_yveltal), 717, 770, Type.DARK, Type.FLYING, abilities, 126, 131, 95, 131, 98, 99));
p = perName.get(ctx.getString(R.string.name_yveltal));
p.evolutions = null;
p.catchRate = 30;
p.weight = 203.0f;
p.hatch = -1;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 5.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRANKSTER);this.add(Ability.DEFIANT);}};
perName.put(ctx.getString(R.string.name_thundurus_therian_forme), new Pokemon(ctx.getString(R.string.name_thundurus_therian_forme), 642, 685, Type.ELECTRIC, Type.FLYING, abilities, 79, 105, 70, 145, 80, 101));
p = perName.get(ctx.getString(R.string.name_thundurus_therian_forme));
p.evolutions = null;
p.catchRate = 3;
p.weight = 65f;
p.hatch = 30855;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HUSTLE);this.add(Ability.NATURAL_CURE);}};
perName.put(ctx.getString(R.string.name_corsola), new Pokemon(ctx.getString(R.string.name_corsola), 222, 237, Type.WATER, Type.ROCK, abilities, 55, 55, 85, 65, 85, 35));
p = perName.get(ctx.getString(R.string.name_corsola));
p.evolutions = null;
p.catchRate = 45;
p.weight = 5.0f;
p.hatch = 5376;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER3};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GUTS);this.add(Ability.NO_GUARD);this.add(Ability.STEADFAST);}};
perName.put(ctx.getString(R.string.name_machamp), new Pokemon(ctx.getString(R.string.name_machamp), 68, 73, Type.FIGHTING, Type.NONE, abilities, 90, 130, 80, 65, 85, 55));
p = perName.get(ctx.getString(R.string.name_machamp));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_machop)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "28", new EvolutionNode(perName.get(ctx.getString(R.string.name_machoke)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_machamp)), null));}}));}});
p.catchRate = 45;
p.weight = 130.0f;
p.hatch = 5120;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BATTLE_ARMOR);this.add(Ability.SNIPER);this.add(Ability.KEEN_EYE);}};
perName.put(ctx.getString(R.string.name_skorupi), new Pokemon(ctx.getString(R.string.name_skorupi), 451, 483, Type.POISON, Type.BUG, abilities, 40, 50, 90, 30, 55, 65));
p = perName.get(ctx.getString(R.string.name_skorupi));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_skorupi)), new HashMap<String, EvolutionNode>(){{this.put("niveau 40", new EvolutionNode(perName.get(ctx.getString(R.string.name_drapion)), null));}});
p.catchRate = 120;
p.weight = 12.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG,EggGroup.WATER3};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GLUTTONY);this.add(Ability.OVERGROW);}};
perName.put(ctx.getString(R.string.name_simisage), new Pokemon(ctx.getString(R.string.name_simisage), 512, 552, Type.GRASS, Type.NONE, abilities, 75, 98, 63, 98, 63, 101));
p = perName.get(ctx.getString(R.string.name_simisage));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pansage)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get(ctx.getString(R.string.name_simisage)), null));}});
p.catchRate = 75;
p.weight = 30.5f;
p.hatch = 5355;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GUTS);this.add(Ability.QUICK_FEET);this.add(Ability.UNNERVE);}};
perName.put(ctx.getString(R.string.name_ursaring), new Pokemon(ctx.getString(R.string.name_ursaring), 217, 232, Type.NORMAL, Type.NONE, abilities, 90, 130, 75, 75, 75, 55));
p = perName.get(ctx.getString(R.string.name_ursaring));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_teddiursa)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_ursaring)), null));}});
p.catchRate = 60;
p.weight = 125.8f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BATTLE_ARMOR);this.add(Ability.SWIFT_SWIM);}};
perName.put(ctx.getString(R.string.name_anorith), new Pokemon(ctx.getString(R.string.name_anorith), 347, 370, Type.ROCK, Type.BUG, abilities, 45, 95, 50, 40, 50, 75));
p = perName.get(ctx.getString(R.string.name_anorith));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_anorith)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_armaldo)), null));}});
p.catchRate = 45;
p.weight = 12.5f;
p.hatch = 7680;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER3};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OVERGROW);this.add(Ability.CONTRARY);}};
perName.put(ctx.getString(R.string.name_snivy), new Pokemon(ctx.getString(R.string.name_snivy), 495, 535, Type.GRASS, Type.NONE, abilities, 45, 45, 55, 45, 55, 63));
p = perName.get(ctx.getString(R.string.name_snivy));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_snivy)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "17", new EvolutionNode(perName.get(ctx.getString(R.string.name_servine)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_serperior)), null));}}));}});
p.catchRate = 45;
p.weight = 8.1f;
p.hatch = 5355;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.GRASS};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SYNCHRONIZE);this.add(Ability.TRACE);this.add(Ability.TELEPATHY);}};
perName.put(ctx.getString(R.string.name_gardevoir), new Pokemon(ctx.getString(R.string.name_gardevoir), 282, 300, Type.PSYCHIC, Type.NONE, abilities, 68, 65, 65, 125, 115, 80));
p = perName.get(ctx.getString(R.string.name_gardevoir));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_ralts)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_kirlia)), new HashMap<String, EvolutionNode>(){{this.put("Male + Pierre Aube", new EvolutionNode(perName.get(ctx.getString(R.string.name_gallade)), null));this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_gardevoir)), new HashMap<String, EvolutionNode>(){{this.put("Gardevoirite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_gardevoir)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 48.4f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GUTS);this.add(Ability.SWARM);this.add(Ability.MOXIE);}};
perName.put(ctx.getString(R.string.name_heracross), new Pokemon(ctx.getString(R.string.name_heracross), 214, 228, Type.BUG, Type.FIGHTING, abilities, 80, 125, 75, 40, 95, 85));
p = perName.get(ctx.getString(R.string.name_heracross));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_heracross)), new HashMap<String, EvolutionNode>(){{this.put("Scarhinoite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_heracross)), null));}});
p.catchRate = 45;
p.weight = 54.0f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLASH_FIRE);this.add(Ability.EARLY_BIRD);this.add(Ability.UNNERVE);}};
perName.put(ctx.getString(R.string.name_houndoom), new Pokemon(ctx.getString(R.string.name_houndoom), 229, 244, Type.DARK, Type.FIRE, abilities, 75, 90, 50, 110, 80, 95));
p = perName.get(ctx.getString(R.string.name_houndoom));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_houndour)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "24", new EvolutionNode(perName.get(ctx.getString(R.string.name_houndoom)), new HashMap<String, EvolutionNode>(){{this.put("Demolossite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_houndoom)), null));}}));}});
p.catchRate = 4;
p.weight = 35.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.POISON_TOUCH);this.add(Ability.WATER_ABSORB);}};
perName.put(ctx.getString(R.string.name_seismitoad), new Pokemon(ctx.getString(R.string.name_seismitoad), 537, 577, Type.WATER, Type.GROUND, abilities, 105, 85, 75, 85, 75, 74));
p = perName.get(ctx.getString(R.string.name_seismitoad));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tympole)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_palpitoad)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_seismitoad)), null));}}));}});
p.catchRate = 45;
p.weight = 62.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.SHELL_ARMOR);this.add(Ability.WEAK_ARMOR);}};
perName.put(ctx.getString(R.string.name_crustle), new Pokemon(ctx.getString(R.string.name_crustle), 558, 599, Type.BUG, Type.ROCK, abilities, 70, 95, 125, 65, 75, 45));
p = perName.get(ctx.getString(R.string.name_crustle));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_dwebble)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "34", new EvolutionNode(perName.get(ctx.getString(R.string.name_crustle)), null));}});
p.catchRate = 75;
p.weight = 200.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG,EggGroup.MINERAL};
p.size = 1.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RIVALRY);this.add(Ability.MOLD_BREAKER);this.add(Ability.UNNERVE);}};
perName.put(ctx.getString(R.string.name_haxorus), new Pokemon(ctx.getString(R.string.name_haxorus), 612, 653, Type.DRAGON, Type.NONE, abilities, 76, 147, 90, 60, 70, 97));
p = perName.get(ctx.getString(R.string.name_haxorus));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_axew)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "38", new EvolutionNode(perName.get(ctx.getString(R.string.name_fraxure)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "48", new EvolutionNode(perName.get(ctx.getString(R.string.name_haxorus)), null));}}));}});
p.catchRate = 45;
p.weight = 105.5f;
p.hatch = 10455;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.DRAGON};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);this.add(Ability.UNNERVE);}};
perName.put(ctx.getString(R.string.name_mewtwo), new Pokemon(ctx.getString(R.string.name_mewtwo), 150, 160, Type.PSYCHIC, Type.NONE, abilities, 106, 110, 90, 154, 90, 130));
p = perName.get(ctx.getString(R.string.name_mewtwo));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mewtwo)), new HashMap<String, EvolutionNode>(){{this.put("Mewtwoite X", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_mewtwo_x)), null));this.put("Mewtwoite Y", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_mewtwo_y)), null));}});
p.catchRate = 3;
p.weight = 122.0f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BLAZE);this.add(Ability.FLASH_FIRE);}};
perName.put(ctx.getString(R.string.name_quilava), new Pokemon(ctx.getString(R.string.name_quilava), 156, 168, Type.FIRE, Type.NONE, abilities, 58, 64, 58, 80, 65, 80));
p = perName.get(ctx.getString(R.string.name_quilava));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cyndaquil)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "14", new EvolutionNode(perName.get(ctx.getString(R.string.name_quilava)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_typhlosion)), null));}}));}});
p.catchRate = 45;
p.weight = 19f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.ROCK_HEAD);this.add(Ability.HEAVY_METAL);}};
perName.put(ctx.getString(R.string.name_aggron), new Pokemon(ctx.getString(R.string.name_aggron), 306, 326, Type.STEEL, Type.ROCK, abilities, 70, 110, 180, 60, 60, 50));
p = perName.get(ctx.getString(R.string.name_aggron));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_aron)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_lairon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "42", new EvolutionNode(perName.get(ctx.getString(R.string.name_aggron)), new HashMap<String, EvolutionNode>(){{this.put("Galekingite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_aggron)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 360.0f;
p.hatch = 8960;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 2.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ILLUMINATE);this.add(Ability.KEEN_EYE);this.add(Ability.ANALYTIC);}};
perName.put(ctx.getString(R.string.name_watchog), new Pokemon(ctx.getString(R.string.name_watchog), 505, 545, Type.NORMAL, Type.NONE, abilities, 60, 85, 69, 60, 69, 77));
p = perName.get(ctx.getString(R.string.name_watchog));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_patrat)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_watchog)), null));}});
p.catchRate = 255;
p.weight = 27f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_STREAM);this.add(Ability.UNNERVE);}};
perName.put(ctx.getString(R.string.name_tyranitar), new Pokemon(ctx.getString(R.string.name_tyranitar), 248, 264, Type.ROCK, Type.DARK, abilities, 100, 134, 110, 95, 100, 61));
p = perName.get(ctx.getString(R.string.name_tyranitar));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_larvitar)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_pupitar)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "55", new EvolutionNode(perName.get(ctx.getString(R.string.name_tyranitar)), new HashMap<String, EvolutionNode>(){{this.put("Tyranocivite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_tyranitar)), null));}}));}}));}});
p.catchRate = 45;
p.weight = 202.0f;
p.hatch = 10240;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HYPER_CUTTER);this.add(Ability.SAND_VEIL);this.add(Ability.POISON_HEAL);}};
perName.put(ctx.getString(R.string.name_gliscor), new Pokemon(ctx.getString(R.string.name_gliscor), 472, 505, Type.GROUND, Type.FLYING, abilities, 75, 95, 125, 45, 75, 95));
p = perName.get(ctx.getString(R.string.name_gliscor));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_gligar)), new HashMap<String, EvolutionNode>(){{this.put("Gagne un niveau de nuit en tenant un Croc Rasoir", new EvolutionNode(perName.get(ctx.getString(R.string.name_gliscor)), null));}});
p.catchRate = 30;
p.weight = 42.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.WATER_ABSORB);}};
perName.put(ctx.getString(R.string.name_mantine), new Pokemon(ctx.getString(R.string.name_mantine), 226, 241, Type.WATER, Type.FLYING, abilities, 65, 40, 70, 80, 140, 70));
p = perName.get(ctx.getString(R.string.name_mantine));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mantyke)), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau avec Remoraid dans l'equipe", new EvolutionNode(perName.get(ctx.getString(R.string.name_mantine)), null));}});
p.catchRate = 25;
p.weight = 220.0f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1};
p.size = 2.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_solrock), new Pokemon(ctx.getString(R.string.name_solrock), 338, 361, Type.ROCK, Type.PSYCHIC, abilities, 70, 95, 85, 55, 65, 70));
p = perName.get(ctx.getString(R.string.name_solrock));
p.evolutions = null;
p.catchRate = 45;
p.weight = 154.0f;
p.hatch = 6400;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BIG_PECKS);this.add(Ability.GALE_WINGS);}};
perName.put(ctx.getString(R.string.name_fletchling), new Pokemon(ctx.getString(R.string.name_fletchling), 661, 707, Type.NORMAL, Type.FLYING, abilities, 45, 50, 43, 40, 38, 62));
p = perName.get(ctx.getString(R.string.name_fletchling));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_fletchling)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "17", new EvolutionNode(perName.get(ctx.getString(R.string.name_fletchinder)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_talonflame)), null));}}));}});
p.catchRate = -1;
p.weight = 1.7f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SKILL_LINK);}};
perName.put(ctx.getString(R.string.name_mega_heracross), new Pokemon(ctx.getString(R.string.name_mega_heracross), 214, 229, Type.BUG, Type.FIGHTING, abilities, 80, 185, 115, 40, 105, 75));
p = perName.get(ctx.getString(R.string.name_mega_heracross));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_heracross)), new HashMap<String, EvolutionNode>(){{this.put("Scarhinoite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_heracross)), null));}});
p.catchRate = -1;
p.weight = 62.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TORRENT);this.add(Ability.DAMP);}};
perName.put(ctx.getString(R.string.name_marshtomp), new Pokemon(ctx.getString(R.string.name_marshtomp), 259, 277, Type.WATER, Type.GROUND, abilities, 70, 85, 70, 60, 70, 50));
p = perName.get(ctx.getString(R.string.name_marshtomp));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mudkip)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_marshtomp)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "36", new EvolutionNode(perName.get(ctx.getString(R.string.name_swampert)), null));}}));}});
p.catchRate = 45;
p.weight = 28.0f;
p.hatch = 5120;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.WATER1};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SNOW_CLOAK);}};
perName.put(ctx.getString(R.string.name_piloswine), new Pokemon(ctx.getString(R.string.name_piloswine), 221, 236, Type.ICE, Type.GROUND, abilities, 100, 100, 80, 60, 60, 50));
p = perName.get(ctx.getString(R.string.name_piloswine));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_swinub)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "33", new EvolutionNode(perName.get(ctx.getString(R.string.name_piloswine)), new HashMap<String, EvolutionNode>(){{this.put("En connaissant l'attaque Pouv.Antique", new EvolutionNode(perName.get(ctx.getString(R.string.name_mamoswine)), null));}}));}});
p.catchRate = 75;
p.weight = 55.8f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NATURAL_CURE);this.add(Ability.POISON_POINT);this.add(Ability.TECHNICIAN);}};
perName.put(ctx.getString(R.string.name_roserade), new Pokemon(ctx.getString(R.string.name_roserade), 407, 435, Type.GRASS, Type.POISON, abilities, 60, 70, 55, 125, 105, 90));
p = perName.get(ctx.getString(R.string.name_roserade));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_budew)), new HashMap<String, EvolutionNode>(){{this.put("Bonheur , Jour", new EvolutionNode(perName.get(ctx.getString(R.string.name_roselia)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get(ctx.getString(R.string.name_roserade)), null));}}));}});
p.catchRate = 75;
p.weight = 14.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY,EggGroup.GRASS};
p.size = 0.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OBLIVIOUS);this.add(Ability.SIMPLE);}};
perName.put(ctx.getString(R.string.name_numel), new Pokemon(ctx.getString(R.string.name_numel), 322, 345, Type.FIRE, Type.GROUND, abilities, 60, 60, 40, 65, 45, 35));
p = perName.get(ctx.getString(R.string.name_numel));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_numel)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "33", new EvolutionNode(perName.get(ctx.getString(R.string.name_camerupt)), null));}});
p.catchRate = 255;
p.weight = 24.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LIMBER);this.add(Ability.UNBURDEN);this.add(Ability.PRANKSTER);}};
perName.put(ctx.getString(R.string.name_purrloin), new Pokemon(ctx.getString(R.string.name_purrloin), 509, 549, Type.DARK, Type.NONE, abilities, 41, 50, 37, 50, 37, 66));
p = perName.get(ctx.getString(R.string.name_purrloin));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_purrloin)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_liepard)), null));}});
p.catchRate = 255;
p.weight = 10.1f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INFILTRATOR);this.add(Ability.KEEN_EYE);this.add(Ability.OWN_TEMPO);}};
perName.put(ctx.getString(R.string.name_espurr), new Pokemon(ctx.getString(R.string.name_espurr), 677, 723, Type.PSYCHIC, Type.NONE, abilities, 60, 22, 62, 72, 72, 95));
p = perName.get(ctx.getString(R.string.name_espurr));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_espurr)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_meowstic)), null));}});
p.catchRate = -1;
p.weight = 3.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FRISK);this.add(Ability.COMPETITIVE);this.add(Ability.SHADOW_TAG);}};
perName.put(ctx.getString(R.string.name_gothita), new Pokemon(ctx.getString(R.string.name_gothita), 574, 615, Type.PSYCHIC, Type.NONE, abilities, 45, 30, 50, 55, 65, 45));
p = perName.get(ctx.getString(R.string.name_gothita));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_gothita)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_gothorita)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "41", new EvolutionNode(perName.get(ctx.getString(R.string.name_gothitelle)), null));}}));}});
p.catchRate = 200;
p.weight = 5.8f;
p.hatch = 5355;
p.gender = 75f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.REGENERATOR);this.add(Ability.INNER_FOCUS);this.add(Ability.RECKLESS);}};
perName.put(ctx.getString(R.string.name_mienfoo), new Pokemon(ctx.getString(R.string.name_mienfoo), 619, 660, Type.FIGHTING, Type.NONE, abilities, 45, 85, 50, 55, 50, 65));
p = perName.get(ctx.getString(R.string.name_mienfoo));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mienfoo)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "50", new EvolutionNode(perName.get(ctx.getString(R.string.name_mienshao)), null));}});
p.catchRate = 180;
p.weight = 20.0f;
p.hatch = 6630;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.HUMANLIKE};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SNOW_CLOAK);this.add(Ability.CURSED_BODY);}};
perName.put(ctx.getString(R.string.name_froslass), new Pokemon(ctx.getString(R.string.name_froslass), 478, 511, Type.ICE, Type.GHOST, abilities, 70, 80, 70, 80, 70, 110));
p = perName.get(ctx.getString(R.string.name_froslass));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_snorunt)), new HashMap<String, EvolutionNode>(){{this.put("Femelle + Pierre Aube", new EvolutionNode(perName.get(ctx.getString(R.string.name_froslass)), null));this.put(ctx.getString(R.string.level) + "42", new EvolutionNode(perName.get(ctx.getString(R.string.name_glalie)), null));}});
p.catchRate = 75;
p.weight = 26.6f;
p.hatch = 5120;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY,EggGroup.MINERAL};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LIMBER);this.add(Ability.UNBURDEN);this.add(Ability.PRANKSTER);}};
perName.put(ctx.getString(R.string.name_liepard), new Pokemon(ctx.getString(R.string.name_liepard), 510, 550, Type.DARK, Type.NONE, abilities, 64, 88, 50, 88, 50, 106));
p = perName.get(ctx.getString(R.string.name_liepard));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_purrloin)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_liepard)), null));}});
p.catchRate = 90;
p.weight = 37.5f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);this.add(Ability.REGENERATOR);}};
perName.put(ctx.getString(R.string.name_ho_oh), new Pokemon(ctx.getString(R.string.name_ho_oh), 250, 267, Type.FIRE, Type.FLYING, abilities, 106, 130, 90, 110, 154, 90));
p = perName.get(ctx.getString(R.string.name_ho_oh));
p.evolutions = null;
p.catchRate = 3;
p.weight = 199.0f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 3.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.HYPER_CUTTER);this.add(Ability.SHELL_ARMOR);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_krabby), new Pokemon(ctx.getString(R.string.name_krabby), 98, 104, Type.WATER, Type.NONE, abilities, 30, 105, 90, 25, 25, 50));
p = perName.get(ctx.getString(R.string.name_krabby));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_krabby)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "28", new EvolutionNode(perName.get(ctx.getString(R.string.name_kingler)), null));}});
p.catchRate = 225;
p.weight = 6.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER3};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);this.add(Ability.WATER_ABSORB);}};
perName.put(ctx.getString(R.string.name_suicune), new Pokemon(ctx.getString(R.string.name_suicune), 245, 261, Type.WATER, Type.NONE, abilities, 100, 75, 115, 90, 115, 85));
p = perName.get(ctx.getString(R.string.name_suicune));
p.evolutions = null;
p.catchRate = 3;
p.weight = 187.0f;
p.hatch = 20480;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LIGHTNINGROD);this.add(Ability.MOTOR_DRIVE);this.add(Ability.SAP_SIPPER);}};
perName.put(ctx.getString(R.string.name_zebstrika), new Pokemon(ctx.getString(R.string.name_zebstrika), 523, 563, Type.ELECTRIC, Type.NONE, abilities, 75, 100, 63, 80, 63, 116));
p = perName.get(ctx.getString(R.string.name_zebstrika));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_blitzle)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "27", new EvolutionNode(perName.get(ctx.getString(R.string.name_zebstrika)), null));}});
p.catchRate = 75;
p.weight = 79.5f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHEEK_POUCH);this.add(Ability.PICKUP);this.add(Ability.HUGE_POWER);}};
perName.put(ctx.getString(R.string.name_diggersby), new Pokemon(ctx.getString(R.string.name_diggersby), 660, 706, Type.NORMAL, Type.GROUND, abilities, 85, 56, 77, 50, 77, 78));
p = perName.get(ctx.getString(R.string.name_diggersby));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bunnelby)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_diggersby)), null));}});
p.catchRate = 5;
p.weight = 42.4f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.SAND_VEIL);}};
perName.put(ctx.getString(R.string.name_donphan), new Pokemon(ctx.getString(R.string.name_donphan), 232, 248, Type.GROUND, Type.NONE, abilities, 90, 120, 120, 60, 60, 50));
p = perName.get(ctx.getString(R.string.name_donphan));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_phanpy)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_donphan)), null));}});
p.catchRate = 60;
p.weight = 120.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OWN_TEMPO);this.add(Ability.ICE_BODY);this.add(Ability.STURDY);}};
perName.put(ctx.getString(R.string.name_bergmite), new Pokemon(ctx.getString(R.string.name_bergmite), 712, 765, Type.ICE, Type.NONE, abilities, 55, 69, 85, 32, 35, 28));
p = perName.get(ctx.getString(R.string.name_bergmite));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bergmite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_avalugg)), null));}});
p.catchRate = -1;
p.weight = 99.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.FRISK);this.add(Ability.INSOMNIA);}};
perName.put(ctx.getString(R.string.name_pumpkaboo_super_size), new Pokemon(ctx.getString(R.string.name_pumpkaboo_super_size), 710, 760, Type.GHOST, Type.GRASS, abilities, 59, 66, 70, 44, 55, 41));
p = perName.get(ctx.getString(R.string.name_pumpkaboo_super_size));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pumpkaboo_super_size)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_gourgeist_super_size)), null));}});
p.catchRate = -1;
p.weight = 3.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SNOW_WARNING);this.add(Ability.SOUNDPROOF);}};
perName.put(ctx.getString(R.string.name_snover), new Pokemon(ctx.getString(R.string.name_snover), 459, 491, Type.GRASS, Type.ICE, abilities, 60, 62, 50, 62, 60, 40));
p = perName.get(ctx.getString(R.string.name_snover));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_snover)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_abomasnow)), new HashMap<String, EvolutionNode>(){{this.put("Blizzarite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_abomasnow)), null));}}));}});
p.catchRate = 120;
p.weight = 50.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER,EggGroup.GRASS};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MAGIC_BOUNCE);}};
perName.put(ctx.getString(R.string.name_mega_absol), new Pokemon(ctx.getString(R.string.name_mega_absol), 359, 384, Type.DARK, Type.NONE, abilities, 65, 150, 60, 115, 60, 115));
p = perName.get(ctx.getString(R.string.name_mega_absol));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_absol)), new HashMap<String, EvolutionNode>(){{this.put("Absolite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_absol)), null));}});
p.catchRate = -1;
p.weight = 49.0f;
p.hatch = -1;
p.gender = 100f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CLEAR_BODY);this.add(Ability.STURDY);}};
perName.put(ctx.getString(R.string.name_carbink), new Pokemon(ctx.getString(R.string.name_carbink), 703, 750, Type.ROCK, Type.FAIRY, abilities, 50, 50, 150, 50, 150, 50));
p = perName.get(ctx.getString(R.string.name_carbink));
p.evolutions = null;
p.catchRate = -1;
p.weight = 5.7f;
p.hatch = -1;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY,EggGroup.MINERAL};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRANKSTER);this.add(Ability.MAGICIAN);}};
perName.put(ctx.getString(R.string.name_klefki), new Pokemon(ctx.getString(R.string.name_klefki), 707, 754, Type.STEEL, Type.FAIRY, abilities, 57, 80, 91, 80, 87, 75));
p = perName.get(ctx.getString(R.string.name_klefki));
p.evolutions = null;
p.catchRate = -1;
p.weight = 3.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MINERAL};
p.size = 0.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FORECAST);}};
perName.put(ctx.getString(R.string.name_castform), new Pokemon(ctx.getString(R.string.name_castform), 351, 374, Type.NORMAL, Type.NONE, abilities, 70, 70, 70, 70, 70, 70));
p = perName.get(ctx.getString(R.string.name_castform));
p.evolutions = null;
p.catchRate = 45;
p.weight = 0.8f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY,EggGroup.UNKNOWN};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STURDY);this.add(Ability.KEEN_EYE);this.add(Ability.WEAK_ARMOR);}};
perName.put(ctx.getString(R.string.name_skarmory), new Pokemon(ctx.getString(R.string.name_skarmory), 227, 242, Type.STEEL, Type.FLYING, abilities, 65, 80, 140, 40, 70, 70));
p = perName.get(ctx.getString(R.string.name_skarmory));
p.evolutions = null;
p.catchRate = 25;
p.weight = 50.5f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SOUNDPROOF);this.add(Ability.FILTER);this.add(Ability.TECHNICIAN);}};
perName.put(ctx.getString(R.string.name_mr_mime), new Pokemon(ctx.getString(R.string.name_mr_mime), 122, 129, Type.PSYCHIC, Type.NONE, abilities, 40, 45, 65, 100, 120, 90));
p = perName.get(ctx.getString(R.string.name_mr_mime));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mime_jr)), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l'attaque Copie", new EvolutionNode(perName.get(ctx.getString(R.string.name_mr_mime)), null));}});
p.catchRate = 45;
p.weight = 54.5f;
p.hatch = 6400;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 1.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SYNCHRONIZE);this.add(Ability.EARLY_BIRD);this.add(Ability.MAGIC_BOUNCE);}};
perName.put(ctx.getString(R.string.name_natu), new Pokemon(ctx.getString(R.string.name_natu), 177, 189, Type.PSYCHIC, Type.FLYING, abilities, 40, 50, 45, 70, 45, 70));
p = perName.get(ctx.getString(R.string.name_natu));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_natu)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_xatu)), null));}});
p.catchRate = 190;
p.weight = 2.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 0.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STATIC);}};
perName.put(ctx.getString(R.string.name_flaaffy), new Pokemon(ctx.getString(R.string.name_flaaffy), 180, 192, Type.ELECTRIC, Type.NONE, abilities, 70, 55, 55, 80, 60, 45));
p = perName.get(ctx.getString(R.string.name_flaaffy));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_mareep)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "15", new EvolutionNode(perName.get(ctx.getString(R.string.name_flaaffy)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_ampharos)), new HashMap<String, EvolutionNode>(){{this.put("Pharampite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_ampharos)), null));}}));}}));}});
p.catchRate = 120;
p.weight = 13.3f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.MONSTER};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_FORCE);}};
perName.put(ctx.getString(R.string.name_mega_garchomp), new Pokemon(ctx.getString(R.string.name_mega_garchomp), 445, 476, Type.DRAGON, Type.GROUND, abilities, 108, 170, 115, 120, 95, 92));
p = perName.get(ctx.getString(R.string.name_mega_garchomp));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_gible)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "24", new EvolutionNode(perName.get(ctx.getString(R.string.name_gabite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "48", new EvolutionNode(perName.get(ctx.getString(R.string.name_garchomp)), new HashMap<String, EvolutionNode>(){{this.put("Carchacrokite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_garchomp)), null));}}));}}));}});
p.catchRate = -1;
p.weight = 95.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWARM);this.add(Ability.EARLY_BIRD);this.add(Ability.RATTLED);}};
perName.put(ctx.getString(R.string.name_ledyba), new Pokemon(ctx.getString(R.string.name_ledyba), 165, 177, Type.BUG, Type.FLYING, abilities, 40, 20, 30, 40, 80, 55));
p = perName.get(ctx.getString(R.string.name_ledyba));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_ledyba)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "18", new EvolutionNode(perName.get(ctx.getString(R.string.name_ledian)), null));}});
p.catchRate = 255;
p.weight = 10.8f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 1.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.NATURAL_CURE);}};
perName.put(ctx.getString(R.string.name_shaymin_land_forme), new Pokemon(ctx.getString(R.string.name_shaymin_land_forme), 492, 531, Type.GRASS, Type.NONE, abilities, 100, 100, 100, 100, 100, 100));
p = perName.get(ctx.getString(R.string.name_shaymin_land_forme));
p.evolutions = null;
p.catchRate = 45;
p.weight = 2.1f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PICKUP);this.add(Ability.FRISK);this.add(Ability.INSOMNIA);}};
perName.put(ctx.getString(R.string.name_gourgeist_large_size), new Pokemon(ctx.getString(R.string.name_gourgeist_large_size), 711, 763, Type.GHOST, Type.GRASS, abilities, 75, 95, 122, 58, 75, 69));
p = perName.get(ctx.getString(R.string.name_gourgeist_large_size));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pumpkaboo_large_size)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_gourgeist_large_size)), null));}});
p.catchRate = -1;
p.weight = 9.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_VEIL);this.add(Ability.WATER_ABSORB);}};
perName.put(ctx.getString(R.string.name_cacnea), new Pokemon(ctx.getString(R.string.name_cacnea), 331, 354, Type.GRASS, Type.NONE, abilities, 50, 85, 40, 85, 40, 35));
p = perName.get(ctx.getString(R.string.name_cacnea));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_cacnea)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_cacturne)), null));}});
p.catchRate = 190;
p.weight = 51.3f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS,EggGroup.HUMANLIKE};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_koffing), new Pokemon(ctx.getString(R.string.name_koffing), 109, 115, Type.POISON, Type.NONE, abilities, 40, 65, 95, 60, 45, 35));
p = perName.get(ctx.getString(R.string.name_koffing));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_koffing)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "35", new EvolutionNode(perName.get(ctx.getString(R.string.name_weezing)), null));}});
p.catchRate = 190;
p.weight = 1.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.FLASH_FIRE);this.add(Ability.JUSTIFIED);}};
perName.put(ctx.getString(R.string.name_arcanine), new Pokemon(ctx.getString(R.string.name_arcanine), 59, 63, Type.FIRE, Type.NONE, abilities, 90, 110, 80, 100, 80, 95));
p = perName.get(ctx.getString(R.string.name_arcanine));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_growlithe)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Feu", new EvolutionNode(perName.get(ctx.getString(R.string.name_arcanine)), null));}});
p.catchRate = 75;
p.weight = 155.0f;
p.hatch = 5120;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 1.9f;

abilities = new ArrayList<Ability>(){{this.add(Ability.MARVEL_SCALE);this.add(Ability.COMPETITIVE);this.add(Ability.CUTE_CHARM);}};
perName.put(ctx.getString(R.string.name_milotic), new Pokemon(ctx.getString(R.string.name_milotic), 350, 373, Type.WATER, Type.NONE, abilities, 95, 60, 79, 100, 125, 81));
p = perName.get(ctx.getString(R.string.name_milotic));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_feebas)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "de Beaute superieur ou egal a 170 (3eme et 4eme generations) ou Echange en tenant l'objet Bel'Ecaille (5eme et 6eme generations) ou Tenir le Voile Venus (Pokemon Donjon Mystere)", new EvolutionNode(perName.get(ctx.getString(R.string.name_milotic)), null));}});
p.catchRate = 60;
p.weight = 162.0f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON,EggGroup.WATER1};
p.size = 6.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_VEIL);this.add(Ability.ARENA_TRAP);this.add(Ability.SAND_FORCE);}};
perName.put(ctx.getString(R.string.name_diglett), new Pokemon(ctx.getString(R.string.name_diglett), 50, 54, Type.GROUND, Type.NONE, abilities, 10, 55, 25, 35, 45, 95));
p = perName.get(ctx.getString(R.string.name_diglett));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_diglett)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "26", new EvolutionNode(perName.get(ctx.getString(R.string.name_dugtrio)), null));}});
p.catchRate = 255;
p.weight = 0.8f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.RUN_AWAY);this.add(Ability.PICKUP);this.add(Ability.SKILL_LINK);}};
perName.put(ctx.getString(R.string.name_aipom), new Pokemon(ctx.getString(R.string.name_aipom), 190, 203, Type.NORMAL, Type.NONE, abilities, 55, 70, 55, 40, 55, 85));
p = perName.get(ctx.getString(R.string.name_aipom));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_aipom)), new HashMap<String, EvolutionNode>(){{this.put("En connaissant l'attaque Coup Double", new EvolutionNode(perName.get(ctx.getString(R.string.name_ambipom)), null));}});
p.catchRate = 45;
p.weight = 11.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRANKSTER);this.add(Ability.DEFIANT);}};
perName.put(ctx.getString(R.string.name_thundurus_incarnate_forme), new Pokemon(ctx.getString(R.string.name_thundurus_incarnate_forme), 642, 684, Type.ELECTRIC, Type.FLYING, abilities, 79, 115, 70, 125, 80, 111));
p = perName.get(ctx.getString(R.string.name_thundurus_incarnate_forme));
p.evolutions = null;
p.catchRate = 3;
p.weight = 65f;
p.hatch = 30855;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.GUTS);this.add(Ability.NO_GUARD);this.add(Ability.STEADFAST);}};
perName.put(ctx.getString(R.string.name_machop), new Pokemon(ctx.getString(R.string.name_machop), 66, 71, Type.FIGHTING, Type.NONE, abilities, 70, 80, 50, 35, 35, 35));
p = perName.get(ctx.getString(R.string.name_machop));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_machop)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "28", new EvolutionNode(perName.get(ctx.getString(R.string.name_machoke)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_machamp)), null));}}));}});
p.catchRate = 180;
p.weight = 19.5f;
p.hatch = 5120;
p.gender = 25f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 0.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWIFT_SWIM);this.add(Ability.RAIN_DISH);}};
perName.put(ctx.getString(R.string.name_ludicolo), new Pokemon(ctx.getString(R.string.name_ludicolo), 272, 290, Type.WATER, Type.GRASS, abilities, 80, 70, 70, 90, 100, 70));
p = perName.get(ctx.getString(R.string.name_ludicolo));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_lotad)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "14", new EvolutionNode(perName.get(ctx.getString(R.string.name_lombre)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eau", new EvolutionNode(perName.get(ctx.getString(R.string.name_ludicolo)), null));}}));}});
p.catchRate = 45;
p.weight = 55.0f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.GRASS};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INSOMNIA);this.add(Ability.KEEN_EYE);this.add(Ability.TINTED_LENS);}};
perName.put(ctx.getString(R.string.name_noctowl), new Pokemon(ctx.getString(R.string.name_noctowl), 164, 176, Type.NORMAL, Type.FLYING, abilities, 100, 50, 50, 76, 96, 70));
p = perName.get(ctx.getString(R.string.name_noctowl));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_hoot_hoot)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "20", new EvolutionNode(perName.get(ctx.getString(R.string.name_noctowl)), null));}});
p.catchRate = 90;
p.weight = 40.8f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SERENE_GRACE);}};
perName.put(ctx.getString(R.string.name_meloetta_pirouette_forme), new Pokemon(ctx.getString(R.string.name_meloetta_pirouette_forme), 648, 694, Type.NORMAL, Type.PSYCHIC, abilities, 100, 128, 90, 77, 77, 128));
p = perName.get(ctx.getString(R.string.name_meloetta_pirouette_forme));
p.evolutions = null;
p.catchRate = 5;
p.weight = 6.5f;
p.hatch = 5355;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 0.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SUCTION_CUPS);this.add(Ability.CONTRARY);this.add(Ability.INFILTRATOR);}};
perName.put(ctx.getString(R.string.name_inkay), new Pokemon(ctx.getString(R.string.name_inkay), 686, 733, Type.DARK, Type.PSYCHIC, abilities, 53, 54, 53, 37, 46, 45));
p = perName.get(ctx.getString(R.string.name_inkay));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_inkay)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30, en retournant la 3DS", new EvolutionNode(perName.get(ctx.getString(R.string.name_malamar)), null));}});
p.catchRate = -1;
p.weight = 3.5f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER2};
p.size = 0.4f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SWARM);this.add(Ability.HUSTLE);this.add(Ability.TRUANT);}};
perName.put(ctx.getString(R.string.name_durant), new Pokemon(ctx.getString(R.string.name_durant), 632, 673, Type.BUG, Type.STEEL, abilities, 58, 109, 112, 48, 48, 109));
p = perName.get(ctx.getString(R.string.name_durant));
p.evolutions = null;
p.catchRate = 90;
p.weight = 33.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CLEAR_BODY);this.add(Ability.ICE_BODY);}};
perName.put(ctx.getString(R.string.name_regice), new Pokemon(ctx.getString(R.string.name_regice), 378, 403, Type.ICE, Type.NONE, abilities, 80, 50, 100, 100, 200, 50));
p = perName.get(ctx.getString(R.string.name_regice));
p.evolutions = null;
p.catchRate = 3;
p.weight = 175.0f;
p.hatch = 20480;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.8f;

abilities = new ArrayList<Ability>(){{this.add(Ability.BATTLE_ARMOR);this.add(Ability.SWIFT_SWIM);}};
perName.put(ctx.getString(R.string.name_armaldo), new Pokemon(ctx.getString(R.string.name_armaldo), 348, 371, Type.ROCK, Type.BUG, abilities, 75, 125, 100, 70, 80, 45));
p = perName.get(ctx.getString(R.string.name_armaldo));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_anorith)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "40", new EvolutionNode(perName.get(ctx.getString(R.string.name_armaldo)), null));}});
p.catchRate = 45;
p.weight = 68.2f;
p.hatch = 7680;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER3};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TELEPATHY);this.add(Ability.SYNCHRONIZE);this.add(Ability.ANALYTIC);}};
perName.put(ctx.getString(R.string.name_elgyem), new Pokemon(ctx.getString(R.string.name_elgyem), 605, 646, Type.PSYCHIC, Type.NONE, abilities, 55, 55, 55, 85, 55, 30));
p = perName.get(ctx.getString(R.string.name_elgyem));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_elgyem)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "42", new EvolutionNode(perName.get(ctx.getString(R.string.name_beheeyem)), null));}});
p.catchRate = 255;
p.weight = 9.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.HUMANLIKE};
p.size = 0.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STICKY_HOLD);this.add(Ability.STORM_DRAIN);this.add(Ability.SAND_FORCE);}};
perName.put(ctx.getString(R.string.name_shellos), new Pokemon(ctx.getString(R.string.name_shellos), 422, 452, Type.WATER, Type.NONE, abilities, 76, 48, 48, 57, 62, 34));
p = perName.get(ctx.getString(R.string.name_shellos));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_shellos)), new HashMap<String, EvolutionNode>(){{this.put("niveau 30", new EvolutionNode(perName.get(ctx.getString(R.string.name_gastrodon)), null));}});
p.catchRate = 190;
p.weight = 6.3f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.UNKNOWN};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SAND_FORCE);this.add(Ability.SHEER_FORCE);}};
perName.put(ctx.getString(R.string.name_landorus_therian_forme), new Pokemon(ctx.getString(R.string.name_landorus_therian_forme), 645, 689, Type.GROUND, Type.FLYING, abilities, 89, 145, 90, 105, 80, 91));
p = perName.get(ctx.getString(R.string.name_landorus_therian_forme));
p.evolutions = null;
p.catchRate = 3;
p.weight = 68.0f;
p.hatch = 30855;
p.gender = 0f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.EFFECT_SPORE);this.add(Ability.REGENERATOR);}};
perName.put(ctx.getString(R.string.name_foongus), new Pokemon(ctx.getString(R.string.name_foongus), 590, 631, Type.GRASS, Type.POISON, abilities, 69, 55, 45, 55, 55, 15));
p = perName.get(ctx.getString(R.string.name_foongus));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_foongus)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "39", new EvolutionNode(perName.get(ctx.getString(R.string.name_amoonguss)), null));}});
p.catchRate = 190;
p.weight = 1.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 0.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.CHLOROPHYLL);this.add(Ability.GLUTTONY);}};
perName.put(ctx.getString(R.string.name_victreebel), new Pokemon(ctx.getString(R.string.name_victreebel), 71, 76, Type.GRASS, Type.POISON, abilities, 80, 105, 65, 100, 60, 70));
p = perName.get(ctx.getString(R.string.name_victreebel));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bellsprout)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "21", new EvolutionNode(perName.get(ctx.getString(R.string.name_weepinbell)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get(ctx.getString(R.string.name_victreebel)), null));}}));}});
p.catchRate = 45;
p.weight = 15.5f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.GRASS};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.ROCK_HEAD);this.add(Ability.OVERCOAT);}};
perName.put(ctx.getString(R.string.name_shelgon), new Pokemon(ctx.getString(R.string.name_shelgon), 372, 397, Type.DRAGON, Type.NONE, abilities, 65, 95, 100, 60, 50, 50));
p = perName.get(ctx.getString(R.string.name_shelgon));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bagon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_shelgon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "50", new EvolutionNode(perName.get(ctx.getString(R.string.name_salamence)), null));}}));}});
p.catchRate = 45;
p.weight = 110.5f;
p.hatch = 10240;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON};
p.size = 1.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SHIELD_DUST);this.add(Ability.RUN_AWAY);}};
perName.put(ctx.getString(R.string.name_caterpie), new Pokemon(ctx.getString(R.string.name_caterpie), 10, 14, Type.BUG, Type.NONE, abilities, 45, 30, 35, 20, 20, 45));
p = perName.get(ctx.getString(R.string.name_caterpie));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_caterpie)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "7", new EvolutionNode(perName.get(ctx.getString(R.string.name_metapod)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "10", new EvolutionNode(perName.get(ctx.getString(R.string.name_butterfree)), null));}}));}});
p.catchRate = 255;
p.weight = 2.9f;
p.hatch = 3840;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(1, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 0.3f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STATIC);this.add(Ability.LIMBER);this.add(Ability.SAND_VEIL);}};
perName.put(ctx.getString(R.string.name_stunfisk), new Pokemon(ctx.getString(R.string.name_stunfisk), 618, 659, Type.ELECTRIC, Type.GROUND, abilities, 109, 66, 84, 81, 99, 32));
p = perName.get(ctx.getString(R.string.name_stunfisk));
p.evolutions = null;
p.catchRate = 75;
p.weight = 11.0f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.UNKNOWN};
p.size = 0.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.AFTERMATH);this.add(Ability.UNBURDEN);this.add(Ability.FLARE_BOOST);}};
perName.put(ctx.getString(R.string.name_drifblim), new Pokemon(ctx.getString(R.string.name_drifblim), 426, 456, Type.GHOST, Type.FLYING, abilities, 150, 80, 44, 90, 54, 80));
p = perName.get(ctx.getString(R.string.name_drifblim));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_drifloon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "28", new EvolutionNode(perName.get(ctx.getString(R.string.name_drifblim)), null));}});
p.catchRate = 60;
p.weight = 15.0f;
p.hatch = 7680;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.life_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.FLOWER_VEIL);this.add(Ability.SYMBIOSIS);}};
perName.put(ctx.getString(R.string.name_flabebe), new Pokemon(ctx.getString(R.string.name_flabebe), 669, 715, Type.FAIRY, Type.NONE, abilities, 44, 38, 39, 61, 79, 42));
p = perName.get(ctx.getString(R.string.name_flabebe));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_flabebe)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "19", new EvolutionNode(perName.get(ctx.getString(R.string.name_floette)), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get(ctx.getString(R.string.name_florges)), null));}}));}});
p.catchRate = -1;
p.weight = 0.1f;
p.hatch = -1;
p.gender = 100f;
p.ev = new SparseIntArray(){{this.append(1, R.string.spdef_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FAIRY};
p.size = 0.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.TRACE);}};
perName.put(ctx.getString(R.string.name_mega_alakazam), new Pokemon(ctx.getString(R.string.name_mega_alakazam), 65, 70, Type.PSYCHIC, Type.NONE, abilities, 55, 50, 65, 175, 95, 150));
p = perName.get(ctx.getString(R.string.name_mega_alakazam));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_abra)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "16", new EvolutionNode(perName.get(ctx.getString(R.string.name_kadabra)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_alakazam)), new HashMap<String, EvolutionNode>(){{this.put("Alakazamite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_alakazam)), null));}}));}}));}});
p.catchRate = -1;
p.weight = 48.0f;
p.hatch = -1;
p.gender = 25f;
p.ev = new SparseIntArray(){{}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.POISON_POINT);this.add(Ability.SWARM);this.add(Ability.QUICK_FEET);}};
perName.put(ctx.getString(R.string.name_scolipede), new Pokemon(ctx.getString(R.string.name_scolipede), 545, 585, Type.BUG, Type.POISON, abilities, 60, 90, 89, 55, 69, 112));
p = perName.get(ctx.getString(R.string.name_scolipede));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_venipede)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "22", new EvolutionNode(perName.get(ctx.getString(R.string.name_whirlipede)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_scolipede)), null));}}));}});
p.catchRate = 45;
p.weight = 200.5f;
p.hatch = 5355;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.speed_short);}};
p.eggGroup = new EggGroup[]{EggGroup.BUG};
p.size = 2.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);}};
perName.put(ctx.getString(R.string.name_deoxys_normal_forme), new Pokemon(ctx.getString(R.string.name_deoxys_normal_forme), 386, 411, Type.PSYCHIC, Type.NONE, abilities, 50, 150, 50, 150, 50, 150));
p = perName.get(ctx.getString(R.string.name_deoxys_normal_forme));
p.evolutions = null;
p.catchRate = 3;
p.weight = 60.8f;
p.hatch = 30720;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(1, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 1.7f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SOLID_ROCK);this.add(Ability.STURDY);this.add(Ability.SWIFT_SWIM);}};
perName.put(ctx.getString(R.string.name_carracosta), new Pokemon(ctx.getString(R.string.name_carracosta), 565, 606, Type.WATER, Type.ROCK, abilities, 74, 108, 133, 83, 65, 32));
p = perName.get(ctx.getString(R.string.name_carracosta));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tirtouga)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_carracosta)), null));}});
p.catchRate = 45;
p.weight = 81.0f;
p.hatch = 7905;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.WATER1,EggGroup.WATER3};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.SUPER_LUCK);this.add(Ability.BIG_PECKS);this.add(Ability.RIVALRY);}};
perName.put(ctx.getString(R.string.name_unfezant), new Pokemon(ctx.getString(R.string.name_unfezant), 521, 561, Type.NORMAL, Type.FLYING, abilities, 80, 105, 80, 65, 55, 93));
p = perName.get(ctx.getString(R.string.name_unfezant));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pidove)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "21", new EvolutionNode(perName.get(ctx.getString(R.string.name_tranquill)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32", new EvolutionNode(perName.get(ctx.getString(R.string.name_unfezant)), null));}}));}});
p.catchRate = 45;
p.weight = 29.0f;
p.hatch = 4080;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FLYING};
p.size = 1.2f;

abilities = new ArrayList<Ability>(){{this.add(Ability.LEVITATE);}};
perName.put(ctx.getString(R.string.name_haunter), new Pokemon(ctx.getString(R.string.name_haunter), 93, 98, Type.GHOST, Type.POISON, abilities, 45, 50, 45, 115, 55, 95));
p = perName.get(ctx.getString(R.string.name_haunter));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_gastly)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "25", new EvolutionNode(perName.get(ctx.getString(R.string.name_haunter)), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get(ctx.getString(R.string.name_gengar)), new HashMap<String, EvolutionNode>(){{this.put("Ectoplasmite", new EvolutionNode(perName.get(ctx.getString(R.string.name_mega_gengar)), null));}}));}}));}});
p.catchRate = 90;
p.weight = 0.1f;
p.hatch = 5120;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.UNKNOWN};
p.size = 1.6f;

abilities = new ArrayList<Ability>(){{this.add(Ability.IRON_FIST);this.add(Ability.MOLD_BREAKER);this.add(Ability.SCRAPPY);}};
perName.put(ctx.getString(R.string.name_pangoro), new Pokemon(ctx.getString(R.string.name_pangoro), 675, 721, Type.FIGHTING, Type.DARK, abilities, 95, 124, 78, 69, 71, 58));
p = perName.get(ctx.getString(R.string.name_pangoro));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_pancham)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "32, avec un Pokemon dans l'equipe", new EvolutionNode(perName.get(ctx.getString(R.string.name_pangoro)), null));}});
p.catchRate = -1;
p.weight = 136.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.FIELD,EggGroup.HUMANLIKE};
p.size = 2.1f;

abilities = new ArrayList<Ability>(){{this.add(Ability.STRONG_JAW);}};
perName.put(ctx.getString(R.string.name_tyrantrum), new Pokemon(ctx.getString(R.string.name_tyrantrum), 697, 744, Type.ROCK, Type.DRAGON, abilities, 82, 121, 119, 69, 59, 71));
p = perName.get(ctx.getString(R.string.name_tyrantrum));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_tyrunt)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "39 pendant la journee", new EvolutionNode(perName.get(ctx.getString(R.string.name_tyrantrum)), null));}});
p.catchRate = -1;
p.weight = 270.0f;
p.hatch = -1;
p.gender = 12.5f;
p.ev = new SparseIntArray(){{this.append(2, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.PRESSURE);this.add(Ability.FLAME_BODY);}};
perName.put(ctx.getString(R.string.name_moltres), new Pokemon(ctx.getString(R.string.name_moltres), 146, 156, Type.FIRE, Type.FLYING, abilities, 90, 100, 90, 125, 85, 90));
p = perName.get(ctx.getString(R.string.name_moltres));
p.evolutions = null;
p.catchRate = 3;
p.weight = 60.0f;
p.hatch = 20480;
p.gender = -1f;
p.ev = new SparseIntArray(){{this.append(3, R.string.spatt_short);}};
p.eggGroup = new EggGroup[]{EggGroup.NO_EGG};
p.size = 2.0f;

abilities = new ArrayList<Ability>(){{this.add(Ability.INTIMIDATE);this.add(Ability.MOXIE);}};
perName.put(ctx.getString(R.string.name_salamence), new Pokemon(ctx.getString(R.string.name_salamence), 373, 398, Type.DRAGON, Type.FLYING, abilities, 95, 135, 80, 110, 80, 100));
p = perName.get(ctx.getString(R.string.name_salamence));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bagon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "30", new EvolutionNode(perName.get(ctx.getString(R.string.name_shelgon)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "50", new EvolutionNode(perName.get(ctx.getString(R.string.name_salamence)), null));}}));}});
p.catchRate = 45;
p.weight = 102.6f;
p.hatch = 10240;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(3, R.string.att_short);}};
p.eggGroup = new EggGroup[]{EggGroup.DRAGON};
p.size = 1.5f;

abilities = new ArrayList<Ability>(){{this.add(Ability.OWN_TEMPO);this.add(Ability.ICE_BODY);this.add(Ability.STURDY);}};
perName.put(ctx.getString(R.string.name_avalugg), new Pokemon(ctx.getString(R.string.name_avalugg), 713, 766, Type.ICE, Type.NONE, abilities, 95, 117, 184, 44, 46, 28));
p = perName.get(ctx.getString(R.string.name_avalugg));
p.evolutions = new EvolutionNode(perName.get(ctx.getString(R.string.name_bergmite)), new HashMap<String, EvolutionNode>(){{this.put(ctx.getString(R.string.level) + "37", new EvolutionNode(perName.get(ctx.getString(R.string.name_avalugg)), null));}});
p.catchRate = -1;
p.weight = 505.0f;
p.hatch = -1;
p.gender = 50f;
p.ev = new SparseIntArray(){{this.append(2, R.string.def_short);}};
p.eggGroup = new EggGroup[]{EggGroup.MONSTER};
p.size = 2.0f;
"""



main(data)

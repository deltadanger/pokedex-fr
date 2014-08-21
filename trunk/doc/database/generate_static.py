from app.models import EggGroup, PokemonType

def main(data):
    for group in data["egg_groups"]:
        EggGroup.objects.get_or_create(name=group)
    
    for typekw in data["types"]:
        PokemonType.objects.get_or_create(**typekw)

data = {
    "egg_groups": [
        "R.string.egg_group_flying",
        "R.string.egg_group_amorphous",
        "R.string.egg_group_water1",
        "R.string.egg_group_water2",
        "R.string.egg_group_water3",
        "R.string.egg_group_dragon",
        "R.string.egg_group_fairy",
        "R.string.egg_group_humanlike",
        "R.string.egg_group_unknown",
        "R.string.egg_group_bug",
        "R.string.egg_group_ditto",
        "R.string.egg_group_mineral",
        "R.string.egg_group_monster",
        "R.string.egg_group_field",
        "R.string.egg_group_grass",
        "R.string.egg_group_no_egg",
    ],
    "types": [
        {"name": "NONE", "image":"0"},
        {"name": "STEEL", "image":"R.drawable.steel"},
        {"name": "FIGHTING", "image":"R.drawable.fighting"},
        {"name": "DRAGON", "image":"R.drawable.dragon"},
        {"name": "WATER", "image":"R.drawable.water"},
        {"name": "ELECTRIC", "image":"R.drawable.electric"},
        {"name": "FAIRY", "image":"R.drawable.fairy"},
        {"name": "FIRE", "image":"R.drawable.fire"},
        {"name": "ICE", "image":"R.drawable.ice"},
        {"name": "BUG", "image":"R.drawable.bug"},
        {"name": "NORMAL", "image":"R.drawable.normal"},
        {"name": "GRASS", "image":"R.drawable.grass"},
        {"name": "POISON", "image":"R.drawable.poison"},
        {"name": "PSYCHIC", "image":"R.drawable.psychic"},
        {"name": "ROCK", "image":"R.drawable.rock"},
        {"name": "GROUND", "image":"R.drawable.ground"},
        {"name": "GHOST", "image":"R.drawable.ghost"},
        {"name": "DARK", "image":"R.drawable.dark"},
        {"name": "FLYING", "image":"R.drawable.flying"},
    ]
}


main(data)
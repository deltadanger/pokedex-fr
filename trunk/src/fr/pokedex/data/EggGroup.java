package fr.pokedex.data;

import fr.pokedex.R;

public enum EggGroup {
    FLYING(R.string.egg_group_flying),
    AMORPHOUS(R.string.egg_group_amorphous),
    WATER1(R.string.egg_group_water1),
    WATER2(R.string.egg_group_water2),
    WATER3(R.string.egg_group_water3),
    DRAGON(R.string.egg_group_dragon),
    FAIRY(R.string.egg_group_fairy),
    HUMANLIKE(R.string.egg_group_humanlike),
    UNKNOWN(R.string.egg_group_unknown),
    BUG(R.string.egg_group_bug),
    DITTO(R.string.egg_group_ditto),
    MINERAL(R.string.egg_group_mineral),
    MONSTER(R.string.egg_group_monster),
    FIELD(R.string.egg_group_field),
    GRASS(R.string.egg_group_grass),
    NO_EGG(R.string.egg_group_no_egg);
    
    public int name;
    
    EggGroup(int name) {
        this.name = name;
    };
}

package fr.pokedex.data;

import fr.pokedex.R;


public enum Type {
    NONE (0),
    STEEL (R.drawable.steel),
    FIGHTING (R.drawable.fighting),
    DRAGON (R.drawable.dragon),
    WATER (R.drawable.water),
    ELECTRIC (R.drawable.electric),
    FAIRY (R.drawable.fairy),
    FIRE (R.drawable.fire),
    ICE (R.drawable.ice),
    BUG (R.drawable.bug),
    NORMAL (R.drawable.normal),
    GRASS (R.drawable.grass),
    POISON (R.drawable.poison),
    PSYCHIC (R.drawable.psychic),
    ROCK (R.drawable.rock),
    GROUND (R.drawable.ground),
    GHOST (R.drawable.ghost),
    DARK (R.drawable.dark),
    FLYING (R.drawable.flying);

    public int image;
    private Type(int image) {
        this.image = image;
    }
}

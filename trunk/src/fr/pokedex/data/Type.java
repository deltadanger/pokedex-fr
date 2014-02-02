package fr.pokedex.data;

import fr.pokedex.R;


public enum Type {
    NONE (0),
    ACIER (R.drawable.acier),
    COMBAT (R.drawable.combat),
    DRAGON (R.drawable.dragon),
    EAU (R.drawable.eau),
    ELECTRIQUE (R.drawable.electrique),
    FEE (R.drawable.fee),
    FEU (R.drawable.feu),
    GLACE (R.drawable.glace),
    INSECTE (R.drawable.insecte),
    NORMAL (R.drawable.normal),
    PLANTE (R.drawable.plante),
    POISON (R.drawable.poison),
    PSY (R.drawable.psy),
    ROCHE (R.drawable.roche),
    SOL (R.drawable.sol),
    SPECTRE (R.drawable.spectre),
    TENEBRE (R.drawable.tenebre),
    VOL (R.drawable.vol);
    
    public int image;
    private Type(int image) {
        this.image = image;
    }
}

package fr.pokedex.data;

import fr.pokedex.R;


public enum Weakness implements Comparable<Weakness> {
    VERY_WEAK (R.drawable.weakness_very_weak),
    WEAK (R.drawable.weakness_weak),
    NORMAL (R.drawable.weakness_normal),
    STRONG (R.drawable.weakness_strong),
    VERY_STRONG (R.drawable.weakness_very_strong),
    IGNORE (R.drawable.weakness_ignore);
    
    public int resource;
    private Weakness(int r) {
    	this.resource = r;
	}
    
    public Weakness increase() {
    	if (Weakness.WEAK.equals(this)) {
    		return Weakness.VERY_WEAK;
    	} else if (Weakness.NORMAL.equals(this)) {
    		return Weakness.WEAK;
    	} else if (Weakness.STRONG.equals(this)) {
    		return Weakness.NORMAL;
    	}
    	return this;
    }
    
    public Weakness decrease() {
    	if (Weakness.STRONG.equals(this)) {
    		return Weakness.VERY_STRONG;
    	} else if (Weakness.NORMAL.equals(this)) {
    		return Weakness.STRONG;
    	} else if (Weakness.WEAK.equals(this)) {
    		return Weakness.NORMAL;
    	}
    	return this;
    }
}

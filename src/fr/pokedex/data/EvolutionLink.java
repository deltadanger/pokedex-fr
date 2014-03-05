package fr.pokedex.data;

import java.util.HashMap;

public class EvolutionLink {
    public Pokemon base;
    
    public HashMap<String, EvolutionLink> evolutions;
    
    public EvolutionLink(Pokemon base, HashMap<String, EvolutionLink> evolutions) {
        this.base = base;
        this.evolutions = evolutions;
    }
}

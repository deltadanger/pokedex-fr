package fr.pokedex.data;

import java.util.HashMap;

public class EvolutionNode {
    public Pokemon base;
    
    public HashMap<String, EvolutionNode> evolutions;
    
    public EvolutionNode(Pokemon base, HashMap<String, EvolutionNode> evolutions) {
        this.base = base;
        this.evolutions = evolutions;
    }
}

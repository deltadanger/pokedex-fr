package fr.pokedex.data;

import java.util.ArrayList;
import java.util.HashMap;


public class Pokemon {
    
    @SuppressWarnings("serial")
    public static Pokemon UNKNOWN = new Pokemon("Unknown", 0, 0, Type.NONE, Type.NONE, new ArrayList<Talent>(){{this.add(Talent.ERREUR);}}, 0, 0, 0, 0, 0, 0){{this.evolutions = null;}};
    
    public String name;
    public int number;
    public int index;
    
    public Type type1;
    public Type type2;
    
    public ArrayList<Talent> abilities;
    
    public int life;
    public int attack;
    public int defense;
    public int spAttack;
    public int spDefense;
    public int speed;
    
    public EvolutionNode evolutions;
    
    public String catchRate;
    public String weight;
    public String hatch;
    public String gender;
    public String ev;
    public String eggGroup;
    public String size;
    
    public Pokemon(String name, int number, int index, Type type1, Type type2,
            ArrayList<Talent> abilities, int life, int attack, int defense, int spAttack,
            int spDefense, int speed) {
        super();
        this.name = name;
        this.number = number;
        this.index = index;
        this.type1 = type1;
        this.type2 = type2;
        this.abilities = abilities;
        this.life = life;
        this.attack = attack;
        this.defense = defense;
        this.spAttack = spAttack;
        this.spDefense = spDefense;
        this.speed = speed;
    }
    
    @SuppressWarnings("unchecked")
	public HashMap<Type, Weakness> getWeaknesses() {
    	HashMap<Type, Weakness> result = (HashMap<Type, Weakness>)ReceiveTypeTable.table.get(type1).clone();
    	
    	HashMap<Type, Weakness> type2Weaknesses = (HashMap<Type, Weakness>)ReceiveTypeTable.table.get(type2).clone();
    	
    	for (Type t : type2Weaknesses.keySet()) {
    		if (Weakness.IGNORE.equals(type2Weaknesses.get(t))) {
    			result.put(t, Weakness.IGNORE);
    			
    		} else if (type2Weaknesses.get(t).compareTo(Weakness.NORMAL) > 0) {
    			result.put(t, result.get(t).decrease());
    			
    		} else if (type2Weaknesses.get(t).compareTo(Weakness.NORMAL) < 0) {
    			result.put(t, result.get(t).increase());
    		}
    	}
    	
    	return result;
    }
    
    public Pokemon[] getSimpleEvolutionList() {
        return getEvolutionList(evolutions).toArray(new Pokemon[]{});
    }
    
    @SuppressWarnings("serial")
    private ArrayList<Pokemon> getEvolutionList(final EvolutionNode root) {
        if (root == null) {
            return new ArrayList<Pokemon>();
        }
        
        if (root.evolutions == null || root.evolutions.size() < 1) {
            return new ArrayList<Pokemon>(){{this.add(root.base);}};
        }
        
        ArrayList<Pokemon> result = new ArrayList<Pokemon>(){{this.add(root.base);}};
        for (String path : root.evolutions.keySet()) {
            result.addAll(getEvolutionList(root.evolutions.get(path)));
        }
        return result;
    }
    
    public String toString() {
        return name;
    }
}

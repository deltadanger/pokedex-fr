package fr.pokedex;

import java.util.ArrayList;
import java.util.HashMap;


public class Pokemon {
    public String name;
    public int number;
    
    public Type type1;
    public Type type2;
    
    public ArrayList<Talent> abilities;
    
    public int life;
    public int attack;
    public int defense;
    public int spAttack;
    public int spDefense;
    public int speed;
    
    public Pokemon(String name, int number, Type type1, Type type2,
            ArrayList<Talent> abilities, int life, int attack, int defense, int spAttack,
            int spDefense, int speed) {
        super();
        this.name = name;
        this.number = number;
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
}

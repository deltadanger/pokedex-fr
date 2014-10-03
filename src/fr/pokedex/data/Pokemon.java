package fr.pokedex.data;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.SortedSet;
import java.util.TreeSet;

import fr.pokedex.R;


public class Pokemon implements Comparable<Pokemon> {
    
    @SuppressWarnings("serial")
    public static Pokemon MISSINGNO = new Pokemon(){{
            name = R.string.name_missigno;
            name_str = "name_missigno";
            number = index = life = attack = defense = spAttack = spDefense = speed = catchRate = hatch = 0;
            weight = size = 0f;
            type1 = DataHolder.typeByName.get("NORMAL");
            type2 = DataHolder.typeByName.get("NONE");
            abilities = new ArrayList<Ability>(){{
                this.add(Ability.ERROR);
            }};
            evolutionRoot = null;
            gender = -1;
            ev = new EVBonus(0,0,0,0,0,0);
            eggGroup = new ArrayList<EggGroup>();
    }};

    public static String MEGA_AFFIX = "mega";
    public static String MEGA_X_AFFIX = "_x";
    public static String MEGA_Y_AFFIX = "_y";
    
    public int db_id;
    public int name;
    public String name_str;
    public int number;
    public int index;
    
    public Type type1;
    public Type type2;
    
    public ArrayList<Ability> abilities;
    
    public int life;
    public int attack;
    public int defense;
    public int spAttack;
    public int spDefense;
    public int speed;
    
    public int ancestor_id;
    public String evolution_path;
    public EvolutionNode evolutionRoot;

    public float size;
    public float weight;
    public EVBonus ev;
    public int catchRate;
    public float gender;
    public int hatch;
    public ArrayList<EggGroup> eggGroup;
    
    @SuppressWarnings("unchecked")
	public HashMap<Type, Weakness> getWeaknesses() {
    	HashMap<Type, Weakness> result = (HashMap<Type, Weakness>)DataHolder.weaknesses.get(type1).clone();
    	
    	HashMap<Type, Weakness> type2Weaknesses = (HashMap<Type, Weakness>)DataHolder.weaknesses.get(type2).clone();
    	
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
    
    public boolean hasEvolutions() {
        return evolutionRoot != null && !evolutionRoot.isLeaf();
    }
    
    public Pokemon[] getSimpleEvolutionList() {
        return getEvolutionList(evolutionRoot).toArray(new Pokemon[]{});
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

    public Pokemon getPrevious() {
        SortedSet<Pokemon> sameNumbers = DataHolder.pokemonByNumber.get(number);
        
        SortedSet<Pokemon> previousSet = new TreeSet<Pokemon>(sameNumbers.headSet(this));
        if (previousSet.size() == 0) {
            previousSet = DataHolder.pokemonByNumber.get(number-1);
            
            if (previousSet == null || previousSet.size() == 0) {
                return null;
            }
        }
        return previousSet.last();
    }

    public Pokemon getNext() {
        SortedSet<Pokemon> sameNumbers = DataHolder.pokemonByNumber.get(number);
        
        SortedSet<Pokemon> nextSet = new TreeSet<Pokemon>(sameNumbers.tailSet(this));
        nextSet.remove(this); // tailSet() includes provided item in returned set.
        if (nextSet.size() == 0) {
            nextSet = DataHolder.pokemonByNumber.get(number+1);
            
            if (nextSet == null || nextSet.size() == 0) {
                return null;
            }
        }
        return nextSet.first();
    }

    public boolean hasPrevious() {
        return getPrevious() != null;
    }

    public boolean hasNext() {
        return getNext() != null;
    }

    @Override
    public int compareTo(Pokemon other) {
        // Compare numbers
        if (this.number != other.number) {
            return this.number - other.number;
        }
        
        // If numbers are same, megaY > megaX > mega > other
        if (this.name_str.contains(MEGA_Y_AFFIX)) {
            return 1;
        }
        if (other.name_str.contains(MEGA_Y_AFFIX)) {
            return -1;
        }
        if (this.name_str.contains(MEGA_X_AFFIX)) {
            return 1;
        }
        if (other.name_str.contains(MEGA_X_AFFIX)) {
            return -1;
        }
        if (this.name_str.contains(MEGA_AFFIX)) {
            return 1;
        }
        if (other.name_str.contains(MEGA_AFFIX)) {
            return -1;
        }
        
        // No mega in comparison, sort by name
        return this.name_str.compareTo(other.name_str);
    }
}

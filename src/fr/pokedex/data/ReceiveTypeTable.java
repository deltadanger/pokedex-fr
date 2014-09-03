package fr.pokedex.data;

import java.util.HashMap;

public class ReceiveTypeTable {
//    @SuppressWarnings("serial")
//    public static HashMap<Type, HashMap<Type, Weakness>> table = new HashMap<Type, HashMap<Type,Weakness>>() {{
//        
//        this.put(Type.NONE, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.NORMAL);
//            this.put(Type.FIGHTING, Weakness.NORMAL);
//            this.put(Type.DRAGON, Weakness.NORMAL);
//            this.put(Type.WATER, Weakness.NORMAL);
//            this.put(Type.ELECTRIC, Weakness.NORMAL);
//            this.put(Type.FAIRY, Weakness.NORMAL);
//            this.put(Type.FIRE, Weakness.NORMAL);
//            this.put(Type.ICE, Weakness.NORMAL);
//            this.put(Type.BUG, Weakness.NORMAL);
//            this.put(Type.NORMAL, Weakness.NORMAL);
//            this.put(Type.GRASS, Weakness.NORMAL);
//            this.put(Type.POISON, Weakness.NORMAL);
//            this.put(Type.PSYCHIC, Weakness.NORMAL);
//            this.put(Type.ROCK, Weakness.NORMAL);
//            this.put(Type.GROUND, Weakness.NORMAL);
//            this.put(Type.GHOST, Weakness.NORMAL);
//            this.put(Type.DARK, Weakness.NORMAL);
//            this.put(Type.FLYING, Weakness.NORMAL);
//        }});
//        
//        this.put(Type.STEEL, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.STRONG);
//            this.put(Type.FIGHTING, Weakness.WEAK);
//            this.put(Type.DRAGON, Weakness.STRONG);
//            this.put(Type.WATER, Weakness.NORMAL);
//            this.put(Type.ELECTRIC, Weakness.NORMAL);
//            this.put(Type.FAIRY, Weakness.STRONG);
//            this.put(Type.FIRE, Weakness.WEAK);
//            this.put(Type.ICE, Weakness.STRONG);
//            this.put(Type.BUG, Weakness.STRONG);
//            this.put(Type.NORMAL, Weakness.STRONG);
//            this.put(Type.GRASS, Weakness.STRONG);
//            this.put(Type.POISON, Weakness.IGNORE);
//            this.put(Type.PSYCHIC, Weakness.STRONG);
//            this.put(Type.ROCK, Weakness.STRONG);
//            this.put(Type.GROUND, Weakness.WEAK);
//            this.put(Type.GHOST, Weakness.NORMAL);
//            this.put(Type.DARK, Weakness.NORMAL);
//            this.put(Type.FLYING, Weakness.STRONG);
//        }});
//
//        this.put(Type.FIGHTING, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.NORMAL);
//            this.put(Type.FIGHTING, Weakness.NORMAL);
//            this.put(Type.DRAGON, Weakness.NORMAL);
//            this.put(Type.WATER, Weakness.NORMAL);
//            this.put(Type.ELECTRIC, Weakness.NORMAL);
//            this.put(Type.FAIRY, Weakness.WEAK);
//            this.put(Type.FIRE, Weakness.NORMAL);
//            this.put(Type.ICE, Weakness.NORMAL);
//            this.put(Type.BUG, Weakness.STRONG);
//            this.put(Type.NORMAL, Weakness.NORMAL);
//            this.put(Type.GRASS, Weakness.NORMAL);
//            this.put(Type.POISON, Weakness.NORMAL);
//            this.put(Type.PSYCHIC, Weakness.WEAK);
//            this.put(Type.ROCK, Weakness.STRONG);
//            this.put(Type.GROUND, Weakness.NORMAL);
//            this.put(Type.GHOST, Weakness.NORMAL);
//            this.put(Type.DARK, Weakness.STRONG);
//            this.put(Type.FLYING, Weakness.WEAK);
//        }});
//
//        this.put(Type.DRAGON, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.NORMAL);
//            this.put(Type.FIGHTING, Weakness.NORMAL);
//            this.put(Type.DRAGON, Weakness.WEAK);
//            this.put(Type.WATER, Weakness.STRONG);
//            this.put(Type.ELECTRIC, Weakness.STRONG);
//            this.put(Type.FAIRY, Weakness.WEAK);
//            this.put(Type.FIRE, Weakness.STRONG);
//            this.put(Type.ICE, Weakness.WEAK);
//            this.put(Type.BUG, Weakness.NORMAL);
//            this.put(Type.NORMAL, Weakness.NORMAL);
//            this.put(Type.GRASS, Weakness.STRONG);
//            this.put(Type.POISON, Weakness.NORMAL);
//            this.put(Type.PSYCHIC, Weakness.NORMAL);
//            this.put(Type.ROCK, Weakness.NORMAL);
//            this.put(Type.GROUND, Weakness.NORMAL);
//            this.put(Type.GHOST, Weakness.NORMAL);
//            this.put(Type.DARK, Weakness.NORMAL);
//            this.put(Type.FLYING, Weakness.NORMAL);
//        }});
//
//        this.put(Type.WATER, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.STRONG);
//            this.put(Type.FIGHTING, Weakness.NORMAL);
//            this.put(Type.DRAGON, Weakness.NORMAL);
//            this.put(Type.WATER, Weakness.STRONG);
//            this.put(Type.ELECTRIC, Weakness.WEAK);
//            this.put(Type.FAIRY, Weakness.NORMAL);
//            this.put(Type.FIRE, Weakness.STRONG);
//            this.put(Type.ICE, Weakness.STRONG);
//            this.put(Type.BUG, Weakness.NORMAL);
//            this.put(Type.NORMAL, Weakness.NORMAL);
//            this.put(Type.GRASS, Weakness.WEAK);
//            this.put(Type.POISON, Weakness.NORMAL);
//            this.put(Type.PSYCHIC, Weakness.NORMAL);
//            this.put(Type.ROCK, Weakness.NORMAL);
//            this.put(Type.GROUND, Weakness.NORMAL);
//            this.put(Type.GHOST, Weakness.NORMAL);
//            this.put(Type.DARK, Weakness.NORMAL);
//            this.put(Type.FLYING, Weakness.NORMAL);
//        }});
//
//        this.put(Type.ELECTRIC, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.STRONG);
//            this.put(Type.FIGHTING, Weakness.NORMAL);
//            this.put(Type.DRAGON, Weakness.NORMAL);
//            this.put(Type.WATER, Weakness.NORMAL);
//            this.put(Type.ELECTRIC, Weakness.STRONG);
//            this.put(Type.FAIRY, Weakness.NORMAL);
//            this.put(Type.FIRE, Weakness.NORMAL);
//            this.put(Type.ICE, Weakness.NORMAL);
//            this.put(Type.BUG, Weakness.NORMAL);
//            this.put(Type.NORMAL, Weakness.NORMAL);
//            this.put(Type.GRASS, Weakness.NORMAL);
//            this.put(Type.POISON, Weakness.NORMAL);
//            this.put(Type.PSYCHIC, Weakness.NORMAL);
//            this.put(Type.ROCK, Weakness.NORMAL);
//            this.put(Type.GROUND, Weakness.WEAK);
//            this.put(Type.GHOST, Weakness.NORMAL);
//            this.put(Type.DARK, Weakness.NORMAL);
//            this.put(Type.FLYING, Weakness.STRONG);
//        }});
//
//        this.put(Type.FAIRY, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.WEAK);
//            this.put(Type.FIGHTING, Weakness.STRONG);
//            this.put(Type.DRAGON, Weakness.IGNORE);
//            this.put(Type.WATER, Weakness.NORMAL);
//            this.put(Type.ELECTRIC, Weakness.NORMAL);
//            this.put(Type.FAIRY, Weakness.NORMAL);
//            this.put(Type.FIRE, Weakness.NORMAL);
//            this.put(Type.ICE, Weakness.NORMAL);
//            this.put(Type.BUG, Weakness.STRONG);
//            this.put(Type.NORMAL, Weakness.NORMAL);
//            this.put(Type.GRASS, Weakness.NORMAL);
//            this.put(Type.POISON, Weakness.WEAK);
//            this.put(Type.PSYCHIC, Weakness.NORMAL);
//            this.put(Type.ROCK, Weakness.NORMAL);
//            this.put(Type.GROUND, Weakness.NORMAL);
//            this.put(Type.GHOST, Weakness.NORMAL);
//            this.put(Type.DARK, Weakness.STRONG);
//            this.put(Type.FLYING, Weakness.NORMAL);
//        }});
//
//        this.put(Type.FIRE, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.STRONG);
//            this.put(Type.FIGHTING, Weakness.NORMAL);
//            this.put(Type.DRAGON, Weakness.NORMAL);
//            this.put(Type.WATER, Weakness.WEAK);
//            this.put(Type.ELECTRIC, Weakness.NORMAL);
//            this.put(Type.FAIRY, Weakness.STRONG);
//            this.put(Type.FIRE, Weakness.STRONG);
//            this.put(Type.ICE, Weakness.STRONG);
//            this.put(Type.BUG, Weakness.STRONG);
//            this.put(Type.NORMAL, Weakness.NORMAL);
//            this.put(Type.GRASS, Weakness.STRONG);
//            this.put(Type.POISON, Weakness.NORMAL);
//            this.put(Type.PSYCHIC, Weakness.NORMAL);
//            this.put(Type.ROCK, Weakness.WEAK);
//            this.put(Type.GROUND, Weakness.WEAK);
//            this.put(Type.GHOST, Weakness.NORMAL);
//            this.put(Type.DARK, Weakness.NORMAL);
//            this.put(Type.FLYING, Weakness.NORMAL);
//        }});
//
//        this.put(Type.ICE, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.WEAK);
//            this.put(Type.FIGHTING, Weakness.WEAK);
//            this.put(Type.DRAGON, Weakness.NORMAL);
//            this.put(Type.WATER, Weakness.NORMAL);
//            this.put(Type.ELECTRIC, Weakness.NORMAL);
//            this.put(Type.FAIRY, Weakness.NORMAL);
//            this.put(Type.FIRE, Weakness.WEAK);
//            this.put(Type.ICE, Weakness.STRONG);
//            this.put(Type.BUG, Weakness.NORMAL);
//            this.put(Type.NORMAL, Weakness.NORMAL);
//            this.put(Type.GRASS, Weakness.NORMAL);
//            this.put(Type.POISON, Weakness.NORMAL);
//            this.put(Type.PSYCHIC, Weakness.NORMAL);
//            this.put(Type.ROCK, Weakness.WEAK);
//            this.put(Type.GROUND, Weakness.NORMAL);
//            this.put(Type.GHOST, Weakness.NORMAL);
//            this.put(Type.DARK, Weakness.NORMAL);
//            this.put(Type.FLYING, Weakness.NORMAL);
//        }});
//
//        this.put(Type.BUG, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.NORMAL);
//            this.put(Type.FIGHTING, Weakness.STRONG);
//            this.put(Type.DRAGON, Weakness.NORMAL);
//            this.put(Type.WATER, Weakness.NORMAL);
//            this.put(Type.ELECTRIC, Weakness.NORMAL);
//            this.put(Type.FAIRY, Weakness.NORMAL);
//            this.put(Type.FIRE, Weakness.WEAK);
//            this.put(Type.ICE, Weakness.NORMAL);
//            this.put(Type.BUG, Weakness.NORMAL);
//            this.put(Type.NORMAL, Weakness.NORMAL);
//            this.put(Type.GRASS, Weakness.STRONG);
//            this.put(Type.POISON, Weakness.NORMAL);
//            this.put(Type.PSYCHIC, Weakness.NORMAL);
//            this.put(Type.ROCK, Weakness.WEAK);
//            this.put(Type.GROUND, Weakness.STRONG);
//            this.put(Type.GHOST, Weakness.NORMAL);
//            this.put(Type.DARK, Weakness.NORMAL);
//            this.put(Type.FLYING, Weakness.WEAK);
//        }});
//
//        this.put(Type.NORMAL, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.NORMAL);
//            this.put(Type.FIGHTING, Weakness.WEAK);
//            this.put(Type.DRAGON, Weakness.NORMAL);
//            this.put(Type.WATER, Weakness.NORMAL);
//            this.put(Type.ELECTRIC, Weakness.NORMAL);
//            this.put(Type.FAIRY, Weakness.NORMAL);
//            this.put(Type.FIRE, Weakness.NORMAL);
//            this.put(Type.ICE, Weakness.NORMAL);
//            this.put(Type.BUG, Weakness.NORMAL);
//            this.put(Type.NORMAL, Weakness.NORMAL);
//            this.put(Type.GRASS, Weakness.NORMAL);
//            this.put(Type.POISON, Weakness.NORMAL);
//            this.put(Type.PSYCHIC, Weakness.NORMAL);
//            this.put(Type.ROCK, Weakness.NORMAL);
//            this.put(Type.GROUND, Weakness.NORMAL);
//            this.put(Type.GHOST, Weakness.IGNORE);
//            this.put(Type.DARK, Weakness.NORMAL);
//            this.put(Type.FLYING, Weakness.NORMAL);
//        }});
//
//        this.put(Type.GRASS, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.NORMAL);
//            this.put(Type.FIGHTING, Weakness.NORMAL);
//            this.put(Type.DRAGON, Weakness.NORMAL);
//            this.put(Type.WATER, Weakness.STRONG);
//            this.put(Type.ELECTRIC, Weakness.STRONG);
//            this.put(Type.FAIRY, Weakness.NORMAL);
//            this.put(Type.FIRE, Weakness.WEAK);
//            this.put(Type.ICE, Weakness.WEAK);
//            this.put(Type.BUG, Weakness.WEAK);
//            this.put(Type.NORMAL, Weakness.NORMAL);
//            this.put(Type.GRASS, Weakness.STRONG);
//            this.put(Type.POISON, Weakness.WEAK);
//            this.put(Type.PSYCHIC, Weakness.NORMAL);
//            this.put(Type.ROCK, Weakness.NORMAL);
//            this.put(Type.GROUND, Weakness.STRONG);
//            this.put(Type.GHOST, Weakness.NORMAL);
//            this.put(Type.DARK, Weakness.NORMAL);
//            this.put(Type.FLYING, Weakness.WEAK);
//        }});
//
//        this.put(Type.POISON, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.NORMAL);
//            this.put(Type.FIGHTING, Weakness.STRONG);
//            this.put(Type.DRAGON, Weakness.NORMAL);
//            this.put(Type.WATER, Weakness.NORMAL);
//            this.put(Type.ELECTRIC, Weakness.NORMAL);
//            this.put(Type.FAIRY, Weakness.STRONG);
//            this.put(Type.FIRE, Weakness.NORMAL);
//            this.put(Type.ICE, Weakness.NORMAL);
//            this.put(Type.BUG, Weakness.STRONG);
//            this.put(Type.NORMAL, Weakness.NORMAL);
//            this.put(Type.GRASS, Weakness.STRONG);
//            this.put(Type.POISON, Weakness.STRONG);
//            this.put(Type.PSYCHIC, Weakness.WEAK);
//            this.put(Type.ROCK, Weakness.NORMAL);
//            this.put(Type.GROUND, Weakness.WEAK);
//            this.put(Type.GHOST, Weakness.NORMAL);
//            this.put(Type.DARK, Weakness.NORMAL);
//            this.put(Type.FLYING, Weakness.NORMAL);
//        }});
//
//        this.put(Type.PSYCHIC, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.NORMAL);
//            this.put(Type.FIGHTING, Weakness.STRONG);
//            this.put(Type.DRAGON, Weakness.NORMAL);
//            this.put(Type.WATER, Weakness.NORMAL);
//            this.put(Type.ELECTRIC, Weakness.NORMAL);
//            this.put(Type.FAIRY, Weakness.NORMAL);
//            this.put(Type.FIRE, Weakness.NORMAL);
//            this.put(Type.ICE, Weakness.NORMAL);
//            this.put(Type.BUG, Weakness.WEAK);
//            this.put(Type.NORMAL, Weakness.NORMAL);
//            this.put(Type.GRASS, Weakness.NORMAL);
//            this.put(Type.POISON, Weakness.NORMAL);
//            this.put(Type.PSYCHIC, Weakness.STRONG);
//            this.put(Type.ROCK, Weakness.NORMAL);
//            this.put(Type.GROUND, Weakness.NORMAL);
//            this.put(Type.GHOST, Weakness.WEAK);
//            this.put(Type.DARK, Weakness.WEAK);
//            this.put(Type.FLYING, Weakness.NORMAL);
//        }});
//
//        this.put(Type.ROCK, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.WEAK);
//            this.put(Type.FIGHTING, Weakness.WEAK);
//            this.put(Type.DRAGON, Weakness.NORMAL);
//            this.put(Type.WATER, Weakness.WEAK);
//            this.put(Type.ELECTRIC, Weakness.NORMAL);
//            this.put(Type.FAIRY, Weakness.NORMAL);
//            this.put(Type.FIRE, Weakness.STRONG);
//            this.put(Type.ICE, Weakness.NORMAL);
//            this.put(Type.BUG, Weakness.NORMAL);
//            this.put(Type.NORMAL, Weakness.STRONG);
//            this.put(Type.GRASS, Weakness.WEAK);
//            this.put(Type.POISON, Weakness.STRONG);
//            this.put(Type.PSYCHIC, Weakness.NORMAL);
//            this.put(Type.ROCK, Weakness.NORMAL);
//            this.put(Type.GROUND, Weakness.WEAK);
//            this.put(Type.GHOST, Weakness.NORMAL);
//            this.put(Type.DARK, Weakness.NORMAL);
//            this.put(Type.FLYING, Weakness.STRONG);
//        }});
//
//        this.put(Type.GROUND, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.NORMAL);
//            this.put(Type.FIGHTING, Weakness.NORMAL);
//            this.put(Type.DRAGON, Weakness.NORMAL);
//            this.put(Type.WATER, Weakness.WEAK);
//            this.put(Type.ELECTRIC, Weakness.IGNORE);
//            this.put(Type.FAIRY, Weakness.NORMAL);
//            this.put(Type.FIRE, Weakness.NORMAL);
//            this.put(Type.ICE, Weakness.WEAK);
//            this.put(Type.BUG, Weakness.NORMAL);
//            this.put(Type.NORMAL, Weakness.NORMAL);
//            this.put(Type.GRASS, Weakness.WEAK);
//            this.put(Type.POISON, Weakness.STRONG);
//            this.put(Type.PSYCHIC, Weakness.NORMAL);
//            this.put(Type.ROCK, Weakness.STRONG);
//            this.put(Type.GROUND, Weakness.NORMAL);
//            this.put(Type.GHOST, Weakness.NORMAL);
//            this.put(Type.DARK, Weakness.NORMAL);
//            this.put(Type.FLYING, Weakness.NORMAL);
//        }});
//
//        this.put(Type.GHOST, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.NORMAL);
//            this.put(Type.FIGHTING, Weakness.IGNORE);
//            this.put(Type.DRAGON, Weakness.NORMAL);
//            this.put(Type.WATER, Weakness.NORMAL);
//            this.put(Type.ELECTRIC, Weakness.NORMAL);
//            this.put(Type.FAIRY, Weakness.NORMAL);
//            this.put(Type.FIRE, Weakness.NORMAL);
//            this.put(Type.ICE, Weakness.NORMAL);
//            this.put(Type.BUG, Weakness.STRONG);
//            this.put(Type.NORMAL, Weakness.IGNORE);
//            this.put(Type.GRASS, Weakness.NORMAL);
//            this.put(Type.POISON, Weakness.STRONG);
//            this.put(Type.PSYCHIC, Weakness.NORMAL);
//            this.put(Type.ROCK, Weakness.NORMAL);
//            this.put(Type.GROUND, Weakness.NORMAL);
//            this.put(Type.GHOST, Weakness.WEAK);
//            this.put(Type.DARK, Weakness.WEAK);
//            this.put(Type.FLYING, Weakness.NORMAL);
//        }});
//
//        this.put(Type.DARK, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.NORMAL);
//            this.put(Type.FIGHTING, Weakness.WEAK);
//            this.put(Type.DRAGON, Weakness.NORMAL);
//            this.put(Type.WATER, Weakness.NORMAL);
//            this.put(Type.ELECTRIC, Weakness.NORMAL);
//            this.put(Type.FAIRY, Weakness.WEAK);
//            this.put(Type.FIRE, Weakness.NORMAL);
//            this.put(Type.ICE, Weakness.NORMAL);
//            this.put(Type.BUG, Weakness.WEAK);
//            this.put(Type.NORMAL, Weakness.NORMAL);
//            this.put(Type.GRASS, Weakness.NORMAL);
//            this.put(Type.POISON, Weakness.NORMAL);
//            this.put(Type.PSYCHIC, Weakness.IGNORE);
//            this.put(Type.ROCK, Weakness.NORMAL);
//            this.put(Type.GROUND, Weakness.NORMAL);
//            this.put(Type.GHOST, Weakness.STRONG);
//            this.put(Type.DARK, Weakness.STRONG);
//            this.put(Type.FLYING, Weakness.NORMAL);
//        }});
//
//        this.put(Type.FLYING, new HashMap<Type, Weakness>(){{
//            this.put(Type.STEEL, Weakness.NORMAL);
//            this.put(Type.FIGHTING, Weakness.STRONG);
//            this.put(Type.DRAGON, Weakness.NORMAL);
//            this.put(Type.WATER, Weakness.NORMAL);
//            this.put(Type.ELECTRIC, Weakness.WEAK);
//            this.put(Type.FAIRY, Weakness.NORMAL);
//            this.put(Type.FIRE, Weakness.NORMAL);
//            this.put(Type.ICE, Weakness.WEAK);
//            this.put(Type.BUG, Weakness.STRONG);
//            this.put(Type.NORMAL, Weakness.NORMAL);
//            this.put(Type.GRASS, Weakness.STRONG);
//            this.put(Type.POISON, Weakness.NORMAL);
//            this.put(Type.PSYCHIC, Weakness.NORMAL);
//            this.put(Type.ROCK, Weakness.WEAK);
//            this.put(Type.GROUND, Weakness.IGNORE);
//            this.put(Type.GHOST, Weakness.NORMAL);
//            this.put(Type.DARK, Weakness.NORMAL);
//            this.put(Type.FLYING, Weakness.NORMAL);
//        }});        
//    }};
}

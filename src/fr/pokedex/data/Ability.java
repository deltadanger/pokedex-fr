package fr.pokedex.data;

import fr.pokedex.R;


public class Ability {

    public static String PREFIX_NAME = "ability_name_";
    public static String PREFIX_IN_FIGHT = "ability_infight_";
    public static String PREFIX_OUT_FIGHT = "ability_outfight_";
    
    public static Ability ERROR = new Ability("error");
    
    /**
     * Resource ids
     */
    public int name;
    public int inFight;
    public int outFight;
    
    Ability(String name) {
        try {
            this.name = R.string.class.getField(PREFIX_NAME + name).getInt(null);
            this.inFight = R.string.class.getField(PREFIX_IN_FIGHT + name).getInt(null);
            this.outFight = R.string.class.getField(PREFIX_OUT_FIGHT + name).getInt(null);
        } catch (IllegalArgumentException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (NoSuchFieldException e) {
            e.printStackTrace();
        }
    };
}

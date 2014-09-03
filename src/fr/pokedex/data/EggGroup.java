package fr.pokedex.data;

import fr.pokedex.R;

public class EggGroup {
    
    public int name;
    EggGroup(String name) {
        try {
            this.name = R.string.class.getField(name.toLowerCase()).getInt(null);
        } catch (IllegalArgumentException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (NoSuchFieldException e) {
            e.printStackTrace();
        };
    }
}

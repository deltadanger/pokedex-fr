package fr.pokedex.data;

import fr.pokedex.R;


public class Type {
    public int image;
    
    Type(String name) {
        try {
            this.image = R.drawable.class.getField(name.toLowerCase()).getInt(null);
        } catch (IllegalArgumentException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (NoSuchFieldException e) {
            e.printStackTrace();
        };
    }
}

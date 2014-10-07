package fr.pokedex.data;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.TreeSet;

import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.util.Log;
import android.util.SparseArray;
import fr.pokedex.R;

public class DataHolder {

    public static SparseArray<Ability> abilities;
    public static SparseArray<Type> types;
    public static HashMap<String, Type> typeByName;
    public static HashMap<Type, HashMap<Type, Weakness>> weaknesses;
    public static SparseArray<EggGroup> eggGroups;
    public static SparseArray<EVBonus> evBonus;
    public static HashMap<String, Pokemon> pokemons;
    public static SparseArray<Pokemon> pokemonById;
    public static SparseArray<TreeSet<Pokemon>> pokemonByNumber;
    public static SparseArray<ArrayList<Pokemon>> pokemonByAncestor;

    public static String DATABASE_NAME = "pokemon_db";
    public static String DATABASE_TABLE_ABILITIES = "app_ability";
    public static String DATABASE_TABLE_TYPES = "app_pokemontype";
    public static String DATABASE_TABLE_WEAKNESSES = "app_weakness";
    public static String DATABASE_TABLE_EGGROUPS = "app_egggroup";
    public static String DATABASE_TABLE_EVBONUS = "app_evbonus";
    public static String DATABASE_TABLE_POKEMONS = "app_pokemon";
    public static String DATABASE_TABLE_POKEMON_ABILITIES = "app_pokemon_abilities";
    public static String DATABASE_TABLE_POKEMON_EGG_GROUPS = "app_pokemon_egg_group";
    
    public static String NO_TYPE_NAME = "NONE";
    
    private static class SQLiteOpener extends SQLiteOpenHelper {
        
        Context context;
        
        SQLiteOpener(Context context) {
            super(context, DATABASE_NAME, null, 1);
            
            this.context = context;
            
            try {
                copyDataBaseFromAssets();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        @Override
        public void onCreate(SQLiteDatabase db) {}

        @Override
        public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {}

        private void copyDataBaseFromAssets() throws IOException {
            InputStream databaseFileSource = context.getResources().openRawResource(R.raw.pokedex_db);
            OutputStream databaseFileDest = new FileOutputStream(context.getDatabasePath(DATABASE_NAME));

            byte[] buffer = new byte[1024];
            int length;
            while ((length = databaseFileSource.read(buffer))>0){
                databaseFileDest.write(buffer, 0, length);
            }

            databaseFileDest.flush();
            databaseFileDest.close();
            databaseFileSource.close();
        }
    }
    
    private static SQLiteDatabase db;

    private static Type noType;
	
	public static void initialize(final Context context) {
        db = new SQLiteOpener(context).getReadableDatabase();
        
        if (abilities == null)
            abilities = new SparseArray<Ability>();
        
        if (types == null)
            types = new SparseArray<Type>();
        
        if (typeByName == null)
            typeByName = new HashMap<String, Type>();
        
        if (weaknesses == null)
            weaknesses = new HashMap<Type, HashMap<Type, Weakness>>();
        
        if (eggGroups == null)
            eggGroups= new SparseArray<EggGroup>();
        
        if (evBonus == null)
            evBonus = new SparseArray<EVBonus>();
        
        if (pokemons == null)
            pokemons = new HashMap<String, Pokemon>();
        
        if (pokemonById == null)
            pokemonById = new SparseArray<Pokemon>();
        
        if (pokemonByNumber == null)
            pokemonByNumber = new SparseArray<TreeSet<Pokemon>>();
        
        if (pokemonByAncestor == null)
            pokemonByAncestor = new SparseArray<ArrayList<Pokemon>>();
        
	    try {
	        Log.d("test","loadAbilities");
	        loadAbilities();
            Log.d("test","loadTypes");
            loadTypes();
            Log.d("test","loadEggGroups");
            loadEggGroups();
            Log.d("test","loadEvBonus");
            loadEvBonus();
            Log.d("test","loadPokemons");
            loadPokemons();
            Log.d("test","Loading done");
        } catch (IllegalArgumentException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (NoSuchFieldException e) {
            e.printStackTrace();
        }
	}

    private static void loadAbilities() {
        Cursor resultSet = db.query(DATABASE_TABLE_ABILITIES, new String[]{"id","identifier"}, null, null, null, null, null);
        try {
            while (resultSet.moveToNext()) {
                abilities.put(resultSet.getInt(0), new Ability(resultSet.getString(1)));
            }
        } finally {
            resultSet.close();
        }
    }

    private static void loadTypes() throws IllegalArgumentException, IllegalAccessException, NoSuchFieldException {
        Cursor resultSet = db.query(DATABASE_TABLE_TYPES, new String[]{"id","name"}, null, null, null, null, null);
        
        try {
            Type type;
            while (resultSet.moveToNext()) {
                String name = resultSet.getString(1);
                type = new Type(name);
                types.put(resultSet.getInt(0), type);
                typeByName.put(name, type);
                
                if (NO_TYPE_NAME.equals(resultSet.getString(1))) {
                    noType = type;
                }
            }
        } finally {
            resultSet.close();
        }
        
        resultSet = db.query(DATABASE_TABLE_WEAKNESSES, new String[]{"base_type_id","receiving_type_id", "weakness"}, null, null, null, null, null);

        try {
            while (resultSet.moveToNext()) {
                Type baseType = types.get(resultSet.getInt(0));
                Type receivingType = types.get(resultSet.getInt(1));
                Weakness weakness = (Weakness) Weakness.class.getField(resultSet.getString(2)).get(null);
                
                if (!weaknesses.containsKey(baseType)) {
                    weaknesses.put(baseType, new HashMap<Type, Weakness>());
                }
                
                weaknesses.get(baseType).put(receivingType, weakness);
            }
        } finally {
            resultSet.close();
        }
    }

    private static void loadEggGroups() {
        Cursor resultSet = db.query(DATABASE_TABLE_EGGROUPS, new String[]{"id","name"}, null, null, null, null, null);

        try {
            while (resultSet.moveToNext()) {
                eggGroups.put(resultSet.getInt(0), new EggGroup(resultSet.getString(1)));
            }
        } finally {
            resultSet.close();
        }
    }

    private static void loadEvBonus() {
        Cursor resultSet = db.query(DATABASE_TABLE_EVBONUS, new String[]{"id","life","attack","defense","sp_attack","sp_defense","speed"}, null, null, null, null, null);

        try {
            while (resultSet.moveToNext()) {
                evBonus.put(resultSet.getInt(0), new EVBonus(resultSet.getInt(1),resultSet.getInt(2),resultSet.getInt(3),resultSet.getInt(4),resultSet.getInt(5),resultSet.getInt(6)));
            }
        } finally {
            resultSet.close();
        }
    }

    private static void loadPokemons() throws IllegalArgumentException, IllegalAccessException, NoSuchFieldException {
        Pokemon p;
        
        Cursor resultSet = db.query(DATABASE_TABLE_POKEMONS,
                new String[]{
                "id", // 0
                "name", // 1
                "number", // 2
                "type1_id", // 3
                "type2_id", // 4
                "ancestor_id", // 5
                "evolution_path", // 6
                "size", // 7
                "weight", // 8
                "ev_id", // 9
                "catch_rate", // 10
                "gender", // 11
                "hatch", // 12
                "life", // 13
                "attack", // 14
                "defense", // 15
                "sp_attack", // 16
                "sp_defense", // 17
                "speed", // 18
                }, null, null, null, null, null);

        try {
            while (resultSet.moveToNext()) {
                p = new Pokemon();
                p.db_id = resultSet.getInt(0);
                p.name_str = resultSet.getString(1);
                p.name = R.string.class.getField(p.name_str).getInt(null);
                p.number = resultSet.getInt(2);
                p.type1 = types.get(resultSet.getInt(3));
                
                try {
                    p.type2 = types.get(resultSet.getInt(4));
                } catch (Exception e) {
                    p.type2 = noType;
                }
                
                try {
                    p.ancestor_id = resultSet.getInt(5);
                    p.evolution_path = resultSet.getString(6);
                } catch (Exception e) {
                    p.ancestor_id = 0;
                }
                
                p.size = resultSet.getFloat(7);
                p.weight = resultSet.getFloat(8);
                p.ev = evBonus.get(resultSet.getInt(9));
                p.catchRate = resultSet.getInt(10);
                p.gender = resultSet.getFloat(11);
                p.hatch = resultSet.getInt(12);
                p.life = resultSet.getInt(13);
                p.attack = resultSet.getInt(14);
                p.defense = resultSet.getInt(15);
                p.spAttack = resultSet.getInt(16);
                p.spDefense = resultSet.getInt(17);
                p.speed = resultSet.getInt(18);
                
                p.abilities = new ArrayList<Ability>();
                Cursor pokemonAbilitiesResult = db.query(DATABASE_TABLE_POKEMON_ABILITIES, new String[]{"ability_id"}, " pokemon_id=" + p.db_id, null, null, null, null);

                try {
                    while (pokemonAbilitiesResult.moveToNext()) {
                        p.abilities.add(abilities.get(pokemonAbilitiesResult.getInt(0)));
                    }
                } finally {
                    pokemonAbilitiesResult.close();
                }
                
                p.eggGroup = new ArrayList<EggGroup>();
                Cursor pokemonEggGroupResult = db.query(DATABASE_TABLE_POKEMON_EGG_GROUPS, new String[]{"egggroup_id"}, " pokemon_id=" + p.db_id, null, null, null, null);

                try {
                    while (pokemonEggGroupResult.moveToNext()) {
                        p.eggGroup.add(eggGroups.get(pokemonEggGroupResult.getInt(0)));
                    }
                } finally {
                    pokemonEggGroupResult.close();
                }
    
                pokemonById.put(p.db_id, p);
                pokemons.put(p.name_str, p);
                if (p.ancestor_id > -1) {
                    if (pokemonByAncestor.get(p.ancestor_id) == null) {
                        pokemonByAncestor.put(p.ancestor_id, new ArrayList<Pokemon>());
                    }
                    if (!pokemonByAncestor.get(p.ancestor_id).contains(p)) {
                        pokemonByAncestor.get(p.ancestor_id).add(p);
                    }
                }
                if (pokemonByNumber.get(p.number) == null) {
                    pokemonByNumber.put(p.number, new TreeSet<Pokemon>());
                }
                if (!pokemonByNumber.get(p.number).contains(p)) {
                    pokemonByNumber.get(p.number).add(p);
                }
            }
        } finally {
            resultSet.close();
        }
        
        for (int i = 0; i < pokemonById.size(); i++) {
            // Evolutions
            Pokemon pokemon = pokemonById.valueAt(i);
            Pokemon ancestor = pokemon;
            while (ancestor.ancestor_id > 0) {
                ancestor = pokemonById.get(ancestor.ancestor_id);
            }
            pokemon.evolutionRoot = generateEvolutions(ancestor);
        }
    }

    private static EvolutionNode generateEvolutions(Pokemon ancestor) {
        EvolutionNode result = new EvolutionNode(ancestor, new HashMap<String, EvolutionNode>());
        
        if (pokemonByAncestor.get(ancestor.db_id) != null) {
            for (Pokemon p : pokemonByAncestor.get(ancestor.db_id)) {
                result.evolutions.put(p.evolution_path, generateEvolutions(p));
            }
        }
        
        return result;
    }
}

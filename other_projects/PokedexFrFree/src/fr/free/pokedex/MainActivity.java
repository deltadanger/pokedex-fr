package fr.free.pokedex;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import fr.pokedex.data.PokemonList;


public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        PokemonList.initialize();

        Intent intent = new Intent(this, PokemonPage.class);
        intent.putExtra(PokemonPage.INTENT_EXTRA_POKEMON_INDEX, 1);
        startActivity(intent);
        finish();
    }
}

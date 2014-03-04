package fr.pokedex;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import fr.pokedex.data.PokemonList;

/*
 * TODO:
 * - Ajout d'infos supplémentaires
 *      - Taille
 *      - Poids
 *      - Moyens d'évolution
 *      - Groupe Oeuf
 *      - Nombre de pas
 *      - Répartition Male/Femelle
 *      - Talents
 * - Recherche par type
 * - Theme sombre
 * - Liste des attaques apprises
 */

/* 
 * java.lang.OutOfMemoryError
 */

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

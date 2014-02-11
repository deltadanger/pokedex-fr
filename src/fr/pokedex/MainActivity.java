package fr.pokedex;


import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import fr.pokedex.data.PokemonList;

/*
 * TODO:
 * - Swipe gauche/droite
 * - Ajout d'infos suppl�mentaires
 *      - Taille
 *      - Poids
 *      - Moyens d'�volution
 *      - Groupe Oeuf
 *      - Nombre de pas
 *      - R�partition Male/Femelle
 *      - Talents
 * - Recherche par type
 * - Theme sombre
 * - Liste des attaques apprises
 */

public class MainActivity extends Activity {
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        PokemonList.initialize();
        
        Intent intent = new Intent(this, PokemonPage.class);
        intent.putExtra(PokemonPage.INTENT_EXTRA_POKEMON_NUMBER, 1);
        startActivity(intent);
        finish();
    }
}

package fr.pokedex;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Window;
import fr.pokedex.data.PokemonList;

/*
 * TODO:
 * - Icone transparente
 * - Ajout d'infos suppl�mentaires
 *      - Taille
 *      - Poids
 *      - Moyens d'�volution
 *      - Groupe Oeuf
 *      - Nombre de pas
 *      - R�partition Male/Femelle
 *      - Talents
 * - Garder section "info supp" dans le m�me �tat lors d'un changement de page
 * X Recherche par type
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
        requestWindowFeature(Window.FEATURE_NO_TITLE);

        PokemonList.initialize();

        Intent intent = new Intent(this, PokemonPage.class);
        intent.putExtra(PokemonPage.INTENT_EXTRA_POKEMON_INDEX, 1);
        startActivity(intent);
        finish();
    }
}

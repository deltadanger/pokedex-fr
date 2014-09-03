package fr.pokedex;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Window;
import fr.pokedex.data.DataHolder;

/*
 * TODO:
 * / Ajouter lien entre Ptéra et Mega-Ptéra
 * - Clavier qui apparait quand on ferme les details d'un talent
 * - Layout de l'affichage des détails (certains mots sortent tel: Y530 (hwY530-U00))
 * - Trier les types par ordre alphabétiques dans la langue sélectionnée
 * - Recherche par texte pur (incluant par numéro)
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

        DataHolder.initialize(this);

        Intent intent = new Intent(this, PokemonPage.class);
        intent.putExtra(PokemonPage.INTENT_EXTRA_POKEMON_INDEX, 1);
        startActivity(intent);
        finish();
    }
}

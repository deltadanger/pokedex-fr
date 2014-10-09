package fr.pokedex;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Window;
import fr.pokedex.data.DataHolder;

/*
 * TODO:
 * / Ajouter lien entre Pt�ra et Mega-Pt�ra
 * / Ajouter images pour les formes alternatives
 * / Evolutions disparues 
 * 
 * - Clavier qui apparait quand on ferme les details d'un talent / change de langue
 * - Layout de l'affichage des d�tails (certains mots sortent tel: Y530 (hwY530-U00))
 * - Trier les types par ordre alphab�tiques dans la langue s�lectionn�e
 * - Recherche par texte pur (incluant par num�ro)
 * X Recherche par type
 * - Theme sombre
 * - Liste des attaques apprises
 * - Erreurs diverses
 */

public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);

        DataHolder.initialize(this);

        Intent intent = new Intent(this, PokemonPage.class);
        startActivity(intent);
        finish();
    }
}

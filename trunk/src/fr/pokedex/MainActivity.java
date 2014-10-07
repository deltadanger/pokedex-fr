package fr.pokedex;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Window;
import fr.pokedex.data.DataHolder;

/*
 * TODO:
 * / Ajouter lien entre Ptéra et Mega-Ptéra
 * / Ajouter images pour :
name_aegislash_shield_forme
name_darmanitan_standard_mode
name_deoxys_defense_forme
name_deoxys_normal_forme
name_deoxys_speed_forme
name_giratina_origin_forme
name_kyurem_black_kyurem
name_landorus_therian_forme
name_meloetta_aria_forme
name_rotom_fan_rotom
name_rotom_frost_rotom
name_rotom_heat_rotom
name_rotom_normal_rotom
name_rotom_wash_rotom
name_shaymin_sky_forme
name_thundurus_therian_forme
name_tornadus_therian_forme
name_wormadam_plant_cloak
name_wormadam_sandy_cloak
 * - Evolutions disparues ????
 * - Clavier qui apparait quand on ferme les details d'un talent
 * - Layout de l'affichage des détails (certains mots sortent tel: Y530 (hwY530-U00))
 * - Trier les types par ordre alphabétiques dans la langue sélectionnée
 * - Recherche par texte pur (incluant par numéro)
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
//        intent.putExtra(PokemonPage.INTENT_EXTRA_POKEMON_NAME, "");
        startActivity(intent);
        finish();
    }
}

package fr.pokedex.data;

import java.util.ArrayList;
import java.util.HashMap;

import android.util.SparseArray;

@SuppressWarnings("serial")
public class PokemonList {
    
    public static SparseArray<Pokemon> perIndex = new SparseArray<Pokemon>();
	
	public static void initialize() {
	    Pokemon p;
	    
	    for (String name : perName.keySet()) {
	        p = perName.get(name);
	        perIndex.put(p.index, p);
	    }

        setAdditionalInformationPart1();
        setAdditionalInformationPart2();
	}
	
	private static void setAdditionalInformationPart1() {
	    Pokemon p;
	    
	    // Set additional information
        p = perName.get("Rattatac");
        p.evolutions = new EvolutionNode(perName.get("Rattata"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Rattatac"), null));}});
        p.catchRate = "127";
        p.weight = "18,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,7m";

        p = perName.get("Incisache");
        p.evolutions = new EvolutionNode(perName.get("Coupenotte"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 38", new EvolutionNode(perName.get("Incisache"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 48", new EvolutionNode(perName.get("Tranchodon"), null));}}));}});
        p.catchRate = "60";
        p.weight = "36,0kg";
        p.hatch = "40 cycles - 10455 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Monstre/Dragon";
        p.size = "1,0m";

        p = perName.get("Baggiguane");
        p.evolutions = new EvolutionNode(perName.get("Baggiguane"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 39", new EvolutionNode(perName.get("Baggaid"), null));}});
        p.catchRate = "180";
        p.weight = "11,8kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Dragon/Sol";
        p.size = "0,6m";

        p = perName.get("Noadkoko");
        p.evolutions = new EvolutionNode(perName.get("Noeunoeuf"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get("Noadkoko"), null));}});
        p.catchRate = "45";
        p.weight = "120,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Plante";
        p.size = "2,0m";

        p = perName.get("Gueriaigle");
        p.evolutions = new EvolutionNode(perName.get("Furaiglon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 54", new EvolutionNode(perName.get("Gueriaigle"), null));}});
        p.catchRate = "60";
        p.weight = "41kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Vol";
        p.size = "1,5m";

        p = perName.get("Floravol");
        p.evolutions = new EvolutionNode(perName.get("Granivol"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Floravol"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 27", new EvolutionNode(perName.get("Cotovol"), null));}}));}});
        p.catchRate = "120";
        p.weight = "1,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Fee/Plante";
        p.size = "0,6m";

        p = perName.get("Polichombr");
        p.evolutions = new EvolutionNode(perName.get("Polichombr"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Branette"), new HashMap<String, EvolutionNode>(){{this.put("Branettite", new EvolutionNode(perName.get("Mega-Branette"), null));}}));}});
        p.catchRate = "225";
        p.weight = "2,3kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Indetermine";
        p.size = "0,6m";

        p = perName.get("Gaulet");
        p.evolutions = new EvolutionNode(perName.get("Trompignon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 39", new EvolutionNode(perName.get("Gaulet"), null));}});
        p.catchRate = "75";
        p.weight = "10,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Plante";
        p.size = "0,6m";

        p = perName.get("Hyporoi");
        p.evolutions = new EvolutionNode(perName.get("Hypotrempe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Hypocean"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Ecaille Draco", new EvolutionNode(perName.get("Hyporoi"), null));}}));}});
        p.catchRate = "45";
        p.weight = "152,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.; +1 Att. Spe; +1 Def. Spe";
        p.eggGroup = "Eau 1/Dragon";
        p.size = "1,8m";

        p = perName.get("Elekable");
        p.evolutions = new EvolutionNode(perName.get("Elekid"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Elektek"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant un Electiriseur", new EvolutionNode(perName.get("Elekable"), null));}}));}});
        p.catchRate = "30";
        p.weight = "140,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Humanoide";
        p.size = "1,8m";

        p = perName.get("Roussil");
        p.evolutions = new EvolutionNode(perName.get("Feunnec"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Roussil"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Goupelin"), null));}}));}});
        p.catchRate = "45";
        p.weight = "14,5kg";
        p.hatch = "pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Pashmilla");
        p.evolutions = new EvolutionNode(perName.get("Chinchidou"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get("Pashmilla"), null));}});
        p.catchRate = "255";
        p.weight = "7,5kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,5m";

        p = perName.get("Emolga");
        p.evolutions = null;
        p.catchRate = "200";
        p.weight = "5,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,4m";

        p = perName.get("Grolem");
        p.evolutions = new EvolutionNode(perName.get("Racaillou"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Gravalanch"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Grolem"), null));}}));}});
        p.catchRate = "45";
        p.weight = "300,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Def.";
        p.eggGroup = "Mineral";
        p.size = "1,4m";

        p = perName.get("Cresselia");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "85,6kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+3 Vit.";
        p.eggGroup = "Sans oeuf";
        p.size = "1,5m";

        p = perName.get("Flotoutan");
        p.evolutions = new EvolutionNode(perName.get("Flotajou"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Flotoutan"), null));}});
        p.catchRate = "75";
        p.weight = "29,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Bekipan");
        p.evolutions = new EvolutionNode(perName.get("Goelise"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Bekipan"), null));}});
        p.catchRate = "45";
        p.weight = "28,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Eau 1/Vol";
        p.size = "1,2m";

        p = perName.get("Dinoclier");
        p.evolutions = new EvolutionNode(perName.get("Dinoclier"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Bastiodon"), null));}});
        p.catchRate = "45";
        p.weight = "57,0kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Monstre";
        p.size = "0,5m";

        p = perName.get("Absol");
        p.evolutions = new EvolutionNode(perName.get("Absol"), new HashMap<String, EvolutionNode>(){{this.put("Absolite", new EvolutionNode(perName.get("Mega-Absol"), null));}});
        p.catchRate = "30";
        p.weight = "47,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol";
        p.size = "1,2m";

        p = perName.get("Azurill");
        p.evolutions = new EvolutionNode(perName.get("Azurill"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Marill"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Azumarill"), null));}}));}});
        p.catchRate = "60";
        p.weight = "2,0kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+1 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "0,2m";

        p = perName.get("Cacnea");
        p.evolutions = new EvolutionNode(perName.get("Cacnea"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Cacturne"), null));}});
        p.catchRate = "190";
        p.weight = "51,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Plante/Humanoide";
        p.size = "0,4m";

        p = perName.get("Apireine");
        p.evolutions = new EvolutionNode(perName.get("Apitrini"), new HashMap<String, EvolutionNode>(){{this.put("Si Femelle, Niveau 21", new EvolutionNode(perName.get("Apireine"), null));}});
        p.catchRate = "45";
        p.weight = "38,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+1 Def.; +1 Def. Spe";
        p.eggGroup = "Insecte";
        p.size = "1,2m";

        p = perName.get("Dracaufeu");
        p.evolutions = new EvolutionNode(perName.get("Salameche"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Reptincel"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Dracaufeu"), new HashMap<String, EvolutionNode>(){{this.put("Dracaufite X", new EvolutionNode(perName.get("Mega-Dracaufeu X"), null));this.put("Dracaufite Y", new EvolutionNode(perName.get("Mega-Dracaufeu Y"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "90,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Dragon/Monstre";
        p.size = "1,7m";

        p = perName.get("Solochi");
        p.evolutions = new EvolutionNode(perName.get("Solochi"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 50", new EvolutionNode(perName.get("Diamat"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 64", new EvolutionNode(perName.get("Trioxhydre"), null));}}));}});
        p.catchRate = "45";
        p.weight = "17,3kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Dragon";
        p.size = "0,8m";

        p = perName.get("Motisma (Forme Tonte)");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "0,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att. Spe; +1 Vit.";
        p.eggGroup = "Indetermine";
        p.size = "0,3m";

        p = perName.get("Volcaropod");
        p.evolutions = new EvolutionNode(perName.get("Limagma"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 38", new EvolutionNode(perName.get("Volcaropod"), null));}});
        p.catchRate = "75";
        p.weight = "55,0kg";
        p.hatch = "21 cycles - 5610 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Indetermine";
        p.size = "0,8m";

        p = perName.get("Boreas (Forme Totemique)");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "63,0kg";
        p.hatch = "120 cycles - 30855 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "1,5m";

        p = perName.get("Meloetta (Forme Voix)");
        p.evolutions = null;
        p.catchRate = "5";
        p.weight = "6,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att. Spe; +1 Def. Spe; +1 Vit.";
        p.eggGroup = "Sans oeuf";
        p.size = "0,6m";

        p = perName.get("Snubbull");
        p.evolutions = new EvolutionNode(perName.get("Snubbull"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 23", new EvolutionNode(perName.get("Granbull"), null));}});
        p.catchRate = "190";
        p.weight = "7,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol/Fee";
        p.size = "0,6m";

        p = perName.get("Sharpedo");
        p.evolutions = new EvolutionNode(perName.get("Carvanha"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Sharpedo"), null));}});
        p.catchRate = "60";
        p.weight = "88,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Eau 2";
        p.size = "1,8m";

        p = perName.get("Noeunoeuf");
        p.evolutions = new EvolutionNode(perName.get("Noeunoeuf"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get("Noadkoko"), null));}});
        p.catchRate = "90";
        p.weight = "2,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Plante";
        p.size = "0,4m";

        p = perName.get("Mega-Mewtwo Y");
        p.evolutions = new EvolutionNode(perName.get("Mewtwo"), new HashMap<String, EvolutionNode>(){{this.put("Mewtwoite X", new EvolutionNode(perName.get("Mega-Mewtwo X"), null));this.put("Mewtwoite Y", new EvolutionNode(perName.get("Mega-Mewtwo Y"), null));}});
        p.catchRate = "";
        p.weight = "33,0kg";
        p.hatch = "";
        p.gender = "Asexue";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,5m";

        p = perName.get("Tutafeh");
        p.evolutions = new EvolutionNode(perName.get("Tutafeh"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 34", new EvolutionNode(perName.get("Tutankafer"), null));}});
        p.catchRate = "190";
        p.weight = "1,5kg";
        p.hatch = "25 cycles - 6630 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Mineral/Indetermine";
        p.size = "0,5m";

        p = perName.get("Zigzaton");
        p.evolutions = new EvolutionNode(perName.get("Zigzaton"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Lineon"), null));}});
        p.catchRate = "255";
        p.weight = "17,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,4m";

        p = perName.get("Melodelfe");
        p.evolutions = new EvolutionNode(perName.get("Melo"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Melofee"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get("Melodelfe"), null));}}));}});
        p.catchRate = "25";
        p.weight = "40,0kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+3 PV";
        p.eggGroup = "Fee";
        p.size = "1,3m";

        p = perName.get("Mega-Mewtwo X");
        p.evolutions = new EvolutionNode(perName.get("Mewtwo"), new HashMap<String, EvolutionNode>(){{this.put("Mewtwoite X", new EvolutionNode(perName.get("Mega-Mewtwo X"), null));this.put("Mewtwoite Y", new EvolutionNode(perName.get("Mega-Mewtwo Y"), null));}});
        p.catchRate = "";
        p.weight = "127,0kg";
        p.hatch = "";
        p.gender = "Asexue";
        p.ev = "";
        p.eggGroup = "";
        p.size = "2,3m";

        p = perName.get("Airmure");
        p.evolutions = null;
        p.catchRate = "25";
        p.weight = "50,5kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Vol";
        p.size = "1,7m";

        p = perName.get("Celebi");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "5,0kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "0,6m";

        p = perName.get("Cocotine");
        p.evolutions = new EvolutionNode(perName.get("Fluvetin"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Sachet Senteur", new EvolutionNode(perName.get("Cocotine"), null));}});
        p.catchRate = "";
        p.weight = "15,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Fee";
        p.size = "0,8m";

        p = perName.get("Ptitard");
        p.evolutions = new EvolutionNode(perName.get("Ptitard"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Tetarte"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Roche Royale", new EvolutionNode(perName.get("Tarpaud"), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Tartard"), null));}}));}});
        p.catchRate = "255";
        p.weight = "12,4kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Eau 1";
        p.size = "0,6m";

        p = perName.get("Zorua");
        p.evolutions = new EvolutionNode(perName.get("Zorua"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Zoroark"), null));}});
        p.catchRate = "75";
        p.weight = "12,5kg";
        p.hatch = "25 cycles - 6630 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "0,7m";

        p = perName.get("Mega-Elecsprint");
        p.evolutions = new EvolutionNode(perName.get("Dynavolt"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 26", new EvolutionNode(perName.get("Elecsprint"), new HashMap<String, EvolutionNode>(){{this.put("Elecsprintite", new EvolutionNode(perName.get("Mega-Elecsprint"), null));}}));}});
        p.catchRate = "";
        p.weight = "44kg";
        p.hatch = "";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,8m";

        p = perName.get("Carabing");
        p.evolutions = new EvolutionNode(perName.get("Carabing"), new HashMap<String, EvolutionNode>(){{this.put("Echange avec Escargaume", new EvolutionNode(perName.get("Lancargot"), null));}});
        p.catchRate = "200";
        p.weight = "5,9kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Insecte";
        p.size = "0,5m";

        p = perName.get("Okeoke");
        p.evolutions = new EvolutionNode(perName.get("Okeoke"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 15", new EvolutionNode(perName.get("Qulbutoke"), null));}});
        p.catchRate = "125";
        p.weight = "14,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "0,6m";

        p = perName.get("Hypotrempe");
        p.evolutions = new EvolutionNode(perName.get("Hypotrempe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Hypocean"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Ecaille Draco", new EvolutionNode(perName.get("Hyporoi"), null));}}));}});
        p.catchRate = "225";
        p.weight = "8,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Eau 1/Dragon";
        p.size = "0,4m";

        p = perName.get("Nymphali");
        p.evolutions = new EvolutionNode(perName.get("Evoli"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get("Voltali"), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get("Phyllali"), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get("Mentali"), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get("Nymphali"), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Aquali"), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get("Givrali"), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get("Pyroli"), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get("Noctali"), null));}});
        p.catchRate = "45";
        p.weight = "23,5kg";
        p.hatch = "34 cycles - 8960 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Venalgue");
        p.evolutions = new EvolutionNode(perName.get("Venalgue"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 48", new EvolutionNode(perName.get("Kravarech"), null));}});
        p.catchRate = "";
        p.weight = "7,3kg";
        p.hatch = "pas";
        p.gender = "Repartition inconnue";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Eau 1/Dragon";
        p.size = "0,5m";

        p = perName.get("Mega-Scarabrute");
        p.evolutions = new EvolutionNode(perName.get("Scarabrute"), new HashMap<String, EvolutionNode>(){{this.put("Scarabruite", new EvolutionNode(perName.get("Mega-Scarabrute"), null));}});
        p.catchRate = "";
        p.weight = "59kg";
        p.hatch = "";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,7m";

        p = perName.get("Maraiste");
        p.evolutions = new EvolutionNode(perName.get("Axoloto"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Maraiste"), null));}});
        p.catchRate = "90";
        p.weight = "75,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Eau 1/Sol";
        p.size = "1,4m";

        p = perName.get("Mega-Florizarre");
        p.evolutions = new EvolutionNode(perName.get("Bulbizarre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Herbizarre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Florizarre"), new HashMap<String, EvolutionNode>(){{this.put("Florizarrite", new EvolutionNode(perName.get("Mega-Florizarre"), null));}}));}}));}});
        p.catchRate = "";
        p.weight = "155,5kg";
        p.hatch = "";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "2,4m";

        p = perName.get("Papilusion");
        p.evolutions = new EvolutionNode(perName.get("Chenipan"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 7", new EvolutionNode(perName.get("Chrysacier"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 10", new EvolutionNode(perName.get("Papilusion"), null));}}));}});
        p.catchRate = "45";
        p.weight = "32,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe; +1 Def. Spe";
        p.eggGroup = "Insecte";
        p.size = "1,1m";

        p = perName.get("Charpenti");
        p.evolutions = new EvolutionNode(perName.get("Charpenti"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Ouvrifier"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Betochef"), null));}}));}});
        p.catchRate = "190";
        p.weight = "12,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Humanoide";
        p.size = "0,6m";

        p = perName.get("Doduo");
        p.evolutions = new EvolutionNode(perName.get("Doduo"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 31", new EvolutionNode(perName.get("Dodrio"), null));}});
        p.catchRate = "190";
        p.weight = "39,2kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Vol";
        p.size = "1,4m";

        p = perName.get("Coatox");
        p.evolutions = new EvolutionNode(perName.get("Cradopaud"), new HashMap<String, EvolutionNode>(){{this.put("niveau 37", new EvolutionNode(perName.get("Coatox"), null));}});
        p.catchRate = "75";
        p.weight = "44,4kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Humanoide";
        p.size = "1,3m";

        p = perName.get("Charmina");
        p.evolutions = new EvolutionNode(perName.get("Meditikka"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Charmina"), new HashMap<String, EvolutionNode>(){{this.put("Charminite", new EvolutionNode(perName.get("Mega-Charmina"), null));}}));}});
        p.catchRate = "90";
        p.weight = "31,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Humanoide";
        p.size = "1,3m";

        p = perName.get("Chinchidou");
        p.evolutions = new EvolutionNode(perName.get("Chinchidou"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get("Pashmilla"), null));}});
        p.catchRate = "255";
        p.weight = "5,8kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,4m";

        p = perName.get("Pitrouille (Taille Maxi)");
        p.evolutions = new EvolutionNode(perName.get("Pitrouille (Taille Maxi)"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Banshitrouye (Taille Maxi)"), null));}});
        p.catchRate = "";
        p.weight = "3,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Indetermine";
        p.size = "0,3m";

        p = perName.get("Cheniselle (Cape Dechet)");
        p.evolutions = new EvolutionNode(perName.get("Cheniti"), new HashMap<String, EvolutionNode>(){{this.put("Si Male, Niveau 20", new EvolutionNode(perName.get("Papilord"), null));this.put("Si Femelle, Niveau 20", new EvolutionNode(perName.get("Cheniselle (Cape Dechet)"), null));}});
        p.catchRate = "45";
        p.weight = "6,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Insecte";
        p.size = "0,5m";

        p = perName.get("Exagide (Forme Assaut)");
        p.evolutions = new EvolutionNode(perName.get("Monorpale"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Dimocles"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get("Exagide (Forme Assaut)"), null));}}));}});
        p.catchRate = "";
        p.weight = "53,0kg";
        p.hatch = "18 cycles - 4845 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.; +1 Def. Spe";
        p.eggGroup = "Mineral";
        p.size = "1,7m";

        p = perName.get("Tarsal");
        p.evolutions = new EvolutionNode(perName.get("Tarsal"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Kirlia"), new HashMap<String, EvolutionNode>(){{this.put("Male + Pierre Aube", new EvolutionNode(perName.get("Gallame"), null));this.put("Niveau 30", new EvolutionNode(perName.get("Gardevoir"), new HashMap<String, EvolutionNode>(){{this.put("Gardevoirite", new EvolutionNode(perName.get("Mega-Gardevoir"), null));}}));}}));}});
        p.catchRate = "235";
        p.weight = "6,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Indetermine";
        p.size = "0,4m";

        p = perName.get("Scalpion");
        p.evolutions = new EvolutionNode(perName.get("Scalpion"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 52", new EvolutionNode(perName.get("Scalproie"), null));}});
        p.catchRate = "120";
        p.weight = "10,2kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Humanoide";
        p.size = "0,5m";

        p = perName.get("Galegon");
        p.evolutions = new EvolutionNode(perName.get("Galekid"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Galegon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 42", new EvolutionNode(perName.get("Galeking"), new HashMap<String, EvolutionNode>(){{this.put("Galekingite", new EvolutionNode(perName.get("Mega-Galeking"), null));}}));}}));}});
        p.catchRate = "90";
        p.weight = "120,0kg";
        p.hatch = "34 cycles - 8960 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Monstre";
        p.size = "0,9m";

        p = perName.get("Smogogo");
        p.evolutions = new EvolutionNode(perName.get("Smogo"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Smogogo"), null));}});
        p.catchRate = "60";
        p.weight = "9,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Indetermine";
        p.size = "1,2m";

        p = perName.get("Baudrive");
        p.evolutions = new EvolutionNode(perName.get("Baudrive"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 28", new EvolutionNode(perName.get("Grodrive"), null));}});
        p.catchRate = "125";
        p.weight = "1,2kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Indetermine";
        p.size = "0,4m";

        p = perName.get("Libegon");
        p.evolutions = new EvolutionNode(perName.get("Kraknoix"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Vibraninf"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 45", new EvolutionNode(perName.get("Libegon"), null));}}));}});
        p.catchRate = "45";
        p.weight = "82,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.; +2 Vit.";
        p.eggGroup = "Insecte";
        p.size = "2,0m";

        p = perName.get("Judokrak");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "55,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+2 PV";
        p.eggGroup = "Humanoide";
        p.size = "1,3m";

        p = perName.get("Korillon");
        p.evolutions = new EvolutionNode(perName.get("Korillon"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur , Nuit", new EvolutionNode(perName.get("Eoko"), null));}});
        p.catchRate = "120";
        p.weight = "0,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "0,2m";

        p = perName.get("Boguerisse");
        p.evolutions = new EvolutionNode(perName.get("Marisson"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Boguerisse"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Blindepique"), null));}}));}});
        p.catchRate = "45";
        p.weight = "29,0kg";
        p.hatch = "pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Sol";
        p.size = "0,7m";

        p = perName.get("Mime Jr.");
        p.evolutions = new EvolutionNode(perName.get("Mime Jr."), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l'attaque Copie", new EvolutionNode(perName.get("M. Mime"), null));}});
        p.catchRate = "145";
        p.weight = "13,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "0,6m";

        p = perName.get("Queulorior");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "58,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "1,2m";

        p = perName.get("Ecremeuh");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "75,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Sol";
        p.size = "1,2m";

        p = perName.get("Lineon");
        p.evolutions = new EvolutionNode(perName.get("Zigzaton"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Lineon"), null));}});
        p.catchRate = "90";
        p.weight = "32,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,5m";

        p = perName.get("Osselait");
        p.evolutions = new EvolutionNode(perName.get("Osselait"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 28", new EvolutionNode(perName.get("Ossatueur"), null));}});
        p.catchRate = "190";
        p.weight = "6,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Monstre";
        p.size = "0,4m";

        p = perName.get("Castorno");
        p.evolutions = new EvolutionNode(perName.get("Keunotor"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 15", new EvolutionNode(perName.get("Castorno"), null));}});
        p.catchRate = "127";
        p.weight = "31,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Eau 1/Sol";
        p.size = "1,0m";

        p = perName.get("Heliatronc");
        p.evolutions = new EvolutionNode(perName.get("Tournegrin"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierresoleil", new EvolutionNode(perName.get("Heliatronc"), null));}});
        p.catchRate = "120";
        p.weight = "8,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Plante";
        p.size = "0,8m";

        p = perName.get("Hypnomade");
        p.evolutions = new EvolutionNode(perName.get("Soporifik"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 26", new EvolutionNode(perName.get("Hypnomade"), null));}});
        p.catchRate = "75";
        p.weight = "75,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Humanoide";
        p.size = "1,6m";

        p = perName.get("Electrode");
        p.evolutions = new EvolutionNode(perName.get("Voltorbe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Electrode"), null));}});
        p.catchRate = "60";
        p.weight = "66,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+2 Vit.";
        p.eggGroup = "Mineral";
        p.size = "1,2m";

        p = perName.get("Motisma (Forme Helice)");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "0,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att. Spe; +1 Vit.";
        p.eggGroup = "Indetermine";
        p.size = "0,3m";

        p = perName.get("Kranidos");
        p.evolutions = new EvolutionNode(perName.get("Kranidos"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Charkos"), null));}});
        p.catchRate = "45";
        p.weight = "31,5kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Monstre";
        p.size = "0,9m";

        p = perName.get("Mammochon");
        p.evolutions = new EvolutionNode(perName.get("Marcacrin"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 33", new EvolutionNode(perName.get("Cochignon"), new HashMap<String, EvolutionNode>(){{this.put("En connaissant l'attaque Pouv.Antique et lui faire monter d'un niveau", new EvolutionNode(perName.get("Mammochon"), null));}}));}});
        p.catchRate = "50";
        p.weight = "291,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Sol";
        p.size = "2,5m";

        p = perName.get("Moufouette");
        p.evolutions = new EvolutionNode(perName.get("Moufouette"), new HashMap<String, EvolutionNode>(){{this.put("niveau 34", new EvolutionNode(perName.get("Moufflair"), null));}});
        p.catchRate = "225";
        p.weight = "19,2kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,4m";

        p = perName.get("Miasmax");
        p.evolutions = new EvolutionNode(perName.get("Miamiasme"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Miasmax"), null));}});
        p.catchRate = "60";
        p.weight = "107,3kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Mineral";
        p.size = "1,9m";

        p = perName.get("Aflamanoir");
        p.evolutions = null;
        p.catchRate = "90";
        p.weight = "58,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att Spe.";
        p.eggGroup = "Sol";
        p.size = "1,4m";

        p = perName.get("Makuhita");
        p.evolutions = new EvolutionNode(perName.get("Makuhita"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 24", new EvolutionNode(perName.get("Hariyama"), null));}});
        p.catchRate = "180";
        p.weight = "86,4kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+1 PV";
        p.eggGroup = "Humanoide";
        p.size = "1,0m";

        p = perName.get("Cerfrousse");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "71,2kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol";
        p.size = "1,4m";

        p = perName.get("Alakazam");
        p.evolutions = new EvolutionNode(perName.get("Abra"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Kadabra"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Alakazam"), new HashMap<String, EvolutionNode>(){{this.put("Alakazamite", new EvolutionNode(perName.get("Mega-Alakazam"), null));}}));}}));}});
        p.catchRate = "50";
        p.weight = "48,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Humanoide";
        p.size = "1,5m";

        p = perName.get("Reptincel");
        p.evolutions = new EvolutionNode(perName.get("Salameche"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Reptincel"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Dracaufeu"), new HashMap<String, EvolutionNode>(){{this.put("Dracaufite X", new EvolutionNode(perName.get("Mega-Dracaufeu X"), null));this.put("Dracaufite Y", new EvolutionNode(perName.get("Mega-Dracaufeu Y"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "19,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Vit.; +1 Att. Spe";
        p.eggGroup = "Monstre/Dragon";
        p.size = "1,1m";

        p = perName.get("Carapagos");
        p.evolutions = new EvolutionNode(perName.get("Carapagos"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Megapagos"), null));}});
        p.catchRate = "45";
        p.weight = "16,5kg";
        p.hatch = "30 cycles - 7905 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Eau 1/Eau 3";
        p.size = "0,7m";

        p = perName.get("Hypocean");
        p.evolutions = new EvolutionNode(perName.get("Hypotrempe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Hypocean"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Ecaille Draco", new EvolutionNode(perName.get("Hyporoi"), null));}}));}});
        p.catchRate = "75";
        p.weight = "25,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.; +1 Att. Spe";
        p.eggGroup = "Eau 1/Dragon";
        p.size = "1,2m";

        p = perName.get("Tortipouss");
        p.evolutions = new EvolutionNode(perName.get("Tortipouss"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Boskara"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Torterra"), null));}}));}});
        p.catchRate = "45";
        p.weight = "10,2kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Monstre/Plante";
        p.size = "0,4m";

        p = perName.get("Stalgamin");
        p.evolutions = new EvolutionNode(perName.get("Stalgamin"), new HashMap<String, EvolutionNode>(){{this.put("Femelle + Pierre Aube", new EvolutionNode(perName.get("Momartik"), null));this.put("Niveau 42", new EvolutionNode(perName.get("Oniglali"), null));}});
        p.catchRate = "190";
        p.weight = "16,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Fee/Mineral";
        p.size = "0,7m";

        p = perName.get("Lancargot");
        p.evolutions = new EvolutionNode(perName.get("Carabing"), new HashMap<String, EvolutionNode>(){{this.put("Echange avec Escargaume", new EvolutionNode(perName.get("Lancargot"), null));}});
        p.catchRate = "75";
        p.weight = "33,0kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Insecte";
        p.size = "1,0m";

        p = perName.get("Chuchmur");
        p.evolutions = new EvolutionNode(perName.get("Chuchmur"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Ramboum"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Brouhabam"), null));}}));}});
        p.catchRate = "190";
        p.weight = "16,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Monstre/Sol";
        p.size = "0,6m";

        p = perName.get("Motisma (Forme Normale)");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "0,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att. Spe; +1 Vit.";
        p.eggGroup = "Indetermine";
        p.size = "0,3m";

        p = perName.get("Maganon");
        p.evolutions = new EvolutionNode(perName.get("Magby"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Magmar"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Magmariseur", new EvolutionNode(perName.get("Maganon"), null));}}));}});
        p.catchRate = "30";
        p.weight = "68,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Humanoide";
        p.size = "1,6m";

        p = perName.get("Parecool");
        p.evolutions = new EvolutionNode(perName.get("Parecool"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Vigoroth"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Monaflemit"), null));}}));}});
        p.catchRate = "255";
        p.weight = "24,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Sol";
        p.size = "0,8m";

        p = perName.get("Wattouat");
        p.evolutions = new EvolutionNode(perName.get("Wattouat"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 15", new EvolutionNode(perName.get("Lainergie"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Pharamp"), new HashMap<String, EvolutionNode>(){{this.put("Pharampite", new EvolutionNode(perName.get("Mega-Pharamp"), null));}}));}}));}});
        p.catchRate = "235";
        p.weight = "7,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Sol/Monstre";
        p.size = "0,6m";

        p = perName.get("Opermine");
        p.evolutions = new EvolutionNode(perName.get("Opermine"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 39", new EvolutionNode(perName.get("Golgopathe"), null));}});
        p.catchRate = "";
        p.weight = "31,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Eau 3";
        p.size = "0,5m";

        p = perName.get("Mega-Demolosse");
        p.evolutions = new EvolutionNode(perName.get("Malosse"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 24", new EvolutionNode(perName.get("Demolosse"), new HashMap<String, EvolutionNode>(){{this.put("Demolossite", new EvolutionNode(perName.get("Mega-Demolosse"), null));}}));}});
        p.catchRate = "";
        p.weight = "35kg";
        p.hatch = "";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,4m";

        p = perName.get("Anchwatt");
        p.evolutions = new EvolutionNode(perName.get("Anchwatt"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 39", new EvolutionNode(perName.get("Lamperoie"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get("Ohmassacre"), null));}}));}});
        p.catchRate = "190";
        p.weight = "0,3kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Indetermine";
        p.size = "0,2m";

        p = perName.get("Posipi");
        p.evolutions = null;
        p.catchRate = "200";
        p.weight = "4,2kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Fee";
        p.size = "0,4m";

        p = perName.get("Herbizarre");
        p.evolutions = new EvolutionNode(perName.get("Bulbizarre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Herbizarre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Florizarre"), new HashMap<String, EvolutionNode>(){{this.put("Florizarrite", new EvolutionNode(perName.get("Mega-Florizarre"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "13,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att. Spe; +1 Def. Spe";
        p.eggGroup = "Monstre/Plante";
        p.size = "1,0m";

        p = perName.get("Exagide (Forme Parade)");
        p.evolutions = new EvolutionNode(perName.get("Monorpale"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Dimocles"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get("Exagide (Forme Parade)"), null));}}));}});
        p.catchRate = "";
        p.weight = "53,0kg";
        p.hatch = "18 cycles - 4845 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.; +1 Def. Spe";
        p.eggGroup = "Mineral";
        p.size = "1,7m";

        p = perName.get("Elekid");
        p.evolutions = new EvolutionNode(perName.get("Elekid"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Elektek"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Electiriseur", new EvolutionNode(perName.get("Elekable"), null));}}));}});
        p.catchRate = "45";
        p.weight = "23,5kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sans oeuf";
        p.size = "0,6m";

        p = perName.get("Sulfura");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "60,0kg";
        p.hatch = "79 cycles - 20480 pas";
        p.gender = "Asexue";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "2,0m";

        p = perName.get("Balbuto");
        p.evolutions = new EvolutionNode(perName.get("Balbuto"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Kaorine"), null));}});
        p.catchRate = "255";
        p.weight = "21,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+1 Vit.";
        p.eggGroup = "Mineral";
        p.size = "0,5m";

        p = perName.get("Yanma");
        p.evolutions = new EvolutionNode(perName.get("Yanma"), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l' attaque  Pouv.Antique", new EvolutionNode(perName.get("Yanmega"), null));}});
        p.catchRate = "75";
        p.weight = "38,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Insecte";
        p.size = "1,2m";

        p = perName.get("Poichigeon");
        p.evolutions = new EvolutionNode(perName.get("Poichigeon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 21", new EvolutionNode(perName.get("Colombeau"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Deflaisan"), null));}}));}});
        p.catchRate = "255";
        p.weight = "2,1kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Vol";
        p.size = "0,3m";

        p = perName.get("Lamperoie");
        p.evolutions = new EvolutionNode(perName.get("Anchwatt"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 39", new EvolutionNode(perName.get("Lamperoie"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get("Ohmassacre"), null));}}));}});
        p.catchRate = "60";
        p.weight = "22,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Indetermine";
        p.size = "1,2m";

        p = perName.get("Kirlia");
        p.evolutions = new EvolutionNode(perName.get("Tarsal"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Kirlia"), new HashMap<String, EvolutionNode>(){{this.put("Male + Pierre Aube", new EvolutionNode(perName.get("Gallame"), null));this.put("Niveau 30", new EvolutionNode(perName.get("Gardevoir"), new HashMap<String, EvolutionNode>(){{this.put("Gardevoirite", new EvolutionNode(perName.get("Mega-Gardevoir"), null));}}));}}));}});
        p.catchRate = "120";
        p.weight = "20,2kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Indetermine";
        p.size = "0,8m";

        p = perName.get("Chaffreux");
        p.evolutions = new EvolutionNode(perName.get("Chaglam"), new HashMap<String, EvolutionNode>(){{this.put("niveau 38", new EvolutionNode(perName.get("Chaffreux"), null));}});
        p.catchRate = "75";
        p.weight = "43,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Mystherbe");
        p.evolutions = new EvolutionNode(perName.get("Mystherbe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 21", new EvolutionNode(perName.get("Ortide"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get("Rafflesia"), null));this.put("Avec une Pierresoleil", new EvolutionNode(perName.get("Joliflor"), null));}}));}});
        p.catchRate = "255";
        p.weight = "5,4kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Plante";
        p.size = "0,5m";

        p = perName.get("Metang");
        p.evolutions = new EvolutionNode(perName.get("Terhal"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Metang"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 45", new EvolutionNode(perName.get("Metalosse"), null));}}));}});
        p.catchRate = "3";
        p.weight = "202,5kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "Asexue";
        p.ev = "+2 Def.";
        p.eggGroup = "Mineral";
        p.size = "1,2m";

        p = perName.get("Tritosor");
        p.evolutions = new EvolutionNode(perName.get("Sancoki"), new HashMap<String, EvolutionNode>(){{this.put("niveau 30", new EvolutionNode(perName.get("Tritosor"), null));}});
        p.catchRate = "75";
        p.weight = "29,9kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Eau 1/Indetermine";
        p.size = "0,9m";

        p = perName.get("Dracolosse");
        p.evolutions = new EvolutionNode(perName.get("Minidraco"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Draco"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 55", new EvolutionNode(perName.get("Dracolosse"), null));}}));}});
        p.catchRate = "45";
        p.weight = "210,0kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Dragon/Eau 1";
        p.size = "2,2m";

        p = perName.get("Fragilady");
        p.evolutions = new EvolutionNode(perName.get("Chlorobule"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierresoleil", new EvolutionNode(perName.get("Fragilady"), null));}});
        p.catchRate = "75";
        p.weight = "16,3kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Plante";
        p.size = "1,1m";

        p = perName.get("Fulguris (Forme Totemique)");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "65kg";
        p.hatch = "120 cycles - 30855 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "1,5m";

        p = perName.get("Nidorino");
        p.evolutions = new EvolutionNode(perName.get("Nidoran M"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Nidorino"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get("Nidoking"), null));}}));}});
        p.catchRate = "120";
        p.weight = "19,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Monstre/Sol";
        p.size = "0,9m";

        p = perName.get("Branette");
        p.evolutions = new EvolutionNode(perName.get("Polichombr"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Branette"), new HashMap<String, EvolutionNode>(){{this.put("Branettite", new EvolutionNode(perName.get("Mega-Branette"), null));}}));}});
        p.catchRate = "45";
        p.weight = "12,5kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Indetermine";
        p.size = "1,1m";

        p = perName.get("Nidorina");
        p.evolutions = new EvolutionNode(perName.get("Nidoran F"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Nidorina"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get("Nidoqueen"), null));}}));}});
        p.catchRate = "120";
        p.weight = "20,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+2 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "0,8m";

        p = perName.get("Rhinoferos");
        p.evolutions = new EvolutionNode(perName.get("Rhinocorne"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 42", new EvolutionNode(perName.get("Rhinoferos"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Protecteur", new EvolutionNode(perName.get("Rhinastoc"), null));}}));}});
        p.catchRate = "60";
        p.weight = "120,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Monstre/Sol";
        p.size = "1,9m";

        p = perName.get("Regigigas");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "420,0kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 Att.";
        p.eggGroup = "Sans oeuf";
        p.size = "3,7m";

        p = perName.get("Tentacruel");
        p.evolutions = new EvolutionNode(perName.get("Tentacool"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Tentacruel"), null));}});
        p.catchRate = "60";
        p.weight = "55,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Eau 3";
        p.size = "1,6m";

        p = perName.get("Chlorobule");
        p.evolutions = new EvolutionNode(perName.get("Chlorobule"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierresoleil", new EvolutionNode(perName.get("Fragilady"), null));}});
        p.catchRate = "190";
        p.weight = "6,6kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Plante";
        p.size = "0,5m";

        p = perName.get("Mateloutre");
        p.evolutions = new EvolutionNode(perName.get("Moustillon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 17", new EvolutionNode(perName.get("Mateloutre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Clamiral"), null));}}));}});
        p.catchRate = "45";
        p.weight = "24,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att. Spe.";
        p.eggGroup = "Sol";
        p.size = "0,8m";

        p = perName.get("Flagadoss");
        p.evolutions = new EvolutionNode(perName.get("Ramoloss"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Flagadoss"), null));this.put("Echange en tenant Roche Royale", new EvolutionNode(perName.get("Roigada"), null));}});
        p.catchRate = "75";
        p.weight = "78,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Monstre/Eau 1";
        p.size = "1,6m";

        p = perName.get("Crikzik");
        p.evolutions = new EvolutionNode(perName.get("Crikzik"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 10", new EvolutionNode(perName.get("Melokrik"), null));}});
        p.catchRate = "255";
        p.weight = "2,2kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Insecte";
        p.size = "0,3m";

        p = perName.get("Florges");
        p.evolutions = new EvolutionNode(perName.get("Flabebe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 19", new EvolutionNode(perName.get("Floette"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get("Florges"), null));}}));}});
        p.catchRate = "";
        p.weight = "10,0kg";
        p.hatch = "pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+3 Def. Spe";
        p.eggGroup = "Fee";
        p.size = "1,1m";

        p = perName.get("Scarabrute");
        p.evolutions = new EvolutionNode(perName.get("Scarabrute"), new HashMap<String, EvolutionNode>(){{this.put("Scarabruite", new EvolutionNode(perName.get("Mega-Scarabrute"), null));}});
        p.catchRate = "45";
        p.weight = "55,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Insecte";
        p.size = "1,5m";

        p = perName.get("Mimigal");
        p.evolutions = new EvolutionNode(perName.get("Mimigal"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 22", new EvolutionNode(perName.get("Migalos"), null));}});
        p.catchRate = "255";
        p.weight = "8,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Insecte";
        p.size = "0,5m";

        p = perName.get("Porygon-Z");
        p.evolutions = new EvolutionNode(perName.get("Porygon"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Ameliorator", new EvolutionNode(perName.get("Porygon2"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant CD Douteux", new EvolutionNode(perName.get("Porygon-Z"), null));}}));}});
        p.catchRate = "30";
        p.weight = "34,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Mineral";
        p.size = "0,9m";

        p = perName.get("Dodrio");
        p.evolutions = new EvolutionNode(perName.get("Doduo"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 31", new EvolutionNode(perName.get("Dodrio"), null));}});
        p.catchRate = "45";
        p.weight = "85,2kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Vol";
        p.size = "1,8m";

        p = perName.get("Pijako");
        p.evolutions = null;
        p.catchRate = "30";
        p.weight = "1,9kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Vol";
        p.size = "0,5m";

        p = perName.get("Lepidonille");
        p.evolutions = new EvolutionNode(perName.get("Lepidonille"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 9", new EvolutionNode(perName.get("Peregrain"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 12", new EvolutionNode(perName.get("Prismillon"), null));}}));}});
        p.catchRate = "";
        p.weight = "2,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Insecte";
        p.size = "0,3m";

        p = perName.get("Bargantua");
        p.evolutions = null;
        p.catchRate = "25";
        p.weight = "18,0kg";
        p.hatch = "40 cycles - 10455 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Eau 2";
        p.size = "1,0m";

        p = perName.get("Chrysacier");
        p.evolutions = new EvolutionNode(perName.get("Chenipan"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 7", new EvolutionNode(perName.get("Chrysacier"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 10", new EvolutionNode(perName.get("Papilusion"), null));}}));}});
        p.catchRate = "120";
        p.weight = "9,9kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Insecte";
        p.size = "0,7m";

        p = perName.get("Genesect");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "82,5kg";
        p.hatch = "120 cycles - 30855 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att.; +1 Att. Spe; +1 Vit.";
        p.eggGroup = "Sans oeuf";
        p.size = "1,5m";

        p = perName.get("Lilia");
        p.evolutions = new EvolutionNode(perName.get("Lilia"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Vacilys"), null));}});
        p.catchRate = "45";
        p.weight = "23,8kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Eau 3";
        p.size = "1,0m";

        p = perName.get("Givrali");
        p.evolutions = new EvolutionNode(perName.get("Evoli"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get("Voltali"), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get("Phyllali"), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get("Mentali"), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get("Nymphali"), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Aquali"), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get("Givrali"), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get("Pyroli"), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get("Noctali"), null));}});
        p.catchRate = "45";
        p.weight = "25,9kg";
        p.hatch = "34 cycles - 8960 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "0,8m";

        p = perName.get("Gloupti");
        p.evolutions = new EvolutionNode(perName.get("Gloupti"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 26", new EvolutionNode(perName.get("Avaltout"), null));}});
        p.catchRate = "225";
        p.weight = "10,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Indetermine";
        p.size = "0,4m";

        p = perName.get("Miamiasme");
        p.evolutions = new EvolutionNode(perName.get("Miamiasme"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Miasmax"), null));}});
        p.catchRate = "190";
        p.weight = "31,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Mineral";
        p.size = "0,6m";

        p = perName.get("Togepi");
        p.evolutions = new EvolutionNode(perName.get("Togepi"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Togetic"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get("Togekiss"), null));}}));}});
        p.catchRate = "190";
        p.weight = "1,5kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "0,3m";

        p = perName.get("Corboss");
        p.evolutions = new EvolutionNode(perName.get("Cornebre"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get("Corboss"), null));}});
        p.catchRate = "30";
        p.weight = "27,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Vol";
        p.size = "0,9m";

        p = perName.get("Flamajou");
        p.evolutions = new EvolutionNode(perName.get("Flamajou"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Feu", new EvolutionNode(perName.get("Flamoutan"), null));}});
        p.catchRate = "190";
        p.weight = "11,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,5m";

        p = perName.get("Etourvol");
        p.evolutions = new EvolutionNode(perName.get("Etourmi"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 14", new EvolutionNode(perName.get("Etourvol"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 34", new EvolutionNode(perName.get("Etouraptor"), null));}}));}});
        p.catchRate = "120";
        p.weight = "15,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Vol";
        p.size = "0,6m";

        p = perName.get("Abo");
        p.evolutions = new EvolutionNode(perName.get("Abo"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 22", new EvolutionNode(perName.get("Arbok"), null));}});
        p.catchRate = "255";
        p.weight = "6,9kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol/Dragon";
        p.size = "2,0m";

        p = perName.get("Rondoudou");
        p.evolutions = new EvolutionNode(perName.get("Toudoudou"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Rondoudou"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get("Grodoudou"), null));}}));}});
        p.catchRate = "170";
        p.weight = "5,5kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+2 PV";
        p.eggGroup = "Fee";
        p.size = "0,5m";

        p = perName.get("Octillery");
        p.evolutions = new EvolutionNode(perName.get("Remoraid"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Octillery"), null));}});
        p.catchRate = "75";
        p.weight = "28,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.; +1 Att. Spe";
        p.eggGroup = "Eau 1/Eau 2";
        p.size = "0,9m";

        p = perName.get("Roitiflam");
        p.evolutions = new EvolutionNode(perName.get("Gruikui"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 17", new EvolutionNode(perName.get("Grotichon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Roitiflam"), null));}}));}});
        p.catchRate = "45";
        p.weight = "150kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Sol";
        p.size = "1,6m";

        p = perName.get("Zygarde");
        p.evolutions = null;
        p.catchRate = "";
        p.weight = "305,0kg";
        p.hatch = "pas";
        p.gender = "Asexue";
        p.ev = "+3 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "5,0m";

        p = perName.get("Pikachu");
        p.evolutions = new EvolutionNode(perName.get("Pichu"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Pikachu"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get("Raichu"), null));}}));}});
        p.catchRate = "190";
        p.weight = "6,0kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol/Fee";
        p.size = "0,4m";

        p = perName.get("Zoroark");
        p.evolutions = new EvolutionNode(perName.get("Zorua"), new HashMap<String, EvolutionNode>(){{this.put("Niv 30", new EvolutionNode(perName.get("Zoroark"), null));}});
        p.catchRate = "45";
        p.weight = "81,1kg";
        p.hatch = "21 cycles - 5535 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "1,6m";

        p = perName.get("Mega-Mysdibule");
        p.evolutions = new EvolutionNode(perName.get("Mysdibule"), new HashMap<String, EvolutionNode>(){{this.put("Mysdibulite", new EvolutionNode(perName.get("Mega-Mysdibule"), null));}});
        p.catchRate = "";
        p.weight = "23,5kg";
        p.hatch = "";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,0m";

        p = perName.get("Nodulithe");
        p.evolutions = new EvolutionNode(perName.get("Nodulithe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Geolithe"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Gigalithe"), null));}}));}});
        p.catchRate = "255";
        p.weight = "18,0kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Mineral";
        p.size = "0,4m";

        p = perName.get("Rhinastoc");
        p.evolutions = new EvolutionNode(perName.get("Rhinocorne"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 42", new EvolutionNode(perName.get("Rhinoferos"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Protecteur", new EvolutionNode(perName.get("Rhinastoc"), null));}}));}});
        p.catchRate = "30";
        p.weight = "282,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Monstre/Sol";
        p.size = "2,4m";

        p = perName.get("Amonistar");
        p.evolutions = new EvolutionNode(perName.get("Amonita"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Amonistar"), null));}});
        p.catchRate = "45";
        p.weight = "35,0kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Eau 1/Eau 3";
        p.size = "1,0m";

        p = perName.get("Mega-Gardevoir");
        p.evolutions = new EvolutionNode(perName.get("Tarsal"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Kirlia"), new HashMap<String, EvolutionNode>(){{this.put("Male + Pierre Aube", new EvolutionNode(perName.get("Gallame"), null));this.put("Niveau 30", new EvolutionNode(perName.get("Gardevoir"), new HashMap<String, EvolutionNode>(){{this.put("Gardevoirite", new EvolutionNode(perName.get("Mega-Gardevoir"), null));}}));}}));}});
        p.catchRate = "";
        p.weight = "48,4kg";
        p.hatch = "";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,6m";

        p = perName.get("Rafflesia");
        p.evolutions = new EvolutionNode(perName.get("Mystherbe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 21", new EvolutionNode(perName.get("Ortide"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get("Rafflesia"), null));this.put("Avec une Pierresoleil", new EvolutionNode(perName.get("Joliflor"), null));}}));}});
        p.catchRate = "45";
        p.weight = "18,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Plante";
        p.size = "1,2m";

        p = perName.get("Mega-Brasegali");
        p.evolutions = new EvolutionNode(perName.get("Poussifeu"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Galifeu"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Brasegali"), new HashMap<String, EvolutionNode>(){{this.put("Brasegalite", new EvolutionNode(perName.get("Mega-Brasegali"), null));}}));}}));}});
        p.catchRate = "";
        p.weight = "52kg";
        p.hatch = "";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,9m";

        p = perName.get("Grainipiot");
        p.evolutions = new EvolutionNode(perName.get("Grainipiot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 14", new EvolutionNode(perName.get("Pifeuil"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get("Tengalice"), null));}}));}});
        p.catchRate = "255";
        p.weight = "4,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Sol/Plante";
        p.size = "0,5m";

        p = perName.get("Qwilfish");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "3,9kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Eau 2";
        p.size = "0,5m";

        p = perName.get("Cliticlic");
        p.evolutions = new EvolutionNode(perName.get("Tic"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 38", new EvolutionNode(perName.get("Clic"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 49", new EvolutionNode(perName.get("Cliticlic"), null));}}));}});
        p.catchRate = "30";
        p.weight = "81,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "Asexue";
        p.ev = "+3 Def.";
        p.eggGroup = "Mineral";
        p.size = "0,6m";

        p = perName.get("Latios");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "60,0kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "2,0m";

        p = perName.get("Groret");
        p.evolutions = new EvolutionNode(perName.get("Spoink"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Groret"), null));}});
        p.catchRate = "60";
        p.weight = "71,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Sol";
        p.size = "0,9m";

        p = perName.get("Cheniselle (Cape Plante)");
        p.evolutions = new EvolutionNode(perName.get("Cheniti"), new HashMap<String, EvolutionNode>(){{this.put("Si Male, Niveau 20", new EvolutionNode(perName.get("Papilord"), null));this.put("Si Femelle, Niveau 20", new EvolutionNode(perName.get("Cheniselle (Cape Plante)"), null));}});
        p.catchRate = "45";
        p.weight = "6,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Insecte";
        p.size = "0,5m";

        p = perName.get("Meganium");
        p.evolutions = new EvolutionNode(perName.get("Germignon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Macronium"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Meganium"), null));}}));}});
        p.catchRate = "45";
        p.weight = "100,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Def.; +2 Def. Spe";
        p.eggGroup = "Monstre/Plante";
        p.size = "1,8m";

        p = perName.get("Steelix");
        p.evolutions = new EvolutionNode(perName.get("Onix"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Peau Metal", new EvolutionNode(perName.get("Steelix"), null));}});
        p.catchRate = "25";
        p.weight = "400,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Mineral";
        p.size = "9,2m";

        p = perName.get("Crefollet");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "0,3kg";
        p.hatch = "79 cycles - 20480 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att. Spe; +1 Def. Spe; +1 Vit.";
        p.eggGroup = "Sans oeuf";
        p.size = "0,3m";

        p = perName.get("Electhor");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "52,6kg";
        p.hatch = "79 cycles - 20480 pas";
        p.gender = "Asexue";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "1,6m";

        p = perName.get("Phanpy");
        p.evolutions = new EvolutionNode(perName.get("Phanpy"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Donphan"), null));}});
        p.catchRate = "120";
        p.weight = "33,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Sol";
        p.size = "0,5m";

        p = perName.get("Crehelf");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "0,3kg";
        p.hatch = "79 cycles - 20480 pas";
        p.gender = "Asexue";
        p.ev = "+2 Def.; +1 Def. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "0,3m";

        p = perName.get("Ortide");
        p.evolutions = new EvolutionNode(perName.get("Mystherbe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 21", new EvolutionNode(perName.get("Ortide"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get("Rafflesia"), null));this.put("Avec une Pierresoleil", new EvolutionNode(perName.get("Joliflor"), null));}}));}});
        p.catchRate = "120";
        p.weight = "8,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Plante";
        p.size = "0,8m";

        p = perName.get("Metalosse");
        p.evolutions = new EvolutionNode(perName.get("Terhal"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Metang"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 45", new EvolutionNode(perName.get("Metalosse"), null));}}));}});
        p.catchRate = "3";
        p.weight = "550,0kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "Asexue";
        p.ev = "+3 Def.";
        p.eggGroup = "Mineral";
        p.size = "1,6m";

        p = perName.get("Azumarill");
        p.evolutions = new EvolutionNode(perName.get("Azurill"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Marill"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Azumarill"), null));}}));}});
        p.catchRate = "75";
        p.weight = "28,5kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 PV";
        p.eggGroup = "Eau 1/Fee";
        p.size = "0,8m";

        p = perName.get("Mega-Branette");
        p.evolutions = new EvolutionNode(perName.get("Polichombr"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Branette"), new HashMap<String, EvolutionNode>(){{this.put("Branettite", new EvolutionNode(perName.get("Mega-Branette"), null));}}));}});
        p.catchRate = "";
        p.weight = "13kg";
        p.hatch = "";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,2m";

        p = perName.get("Scorplane");
        p.evolutions = new EvolutionNode(perName.get("Scorplane"), new HashMap<String, EvolutionNode>(){{this.put("Gagne un niveau de nuit en tenant un Croc Rasoir", new EvolutionNode(perName.get("Scorvol"), null));}});
        p.catchRate = "60";
        p.weight = "64,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Insecte";
        p.size = "1,1m";

        p = perName.get("Joliflor");
        p.evolutions = new EvolutionNode(perName.get("Mystherbe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 21", new EvolutionNode(perName.get("Ortide"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get("Rafflesia"), null));this.put("Avec une Pierresoleil", new EvolutionNode(perName.get("Joliflor"), null));}}));}});
        p.catchRate = "45";
        p.weight = "5,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Def. Spe";
        p.eggGroup = "Plante";
        p.size = "0,4m";

        p = perName.get("Florizarre");
        p.evolutions = new EvolutionNode(perName.get("Bulbizarre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Herbizarre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Florizarre"), new HashMap<String, EvolutionNode>(){{this.put("Florizarrite", new EvolutionNode(perName.get("Mega-Florizarre"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "100,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att. Spe; +1 Def. Spe";
        p.eggGroup = "Monstre/Plante";
        p.size = "2,0m";

        p = perName.get("Elektek");
        p.evolutions = new EvolutionNode(perName.get("Elekid"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Elektek"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Electiriseur", new EvolutionNode(perName.get("Elekable"), null));}}));}});
        p.catchRate = "45";
        p.weight = "30,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Humanoide";
        p.size = "1,1m";

        p = perName.get("Voltorbe");
        p.evolutions = new EvolutionNode(perName.get("Voltorbe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Electrode"), null));}});
        p.catchRate = "190";
        p.weight = "10,4kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+1 Vit.";
        p.eggGroup = "Mineral";
        p.size = "0,5m";

        p = perName.get("Cradopaud");
        p.evolutions = new EvolutionNode(perName.get("Cradopaud"), new HashMap<String, EvolutionNode>(){{this.put("niveau 37", new EvolutionNode(perName.get("Coatox"), null));}});
        p.catchRate = "140";
        p.weight = "23,0kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Humanoide";
        p.size = "0,7m";

        p = perName.get("Leveinard");
        p.evolutions = new EvolutionNode(perName.get("Ptiravi"), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau en tenant une Pierre Ovale", new EvolutionNode(perName.get("Leveinard"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Leuphorie"), null));}}));}});
        p.catchRate = "30";
        p.weight = "34,6kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+2 PV";
        p.eggGroup = "Fee";
        p.size = "1,1m";

        p = perName.get("Ferosinge");
        p.evolutions = new EvolutionNode(perName.get("Ferosinge"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 28", new EvolutionNode(perName.get("Colossinge"), null));}});
        p.catchRate = "190";
        p.weight = "28,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol";
        p.size = "0,5m";

        p = perName.get("Simularbre");
        p.evolutions = new EvolutionNode(perName.get("Manzai"), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l'attaque Copie", new EvolutionNode(perName.get("Simularbre"), null));}});
        p.catchRate = "65";
        p.weight = "61,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Mineral";
        p.size = "1,4m";

        p = perName.get("Maracachi");
        p.evolutions = null;
        p.catchRate = "255";
        p.weight = "28,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Plante";
        p.size = "1,0m";

        p = perName.get("Sancoki");
        p.evolutions = new EvolutionNode(perName.get("Sancoki"), new HashMap<String, EvolutionNode>(){{this.put("niveau 30", new EvolutionNode(perName.get("Tritosor"), null));}});
        p.catchRate = "190";
        p.weight = "6,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Eau 1/Indetermine";
        p.size = "0,3m";

        p = perName.get("Dragmara");
        p.evolutions = new EvolutionNode(perName.get("Amagara"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 39 pendant la nuit", new EvolutionNode(perName.get("Dragmara"), null));}});
        p.catchRate = "45";
        p.weight = "225,0kg";
        p.hatch = "pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 PV";
        p.eggGroup = "Monstre";
        p.size = "2,7m";

        p = perName.get("Insecateur");
        p.evolutions = new EvolutionNode(perName.get("Insecateur"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Peau Metal", new EvolutionNode(perName.get("Cizayox"), new HashMap<String, EvolutionNode>(){{this.put("Mega-Evolution", new EvolutionNode(perName.get("Mega-Cizayox"), null));}}));}});
        p.catchRate = "45";
        p.weight = "56,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "Repartition inconnue";
        p.ev = "+1 Att.";
        p.eggGroup = "Insecte";
        p.size = "1,5m";

        p = perName.get("Laporeille");
        p.evolutions = new EvolutionNode(perName.get("Laporeille"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Lockpin"), null));}});
        p.catchRate = "190";
        p.weight = "5,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol/Humanoide";
        p.size = "0,4m";

        p = perName.get("Hoot-hoot");
        p.evolutions = new EvolutionNode(perName.get("Hoot-hoot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Noarfang"), null));}});
        p.catchRate = "255";
        p.weight = "21,2kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Vol";
        p.size = "0,7m";

        p = perName.get("Lokhlass");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "220,0kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Monstre/Eau 1";
        p.size = "2,5m";

        p = perName.get("Spiritomb");
        p.evolutions = null;
        p.catchRate = "100";
        p.weight = "108kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Indetermine";
        p.size = "1,0m";

        p = perName.get("Limagma");
        p.evolutions = new EvolutionNode(perName.get("Limagma"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 38", new EvolutionNode(perName.get("Volcaropod"), null));}});
        p.catchRate = "190";
        p.weight = "35,0kg";
        p.hatch = "21 cycles - 5610 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Indetermine";
        p.size = "0,7m";

        p = perName.get("Paras");
        p.evolutions = new EvolutionNode(perName.get("Paras"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 24", new EvolutionNode(perName.get("Parasect"), null));}});
        p.catchRate = "190";
        p.weight = "5,4kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Insecte/Plante";
        p.size = "0,3m";

        p = perName.get("Pyronille");
        p.evolutions = new EvolutionNode(perName.get("Pyronille"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 59", new EvolutionNode(perName.get("Pyrax"), null));}});
        p.catchRate = "45";
        p.weight = "28,8kg";
        p.hatch = "40 cycles - 10455 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Insecte";
        p.size = "1,1m";

        p = perName.get("Grotadmorv");
        p.evolutions = new EvolutionNode(perName.get("Tadmorv"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 38", new EvolutionNode(perName.get("Grotadmorv"), null));}});
        p.catchRate = "75";
        p.weight = "30,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV; +1 Att.";
        p.eggGroup = "Indetermine";
        p.size = "1,2m";

        p = perName.get("Melo");
        p.evolutions = new EvolutionNode(perName.get("Melo"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Melofee"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get("Melodelfe"), null));}}));}});
        p.catchRate = "150";
        p.weight = "3,0kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "0,3m";

        p = perName.get("Lianaja");
        p.evolutions = new EvolutionNode(perName.get("Vipelierre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 17", new EvolutionNode(perName.get("Lianaja"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Majaspic"), null));}}));}});
        p.catchRate = "45";
        p.weight = "16kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol/Plante";
        p.size = "0,8m";

        p = perName.get("Arcko");
        p.evolutions = new EvolutionNode(perName.get("Arcko"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Massko"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Jungko"), null));}}));}});
        p.catchRate = "45";
        p.weight = "5,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Monstre/Dragon";
        p.size = "0,5m";

        p = perName.get("Archeomire");
        p.evolutions = new EvolutionNode(perName.get("Archeomire"), new HashMap<String, EvolutionNode>(){{this.put("niveau 33", new EvolutionNode(perName.get("Archeodong"), null));}});
        p.catchRate = "255";
        p.weight = "60,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+1 Def.";
        p.eggGroup = "Mineral";
        p.size = "0,5m";

        p = perName.get("Hippopotas");
        p.evolutions = new EvolutionNode(perName.get("Hippopotas"), new HashMap<String, EvolutionNode>(){{this.put("niveau 34", new EvolutionNode(perName.get("Hippodocus"), null));}});
        p.catchRate = "140";
        p.weight = "49,5kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Sol";
        p.size = "0,8m";

        p = perName.get("Feuforeve");
        p.evolutions = new EvolutionNode(perName.get("Feuforeve"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get("Magireve"), null));}});
        p.catchRate = "45";
        p.weight = "1,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe; +1 Def. Spe";
        p.eggGroup = "Indetermine";
        p.size = "0,7m";

        p = perName.get("Yveltal");
        p.evolutions = null;
        p.catchRate = "30";
        p.weight = "203,0kg";
        p.hatch = "pas";
        p.gender = "Asexue";
        p.ev = "+3 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "5,8m";

        p = perName.get("Neitram");
        p.evolutions = new EvolutionNode(perName.get("Lewsor"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 42", new EvolutionNode(perName.get("Neitram"), null));}});
        p.catchRate = "90";
        p.weight = "34,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Humanoide";
        p.size = "1,0m";

        p = perName.get("Psystigri");
        p.evolutions = new EvolutionNode(perName.get("Psystigri"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Mistigrix"), null));}});
        p.catchRate = "";
        p.weight = "3,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,3m";

        p = perName.get("Tropius");
        p.evolutions = null;
        p.catchRate = "200";
        p.weight = "100,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Monstre/Plante";
        p.size = "2,0m";

        p = perName.get("Doudouvet");
        p.evolutions = new EvolutionNode(perName.get("Doudouvet"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierresoleil", new EvolutionNode(perName.get("Farfaduvet"), null));}});
        p.catchRate = "190";
        p.weight = "0,6kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Plante/Fee";
        p.size = "0,3m";

        p = perName.get("Lamantine");
        p.evolutions = new EvolutionNode(perName.get("Otaria"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 34", new EvolutionNode(perName.get("Lamantine"), null));}});
        p.catchRate = "75";
        p.weight = "120,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Eau 1/Sol";
        p.size = "1,7m";

        p = perName.get("Parasect");
        p.evolutions = new EvolutionNode(perName.get("Paras"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 24", new EvolutionNode(perName.get("Parasect"), null));}});
        p.catchRate = "75";
        p.weight = "29,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.; +1 Def.";
        p.eggGroup = "Insecte/Plante";
        p.size = "1,0m";

        p = perName.get("Avaltout");
        p.evolutions = new EvolutionNode(perName.get("Gloupti"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 26", new EvolutionNode(perName.get("Avaltout"), null));}});
        p.catchRate = "75";
        p.weight = "80,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Indetermine";
        p.size = "1,7m";

        p = perName.get("Funecire");
        p.evolutions = new EvolutionNode(perName.get("Funecire"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 41", new EvolutionNode(perName.get("Melancolux"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get("Lugulabre"), null));}}));}});
        p.catchRate = "190";
        p.weight = "3,1kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Indetermine";
        p.size = "0,3m";

        p = perName.get("Magicarpe");
        p.evolutions = new EvolutionNode(perName.get("Magicarpe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Leviator"), new HashMap<String, EvolutionNode>(){{this.put("Leviatorite", new EvolutionNode(perName.get("Mega-Leviator"), null));}}));}});
        p.catchRate = "255";
        p.weight = "10,0kg";
        p.hatch = "4 cycles - 1280 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Eau 2/Dragon";
        p.size = "0,9m";

        p = perName.get("Stari");
        p.evolutions = new EvolutionNode(perName.get("Stari"), new HashMap<String, EvolutionNode>(){{this.put("Pierre Eau", new EvolutionNode(perName.get("Staross"), null));}});
        p.catchRate = "225";
        p.weight = "34,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+1 Vit.";
        p.eggGroup = "Eau 3";
        p.size = "0,8m";

        p = perName.get("Heledelle");
        p.evolutions = new EvolutionNode(perName.get("Nirondelle"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 22", new EvolutionNode(perName.get("Heledelle"), null));}});
        p.catchRate = "45";
        p.weight = "19,8kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Vol";
        p.size = "0,7m";

        p = perName.get("Noacier");
        p.evolutions = new EvolutionNode(perName.get("Grindur"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Noacier"), null));}});
        p.catchRate = "90";
        p.weight = "110kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Plante/Mineral";
        p.size = "1,0m";

        p = perName.get("Laggron");
        p.evolutions = new EvolutionNode(perName.get("Gobou"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Flobio"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Laggron"), null));}}));}});
        p.catchRate = "45";
        p.weight = "81,9kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Monstre/Eau 1";
        p.size = "1,6m";

        p = perName.get("Gobou");
        p.evolutions = new EvolutionNode(perName.get("Gobou"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Flobio"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Laggron"), null));}}));}});
        p.catchRate = "45";
        p.weight = "7,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Monstre/Eau 1";
        p.size = "0,4m";

        p = perName.get("Canarticho");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "15,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Vol/Sol";
        p.size = "0,8m";

        p = perName.get("Groudon");
        p.evolutions = null;
        p.catchRate = "5";
        p.weight = "950,0kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 Att.";
        p.eggGroup = "Sans oeuf";
        p.size = "3,5m";

        p = perName.get("Rapion");
        p.evolutions = new EvolutionNode(perName.get("Rapion"), new HashMap<String, EvolutionNode>(){{this.put("niveau 40", new EvolutionNode(perName.get("Drascore"), null));}});
        p.catchRate = "120";
        p.weight = "12,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Insecte/Eau 3";
        p.size = "0,8m";

        p = perName.get("Tournegrin");
        p.evolutions = new EvolutionNode(perName.get("Tournegrin"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierresoleil", new EvolutionNode(perName.get("Heliatronc"), null));}});
        p.catchRate = "235";
        p.weight = "1,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Plante";
        p.size = "0,3m";

        p = perName.get("Nidoqueen");
        p.evolutions = new EvolutionNode(perName.get("Nidoran F"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Nidorina"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get("Nidoqueen"), null));}}));}});
        p.catchRate = "45";
        p.weight = "60,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+3 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "1,3m";

        p = perName.get("Altaria");
        p.evolutions = new EvolutionNode(perName.get("Tylton"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Altaria"), null));}});
        p.catchRate = "45";
        p.weight = "20,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Vol/Dragon";
        p.size = "1,1m";

        p = perName.get("Roucool");
        p.evolutions = new EvolutionNode(perName.get("Roucool"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Roucoups"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Roucarnage"), null));}}));}});
        p.catchRate = "255";
        p.weight = "1,8kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Vol";
        p.size = "0,3m";

        p = perName.get("Ratentif");
        p.evolutions = new EvolutionNode(perName.get("Ratentif"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Miradar"), null));}});
        p.catchRate = "255";
        p.weight = "11,6kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol";
        p.size = "0,5m";

        p = perName.get("Malosse");
        p.evolutions = new EvolutionNode(perName.get("Malosse"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 24", new EvolutionNode(perName.get("Demolosse"), new HashMap<String, EvolutionNode>(){{this.put("Demolossite", new EvolutionNode(perName.get("Mega-Demolosse"), null));}}));}});
        p.catchRate = "120";
        p.weight = "10,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "0,6m";

        p = perName.get("Vaututrice");
        p.evolutions = new EvolutionNode(perName.get("Vostourno"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 54", new EvolutionNode(perName.get("Vaututrice"), null));}});
        p.catchRate = "60";
        p.weight = "39,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Vol";
        p.size = "1,2m";

        p = perName.get("Togekiss");
        p.evolutions = new EvolutionNode(perName.get("Togepi"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Togetic"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get("Togekiss"), null));}}));}});
        p.catchRate = "30";
        p.weight = "38,0kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att. Spe; +1 Def. Spe";
        p.eggGroup = "Vol/Fee";
        p.size = "1,5m";

        p = perName.get("Tritonde");
        p.evolutions = new EvolutionNode(perName.get("Tritonde"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Batracne"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Crapustule"), null));}}));}});
        p.catchRate = "255";
        p.weight = "4,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Eau 1";
        p.size = "0,5m";

        p = perName.get("Moufflair");
        p.evolutions = new EvolutionNode(perName.get("Moufouette"), new HashMap<String, EvolutionNode>(){{this.put("niveau 34", new EvolutionNode(perName.get("Moufflair"), null));}});
        p.catchRate = "60";
        p.weight = "38,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Tiplouf");
        p.evolutions = new EvolutionNode(perName.get("Tiplouf"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Prinplouf"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Pingoleon"), null));}}));}});
        p.catchRate = "45";
        p.weight = "5,2kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Eau 1/Sol";
        p.size = "0,4m";

        p = perName.get("Lumivole");
        p.evolutions = null;
        p.catchRate = "150";
        p.weight = "17,7kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Insecte/Humanoide";
        p.size = "0,6m";

        p = perName.get("Carmache");
        p.evolutions = new EvolutionNode(perName.get("Griknot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 24", new EvolutionNode(perName.get("Carmache"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 48", new EvolutionNode(perName.get("Carchacrok"), new HashMap<String, EvolutionNode>(){{this.put("Carchacrokite", new EvolutionNode(perName.get("Mega-Carchacrok"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "56,0kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Dragon/Monstre";
        p.size = "1,4m";

        p = perName.get("Carchacrok");
        p.evolutions = new EvolutionNode(perName.get("Griknot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 24", new EvolutionNode(perName.get("Carmache"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 48", new EvolutionNode(perName.get("Carchacrok"), new HashMap<String, EvolutionNode>(){{this.put("Carchacrokite", new EvolutionNode(perName.get("Mega-Carchacrok"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "95,0kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Dragon/Monstre";
        p.size = "1,9m";

        p = perName.get("Charkos");
        p.evolutions = new EvolutionNode(perName.get("Kranidos"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Charkos"), null));}});
        p.catchRate = "45";
        p.weight = "102,5kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Monstre";
        p.size = "1,6m";

        p = perName.get("Poussifeu");
        p.evolutions = new EvolutionNode(perName.get("Poussifeu"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Galifeu"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Brasegali"), new HashMap<String, EvolutionNode>(){{this.put("Brasegalite", new EvolutionNode(perName.get("Mega-Brasegali"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "2,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "0,4m";

        p = perName.get("Limaspeed");
        p.evolutions = new EvolutionNode(perName.get("Escargaume"), new HashMap<String, EvolutionNode>(){{this.put("Echange avec Carabing", new EvolutionNode(perName.get("Limaspeed"), null));}});
        p.catchRate = "75";
        p.weight = "23,5kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Insecte";
        p.size = "0,8m";

        p = perName.get("Iguolta");
        p.evolutions = new EvolutionNode(perName.get("Galvaran"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierresoleil", new EvolutionNode(perName.get("Iguolta"), null));}});
        p.catchRate = "";
        p.weight = "21,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Monstre/Dragon";
        p.size = "1,0m";

        p = perName.get("Cheniti");
        p.evolutions = new EvolutionNode(perName.get("Cheniti"), new HashMap<String, EvolutionNode>(){{this.put("Si Male, Niveau 20", new EvolutionNode(perName.get("Papilord"), null));this.put("Si Femelle, Niveau 20", new EvolutionNode(perName.get("Cheniselle (Cape Plante)"), null));}});
        p.catchRate = "120";
        p.weight = "3,4kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Insecte";
        p.size = "0,2m";

        p = perName.get("Kapoera");
        p.evolutions = new EvolutionNode(perName.get("Debugant"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20, Attaque Defense", new EvolutionNode(perName.get("Tygnon"), null));this.put("Niveau 20, Attaque et Defense identiques", new EvolutionNode(perName.get("Kapoera"), null));}});
        p.catchRate = "45";
        p.weight = "48,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Humanoide";
        p.size = "1,4m";

        p = perName.get("Darumacho (Mode Daruma)");
        p.evolutions = new EvolutionNode(perName.get("Darumarond"), null);
        p.catchRate = "60";
        p.weight = "92,9kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att";
        p.eggGroup = "Sol";
        p.size = "1,3m";

        p = perName.get("Marill");
        p.evolutions = new EvolutionNode(perName.get("Azurill"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Marill"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Azumarill"), null));}}));}});
        p.catchRate = "190";
        p.weight = "8,5kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Eau 1/Fee";
        p.size = "0,4m";

        p = perName.get("Mega-Lucario");
        p.evolutions = new EvolutionNode(perName.get("Riolu"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur + gagne un niveau de jour", new EvolutionNode(perName.get("Lucario"), new HashMap<String, EvolutionNode>(){{this.put("Lucarite", new EvolutionNode(perName.get("Mega-Lucario"), null));}}));}});
        p.catchRate = "";
        p.weight = "57,5kg";
        p.hatch = "";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,5m";

        p = perName.get("Skitty");
        p.evolutions = new EvolutionNode(perName.get("Skitty"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get("Delcatty"), null));}});
        p.catchRate = "255";
        p.weight = "11,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol/Fee";
        p.size = "0,6m";

        p = perName.get("Abra");
        p.evolutions = new EvolutionNode(perName.get("Abra"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Kadabra"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Alakazam"), new HashMap<String, EvolutionNode>(){{this.put("Alakazamite", new EvolutionNode(perName.get("Mega-Alakazam"), null));}}));}}));}});
        p.catchRate = "200";
        p.weight = "19,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Humanoide";
        p.size = "0,9m";

        p = perName.get("Couverdure");
        p.evolutions = new EvolutionNode(perName.get("Larveyette"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Couverdure"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Manternel"), null));}}));}});
        p.catchRate = "120";
        p.weight = "7,3kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Insecte";
        p.size = "0,5m";

        p = perName.get("Grodoudou");
        p.evolutions = new EvolutionNode(perName.get("Toudoudou"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Rondoudou"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get("Grodoudou"), null));}}));}});
        p.catchRate = "50";
        p.weight = "12,0kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+3 PV";
        p.eggGroup = "Fee";
        p.size = "1,0m";

        p = perName.get("Ptyranidur");
        p.evolutions = new EvolutionNode(perName.get("Ptyranidur"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 39 pendant la journee", new EvolutionNode(perName.get("Rexillius"), null));}});
        p.catchRate = "";
        p.weight = "26,0kg";
        p.hatch = "pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att.";
        p.eggGroup = "";
        p.size = "0,8m";

        p = perName.get("Kecleon");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "22,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Deoxys (Forme Vitesse)");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "60,8kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att.; +1 Att. Spe; +1 Vit.";
        p.eggGroup = "Sans oeuf";
        p.size = "1,7m";

        p = perName.get("Crustabri");
        p.evolutions = new EvolutionNode(perName.get("Kokiyas"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Crustabri"), null));}});
        p.catchRate = "60";
        p.weight = "132,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Eau 3";
        p.size = "1,5m";

        p = perName.get("Motisma (Forme Chaleur)");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "0,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att. Spe; +1 Vit.";
        p.eggGroup = "Indetermine";
        p.size = "0,3m";

        p = perName.get("Deoxys (Forme de Base)");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "60,8kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att.; +1 Att. Spe; +1 Vit.";
        p.eggGroup = "Sans oeuf";
        p.size = "1,7m";

        p = perName.get("Fluvetin");
        p.evolutions = new EvolutionNode(perName.get("Fluvetin"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Sachet Senteur", new EvolutionNode(perName.get("Cocotine"), null));}});
        p.catchRate = "";
        p.weight = "0,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Fee";
        p.size = "0,2m";

        p = perName.get("Haydaim");
        p.evolutions = new EvolutionNode(perName.get("Vivaldaim"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 34", new EvolutionNode(perName.get("Haydaim"), null));}});
        p.catchRate = "75";
        p.weight = "92,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol";
        p.size = "1,9m";

        p = perName.get("Kyurem (Noir)");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "325kg";
        p.hatch = "120 cycles - 30855 pas";
        p.gender = "Asexue";
        p.ev = "+1 PV; +1 Att.; +1 Def. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "3,0m";

        p = perName.get("Chenipotte");
        p.evolutions = new EvolutionNode(perName.get("Chenipotte"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 10", new EvolutionNode(perName.get("Papinox"), null));this.put("Niveau 7, au hasard", new EvolutionNode(perName.get("Blindalys"), null));}});
        p.catchRate = "255";
        p.weight = "3,6kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Insecte";
        p.size = "0,3m";

        p = perName.get("Coconfort");
        p.evolutions = new EvolutionNode(perName.get("Aspicot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 7", new EvolutionNode(perName.get("Coconfort"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 10", new EvolutionNode(perName.get("Dardargnan"), null));}}));}});
        p.catchRate = "120";
        p.weight = "10,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Insecte";
        p.size = "0,6m";

        p = perName.get("Motisma (Forme Froid)");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "0,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att. Spe; +1 Vit.";
        p.eggGroup = "Indetermine";
        p.size = "0,3m";

        p = perName.get("Noctunoir");
        p.evolutions = new EvolutionNode(perName.get("Skelenox"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Teraclope"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Tissu Fauche", new EvolutionNode(perName.get("Noctunoir"), null));}}));}});
        p.catchRate = "45";
        p.weight = "106,6kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Indetermine";
        p.size = "2,2m";

        p = perName.get("Rattata");
        p.evolutions = new EvolutionNode(perName.get("Rattata"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Rattatac"), null));}});
        p.catchRate = "255";
        p.weight = "3,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,3m";

        p = perName.get("Girafarig");
        p.evolutions = null;
        p.catchRate = "60";
        p.weight = "41,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "1,5m";

        p = perName.get("Otaria");
        p.evolutions = new EvolutionNode(perName.get("Otaria"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 34", new EvolutionNode(perName.get("Lamantine"), null));}});
        p.catchRate = "190";
        p.weight = "90,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Eau 1/Sol";
        p.size = "1,1m";

        p = perName.get("Granbull");
        p.evolutions = new EvolutionNode(perName.get("Snubbull"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 23", new EvolutionNode(perName.get("Granbull"), null));}});
        p.catchRate = "75";
        p.weight = "48,7kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol/Fee";
        p.size = "1,4m";

        p = perName.get("Kabutops");
        p.evolutions = new EvolutionNode(perName.get("Kabuto"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Kabutops"), null));}});
        p.catchRate = "45";
        p.weight = "40,5kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Eau 1/Eau 3";
        p.size = "1,3m";

        p = perName.get("Cheniselle (Cape Sol)");
        p.evolutions = new EvolutionNode(perName.get("Cheniti"), new HashMap<String, EvolutionNode>(){{this.put("Si Male, Niveau 20", new EvolutionNode(perName.get("Papilord"), null));this.put("Si Femelle, Niveau 20", new EvolutionNode(perName.get("Cheniselle (Cape Sol)"), null));}});
        p.catchRate = "45";
        p.weight = "6,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Insecte";
        p.size = "0,5m";

        p = perName.get("Bulbizarre");
        p.evolutions = new EvolutionNode(perName.get("Bulbizarre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Herbizarre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Florizarre"), new HashMap<String, EvolutionNode>(){{this.put("Florizarrite", new EvolutionNode(perName.get("Mega-Florizarre"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "6,9kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Monstre/Plante";
        p.size = "0,7m";

        p = perName.get("Couafarel");
        p.evolutions = null;
        p.catchRate = "";
        p.weight = "28,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Sol/Humanoide";
        p.size = "1,2m";

        p = perName.get("Siderella");
        p.evolutions = new EvolutionNode(perName.get("Scrutella"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Mesmerella"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 41", new EvolutionNode(perName.get("Siderella"), null));}}));}});
        p.catchRate = "50";
        p.weight = "44kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+3 Att. Spe.";
        p.eggGroup = "Humanoide";
        p.size = "1,5m";

        p = perName.get("Dedenne");
        p.evolutions = null;
        p.catchRate = "";
        p.weight = "2,2kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol/Fee";
        p.size = "0,2m";

        p = perName.get("Chaglam");
        p.evolutions = new EvolutionNode(perName.get("Chaglam"), new HashMap<String, EvolutionNode>(){{this.put("niveau 38", new EvolutionNode(perName.get("Chaffreux"), null));}});
        p.catchRate = "190";
        p.weight = "3,9kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,75m";

        p = perName.get("Lixy");
        p.evolutions = new EvolutionNode(perName.get("Lixy"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 15", new EvolutionNode(perName.get("Luxio"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Luxray"), null));}}));}});
        p.catchRate = "235";
        p.weight = "9,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol";
        p.size = "0,5m";

        p = perName.get("Roucarnage");
        p.evolutions = new EvolutionNode(perName.get("Roucool"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Roucoups"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Roucarnage"), null));}}));}});
        p.catchRate = "45";
        p.weight = "39,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Vit.";
        p.eggGroup = "Vol";
        p.size = "1,5m";

        p = perName.get("Tarinor");
        p.evolutions = new EvolutionNode(perName.get("Tarinor"), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau dans un lieu indique", new EvolutionNode(perName.get("Tarinorme"), null));}});
        p.catchRate = "255";
        p.weight = "97,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Mineral";
        p.size = "1,0m";

        p = perName.get("Rapasdepic");
        p.evolutions = new EvolutionNode(perName.get("Piafabec"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Rapasdepic"), null));}});
        p.catchRate = "90";
        p.weight = "38,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Vol";
        p.size = "1,2m";

        p = perName.get("Embrylex");
        p.evolutions = new EvolutionNode(perName.get("Embrylex"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Ymphect"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 55", new EvolutionNode(perName.get("Tyranocif"), new HashMap<String, EvolutionNode>(){{this.put("Tyranocivite", new EvolutionNode(perName.get("Mega-Tyranocif"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "72,0kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Monstre";
        p.size = "0,6m";

        p = perName.get("Togetic");
        p.evolutions = new EvolutionNode(perName.get("Togepi"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Togetic"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get("Togekiss"), null));}}));}});
        p.catchRate = "75";
        p.weight = "3,2kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Vol/Fee";
        p.size = "0,6m";

        p = perName.get("Roselia");
        p.evolutions = new EvolutionNode(perName.get("Rozbouton"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur , Jour", new EvolutionNode(perName.get("Roselia"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get("Roserade"), null));}}));}});
        p.catchRate = "150";
        p.weight = "2,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Fee/Plante";
        p.size = "0,3m";

        p = perName.get("Brouhabam");
        p.evolutions = new EvolutionNode(perName.get("Chuchmur"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Ramboum"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Brouhabam"), null));}}));}});
        p.catchRate = "45";
        p.weight = "84,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "45% femelle; 55% male";
        p.ev = "+3 PV";
        p.eggGroup = "Monstre/Sol";
        p.size = "1,5m";

        p = perName.get("Babimanta");
        p.evolutions = new EvolutionNode(perName.get("Babimanta"), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau avec Remoraid dans l'equipe", new EvolutionNode(perName.get("Demanta"), null));}});
        p.catchRate = "25";
        p.weight = "65,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sans oeuf";
        p.size = "1,0m";

        p = perName.get("Rhinolove");
        p.evolutions = new EvolutionNode(perName.get("Chovsourir"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Rhinolove"), null));}});
        p.catchRate = "45";
        p.weight = "10,5kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol/Vol";
        p.size = "0,9m";

        p = perName.get("Vigoroth");
        p.evolutions = new EvolutionNode(perName.get("Parecool"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Vigoroth"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Monaflemit"), null));}}));}});
        p.catchRate = "120";
        p.weight = "46,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "1,4m";

        p = perName.get("Clamiral");
        p.evolutions = new EvolutionNode(perName.get("Moustillon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 17", new EvolutionNode(perName.get("Mateloutre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Clamiral"), null));}}));}});
        p.catchRate = "45";
        p.weight = "94,6kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+3 Att. Spe.";
        p.eggGroup = "Sol";
        p.size = "1,5m";

        p = perName.get("Ronflex");
        p.evolutions = new EvolutionNode(perName.get("Goinfrex"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Ronflex"), null));}});
        p.catchRate = "25";
        p.weight = "460,0kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 PV";
        p.eggGroup = "Monstre";
        p.size = "2,1m";

        p = perName.get("Kyurem (Blanc)");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "325kg";
        p.hatch = "120 cycles - 30855 pas";
        p.gender = "Asexue";
        p.ev = "+1 PV; +1 Att.; +1 Def. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "3,0m";

        p = perName.get("Symbios");
        p.evolutions = new EvolutionNode(perName.get("Nucleos"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Meios"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 41", new EvolutionNode(perName.get("Symbios"), null));}}));}});
        p.catchRate = "50";
        p.weight = "20,1kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Indetermine";
        p.size = "1,0m";

        p = perName.get("Polagriffe");
        p.evolutions = new EvolutionNode(perName.get("Polarhume"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Polagriffe"), null));}});
        p.catchRate = "60";
        p.weight = "260,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol";
        p.size = "2,6m";

        p = perName.get("Mentali");
        p.evolutions = new EvolutionNode(perName.get("Evoli"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get("Voltali"), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get("Phyllali"), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get("Mentali"), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get("Nymphali"), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Aquali"), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get("Givrali"), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get("Pyroli"), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get("Noctali"), null));}});
        p.catchRate = "45";
        p.weight = "26,5kg";
        p.hatch = "34 cycles - 8960 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "0,9m";

        p = perName.get("Betochef");
        p.evolutions = new EvolutionNode(perName.get("Charpenti"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Ouvrifier"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Betochef"), null));}}));}});
        p.catchRate = "45";
        p.weight = "87,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Humanoide";
        p.size = "1,4m";

        p = perName.get("Darumacho (Mode Normal)");
        p.evolutions = new EvolutionNode(perName.get("Darumarond"), null);
        p.catchRate = "60";
        p.weight = "92,9kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att";
        p.eggGroup = "Sol";
        p.size = "1,3m";

        p = perName.get("Arkeapti");
        p.evolutions = new EvolutionNode(perName.get("Arkeapti"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Aeropteryx"), null));}});
        p.catchRate = "45";
        p.weight = "9,5kg";
        p.hatch = "30 cycles - 7905 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Vol";
        p.size = "0,6m";

        p = perName.get("Crocorible");
        p.evolutions = new EvolutionNode(perName.get("Mascaiman"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 29", new EvolutionNode(perName.get("Escroco"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Crocorible"), null));}}));}});
        p.catchRate = "45";
        p.weight = "96,3kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Sol";
        p.size = "1,5m";

        p = perName.get("Heatran");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "430,0kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "1,7m";

        p = perName.get("Ponyta");
        p.evolutions = new EvolutionNode(perName.get("Ponyta"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Galopa"), null));}});
        p.catchRate = "190";
        p.weight = "30,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Crefadet");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "0,3kg";
        p.hatch = "79 cycles - 20480 pas";
        p.gender = "Asexue";
        p.ev = "+2 Att.; +1 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "0,3m";

        p = perName.get("Giratina (Forme Alternative)");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "750kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "4,5m";

        p = perName.get("Hariyama");
        p.evolutions = new EvolutionNode(perName.get("Makuhita"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 24", new EvolutionNode(perName.get("Hariyama"), null));}});
        p.catchRate = "200";
        p.weight = "253,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+2 PV";
        p.eggGroup = "Humanoide";
        p.size = "2,3m";

        p = perName.get("Qulbutoke");
        p.evolutions = new EvolutionNode(perName.get("Okeoke"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 15", new EvolutionNode(perName.get("Qulbutoke"), null));}});
        p.catchRate = "45";
        p.weight = "28,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Indetermine";
        p.size = "1,3m";

        p = perName.get("Staross");
        p.evolutions = new EvolutionNode(perName.get("Stari"), new HashMap<String, EvolutionNode>(){{this.put("Pierre Eau", new EvolutionNode(perName.get("Staross"), null));}});
        p.catchRate = "60";
        p.weight = "80,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+2 Vit.";
        p.eggGroup = "Eau 3";
        p.size = "1,1m";

        p = perName.get("Hexagel");
        p.evolutions = null;
        p.catchRate = "25";
        p.weight = "148,0kg";
        p.hatch = "25 cycles - 6630 pas";
        p.gender = "Asexue";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Mineral";
        p.size = "1,1m";

        p = perName.get("Lippouti");
        p.evolutions = new EvolutionNode(perName.get("Lippouti"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Lippoutou"), null));}});
        p.catchRate = "45";
        p.weight = "6,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "0,6m";

        p = perName.get("Colimucus");
        p.evolutions = new EvolutionNode(perName.get("Mucuscule"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Colimucus"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 50, quand il pleut", new EvolutionNode(perName.get("Muplodocus"), null));}}));}});
        p.catchRate = "";
        p.weight = "17,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Dragon";
        p.size = "0,8m";

        p = perName.get("Bastiodon");
        p.evolutions = new EvolutionNode(perName.get("Dinoclier"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Bastiodon"), null));}});
        p.catchRate = "45";
        p.weight = "149,5kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Monstre";
        p.size = "1,3m";

        p = perName.get("Peregrain");
        p.evolutions = new EvolutionNode(perName.get("Lepidonille"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 9", new EvolutionNode(perName.get("Peregrain"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 12", new EvolutionNode(perName.get("Prismillon"), null));}}));}});
        p.catchRate = "";
        p.weight = "8,4kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Insecte";
        p.size = "0,3m";

        p = perName.get("Motisma (Forme Lavage)");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "0,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att. Spe; +1 Vit.";
        p.eggGroup = "Indetermine";
        p.size = "0,3m";

        p = perName.get("Baggaid");
        p.evolutions = new EvolutionNode(perName.get("Baggiguane"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 39", new EvolutionNode(perName.get("Baggaid"), null));}});
        p.catchRate = "90";
        p.weight = "30,0kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Sol/Dragon";
        p.size = "1,1m";

        p = perName.get("Mega-Charmina");
        p.evolutions = new EvolutionNode(perName.get("Meditikka"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Charmina"), new HashMap<String, EvolutionNode>(){{this.put("Charminite", new EvolutionNode(perName.get("Mega-Charmina"), null));}}));}});
        p.catchRate = "";
        p.weight = "31,5kg";
        p.hatch = "";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,3m";

        p = perName.get("Bouldeneu");
        p.evolutions = new EvolutionNode(perName.get("Saquedeneu"), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l'attaque Pouv.Antique", new EvolutionNode(perName.get("Bouldeneu"), null));}});
        p.catchRate = "30";
        p.weight = "128,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Plante";
        p.size = "2,0m";

        p = perName.get("Jirachi");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "1,1kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "0,3m";

        p = perName.get("Gamblast");
        p.evolutions = new EvolutionNode(perName.get("Flingouste"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Gamblast"), null));}});
        p.catchRate = "";
        p.weight = "35,3kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Eau 1/Eau 3";
        p.size = "1,3m";

        p = perName.get("Eoko");
        p.evolutions = new EvolutionNode(perName.get("Korillon"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur , Nuit", new EvolutionNode(perName.get("Eoko"), null));}});
        p.catchRate = "45";
        p.weight = "1,0kg";
        p.hatch = "25 cycles - 6655 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe; +1 Def. Spe";
        p.eggGroup = "Indetermine";
        p.size = "0,6m";

        p = perName.get("Brutalibre");
        p.evolutions = null;
        p.catchRate = "";
        p.weight = "21,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Humanoide";
        p.size = "0,8m";

        p = perName.get("Furaiglon");
        p.evolutions = new EvolutionNode(perName.get("Furaiglon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 54", new EvolutionNode(perName.get("Gueriaigle"), null));}});
        p.catchRate = "190";
        p.weight = "10,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Vol";
        p.size = "0,5m";

        p = perName.get("Chevroum");
        p.evolutions = new EvolutionNode(perName.get("Cabriolaine"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Chevroum"), null));}});
        p.catchRate = "";
        p.weight = "91,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Sol";
        p.size = "1,7m";

        p = perName.get("Flamoutan");
        p.evolutions = new EvolutionNode(perName.get("Flamajou"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Feu", new EvolutionNode(perName.get("Flamoutan"), null));}});
        p.catchRate = "75";
        p.weight = "28,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Prismillon");
        p.evolutions = new EvolutionNode(perName.get("Lepidonille"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 9", new EvolutionNode(perName.get("Peregrain"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 12", new EvolutionNode(perName.get("Prismillon"), null));}}));}});
        p.catchRate = "";
        p.weight = "17,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 PV.; +1 Att. Spe; +1 Vit.";
        p.eggGroup = "";
        p.size = "1,2m";

        p = perName.get("Sonistrelle");
        p.evolutions = new EvolutionNode(perName.get("Sonistrelle"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 48", new EvolutionNode(perName.get("Bruyverne"), null));}});
        p.catchRate = "";
        p.weight = "8,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Vol";
        p.size = "0,5m";

        p = perName.get("Goupix");
        p.evolutions = new EvolutionNode(perName.get("Goupix"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Feu", new EvolutionNode(perName.get("Feunard"), null));}});
        p.catchRate = "190";
        p.weight = "9,9kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,6m";

        p = perName.get("Gravalanch");
        p.evolutions = new EvolutionNode(perName.get("Racaillou"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Gravalanch"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Grolem"), null));}}));}});
        p.catchRate = "120";
        p.weight = "105,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Mineral";
        p.size = "1,0m";

        p = perName.get("Nostenfer");
        p.evolutions = new EvolutionNode(perName.get("Nosferapti"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 22", new EvolutionNode(perName.get("Nosferalto"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Nostenfer"), null));}}));}});
        p.catchRate = "90";
        p.weight = "75,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Vit.";
        p.eggGroup = "Vol";
        p.size = "1,8m";

        p = perName.get("Chetiflor");
        p.evolutions = new EvolutionNode(perName.get("Chetiflor"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 21", new EvolutionNode(perName.get("Boustiflor"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get("Empiflor"), null));}}));}});
        p.catchRate = "255";
        p.weight = "4,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Plante";
        p.size = "0,7m";

        p = perName.get("Carvanha");
        p.evolutions = new EvolutionNode(perName.get("Carvanha"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Sharpedo"), null));}});
        p.catchRate = "225";
        p.weight = "20,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Eau 2";
        p.size = "0,8m";

        p = perName.get("Lumineon");
        p.evolutions = new EvolutionNode(perName.get("Ecayon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 31", new EvolutionNode(perName.get("Lumineon"), null));}});
        p.catchRate = "75";
        p.weight = "24,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Eau 2";
        p.size = "1,2m";

        p = perName.get("Croaporal");
        p.evolutions = new EvolutionNode(perName.get("Grenousse"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Croaporal"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Amphinobi"), null));}}));}});
        p.catchRate = "45";
        p.weight = "10,9kg";
        p.hatch = "pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Eau 1";
        p.size = "0,6m";

        p = perName.get("Rhinocorne");
        p.evolutions = new EvolutionNode(perName.get("Rhinocorne"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 42", new EvolutionNode(perName.get("Rhinoferos"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Protecteur", new EvolutionNode(perName.get("Rhinastoc"), null));}}));}});
        p.catchRate = "120";
        p.weight = "115,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Monstre/Sol";
        p.size = "1,0m";

        p = perName.get("Leviator");
        p.evolutions = new EvolutionNode(perName.get("Magicarpe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Leviator"), new HashMap<String, EvolutionNode>(){{this.put("Leviatorite", new EvolutionNode(perName.get("Mega-Leviator"), null));}}));}});
        p.catchRate = "45";
        p.weight = "235,0kg";
        p.hatch = "4 cycles - 1280 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Eau 2/Dragon";
        p.size = "6,5m";

        p = perName.get("Cryptero");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "14,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Vol";
        p.size = "1,4m";

        p = perName.get("Pharamp");
        p.evolutions = new EvolutionNode(perName.get("Wattouat"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 15", new EvolutionNode(perName.get("Lainergie"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Pharamp"), new HashMap<String, EvolutionNode>(){{this.put("Pharampite", new EvolutionNode(perName.get("Mega-Pharamp"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "61,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Monstre/Sol";
        p.size = "1,4m";

        p = perName.get("Dialga");
        p.evolutions = null;
        p.catchRate = "30";
        p.weight = "683kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "5,4m";

        p = perName.get("Sabelette");
        p.evolutions = new EvolutionNode(perName.get("Sabelette"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 22", new EvolutionNode(perName.get("Sablaireau"), null));}});
        p.catchRate = "255";
        p.weight = "12,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Sol";
        p.size = "0,6m";

        p = perName.get("Dynavolt");
        p.evolutions = new EvolutionNode(perName.get("Dynavolt"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 26", new EvolutionNode(perName.get("Elecsprint"), new HashMap<String, EvolutionNode>(){{this.put("Mega-Evolution", new EvolutionNode(perName.get("Mega-Elecsprint"), null));}}));}});
        p.catchRate = "120";
        p.weight = "15,2kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,6m";

        p = perName.get("Pichu");
        p.evolutions = new EvolutionNode(perName.get("Pichu"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Pikachu"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get("Raichu"), null));}}));}});
        p.catchRate = "190";
        p.weight = "2,0kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sans oeuf";
        p.size = "0,3m";

        p = perName.get("Terrakium");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "260kg";
        p.hatch = "80 cycles - 20655 pas";
        p.gender = "Asexue";
        p.ev = "+3 Att.";
        p.eggGroup = "Sans oeuf";
        p.size = "1,9m";

        p = perName.get("Amagara");
        p.evolutions = new EvolutionNode(perName.get("Amagara"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 39 pendant la nuit", new EvolutionNode(perName.get("Dragmara"), null));}});
        p.catchRate = "45";
        p.weight = "25,2kg";
        p.hatch = "pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 PV";
        p.eggGroup = "";
        p.size = "1,3m";

        p = perName.get("Poissirene");
        p.evolutions = new EvolutionNode(perName.get("Poissirene"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 33", new EvolutionNode(perName.get("Poissoroy"), null));}});
        p.catchRate = "225";
        p.weight = "15,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Eau 2";
        p.size = "0,6m";

        p = perName.get("Magby");
        p.evolutions = new EvolutionNode(perName.get("Magby"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Magmar"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Magmariseur", new EvolutionNode(perName.get("Maganon"), null));}}));}});
        p.catchRate = "45";
        p.weight = "21,4kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sans oeuf";
        p.size = "0,7m";

        p = perName.get("Farfaduvet");
        p.evolutions = new EvolutionNode(perName.get("Doudouvet"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierresoleil", new EvolutionNode(perName.get("Farfaduvet"), null));}});
        p.catchRate = "75";
        p.weight = "6,6kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Plante/Fee";
        p.size = "0,7m";

        p = perName.get("Lockpin");
        p.evolutions = new EvolutionNode(perName.get("Laporeille"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Lockpin"), null));}});
        p.catchRate = "60";
        p.weight = "33,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol/Humanoide";
        p.size = "1,2m";

        p = perName.get("Flotajou");
        p.evolutions = new EvolutionNode(perName.get("Flotajou"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Flotoutan"), null));}});
        p.catchRate = "190";
        p.weight = "13,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,6m";

        p = perName.get("Fouinar");
        p.evolutions = new EvolutionNode(perName.get("Fouinette"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 15", new EvolutionNode(perName.get("Fouinar"), null));}});
        p.catchRate = "90";
        p.weight = "32,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "1,8m";

        p = perName.get("Banshitrouye (Taille Ultra)");
        p.evolutions = new EvolutionNode(perName.get("Pitrouille (Taille Ultra)"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Banshitrouye (Taille Ultra)"), null));}});
        p.catchRate = "";
        p.weight = "9,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Indetermine";
        p.size = "0,7m";

        p = perName.get("Keldeo");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "48,5kg";
        p.hatch = "80 cycles - 20655 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att. Spe; +1 Def. Spe; +1 Vit.";
        p.eggGroup = "Sans oeuf";
        p.size = "1,4m";

        p = perName.get("Jungko");
        p.evolutions = new EvolutionNode(perName.get("Arcko"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Massko"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Jungko"), null));}}));}});
        p.catchRate = "45";
        p.weight = "52,2kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+3 Vit.";
        p.eggGroup = "Monstre/Dragon";
        p.size = "1,7m";

        p = perName.get("Boreas (Forme Avatar)");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "63,0kg";
        p.hatch = "120 cycles - 30855 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "1,5m";

        p = perName.get("Registeel");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "205,0kg";
        p.hatch = "79 cycles - 20480 pas";
        p.gender = "Asexue";
        p.ev = "+2 Def.; +1 Def. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "1,9m";

        p = perName.get("Xatu");
        p.evolutions = new EvolutionNode(perName.get("Natu"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Xatu"), null));}});
        p.catchRate = "75";
        p.weight = "15,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe; +1 Vit.";
        p.eggGroup = "Vol";
        p.size = "1,5m";

        p = perName.get("Skelenox");
        p.evolutions = new EvolutionNode(perName.get("Skelenox"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Teraclope"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Tissu Fauche", new EvolutionNode(perName.get("Noctunoir"), null));}}));}});
        p.catchRate = "190";
        p.weight = "15,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Indetermine";
        p.size = "0,8m";

        p = perName.get("Etourmi");
        p.evolutions = new EvolutionNode(perName.get("Etourmi"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 14", new EvolutionNode(perName.get("Etourvol"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 34", new EvolutionNode(perName.get("Etouraptor"), null));}}));}});
        p.catchRate = "255";
        p.weight = "2,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Vol";
        p.size = "0,3m";

        p = perName.get("Roigada");
        p.evolutions = new EvolutionNode(perName.get("Ramoloss"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Flagadoss"), null));this.put("Echange en tenant Roche Royale", new EvolutionNode(perName.get("Roigada"), null));}});
        p.catchRate = "70";
        p.weight = "79,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Def. Spe";
        p.eggGroup = "Monstre/Eau 1";
        p.size = "2,0m";

        p = perName.get("Tortank");
        p.evolutions = new EvolutionNode(perName.get("Carapuce"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Carabaffe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Tortank"), new HashMap<String, EvolutionNode>(){{this.put("Tortankite", new EvolutionNode(perName.get("Mega-Tortank"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "85,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+3 Def. Spe";
        p.eggGroup = "Eau 1/Monstre";
        p.size = "1,6m";

        p = perName.get("Mega-Cizayox");
        p.evolutions = new EvolutionNode(perName.get("Insecateur"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Peau Metal", new EvolutionNode(perName.get("Cizayox"), new HashMap<String, EvolutionNode>(){{this.put("Cizayoxite", new EvolutionNode(perName.get("Mega-Cizayox"), null));}}));}});
        p.catchRate = "";
        p.weight = "125kg";
        p.hatch = "";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "2m";

        p = perName.get("Minidraco");
        p.evolutions = new EvolutionNode(perName.get("Minidraco"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Draco"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 55", new EvolutionNode(perName.get("Dracolosse"), null));}}));}});
        p.catchRate = "45";
        p.weight = "3,3kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Dragon/Eau 1";
        p.size = "1,8m";

        p = perName.get("Trioxhydre");
        p.evolutions = new EvolutionNode(perName.get("Solochi"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 50", new EvolutionNode(perName.get("Diamat"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 64", new EvolutionNode(perName.get("Trioxhydre"), null));}}));}});
        p.catchRate = "30";
        p.weight = "160,0kg";
        p.hatch = "40 cycles - 10455 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Dragon";
        p.size = "1,8m";

        p = perName.get("Melofee");
        p.evolutions = new EvolutionNode(perName.get("Melo"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Melofee"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get("Melodelfe"), null));}}));}});
        p.catchRate = "150";
        p.weight = "7,5kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+2 PV";
        p.eggGroup = "Fee";
        p.size = "0,6m";

        p = perName.get("Crabicoque");
        p.evolutions = new EvolutionNode(perName.get("Crabicoque"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 34", new EvolutionNode(perName.get("Crabaraque"), null));}});
        p.catchRate = "190";
        p.weight = "14,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Insecte/Mineral";
        p.size = "0,3m";

        p = perName.get("Torterra");
        p.evolutions = new EvolutionNode(perName.get("Tortipouss"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Boskara"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Torterra"), null));}}));}});
        p.catchRate = "45";
        p.weight = "310,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att.; +1 Def.";
        p.eggGroup = "Monstre/Plante";
        p.size = "2,2m";

        p = perName.get("Rototaupe");
        p.evolutions = new EvolutionNode(perName.get("Rototaupe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 31", new EvolutionNode(perName.get("Minotaupe"), null));}});
        p.catchRate = "120";
        p.weight = "8,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol";
        p.size = "0,3m";

        p = perName.get("Ceribou");
        p.evolutions = new EvolutionNode(perName.get("Ceribou"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Ceriflor"), null));}});
        p.catchRate = "190";
        p.weight = "3,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Fee/Plante";
        p.size = "0,4m";

        p = perName.get("Keunotor");
        p.evolutions = new EvolutionNode(perName.get("Keunotor"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 15", new EvolutionNode(perName.get("Castorno"), null));}});
        p.catchRate = "255";
        p.weight = "20,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Eau 1/Sol";
        p.size = "0,5m";

        p = perName.get("Nidoran F");
        p.evolutions = new EvolutionNode(perName.get("Nidoran F"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Nidorina"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get("Nidoqueen"), null));}}));}});
        p.catchRate = "235";
        p.weight = "7,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+1 PV";
        p.eggGroup = "Monstre/Sol";
        p.size = "0,4m";

        p = perName.get("Flambusard");
        p.evolutions = new EvolutionNode(perName.get("Passerouge"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 17", new EvolutionNode(perName.get("Braisillon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Flambusard"), null));}}));}});
        p.catchRate = "";
        p.weight = "24,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Vit.";
        p.eggGroup = "Vol";
        p.size = "1,2m";

        p = perName.get("Helionceau");
        p.evolutions = new EvolutionNode(perName.get("Helionceau"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Nemelios"), null));}});
        p.catchRate = "";
        p.weight = "13,5kg";
        p.hatch = "pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "0,6m";

        p = perName.get("Entei");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "198,0kg";
        p.hatch = "79 cycles - 20480 pas";
        p.gender = "Asexue";
        p.ev = "+1 PV; +2 Att.";
        p.eggGroup = "Sans oeuf";
        p.size = "2,1m";

        p = perName.get("Nidoran M");
        p.evolutions = new EvolutionNode(perName.get("Nidoran M"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Nidorino"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get("Nidoking"), null));}}));}});
        p.catchRate = "235";
        p.weight = "9,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Monstre/Sol";
        p.size = "0,5m";

        p = perName.get("Moustillon");
        p.evolutions = new EvolutionNode(perName.get("Moustillon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 17", new EvolutionNode(perName.get("Mateloutre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Clamiral"), null));}}));}});
        p.catchRate = "45";
        p.weight = "5,9kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att. Spe.";
        p.eggGroup = "Sol";
        p.size = "0,5m";

        p = perName.get("Soporifik");
        p.evolutions = new EvolutionNode(perName.get("Soporifik"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 26", new EvolutionNode(perName.get("Hypnomade"), null));}});
        p.catchRate = "190";
        p.weight = "32,4kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Humanoide";
        p.size = "1,0m";

        p = perName.get("Dimocles");
        p.evolutions = new EvolutionNode(perName.get("Monorpale"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Dimocles"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get("Exagide (Forme Parade)"), null));}}));}});
        p.catchRate = "";
        p.weight = "4,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "Mineral";
        p.size = "0,8m";

        p = perName.get("Riolu");
        p.evolutions = new EvolutionNode(perName.get("Riolu"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur + gagne un niveau de jour", new EvolutionNode(perName.get("Lucario"), new HashMap<String, EvolutionNode>(){{this.put("Lucarite", new EvolutionNode(perName.get("Mega-Lucario"), null));}}));}});
        p.catchRate = "75";
        p.weight = "20,2kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sans oeuf";
        p.size = "0,7m";

        p = perName.get("Spoink");
        p.evolutions = new EvolutionNode(perName.get("Spoink"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Groret"), null));}});
        p.catchRate = "255";
        p.weight = "30,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Sol";
        p.size = "0,7m";

        p = perName.get("Aspicot");
        p.evolutions = new EvolutionNode(perName.get("Aspicot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 7", new EvolutionNode(perName.get("Coconfort"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 10", new EvolutionNode(perName.get("Dardargnan"), null));}}));}});
        p.catchRate = "255";
        p.weight = "3,2kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Insecte";
        p.size = "0,3m";

        p = perName.get("Marcacrin");
        p.evolutions = new EvolutionNode(perName.get("Marcacrin"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 33", new EvolutionNode(perName.get("Cochignon"), new HashMap<String, EvolutionNode>(){{this.put("En connaissant l'attaque Pouv.Antique", new EvolutionNode(perName.get("Mammochon"), null));}}));}});
        p.catchRate = "225";
        p.weight = "6,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol";
        p.size = "0,4m";

        p = perName.get("Mysdibule");
        p.evolutions = new EvolutionNode(perName.get("Mysdibule"), new HashMap<String, EvolutionNode>(){{this.put("Mysdibulite", new EvolutionNode(perName.get("Mega-Mysdibule"), null));}});
        p.catchRate = "45";
        p.weight = "11,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.; +1 Def.";
        p.eggGroup = "Sol/Fee";
        p.size = "0,6m";

        p = perName.get("Chartor");
        p.evolutions = null;
        p.catchRate = "90";
        p.weight = "80,4kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Sol";
        p.size = "0,5m";

        p = perName.get("Minotaupe");
        p.evolutions = new EvolutionNode(perName.get("Rototaupe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 31", new EvolutionNode(perName.get("Minotaupe"), null));}});
        p.catchRate = "60";
        p.weight = "40,4kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol";
        p.size = "0,7m";

        p = perName.get("Maskadra");
        p.evolutions = new EvolutionNode(perName.get("Arakdo"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 22", new EvolutionNode(perName.get("Maskadra"), null));}});
        p.catchRate = "75";
        p.weight = "3,6kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe; +1 Def. Spe";
        p.eggGroup = "Eau 1/Insecte";
        p.size = "0,8m";

        p = perName.get("Yanmega");
        p.evolutions = new EvolutionNode(perName.get("Yanma"), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l'attaque Pouv.Antique", new EvolutionNode(perName.get("Yanmega"), null));}});
        p.catchRate = "30";
        p.weight = "51,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Insecte";
        p.size = "1,9m";

        p = perName.get("Melokrik");
        p.evolutions = new EvolutionNode(perName.get("Crikzik"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 10", new EvolutionNode(perName.get("Melokrik"), null));}});
        p.catchRate = "45";
        p.weight = "25,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Insecte";
        p.size = "1,0m";

        p = perName.get("Scobolide");
        p.evolutions = new EvolutionNode(perName.get("Venipatte"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 22", new EvolutionNode(perName.get("Scobolide"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Brutapode"), null));}}));}});
        p.catchRate = "120";
        p.weight = "58,5kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Insecte";
        p.size = "1,2m";

        p = perName.get("Massko");
        p.evolutions = new EvolutionNode(perName.get("Arcko"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Massko"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Jungko"), null));}}));}});
        p.catchRate = "45";
        p.weight = "21,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Monstre/Dragon";
        p.size = "0,9m";

        p = perName.get("Drackhaus");
        p.evolutions = new EvolutionNode(perName.get("Draby"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Drackhaus"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 50", new EvolutionNode(perName.get("Drattak"), null));}}));}});
        p.catchRate = "45";
        p.weight = "110,5kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Dragon";
        p.size = "1,1m";

        p = perName.get("Sepiatroce");
        p.evolutions = new EvolutionNode(perName.get("Sepiatop"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30, en retournant la 3DS", new EvolutionNode(perName.get("Sepiatroce"), null));}});
        p.catchRate = "";
        p.weight = "47,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Eau 1/Eau 2";
        p.size = "1,5m";

        p = perName.get("Vostourno");
        p.evolutions = new EvolutionNode(perName.get("Vostourno"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 54", new EvolutionNode(perName.get("Vaututrice"), null));}});
        p.catchRate = "190";
        p.weight = "9,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Vol";
        p.size = "0,5m";

        p = perName.get("Ossatueur");
        p.evolutions = new EvolutionNode(perName.get("Osselait"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 28", new EvolutionNode(perName.get("Ossatueur"), null));}});
        p.catchRate = "75";
        p.weight = "45,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Monstre";
        p.size = "1,0m";

        p = perName.get("Cabriolaine");
        p.evolutions = new EvolutionNode(perName.get("Cabriolaine"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Chevroum"), null));}});
        p.catchRate = "";
        p.weight = "31,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Sol";
        p.size = "0,9m";

        p = perName.get("Lombre");
        p.evolutions = new EvolutionNode(perName.get("Nenupiot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 14", new EvolutionNode(perName.get("Lombre"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Ludicolo"), null));}}));}});
        p.catchRate = "120";
        p.weight = "32,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Eau 1/Plante";
        p.size = "1,2m";

        p = perName.get("Apitrini");
        p.evolutions = new EvolutionNode(perName.get("Apitrini"), new HashMap<String, EvolutionNode>(){{this.put("Si Femelle, Niveau 21", new EvolutionNode(perName.get("Apireine"), null));}});
        p.catchRate = "120";
        p.weight = "5,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Insecte";
        p.size = "0,3m";

        p = perName.get("Nirondelle");
        p.evolutions = new EvolutionNode(perName.get("Nirondelle"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 22", new EvolutionNode(perName.get("Heledelle"), null));}});
        p.catchRate = "200";
        p.weight = "2,3kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Vol";
        p.size = "0,3m";

        p = perName.get("Voltali");
        p.evolutions = new EvolutionNode(perName.get("Evoli"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get("Voltali"), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get("Phyllali"), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get("Mentali"), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get("Nymphali"), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Aquali"), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get("Givrali"), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get("Pyroli"), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get("Noctali"), null));}});
        p.catchRate = "45";
        p.weight = "24,5kg";
        p.hatch = "34 cycles - 8960 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,8m";

        p = perName.get("Arceus");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "320,0kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "3,2m";

        p = perName.get("Kadabra");
        p.evolutions = new EvolutionNode(perName.get("Abra"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Kadabra"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Alakazam"), new HashMap<String, EvolutionNode>(){{this.put("Alakazamite", new EvolutionNode(perName.get("Mega-Alakazam"), null));}}));}}));}});
        p.catchRate = "100";
        p.weight = "56,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Humanoide";
        p.size = "1,3m";

        p = perName.get("Muciole");
        p.evolutions = null;
        p.catchRate = "150";
        p.weight = "17,7kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Insecte/Humanoide";
        p.size = "0,7m";

        p = perName.get("Regirock");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "230,0kg";
        p.hatch = "79 cycles - 20480 pas";
        p.gender = "Asexue";
        p.ev = "+3 Def.";
        p.eggGroup = "Sans oeuf";
        p.size = "1,7m";

        p = perName.get("Deoxys (Forme Attaque)");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "60,8kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att.; +1 Att. Spe; +1 Vit.";
        p.eggGroup = "Sans oeuf";
        p.size = "1,7m";

        p = perName.get("Tarpaud");
        p.evolutions = new EvolutionNode(perName.get("Ptitard"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Tetarte"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Roche Royale", new EvolutionNode(perName.get("Tarpaud"), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Tartard"), null));}}));}});
        p.catchRate = "45";
        p.weight = "33,9kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Eau 1";
        p.size = "1,1m";

        p = perName.get("Sapereau");
        p.evolutions = new EvolutionNode(perName.get("Sapereau"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Excavarenne"), null));}});
        p.catchRate = "";
        p.weight = "5,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,4m";

        p = perName.get("Cacturne");
        p.evolutions = new EvolutionNode(perName.get("Cacnea"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Cacturne"), null));}});
        p.catchRate = "60";
        p.weight = "77,4kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.; +1 Att. Spe";
        p.eggGroup = "Plante/Humanoide";
        p.size = "1,3m";

        p = perName.get("Raichu");
        p.evolutions = new EvolutionNode(perName.get("Pichu"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Pikachu"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get("Raichu"), null));}}));}});
        p.catchRate = "75";
        p.weight = "30,0kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Vit.";
        p.eggGroup = "Sol/Fee";
        p.size = "0,8m";

        p = perName.get("Poissoroy");
        p.evolutions = new EvolutionNode(perName.get("Poissirene"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 33", new EvolutionNode(perName.get("Poissoroy"), null));}});
        p.catchRate = "60";
        p.weight = "39,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Eau 2";
        p.size = "1,3m";

        p = perName.get("Vibraninf");
        p.evolutions = new EvolutionNode(perName.get("Kraknoix"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Vibraninf"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 45", new EvolutionNode(perName.get("Libegon"), null));}}));}});
        p.catchRate = "120";
        p.weight = "15,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.; +1 Vit.";
        p.eggGroup = "Insecte";
        p.size = "1,1m";

        p = perName.get("Vivaldaim");
        p.evolutions = new EvolutionNode(perName.get("Vivaldaim"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 34", new EvolutionNode(perName.get("Haydaim"), null));}});
        p.catchRate = "190";
        p.weight = "19,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,6m";

        p = perName.get("Tadmorv");
        p.evolutions = new EvolutionNode(perName.get("Tadmorv"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 38", new EvolutionNode(perName.get("Grotadmorv"), null));}});
        p.catchRate = "190";
        p.weight = "30,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Indetermine";
        p.size = "0,9m";

        p = perName.get("Zarbi");
        p.evolutions = null;
        p.catchRate = "225";
        p.weight = "5,0kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att.; +1 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "0,5m";

        p = perName.get("Galifeu");
        p.evolutions = new EvolutionNode(perName.get("Poussifeu"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Galifeu"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Brasegali"), new HashMap<String, EvolutionNode>(){{this.put("Brasegalite", new EvolutionNode(perName.get("Mega-Brasegali"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "19,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att.; +1 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "0,9m";

        p = perName.get("Dardargnan");
        p.evolutions = new EvolutionNode(perName.get("Aspicot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 7", new EvolutionNode(perName.get("Coconfort"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 10", new EvolutionNode(perName.get("Dardargnan"), null));}}));}});
        p.catchRate = "45";
        p.weight = "29,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.; +1 Def. Spe";
        p.eggGroup = "Insecte";
        p.size = "1,0m";

        p = perName.get("Tylton");
        p.evolutions = new EvolutionNode(perName.get("Tylton"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Altaria"), null));}});
        p.catchRate = "255";
        p.weight = "1,2kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Vol/Dragon";
        p.size = "0,4m";

        p = perName.get("Feuillajou");
        p.evolutions = new EvolutionNode(perName.get("Feuillajou"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get("Feuiloutan"), null));}});
        p.catchRate = "190";
        p.weight = "10,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,6m";

        p = perName.get("Manternel");
        p.evolutions = new EvolutionNode(perName.get("Larveyette"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Couverdure"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Manternel"), null));}}));}});
        p.catchRate = "45";
        p.weight = "20,5kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Insecte";
        p.size = "1,2m";

        p = perName.get("Cornebre");
        p.evolutions = new EvolutionNode(perName.get("Cornebre"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get("Corboss"), null));}});
        p.catchRate = "30";
        p.weight = "2,1kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Vol";
        p.size = "0,5m";

        p = perName.get("Terhal");
        p.evolutions = new EvolutionNode(perName.get("Terhal"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Metang"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 45", new EvolutionNode(perName.get("Metalosse"), null));}}));}});
        p.catchRate = "3";
        p.weight = "95,2kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "Asexue";
        p.ev = "+1 Def.";
        p.eggGroup = "Mineral";
        p.size = "0,6m";

        p = perName.get("Shaofouine");
        p.evolutions = new EvolutionNode(perName.get("Kungfouine"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 50", new EvolutionNode(perName.get("Shaofouine"), null));}});
        p.catchRate = "45";
        p.weight = "35,5kg";
        p.hatch = "25 cycles - 6630 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol/Humanoide";
        p.size = "1,4m";

        p = perName.get("Papilord");
        p.evolutions = new EvolutionNode(perName.get("Cheniti"), new HashMap<String, EvolutionNode>(){{this.put("Si Male, Niveau 20", new EvolutionNode(perName.get("Papilord"), null));this.put("Si Femelle, Niveau 20", new EvolutionNode(perName.get("Cheniselle (Cape Plante)"), null));}});
        p.catchRate = "45";
        p.weight = "23,3kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+1 Att.; +1 Att. Spe";
        p.eggGroup = "Insecte";
        p.size = "0,9m";

        p = perName.get("Fantominus");
        p.evolutions = new EvolutionNode(perName.get("Fantominus"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Spectrum"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Ectoplasma"), new HashMap<String, EvolutionNode>(){{this.put("Ectoplasmite", new EvolutionNode(perName.get("Mega-Ectoplasma"), null));}}));}}));}});
        p.catchRate = "190";
        p.weight = "0,1kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Indetermine";
        p.size = "1,3m";

        p = perName.get("Lakmecygne");
        p.evolutions = new EvolutionNode(perName.get("Couaneton"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Lakmecygne"), null));}});
        p.catchRate = "45";
        p.weight = "24,2kg";
        p.hatch = "30 cycles - 7905 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Eau 1/Vol";
        p.size = "1,3m";

        p = perName.get("Kraknoix");
        p.evolutions = new EvolutionNode(perName.get("Kraknoix"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Vibraninf"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 45", new EvolutionNode(perName.get("Libegon"), null));}}));}});
        p.catchRate = "255";
        p.weight = "15,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Insecte";
        p.size = "0,7m";

        p = perName.get("Leuphorie");
        p.evolutions = new EvolutionNode(perName.get("Ptiravi"), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau en tenant une Pierre Ovale", new EvolutionNode(perName.get("Leveinard"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Leuphorie"), null));}}));}});
        p.catchRate = "30";
        p.weight = "46,8kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+3 PV";
        p.eggGroup = "Fee";
        p.size = "1,5m";

        p = perName.get("Boskara");
        p.evolutions = new EvolutionNode(perName.get("Tortipouss"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Boskara"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Torterra"), null));}}));}});
        p.catchRate = "45";
        p.weight = "97,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att.; +1 Att. Spe";
        p.eggGroup = "Monstre/Plante";
        p.size = "1,1m";

        p = perName.get("Giratina (Forme Originelle)");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "750kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "4,5m";

        p = perName.get("Gigalithe");
        p.evolutions = new EvolutionNode(perName.get("Nodulithe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Geolithe"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Gigalithe"), null));}}));}});
        p.catchRate = "45";
        p.weight = "260,0kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Mineral";
        p.size = "1,7m";

        p = perName.get("Ecayon");
        p.evolutions = new EvolutionNode(perName.get("Ecayon"), new HashMap<String, EvolutionNode>(){{this.put("niveau 31", new EvolutionNode(perName.get("Lumineon"), null));}});
        p.catchRate = "190";
        p.weight = "7,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Eau 2";
        p.size = "0,4m";

        p = perName.get("Statitik");
        p.evolutions = new EvolutionNode(perName.get("Statitik"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Mygavolt"), null));}});
        p.catchRate = "190";
        p.weight = "0,6kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Insecte";
        p.size = "0,1m";

        p = perName.get("Teraclope");
        p.evolutions = new EvolutionNode(perName.get("Skelenox"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Teraclope"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant l'objet Tissu Fauche", new EvolutionNode(perName.get("Noctunoir"), null));}}));}});
        p.catchRate = "90";
        p.weight = "30,6kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.; +1 Def. Spe";
        p.eggGroup = "Indetermine";
        p.size = "1,6m";
    }
    
    private static void setAdditionalInformationPart2() {
        Pokemon p;

        p = perName.get("Aquali");
        p.evolutions = new EvolutionNode(perName.get("Evoli"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get("Voltali"), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get("Phyllali"), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get("Mentali"), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get("Nymphali"), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Aquali"), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get("Givrali"), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get("Pyroli"), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get("Noctali"), null));}});
        p.catchRate = "45";
        p.weight = "29,0kg";
        p.hatch = "34 cycles - 8960 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 PV";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Draco");
        p.evolutions = new EvolutionNode(perName.get("Minidraco"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Draco"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 55", new EvolutionNode(perName.get("Dracolosse"), null));}}));}});
        p.catchRate = "45";
        p.weight = "16,5kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Dragon/Eau 1";
        p.size = "4,0m";

        p = perName.get("Magnezone");
        p.evolutions = new EvolutionNode(perName.get("Magneti"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Magneton"), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau dans un lieu indique", new EvolutionNode(perName.get("Magnezone"), null));}}));}});
        p.catchRate = "30";
        p.weight = "180,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Mineral";
        p.size = "1,2m";

        p = perName.get("Mega-Galeking");
        p.evolutions = new EvolutionNode(perName.get("Galekid"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Galegon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 42", new EvolutionNode(perName.get("Galeking"), new HashMap<String, EvolutionNode>(){{this.put("Galekingite", new EvolutionNode(perName.get("Mega-Galeking"), null));}}));}}));}});
        p.catchRate = "";
        p.weight = "395kg";
        p.hatch = "";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "2,2m";

        p = perName.get("Monaflemit");
        p.evolutions = new EvolutionNode(perName.get("Parecool"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Vigoroth"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Monaflemit"), null));}}));}});
        p.catchRate = "45";
        p.weight = "130,5kg";
        p.hatch = "15 cycles - 4095 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 PV";
        p.eggGroup = "Sol";
        p.size = "2,0m";

        p = perName.get("Spinda");
        p.evolutions = null;
        p.catchRate = "255";
        p.weight = "5,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Sol/Humanoide";
        p.size = "1,1m";

        p = perName.get("Tartard");
        p.evolutions = new EvolutionNode(perName.get("Ptitard"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Tetarte"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Roche Royale", new EvolutionNode(perName.get("Tarpaud"), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Tartard"), null));}}));}});
        p.catchRate = "45";
        p.weight = "54,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Def.";
        p.eggGroup = "Eau 1";
        p.size = "1,3m";

        p = perName.get("Palkia");
        p.evolutions = null;
        p.catchRate = "30";
        p.weight = "336,0kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "4,2m";

        p = perName.get("Tauros");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "88,4kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+1 Att.; +1 Vit.";
        p.eggGroup = "Sol";
        p.size = "1,4m";

        p = perName.get("Etouraptor");
        p.evolutions = new EvolutionNode(perName.get("Etourmi"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 14", new EvolutionNode(perName.get("Etourvol"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 34", new EvolutionNode(perName.get("Etouraptor"), null));}}));}});
        p.catchRate = "45";
        p.weight = "24,9kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Vol";
        p.size = "1,2m";

        p = perName.get("Suicune");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "187,0kg";
        p.hatch = "79 cycles - 20480 pas";
        p.gender = "Asexue";
        p.ev = "+1 Def.; +2 Def. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "2,0m";

        p = perName.get("Raikou");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "178,0kg";
        p.hatch = "79 cycles - 20480 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att. Spe; +2 Vit.";
        p.eggGroup = "Sans oeuf";
        p.size = "1,9m";

        p = perName.get("Pingoleon");
        p.evolutions = new EvolutionNode(perName.get("Tiplouf"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Prinplouf"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Pingoleon"), null));}}));}});
        p.catchRate = "45";
        p.weight = "84,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Eau 1/Sol";
        p.size = "1,7m";

        p = perName.get("Hericendre");
        p.evolutions = new EvolutionNode(perName.get("Hericendre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 14", new EvolutionNode(perName.get("Feurisson"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Typhlosion"), null));}}));}});
        p.catchRate = "45";
        p.weight = "7,9kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,5m";

        p = perName.get("Arbok");
        p.evolutions = new EvolutionNode(perName.get("Abo"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 22", new EvolutionNode(perName.get("Arbok"), null));}});
        p.catchRate = "90";
        p.weight = "65,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol/Dragon";
        p.size = "3,5m";

        p = perName.get("Mesmerella");
        p.evolutions = new EvolutionNode(perName.get("Scrutella"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Mesmerella"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 41", new EvolutionNode(perName.get("Siderella"), null));}}));}});
        p.catchRate = "100";
        p.weight = "18,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Humanoide";
        p.size = "0,7m";

        p = perName.get("Chimpenfeu");
        p.evolutions = new EvolutionNode(perName.get("Ouisticram"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 14", new EvolutionNode(perName.get("Chimpenfeu"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Simiabraz"), null));}}));}});
        p.catchRate = "45";
        p.weight = "22,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att. Spe; +1 Vit.";
        p.eggGroup = "Sol/Humanoide";
        p.size = "0,9m";

        p = perName.get("Psykokwak");
        p.evolutions = new EvolutionNode(perName.get("Psykokwak"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 33", new EvolutionNode(perName.get("Akwakwak"), null));}});
        p.catchRate = "190";
        p.weight = "19,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Eau 1/Sol";
        p.size = "0,8m";

        p = perName.get("Boustiflor");
        p.evolutions = new EvolutionNode(perName.get("Chetiflor"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 21", new EvolutionNode(perName.get("Boustiflor"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get("Empiflor"), null));}}));}});
        p.catchRate = "120";
        p.weight = "6,4kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Plante";
        p.size = "1,0m";

        p = perName.get("Porygon2");
        p.evolutions = new EvolutionNode(perName.get("Porygon"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Ameliorator", new EvolutionNode(perName.get("Porygon2"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant CD Douteux", new EvolutionNode(perName.get("Porygon-Z"), null));}}));}});
        p.catchRate = "45";
        p.weight = "32,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Mineral";
        p.size = "0,6m";

        p = perName.get("Kaimorse");
        p.evolutions = new EvolutionNode(perName.get("Obalie"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Phogleur"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 44", new EvolutionNode(perName.get("Kaimorse"), null));}}));}});
        p.catchRate = "45";
        p.weight = "150,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 PV";
        p.eggGroup = "Eau 1/Sol";
        p.size = "1,4m";

        p = perName.get("Akwakwak");
        p.evolutions = new EvolutionNode(perName.get("Psykokwak"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 33", new EvolutionNode(perName.get("Akwakwak"), null));}});
        p.catchRate = "75";
        p.weight = "76,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Eau 1/Sol";
        p.size = "1,7m";

        p = perName.get("Tygnon");
        p.evolutions = new EvolutionNode(perName.get("Debugant"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20, Attaque Defense", new EvolutionNode(perName.get("Tygnon"), null));this.put("Niveau 20, Attaque et Defense identiques", new EvolutionNode(perName.get("Kapoera"), null));}});
        p.catchRate = "45";
        p.weight = "50,2kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Humanoide";
        p.size = "1,4m";

        p = perName.get("Goinfrex");
        p.evolutions = new EvolutionNode(perName.get("Goinfrex"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Ronflex"), null));}});
        p.catchRate = "50";
        p.weight = "105,0kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "0,6m";

        p = perName.get("Griknot");
        p.evolutions = new EvolutionNode(perName.get("Griknot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 24", new EvolutionNode(perName.get("Carmache"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 48", new EvolutionNode(perName.get("Carchacrok"), new HashMap<String, EvolutionNode>(){{this.put("Carchacrokite", new EvolutionNode(perName.get("Mega-Carchacrok"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "20,5kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Dragon/Monstre";
        p.size = "0,7m";

        p = perName.get("Sucroquin");
        p.evolutions = new EvolutionNode(perName.get("Sucroquin"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Chantibonbon", new EvolutionNode(perName.get("Cupcanaille"), null));}});
        p.catchRate = "";
        p.weight = "3,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Fee";
        p.size = "0,4m";

        p = perName.get("Escargaume");
        p.evolutions = new EvolutionNode(perName.get("Escargaume"), new HashMap<String, EvolutionNode>(){{this.put("Echange avec Carabing", new EvolutionNode(perName.get("Limaspeed"), null));}});
        p.catchRate = "200";
        p.weight = "7,7kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Insecte";
        p.size = "0,4m";

        p = perName.get("Monorpale");
        p.evolutions = new EvolutionNode(perName.get("Monorpale"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Dimocles"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get("Exagide (Forme Parade)"), null));}}));}});
        p.catchRate = "";
        p.weight = "2,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Mineral";
        p.size = "0,8m";

        p = perName.get("Goupelin");
        p.evolutions = new EvolutionNode(perName.get("Feunnec"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Roussil"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Goupelin"), null));}}));}});
        p.catchRate = "45";
        p.weight = "39,0kg";
        p.hatch = "pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "1,5m";

        p = perName.get("Tenefix");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "11,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.; +1 Def.";
        p.eggGroup = "Humanoide";
        p.size = "0,5m";

        p = perName.get("Mustebouee");
        p.evolutions = new EvolutionNode(perName.get("Mustebouee"), new HashMap<String, EvolutionNode>(){{this.put("niveau 26", new EvolutionNode(perName.get("Musteflott"), null));}});
        p.catchRate = "190";
        p.weight = "29,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Eau 1/Sol";
        p.size = "0,7m";

        p = perName.get("Geolithe");
        p.evolutions = new EvolutionNode(perName.get("Nodulithe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Geolithe"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Gigalithe"), null));}}));}});
        p.catchRate = "120";
        p.weight = "102,0kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.; +1 Def.";
        p.eggGroup = "Mineral";
        p.size = "0,9m";

        p = perName.get("Pomdepik");
        p.evolutions = new EvolutionNode(perName.get("Pomdepik"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 31", new EvolutionNode(perName.get("Foretress"), null));}});
        p.catchRate = "190";
        p.weight = "7,2kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Insecte";
        p.size = "0,6m";

        p = perName.get("Relicanth");
        p.evolutions = null;
        p.catchRate = "25";
        p.weight = "23,4kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 PV; +1 Def.";
        p.eggGroup = "Eau 1/Eau 2";
        p.size = "1,0m";

        p = perName.get("Mushana");
        p.evolutions = new EvolutionNode(perName.get("Munna"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get("Mushana"), null));}});
        p.catchRate = "75";
        p.weight = "60,5kg";
        p.hatch = "10 cycles - 2805 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Sol";
        p.size = "1,1m";

        p = perName.get("Ptiravi");
        p.evolutions = new EvolutionNode(perName.get("Ptiravi"), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau en journee en tenant une Pierre Ovale", new EvolutionNode(perName.get("Leveinard"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Leuphorie"), null));}}));}});
        p.catchRate = "130";
        p.weight = "24,4kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+1 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "0,6m";

        p = perName.get("Sablaireau");
        p.evolutions = new EvolutionNode(perName.get("Sabelette"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 22", new EvolutionNode(perName.get("Sablaireau"), null));}});
        p.catchRate = "90";
        p.weight = "29,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Ohmassacre");
        p.evolutions = new EvolutionNode(perName.get("Anchwatt"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 39", new EvolutionNode(perName.get("Lamperoie"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get("Ohmassacre"), null));}}));}});
        p.catchRate = "30";
        p.weight = "80,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Indetermine";
        p.size = "2,1m";

        p = perName.get("Banshitrouye (Taille Mini)");
        p.evolutions = new EvolutionNode(perName.get("Pitrouille (Taille Mini)"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Banshitrouye (Taille Mini)"), null));}});
        p.catchRate = "";
        p.weight = "9,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Indetermine";
        p.size = "0,7m";

        p = perName.get("Brocelome");
        p.evolutions = new EvolutionNode(perName.get("Brocelome"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Desseliande"), null));}});
        p.catchRate = "";
        p.weight = "7,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Plante/Indetermine";
        p.size = "0,4m";

        p = perName.get("Rozbouton");
        p.evolutions = new EvolutionNode(perName.get("Rozbouton"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur , Jour", new EvolutionNode(perName.get("Roselia"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get("Roserade"), null));}}));}});
        p.catchRate = "255";
        p.weight = "1,2kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "0,2m";

        p = perName.get("Scalproie");
        p.evolutions = new EvolutionNode(perName.get("Scalpion"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 52", new EvolutionNode(perName.get("Scalproie"), null));}});
        p.catchRate = "45";
        p.weight = "70,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Humanoide";
        p.size = "1,6m";

        p = perName.get("Phogleur");
        p.evolutions = new EvolutionNode(perName.get("Obalie"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Phogleur"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 44", new EvolutionNode(perName.get("Kaimorse"), null));}}));}});
        p.catchRate = "120";
        p.weight = "87,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Eau 1/Sol";
        p.size = "1,1m";

        p = perName.get("Venipatte");
        p.evolutions = new EvolutionNode(perName.get("Venipatte"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 22", new EvolutionNode(perName.get("Scobolide"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Brutapode"), null));}}));}});
        p.catchRate = "255";
        p.weight = "5,3kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Insecte";
        p.size = "0,4m";

        p = perName.get("Chovsourir");
        p.evolutions = new EvolutionNode(perName.get("Chovsourir"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Rhinolove"), null));}});
        p.catchRate = "190";
        p.weight = "2,1kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol/Vol";
        p.size = "0,4m";

        p = perName.get("Musteflott");
        p.evolutions = new EvolutionNode(perName.get("Mustebouee"), new HashMap<String, EvolutionNode>(){{this.put("niveau 26", new EvolutionNode(perName.get("Musteflott"), null));}});
        p.catchRate = "75";
        p.weight = "33,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Eau 1/Sol";
        p.size = "1,1m";

        p = perName.get("Insolourdo");
        p.evolutions = null;
        p.catchRate = "190";
        p.weight = "14,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Sol";
        p.size = "1,5m";

        p = perName.get("Mega-Tyranocif");
        p.evolutions = new EvolutionNode(perName.get("Embrylex"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Ymphect"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 55", new EvolutionNode(perName.get("Tyranocif"), new HashMap<String, EvolutionNode>(){{this.put("Tyranocivite", new EvolutionNode(perName.get("Mega-Tyranocif"), null));}}));}}));}});
        p.catchRate = "";
        p.weight = "255,0kg";
        p.hatch = "";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "2,5m";

        p = perName.get("Munja");
        p.evolutions = new EvolutionNode(perName.get("Ningale"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Ninjask"), null));this.put("Niveau 20, emplacement libre et Poke Ball dans l'inventaire", new EvolutionNode(perName.get("Munja"), null));}});
        p.catchRate = "45";
        p.weight = "1,2kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "Asexue";
        p.ev = "+2 PV";
        p.eggGroup = "Mineral";
        p.size = "0,8m";

        p = perName.get("Drakkarmin");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "139,0kg";
        p.hatch = "30 cycles - 7905 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Dragon/Monstre";
        p.size = "1,6m";

        p = perName.get("Sorbouboul");
        p.evolutions = new EvolutionNode(perName.get("Sorbebe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Sorboul"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 47", new EvolutionNode(perName.get("Sorbouboul"), null));}}));}});
        p.catchRate = "45";
        p.weight = "57,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Mineral";
        p.size = "1,5m";

        p = perName.get("Mega-Blizzaroi");
        p.evolutions = new EvolutionNode(perName.get("Blizzi"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Blizzaroi"), new HashMap<String, EvolutionNode>(){{this.put("Blizzarite", new EvolutionNode(perName.get("Mega-Blizzaroi"), null));}}));}});
        p.catchRate = "";
        p.weight = "135,5kg";
        p.hatch = "";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "2,2m";

        p = perName.get("Zekrom");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "345kg";
        p.hatch = "120 cycles - 30855 pas";
        p.gender = "Asexue";
        p.ev = "+3 Att.";
        p.eggGroup = "Sans oeuf";
        p.size = "2,9m";

        p = perName.get("Remoraid");
        p.evolutions = new EvolutionNode(perName.get("Remoraid"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Octillery"), null));}});
        p.catchRate = "190";
        p.weight = "12,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Eau 1/Eau 2";
        p.size = "0,6m";

        p = perName.get("Mamanbo");
        p.evolutions = null;
        p.catchRate = "75";
        p.weight = "31,6kg";
        p.hatch = "40 cycles - 10455 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Eau 1/Eau 2";
        p.size = "1,2m";

        p = perName.get("Meios");
        p.evolutions = new EvolutionNode(perName.get("Nucleos"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Meios"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 41", new EvolutionNode(perName.get("Symbios"), null));}}));}});
        p.catchRate = "100";
        p.weight = "8,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Indetermine";
        p.size = "0,6m";

        p = perName.get("Noctali");
        p.evolutions = new EvolutionNode(perName.get("Evoli"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get("Voltali"), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get("Phyllali"), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get("Mentali"), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get("Nymphali"), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Aquali"), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get("Givrali"), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get("Pyroli"), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get("Noctali"), null));}});
        p.catchRate = "45";
        p.weight = "27,0kg";
        p.hatch = "34 cycles - 8960 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Def. Spe.";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Mega-Pharamp");
        p.evolutions = new EvolutionNode(perName.get("Wattouat"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 15", new EvolutionNode(perName.get("Lainergie"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Pharamp"), new HashMap<String, EvolutionNode>(){{this.put("Pharampite", new EvolutionNode(perName.get("Mega-Pharamp"), null));}}));}}));}});
        p.catchRate = "";
        p.weight = "61,5kg";
        p.hatch = "";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,4m";

        p = perName.get("Ramoloss");
        p.evolutions = new EvolutionNode(perName.get("Ramoloss"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Flagadoss"), null));this.put("Echange en tenant Roche Royale", new EvolutionNode(perName.get("Roigada"), null));}});
        p.catchRate = "190";
        p.weight = "36,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Monstre/Eau 1";
        p.size = "1,2m";

        p = perName.get("Cupcanaille");
        p.evolutions = new EvolutionNode(perName.get("Sucroquin"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Chantibonbon", new EvolutionNode(perName.get("Cupcanaille"), null));}});
        p.catchRate = "";
        p.weight = "5,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Fee";
        p.size = "0,8m";

        p = perName.get("Carabaffe");
        p.evolutions = new EvolutionNode(perName.get("Carapuce"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Carabaffe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Tortank"), new HashMap<String, EvolutionNode>(){{this.put("Tortankite", new EvolutionNode(perName.get("Mega-Tortank"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "22,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Def.; +1 Def. Spe";
        p.eggGroup = "Eau 1/Monstre";
        p.size = "1,0m";

        p = perName.get("Barbicha");
        p.evolutions = new EvolutionNode(perName.get("Barloche"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Barbicha"), null));}});
        p.catchRate = "75";
        p.weight = "23,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Eau 2";
        p.size = "0,9m";

        p = perName.get("Colombeau");
        p.evolutions = new EvolutionNode(perName.get("Poichigeon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 21", new EvolutionNode(perName.get("Colombeau"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Deflaisan"), null));}}));}});
        p.catchRate = "120";
        p.weight = "15,0kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Vol";
        p.size = "0,6m";

        p = perName.get("Ramboum");
        p.evolutions = new EvolutionNode(perName.get("Chuchmur"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Ramboum"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Brouhabam"), null));}}));}});
        p.catchRate = "120";
        p.weight = "40,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Monstre/Sol";
        p.size = "1,0m";

        p = perName.get("Kicklee");
        p.evolutions = new EvolutionNode(perName.get("Debugant"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20, Attaque Defense", new EvolutionNode(perName.get("Tygnon"), null));this.put("Niveau 20, Attaque et Defense identiques", new EvolutionNode(perName.get("Kapoera"), null));}});
        p.catchRate = "45";
        p.weight = "49,8kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Humanoide";
        p.size = "1,5m";

        p = perName.get("Teddiursa");
        p.evolutions = new EvolutionNode(perName.get("Teddiursa"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Ursaring"), null));}});
        p.catchRate = "120";
        p.weight = "8,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol";
        p.size = "0,6m";

        p = perName.get("Karaclee");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "51,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Humanoide";
        p.size = "1,4m";

        p = perName.get("Serpang");
        p.evolutions = new EvolutionNode(perName.get("Coquiperl"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant une Ecaille Ocean", new EvolutionNode(perName.get("Rosabyss"), null));this.put("Echange en tenant une Dent Ocean", new EvolutionNode(perName.get("Serpang"), null));}});
        p.catchRate = "60";
        p.weight = "27,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.; +1 Def.";
        p.eggGroup = "Eau 1";
        p.size = "1,7m";

        p = perName.get("Porygon");
        p.evolutions = new EvolutionNode(perName.get("Porygon"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Ameliorator", new EvolutionNode(perName.get("Porygon2"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant CD Douteux", new EvolutionNode(perName.get("Porygon-Z"), null));}}));}});
        p.catchRate = "45";
        p.weight = "36,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Mineral";
        p.size = "0,8m";

        p = perName.get("Mastouffe");
        p.evolutions = new EvolutionNode(perName.get("Ponchiot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Ponchien"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Mastouffe"), null));}}));}});
        p.catchRate = "45";
        p.weight = "61,0kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Sol";
        p.size = "1,2m";

        p = perName.get("Majaspic");
        p.evolutions = new EvolutionNode(perName.get("Vipelierre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 17", new EvolutionNode(perName.get("Lianaja"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Majaspic"), null));}}));}});
        p.catchRate = "45";
        p.weight = "63kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+3 Vit.";
        p.eggGroup = "Sol/Plante";
        p.size = "3,3m";

        p = perName.get("Kungfouine");
        p.evolutions = new EvolutionNode(perName.get("Kungfouine"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 50", new EvolutionNode(perName.get("Shaofouine"), null));}});
        p.catchRate = "180";
        p.weight = "20,0kg";
        p.hatch = "25 cycles - 6630 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol/Humanoide";
        p.size = "0,8m";

        p = perName.get("Nenupiot");
        p.evolutions = new EvolutionNode(perName.get("Nenupiot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 14", new EvolutionNode(perName.get("Lombre"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Ludicolo"), null));}}));}});
        p.catchRate = "255";
        p.weight = "2,6kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Eau 1/Plante";
        p.size = "0,5m";

        p = perName.get("Foretress");
        p.evolutions = new EvolutionNode(perName.get("Pomdepik"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 31", new EvolutionNode(perName.get("Foretress"), null));}});
        p.catchRate = "75";
        p.weight = "125,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Insecte";
        p.size = "1,2m";

        p = perName.get("Mimitoss");
        p.evolutions = new EvolutionNode(perName.get("Mimitoss"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 31", new EvolutionNode(perName.get("Aeromite"), null));}});
        p.catchRate = "190";
        p.weight = "30,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Insecte";
        p.size = "1,0m";

        p = perName.get("Lippoutou");
        p.evolutions = new EvolutionNode(perName.get("Lippouti"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Lippoutou"), null));}});
        p.catchRate = "45";
        p.weight = "40,6kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Humanoide";
        p.size = "1,4m";

        p = perName.get("Negapi");
        p.evolutions = null;
        p.catchRate = "200";
        p.weight = "4,2kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Fee";
        p.size = "0,4m";

        p = perName.get("Mega-Leviator");
        p.evolutions = new EvolutionNode(perName.get("Magicarpe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Leviator"), new HashMap<String, EvolutionNode>(){{this.put("Leviatorite", new EvolutionNode(perName.get("Mega-Leviator"), null));}}));}});
        p.catchRate = "";
        p.weight = "305,0kg";
        p.hatch = "";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "6,5m";

        p = perName.get("Mega-Dracaufeu Y");
        p.evolutions = new EvolutionNode(perName.get("Salameche"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Reptincel"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Dracaufeu"), new HashMap<String, EvolutionNode>(){{this.put("Dracaufite X", new EvolutionNode(perName.get("Mega-Dracaufeu X"), null));this.put("Dracaufite Y", new EvolutionNode(perName.get("Mega-Dracaufeu Y"), null));}}));}}));}});
        p.catchRate = "";
        p.weight = "100,5kg";
        p.hatch = "";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,7m";

        p = perName.get("Mega-Dracaufeu X");
        p.evolutions = new EvolutionNode(perName.get("Salameche"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Reptincel"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Dracaufeu"), new HashMap<String, EvolutionNode>(){{this.put("Dracaufite X", new EvolutionNode(perName.get("Mega-Dracaufeu X"), null));this.put("Dracaufite Y", new EvolutionNode(perName.get("Mega-Dracaufeu Y"), null));}}));}}));}});
        p.catchRate = "";
        p.weight = "110,5kg";
        p.hatch = "";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,7m";

        p = perName.get("Ouisticram");
        p.evolutions = new EvolutionNode(perName.get("Ouisticram"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 14", new EvolutionNode(perName.get("Chimpenfeu"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Simiabraz"), null));}}));}});
        p.catchRate = "45";
        p.weight = "6,2kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol/Humanoide";
        p.size = "0,5m";

        p = perName.get("Gallame");
        p.evolutions = new EvolutionNode(perName.get("Tarsal"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Kirlia"), new HashMap<String, EvolutionNode>(){{this.put("Male + Pierre Aube", new EvolutionNode(perName.get("Gallame"), null));this.put("Niveau 30", new EvolutionNode(perName.get("Gardevoir"), new HashMap<String, EvolutionNode>(){{this.put("Gardevoirite", new EvolutionNode(perName.get("Mega-Gardevoir"), null));}}));}}));}});
        p.catchRate = "60";
        p.weight = "52,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Indetermine";
        p.size = "1,6m";

        p = perName.get("Loupio");
        p.evolutions = new EvolutionNode(perName.get("Loupio"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 27", new EvolutionNode(perName.get("Lanturn"), null));}});
        p.catchRate = "190";
        p.weight = "12,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Eau 2";
        p.size = "0,5m";

        p = perName.get("Pandespiegle");
        p.evolutions = new EvolutionNode(perName.get("Pandespiegle"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32, en ayant un Pokemon dans l'equipe", new EvolutionNode(perName.get("Pandarbare"), null));}});
        p.catchRate = "";
        p.weight = "8,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol/Humanoide";
        p.size = "0,6m";

        p = perName.get("Muplodocus");
        p.evolutions = new EvolutionNode(perName.get("Mucuscule"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Colimucus"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 50, quand il pleut", new EvolutionNode(perName.get("Muplodocus"), null));}}));}});
        p.catchRate = "";
        p.weight = "150,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Def. Spe";
        p.eggGroup = "Dragon";
        p.size = "2,0m";

        p = perName.get("Blindepique");
        p.evolutions = new EvolutionNode(perName.get("Marisson"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Boguerisse"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Blindepique"), null));}}));}});
        p.catchRate = "45";
        p.weight = "90,0kg";
        p.hatch = "pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+3 Def.";
        p.eggGroup = "Sol";
        p.size = "1,6m";

        p = perName.get("Melancolux");
        p.evolutions = new EvolutionNode(perName.get("Funecire"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 41", new EvolutionNode(perName.get("Melancolux"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get("Lugulabre"), null));}}));}});
        p.catchRate = "190";
        p.weight = "13,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Indetermine";
        p.size = "0,6m";

        p = perName.get("Viridium");
        p.evolutions = null;
        p.catchRate = "5";
        p.weight = "200,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "Asexue";
        p.ev = "+3 Def. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "2,0m";

        p = perName.get("Fouinette");
        p.evolutions = new EvolutionNode(perName.get("Fouinette"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 15", new EvolutionNode(perName.get("Fouinar"), null));}});
        p.catchRate = "255";
        p.weight = "6,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol";
        p.size = "0,8m";

        p = perName.get("Desseliande");
        p.evolutions = new EvolutionNode(perName.get("Brocelome"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Desseliande"), null));}});
        p.catchRate = "";
        p.weight = "71kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Plante/Indetermine";
        p.size = "1,5m";

        p = perName.get("Seviper");
        p.evolutions = null;
        p.catchRate = "90";
        p.weight = "52,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol/Dragon";
        p.size = "2,7m";

        p = perName.get("Germignon");
        p.evolutions = new EvolutionNode(perName.get("Germignon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Macronium"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Meganium"), null));}}));}});
        p.catchRate = "45";
        p.weight = "6,4kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Monstre/Plante";
        p.size = "0,9m";

        p = perName.get("Ponchiot");
        p.evolutions = new EvolutionNode(perName.get("Ponchiot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Ponchien"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Mastouffe"), null));}}));}});
        p.catchRate = "255";
        p.weight = "4,1kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol";
        p.size = "0,4m";

        p = perName.get("Typhlosion");
        p.evolutions = new EvolutionNode(perName.get("Hericendre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 14", new EvolutionNode(perName.get("Feurisson"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Typhlosion"), null));}}));}});
        p.catchRate = "45";
        p.weight = "79,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "1,7m";

        p = perName.get("Demeteros (Forme Avatar)");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "68,0kg";
        p.hatch = "120 cycles - 30855 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Sans oeuf";
        p.size = "1,5m";

        p = perName.get("Feunard");
        p.evolutions = new EvolutionNode(perName.get("Goupix"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Feu", new EvolutionNode(perName.get("Feunard"), null));}});
        p.catchRate = "75";
        p.weight = "19,9kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+1 Vit.; +1 Def. Spe";
        p.eggGroup = "Sol";
        p.size = "1,1m";

        p = perName.get("Magneti");
        p.evolutions = new EvolutionNode(perName.get("Magneti"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Magneton"), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau dans un lieu indique", new EvolutionNode(perName.get("Magnezone"), null));}}));}});
        p.catchRate = "190";
        p.weight = "6,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Mineral";
        p.size = "0,3m";

        p = perName.get("Cobaltium");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "250kg";
        p.hatch = "80 cycles - 20655 pas";
        p.gender = "Asexue";
        p.ev = "+3 Def.";
        p.eggGroup = "Sans oeuf";
        p.size = "2,1m";

        p = perName.get("Persian");
        p.evolutions = new EvolutionNode(perName.get("Miaouss"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 28", new EvolutionNode(perName.get("Persian"), null));}});
        p.catchRate = "90";
        p.weight = "32,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Nidoking");
        p.evolutions = new EvolutionNode(perName.get("Nidoran M"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Nidorino"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get("Nidoking"), null));}}));}});
        p.catchRate = "45";
        p.weight = "62,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Monstre/Sol";
        p.size = "1,4m";

        p = perName.get("Ninjask");
        p.evolutions = new EvolutionNode(perName.get("Ningale"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Ninjask"), null));this.put("Niveau 20, emplacement libre et Poke Ball dans l'inventaire", new EvolutionNode(perName.get("Munja"), null));}});
        p.catchRate = "120";
        p.weight = "12,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Insecte";
        p.size = "0,8m";

        p = perName.get("Amphinobi");
        p.evolutions = new EvolutionNode(perName.get("Grenousse"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Croaporal"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Amphinobi"), null));}}));}});
        p.catchRate = "45";
        p.weight = "40,0kg";
        p.hatch = "pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+3 Vit.";
        p.eggGroup = "Eau 1";
        p.size = "1,5m";

        p = perName.get("Nemelios");
        p.evolutions = new EvolutionNode(perName.get("Helionceau"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Nemelios"), null));}});
        p.catchRate = "";
        p.weight = "81,5kg";
        p.hatch = "pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "1,5m";

        p = perName.get("Medhyena");
        p.evolutions = new EvolutionNode(perName.get("Medhyena"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Grahyena"), null));}});
        p.catchRate = "255";
        p.weight = "13,6kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol";
        p.size = "0,5m";

        p = perName.get("Evoli");
        p.evolutions = new EvolutionNode(perName.get("Evoli"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get("Voltali"), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get("Phyllali"), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get("Mentali"), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get("Nymphali"), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Aquali"), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get("Givrali"), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get("Pyroli"), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get("Noctali"), null));}});
        p.catchRate = "45";
        p.weight = "6,5kg";
        p.hatch = "34 cycles - 8960 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Sol";
        p.size = "0,3m";

        p = perName.get("Tentacool");
        p.evolutions = new EvolutionNode(perName.get("Tentacool"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Tentacruel"), null));}});
        p.catchRate = "190";
        p.weight = "45,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Eau 3";
        p.size = "0,9m";

        p = perName.get("Kabuto");
        p.evolutions = new EvolutionNode(perName.get("Kabuto"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Kabutops"), null));}});
        p.catchRate = "45";
        p.weight = "11,5kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Eau 1/Eau 3";
        p.size = "0,5m";

        p = perName.get("Grenousse");
        p.evolutions = new EvolutionNode(perName.get("Grenousse"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Croaporal"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Amphinobi"), null));}}));}});
        p.catchRate = "45";
        p.weight = "7,0kg";
        p.hatch = "pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Eau 1";
        p.size = "0,3m";

        p = perName.get("Kaorine");
        p.evolutions = new EvolutionNode(perName.get("Balbuto"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Kaorine"), null));}});
        p.catchRate = "90";
        p.weight = "108,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+2 Vit.";
        p.eggGroup = "Mineral";
        p.size = "1,5m";

        p = perName.get("Debugant");
        p.evolutions = new EvolutionNode(perName.get("Debugant"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20, Attaque Defense", new EvolutionNode(perName.get("Tygnon"), null));this.put("Niveau 20, Attaque et Defense identiques", new EvolutionNode(perName.get("Kapoera"), null));}});
        p.catchRate = "75";
        p.weight = "21,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sans oeuf";
        p.size = "0,7m";

        p = perName.get("Ningale");
        p.evolutions = new EvolutionNode(perName.get("Ningale"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Ninjask"), null));this.put("Niveau 20, emplacement libre et Poke Ball dans l'inventaire", new EvolutionNode(perName.get("Munja"), null));}});
        p.catchRate = "255";
        p.weight = "5,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Insecte";
        p.size = "0,5m";

        p = perName.get("Capidextre");
        p.evolutions = new EvolutionNode(perName.get("Capumain"), new HashMap<String, EvolutionNode>(){{this.put("En connaissant l'attaque Coup Double + passer un niveau", new EvolutionNode(perName.get("Capidextre"), null));}});
        p.catchRate = "45";
        p.weight = "20,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "1,2m";

        p = perName.get("Tic");
        p.evolutions = new EvolutionNode(perName.get("Tic"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 38", new EvolutionNode(perName.get("Clic"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 49", new EvolutionNode(perName.get("Cliticlic"), null));}}));}});
        p.catchRate = "130";
        p.weight = "21,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "Asexue";
        p.ev = "+1 Def";
        p.eggGroup = "Mineral";
        p.size = "0,3m";

        p = perName.get("Piafabec");
        p.evolutions = new EvolutionNode(perName.get("Piafabec"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Rapasdepic"), null));}});
        p.catchRate = "255";
        p.weight = "2,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Vol";
        p.size = "0,3m";

        p = perName.get("Camerupt");
        p.evolutions = new EvolutionNode(perName.get("Chamallot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 33", new EvolutionNode(perName.get("Camerupt"), null));}});
        p.catchRate = "150";
        p.weight = "220,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.; +1 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "1,9m";

        p = perName.get("Goelise");
        p.evolutions = new EvolutionNode(perName.get("Goelise"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Bekipan"), null));}});
        p.catchRate = "190";
        p.weight = "9,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Eau 1/Vol";
        p.size = "0,6m";

        p = perName.get("Golgopathe");
        p.evolutions = new EvolutionNode(perName.get("Opermine"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 39", new EvolutionNode(perName.get("Golgopathe"), null));}});
        p.catchRate = "";
        p.weight = "96,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Eau 3/Eau 1";
        p.size = "1,3m";

        p = perName.get("Reshiram");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "330kg";
        p.hatch = "120 cycles - 30855 pas";
        p.gender = "Asexue";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "3,2m";

        p = perName.get("Excelangue");
        p.evolutions = new EvolutionNode(perName.get("Excelangue"), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l'attaque Roulade", new EvolutionNode(perName.get("Coudlangue"), null));}});
        p.catchRate = "45";
        p.weight = "65,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Monstre";
        p.size = "1,2m";

        p = perName.get("Tetarte");
        p.evolutions = new EvolutionNode(perName.get("Ptitard"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Tetarte"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Roche Royale", new EvolutionNode(perName.get("Tarpaud"), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Tartard"), null));}}));}});
        p.catchRate = "120";
        p.weight = "20,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Eau 1";
        p.size = "1,0m";

        p = perName.get("Mega-Ectoplasma");
        p.evolutions = new EvolutionNode(perName.get("Fantominus"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Spectrum"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Ectoplasma"), new HashMap<String, EvolutionNode>(){{this.put("Ectoplasmite", new EvolutionNode(perName.get("Mega-Ectoplasma"), null));}}));}}));}});
        p.catchRate = "";
        p.weight = "40,5kg";
        p.hatch = "";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,4m";

        p = perName.get("Flingouste");
        p.evolutions = new EvolutionNode(perName.get("Flingouste"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Gamblast"), null));}});
        p.catchRate = "";
        p.weight = "8,3kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Eau 1/Eau 3";
        p.size = "0,5m";

        p = perName.get("Aligatueur");
        p.evolutions = new EvolutionNode(perName.get("Kaiminus"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Crocrodil"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Aligatueur"), null));}}));}});
        p.catchRate = "45";
        p.weight = "88,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att.; +1 Def.";
        p.eggGroup = "Eau 1/Monstre";
        p.size = "2,3m";

        p = perName.get("Magireve");
        p.evolutions = new EvolutionNode(perName.get("Feuforeve"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get("Magireve"), null));}});
        p.catchRate = "45";
        p.weight = "4,4kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe;  +1 Def. Spe";
        p.eggGroup = "Indetermine";
        p.size = "0,9m";

        p = perName.get("Luxray");
        p.evolutions = new EvolutionNode(perName.get("Lixy"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 15", new EvolutionNode(perName.get("Luxio"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Luxray"), null));}}));}});
        p.catchRate = "45";
        p.weight = "42,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Sol";
        p.size = "1,4m";

        p = perName.get("Rosabyss");
        p.evolutions = new EvolutionNode(perName.get("Coquiperl"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant une Ecaille Ocean", new EvolutionNode(perName.get("Rosabyss"), null));this.put("Echange en tenant une Dent Ocean", new EvolutionNode(perName.get("Serpang"), null));}});
        p.catchRate = "60";
        p.weight = "22,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Eau 1";
        p.size = "1,8m";

        p = perName.get("Galekid");
        p.evolutions = new EvolutionNode(perName.get("Galekid"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Galegon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 42", new EvolutionNode(perName.get("Galeking"), new HashMap<String, EvolutionNode>(){{this.put("Galekingite", new EvolutionNode(perName.get("Mega-Galeking"), null));}}));}}));}});
        p.catchRate = "180";
        p.weight = "60,0kg";
        p.hatch = "34 cycles - 8960 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Monstre";
        p.size = "0,4m";

        p = perName.get("Ptera");
        p.evolutions = new EvolutionNode(perName.get("Ptera"), new HashMap<String, EvolutionNode>(){{this.put("Pteraite", new EvolutionNode(perName.get("Mega-Ptera"), null));}});
        p.catchRate = "45";
        p.weight = "59,0kg";
        p.hatch = "34 cycles - 8960 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Vol";
        p.size = "1,8m";

        p = perName.get("Mega-Ptera");
        p.evolutions = new EvolutionNode(perName.get("Ptera"), new HashMap<String, EvolutionNode>(){{this.put("Pteraite", new EvolutionNode(perName.get("Mega-Ptera"), null));}});
        p.catchRate = "";
        p.weight = "79,0kg";
        p.hatch = "";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "2,1m";

        p = perName.get("Galopa");
        p.evolutions = new EvolutionNode(perName.get("Ponyta"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Galopa"), null));}});
        p.catchRate = "60";
        p.weight = "95,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "1,7m";

        p = perName.get("Aeromite");
        p.evolutions = new EvolutionNode(perName.get("Mimitoss"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 31", new EvolutionNode(perName.get("Aeromite"), null));}});
        p.catchRate = "75";
        p.weight = "12,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe; +1 Vit.";
        p.eggGroup = "Insecte";
        p.size = "1,5m";

        p = perName.get("Pitrouille (Taille Mini)");
        p.evolutions = new EvolutionNode(perName.get("Pitrouille (Taille Mini)"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Banshitrouye (Taille Mini)"), null));}});
        p.catchRate = "";
        p.weight = "3,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Indetermine";
        p.size = "0,3m";

        p = perName.get("Marisson");
        p.evolutions = new EvolutionNode(perName.get("Marisson"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Boguerisse"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Blindepique"), null));}}));}});
        p.catchRate = "45";
        p.weight = "9,0kg";
        p.hatch = "pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Sol";
        p.size = "0,4m";

        p = perName.get("Mascaiman");
        p.evolutions = new EvolutionNode(perName.get("Mascaiman"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 29", new EvolutionNode(perName.get("Escroco"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Crocorible"), null));}}));}});
        p.catchRate = "180";
        p.weight = "15,2kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol";
        p.size = "0,7m";

        p = perName.get("Carapuce");
        p.evolutions = new EvolutionNode(perName.get("Carapuce"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Carabaffe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Tortank"), new HashMap<String, EvolutionNode>(){{this.put("Tortankite", new EvolutionNode(perName.get("Mega-Tortank"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "9,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Eau 1/Monstre";
        p.size = "0,5m";

        p = perName.get("Magneton");
        p.evolutions = new EvolutionNode(perName.get("Magneti"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Magneton"), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau dans un lieu indique", new EvolutionNode(perName.get("Magnezone"), null));}}));}});
        p.catchRate = "60";
        p.weight = "60,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Mineral";
        p.size = "1,0m";

        p = perName.get("Mangriff");
        p.evolutions = null;
        p.catchRate = "90";
        p.weight = "40,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol";
        p.size = "1,3m";

        p = perName.get("Wailmer");
        p.evolutions = new EvolutionNode(perName.get("Wailmer"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Wailord"), null));}});
        p.catchRate = "125";
        p.weight = "130,0kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Sol/Eau 2";
        p.size = "2,0m";

        p = perName.get("Grahyena");
        p.evolutions = new EvolutionNode(perName.get("Medhyena"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Grahyena"), null));}});
        p.catchRate = "127";
        p.weight = "37,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Lugia");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "216,0kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 Def. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "5,2m";

        p = perName.get("Onix");
        p.evolutions = new EvolutionNode(perName.get("Onix"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Peau Metal", new EvolutionNode(perName.get("Steelix"), null));}});
        p.catchRate = "45";
        p.weight = "210,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Mineral";
        p.size = "8,8m";

        p = perName.get("Pyroli");
        p.evolutions = new EvolutionNode(perName.get("Evoli"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get("Voltali"), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get("Phyllali"), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get("Mentali"), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get("Nymphali"), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Aquali"), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get("Givrali"), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get("Pyroli"), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get("Noctali"), null));}});
        p.catchRate = "45";
        p.weight = "25,9kg";
        p.hatch = "34 cycles - 8960 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol";
        p.size = "0,9m";

        p = perName.get("Gruikui");
        p.evolutions = new EvolutionNode(perName.get("Gruikui"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 17", new EvolutionNode(perName.get("Grotichon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Roitiflam"), null));}}));}});
        p.catchRate = "45";
        p.weight = "9,9kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 PV";
        p.eggGroup = "Sol";
        p.size = "0,5m";

        p = perName.get("Kokiyas");
        p.evolutions = new EvolutionNode(perName.get("Kokiyas"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Crustabri"), null));}});
        p.catchRate = "190";
        p.weight = "4,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Eau 3";
        p.size = "0,3m";

        p = perName.get("Racaillou");
        p.evolutions = new EvolutionNode(perName.get("Racaillou"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Gravalanch"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Grolem"), null));}}));}});
        p.catchRate = "255";
        p.weight = "20,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Mineral";
        p.size = "0,4m";

        p = perName.get("Colhomard");
        p.evolutions = new EvolutionNode(perName.get("Ecrapince"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Colhomard"), null));}});
        p.catchRate = "255";
        p.weight = "32,8kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Eau 1/Eau 3";
        p.size = "1,1m";

        p = perName.get("Papinox");
        p.evolutions = new EvolutionNode(perName.get("Chenipotte"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 10", new EvolutionNode(perName.get("Papinox"), null));this.put("Niveau 7, au hasard", new EvolutionNode(perName.get("Blindalys"), null));}});
        p.catchRate = "45";
        p.weight = "31,6kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Def. Spe";
        p.eggGroup = "Insecte";
        p.size = "1,2m";

        p = perName.get("Manaphy");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "1,4kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "Asexue";
        p.ev = "+3 PV";
        p.eggGroup = "Eau 1/Fee";
        p.size = "0,3m";

        p = perName.get("Crocrodil");
        p.evolutions = new EvolutionNode(perName.get("Kaiminus"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Crocrodil"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Aligatueur"), null));}}));}});
        p.catchRate = "45";
        p.weight = "25,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att.; +1 Def.";
        p.eggGroup = "Monstre/Eau 1";
        p.size = "1,1m";

        p = perName.get("Ectoplasma");
        p.evolutions = new EvolutionNode(perName.get("Fantominus"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Spectrum"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Ectoplasma"), new HashMap<String, EvolutionNode>(){{this.put("Ectoplasmite", new EvolutionNode(perName.get("Mega-Ectoplasma"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "40,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Indetermine";
        p.size = "1,5m";

        p = perName.get("Nucleos");
        p.evolutions = new EvolutionNode(perName.get("Nucleos"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Meios"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 41", new EvolutionNode(perName.get("Symbios"), null));}}));}});
        p.catchRate = "200";
        p.weight = "1,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Indetermine";
        p.size = "0,3m";

        p = perName.get("Vortente");
        p.evolutions = null;
        p.catchRate = "200";
        p.weight = "27,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Plante";
        p.size = "1,4m";

        p = perName.get("Ecrapince");
        p.evolutions = new EvolutionNode(perName.get("Ecrapince"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Colhomard"), null));}});
        p.catchRate = "205";
        p.weight = "11,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Eau 1/Eau 3";
        p.size = "0,6m";

        p = perName.get("Coxyclaque");
        p.evolutions = new EvolutionNode(perName.get("Coxy"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Coxyclaque"), null));}});
        p.catchRate = "90";
        p.weight = "35,6kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Insecte";
        p.size = "1,4m";

        p = perName.get("Lugulabre");
        p.evolutions = new EvolutionNode(perName.get("Funecire"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 41", new EvolutionNode(perName.get("Melancolux"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Nuit", new EvolutionNode(perName.get("Lugulabre"), null));}}));}});
        p.catchRate = "45";
        p.weight = "34,3kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Indetermine";
        p.size = "1,0m";

        p = perName.get("Moyade");
        p.evolutions = new EvolutionNode(perName.get("Viskuse"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Moyade"), null));}});
        p.catchRate = "60";
        p.weight = "135,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Indetermine";
        p.size = "2,2m";

        p = perName.get("Delcatty");
        p.evolutions = new EvolutionNode(perName.get("Skitty"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get("Delcatty"), null));}});
        p.catchRate = "60";
        p.weight = "32,6kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+1 PV; +1 Vit.";
        p.eggGroup = "Sol/Fee";
        p.size = "1,1m";

        p = perName.get("Floette");
        p.evolutions = new EvolutionNode(perName.get("Flabebe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 19", new EvolutionNode(perName.get("Floette"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get("Florges"), null));}}));}});
        p.catchRate = "";
        p.weight = "0,9kg";
        p.hatch = "pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Fee";
        p.size = "0,2m";

        p = perName.get("Tutankafer");
        p.evolutions = new EvolutionNode(perName.get("Tutafeh"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 34", new EvolutionNode(perName.get("Tutankafer"), null));}});
        p.catchRate = "90";
        p.weight = "76,5kg";
        p.hatch = "25 cycles - 6630 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Mineral/Indetermine";
        p.size = "1,7m";

        p = perName.get("Meditikka");
        p.evolutions = new EvolutionNode(perName.get("Meditikka"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Charmina"), new HashMap<String, EvolutionNode>(){{this.put("Charminite", new EvolutionNode(perName.get("Mega-Charmina"), null));}}));}});
        p.catchRate = "180";
        p.weight = "11,2kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Humanoide";
        p.size = "0,6m";

        p = perName.get("Nanmeouie");
        p.evolutions = null;
        p.catchRate = "255";
        p.weight = "31,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Fee";
        p.size = "1,1m";

        p = perName.get("Feunnec");
        p.evolutions = new EvolutionNode(perName.get("Feunnec"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Roussil"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Goupelin"), null));}}));}});
        p.catchRate = "45";
        p.weight = "9,4kg";
        p.hatch = "pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "0,4m";

        p = perName.get("Archeodong");
        p.evolutions = new EvolutionNode(perName.get("Archeomire"), new HashMap<String, EvolutionNode>(){{this.put("niveau 33", new EvolutionNode(perName.get("Archeodong"), null));}});
        p.catchRate = "90";
        p.weight = "187,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+1 Def.; +1 Def. Spe";
        p.eggGroup = "Mineral";
        p.size = "1,3m";

        p = perName.get("Axoloto");
        p.evolutions = new EvolutionNode(perName.get("Axoloto"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Maraiste"), null));}});
        p.catchRate = "255";
        p.weight = "8,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Eau 1/Sol";
        p.size = "0,4m";

        p = perName.get("Macronium");
        p.evolutions = new EvolutionNode(perName.get("Germignon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Macronium"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Meganium"), null));}}));}});
        p.catchRate = "45";
        p.weight = "15,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Def.; +1 Def. Spe";
        p.eggGroup = "Monstre/Plante";
        p.size = "1,2m";

        p = perName.get("Munna");
        p.evolutions = new EvolutionNode(perName.get("Munna"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get("Mushana"), null));}});
        p.catchRate = "190";
        p.weight = "23,3kg";
        p.hatch = "10 cycles - 2805 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Sol";
        p.size = "0,6m";

        p = perName.get("Caratroc");
        p.evolutions = null;
        p.catchRate = "190";
        p.weight = "20,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.; +1 Def. Spe";
        p.eggGroup = "Insecte";
        p.size = "0,6m";

        p = perName.get("Shaymin (Forme Celeste)");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "2,1kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "0,2m";

        p = perName.get("Ponchien");
        p.evolutions = new EvolutionNode(perName.get("Ponchiot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Ponchien"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Mastouffe"), null));}}));}});
        p.catchRate = "120";
        p.weight = "14,7kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol";
        p.size = "0,9m";

        p = perName.get("Pifeuil");
        p.evolutions = new EvolutionNode(perName.get("Grainipiot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 14", new EvolutionNode(perName.get("Pifeuil"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get("Tengalice"), null));}}));}});
        p.catchRate = "120";
        p.weight = "28,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol/Plante";
        p.size = "1,0m";

        p = perName.get("Toudoudou");
        p.evolutions = new EvolutionNode(perName.get("Toudoudou"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Rondoudou"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Lune", new EvolutionNode(perName.get("Grodoudou"), null));}}));}});
        p.catchRate = "45";
        p.weight = "1,0kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "-75% femelle; 175% male";
        p.ev = "+1 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "0,3m";

        p = perName.get("Vipelierre");
        p.evolutions = new EvolutionNode(perName.get("Vipelierre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 17", new EvolutionNode(perName.get("Lianaja"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Majaspic"), null));}}));}});
        p.catchRate = "45";
        p.weight = "8,1kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol/Plante";
        p.size = "0,6m";

        p = perName.get("Coquiperl");
        p.evolutions = new EvolutionNode(perName.get("Coquiperl"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant une Ecaille Ocean", new EvolutionNode(perName.get("Rosabyss"), null));this.put("Echange en tenant une Dent Ocean", new EvolutionNode(perName.get("Serpang"), null));}});
        p.catchRate = "255";
        p.weight = "52,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Eau 1";
        p.size = "0,4m";

        p = perName.get("Pachirisu");
        p.evolutions = null;
        p.catchRate = "200";
        p.weight = "3,9kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Fee/Sol";
        p.size = "0,4m";

        p = perName.get("Draby");
        p.evolutions = new EvolutionNode(perName.get("Draby"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Drackhaus"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 50", new EvolutionNode(perName.get("Drattak"), null));}}));}});
        p.catchRate = "45";
        p.weight = "42,1kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Dragon";
        p.size = "0,6m";

        p = perName.get("Rayquaza");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "206,5kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+2 Att.; +1 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "7,0m";

        p = perName.get("Granivol");
        p.evolutions = new EvolutionNode(perName.get("Granivol"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Floravol"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 27", new EvolutionNode(perName.get("Cotovol"), null));}}));}});
        p.catchRate = "255";
        p.weight = "0,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Fee/Plante";
        p.size = "0,4m";

        p = perName.get("Ceriflor");
        p.evolutions = new EvolutionNode(perName.get("Ceribou"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Ceriflor"), null));}});
        p.catchRate = "75";
        p.weight = "9,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Fee/Plante";
        p.size = "0,5m";

        p = perName.get("Dimoret");
        p.evolutions = new EvolutionNode(perName.get("Farfuret"), new HashMap<String, EvolutionNode>(){{this.put("Gagne un niveau de nuit en tenant une Griffe Rasoir", new EvolutionNode(perName.get("Dimoret"), null));}});
        p.catchRate = "45";
        p.weight = "34,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.; +1 Vit.";
        p.eggGroup = "Sol";
        p.size = "1,1m";

        p = perName.get("Amonita");
        p.evolutions = new EvolutionNode(perName.get("Amonita"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Amonistar"), null));}});
        p.catchRate = "45";
        p.weight = "7,5kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Eau 1/Eau 3";
        p.size = "0,4m";

        p = perName.get("Larveyette");
        p.evolutions = new EvolutionNode(perName.get("Larveyette"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Couverdure"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Manternel"), null));}}));}});
        p.catchRate = "255";
        p.weight = "2,5kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Insecte";
        p.size = "0,3m";

        p = perName.get("Krabboss");
        p.evolutions = new EvolutionNode(perName.get("Krabby"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 28", new EvolutionNode(perName.get("Krabboss"), null));}});
        p.catchRate = "60";
        p.weight = "60,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Eau 3";
        p.size = "1,3m";

        p = perName.get("Polarhume");
        p.evolutions = new EvolutionNode(perName.get("Polarhume"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Polagriffe"), null));}});
        p.catchRate = "120";
        p.weight = "8,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol";
        p.size = "0,5m";

        p = perName.get("Barloche");
        p.evolutions = new EvolutionNode(perName.get("Barloche"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Barbicha"), null));}});
        p.catchRate = "190";
        p.weight = "1,9kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Eau 2";
        p.size = "0,4m";

        p = perName.get("Hippodocus");
        p.evolutions = new EvolutionNode(perName.get("Hippopotas"), new HashMap<String, EvolutionNode>(){{this.put("niveau 34", new EvolutionNode(perName.get("Hippodocus"), null));}});
        p.catchRate = "60";
        p.weight = "300,0kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Sol";
        p.size = "2,0m";

        p = perName.get("Latias");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "40,0kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+3 Def. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "1,4m";

        p = perName.get("Magmar");
        p.evolutions = new EvolutionNode(perName.get("Magby"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Magmar"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Magmariseur", new EvolutionNode(perName.get("Maganon"), null));}}));}});
        p.catchRate = "45";
        p.weight = "44,5kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Humanoide";
        p.size = "1,3m";

        p = perName.get("Caninos");
        p.evolutions = new EvolutionNode(perName.get("Caninos"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Feu", new EvolutionNode(perName.get("Arcanin"), null));}});
        p.catchRate = "190";
        p.weight = "19,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+1 Att";
        p.eggGroup = "Sol";
        p.size = "0,7m";

        p = perName.get("Seleroc");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "168,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "Asexue";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Mineral";
        p.size = "1,0m";

        p = perName.get("Lucario");
        p.evolutions = new EvolutionNode(perName.get("Riolu"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur + gagne un niveau de jour", new EvolutionNode(perName.get("Lucario"), new HashMap<String, EvolutionNode>(){{this.put("Lucarite", new EvolutionNode(perName.get("Mega-Lucario"), null));}}));}});
        p.catchRate = "45";
        p.weight = "54,0kg";
        p.hatch = "9 cycles - 2560 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att.; +1 Att. Spe";
        p.eggGroup = "Sol/Humanoide";
        p.size = "1,2m";

        p = perName.get("Machopeur");
        p.evolutions = new EvolutionNode(perName.get("Machoc"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 28", new EvolutionNode(perName.get("Machopeur"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Mackogneur"), null));}}));}});
        p.catchRate = "90";
        p.weight = "70,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Humanoide";
        p.size = "1,5m";

        p = perName.get("Barpau");
        p.evolutions = new EvolutionNode(perName.get("Barpau"), new HashMap<String, EvolutionNode>(){{this.put("Niveau de Beaute superieur ou egal a 170 (3eme et 4eme generations) ou Echange en tenant l'objet Bel'Ecaille (5eme et 6eme generations) ou Tenir le Voile Venus (Pokemon Donjon Mystere)", new EvolutionNode(perName.get("Milobellus"), null));}});
        p.catchRate = "255";
        p.weight = "7,4kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Eau 1/Dragon";
        p.size = "0,6m";

        p = perName.get("Armulys");
        p.evolutions = new EvolutionNode(perName.get("Chenipotte"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 10", new EvolutionNode(perName.get("Papinox"), null));this.put("Niveau 7, au hasard", new EvolutionNode(perName.get("Blindalys"), null));}});
        p.catchRate = "120";
        p.weight = "10,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Insecte";
        p.size = "0,6m";

        p = perName.get("Drascore");
        p.evolutions = new EvolutionNode(perName.get("Rapion"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Drascore"), null));}});
        p.catchRate = "45";
        p.weight = "61,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Insecte/Eau 3";
        p.size = "1,3m";

        p = perName.get("Coudlangue");
        p.evolutions = new EvolutionNode(perName.get("Excelangue"), new HashMap<String, EvolutionNode>(){{this.put("En connaissant l'attaque Roulade", new EvolutionNode(perName.get("Coudlangue"), null));}});
        p.catchRate = "30";
        p.weight = "140,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Monstre";
        p.size = "1,7m";

        p = perName.get("Tarinorme");
        p.evolutions = new EvolutionNode(perName.get("Tarinor"), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau dans un lieu indique", new EvolutionNode(perName.get("Tarinorme"), null));}});
        p.catchRate = "60";
        p.weight = "340,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Mineral";
        p.size = "1,4m";

        p = perName.get("Lovdisc");
        p.evolutions = null;
        p.catchRate = "225";
        p.weight = "8,7kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Eau 2";
        p.size = "0,6m";

        p = perName.get("Saquedeneu");
        p.evolutions = new EvolutionNode(perName.get("Saquedeneu"), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l'attaque Pouv.Antique", new EvolutionNode(perName.get("Bouldeneu"), null));}});
        p.catchRate = "45";
        p.weight = "35,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Plante";
        p.size = "1,0m";

        p = perName.get("Darumarond");
        p.evolutions = new EvolutionNode(perName.get("Darumarond"), null);
        p.catchRate = "120";
        p.weight = "37,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol";
        p.size = "0,6m";

        p = perName.get("Golemastoc");
        p.evolutions = new EvolutionNode(perName.get("Gringolem"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 43", new EvolutionNode(perName.get("Golemastoc"), null));}});
        p.catchRate = "90";
        p.weight = "330,0kg";
        p.hatch = "25 cycles - 6630 pas";
        p.gender = "Asexue";
        p.ev = "+2 Att.";
        p.eggGroup = "Mineral";
        p.size = "2,8m";

        p = perName.get("Diamat");
        p.evolutions = new EvolutionNode(perName.get("Solochi"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 50", new EvolutionNode(perName.get("Diamat"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 64", new EvolutionNode(perName.get("Trioxhydre"), null));}}));}});
        p.catchRate = "190";
        p.weight = "50,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Dragon";
        p.size = "1,4m";

        p = perName.get("Phyllali");
        p.evolutions = new EvolutionNode(perName.get("Evoli"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Foudre", new EvolutionNode(perName.get("Voltali"), null));this.put("Pres d'une Pierre Mousse + gagne un niveau", new EvolutionNode(perName.get("Phyllali"), null));this.put("Bonheur , Jour", new EvolutionNode(perName.get("Mentali"), null));this.put("2 coeurs d'affection a la Poke Recre + gagne un niveau + avoir une attaque Fee", new EvolutionNode(perName.get("Nymphali"), null));this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Aquali"), null));this.put("Pres d'une Pierre Glacee + gagne un niveau", new EvolutionNode(perName.get("Givrali"), null));this.put("Avec une Pierre Feu", new EvolutionNode(perName.get("Pyroli"), null));this.put("Bonheur , Nuit", new EvolutionNode(perName.get("Noctali"), null));}});
        p.catchRate = "45";
        p.weight = "25,5kg";
        p.hatch = "34 cycles - 8960 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Mistigrix");
        p.evolutions = new EvolutionNode(perName.get("Psystigri"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Mistigrix"), null));}});
        p.catchRate = "";
        p.weight = "8,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,6m";

        p = perName.get("Balignon");
        p.evolutions = new EvolutionNode(perName.get("Balignon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 23", new EvolutionNode(perName.get("Chapignon"), null));}});
        p.catchRate = "255";
        p.weight = "4,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Fee/Plante";
        p.size = "0,4m";

        p = perName.get("Grotichon");
        p.evolutions = new EvolutionNode(perName.get("Gruikui"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 17", new EvolutionNode(perName.get("Grotichon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Roitiflam"), null));}}));}});
        p.catchRate = "45";
        p.weight = "55,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Mega-Kangourex");
        p.evolutions = new EvolutionNode(perName.get("Kangourex"), new HashMap<String, EvolutionNode>(){{this.put("Kangourexite", new EvolutionNode(perName.get("Mega-Kangourex"), null));}});
        p.catchRate = "";
        p.weight = "100,0kg";
        p.hatch = "";
        p.gender = "100% femelle; 0% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "2,2m";

        p = perName.get("Chapignon");
        p.evolutions = new EvolutionNode(perName.get("Balignon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 23", new EvolutionNode(perName.get("Chapignon"), null));}});
        p.catchRate = "90";
        p.weight = "39,2kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Fee/Plante";
        p.size = "1,2m";

        p = perName.get("Tengalice");
        p.evolutions = new EvolutionNode(perName.get("Grainipiot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 14", new EvolutionNode(perName.get("Pifeuil"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get("Tengalice"), null));}}));}});
        p.catchRate = "45";
        p.weight = "59,6kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Sol/Plante";
        p.size = "1,3m";

        p = perName.get("Ymphect");
        p.evolutions = new EvolutionNode(perName.get("Embrylex"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Ymphect"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 55", new EvolutionNode(perName.get("Tyranocif"), new HashMap<String, EvolutionNode>(){{this.put("Tyranocivite", new EvolutionNode(perName.get("Mega-Tyranocif"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "152,0kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Monstre";
        p.size = "1,2m";

        p = perName.get("Artikodin");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "55,4kg";
        p.hatch = "79 cycles - 20480 pas";
        p.gender = "Asexue";
        p.ev = "+3 Def. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "1,7m";

        p = perName.get("Phione");
        p.evolutions = null;
        p.catchRate = "30";
        p.weight = "3,1kg";
        p.hatch = "41 cycles - 10710 pas";
        p.gender = "Asexue";
        p.ev = "+1 PV";
        p.eggGroup = "Eau 1/Fee";
        p.size = "0,4m";

        p = perName.get("Miaouss");
        p.evolutions = new EvolutionNode(perName.get("Miaouss"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 28", new EvolutionNode(perName.get("Persian"), null));}});
        p.catchRate = "255";
        p.weight = "4,2kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,4m";

        p = perName.get("Braisillon");
        p.evolutions = new EvolutionNode(perName.get("Passerouge"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 17", new EvolutionNode(perName.get("Braisillon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Flambusard"), null));}}));}});
        p.catchRate = "";
        p.weight = "16,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Vol";
        p.size = "0,7m";

        p = perName.get("Scorvol");
        p.evolutions = new EvolutionNode(perName.get("Scorplane"), new HashMap<String, EvolutionNode>(){{this.put("Gagne un niveau de nuit en tenant un Croc Rasoir", new EvolutionNode(perName.get("Scorvol"), null));}});
        p.catchRate = "30";
        p.weight = "42,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Insecte";
        p.size = "2,0m";

        p = perName.get("Manzai");
        p.evolutions = new EvolutionNode(perName.get("Manzai"), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l'attaque Copie", new EvolutionNode(perName.get("Simularbre"), null));}});
        p.catchRate = "255";
        p.weight = "15,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Sans oeuf";
        p.size = "0,5m";

        p = perName.get("Nosferapti");
        p.evolutions = new EvolutionNode(perName.get("Nosferapti"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 22", new EvolutionNode(perName.get("Nosferalto"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Nostenfer"), null));}}));}});
        p.catchRate = "255";
        p.weight = "7,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Vol";
        p.size = "0,8m";

        p = perName.get("Arakdo");
        p.evolutions = new EvolutionNode(perName.get("Arakdo"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 22", new EvolutionNode(perName.get("Maskadra"), null));}});
        p.catchRate = "200";
        p.weight = "1,7kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Eau 1/Insecte";
        p.size = "0,5m";

        p = perName.get("Kaiminus");
        p.evolutions = new EvolutionNode(perName.get("Kaiminus"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Crocrodil"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Aligatueur"), null));}}));}});
        p.catchRate = "45";
        p.weight = "9,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Monstre/Eau 1";
        p.size = "0,6m";

        p = perName.get("Charmillon");
        p.evolutions = new EvolutionNode(perName.get("Chenipotte"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 10", new EvolutionNode(perName.get("Papinox"), null));this.put("Niveau 7, au hasard", new EvolutionNode(perName.get("Blindalys"), null));}});
        p.catchRate = "45";
        p.weight = "28,4kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Insecte";
        p.size = "1,0m";

        p = perName.get("Zebibron");
        p.evolutions = new EvolutionNode(perName.get("Zebibron"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 27", new EvolutionNode(perName.get("Zeblitz"), null));}});
        p.catchRate = "190";
        p.weight = "29,8kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,8m";

        p = perName.get("Coupenotte");
        p.evolutions = new EvolutionNode(perName.get("Coupenotte"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 38", new EvolutionNode(perName.get("Incisache"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 48", new EvolutionNode(perName.get("Tranchodon"), null));}}));}});
        p.catchRate = "75";
        p.weight = "18,0kg";
        p.hatch = "40 cycles - 10455 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Monstre/Dragon";
        p.size = "0,6m";

        p = perName.get("Mygavolt");
        p.evolutions = new EvolutionNode(perName.get("Statitik"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Mygavolt"), null));}});
        p.catchRate = "75";
        p.weight = "14,3kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Insecte";
        p.size = "0,8m";

        p = perName.get("Cizayox");
        p.evolutions = new EvolutionNode(perName.get("Insecateur"), new HashMap<String, EvolutionNode>(){{this.put("Echange en tenant Peau Metal", new EvolutionNode(perName.get("Cizayox"), new HashMap<String, EvolutionNode>(){{this.put("Mega-Evolution", new EvolutionNode(perName.get("Mega-Cizayox"), null));}}));}});
        p.catchRate = "25";
        p.weight = "118,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Insecte";
        p.size = "1,8m";

        p = perName.get("Triopikeur");
        p.evolutions = new EvolutionNode(perName.get("Taupiqueur"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 26", new EvolutionNode(perName.get("Triopikeur"), null));}});
        p.catchRate = "50";
        p.weight = "33,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,7m";

        p = perName.get("Luxio");
        p.evolutions = new EvolutionNode(perName.get("Lixy"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 15", new EvolutionNode(perName.get("Luxio"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Luxray"), null));}}));}});
        p.catchRate = "120";
        p.weight = "30,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol";
        p.size = "0,9m";

        p = perName.get("Ouvrifier");
        p.evolutions = new EvolutionNode(perName.get("Charpenti"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Ouvrifier"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Betochef"), null));}}));}});
        p.catchRate = "90";
        p.weight = "40,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Humanoide";
        p.size = "1,2m";

        p = perName.get("Darkrai");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "50,5kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+1 Vit.; +2 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "1,5m";

        p = perName.get("Mew");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "4,0kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "0,4m";

        p = perName.get("Grindur");
        p.evolutions = new EvolutionNode(perName.get("Grindur"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Noacier"), null));}});
        p.catchRate = "255";
        p.weight = "18,8kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Plante/Mineral";
        p.size = "0,6m";

        p = perName.get("Prinplouf");
        p.evolutions = new EvolutionNode(perName.get("Tiplouf"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Prinplouf"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Pingoleon"), null));}}));}});
        p.catchRate = "45";
        p.weight = "23,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Eau 1/Sol";
        p.size = "0,8m";

        p = perName.get("Donphan");
        p.evolutions = new EvolutionNode(perName.get("Phanpy"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Donphan"), null));}});
        p.catchRate = "60";
        p.weight = "120,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.; +1 Def.";
        p.eggGroup = "Sol";
        p.size = "1,1m";

        p = perName.get("Kravarech");
        p.evolutions = new EvolutionNode(perName.get("Venalgue"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 48", new EvolutionNode(perName.get("Kravarech"), null));}});
        p.catchRate = "";
        p.weight = "81,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Eau 1/Dragon";
        p.size = "1,8m";

        p = perName.get("Batracne");
        p.evolutions = new EvolutionNode(perName.get("Tritonde"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Batracne"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Crapustule"), null));}}));}});
        p.catchRate = "120";
        p.weight = "17,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Eau 1";
        p.size = "0,8m";

        p = perName.get("Xerneas");
        p.evolutions = null;
        p.catchRate = "30";
        p.weight = "215,0kg";
        p.hatch = "pas";
        p.gender = "Asexue";
        p.ev = "+3 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "3,0m";

        p = perName.get("Cadoizo");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "16,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Eau 1/Sol";
        p.size = "0,9m";

        p = perName.get("Salameche");
        p.evolutions = new EvolutionNode(perName.get("Salameche"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Reptincel"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Dracaufeu"), new HashMap<String, EvolutionNode>(){{this.put("Dracaufite X", new EvolutionNode(perName.get("Mega-Dracaufeu X"), null));this.put("Dracaufite Y", new EvolutionNode(perName.get("Mega-Dracaufeu Y"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "8,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Dragon/Monstre";
        p.size = "0,6m";

        p = perName.get("Victini");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "4kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "0,4m";

        p = perName.get("Lanturn");
        p.evolutions = new EvolutionNode(perName.get("Loupio"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 27", new EvolutionNode(perName.get("Lanturn"), null));}});
        p.catchRate = "75";
        p.weight = "22,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Eau 2";
        p.size = "1,2m";

        p = perName.get("Simiabraz");
        p.evolutions = new EvolutionNode(perName.get("Ouisticram"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 14", new EvolutionNode(perName.get("Chimpenfeu"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Simiabraz"), null));}}));}});
        p.catchRate = "45";
        p.weight = "55kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att.; +1 Att. Spe; +1 Vit.";
        p.eggGroup = "Sol/Humanoide";
        p.size = "1,2m";

        p = perName.get("Bruyverne");
        p.evolutions = new EvolutionNode(perName.get("Sonistrelle"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 48", new EvolutionNode(perName.get("Bruyverne"), null));}});
        p.catchRate = "";
        p.weight = "85,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Vol";
        p.size = "1,5m";

        p = perName.get("Mucuscule");
        p.evolutions = new EvolutionNode(perName.get("Mucuscule"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Colimucus"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 50, quand il pleut", new EvolutionNode(perName.get("Muplodocus"), null));}}));}});
        p.catchRate = "";
        p.weight = "2,8kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Dragon";
        p.size = "0,3m";

        p = perName.get("Couaneton");
        p.evolutions = new EvolutionNode(perName.get("Couaneton"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Lakmecygne"), null));}});
        p.catchRate = "190";
        p.weight = "5,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Eau 1/Vol";
        p.size = "0,5m";

        p = perName.get("Aeropteryx");
        p.evolutions = new EvolutionNode(perName.get("Arkeapti"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Aeropteryx"), null));}});
        p.catchRate = "45";
        p.weight = "32,0kg";
        p.hatch = "30 cycles - 7905 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Vol/Eau 3";
        p.size = "1,4m";

        p = perName.get("Farfuret");
        p.evolutions = new EvolutionNode(perName.get("Farfuret"), new HashMap<String, EvolutionNode>(){{this.put("Gagne un niveau de nuit en tenant une Griffe Rasoir", new EvolutionNode(perName.get("Dimoret"), null));}});
        p.catchRate = "60";
        p.weight = "28,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,9m";

        p = perName.get("Cotovol");
        p.evolutions = new EvolutionNode(perName.get("Granivol"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Floravol"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 27", new EvolutionNode(perName.get("Cotovol"), null));}}));}});
        p.catchRate = "45";
        p.weight = "3,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Vit.";
        p.eggGroup = "Fee/Plante";
        p.size = "0,8m";

        p = perName.get("Obalie");
        p.evolutions = new EvolutionNode(perName.get("Obalie"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Phogleur"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 44", new EvolutionNode(perName.get("Kaimorse"), null));}}));}});
        p.catchRate = "255";
        p.weight = "39,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Eau 1/Sol";
        p.size = "0,8m";

        p = perName.get("Sorboul");
        p.evolutions = new EvolutionNode(perName.get("Sorbebe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Sorboul"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 47", new EvolutionNode(perName.get("Sorbouboul"), null));}}));}});
        p.catchRate = "120";
        p.weight = "41,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Mineral";
        p.size = "1,1m";

        p = perName.get("Pyrax");
        p.evolutions = new EvolutionNode(perName.get("Pyronille"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 59", new EvolutionNode(perName.get("Pyrax"), null));}});
        p.catchRate = "15";
        p.weight = "46kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Insecte";
        p.size = "1,6m";

        p = perName.get("Clic");
        p.evolutions = new EvolutionNode(perName.get("Tic"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 38", new EvolutionNode(perName.get("Clic"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 49", new EvolutionNode(perName.get("Cliticlic"), null));}}));}});
        p.catchRate = "60";
        p.weight = "51,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "Asexue";
        p.ev = "+2 Def0";
        p.eggGroup = "Mineral";
        p.size = "0,6m";

        p = perName.get("Oniglali");
        p.evolutions = new EvolutionNode(perName.get("Stalgamin"), new HashMap<String, EvolutionNode>(){{this.put("Femelle + Pierre Aube", new EvolutionNode(perName.get("Momartik"), null));this.put("Niveau 42", new EvolutionNode(perName.get("Oniglali"), null));}});
        p.catchRate = "75";
        p.weight = "256,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Fee/Mineral";
        p.size = "1,5m";

        p = perName.get("Deoxys (Forme Defense)");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "60,8kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att.; +1 Att. Spe; +1 Vit.";
        p.eggGroup = "Sans oeuf";
        p.size = "1,7m";

        p = perName.get("Viskuse");
        p.evolutions = new EvolutionNode(perName.get("Viskuse"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Moyade"), null));}});
        p.catchRate = "190";
        p.weight = "33,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Indetermine";
        p.size = "1,2m";

        p = perName.get("Metamorph");
        p.evolutions = null;
        p.catchRate = "35";
        p.weight = "4,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "Asexue";
        p.ev = "+1 PV";
        p.eggGroup = "Metamorph";
        p.size = "0,3m";

        p = perName.get("Kangourex");
        p.evolutions = new EvolutionNode(perName.get("Kangourex"), new HashMap<String, EvolutionNode>(){{this.put("Kangourexite", new EvolutionNode(perName.get("Mega-Kangourex"), null));}});
        p.catchRate = "45";
        p.weight = "80,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+2 PV";
        p.eggGroup = "Monstre";
        p.size = "2,2m";

        p = perName.get("Pitrouille (Taille Normale)");
        p.evolutions = new EvolutionNode(perName.get("Pitrouille (Taille Normale)"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Banshitrouye (Taille Normale)"), null));}});
        p.catchRate = "";
        p.weight = "3,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Indetermine";
        p.size = "0,3m";

        p = perName.get("Wailord");
        p.evolutions = new EvolutionNode(perName.get("Wailmer"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Wailord"), null));}});
        p.catchRate = "60";
        p.weight = "398,0kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Sol/Eau 2";
        p.size = "14,5m";

        p = perName.get("Colossinge");
        p.evolutions = new EvolutionNode(perName.get("Ferosinge"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 28", new EvolutionNode(perName.get("Colossinge"), null));}});
        p.catchRate = "75";
        p.weight = "32,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Mega-Tortank");
        p.evolutions = new EvolutionNode(perName.get("Carapuce"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Carabaffe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Tortank"), new HashMap<String, EvolutionNode>(){{this.put("Tortankite", new EvolutionNode(perName.get("Mega-Tortank"), null));}}));}}));}});
        p.catchRate = "";
        p.weight = "101,1kg";
        p.hatch = "";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,6m";

        p = perName.get("Corayon");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "5,0kg";
        p.hatch = "20 cycles - 5376 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+1 Def.; +1 Def. Spe";
        p.eggGroup = "Eau 1/Eau 3";
        p.size = "0,6m";

        p = perName.get("Mackogneur");
        p.evolutions = new EvolutionNode(perName.get("Machoc"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 28", new EvolutionNode(perName.get("Machopeur"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Mackogneur"), null));}}));}});
        p.catchRate = "45";
        p.weight = "130,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Humanoide";
        p.size = "1,6m";

        p = perName.get("Blizzaroi");
        p.evolutions = new EvolutionNode(perName.get("Blizzi"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Blizzaroi"), new HashMap<String, EvolutionNode>(){{this.put("Blizzarite", new EvolutionNode(perName.get("Mega-Blizzaroi"), null));}}));}});
        p.catchRate = "60";
        p.weight = "135,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.; +1 Att. Spe";
        p.eggGroup = "Monstre/Plante";
        p.size = "2,2m";

        p = perName.get("Feuiloutan");
        p.evolutions = new EvolutionNode(perName.get("Feuillajou"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get("Feuiloutan"), null));}});
        p.catchRate = "75";
        p.weight = "30,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "1,1m";

        p = perName.get("Ursaring");
        p.evolutions = new EvolutionNode(perName.get("Teddiursa"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Ursaring"), null));}});
        p.catchRate = "60";
        p.weight = "125,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol";
        p.size = "1,8m";

        p = perName.get("Anorith");
        p.evolutions = new EvolutionNode(perName.get("Anorith"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Armaldo"), null));}});
        p.catchRate = "45";
        p.weight = "12,5kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Eau 3";
        p.size = "0,7m";

        p = perName.get("Escroco");
        p.evolutions = new EvolutionNode(perName.get("Mascaiman"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 29", new EvolutionNode(perName.get("Escroco"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Crocorible"), null));}}));}});
        p.catchRate = "90";
        p.weight = "33,4kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Gardevoir");
        p.evolutions = new EvolutionNode(perName.get("Tarsal"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Kirlia"), new HashMap<String, EvolutionNode>(){{this.put("Male + Pierre Aube", new EvolutionNode(perName.get("Gallame"), null));this.put("Niveau 30", new EvolutionNode(perName.get("Gardevoir"), new HashMap<String, EvolutionNode>(){{this.put("Gardevoirite", new EvolutionNode(perName.get("Mega-Gardevoir"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "48,4kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Indetermine";
        p.size = "1,6m";

        p = perName.get("Scarhino");
        p.evolutions = new EvolutionNode(perName.get("Scarhino"), new HashMap<String, EvolutionNode>(){{this.put("Scarhinoite", new EvolutionNode(perName.get("Mega-Scarhino"), null));}});
        p.catchRate = "45";
        p.weight = "54,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Insecte";
        p.size = "1,5m";

        p = perName.get("Demolosse");
        p.evolutions = new EvolutionNode(perName.get("Malosse"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 24", new EvolutionNode(perName.get("Demolosse"), new HashMap<String, EvolutionNode>(){{this.put("Demolossite", new EvolutionNode(perName.get("Mega-Demolosse"), null));}}));}});
        p.catchRate = "4";
        p.weight = "35,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "1,4m";

        p = perName.get("Crapustule");
        p.evolutions = new EvolutionNode(perName.get("Tritonde"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Batracne"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Crapustule"), null));}}));}});
        p.catchRate = "45";
        p.weight = "62,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 PV";
        p.eggGroup = "Eau 1";
        p.size = "1,5m";

        p = perName.get("Crabaraque");
        p.evolutions = new EvolutionNode(perName.get("Crabicoque"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 34", new EvolutionNode(perName.get("Crabaraque"), null));}});
        p.catchRate = "75";
        p.weight = "200,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Insecte/Mineral";
        p.size = "1,4m";

        p = perName.get("Tranchodon");
        p.evolutions = new EvolutionNode(perName.get("Coupenotte"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 38", new EvolutionNode(perName.get("Incisache"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 48", new EvolutionNode(perName.get("Tranchodon"), null));}}));}});
        p.catchRate = "45";
        p.weight = "105,5kg";
        p.hatch = "40 cycles - 10455 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Monstre/Dragon";
        p.size = "1,8m";

        p = perName.get("Mewtwo");
        p.evolutions = new EvolutionNode(perName.get("Mewtwo"), new HashMap<String, EvolutionNode>(){{this.put("Mewtwoite X", new EvolutionNode(perName.get("Mega-Mewtwo X"), null));this.put("Mewtwoite Y", new EvolutionNode(perName.get("Mega-Mewtwo Y"), null));}});
        p.catchRate = "3";
        p.weight = "122,0kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "2,0m";

        p = perName.get("Feurisson");
        p.evolutions = new EvolutionNode(perName.get("Hericendre"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 14", new EvolutionNode(perName.get("Feurisson"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Typhlosion"), null));}}));}});
        p.catchRate = "45";
        p.weight = "19kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+1 Att. Spe, +1 Def. Spe";
        p.eggGroup = "Sol";
        p.size = "0,9m";

        p = perName.get("Galeking");
        p.evolutions = new EvolutionNode(perName.get("Galekid"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Galegon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 42", new EvolutionNode(perName.get("Galeking"), new HashMap<String, EvolutionNode>(){{this.put("Galekingite", new EvolutionNode(perName.get("Mega-Galeking"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "360,0kg";
        p.hatch = "34 cycles - 8960 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Def.";
        p.eggGroup = "Monstre";
        p.size = "2,1m";

        p = perName.get("Miradar");
        p.evolutions = new EvolutionNode(perName.get("Ratentif"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Miradar"), null));}});
        p.catchRate = "255";
        p.weight = "27kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Sol";
        p.size = "1,1m";

        p = perName.get("Tyranocif");
        p.evolutions = new EvolutionNode(perName.get("Embrylex"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Ymphect"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 55", new EvolutionNode(perName.get("Tyranocif"), new HashMap<String, EvolutionNode>(){{this.put("Tyranocivite", new EvolutionNode(perName.get("Mega-Tyranocif"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "202,0kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Monstre";
        p.size = "2,0m";

        p = perName.get("Migalos");
        p.evolutions = new EvolutionNode(perName.get("Mimigal"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 22", new EvolutionNode(perName.get("Migalos"), null));}});
        p.catchRate = "90";
        p.weight = "33,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Insecte";
        p.size = "1,1m";

        p = perName.get("Demanta");
        p.evolutions = new EvolutionNode(perName.get("Babimanta"), new HashMap<String, EvolutionNode>(){{this.put("Gain de niveau avec Remoraid dans l'equipe", new EvolutionNode(perName.get("Demanta"), null));}});
        p.catchRate = "25";
        p.weight = "220,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Eau 1";
        p.size = "2,1m";

        p = perName.get("Solaroc");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "154,0kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "Asexue";
        p.ev = "+2 Att.";
        p.eggGroup = "Mineral";
        p.size = "1,2m";

        p = perName.get("Passerouge");
        p.evolutions = new EvolutionNode(perName.get("Passerouge"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 17", new EvolutionNode(perName.get("Braisillon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Flambusard"), null));}}));}});
        p.catchRate = "";
        p.weight = "1,7kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Vol";
        p.size = "0,3m";

        p = perName.get("Mega-Scarhino");
        p.evolutions = new EvolutionNode(perName.get("Scarhino"), new HashMap<String, EvolutionNode>(){{this.put("Scarhinoite", new EvolutionNode(perName.get("Mega-Scarhino"), null));}});
        p.catchRate = "";
        p.weight = "62,5kg";
        p.hatch = "";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,7m";

        p = perName.get("Flobio");
        p.evolutions = new EvolutionNode(perName.get("Gobou"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Flobio"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Laggron"), null));}}));}});
        p.catchRate = "45";
        p.weight = "28,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Monstre/Eau 1";
        p.size = "0,7m";

        p = perName.get("Cochignon");
        p.evolutions = new EvolutionNode(perName.get("Marcacrin"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 33", new EvolutionNode(perName.get("Cochignon"), new HashMap<String, EvolutionNode>(){{this.put("En connaissant l'attaque Pouv.Antique", new EvolutionNode(perName.get("Mammochon"), null));}}));}});
        p.catchRate = "75";
        p.weight = "55,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV; +1 Att.";
        p.eggGroup = "Sol";
        p.size = "1,1m";

        p = perName.get("Roserade");
        p.evolutions = new EvolutionNode(perName.get("Rozbouton"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur , Jour", new EvolutionNode(perName.get("Roselia"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get("Roserade"), null));}}));}});
        p.catchRate = "75";
        p.weight = "14,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Fee/Plante";
        p.size = "0,9m";

        p = perName.get("Chamallot");
        p.evolutions = new EvolutionNode(perName.get("Chamallot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 33", new EvolutionNode(perName.get("Camerupt"), null));}});
        p.catchRate = "255";
        p.weight = "24,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Sol";
        p.size = "0,7m";

        p = perName.get("Chacripan");
        p.evolutions = new EvolutionNode(perName.get("Chacripan"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Leopardus"), null));}});
        p.catchRate = "255";
        p.weight = "10,1kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,4m";

        p = perName.get("Fulguris (Forme Avatar)");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "65kg";
        p.hatch = "120 cycles - 30855 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "1,5m";

        p = perName.get("Scrutella");
        p.evolutions = new EvolutionNode(perName.get("Scrutella"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Mesmerella"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 41", new EvolutionNode(perName.get("Siderella"), null));}}));}});
        p.catchRate = "200";
        p.weight = "5,8kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "75% femelle; 25% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Humanoide";
        p.size = "0,4m";

        p = perName.get("Blindalys");
        p.evolutions = new EvolutionNode(perName.get("Chenipotte"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 10", new EvolutionNode(perName.get("Papinox"), null));this.put("Niveau 7, au hasard", new EvolutionNode(perName.get("Blindalys"), null));}});
        p.catchRate = "120";
        p.weight = "11,5kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Insecte";
        p.size = "0,7m";

        p = perName.get("Momartik");
        p.evolutions = new EvolutionNode(perName.get("Stalgamin"), new HashMap<String, EvolutionNode>(){{this.put("Femelle + Pierre Aube", new EvolutionNode(perName.get("Momartik"), null));this.put("Niveau 42", new EvolutionNode(perName.get("Oniglali"), null));}});
        p.catchRate = "75";
        p.weight = "26,6kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Fee/Mineral";
        p.size = "1,3m";

        p = perName.get("Leopardus");
        p.evolutions = new EvolutionNode(perName.get("Chacripan"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Leopardus"), null));}});
        p.catchRate = "90";
        p.weight = "37,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "1,1m";

        p = perName.get("Ho-Oh");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "199,0kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 Def. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "3,8m";

        p = perName.get("Krabby");
        p.evolutions = new EvolutionNode(perName.get("Krabby"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 28", new EvolutionNode(perName.get("Krabboss"), null));}});
        p.catchRate = "225";
        p.weight = "6,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Eau 3";
        p.size = "0,4m";

        p = perName.get("Frison");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "94,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol";
        p.size = "1,6m";

        p = perName.get("Zeblitz");
        p.evolutions = new EvolutionNode(perName.get("Zebibron"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 27", new EvolutionNode(perName.get("Zeblitz"), null));}});
        p.catchRate = "75";
        p.weight = "79,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "1,6m";

        p = perName.get("Excavarenne");
        p.evolutions = new EvolutionNode(perName.get("Sapereau"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Excavarenne"), null));}});
        p.catchRate = "5";
        p.weight = "42,4kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Sol";
        p.size = "1,0m";

        p = perName.get("Nosferalto");
        p.evolutions = new EvolutionNode(perName.get("Nosferapti"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 22", new EvolutionNode(perName.get("Nosferalto"), new HashMap<String, EvolutionNode>(){{this.put("Bonheur", new EvolutionNode(perName.get("Nostenfer"), null));}}));}});
        p.catchRate = "90";
        p.weight = "55,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Vol";
        p.size = "1,6m";

        p = perName.get("Grelacon");
        p.evolutions = new EvolutionNode(perName.get("Grelacon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Seracrawl"), null));}});
        p.catchRate = "";
        p.weight = "99,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Monstre";
        p.size = "1,0m";

        p = perName.get("Pitrouille (Taille Ultra)");
        p.evolutions = new EvolutionNode(perName.get("Pitrouille (Taille Ultra)"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Banshitrouye (Taille Ultra)"), null));}});
        p.catchRate = "";
        p.weight = "3,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Indetermine";
        p.size = "0,3m";

        p = perName.get("Blizzi");
        p.evolutions = new EvolutionNode(perName.get("Blizzi"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Blizzaroi"), new HashMap<String, EvolutionNode>(){{this.put("Blizzarite", new EvolutionNode(perName.get("Mega-Blizzaroi"), null));}}));}});
        p.catchRate = "120";
        p.weight = "50,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Monstre/Plante";
        p.size = "1,0m";

        p = perName.get("Mega-Absol");
        p.evolutions = new EvolutionNode(perName.get("Absol"), new HashMap<String, EvolutionNode>(){{this.put("Absolite", new EvolutionNode(perName.get("Mega-Absol"), null));}});
        p.catchRate = "";
        p.weight = "49,0kg";
        p.hatch = "";
        p.gender = "100% femelle; 0% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,2m";

        p = perName.get("Strassie");
        p.evolutions = null;
        p.catchRate = "";
        p.weight = "5,7kg";
        p.hatch = "pas";
        p.gender = "Asexue";
        p.ev = "+1 Def.; +1 Def. Spe";
        p.eggGroup = "Fee/Mineral";
        p.size = "0,3m";

        p = perName.get("Trousselin");
        p.evolutions = null;
        p.catchRate = "";
        p.weight = "3,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Mineral";
        p.size = "0,2m";

        p = perName.get("Morpheo");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "0,8kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Fee/Indetermine";
        p.size = "0,3m";

        p = perName.get("Roucoups");
        p.evolutions = new EvolutionNode(perName.get("Roucool"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Roucoups"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Roucarnage"), null));}}));}});
        p.catchRate = "120";
        p.weight = "30,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Vol";
        p.size = "1,1m";

        p = perName.get("M. Mime");
        p.evolutions = new EvolutionNode(perName.get("Mime Jr."), new HashMap<String, EvolutionNode>(){{this.put("En apprenant l'attaque Copie", new EvolutionNode(perName.get("M. Mime"), null));}});
        p.catchRate = "45";
        p.weight = "54,5kg";
        p.hatch = "24 cycles - 6400 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Humanoide";
        p.size = "1,3m";

        p = perName.get("Natu");
        p.evolutions = new EvolutionNode(perName.get("Natu"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Xatu"), null));}});
        p.catchRate = "190";
        p.weight = "2,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Vol";
        p.size = "0,2m";

        p = perName.get("Spectrum");
        p.evolutions = new EvolutionNode(perName.get("Fantominus"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 25", new EvolutionNode(perName.get("Spectrum"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Ectoplasma"), new HashMap<String, EvolutionNode>(){{this.put("Ectoplasmite", new EvolutionNode(perName.get("Mega-Ectoplasma"), null));}}));}}));}});
        p.catchRate = "90";
        p.weight = "0,1kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Indetermine";
        p.size = "1,6m";

        p = perName.get("Lainergie");
        p.evolutions = new EvolutionNode(perName.get("Wattouat"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 15", new EvolutionNode(perName.get("Lainergie"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Pharamp"), new HashMap<String, EvolutionNode>(){{this.put("Pharampite", new EvolutionNode(perName.get("Mega-Pharamp"), null));}}));}}));}});
        p.catchRate = "120";
        p.weight = "13,3kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att. Spe";
        p.eggGroup = "Sol/Monstre";
        p.size = "0,8m";

        p = perName.get("Elecsprint");
        p.evolutions = new EvolutionNode(perName.get("Dynavolt"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 26", new EvolutionNode(perName.get("Elecsprint"), new HashMap<String, EvolutionNode>(){{this.put("Mega-Evolution", new EvolutionNode(perName.get("Mega-Elecsprint"), null));}}));}});
        p.catchRate = "45";
        p.weight = "40,2kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Vit.";
        p.eggGroup = "Sol";
        p.size = "1,5m";

        p = perName.get("Mega-Carchacrok");
        p.evolutions = new EvolutionNode(perName.get("Griknot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 24", new EvolutionNode(perName.get("Carmache"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 48", new EvolutionNode(perName.get("Carchacrok"), new HashMap<String, EvolutionNode>(){{this.put("Carchacrokite", new EvolutionNode(perName.get("Mega-Carchacrok"), null));}}));}}));}});
        p.catchRate = "";
        p.weight = "95,0kg";
        p.hatch = "";
        p.gender = "50% femelle; 50% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,9m";

        p = perName.get("Coxy");
        p.evolutions = new EvolutionNode(perName.get("Coxy"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 18", new EvolutionNode(perName.get("Coxyclaque"), null));}});
        p.catchRate = "255";
        p.weight = "10,8kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Insecte";
        p.size = "1,0m";

        p = perName.get("Shaymin (Forme Terrestre)");
        p.evolutions = null;
        p.catchRate = "45";
        p.weight = "2,1kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 PV";
        p.eggGroup = "Sans oeuf";
        p.size = "0,2m";

        p = perName.get("Banshitrouye (Taille Maxi)");
        p.evolutions = new EvolutionNode(perName.get("Pitrouille (Taille Maxi)"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Banshitrouye (Taille Maxi)"), null));}});
        p.catchRate = "";
        p.weight = "9,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Indetermine";
        p.size = "0,7m";

        p = perName.get("Kyogre");
        p.evolutions = null;
        p.catchRate = "5";
        p.weight = "352,0kg";
        p.hatch = "119 cycles - 30720 pas";
        p.gender = "Asexue";
        p.ev = "+3 Att. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "4,5m";

        p = perName.get("Smogo");
        p.evolutions = new EvolutionNode(perName.get("Smogo"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Smogogo"), null));}});
        p.catchRate = "190";
        p.weight = "1,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Def.";
        p.eggGroup = "Indetermine";
        p.size = "0,6m";

        p = perName.get("Arcanin");
        p.evolutions = new EvolutionNode(perName.get("Caninos"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Feu", new EvolutionNode(perName.get("Arcanin"), null));}});
        p.catchRate = "75";
        p.weight = "155,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol";
        p.size = "1,9m";

        p = perName.get("Milobellus");
        p.evolutions = new EvolutionNode(perName.get("Barpau"), new HashMap<String, EvolutionNode>(){{this.put("Niveau de Beaute superieur ou egal a 170 (3eme et 4eme generations) ou Echange en tenant l'objet Bel'Ecaille (5eme et 6eme generations) ou Tenir le Voile Venus (Pokemon Donjon Mystere)", new EvolutionNode(perName.get("Milobellus"), null));}});
        p.catchRate = "60";
        p.weight = "162,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Dragon/Eau 1";
        p.size = "6,2m";

        p = perName.get("Taupiqueur");
        p.evolutions = new EvolutionNode(perName.get("Taupiqueur"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 26", new EvolutionNode(perName.get("Triopikeur"), null));}});
        p.catchRate = "255";
        p.weight = "0,8kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,2m";

        p = perName.get("Capumain");
        p.evolutions = new EvolutionNode(perName.get("Capumain"), new HashMap<String, EvolutionNode>(){{this.put("En connaissant l'attaque Coup Double", new EvolutionNode(perName.get("Capidextre"), null));}});
        p.catchRate = "45";
        p.weight = "11,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Sol";
        p.size = "0,8m";

        p = perName.get("Machoc");
        p.evolutions = new EvolutionNode(perName.get("Machoc"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 28", new EvolutionNode(perName.get("Machopeur"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Mackogneur"), null));}}));}});
        p.catchRate = "180";
        p.weight = "19,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "25% femelle; 75% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Humanoide";
        p.size = "0,8m";

        p = perName.get("Ludicolo");
        p.evolutions = new EvolutionNode(perName.get("Nenupiot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 14", new EvolutionNode(perName.get("Lombre"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eau", new EvolutionNode(perName.get("Ludicolo"), null));}}));}});
        p.catchRate = "45";
        p.weight = "55,0kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Def. Spe";
        p.eggGroup = "Eau 1/Plante";
        p.size = "1,5m";

        p = perName.get("Noarfang");
        p.evolutions = new EvolutionNode(perName.get("Hoot-hoot"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 20", new EvolutionNode(perName.get("Noarfang"), null));}});
        p.catchRate = "90";
        p.weight = "40,8kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Vol";
        p.size = "1,6m";

        p = perName.get("Meloetta (Forme Danse)");
        p.evolutions = null;
        p.catchRate = "5";
        p.weight = "6,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att. Spe; +1 Def. Spe; +1 Vit.";
        p.eggGroup = "Sans oeuf";
        p.size = "0,6m";

        p = perName.get("Sepiatop");
        p.evolutions = new EvolutionNode(perName.get("Sepiatop"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30, en retournant la 3DS", new EvolutionNode(perName.get("Sepiatroce"), null));}});
        p.catchRate = "";
        p.weight = "3,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att.";
        p.eggGroup = "Eau 1/Eau 2";
        p.size = "0,4m";

        p = perName.get("Fermite");
        p.evolutions = null;
        p.catchRate = "90";
        p.weight = "33,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Insecte";
        p.size = "0,3m";

        p = perName.get("Regice");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "175,0kg";
        p.hatch = "79 cycles - 20480 pas";
        p.gender = "Asexue";
        p.ev = "+3 Def. Spe";
        p.eggGroup = "Sans oeuf";
        p.size = "1,8m";

        p = perName.get("Armaldo");
        p.evolutions = new EvolutionNode(perName.get("Anorith"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Armaldo"), null));}});
        p.catchRate = "45";
        p.weight = "68,2kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Eau 3";
        p.size = "1,5m";

        p = perName.get("Lewsor");
        p.evolutions = new EvolutionNode(perName.get("Lewsor"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 42", new EvolutionNode(perName.get("Neitram"), null));}});
        p.catchRate = "255";
        p.weight = "9,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Humanoide";
        p.size = "0,5m";

        p = perName.get("Sorbebe");
        p.evolutions = new EvolutionNode(perName.get("Sorbebe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 35", new EvolutionNode(perName.get("Sorboul"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 47", new EvolutionNode(perName.get("Sorbouboul"), null));}}));}});
        p.catchRate = "255";
        p.weight = "5,7kg";
        p.hatch = "13 cycles - 3533 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Att. Spe";
        p.eggGroup = "Mineral";
        p.size = "0,4m";

        p = perName.get("Demeteros (Forme Totemique)");
        p.evolutions = null;
        p.catchRate = "3";
        p.weight = "68,0kg";
        p.hatch = "120 cycles - 30855 pas";
        p.gender = "0% femelle; 100% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Sans oeuf";
        p.size = "1,5m";

        p = perName.get("Trompignon");
        p.evolutions = new EvolutionNode(perName.get("Trompignon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 39", new EvolutionNode(perName.get("Gaulet"), null));}});
        p.catchRate = "190";
        p.weight = "1,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Plante";
        p.size = "0,2m";

        p = perName.get("Empiflor");
        p.evolutions = new EvolutionNode(perName.get("Chetiflor"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 21", new EvolutionNode(perName.get("Boustiflor"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Plante", new EvolutionNode(perName.get("Empiflor"), null));}}));}});
        p.catchRate = "45";
        p.weight = "15,5kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Plante";
        p.size = "1,7m";

        p = perName.get("Brasegali");
        p.evolutions = new EvolutionNode(perName.get("Poussifeu"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Galifeu"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 36", new EvolutionNode(perName.get("Brasegali"), new HashMap<String, EvolutionNode>(){{this.put("Brasegalite", new EvolutionNode(perName.get("Mega-Brasegali"), null));}}));}}));}});
        p.catchRate = "45";
        p.weight = "52,0kg";
        p.hatch = "19 cycles - 5120 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Sol";
        p.size = "1,9m";

        p = perName.get("Chenipan");
        p.evolutions = new EvolutionNode(perName.get("Chenipan"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 7", new EvolutionNode(perName.get("Chrysacier"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 10", new EvolutionNode(perName.get("Papilusion"), null));}}));}});
        p.catchRate = "255";
        p.weight = "2,9kg";
        p.hatch = "14 cycles - 3840 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 PV";
        p.eggGroup = "Insecte";
        p.size = "0,3m";

        p = perName.get("Limonde");
        p.evolutions = null;
        p.catchRate = "75";
        p.weight = "11,0kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Eau 1/Indetermine";
        p.size = "0,7m";

        p = perName.get("Grodrive");
        p.evolutions = new EvolutionNode(perName.get("Baudrive"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 28", new EvolutionNode(perName.get("Grodrive"), null));}});
        p.catchRate = "60";
        p.weight = "15,0kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 PV";
        p.eggGroup = "Indetermine";
        p.size = "1,2m";

        p = perName.get("Flabebe");
        p.evolutions = new EvolutionNode(perName.get("Flabebe"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 19", new EvolutionNode(perName.get("Floette"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierre Eclat", new EvolutionNode(perName.get("Florges"), null));}}));}});
        p.catchRate = "";
        p.weight = "0,1kg";
        p.hatch = "pas";
        p.gender = "100% femelle; 0% male";
        p.ev = "+1 Def. Spe";
        p.eggGroup = "Fee";
        p.size = "0,1m";

        p = perName.get("Mega-Alakazam");
        p.evolutions = new EvolutionNode(perName.get("Abra"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 16", new EvolutionNode(perName.get("Kadabra"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Alakazam"), new HashMap<String, EvolutionNode>(){{this.put("Alakazamite", new EvolutionNode(perName.get("Mega-Alakazam"), null));}}));}}));}});
        p.catchRate = "";
        p.weight = "48,0kg";
        p.hatch = "";
        p.gender = "25% femelle; 75% male";
        p.ev = "";
        p.eggGroup = "";
        p.size = "1,2m";

        p = perName.get("Gringolem");
        p.evolutions = new EvolutionNode(perName.get("Gringolem"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 43", new EvolutionNode(perName.get("Golemastoc"), null));}});
        p.catchRate = "190";
        p.weight = "92,0kg";
        p.hatch = "25 cycles - 6630 pas";
        p.gender = "Asexue";
        p.ev = "+1 Att.";
        p.eggGroup = "Mineral";
        p.size = "1,0m";

        p = perName.get("Galvaran");
        p.evolutions = new EvolutionNode(perName.get("Galvaran"), new HashMap<String, EvolutionNode>(){{this.put("Avec une Pierresoleil", new EvolutionNode(perName.get("Iguolta"), null));}});
        p.catchRate = "";
        p.weight = "6,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+1 Vit.";
        p.eggGroup = "Monstre/Dragon";
        p.size = "0,5m";

        p = perName.get("Megapagos");
        p.evolutions = new EvolutionNode(perName.get("Carapagos"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Megapagos"), null));}});
        p.catchRate = "45";
        p.weight = "81,0kg";
        p.hatch = "30 cycles - 7905 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Eau 1/Eau 3";
        p.size = "1,2m";

        p = perName.get("Drattak");
        p.evolutions = new EvolutionNode(perName.get("Draby"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Drackhaus"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 50", new EvolutionNode(perName.get("Drattak"), null));}}));}});
        p.catchRate = "45";
        p.weight = "102,6kg";
        p.hatch = "39 cycles - 10240 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Dragon";
        p.size = "1,5m";

        p = perName.get("Vacilys");
        p.evolutions = new EvolutionNode(perName.get("Lilia"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 40", new EvolutionNode(perName.get("Vacilys"), null));}});
        p.catchRate = "45";
        p.weight = "60,4kg";
        p.hatch = "29 cycles - 7680 pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Def. Spe";
        p.eggGroup = "Eau 3";
        p.size = "1,5m";

        p = perName.get("Banshitrouye (Taille Normale)");
        p.evolutions = new EvolutionNode(perName.get("Pitrouille (Taille Normale)"), new HashMap<String, EvolutionNode>(){{this.put("Echange", new EvolutionNode(perName.get("Banshitrouye (Taille Normale)"), null));}});
        p.catchRate = "";
        p.weight = "9,5kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Indetermine";
        p.size = "0,7m";

        p = perName.get("Pandarbare");
        p.evolutions = new EvolutionNode(perName.get("Pandespiegle"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32, avec un Pokemon dans l'equipe", new EvolutionNode(perName.get("Pandarbare"), null));}});
        p.catchRate = "";
        p.weight = "136,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Att.";
        p.eggGroup = "Sol/Humanoide";
        p.size = "2,1m";

        p = perName.get("Rexillius");
        p.evolutions = new EvolutionNode(perName.get("Ptyranidur"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 39 pendant la journee", new EvolutionNode(perName.get("Rexillius"), null));}});
        p.catchRate = "";
        p.weight = "270,0kg";
        p.hatch = "pas";
        p.gender = "12.5% femelle; 87.5% male";
        p.ev = "+2 Att.";
        p.eggGroup = "";
        p.size = "2,5m";

        p = perName.get("Brutapode");
        p.evolutions = new EvolutionNode(perName.get("Venipatte"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 22", new EvolutionNode(perName.get("Scobolide"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 30", new EvolutionNode(perName.get("Brutapode"), null));}}));}});
        p.catchRate = "45";
        p.weight = "200,5kg";
        p.hatch = "20 cycles - 5355 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Vit.";
        p.eggGroup = "Insecte";
        p.size = "2,5m";

        p = perName.get("Deflaisan");
        p.evolutions = new EvolutionNode(perName.get("Poichigeon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 21", new EvolutionNode(perName.get("Colombeau"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 32", new EvolutionNode(perName.get("Deflaisan"), null));}}));}});
        p.catchRate = "45";
        p.weight = "29,0kg";
        p.hatch = "15 cycles - 4080 pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+3 Att.";
        p.eggGroup = "Vol";
        p.size = "1,2m";

        p = perName.get("Seracrawl");
        p.evolutions = new EvolutionNode(perName.get("Grelacon"), new HashMap<String, EvolutionNode>(){{this.put("Niveau 37", new EvolutionNode(perName.get("Seracrawl"), null));}});
        p.catchRate = "";
        p.weight = "505,0kg";
        p.hatch = "pas";
        p.gender = "50% femelle; 50% male";
        p.ev = "+2 Def.";
        p.eggGroup = "Monstre";
        p.size = "2,0m";
	}

    public static HashMap<String, Pokemon> perName = new HashMap<String, Pokemon>() {{
        ArrayList<Talent> talents;

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.FUITE);this.add(Talent.AGITATION);}};
        this.put("Rattatac", new Pokemon("Rattatac", 20, 24, Type.NORMAL, Type.NONE, talents, 55, 81, 60, 50, 70, 97));

        talents = new ArrayList<Talent>(){{this.add(Talent.TELECHARGE);this.add(Talent.ADAPTABILITE);this.add(Talent.ANALYSTE);}};
        this.put("Porygon-Z", new Pokemon("Porygon-Z", 474, 507, Type.PSY, Type.NONE, talents, 85, 80, 70, 135, 75, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);this.add(Talent.IMPUDENCE);this.add(Talent.INTIMIDATION);}};
        this.put("Baggiguane", new Pokemon("Baggiguane", 559, 600, Type.TENEBRE, Type.COMBAT, talents, 50, 75, 70, 35, 70, 48));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.RECOLTE);}};
        this.put("Noadkoko", new Pokemon("Noadkoko", 103, 109, Type.PLANTE, Type.PSY, talents, 95, 95, 85, 125, 65, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.SANS_LIMITE);this.add(Talent.ACHARNE);}};
        this.put("Gueriaigle", new Pokemon("Gueriaigle", 628, 669, Type.NORMAL, Type.VOL, talents, 100, 123, 75, 57, 75, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);this.add(Talent.FOUILLE);this.add(Talent.CORPS_MAUDIT);}};
        this.put("Polichombr", new Pokemon("Polichombr", 353, 376, Type.SPECTRE, Type.NONE, talents, 44, 75, 35, 63, 33, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.POSE_SPORE);this.add(Talent.REGE_FORCE);}};
        this.put("Gaulet", new Pokemon("Gaulet", 591, 632, Type.PLANTE, Type.POISON, talents, 114, 85, 70, 85, 80, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.SNIPER);this.add(Talent.MOITEUR);}};
        this.put("Hyporoi", new Pokemon("Hyporoi", 230, 246, Type.EAU, Type.DRAGON, talents, 75, 95, 95, 95, 95, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.MOTORISE);this.add(Talent.ESPRIT_VITAL);}};
        this.put("Elekable", new Pokemon("Elekable", 466, 499, Type.ELECTRIQUE, Type.NONE, talents, 75, 123, 67, 95, 85, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.MAGICIEN);}};
        this.put("Roussil", new Pokemon("Roussil", 654, 700, Type.FEU, Type.NONE, talents, 59, 59, 58, 90, 70, 73));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.TECHNICIEN);this.add(Talent.MULTI_COUPS);}};
        this.put("Pashmilla", new Pokemon("Pashmilla", 573, 614, Type.NORMAL, Type.NONE, talents, 75, 95, 60, 65, 60, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);this.add(Talent.MOTORISE);}};
        this.put("Emolga", new Pokemon("Emolga", 587, 628, Type.ELECTRIQUE, Type.VOL, talents, 55, 75, 60, 75, 60, 103));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.FERMETE);}};
        this.put("Grolem", new Pokemon("Grolem", 76, 81, Type.ROCHE, Type.SOL, talents, 80, 110, 130, 55, 65, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Cresselia", new Pokemon("Cresselia", 488, 527, Type.PSY, Type.NONE, talents, 120, 70, 120, 75, 130, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLOUTONNERIE);this.add(Talent.TORRENT);}};
        this.put("Flotoutan", new Pokemon("Flotoutan", 516, 556, Type.EAU, Type.NONE, talents, 75, 98, 63, 98, 63, 101));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.CUVETTE);}};
        this.put("Bekipan", new Pokemon("Bekipan", 279, 297, Type.EAU, Type.VOL, talents, 60, 50, 100, 85, 70, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.COQUE_ARMURE);}};
        this.put("Mateloutre", new Pokemon("Mateloutre", 502, 542, Type.EAU, Type.NONE, talents, 75, 75, 60, 83, 60, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.ANTI_BRUIT);}};
        this.put("Dinoclier", new Pokemon("Dinoclier", 410, 438, Type.ROCHE, Type.ACIER, talents, 30, 42, 118, 42, 88, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.CHANCEUX);this.add(Talent.COEUR_NOBLE);}};
        this.put("Absol", new Pokemon("Absol", 359, 383, Type.TENEBRE, Type.NONE, talents, 65, 130, 60, 75, 60, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.COLOFORCE);this.add(Talent.HERBIVORE);}};
        this.put("Azurill", new Pokemon("Azurill", 298, 317, Type.NORMAL, Type.NONE, talents, 50, 20, 40, 20, 40, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.TENSION);}};
        this.put("Apireine", new Pokemon("Apireine", 416, 446, Type.INSECTE, Type.VOL, talents, 70, 80, 102, 80, 102, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.FORCE_SOLEIL);}};
        this.put("Dracaufeu", new Pokemon("Dracaufeu", 6, 7, Type.FEU, Type.VOL, talents, 78, 84, 78, 109, 85, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.AGITATION);}};
        this.put("Solochi", new Pokemon("Solochi", 633, 674, Type.TENEBRE, Type.DRAGON, talents, 52, 65, 50, 45, 50, 38));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Motisma (Forme Tonte)", new Pokemon("Motisma (Forme Tonte)", 479, 516, Type.ELECTRIQUE, Type.SPECTRE, talents, 50, 65, 107, 105, 107, 86));

        talents = new ArrayList<Talent>(){{this.add(Talent.ARMUMAGMA);this.add(Talent.CORPS_ARDENT);this.add(Talent.ARMUROUILLEE);}};
        this.put("Volcaropod", new Pokemon("Volcaropod", 219, 234, Type.FEU, Type.ROCHE, talents, 50, 50, 120, 80, 80, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.FARCEUR);this.add(Talent.ACHARNE);}};
        this.put("Boreas (Forme Totemique)", new Pokemon("Boreas (Forme Totemique)", 641, 683, Type.VOL, Type.NONE, talents, 79, 100, 80, 110, 90, 121));

        talents = new ArrayList<Talent>(){{this.add(Talent.SERENITE);}};
        this.put("Meloetta (Forme Voix)", new Pokemon("Meloetta (Forme Voix)", 648, 693, Type.NORMAL, Type.PSY, talents, 100, 77, 77, 128, 128, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.INTIMIDATION);this.add(Talent.PHOBIQUE);}};
        this.put("Snubbull", new Pokemon("Snubbull", 209, 222, Type.NORMAL, Type.NONE, talents, 60, 80, 50, 40, 40, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_DURE);}};
        this.put("Sharpedo", new Pokemon("Sharpedo", 319, 342, Type.EAU, Type.TENEBRE, talents, 70, 120, 40, 95, 40, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Motisma (Forme Froid)", new Pokemon("Motisma (Forme Froid)", 479, 515, Type.ELECTRIQUE, Type.SPECTRE, talents, 50, 65, 107, 105, 107, 86));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);}};
        this.put("Mega-Mewtwo Y", new Pokemon("Mega-Mewtwo Y", 150, 162, Type.PSY, Type.NONE, talents, 106, 150, 70, 194, 120, 140));

        talents = new ArrayList<Talent>(){{this.add(Talent.MOMIE);}};
        this.put("Tutafeh", new Pokemon("Tutafeh", 562, 603, Type.SPECTRE, Type.NONE, talents, 38, 30, 85, 55, 65, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Noctunoir", new Pokemon("Noctunoir", 477, 510, Type.SPECTRE, Type.NONE, talents, 45, 100, 135, 65, 135, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.GARDE_MAGIK);this.add(Talent.INCONSCIENT);}};
        this.put("Melodelfe", new Pokemon("Melodelfe", 36, 40, Type.NORMAL, Type.NONE, talents, 95, 70, 73, 85, 90, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.IMPASSIBLE);}};
        this.put("Mega-Mewtwo X", new Pokemon("Mega-Mewtwo X", 150, 161, Type.PSY, Type.COMBAT, talents, 106, 190, 100, 154, 100, 130));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);}};
        this.put("Celebi", new Pokemon("Celebi", 251, 268, Type.PSY, Type.PLANTE, talents, 100, 100, 100, 100, 100, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_SOIN);this.add(Talent.AROMA_VOILE);}};
        this.put("Cocotine", new Pokemon("Cocotine", 683, 730, Type.FEE, Type.NONE, talents, 100, 65, 75, 95, 90, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.ILLUSION);}};
        this.put("Zorua", new Pokemon("Zorua", 570, 611, Type.TENEBRE, Type.NONE, talents, 40, 65, 40, 80, 40, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);}};
        this.put("Mega-Elecsprint", new Pokemon("Mega-Elecsprint", 310, 333, Type.ELECTRIQUE, Type.NONE, talents, 70, 75, 80, 135, 80, 135));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.MUE);this.add(Talent.ANNULE_GARDE);}};
        this.put("Carabing", new Pokemon("Carabing", 588, 629, Type.INSECTE, Type.NONE, talents, 50, 75, 45, 40, 45, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.MARQUE_OMBRE);this.add(Talent.TELEPATHE);}};
        this.put("Okeoke", new Pokemon("Okeoke", 360, 385, Type.PSY, Type.NONE, talents, 95, 23, 48, 23, 48, 23));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.SNIPER);this.add(Talent.MOITEUR);}};
        this.put("Hypotrempe", new Pokemon("Hypotrempe", 116, 123, Type.EAU, Type.NONE, talents, 30, 40, 70, 70, 25, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.PEAU_FEERIQUE);}};
        this.put("Nymphali", new Pokemon("Nymphali", 700, 747, Type.FEE, Type.NONE, talents, 95, 65, 65, 110, 130, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.TOXITOUCHE);}};
        this.put("Venalgue", new Pokemon("Venalgue", 690, 737, Type.POISON, Type.EAU, talents, 50, 60, 60, 60, 60, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_CELESTE);}};
        this.put("Mega-Scarabrute", new Pokemon("Mega-Scarabrute", 127, 135, Type.INSECTE, Type.VOL, talents, 65, 155, 120, 65, 90, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.MOITEUR);this.add(Talent.INCONSCIENT);}};
        this.put("Maraiste", new Pokemon("Maraiste", 195, 208, Type.EAU, Type.SOL, talents, 95, 85, 85, 65, 65, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);}};
        this.put("Mega-Florizarre", new Pokemon("Mega-Florizarre", 3, 4, Type.PLANTE, Type.POISON, talents, 80, 100, 123, 122, 120, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);this.add(Talent.LENTITEINTEE);}};
        this.put("Papilusion", new Pokemon("Papilusion", 12, 16, Type.INSECTE, Type.VOL, talents, 60, 45, 50, 80, 80, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.SANS_LIMITE);this.add(Talent.POING_DE_FER);}};
        this.put("Charpenti", new Pokemon("Charpenti", 532, 572, Type.COMBAT, Type.NONE, talents, 75, 80, 55, 25, 35, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.MATINAL);this.add(Talent.PIED_CONFUS);}};
        this.put("Doduo", new Pokemon("Doduo", 84, 89, Type.NORMAL, Type.VOL, talents, 35, 85, 45, 35, 35, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTICIPATION);this.add(Talent.PEAU_SECHE);this.add(Talent.TOXITOUCHE);}};
        this.put("Coatox", new Pokemon("Coatox", 454, 486, Type.POISON, Type.COMBAT, talents, 83, 106, 65, 86, 65, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.FORCE_PURE);this.add(Talent.TELEPATHE);}};
        this.put("Charmina", new Pokemon("Charmina", 308, 329, Type.COMBAT, Type.PSY, talents, 60, 60, 75, 60, 75, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_VOLT);this.add(Talent.PIED_VELOCE);}};
        this.put("Voltali", new Pokemon("Voltali", 135, 144, Type.ELECTRIQUE, Type.NONE, talents, 65, 65, 60, 110, 95, 130));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.FOUILLE);this.add(Talent.INSOMNIA);}};
        this.put("Pitrouille (Taille Maxi)", new Pokemon("Pitrouille (Taille Maxi)", 710, 759, Type.SPECTRE, Type.PLANTE, talents, 54, 66, 70, 44, 55, 51));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTICIPATION);this.add(Talent.ENVELOCAPE);}};
        this.put("Cheniselle (Cape Dechet)", new Pokemon("Cheniselle (Cape Dechet)", 413, 443, Type.INSECTE, Type.NONE, talents, 60, 69, 95, 69, 95, 36));

        talents = new ArrayList<Talent>(){{this.add(Talent.DECLIC_TACTIQUE);}};
        this.put("Exagide (Forme Assaut)", new Pokemon("Exagide (Forme Assaut)", 681, 727, Type.ACIER, Type.SPECTRE, talents, 60, 150, 50, 150, 50, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.COEUR_SOIN);}};
        this.put("Joliflor", new Pokemon("Joliflor", 182, 195, Type.PLANTE, Type.NONE, talents, 75, 80, 85, 90, 100, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.CALQUE);this.add(Talent.TELEPATHE);}};
        this.put("Tarsal", new Pokemon("Tarsal", 280, 298, Type.PSY, Type.NONE, talents, 28, 25, 25, 45, 35, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.ACHARNE);this.add(Talent.PRESSION);}};
        this.put("Scalpion", new Pokemon("Scalpion", 624, 665, Type.ACIER, Type.TENEBRE, talents, 45, 85, 70, 40, 40, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.TETE_DE_ROC);this.add(Talent.HEAVY_METAL);}};
        this.put("Galegon", new Pokemon("Galegon", 305, 325, Type.ACIER, Type.ROCHE, talents, 60, 90, 140, 50, 50, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Smogogo", new Pokemon("Smogogo", 110, 116, Type.POISON, Type.NONE, talents, 65, 90, 120, 85, 70, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.BOOM_FINAL);this.add(Talent.DELESTAGE);this.add(Talent.RAGE_BRULURE);}};
        this.put("Baudrive", new Pokemon("Baudrive", 425, 455, Type.SPECTRE, Type.VOL, talents, 90, 50, 34, 60, 44, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Libegon", new Pokemon("Libegon", 330, 353, Type.SOL, Type.DRAGON, talents, 80, 100, 80, 80, 80, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.ENVELOCAPE);}};
        this.put("Pomdepik", new Pokemon("Pomdepik", 204, 217, Type.INSECTE, Type.NONE, talents, 50, 65, 90, 35, 35, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Korillon", new Pokemon("Korillon", 433, 463, Type.PSY, Type.NONE, talents, 45, 30, 50, 65, 50, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.PARE_BALLES);}};
        this.put("Boguerisse", new Pokemon("Boguerisse", 651, 697, Type.PLANTE, Type.NONE, talents, 54, 79, 101, 50, 50, 52));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTI_BRUIT);this.add(Talent.FILTRE);this.add(Talent.TECHNICIEN);}};
        this.put("Mime Jr.", new Pokemon("Mime Jr.", 439, 469, Type.PSY, Type.NONE, talents, 20, 25, 45, 70, 90, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.TECHNICIEN);this.add(Talent.TEMPO_PERSO);this.add(Talent.LUNATIQUE);}};
        this.put("Queulorior", new Pokemon("Queulorior", 235, 251, Type.NORMAL, Type.NONE, talents, 55, 20, 35, 20, 45, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.QUERELLEUR);this.add(Talent.HERBIVORE);}};
        this.put("Ecremeuh", new Pokemon("Ecremeuh", 241, 257, Type.NORMAL, Type.NONE, talents, 95, 80, 105, 40, 70, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.GLOUTONNERIE);this.add(Talent.PIED_VELOCE);}};
        this.put("Lineon", new Pokemon("Lineon", 264, 282, Type.NORMAL, Type.NONE, talents, 78, 70, 61, 50, 61, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.PARATONNERRE);this.add(Talent.ARMURBASTON);}};
        this.put("Osselait", new Pokemon("Osselait", 104, 110, Type.SOL, Type.NONE, talents, 50, 50, 95, 40, 50, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.INCONSCIENT);this.add(Talent.SIMPLE);this.add(Talent.LUNATIQUE);}};
        this.put("Castorno", new Pokemon("Castorno", 400, 428, Type.NORMAL, Type.EAU, talents, 79, 85, 60, 55, 60, 71));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);this.add(Talent.PREDICTION);this.add(Talent.ATTENTION);}};
        this.put("Hypnomade", new Pokemon("Hypnomade", 97, 103, Type.PSY, Type.NONE, talents, 85, 73, 70, 73, 115, 67));

        talents = new ArrayList<Talent>(){{this.add(Talent.VENTOUSE);this.add(Talent.LAVABO);}};
        this.put("Lilia", new Pokemon("Lilia", 345, 368, Type.ROCHE, Type.PLANTE, talents, 66, 41, 77, 61, 87, 23));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Motisma (Forme Helice)", new Pokemon("Motisma (Forme Helice)", 479, 517, Type.ELECTRIQUE, Type.SPECTRE, talents, 50, 65, 107, 105, 107, 86));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRISE_MOULE);this.add(Talent.SANS_LIMITE);}};
        this.put("Kranidos", new Pokemon("Kranidos", 408, 436, Type.ROCHE, Type.NONE, talents, 67, 125, 40, 30, 30, 58));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.RIDEAU_NEIGE);this.add(Talent.ISOGRAISSE);}};
        this.put("Mammochon", new Pokemon("Mammochon", 473, 506, Type.GLACE, Type.SOL, talents, 110, 130, 80, 70, 60, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.PUANTEUR);this.add(Talent.BOOM_FINAL);}};
        this.put("Moufouette", new Pokemon("Moufouette", 434, 464, Type.POISON, Type.TENEBRE, talents, 63, 63, 47, 41, 41, 74));

        talents = new ArrayList<Talent>(){{this.add(Talent.PUANTEUR);this.add(Talent.ARMUROUILLEE);this.add(Talent.BOOM_FINAL);}};
        this.put("Miasmax", new Pokemon("Miasmax", 569, 610, Type.POISON, Type.NONE, talents, 80, 95, 82, 60, 82, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLOUTONNERIE);this.add(Talent.TORCHE);this.add(Talent.ECRAN_FUMEE);}};
        this.put("Aflamanoir", new Pokemon("Aflamanoir", 631, 672, Type.FEU, Type.NONE, talents, 85, 97, 66, 105, 66, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.CRAN);this.add(Talent.SANS_LIMITE);}};
        this.put("Makuhita", new Pokemon("Makuhita", 296, 315, Type.COMBAT, Type.NONE, talents, 72, 60, 30, 20, 30, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.FOUILLE);this.add(Talent.HERBIVORE);}};
        this.put("Cerfrousse", new Pokemon("Cerfrousse", 234, 250, Type.NORMAL, Type.NONE, talents, 73, 95, 62, 85, 65, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.ATTENTION);this.add(Talent.GARDE_MAGIK);}};
        this.put("Alakazam", new Pokemon("Alakazam", 65, 69, Type.PSY, Type.NONE, talents, 55, 50, 45, 135, 85, 120));

        talents = new ArrayList<Talent>(){{this.add(Talent.GRIFFE_DURE);}};
        this.put("Mega-Dracaufeu X", new Pokemon("Mega-Dracaufeu X", 6, 8, Type.FEU, Type.DRAGON, talents, 78, 130, 111, 130, 85, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.FORCE_SOLEIL);}};
        this.put("Reptincel", new Pokemon("Reptincel", 5, 6, Type.FEU, Type.NONE, talents, 58, 64, 58, 80, 65, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.SOLIDE_ROC);this.add(Talent.FERMETE);this.add(Talent.GLISSADE);}};
        this.put("Carapagos", new Pokemon("Carapagos", 564, 605, Type.EAU, Type.ROCHE, talents, 54, 78, 103, 53, 45, 22));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.SNIPER);this.add(Talent.MOITEUR);}};
        this.put("Hypocean", new Pokemon("Hypocean", 117, 124, Type.EAU, Type.NONE, talents, 55, 65, 95, 95, 45, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.COQUE_ARMURE);}};
        this.put("Tortipouss", new Pokemon("Tortipouss", 387, 415, Type.PLANTE, Type.NONE, talents, 55, 68, 64, 45, 55, 31));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.CORPS_GEL);this.add(Talent.LUNATIQUE);}};
        this.put("Stalgamin", new Pokemon("Stalgamin", 361, 386, Type.GLACE, Type.NONE, talents, 50, 50, 50, 50, 50, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.COQUE_ARMURE);this.add(Talent.ENVELOCAPE);}};
        this.put("Lancargot", new Pokemon("Lancargot", 589, 630, Type.INSECTE, Type.ACIER, talents, 70, 135, 105, 60, 105, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTI_BRUIT);this.add(Talent.PHOBIQUE);}};
        this.put("Chuchmur", new Pokemon("Chuchmur", 293, 312, Type.NORMAL, Type.NONE, talents, 64, 51, 23, 51, 23, 28));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Motisma (Forme Normale)", new Pokemon("Motisma (Forme Normale)", 479, 512, Type.ELECTRIQUE, Type.SPECTRE, talents, 50, 50, 77, 95, 77, 91));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_ARDENT);this.add(Talent.ESPRIT_VITAL);}};
        this.put("Maganon", new Pokemon("Maganon", 467, 500, Type.FEU, Type.NONE, talents, 75, 95, 67, 125, 95, 83));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSENTEISME);}};
        this.put("Parecool", new Pokemon("Parecool", 287, 306, Type.NORMAL, Type.NONE, talents, 60, 60, 60, 35, 35, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);}};
        this.put("Wattouat", new Pokemon("Wattouat", 179, 191, Type.ELECTRIQUE, Type.NONE, talents, 55, 40, 40, 65, 45, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.SNIPER);this.add(Talent.GRIFFE_DURE);this.add(Talent.PICKPOCKET);}};
        this.put("Opermine", new Pokemon("Opermine", 688, 735, Type.ROCHE, Type.EAU, talents, 50, 95, 95, 30, 80, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.ACHARNE);}};
        this.put("Prinplouf", new Pokemon("Prinplouf", 394, 422, Type.EAU, Type.NONE, talents, 64, 66, 68, 81, 76, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Anchwatt", new Pokemon("Anchwatt", 602, 643, Type.ELECTRIQUE, Type.NONE, talents, 35, 55, 40, 45, 40, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.PLUS);this.add(Talent.PARATONNERRE);}};
        this.put("Posipi", new Pokemon("Posipi", 311, 334, Type.ELECTRIQUE, Type.NONE, talents, 60, 50, 40, 85, 75, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.DECLIC_TACTIQUE);}};
        this.put("Exagide (Forme Parade)", new Pokemon("Exagide (Forme Parade)", 681, 728, Type.ACIER, Type.SPECTRE, talents, 60, 50, 150, 50, 150, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);this.add(Talent.ESPRIT_VITAL);}};
        this.put("Elekid", new Pokemon("Elekid", 239, 255, Type.ELECTRIQUE, Type.NONE, talents, 45, 63, 37, 65, 55, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_ARDENT);this.add(Talent.AILES_BOURRASQUE);}};
        this.put("Flambusard", new Pokemon("Flambusard", 663, 709, Type.FEU, Type.VOL, talents, 78, 81, 71, 74, 69, 126));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Balbuto", new Pokemon("Balbuto", 343, 366, Type.SOL, Type.PSY, talents, 40, 40, 55, 40, 70, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);this.add(Talent.TURBO);this.add(Talent.FOUILLE);}};
        this.put("Yanma", new Pokemon("Yanma", 193, 206, Type.INSECTE, Type.VOL, talents, 65, 65, 45, 75, 45, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_DE_COQ);this.add(Talent.CHANCEUX);this.add(Talent.RIVALITE);}};
        this.put("Poichigeon", new Pokemon("Poichigeon", 519, 559, Type.NORMAL, Type.VOL, talents, 50, 55, 50, 36, 30, 43));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Lamperoie", new Pokemon("Lamperoie", 603, 644, Type.ELECTRIQUE, Type.NONE, talents, 65, 85, 70, 75, 70, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.CALQUE);this.add(Talent.TELEPATHE);}};
        this.put("Kirlia", new Pokemon("Kirlia", 281, 299, Type.PSY, Type.NONE, talents, 38, 35, 35, 65, 55, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.COEUR_DE_COQ);this.add(Talent.HYDRATATION);}};
        this.put("Couaneton", new Pokemon("Couaneton", 580, 621, Type.EAU, Type.VOL, talents, 62, 44, 50, 44, 50, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FUITE);}};
        this.put("Mystherbe", new Pokemon("Mystherbe", 43, 47, Type.PLANTE, Type.POISON, talents, 45, 50, 55, 75, 65, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.LIGHT_METAL);}};
        this.put("Metang", new Pokemon("Metang", 375, 400, Type.ACIER, Type.PSY, talents, 60, 75, 100, 55, 80, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLUE);this.add(Talent.LAVABO);this.add(Talent.FORCE_SABLE);}};
        this.put("Tritosor", new Pokemon("Tritosor", 423, 453, Type.EAU, Type.SOL, talents, 111, 83, 68, 92, 82, 39));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.MULTIECAILLE);}};
        this.put("Dracolosse", new Pokemon("Dracolosse", 149, 159, Type.DRAGON, Type.VOL, talents, 91, 134, 95, 100, 100, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.TEMPO_PERSO);this.add(Talent.FEUIL_GARDE);}};
        this.put("Fragilady", new Pokemon("Fragilady", 549, 589, Type.PLANTE, Type.NONE, talents, 70, 60, 75, 110, 75, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.TELECHARGE);}};
        this.put("Genesect", new Pokemon("Genesect", 649, 695, Type.INSECTE, Type.ACIER, talents, 71, 120, 95, 120, 95, 99));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.RIVALITE);this.add(Talent.AGITATION);}};
        this.put("Nidorino", new Pokemon("Nidorino", 33, 37, Type.POISON, Type.NONE, talents, 61, 72, 57, 55, 55, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);this.add(Talent.FOUILLE);this.add(Talent.CORPS_MAUDIT);}};
        this.put("Branette", new Pokemon("Branette", 354, 377, Type.SPECTRE, Type.NONE, talents, 64, 115, 65, 83, 63, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.RIVALITE);this.add(Talent.AGITATION);}};
        this.put("Nidorina", new Pokemon("Nidorina", 30, 34, Type.POISON, Type.NONE, talents, 70, 62, 67, 55, 55, 56));

        talents = new ArrayList<Talent>(){{this.add(Talent.PARATONNERRE);this.add(Talent.TETE_DE_ROC);this.add(Talent.TEMERAIRE);}};
        this.put("Rhinoferos", new Pokemon("Rhinoferos", 112, 118, Type.SOL, Type.ROCHE, talents, 105, 130, 120, 45, 45, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.DEBUT_CALME);}};
        this.put("Regigigas", new Pokemon("Regigigas", 486, 524, Type.NORMAL, Type.NONE, talents, 110, 160, 110, 80, 110, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.SUINTEMENT);this.add(Talent.CUVETTE);}};
        this.put("Tentacruel", new Pokemon("Tentacruel", 73, 78, Type.EAU, Type.POISON, talents, 80, 70, 65, 80, 120, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.TEMPO_PERSO);this.add(Talent.FEUIL_GARDE);}};
        this.put("Chlorobule", new Pokemon("Chlorobule", 548, 588, Type.PLANTE, Type.NONE, talents, 45, 35, 50, 70, 50, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.SANS_LIMITE);this.add(Talent.MODE_TRANSE);}};
        this.put("Darumacho (Mode Daruma)", new Pokemon("Darumacho (Mode Daruma)", 555, 596, Type.FEU, Type.NONE, talents, 105, 30, 105, 140, 105, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESPRIT_VITAL);this.add(Talent.COLERIQUE);this.add(Talent.ACHARNE);}};
        this.put("Ferosinge", new Pokemon("Ferosinge", 56, 60, Type.COMBAT, Type.NONE, talents, 40, 80, 35, 35, 45, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.TEMPO_PERSO);this.add(Talent.REGE_FORCE);}};
        this.put("Flagadoss", new Pokemon("Flagadoss", 80, 85, Type.EAU, Type.PSY, talents, 95, 75, 110, 100, 80, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);this.add(Talent.FUITE);}};
        this.put("Crikzik", new Pokemon("Crikzik", 401, 429, Type.INSECTE, Type.NONE, talents, 37, 25, 41, 25, 41, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.FLORA_VOILE);this.add(Talent.SYMBIOSIS);}};
        this.put("Florges", new Pokemon("Florges", 671, 717, Type.FEE, Type.NONE, talents, 78, 65, 68, 112, 154, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYPER_CUTTER);this.add(Talent.BRISE_MOULE);this.add(Talent.IMPUDENCE);}};
        this.put("Scarabrute", new Pokemon("Scarabrute", 127, 134, Type.INSECTE, Type.NONE, talents, 65, 125, 100, 55, 70, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.INSOMNIA);this.add(Talent.SNIPER);}};
        this.put("Mimigal", new Pokemon("Mimigal", 167, 179, Type.INSECTE, Type.POISON, talents, 40, 60, 40, 40, 40, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.MATINAL);this.add(Talent.PIED_CONFUS);}};
        this.put("Dodrio", new Pokemon("Dodrio", 85, 90, Type.NORMAL, Type.VOL, talents, 60, 110, 70, 60, 60, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);this.add(Talent.PIED_CONFUS);this.add(Talent.COEUR_DE_COQ);}};
        this.put("Pijako", new Pokemon("Pijako", 441, 471, Type.NORMAL, Type.VOL, talents, 76, 65, 45, 92, 42, 91));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);this.add(Talent.ECRAN_POUDRE);this.add(Talent.GARDE_AMIE);}};
        this.put("Lepidonille", new Pokemon("Lepidonille", 664, 710, Type.INSECTE, Type.NONE, talents, 38, 35, 40, 27, 25, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.TEMERAIRE);this.add(Talent.ADAPTABILITE);this.add(Talent.BRISE_MOULE);}};
        this.put("Bargantua", new Pokemon("Bargantua", 550, 590, Type.EAU, Type.NONE, talents, 70, 92, 65, 80, 55, 98));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);}};
        this.put("Chrysacier", new Pokemon("Chrysacier", 11, 15, Type.INSECTE, Type.NONE, talents, 50, 20, 55, 25, 25, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTI_BRUIT);this.add(Talent.STATIK);this.add(Talent.BOOM_FINAL);}};
        this.put("Electrode", new Pokemon("Electrode", 101, 107, Type.ELECTRIQUE, Type.NONE, talents, 60, 50, 70, 80, 80, 140));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_GEL);this.add(Talent.ARMUROUILLEE);}};
        this.put("Sorbebe", new Pokemon("Sorbebe", 582, 623, Type.GLACE, Type.NONE, talents, 36, 50, 50, 65, 60, 44));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIDEAU_NEIGE);this.add(Talent.CORPS_GEL);}};
        this.put("Givrali", new Pokemon("Givrali", 471, 504, Type.GLACE, Type.NONE, talents, 65, 60, 110, 130, 95, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.SUINTEMENT);this.add(Talent.GLUE);this.add(Talent.GLOUTONNERIE);}};
        this.put("Gloupti", new Pokemon("Gloupti", 316, 339, Type.POISON, Type.NONE, talents, 70, 43, 53, 43, 53, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.POING_DE_FER);this.add(Talent.MALADRESSE);this.add(Talent.ANNULE_GARDE);}};
        this.put("Gringolem", new Pokemon("Gringolem", 622, 663, Type.SOL, Type.SPECTRE, talents, 59, 74, 50, 35, 50, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.PUANTEUR);this.add(Talent.GLUE);this.add(Talent.BOOM_FINAL);}};
        this.put("Miamiasme", new Pokemon("Miamiasme", 568, 609, Type.POISON, Type.NONE, talents, 50, 50, 62, 40, 62, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.SERENITE);this.add(Talent.AGITATION);this.add(Talent.CHANCEUX);}};
        this.put("Togepi", new Pokemon("Togepi", 175, 187, Type.NORMAL, Type.NONE, talents, 35, 20, 65, 40, 65, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);this.add(Talent.CHANCEUX);this.add(Talent.IMPUDENCE);}};
        this.put("Corboss", new Pokemon("Corboss", 430, 460, Type.TENEBRE, Type.VOL, talents, 100, 125, 52, 105, 52, 71));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLOUTONNERIE);this.add(Talent.BRASIER);}};
        this.put("Flamajou", new Pokemon("Flamajou", 513, 553, Type.FEU, Type.NONE, talents, 50, 53, 48, 53, 48, 64));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.TEMERAIRE);}};
        this.put("Etourvol", new Pokemon("Etourvol", 397, 425, Type.NORMAL, Type.VOL, talents, 55, 75, 50, 40, 40, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.MUE);this.add(Talent.TENSION);}};
        this.put("Abo", new Pokemon("Abo", 23, 27, Type.POISON, Type.NONE, talents, 35, 60, 44, 40, 54, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.CORPS_GEL);this.add(Talent.BENET);}};
        this.put("Obalie", new Pokemon("Obalie", 363, 388, Type.GLACE, Type.EAU, talents, 70, 40, 50, 55, 50, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.VENTOUSE);this.add(Talent.SNIPER);this.add(Talent.LUNATIQUE);}};
        this.put("Octillery", new Pokemon("Octillery", 224, 239, Type.EAU, Type.NONE, talents, 75, 105, 75, 105, 75, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLOUTONNERIE);this.add(Talent.ENGRAIS);}};
        this.put("Feuillajou", new Pokemon("Feuillajou", 511, 551, Type.PLANTE, Type.NONE, talents, 50, 53, 48, 53, 48, 64));

        talents = new ArrayList<Talent>(){{this.add(Talent.AURA_INVERSEE);}};
        this.put("Zygarde", new Pokemon("Zygarde", 718, 771, Type.DRAGON, Type.SOL, talents, 108, 100, 121, 81, 95, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);}};
        this.put("Pikachu", new Pokemon("Pikachu", 25, 29, Type.ELECTRIQUE, Type.NONE, talents, 35, 55, 30, 50, 40, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.ILLUSION);}};
        this.put("Zoroark", new Pokemon("Zoroark", 571, 612, Type.TENEBRE, Type.NONE, talents, 60, 105, 60, 120, 60, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.COLOFORCE);}};
        this.put("Mega-Mysdibule", new Pokemon("Mega-Mysdibule", 303, 323, Type.ACIER, Type.FEE, talents, 50, 105, 125, 55, 95, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.FORCE_SABLE);}};
        this.put("Nodulithe", new Pokemon("Nodulithe", 524, 564, Type.ROCHE, Type.NONE, talents, 55, 75, 85, 25, 25, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.PARATONNERRE);this.add(Talent.SOLIDE_ROC);this.add(Talent.TEMERAIRE);}};
        this.put("Rhinastoc", new Pokemon("Rhinastoc", 464, 497, Type.SOL, Type.ROCHE, talents, 115, 140, 130, 55, 55, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_FEERIQUE);}};
        this.put("Mega-Gardevoir", new Pokemon("Mega-Gardevoir", 282, 301, Type.PSY, Type.FEE, talents, 68, 85, 65, 165, 135, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.TURBO);}};
        this.put("Mega-Brasegali", new Pokemon("Mega-Brasegali", 257, 275, Type.FEU, Type.COMBAT, talents, 80, 160, 80, 130, 80, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.MATINAL);this.add(Talent.PICKPOCKET);}};
        this.put("Grainipiot", new Pokemon("Grainipiot", 273, 291, Type.PLANTE, Type.NONE, talents, 40, 40, 50, 30, 30, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.POINT_POISON);this.add(Talent.INTIMIDATION);}};
        this.put("Qwilfish", new Pokemon("Qwilfish", 211, 224, Type.EAU, Type.POISON, talents, 65, 95, 75, 55, 55, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);this.add(Talent.PEAU_DURE);}};
        this.put("Carchacrok", new Pokemon("Carchacrok", 445, 475, Type.DRAGON, Type.SOL, talents, 108, 130, 95, 80, 85, 102));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Latios", new Pokemon("Latios", 381, 406, Type.DRAGON, Type.PSY, talents, 80, 90, 80, 130, 110, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.TEMPO_PERSO);this.add(Talent.GLOUTONNERIE);}};
        this.put("Groret", new Pokemon("Groret", 326, 349, Type.PSY, Type.NONE, talents, 80, 45, 65, 90, 110, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTICIPATION);this.add(Talent.ENVELOCAPE);}};
        this.put("Cheniselle (Cape Plante)", new Pokemon("Cheniselle (Cape Plante)", 413, 441, Type.INSECTE, Type.NONE, talents, 60, 59, 85, 79, 105, 36));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.CORPS_GEL);this.add(Talent.LUNATIQUE);}};
        this.put("Oniglali", new Pokemon("Oniglali", 362, 387, Type.GLACE, Type.NONE, talents, 80, 80, 80, 80, 80, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.FERMETE);this.add(Talent.SANS_LIMITE);}};
        this.put("Steelix", new Pokemon("Steelix", 208, 221, Type.ACIER, Type.SOL, talents, 75, 85, 200, 55, 65, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Crefollet", new Pokemon("Crefollet", 481, 519, Type.PSY, Type.NONE, talents, 80, 105, 105, 105, 105, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Electhor", new Pokemon("Electhor", 145, 155, Type.ELECTRIQUE, Type.VOL, talents, 90, 90, 85, 125, 90, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.VOILE_SABLE);}};
        this.put("Phanpy", new Pokemon("Phanpy", 231, 247, Type.SOL, Type.NONE, talents, 90, 60, 60, 40, 40, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Crehelf", new Pokemon("Crehelf", 480, 518, Type.PSY, Type.NONE, talents, 75, 75, 130, 75, 130, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);}};
        this.put("Ortide", new Pokemon("Ortide", 44, 48, Type.PLANTE, Type.POISON, talents, 60, 65, 70, 85, 75, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.LIGHT_METAL);}};
        this.put("Metalosse", new Pokemon("Metalosse", 376, 401, Type.ACIER, Type.PSY, talents, 80, 135, 130, 95, 90, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.COLOFORCE);this.add(Talent.HERBIVORE);}};
        this.put("Azumarill", new Pokemon("Azumarill", 184, 197, Type.EAU, Type.NONE, talents, 100, 50, 80, 50, 80, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRACHIN);}};
        this.put("Kyogre", new Pokemon("Kyogre", 382, 407, Type.EAU, Type.NONE, talents, 100, 100, 90, 150, 140, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.FARCEUR);}};
        this.put("Mega-Branette", new Pokemon("Mega-Branette", 354, 378, Type.SPECTRE, Type.NONE, talents, 64, 165, 75, 93, 83, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);this.add(Talent.HYPER_CUTTER);this.add(Talent.VACCIN);}};
        this.put("Scorplane", new Pokemon("Scorplane", 207, 220, Type.SOL, Type.VOL, talents, 65, 75, 105, 35, 65, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECRAN_POUDRE);this.add(Talent.FUITE);}};
        this.put("Chenipotte", new Pokemon("Chenipotte", 265, 283, Type.INSECTE, Type.NONE, talents, 45, 45, 35, 20, 30, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);this.add(Talent.ESPRIT_VITAL);}};
        this.put("Elektek", new Pokemon("Elektek", 125, 132, Type.ELECTRIQUE, Type.NONE, talents, 65, 83, 57, 95, 85, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESPRIT_VITAL);}};
        this.put("Vigoroth", new Pokemon("Vigoroth", 288, 307, Type.NORMAL, Type.NONE, talents, 80, 80, 80, 55, 55, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.SERENITE);this.add(Talent.COEUR_SOIN);}};
        this.put("Leveinard", new Pokemon("Leveinard", 113, 119, Type.NORMAL, Type.NONE, talents, 250, 5, 5, 35, 105, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.REGARD_VIF);this.add(Talent.FOUILLE);}};
        this.put("Fouinar", new Pokemon("Fouinar", 162, 174, Type.NORMAL, Type.NONE, talents, 85, 76, 64, 45, 55, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.TETE_DE_ROC);this.add(Talent.PHOBIQUE);}};
        this.put("Simularbre", new Pokemon("Simularbre", 185, 198, Type.ROCHE, Type.NONE, talents, 70, 100, 115, 30, 65, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIDEAU_NEIGE);this.add(Talent.GLISSADE);}};
        this.put("Polagriffe", new Pokemon("Polagriffe", 614, 655, Type.GLACE, Type.NONE, talents, 95, 110, 80, 70, 80, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.CHLOROPHYLE);this.add(Talent.LAVABO);}};
        this.put("Maracachi", new Pokemon("Maracachi", 556, 597, Type.PLANTE, Type.NONE, talents, 75, 86, 67, 106, 67, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_GELEE);this.add(Talent.ALERTE_NEIGE);}};
        this.put("Dragmara", new Pokemon("Dragmara", 699, 746, Type.ROCHE, Type.GLACE, talents, 123, 77, 72, 99, 92, 58));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.TECHNICIEN);this.add(Talent.IMPASSIBLE);}};
        this.put("Insecateur", new Pokemon("Insecateur", 123, 130, Type.INSECTE, Type.VOL, talents, 70, 110, 80, 55, 80, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.MALADRESSE);this.add(Talent.ECHAUFFEMENT);}};
        this.put("Laporeille", new Pokemon("Laporeille", 427, 457, Type.NORMAL, Type.NONE, talents, 55, 66, 44, 44, 56, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);this.add(Talent.REGARD_VIF);this.add(Talent.LENTITEINTEE);}};
        this.put("Hoot-hoot", new Pokemon("Hoot-hoot", 163, 175, Type.NORMAL, Type.VOL, talents, 60, 30, 30, 36, 56, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.COQUE_ARMURE);this.add(Talent.HYDRATATION);}};
        this.put("Lokhlass", new Pokemon("Lokhlass", 131, 140, Type.EAU, Type.GLACE, talents, 130, 85, 80, 85, 95, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.INFILTRATION);}};
        this.put("Spiritomb", new Pokemon("Spiritomb", 442, 472, Type.SPECTRE, Type.TENEBRE, talents, 50, 92, 108, 92, 108, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.ARMUMAGMA);this.add(Talent.CORPS_ARDENT);this.add(Talent.ARMUROUILLEE);}};
        this.put("Limagma", new Pokemon("Limagma", 218, 233, Type.FEU, Type.NONE, talents, 40, 40, 40, 70, 40, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.POSE_SPORE);this.add(Talent.PEAU_SECHE);}};
        this.put("Paras", new Pokemon("Paras", 46, 50, Type.INSECTE, Type.PLANTE, talents, 35, 70, 55, 45, 55, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_ARDENT);this.add(Talent.ESSAIM);}};
        this.put("Pyronille", new Pokemon("Pyronille", 636, 677, Type.INSECTE, Type.FEU, talents, 55, 85, 55, 50, 55, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENVELOCAPE);this.add(Talent.GARDE_MAGIK);this.add(Talent.REGE_FORCE);}};
        this.put("Symbios", new Pokemon("Symbios", 579, 620, Type.PSY, Type.NONE, talents, 110, 65, 75, 125, 85, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.GARDE_MAGIK);this.add(Talent.GARDE_AMIE);}};
        this.put("Melo", new Pokemon("Melo", 173, 185, Type.NORMAL, Type.NONE, talents, 50, 25, 28, 45, 55, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.CONTESTATION);}};
        this.put("Lianaja", new Pokemon("Lianaja", 496, 536, Type.PLANTE, Type.NONE, talents, 60, 60, 75, 60, 75, 83));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.DELESTAGE);}};
        this.put("Arcko", new Pokemon("Arcko", 252, 269, Type.PLANTE, Type.NONE, talents, 40, 45, 35, 65, 55, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);this.add(Talent.IGNIFUGE);this.add(Talent.HEAVY_METAL);}};
        this.put("Archeomire", new Pokemon("Archeomire", 436, 466, Type.ACIER, Type.PSY, talents, 57, 24, 86, 24, 86, 23));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.FOUILLE);this.add(Talent.INSOMNIA);}};
        this.put("Banshitrouye (Taille Normale)", new Pokemon("Banshitrouye (Taille Normale)", 711, 762, Type.SPECTRE, Type.PLANTE, talents, 65, 90, 122, 58, 75, 84));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Feuforeve", new Pokemon("Feuforeve", 200, 213, Type.SPECTRE, Type.NONE, talents, 60, 60, 60, 85, 85, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEGA_BLASTER);}};
        this.put("Mega-Tortank", new Pokemon("Mega-Tortank", 9, 13, Type.EAU, Type.NONE, talents, 79, 103, 120, 135, 115, 78));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.ESSAIM);this.add(Talent.PIED_VELOCE);}};
        this.put("Venipatte", new Pokemon("Venipatte", 543, 583, Type.INSECTE, Type.POISON, talents, 30, 45, 59, 30, 39, 57));

        talents = new ArrayList<Talent>(){{this.add(Talent.FARCEUR);this.add(Talent.INFILTRATION);this.add(Talent.CHLOROPHYLE);}};
        this.put("Doudouvet", new Pokemon("Doudouvet", 546, 586, Type.PLANTE, Type.NONE, talents, 40, 27, 60, 37, 50, 66));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.HYDRATATION);this.add(Talent.CORPS_GEL);}};
        this.put("Lamantine", new Pokemon("Lamantine", 87, 92, Type.EAU, Type.GLACE, talents, 90, 70, 80, 70, 95, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.POSE_SPORE);this.add(Talent.PEAU_SECHE);}};
        this.put("Parasect", new Pokemon("Parasect", 47, 51, Type.INSECTE, Type.PLANTE, talents, 60, 95, 80, 60, 80, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.SUINTEMENT);this.add(Talent.GLUE);this.add(Talent.GLOUTONNERIE);}};
        this.put("Avaltout", new Pokemon("Avaltout", 317, 340, Type.POISON, Type.NONE, talents, 100, 73, 83, 73, 83, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTI_BRUIT);this.add(Talent.STATIK);this.add(Talent.BOOM_FINAL);}};
        this.put("Voltorbe", new Pokemon("Voltorbe", 100, 106, Type.ELECTRIQUE, Type.NONE, talents, 40, 30, 50, 55, 55, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.PHOBIQUE);}};
        this.put("Magicarpe", new Pokemon("Magicarpe", 129, 137, Type.EAU, Type.NONE, talents, 20, 10, 55, 15, 20, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.SANS_LIMITE);this.add(Talent.MODE_TRANSE);}};
        this.put("Darumacho (Mode Normal)", new Pokemon("Darumacho (Mode Normal)", 555, 595, Type.FEU, Type.NONE, talents, 105, 140, 55, 30, 55, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.QUERELLEUR);}};
        this.put("Heledelle", new Pokemon("Heledelle", 277, 295, Type.NORMAL, Type.VOL, talents, 60, 85, 60, 50, 50, 125));

        talents = new ArrayList<Talent>(){{this.add(Talent.EPINE_DE_FER);}};
        this.put("Noacier", new Pokemon("Noacier", 598, 639, Type.PLANTE, Type.ACIER, talents, 74, 94, 131, 54, 116, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.MOITEUR);}};
        this.put("Laggron", new Pokemon("Laggron", 260, 278, Type.EAU, Type.SOL, talents, 100, 110, 90, 85, 90, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.MOITEUR);}};
        this.put("Gobou", new Pokemon("Gobou", 258, 276, Type.EAU, Type.NONE, talents, 50, 70, 50, 50, 50, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.REGARD_VIF);this.add(Talent.ACHARNE);}};
        this.put("Canarticho", new Pokemon("Canarticho", 83, 88, Type.NORMAL, Type.VOL, talents, 52, 65, 55, 58, 62, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.SECHERESSE);}};
        this.put("Groudon", new Pokemon("Groudon", 383, 408, Type.SOL, Type.NONE, talents, 100, 150, 140, 100, 90, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.ALERTE_NEIGE);this.add(Talent.ANTI_BRUIT);}};
        this.put("Blizzaroi", new Pokemon("Blizzaroi", 460, 492, Type.PLANTE, Type.GLACE, talents, 90, 92, 75, 92, 85, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FORCE_SOLEIL);this.add(Talent.MATINAL);}};
        this.put("Tournegrin", new Pokemon("Tournegrin", 191, 204, Type.PLANTE, Type.NONE, talents, 30, 30, 30, 30, 30, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.RIVALITE);this.add(Talent.SANS_LIMITE);}};
        this.put("Nidoqueen", new Pokemon("Nidoqueen", 31, 35, Type.POISON, Type.SOL, talents, 90, 82, 87, 75, 85, 76));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.CIEL_GRIS);}};
        this.put("Altaria", new Pokemon("Altaria", 334, 357, Type.DRAGON, Type.VOL, talents, 75, 70, 90, 70, 105, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.PIED_CONFUS);this.add(Talent.COEUR_DE_COQ);}};
        this.put("Roucool", new Pokemon("Roucool", 16, 20, Type.NORMAL, Type.VOL, talents, 40, 45, 40, 35, 35, 56));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTICIPATION);this.add(Talent.PEAU_SECHE);this.add(Talent.TOXITOUCHE);}};
        this.put("Cradopaud", new Pokemon("Cradopaud", 453, 485, Type.POISON, Type.COMBAT, talents, 48, 61, 40, 61, 40, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.MATINAL);this.add(Talent.TENSION);}};
        this.put("Malosse", new Pokemon("Malosse", 228, 243, Type.TENEBRE, Type.FEU, talents, 45, 60, 30, 80, 50, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_DE_COQ);this.add(Talent.ENVELOCAPE);this.add(Talent.ARMUROUILLEE);}};
        this.put("Vaututrice", new Pokemon("Vaututrice", 630, 671, Type.TENEBRE, Type.VOL, talents, 110, 65, 105, 55, 95, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.SERENITE);this.add(Talent.AGITATION);this.add(Talent.CHANCEUX);}};
        this.put("Togekiss", new Pokemon("Togekiss", 468, 501, Type.NORMAL, Type.VOL, talents, 85, 50, 95, 120, 115, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.HYDRATATION);this.add(Talent.ABSORB_EAU);}};
        this.put("Tritonde", new Pokemon("Tritonde", 535, 575, Type.EAU, Type.NONE, talents, 50, 50, 40, 50, 40, 64));

        talents = new ArrayList<Talent>(){{this.add(Talent.PUANTEUR);this.add(Talent.BOOM_FINAL);}};
        this.put("Moufflair", new Pokemon("Moufflair", 435, 465, Type.POISON, Type.TENEBRE, talents, 103, 93, 67, 71, 61, 84));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.ACHARNE);}};
        this.put("Tiplouf", new Pokemon("Tiplouf", 393, 421, Type.EAU, Type.NONE, talents, 53, 51, 53, 61, 56, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.LENTITEINTEE);this.add(Talent.FARCEUR);}};
        this.put("Lumivole", new Pokemon("Lumivole", 314, 337, Type.INSECTE, Type.NONE, talents, 65, 47, 55, 73, 75, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);}};
        this.put("Carmache", new Pokemon("Carmache", 444, 474, Type.DRAGON, Type.SOL, talents, 68, 90, 65, 50, 55, 82));

        talents = new ArrayList<Talent>(){{this.add(Talent.PLUS);this.add(Talent.MINUS);this.add(Talent.CORPS_SAIN);}};
        this.put("Cliticlic", new Pokemon("Cliticlic", 601, 642, Type.ACIER, Type.NONE, talents, 60, 100, 115, 70, 85, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);this.add(Talent.PRESSION);this.add(Talent.TELEPATHE);}};
        this.put("Giratina (Forme Originelle)", new Pokemon("Giratina (Forme Originelle)", 487, 526, Type.SPECTRE, Type.DRAGON, talents, 150, 120, 100, 120, 100, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.TURBO);}};
        this.put("Poussifeu", new Pokemon("Poussifeu", 255, 272, Type.FEU, Type.NONE, talents, 45, 60, 40, 70, 50, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYDRATATION);this.add(Talent.GLUE);this.add(Talent.DELESTAGE);}};
        this.put("Limaspeed", new Pokemon("Limaspeed", 617, 658, Type.INSECTE, Type.NONE, talents, 80, 70, 40, 100, 60, 145));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_SECHE);this.add(Talent.VOILE_SABLE);this.add(Talent.FORCE_SOLEIL);}};
        this.put("Iguolta", new Pokemon("Iguolta", 695, 742, Type.ELECTRIQUE, Type.NORMAL, talents, 62, 55, 52, 109, 94, 109));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);this.add(Talent.ENVELOCAPE);}};
        this.put("Cheniti", new Pokemon("Cheniti", 412, 440, Type.INSECTE, Type.NONE, talents, 40, 29, 45, 29, 45, 36));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.TECHNICIEN);this.add(Talent.IMPASSIBLE);}};
        this.put("Kapoera", new Pokemon("Kapoera", 237, 253, Type.COMBAT, Type.NONE, talents, 50, 95, 95, 35, 110, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.RAMASSAGE);this.add(Talent.ABSORB_VOLT);}};
        this.put("Pachirisu", new Pokemon("Pachirisu", 417, 447, Type.ELECTRIQUE, Type.NONE, talents, 60, 45, 70, 45, 90, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.COLOFORCE);this.add(Talent.HERBIVORE);}};
        this.put("Marill", new Pokemon("Marill", 183, 196, Type.EAU, Type.NONE, talents, 70, 20, 50, 20, 50, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.ADAPTABILITE);}};
        this.put("Mega-Lucario", new Pokemon("Mega-Lucario", 448, 480, Type.ACIER, Type.COMBAT, talents, 70, 145, 88, 140, 70, 112));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.NORMALISE);}};
        this.put("Skitty", new Pokemon("Skitty", 300, 319, Type.NORMAL, Type.NONE, talents, 50, 45, 45, 35, 35, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.ATTENTION);this.add(Talent.GARDE_MAGIK);}};
        this.put("Abra", new Pokemon("Abra", 63, 67, Type.PSY, Type.NONE, talents, 25, 20, 15, 105, 55, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.FEUIL_GARDE);this.add(Talent.CHLOROPHYLE);this.add(Talent.ENVELOCAPE);}};
        this.put("Couverdure", new Pokemon("Couverdure", 541, 581, Type.INSECTE, Type.PLANTE, talents, 55, 63, 90, 50, 80, 42));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.BATTANT);this.add(Talent.FOUILLE);}};
        this.put("Grodoudou", new Pokemon("Grodoudou", 40, 44, Type.NORMAL, Type.NONE, talents, 140, 70, 45, 75, 50, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.PROGNATHE);}};
        this.put("Ptyranidur", new Pokemon("Ptyranidur", 696, 743, Type.ROCHE, Type.DRAGON, talents, 58, 89, 77, 45, 45, 48));

        talents = new ArrayList<Talent>(){{this.add(Talent.DEGUISEMENT);this.add(Talent.PROTEEN);}};
        this.put("Kecleon", new Pokemon("Kecleon", 352, 375, Type.NORMAL, Type.NONE, talents, 60, 90, 70, 60, 120, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Deoxys (Forme Vitesse)", new Pokemon("Deoxys (Forme Vitesse)", 386, 414, Type.PSY, Type.NONE, talents, 50, 95, 90, 95, 90, 180));

        talents = new ArrayList<Talent>(){{this.add(Talent.COQUE_ARMURE);this.add(Talent.MULTI_COUPS);this.add(Talent.ENVELOCAPE);}};
        this.put("Crustabri", new Pokemon("Crustabri", 91, 96, Type.EAU, Type.GLACE, talents, 50, 95, 180, 85, 45, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Motisma (Forme Chaleur)", new Pokemon("Motisma (Forme Chaleur)", 479, 513, Type.ELECTRIQUE, Type.SPECTRE, talents, 50, 65, 107, 105, 107, 86));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_SECHE);this.add(Talent.VOILE_SABLE);this.add(Talent.FORCE_SOLEIL);}};
        this.put("Galvaran", new Pokemon("Galvaran", 694, 741, Type.ELECTRIQUE, Type.NORMAL, talents, 44, 38, 33, 61, 43, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_SOIN);this.add(Talent.AROMA_VOILE);}};
        this.put("Fluvetin", new Pokemon("Fluvetin", 682, 729, Type.FEE, Type.NONE, talents, 78, 52, 60, 63, 65, 23));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.HERBIVORE);this.add(Talent.SERENITE);}};
        this.put("Haydaim", new Pokemon("Haydaim", 586, 627, Type.NORMAL, Type.PLANTE, talents, 80, 100, 70, 60, 70, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Kyurem (Noir)", new Pokemon("Kyurem (Noir)", 646, 690, Type.DRAGON, Type.GLACE, talents, 125, 170, 100, 120, 90, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.SABLE_VOLANT);this.add(Talent.FORCE_SABLE);}};
        this.put("Hippopotas", new Pokemon("Hippopotas", 449, 481, Type.SOL, Type.NONE, talents, 68, 72, 78, 38, 42, 32));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);this.add(Talent.PRESSION);this.add(Talent.TELEPATHE);}};
        this.put("Giratina (Forme Alternative)", new Pokemon("Giratina (Forme Alternative)", 487, 525, Type.SPECTRE, Type.DRAGON, talents, 150, 100, 120, 100, 120, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);}};
        this.put("Coconfort", new Pokemon("Coconfort", 14, 18, Type.INSECTE, Type.POISON, talents, 45, 25, 50, 25, 25, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.RECOLTE);}};
        this.put("Noeunoeuf", new Pokemon("Noeunoeuf", 102, 108, Type.PLANTE, Type.PSY, talents, 60, 40, 80, 60, 45, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.GLOUTONNERIE);this.add(Talent.PIED_VELOCE);}};
        this.put("Zigzaton", new Pokemon("Zigzaton", 263, 281, Type.NORMAL, Type.NONE, talents, 38, 30, 41, 30, 41, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.FUITE);this.add(Talent.AGITATION);}};
        this.put("Rattata", new Pokemon("Rattata", 19, 23, Type.NORMAL, Type.NONE, talents, 30, 56, 35, 25, 35, 72));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.MATINAL);this.add(Talent.HERBIVORE);}};
        this.put("Girafarig", new Pokemon("Girafarig", 203, 216, Type.NORMAL, Type.PSY, talents, 70, 80, 65, 90, 65, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.HYDRATATION);this.add(Talent.CORPS_GEL);}};
        this.put("Otaria", new Pokemon("Otaria", 86, 91, Type.EAU, Type.NONE, talents, 65, 45, 55, 45, 70, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.PIED_VELOCE);this.add(Talent.INTIMIDATION);this.add(Talent.PHOBIQUE);}};
        this.put("Granbull", new Pokemon("Granbull", 210, 223, Type.NORMAL, Type.NONE, talents, 90, 120, 75, 60, 60, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.ARMURBASTON);this.add(Talent.ARMUROUILLEE);}};
        this.put("Kabutops", new Pokemon("Kabutops", 141, 150, Type.ROCHE, Type.EAU, talents, 60, 115, 105, 65, 70, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.REGARD_VIF);this.add(Talent.ANALYSTE);}};
        this.put("Ratentif", new Pokemon("Ratentif", 504, 544, Type.NORMAL, Type.NONE, talents, 45, 55, 39, 35, 39, 42));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTICIPATION);this.add(Talent.ENVELOCAPE);}};
        this.put("Cheniselle (Cape Sol)", new Pokemon("Cheniselle (Cape Sol)", 413, 442, Type.INSECTE, Type.NONE, talents, 60, 79, 105, 59, 85, 36));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.CHLOROPHYLE);}};
        this.put("Bulbizarre", new Pokemon("Bulbizarre", 1, 1, Type.PLANTE, Type.POISON, talents, 45, 49, 49, 65, 65, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.TOISON_EPAISSE);}};
        this.put("Couafarel", new Pokemon("Couafarel", 676, 722, Type.NORMAL, Type.NONE, talents, 75, 80, 60, 65, 90, 102));

        talents = new ArrayList<Talent>(){{this.add(Talent.FORCE_SOLEIL);}};
        this.put("Mega-Demolosse", new Pokemon("Mega-Demolosse", 229, 245, Type.TENEBRE, Type.FEU, talents, 75, 90, 90, 140, 90, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.FOUILLE);this.add(Talent.MARQUE_OMBRE);}};
        this.put("Siderella", new Pokemon("Siderella", 576, 617, Type.PSY, Type.NONE, talents, 70, 55, 95, 95, 110, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.BAJOUES);this.add(Talent.PLUS);}};
        this.put("Dedenne", new Pokemon("Dedenne", 702, 749, Type.ELECTRIQUE, Type.FEE, talents, 67, 58, 57, 81, 67, 101));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.CHLOROPHYLE);}};
        this.put("Herbizarre", new Pokemon("Herbizarre", 2, 2, Type.PLANTE, Type.POISON, talents, 62, 62, 63, 80, 80, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.RIVALITE);this.add(Talent.CRAN);}};
        this.put("Lixy", new Pokemon("Lixy", 403, 431, Type.ELECTRIQUE, Type.NONE, talents, 45, 65, 34, 40, 34, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.PIED_CONFUS);this.add(Talent.COEUR_DE_COQ);}};
        this.put("Roucarnage", new Pokemon("Roucarnage", 18, 22, Type.NORMAL, Type.VOL, talents, 83, 80, 75, 70, 70, 91));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.MAGNEPIEGE);this.add(Talent.FORCE_SABLE);}};
        this.put("Tarinor", new Pokemon("Tarinor", 299, 318, Type.ROCHE, Type.NONE, talents, 30, 45, 135, 45, 90, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.SNIPER);}};
        this.put("Rapasdepic", new Pokemon("Rapasdepic", 22, 26, Type.NORMAL, Type.VOL, talents, 65, 90, 65, 61, 61, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);}};
        this.put("Embrylex", new Pokemon("Embrylex", 246, 262, Type.ROCHE, Type.SOL, talents, 50, 64, 50, 45, 50, 41));

        talents = new ArrayList<Talent>(){{this.add(Talent.SERENITE);this.add(Talent.AGITATION);this.add(Talent.CHANCEUX);}};
        this.put("Togetic", new Pokemon("Togetic", 176, 188, Type.NORMAL, Type.VOL, talents, 55, 40, 85, 80, 105, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.FILTRE);}};
        this.put("Mega-Galeking", new Pokemon("Mega-Galeking", 306, 327, Type.ACIER, Type.NONE, talents, 70, 140, 230, 60, 80, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTI_BRUIT);this.add(Talent.QUERELLEUR);}};
        this.put("Brouhabam", new Pokemon("Brouhabam", 295, 314, Type.NORMAL, Type.NONE, talents, 104, 91, 63, 91, 63, 68));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.ABSORB_EAU);}};
        this.put("Babimanta", new Pokemon("Babimanta", 458, 490, Type.EAU, Type.VOL, talents, 45, 20, 50, 60, 120, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.INCONSCIENT);this.add(Talent.MALADRESSE);this.add(Talent.SIMPLE);}};
        this.put("Rhinolove", new Pokemon("Rhinolove", 528, 568, Type.PSY, Type.VOL, talents, 67, 57, 55, 77, 55, 114));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.CHLOROPHYLE);}};
        this.put("Florizarre", new Pokemon("Florizarre", 3, 3, Type.PLANTE, Type.POISON, talents, 80, 82, 83, 100, 100, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.COQUE_ARMURE);}};
        this.put("Clamiral", new Pokemon("Clamiral", 503, 543, Type.EAU, Type.NONE, talents, 95, 100, 85, 108, 70, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.VACCIN);this.add(Talent.ISOGRAISSE);this.add(Talent.GLOUTONNERIE);}};
        this.put("Ronflex", new Pokemon("Ronflex", 143, 153, Type.NORMAL, Type.NONE, talents, 160, 110, 65, 65, 110, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Kyurem (Blanc)", new Pokemon("Kyurem (Blanc)", 646, 691, Type.DRAGON, Type.GLACE, talents, 125, 120, 90, 170, 100, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.PUANTEUR);this.add(Talent.GLUE);this.add(Talent.TOXITOUCHE);}};
        this.put("Grotadmorv", new Pokemon("Grotadmorv", 89, 94, Type.POISON, Type.NONE, talents, 105, 105, 75, 65, 100, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.MOITEUR);this.add(Talent.GLISSADE);}};
        this.put("Ptitard", new Pokemon("Ptitard", 60, 64, Type.EAU, Type.NONE, talents, 40, 50, 40, 40, 40, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.MIROIR_MAGIK);}};
        this.put("Mentali", new Pokemon("Mentali", 196, 209, Type.PSY, Type.NONE, talents, 65, 65, 60, 130, 95, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.SANS_LIMITE);this.add(Talent.POING_DE_FER);}};
        this.put("Betochef", new Pokemon("Betochef", 534, 574, Type.COMBAT, Type.NONE, talents, 105, 140, 95, 55, 65, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.LUMIATTIRANCE);this.add(Talent.ANALYSTE);}};
        this.put("Stari", new Pokemon("Stari", 120, 127, Type.EAU, Type.NONE, talents, 30, 45, 55, 70, 55, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.DEFAITISTE);}};
        this.put("Arkeapti", new Pokemon("Arkeapti", 566, 607, Type.ROCHE, Type.VOL, talents, 55, 112, 45, 74, 45, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.IMPUDENCE);this.add(Talent.COLERIQUE);}};
        this.put("Crocorible", new Pokemon("Crocorible", 553, 593, Type.SOL, Type.TENEBRE, talents, 95, 117, 70, 65, 70, 92));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.CORPS_ARDENT);}};
        this.put("Heatran", new Pokemon("Heatran", 485, 523, Type.FEU, Type.ACIER, talents, 91, 90, 106, 130, 106, 77));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.TORCHE);this.add(Talent.CORPS_ARDENT);}};
        this.put("Ponyta", new Pokemon("Ponyta", 77, 82, Type.FEU, Type.NONE, talents, 50, 85, 55, 65, 65, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Crefadet", new Pokemon("Crefadet", 482, 520, Type.PSY, Type.NONE, talents, 75, 125, 70, 125, 70, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.IMPUDENCE);this.add(Talent.COLERIQUE);}};
        this.put("Escroco", new Pokemon("Escroco", 552, 592, Type.SOL, Type.TENEBRE, talents, 60, 82, 45, 45, 45, 74));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.CRAN);this.add(Talent.SANS_LIMITE);}};
        this.put("Hariyama", new Pokemon("Hariyama", 297, 316, Type.COMBAT, Type.NONE, talents, 144, 120, 60, 40, 60, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.MARQUE_OMBRE);this.add(Talent.TELEPATHE);}};
        this.put("Qulbutoke", new Pokemon("Qulbutoke", 202, 215, Type.PSY, Type.NONE, talents, 190, 33, 58, 33, 58, 33));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.LUMIATTIRANCE);this.add(Talent.ANALYSTE);}};
        this.put("Staross", new Pokemon("Staross", 121, 128, Type.EAU, Type.PSY, talents, 60, 75, 85, 100, 85, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Hexagel", new Pokemon("Hexagel", 615, 656, Type.GLACE, Type.NONE, talents, 70, 50, 30, 95, 135, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.PREDICTION);this.add(Talent.HYDRATATION);}};
        this.put("Lippouti", new Pokemon("Lippouti", 238, 254, Type.GLACE, Type.PSY, talents, 45, 30, 15, 85, 65, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.ANTI_BRUIT);}};
        this.put("Bastiodon", new Pokemon("Bastiodon", 411, 439, Type.ROCHE, Type.ACIER, talents, 60, 52, 168, 47, 138, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);this.add(Talent.GARDE_AMIE);}};
        this.put("Peregrain", new Pokemon("Peregrain", 665, 711, Type.INSECTE, Type.NONE, talents, 45, 22, 60, 37, 30, 29));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_DURE);}};
        this.put("Carvanha", new Pokemon("Carvanha", 318, 341, Type.EAU, Type.TENEBRE, talents, 45, 90, 20, 65, 20, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);}};
        this.put("Pharamp", new Pokemon("Pharamp", 181, 193, Type.ELECTRIQUE, Type.NONE, talents, 90, 75, 75, 115, 90, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.FORCE_PURE);}};
        this.put("Mega-Charmina", new Pokemon("Mega-Charmina", 308, 330, Type.COMBAT, Type.PSY, talents, 60, 100, 85, 80, 85, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FEUIL_GARDE);this.add(Talent.REGE_FORCE);}};
        this.put("Bouldeneu", new Pokemon("Bouldeneu", 465, 498, Type.PLANTE, Type.NONE, talents, 100, 100, 125, 110, 50, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FORCE_SOLEIL);this.add(Talent.MATINAL);}};
        this.put("Heliatronc", new Pokemon("Heliatronc", 192, 205, Type.PLANTE, Type.NONE, talents, 75, 75, 55, 105, 85, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEGA_BLASTER);}};
        this.put("Gamblast", new Pokemon("Gamblast", 693, 740, Type.EAU, Type.NONE, talents, 71, 73, 88, 120, 89, 59));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Eoko", new Pokemon("Eoko", 358, 382, Type.PSY, Type.NONE, talents, 65, 50, 70, 95, 80, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECHAUFFEMENT);this.add(Talent.DELESTAGE);this.add(Talent.BRISE_MOULE);}};
        this.put("Brutalibre", new Pokemon("Brutalibre", 701, 748, Type.COMBAT, Type.VOL, talents, 70, 95, 80, 65, 70, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.SANS_LIMITE);this.add(Talent.AGITATION);}};
        this.put("Furaiglon", new Pokemon("Furaiglon", 627, 668, Type.NORMAL, Type.VOL, talents, 70, 83, 50, 37, 50, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.HERBIVORE);}};
        this.put("Chevroum", new Pokemon("Chevroum", 673, 719, Type.PLANTE, Type.NONE, talents, 123, 100, 62, 97, 81, 68));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLOUTONNERIE);this.add(Talent.BRASIER);}};
        this.put("Flamoutan", new Pokemon("Flamoutan", 514, 554, Type.FEU, Type.NONE, talents, 75, 98, 63, 98, 63, 101));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);this.add(Talent.ECRAN_POUDRE);this.add(Talent.GARDE_AMIE);}};
        this.put("Prismillon", new Pokemon("Prismillon", 666, 712, Type.INSECTE, Type.VOL, talents, 80, 52, 50, 90, 50, 89));

        talents = new ArrayList<Talent>(){{this.add(Talent.FOUILLE);this.add(Talent.INFILTRATION);this.add(Talent.TELEPATHE);}};
        this.put("Sonistrelle", new Pokemon("Sonistrelle", 714, 767, Type.VOL, Type.DRAGON, talents, 70, 60, 60, 82, 60, 97));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.SECHERESSE);}};
        this.put("Goupix", new Pokemon("Goupix", 37, 41, Type.FEU, Type.NONE, talents, 38, 41, 40, 50, 65, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.FERMETE);}};
        this.put("Gravalanch", new Pokemon("Gravalanch", 75, 80, Type.ROCHE, Type.SOL, talents, 55, 95, 115, 45, 45, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.INFILTRATION);}};
        this.put("Nostenfer", new Pokemon("Nostenfer", 169, 181, Type.POISON, Type.VOL, talents, 85, 90, 80, 70, 80, 130));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.GLOUTONNERIE);}};
        this.put("Chetiflor", new Pokemon("Chetiflor", 69, 74, Type.PLANTE, Type.POISON, talents, 50, 75, 35, 70, 30, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Motisma (Forme Lavage)", new Pokemon("Motisma (Forme Lavage)", 479, 514, Type.ELECTRIQUE, Type.SPECTRE, talents, 50, 65, 107, 105, 107, 86));

        talents = new ArrayList<Talent>(){{this.add(Talent.LAVABO);}};
        this.put("Lumineon", new Pokemon("Lumineon", 457, 489, Type.EAU, Type.NONE, talents, 69, 69, 76, 69, 86, 91));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.PROTEEN);}};
        this.put("Croaporal", new Pokemon("Croaporal", 657, 703, Type.EAU, Type.NONE, talents, 54, 63, 52, 83, 56, 97));

        talents = new ArrayList<Talent>(){{this.add(Talent.PARATONNERRE);this.add(Talent.TETE_DE_ROC);this.add(Talent.TEMERAIRE);}};
        this.put("Rhinocorne", new Pokemon("Rhinocorne", 111, 117, Type.SOL, Type.ROCHE, talents, 80, 85, 95, 30, 30, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.IMPUDENCE);}};
        this.put("Leviator", new Pokemon("Leviator", 130, 138, Type.EAU, Type.VOL, talents, 95, 125, 79, 60, 100, 81));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_MIRACLE);this.add(Talent.GARDE_MAGIK);this.add(Talent.LENTITEINTEE);}};
        this.put("Cryptero", new Pokemon("Cryptero", 561, 602, Type.PSY, Type.VOL, talents, 72, 58, 80, 103, 80, 97));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.TEMPO_PERSO);}};
        this.put("Spoink", new Pokemon("Spoink", 325, 348, Type.PSY, Type.NONE, talents, 60, 25, 35, 70, 80, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.TELEPATHE);}};
        this.put("Dialga", new Pokemon("Dialga", 483, 521, Type.ACIER, Type.DRAGON, talents, 100, 120, 120, 150, 100, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);this.add(Talent.BAIGNE_SABLE);}};
        this.put("Sabelette", new Pokemon("Sabelette", 27, 31, Type.SOL, Type.NONE, talents, 50, 75, 85, 20, 30, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.PARATONNERRE);this.add(Talent.STATIK);}};
        this.put("Dynavolt", new Pokemon("Dynavolt", 309, 331, Type.ELECTRIQUE, Type.NONE, talents, 40, 45, 40, 65, 40, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);this.add(Talent.PARATONNERRE);}};
        this.put("Pichu", new Pokemon("Pichu", 172, 184, Type.ELECTRIQUE, Type.NONE, talents, 20, 40, 15, 35, 35, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_NOBLE);}};
        this.put("Terrakium", new Pokemon("Terrakium", 639, 680, Type.ROCHE, Type.COMBAT, talents, 91, 129, 90, 72, 90, 108));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_GELEE);}};
        this.put("Amagara", new Pokemon("Amagara", 698, 745, Type.ROCHE, Type.GLACE, talents, 77, 59, 50, 67, 63, 46));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.IGNIFU_VOILE);}};
        this.put("Poissirene", new Pokemon("Poissirene", 118, 125, Type.EAU, Type.NONE, talents, 45, 67, 60, 35, 50, 63));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_ARDENT);this.add(Talent.ESPRIT_VITAL);}};
        this.put("Magby", new Pokemon("Magby", 240, 256, Type.FEU, Type.NONE, talents, 45, 75, 37, 70, 55, 83));

        talents = new ArrayList<Talent>(){{this.add(Talent.FARCEUR);this.add(Talent.INFILTRATION);this.add(Talent.CHLOROPHYLE);}};
        this.put("Farfaduvet", new Pokemon("Farfaduvet", 547, 587, Type.PLANTE, Type.NONE, talents, 60, 67, 85, 77, 75, 116));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.MALADRESSE);this.add(Talent.ECHAUFFEMENT);}};
        this.put("Lockpin", new Pokemon("Lockpin", 428, 458, Type.NORMAL, Type.NONE, talents, 65, 76, 84, 54, 96, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_VOLT);this.add(Talent.LUMIATTIRANCE);this.add(Talent.ABSORB_EAU);}};
        this.put("Loupio", new Pokemon("Loupio", 170, 182, Type.EAU, Type.ELECTRIQUE, talents, 75, 38, 38, 56, 56, 67));

        talents = new ArrayList<Talent>(){{this.add(Talent.PARATONNERRE);this.add(Talent.STATIK);this.add(Talent.MINUS);}};
        this.put("Elecsprint", new Pokemon("Elecsprint", 310, 332, Type.ELECTRIQUE, Type.NONE, talents, 70, 75, 60, 105, 60, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.FOUILLE);this.add(Talent.INSOMNIA);}};
        this.put("Banshitrouye (Taille Ultra)", new Pokemon("Banshitrouye (Taille Ultra)", 711, 764, Type.SPECTRE, Type.PLANTE, talents, 85, 100, 122, 58, 75, 54));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_NOBLE);}};
        this.put("Keldeo", new Pokemon("Keldeo", 647, 692, Type.EAU, Type.COMBAT, talents, 91, 72, 90, 129, 90, 108));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.DELESTAGE);}};
        this.put("Jungko", new Pokemon("Jungko", 254, 271, Type.PLANTE, Type.NONE, talents, 70, 85, 65, 105, 85, 120));

        talents = new ArrayList<Talent>(){{this.add(Talent.FARCEUR);this.add(Talent.ACHARNE);}};
        this.put("Boreas (Forme Avatar)", new Pokemon("Boreas (Forme Avatar)", 641, 682, Type.VOL, Type.NONE, talents, 79, 115, 70, 125, 80, 111));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.LIGHT_METAL);}};
        this.put("Registeel", new Pokemon("Registeel", 379, 404, Type.ACIER, Type.NONE, talents, 80, 75, 150, 75, 150, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.MATINAL);this.add(Talent.MIROIR_MAGIK);}};
        this.put("Xatu", new Pokemon("Xatu", 178, 190, Type.PSY, Type.VOL, talents, 65, 75, 70, 95, 70, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Skelenox", new Pokemon("Skelenox", 355, 379, Type.SPECTRE, Type.NONE, talents, 20, 40, 90, 30, 90, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);}};
        this.put("Etourmi", new Pokemon("Etourmi", 396, 424, Type.NORMAL, Type.VOL, talents, 40, 55, 30, 30, 30, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECRAN_POUDRE);this.add(Talent.LENTITEINTEE);}};
        this.put("Aeromite", new Pokemon("Aeromite", 49, 53, Type.INSECTE, Type.POISON, talents, 70, 65, 60, 90, 75, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.CUVETTE);}};
        this.put("Tortank", new Pokemon("Tortank", 9, 12, Type.EAU, Type.NONE, talents, 79, 83, 100, 85, 105, 78));

        talents = new ArrayList<Talent>(){{this.add(Talent.TECHNICIEN);}};
        this.put("Mega-Cizayox", new Pokemon("Mega-Cizayox", 212, 226, Type.INSECTE, Type.ACIER, talents, 70, 150, 140, 65, 100, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);this.add(Talent.ECAILLE_SPECIALE);}};
        this.put("Minidraco", new Pokemon("Minidraco", 147, 157, Type.DRAGON, Type.NONE, talents, 41, 64, 45, 50, 50, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Trioxhydre", new Pokemon("Trioxhydre", 635, 676, Type.TENEBRE, Type.DRAGON, talents, 92, 105, 90, 125, 90, 98));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.GARDE_MAGIK);this.add(Talent.GARDE_AMIE);}};
        this.put("Melofee", new Pokemon("Melofee", 35, 39, Type.NORMAL, Type.NONE, talents, 70, 45, 48, 60, 65, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.COQUE_ARMURE);this.add(Talent.ARMUROUILLEE);}};
        this.put("Crabicoque", new Pokemon("Crabicoque", 557, 598, Type.INSECTE, Type.ROCHE, talents, 50, 65, 85, 35, 35, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.COQUE_ARMURE);}};
        this.put("Torterra", new Pokemon("Torterra", 389, 417, Type.PLANTE, Type.SOL, talents, 95, 109, 105, 75, 85, 56));

        talents = new ArrayList<Talent>(){{this.add(Talent.BAIGNE_SABLE);this.add(Talent.FORCE_SABLE);this.add(Talent.BRISE_MOULE);}};
        this.put("Rototaupe", new Pokemon("Rototaupe", 529, 569, Type.SOL, Type.NONE, talents, 60, 85, 40, 30, 45, 68));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);}};
        this.put("Ceribou", new Pokemon("Ceribou", 420, 450, Type.PLANTE, Type.NONE, talents, 45, 35, 45, 62, 53, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.SIMPLE);this.add(Talent.INCONSCIENT);this.add(Talent.LUNATIQUE);}};
        this.put("Keunotor", new Pokemon("Keunotor", 399, 427, Type.NORMAL, Type.NONE, talents, 59, 45, 40, 35, 40, 31));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.RIVALITE);this.add(Talent.AGITATION);}};
        this.put("Nidoran F", new Pokemon("Nidoran F", 29, 33, Type.POISON, Type.NONE, talents, 55, 47, 52, 40, 40, 41));

        talents = new ArrayList<Talent>(){{this.add(Talent.TENSION);this.add(Talent.RIVALITE);this.add(Talent.IMPUDENCE);}};
        this.put("Helionceau", new Pokemon("Helionceau", 667, 713, Type.FEU, Type.NORMAL, talents, 62, 50, 58, 73, 54, 72));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.TORCHE);}};
        this.put("Entei", new Pokemon("Entei", 244, 260, Type.FEU, Type.NONE, talents, 115, 115, 85, 90, 75, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.RIVALITE);this.add(Talent.AGITATION);}};
        this.put("Nidoran M", new Pokemon("Nidoran M", 32, 36, Type.POISON, Type.NONE, talents, 46, 57, 40, 40, 40, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.COQUE_ARMURE);}};
        this.put("Moustillon", new Pokemon("Moustillon", 501, 541, Type.EAU, Type.NONE, talents, 55, 55, 45, 63, 45, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);this.add(Talent.TENSION);this.add(Talent.ESSAIM);}};
        this.put("Mygavolt", new Pokemon("Mygavolt", 596, 637, Type.INSECTE, Type.ELECTRIQUE, talents, 70, 77, 60, 97, 60, 108));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);this.add(Talent.PREDICTION);this.add(Talent.ATTENTION);}};
        this.put("Soporifik", new Pokemon("Soporifik", 96, 102, Type.PSY, Type.NONE, talents, 60, 48, 45, 43, 90, 42));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANNULE_GARDE);}};
        this.put("Dimocles", new Pokemon("Dimocles", 680, 726, Type.ACIER, Type.SPECTRE, talents, 59, 110, 150, 45, 49, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.IMPASSIBLE);this.add(Talent.FARCEUR);}};
        this.put("Riolu", new Pokemon("Riolu", 447, 478, Type.COMBAT, Type.NONE, talents, 40, 70, 40, 35, 40, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECRAN_POUDRE);this.add(Talent.FUITE);}};
        this.put("Aspicot", new Pokemon("Aspicot", 13, 17, Type.INSECTE, Type.POISON, talents, 40, 35, 30, 20, 20, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIDEAU_NEIGE);}};
        this.put("Marcacrin", new Pokemon("Marcacrin", 220, 235, Type.GLACE, Type.SOL, talents, 50, 50, 40, 30, 30, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYPER_CUTTER);this.add(Talent.INTIMIDATION);this.add(Talent.SANS_LIMITE);}};
        this.put("Mysdibule", new Pokemon("Mysdibule", 303, 322, Type.ACIER, Type.NONE, talents, 50, 85, 85, 55, 55, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECRAN_FUMEE);this.add(Talent.COQUE_ARMURE);}};
        this.put("Chartor", new Pokemon("Chartor", 324, 347, Type.FEU, Type.NONE, talents, 70, 85, 140, 85, 70, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.BAIGNE_SABLE);this.add(Talent.FORCE_SABLE);this.add(Talent.BRISE_MOULE);}};
        this.put("Minotaupe", new Pokemon("Minotaupe", 530, 570, Type.SOL, Type.ACIER, talents, 110, 135, 60, 50, 65, 88));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.TENSION);}};
        this.put("Maskadra", new Pokemon("Maskadra", 284, 303, Type.INSECTE, Type.VOL, talents, 70, 60, 62, 80, 82, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.TURBO);this.add(Talent.LENTITEINTEE);this.add(Talent.FOUILLE);}};
        this.put("Yanmega", new Pokemon("Yanmega", 469, 502, Type.INSECTE, Type.VOL, talents, 86, 76, 86, 116, 56, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.TECHNICIEN);}};
        this.put("Melokrik", new Pokemon("Melokrik", 402, 430, Type.INSECTE, Type.NONE, talents, 77, 85, 51, 55, 51, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.ESSAIM);this.add(Talent.TURBO);}};
        this.put("Scobolide", new Pokemon("Scobolide", 544, 584, Type.INSECTE, Type.POISON, talents, 40, 55, 99, 40, 79, 47));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.DELESTAGE);}};
        this.put("Massko", new Pokemon("Massko", 253, 270, Type.PLANTE, Type.NONE, talents, 50, 65, 45, 85, 65, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.TURBO);}};
        this.put("Brasegali", new Pokemon("Brasegali", 257, 274, Type.FEU, Type.COMBAT, talents, 80, 120, 70, 110, 70, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.VENTOUSE);this.add(Talent.CONTESTATION);}};
        this.put("Sepiatroce", new Pokemon("Sepiatroce", 687, 734, Type.TENEBRE, Type.PSY, talents, 86, 92, 88, 68, 73, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_DE_COQ);this.add(Talent.ENVELOCAPE);this.add(Talent.ARMUROUILLEE);}};
        this.put("Vostourno", new Pokemon("Vostourno", 629, 670, Type.TENEBRE, Type.VOL, talents, 70, 55, 75, 45, 65, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.PARATONNERRE);this.add(Talent.ARMURBASTON);}};
        this.put("Ossatueur", new Pokemon("Ossatueur", 105, 111, Type.SOL, Type.NONE, talents, 60, 80, 110, 50, 80, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.HERBIVORE);}};
        this.put("Cabriolaine", new Pokemon("Cabriolaine", 672, 718, Type.PLANTE, Type.NONE, talents, 66, 65, 48, 62, 57, 52));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.CUVETTE);}};
        this.put("Lombre", new Pokemon("Lombre", 271, 289, Type.EAU, Type.PLANTE, talents, 60, 50, 50, 60, 70, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHERCHE_MIEL);this.add(Talent.AGITATION);}};
        this.put("Apitrini", new Pokemon("Apitrini", 415, 445, Type.INSECTE, Type.VOL, talents, 30, 30, 42, 30, 42, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.QUERELLEUR);}};
        this.put("Nirondelle", new Pokemon("Nirondelle", 276, 294, Type.NORMAL, Type.VOL, talents, 40, 55, 30, 30, 30, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.TECHNICIEN);this.add(Talent.MULTI_COUPS);}};
        this.put("Chinchidou", new Pokemon("Chinchidou", 572, 613, Type.NORMAL, Type.NONE, talents, 55, 50, 40, 40, 40, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.MULTITYPE);}};
        this.put("Arceus", new Pokemon("Arceus", 493, 533, Type.NORMAL, Type.NONE, talents, 120, 120, 120, 120, 120, 120));

        talents = new ArrayList<Talent>(){{this.add(Talent.GRIFFE_DURE);}};
        this.put("Mega-Ptera", new Pokemon("Mega-Ptera", 142, 152, Type.ROCHE, Type.VOL, talents, 80, 135, 85, 70, 95, 150));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.ATTENTION);this.add(Talent.GARDE_MAGIK);}};
        this.put("Kadabra", new Pokemon("Kadabra", 64, 68, Type.PSY, Type.NONE, talents, 40, 35, 30, 120, 70, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.FERMETE);}};
        this.put("Regirock", new Pokemon("Regirock", 377, 402, Type.ROCHE, Type.NONE, talents, 80, 100, 200, 50, 100, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Deoxys (Forme Attaque)", new Pokemon("Deoxys (Forme Attaque)", 386, 412, Type.PSY, Type.NONE, talents, 50, 180, 20, 180, 20, 150));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.MOITEUR);this.add(Talent.CRACHIN);}};
        this.put("Tarpaud", new Pokemon("Tarpaud", 186, 199, Type.EAU, Type.NONE, talents, 90, 75, 75, 90, 100, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.BAJOUES);this.add(Talent.COLOFORCE);}};
        this.put("Sapereau", new Pokemon("Sapereau", 659, 705, Type.NORMAL, Type.NONE, talents, 38, 36, 38, 32, 36, 57));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);this.add(Talent.ABSORB_EAU);}};
        this.put("Cacturne", new Pokemon("Cacturne", 332, 355, Type.PLANTE, Type.TENEBRE, talents, 70, 115, 60, 115, 60, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);this.add(Talent.PARATONNERRE);}};
        this.put("Raichu", new Pokemon("Raichu", 26, 30, Type.ELECTRIQUE, Type.NONE, talents, 60, 90, 55, 90, 80, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.IGNIFU_VOILE);this.add(Talent.PARATONNERRE);}};
        this.put("Poissoroy", new Pokemon("Poissoroy", 119, 126, Type.EAU, Type.NONE, talents, 80, 92, 65, 65, 80, 68));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Vibraninf", new Pokemon("Vibraninf", 329, 352, Type.SOL, Type.DRAGON, talents, 50, 70, 50, 50, 50, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.VENTOUSE);this.add(Talent.LAVABO);}};
        this.put("Vacilys", new Pokemon("Vacilys", 346, 369, Type.ROCHE, Type.PLANTE, talents, 86, 81, 97, 81, 107, 43));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.HERBIVORE);this.add(Talent.SERENITE);}};
        this.put("Vivaldaim", new Pokemon("Vivaldaim", 585, 626, Type.NORMAL, Type.PLANTE, talents, 60, 60, 50, 40, 50, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.PUANTEUR);this.add(Talent.GLUE);this.add(Talent.TOXITOUCHE);}};
        this.put("Tadmorv", new Pokemon("Tadmorv", 88, 93, Type.POISON, Type.NONE, talents, 80, 80, 50, 40, 50, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Zarbi", new Pokemon("Zarbi", 201, 214, Type.PSY, Type.NONE, talents, 48, 72, 48, 72, 48, 48));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.TURBO);}};
        this.put("Galifeu", new Pokemon("Galifeu", 256, 273, Type.FEU, Type.COMBAT, talents, 60, 85, 60, 85, 60, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.SNIPER);}};
        this.put("Dardargnan", new Pokemon("Dardargnan", 15, 19, Type.INSECTE, Type.POISON, talents, 65, 80, 40, 45, 80, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIDEAU_NEIGE);this.add(Talent.PHOBIQUE);}};
        this.put("Polarhume", new Pokemon("Polarhume", 613, 654, Type.GLACE, Type.NONE, talents, 55, 70, 40, 60, 40, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.CIEL_GRIS);}};
        this.put("Tylton", new Pokemon("Tylton", 333, 356, Type.NORMAL, Type.VOL, talents, 45, 40, 60, 40, 75, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.TEMERAIRE);}};
        this.put("Roitiflam", new Pokemon("Roitiflam", 500, 540, Type.FEU, Type.COMBAT, talents, 110, 123, 65, 100, 65, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.CHLOROPHYLE);this.add(Talent.ENVELOCAPE);}};
        this.put("Manternel", new Pokemon("Manternel", 542, 582, Type.INSECTE, Type.PLANTE, talents, 75, 103, 80, 70, 70, 92));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);this.add(Talent.CHANCEUX);this.add(Talent.FARCEUR);}};
        this.put("Cornebre", new Pokemon("Cornebre", 198, 211, Type.TENEBRE, Type.VOL, talents, 60, 85, 42, 85, 42, 91));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.LIGHT_METAL);}};
        this.put("Terhal", new Pokemon("Terhal", 374, 399, Type.ACIER, Type.PSY, talents, 40, 55, 80, 35, 60, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGE_FORCE);this.add(Talent.ATTENTION);this.add(Talent.TEMERAIRE);}};
        this.put("Shaofouine", new Pokemon("Shaofouine", 620, 661, Type.COMBAT, Type.NONE, talents, 65, 125, 60, 95, 60, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.LENTITEINTEE);}};
        this.put("Papilord", new Pokemon("Papilord", 414, 444, Type.INSECTE, Type.VOL, talents, 70, 94, 50, 94, 50, 66));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Fantominus", new Pokemon("Fantominus", 92, 97, Type.SPECTRE, Type.POISON, talents, 30, 35, 30, 100, 35, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.COEUR_DE_COQ);this.add(Talent.HYDRATATION);}};
        this.put("Lakmecygne", new Pokemon("Lakmecygne", 581, 622, Type.EAU, Type.VOL, talents, 75, 87, 63, 87, 63, 98));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYPER_CUTTER);this.add(Talent.PIEGE);this.add(Talent.SANS_LIMITE);}};
        this.put("Kraknoix", new Pokemon("Kraknoix", 328, 351, Type.SOL, Type.NONE, talents, 45, 100, 45, 45, 45, 10));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.SERENITE);this.add(Talent.COEUR_SOIN);}};
        this.put("Leuphorie", new Pokemon("Leuphorie", 242, 258, Type.NORMAL, Type.NONE, talents, 255, 10, 10, 75, 135, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.COQUE_ARMURE);}};
        this.put("Boskara", new Pokemon("Boskara", 388, 416, Type.PLANTE, Type.NONE, talents, 75, 89, 85, 55, 65, 36));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRISE_MOULE);this.add(Talent.SANS_LIMITE);}};
        this.put("Charkos", new Pokemon("Charkos", 409, 437, Type.ROCHE, Type.NONE, talents, 97, 165, 60, 65, 50, 58));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.FORCE_SABLE);}};
        this.put("Gigalithe", new Pokemon("Gigalithe", 526, 566, Type.ROCHE, Type.NONE, talents, 85, 135, 130, 60, 70, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.PIED_CONFUS);this.add(Talent.COEUR_DE_COQ);}};
        this.put("Roucoups", new Pokemon("Roucoups", 17, 21, Type.NORMAL, Type.VOL, talents, 63, 60, 55, 50, 50, 71));

        talents = new ArrayList<Talent>(){{this.add(Talent.LAVABO);this.add(Talent.GLISSADE);this.add(Talent.IGNIFU_VOILE);}};
        this.put("Ecayon", new Pokemon("Ecayon", 456, 488, Type.EAU, Type.NONE, talents, 49, 49, 56, 49, 61, 66));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);this.add(Talent.TENSION);this.add(Talent.ESSAIM);}};
        this.put("Statitik", new Pokemon("Statitik", 595, 636, Type.INSECTE, Type.ELECTRIQUE, talents, 50, 47, 50, 57, 50, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Teraclope", new Pokemon("Teraclope", 356, 380, Type.SPECTRE, Type.NONE, talents, 40, 70, 130, 60, 130, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.HYDRATATION);}};
        this.put("Aquali", new Pokemon("Aquali", 134, 143, Type.EAU, Type.NONE, talents, 130, 65, 60, 110, 95, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.FORCE_SABLE);}};
        this.put("Geolithe", new Pokemon("Geolithe", 525, 565, Type.ROCHE, Type.NONE, talents, 70, 105, 105, 50, 40, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);this.add(Talent.ECAILLE_SPECIALE);}};
        this.put("Draco", new Pokemon("Draco", 148, 158, Type.DRAGON, Type.NONE, talents, 61, 84, 65, 70, 70, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.MAGNEPIEGE);this.add(Talent.ANALYSTE);}};
        this.put("Magnezone", new Pokemon("Magnezone", 462, 495, Type.ELECTRIQUE, Type.ACIER, talents, 70, 70, 115, 130, 90, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.POINT_POISON);this.add(Talent.FEUIL_GARDE);}};
        this.put("Roselia", new Pokemon("Roselia", 315, 338, Type.PLANTE, Type.POISON, talents, 50, 60, 45, 100, 80, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSENTEISME);}};
        this.put("Monaflemit", new Pokemon("Monaflemit", 289, 308, Type.NORMAL, Type.NONE, talents, 150, 160, 100, 95, 65, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.TEMPO_PERSO);this.add(Talent.PIED_CONFUS);this.add(Talent.CONTESTATION);}};
        this.put("Spinda", new Pokemon("Spinda", 327, 350, Type.NORMAL, Type.NONE, talents, 60, 60, 60, 60, 60, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.MOITEUR);this.add(Talent.GLISSADE);}};
        this.put("Tartard", new Pokemon("Tartard", 62, 66, Type.EAU, Type.COMBAT, talents, 90, 85, 95, 70, 90, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.TELEPATHE);}};
        this.put("Palkia", new Pokemon("Palkia", 484, 522, Type.EAU, Type.DRAGON, talents, 90, 120, 100, 150, 120, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.AGITATION);this.add(Talent.ATTENTION);}};
        this.put("Darumarond", new Pokemon("Darumarond", 554, 594, Type.FEU, Type.NONE, talents, 70, 90, 45, 15, 45, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.PREDICTION);this.add(Talent.SYNCHRO);this.add(Talent.TELEPATHE);}};
        this.put("Munna", new Pokemon("Munna", 517, 557, Type.PSY, Type.NONE, talents, 76, 25, 45, 67, 55, 24));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.COLERIQUE);this.add(Talent.SANS_LIMITE);}};
        this.put("Tauros", new Pokemon("Tauros", 128, 136, Type.NORMAL, Type.NONE, talents, 75, 100, 95, 40, 70, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.TEMERAIRE);}};
        this.put("Etouraptor", new Pokemon("Etouraptor", 398, 426, Type.NORMAL, Type.VOL, talents, 85, 120, 70, 50, 50, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.TEMERAIRE);this.add(Talent.HERBIVORE);this.add(Talent.ANTI_BRUIT);}};
        this.put("Frison", new Pokemon("Frison", 626, 667, Type.NORMAL, Type.NONE, talents, 95, 110, 95, 40, 95, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.ABSORB_VOLT);}};
        this.put("Raikou", new Pokemon("Raikou", 243, 259, Type.ELECTRIQUE, Type.NONE, talents, 90, 85, 75, 115, 100, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.ACHARNE);}};
        this.put("Pingoleon", new Pokemon("Pingoleon", 395, 423, Type.EAU, Type.ACIER, talents, 84, 86, 88, 111, 101, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.TORCHE);}};
        this.put("Hericendre", new Pokemon("Hericendre", 155, 167, Type.FEU, Type.NONE, talents, 39, 52, 43, 60, 50, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.MUE);this.add(Talent.TENSION);}};
        this.put("Arbok", new Pokemon("Arbok", 24, 28, Type.POISON, Type.NONE, talents, 60, 85, 69, 65, 79, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.FOUILLE);this.add(Talent.BATTANT);this.add(Talent.MARQUE_OMBRE);}};
        this.put("Mesmerella", new Pokemon("Mesmerella", 575, 616, Type.PSY, Type.NONE, talents, 60, 45, 70, 75, 85, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.POING_DE_FER);}};
        this.put("Chimpenfeu", new Pokemon("Chimpenfeu", 391, 419, Type.FEU, Type.COMBAT, talents, 64, 78, 52, 78, 52, 81));

        talents = new ArrayList<Talent>(){{this.add(Talent.MOITEUR);this.add(Talent.CIEL_GRIS);this.add(Talent.GLISSADE);}};
        this.put("Psykokwak", new Pokemon("Psykokwak", 54, 58, Type.EAU, Type.NONE, talents, 50, 52, 48, 65, 50, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.GLOUTONNERIE);}};
        this.put("Boustiflor", new Pokemon("Boustiflor", 70, 75, Type.PLANTE, Type.POISON, talents, 65, 90, 50, 85, 45, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.CALQUE);this.add(Talent.TELECHARGE);this.add(Talent.ANALYSTE);}};
        this.put("Porygon2", new Pokemon("Porygon2", 233, 249, Type.NORMAL, Type.NONE, talents, 85, 80, 90, 105, 95, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.CORPS_GEL);this.add(Talent.BENET);}};
        this.put("Kaimorse", new Pokemon("Kaimorse", 365, 390, Type.GLACE, Type.EAU, talents, 110, 80, 90, 95, 90, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.MOITEUR);this.add(Talent.CIEL_GRIS);this.add(Talent.GLISSADE);}};
        this.put("Akwakwak", new Pokemon("Akwakwak", 55, 59, Type.EAU, Type.NONE, talents, 80, 82, 78, 95, 80, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.POING_DE_FER);this.add(Talent.ATTENTION);}};
        this.put("Tygnon", new Pokemon("Tygnon", 107, 113, Type.COMBAT, Type.NONE, talents, 50, 105, 79, 35, 110, 76));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.ISOGRAISSE);this.add(Talent.GLOUTONNERIE);}};
        this.put("Goinfrex", new Pokemon("Goinfrex", 446, 477, Type.NORMAL, Type.NONE, talents, 135, 85, 40, 40, 85, 5));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);}};
        this.put("Griknot", new Pokemon("Griknot", 443, 473, Type.DRAGON, Type.SOL, talents, 58, 70, 45, 40, 45, 42));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLUCO_VOILE);this.add(Talent.DELESTAGE);}};
        this.put("Sucroquin", new Pokemon("Sucroquin", 684, 731, Type.FEE, Type.NONE, talents, 62, 48, 66, 59, 57, 49));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYDRATATION);this.add(Talent.COQUE_ARMURE);this.add(Talent.ENVELOCAPE);}};
        this.put("Escargaume", new Pokemon("Escargaume", 616, 657, Type.INSECTE, Type.NONE, talents, 50, 40, 85, 40, 65, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANNULE_GARDE);}};
        this.put("Monorpale", new Pokemon("Monorpale", 679, 725, Type.ACIER, Type.SPECTRE, talents, 40, 90, 130, 35, 30, 10));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.MAGICIEN);}};
        this.put("Goupelin", new Pokemon("Goupelin", 655, 701, Type.FEU, Type.PSY, talents, 75, 69, 72, 114, 100, 104));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.FREIN);this.add(Talent.FARCEUR);}};
        this.put("Tenefix", new Pokemon("Tenefix", 302, 321, Type.TENEBRE, Type.SPECTRE, talents, 50, 75, 75, 65, 65, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);}};
        this.put("Mustebouee", new Pokemon("Mustebouee", 418, 448, Type.EAU, Type.NONE, talents, 55, 65, 35, 60, 30, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.INFILTRATION);}};
        this.put("Nosferalto", new Pokemon("Nosferalto", 42, 46, Type.POISON, Type.VOL, talents, 75, 80, 70, 65, 75, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.ATTENTION);this.add(Talent.BRISE_MOULE);}};
        this.put("Judokrak", new Pokemon("Judokrak", 538, 578, Type.COMBAT, Type.NONE, talents, 120, 100, 85, 30, 85, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.TETE_DE_ROC);this.add(Talent.FERMETE);}};
        this.put("Relicanth", new Pokemon("Relicanth", 369, 394, Type.EAU, Type.ROCHE, talents, 100, 90, 130, 45, 65, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.PREDICTION);this.add(Talent.SYNCHRO);this.add(Talent.TELEPATHE);}};
        this.put("Mushana", new Pokemon("Mushana", 518, 558, Type.PSY, Type.NONE, talents, 116, 55, 85, 107, 95, 29));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.SERENITE);this.add(Talent.GARDE_AMIE);}};
        this.put("Ptiravi", new Pokemon("Ptiravi", 440, 470, Type.NORMAL, Type.NONE, talents, 100, 5, 5, 15, 65, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.COQUE_ARMURE);this.add(Talent.PHOBIQUE);}};
        this.put("Coquiperl", new Pokemon("Coquiperl", 366, 391, Type.EAU, Type.NONE, talents, 35, 64, 85, 74, 55, 32));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Ohmassacre", new Pokemon("Ohmassacre", 604, 645, Type.ELECTRIQUE, Type.NONE, talents, 85, 115, 80, 105, 80, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.FOUILLE);this.add(Talent.RECOLTE);}};
        this.put("Brocelome", new Pokemon("Brocelome", 708, 755, Type.SPECTRE, Type.PLANTE, talents, 43, 70, 48, 50, 60, 38));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.POINT_POISON);this.add(Talent.FEUIL_GARDE);}};
        this.put("Rozbouton", new Pokemon("Rozbouton", 406, 434, Type.PLANTE, Type.NONE, talents, 40, 30, 35, 50, 70, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.ACHARNE);this.add(Talent.PRESSION);}};
        this.put("Scalproie", new Pokemon("Scalproie", 625, 666, Type.ACIER, Type.TENEBRE, talents, 65, 125, 100, 60, 70, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.CORPS_GEL);this.add(Talent.BENET);}};
        this.put("Phogleur", new Pokemon("Phogleur", 364, 389, Type.GLACE, Type.EAU, talents, 90, 60, 70, 75, 70, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.TELEPATHE);this.add(Talent.SYNCHRO);this.add(Talent.ANALYSTE);}};
        this.put("Neitram", new Pokemon("Neitram", 606, 647, Type.PSY, Type.NONE, talents, 75, 75, 75, 125, 95, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.INCONSCIENT);this.add(Talent.MALADRESSE);this.add(Talent.SIMPLE);}};
        this.put("Chovsourir", new Pokemon("Chovsourir", 527, 567, Type.PSY, Type.VOL, talents, 55, 45, 43, 55, 43, 72));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);}};
        this.put("Musteflott", new Pokemon("Musteflott", 419, 449, Type.EAU, Type.NONE, talents, 85, 105, 55, 85, 50, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.SERENITE);this.add(Talent.FUITE);this.add(Talent.PHOBIQUE);}};
        this.put("Insolourdo", new Pokemon("Insolourdo", 206, 219, Type.NORMAL, Type.NONE, talents, 100, 70, 70, 65, 65, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.SABLE_VOLANT);}};
        this.put("Mega-Tyranocif", new Pokemon("Mega-Tyranocif", 248, 265, Type.ROCHE, Type.TENEBRE, talents, 100, 164, 150, 95, 120, 71));

        talents = new ArrayList<Talent>(){{this.add(Talent.GARDE_MYSTIK);}};
        this.put("Munja", new Pokemon("Munja", 292, 311, Type.INSECTE, Type.SPECTRE, talents, 1, 90, 45, 30, 30, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_DURE);this.add(Talent.SANS_LIMITE);this.add(Talent.BRISE_MOULE);}};
        this.put("Drakkarmin", new Pokemon("Drakkarmin", 621, 662, Type.DRAGON, Type.NONE, talents, 77, 120, 90, 60, 90, 48));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_GEL);this.add(Talent.ARMUROUILLEE);}};
        this.put("Sorbouboul", new Pokemon("Sorbouboul", 584, 625, Type.GLACE, Type.NONE, talents, 71, 95, 85, 110, 95, 79));

        talents = new ArrayList<Talent>(){{this.add(Talent.ALERTE_NEIGE);}};
        this.put("Mega-Blizzaroi", new Pokemon("Mega-Blizzaroi", 460, 493, Type.GLACE, Type.PLANTE, talents, 90, 132, 105, 132, 105, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.TERA_VOLTAGE);}};
        this.put("Zekrom", new Pokemon("Zekrom", 644, 687, Type.DRAGON, Type.ELECTRIQUE, talents, 100, 150, 120, 120, 100, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.AGITATION);this.add(Talent.SNIPER);this.add(Talent.LUNATIQUE);}};
        this.put("Remoraid", new Pokemon("Remoraid", 223, 238, Type.EAU, Type.NONE, talents, 35, 65, 35, 65, 35, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYDRATATION);this.add(Talent.COEUR_SOIN);this.add(Talent.REGE_FORCE);}};
        this.put("Mamanbo", new Pokemon("Mamanbo", 594, 635, Type.EAU, Type.NONE, talents, 165, 75, 80, 40, 45, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENVELOCAPE);this.add(Talent.GARDE_MAGIK);this.add(Talent.REGE_FORCE);}};
        this.put("Meios", new Pokemon("Meios", 578, 619, Type.PSY, Type.NONE, talents, 65, 40, 50, 125, 60, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.ATTENTION);}};
        this.put("Noctali", new Pokemon("Noctali", 197, 210, Type.TENEBRE, Type.NONE, talents, 95, 65, 110, 60, 130, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRISE_MOULE);}};
        this.put("Mega-Pharamp", new Pokemon("Mega-Pharamp", 181, 194, Type.ELECTRIQUE, Type.DRAGON, talents, 90, 95, 105, 165, 110, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.TEMPO_PERSO);this.add(Talent.REGE_FORCE);}};
        this.put("Ramoloss", new Pokemon("Ramoloss", 79, 84, Type.EAU, Type.PSY, talents, 90, 65, 65, 40, 40, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLUCO_VOILE);this.add(Talent.DELESTAGE);}};
        this.put("Cupcanaille", new Pokemon("Cupcanaille", 685, 732, Type.FEE, Type.NONE, talents, 82, 80, 86, 85, 75, 72));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.CUVETTE);}};
        this.put("Carabaffe", new Pokemon("Carabaffe", 8, 11, Type.EAU, Type.NONE, talents, 59, 63, 80, 65, 80, 58));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.ANTICIPATION);this.add(Talent.HYDRATATION);}};
        this.put("Barbicha", new Pokemon("Barbicha", 340, 363, Type.EAU, Type.SOL, talents, 110, 78, 73, 76, 71, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_DE_COQ);this.add(Talent.CHANCEUX);this.add(Talent.RIVALITE);}};
        this.put("Colombeau", new Pokemon("Colombeau", 520, 560, Type.NORMAL, Type.VOL, talents, 62, 77, 62, 50, 42, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);this.add(Talent.IMPUDENCE);this.add(Talent.INTIMIDATION);}};
        this.put("Baggaid", new Pokemon("Baggaid", 560, 601, Type.TENEBRE, Type.COMBAT, talents, 65, 90, 115, 45, 115, 58));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTI_BRUIT);this.add(Talent.QUERELLEUR);}};
        this.put("Ramboum", new Pokemon("Ramboum", 294, 313, Type.NORMAL, Type.NONE, talents, 84, 71, 43, 71, 43, 48));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECHAUFFEMENT);this.add(Talent.TEMERAIRE);this.add(Talent.DELESTAGE);}};
        this.put("Kicklee", new Pokemon("Kicklee", 106, 112, Type.COMBAT, Type.NONE, talents, 50, 120, 53, 35, 110, 87));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.PIED_VELOCE);this.add(Talent.CHERCHE_MIEL);}};
        this.put("Teddiursa", new Pokemon("Teddiursa", 216, 231, Type.NORMAL, Type.NONE, talents, 60, 80, 50, 50, 50, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.ATTENTION);this.add(Talent.BRISE_MOULE);}};
        this.put("Karaclee", new Pokemon("Karaclee", 539, 579, Type.COMBAT, Type.NONE, talents, 75, 125, 75, 30, 75, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.IGNIFU_VOILE);}};
        this.put("Serpang", new Pokemon("Serpang", 367, 392, Type.EAU, Type.NONE, talents, 55, 104, 105, 94, 75, 52));

        talents = new ArrayList<Talent>(){{this.add(Talent.CALQUE);this.add(Talent.TELECHARGE);this.add(Talent.ANALYSTE);}};
        this.put("Porygon", new Pokemon("Porygon", 137, 146, Type.NORMAL, Type.NONE, talents, 65, 60, 70, 85, 75, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.BAIGNE_SABLE);this.add(Talent.QUERELLEUR);}};
        this.put("Mastouffe", new Pokemon("Mastouffe", 508, 548, Type.NORMAL, Type.NONE, talents, 85, 100, 90, 45, 90, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_ARDENT);this.add(Talent.ESSAIM);}};
        this.put("Pyrax", new Pokemon("Pyrax", 637, 678, Type.INSECTE, Type.FEU, talents, 85, 60, 65, 135, 105, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.CONTESTATION);}};
        this.put("Majaspic", new Pokemon("Majaspic", 497, 537, Type.PLANTE, Type.NONE, talents, 75, 75, 95, 75, 95, 113));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);}};
        this.put("Blindalys", new Pokemon("Blindalys", 268, 286, Type.INSECTE, Type.NONE, talents, 50, 35, 55, 25, 25, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.CUVETTE);}};
        this.put("Nenupiot", new Pokemon("Nenupiot", 270, 288, Type.EAU, Type.PLANTE, talents, 40, 30, 30, 40, 50, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.ENVELOCAPE);}};
        this.put("Foretress", new Pokemon("Foretress", 205, 218, Type.INSECTE, Type.ACIER, talents, 75, 90, 140, 60, 60, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);this.add(Talent.LENTITEINTEE);this.add(Talent.FUITE);}};
        this.put("Mimitoss", new Pokemon("Mimitoss", 48, 52, Type.INSECTE, Type.POISON, talents, 60, 55, 50, 40, 55, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.PREDICTION);this.add(Talent.PEAU_SECHE);}};
        this.put("Lippoutou", new Pokemon("Lippoutou", 124, 131, Type.GLACE, Type.PSY, talents, 65, 50, 35, 115, 95, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.MINUS);}};
        this.put("Negapi", new Pokemon("Negapi", 312, 335, Type.ELECTRIQUE, Type.NONE, talents, 60, 40, 50, 75, 85, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRISE_MOULE);}};
        this.put("Mega-Leviator", new Pokemon("Mega-Leviator", 130, 139, Type.EAU, Type.TENEBRE, talents, 95, 155, 109, 70, 130, 81));

        talents = new ArrayList<Talent>(){{this.add(Talent.SECHERESSE);}};
        this.put("Mega-Dracaufeu Y", new Pokemon("Mega-Dracaufeu Y", 6, 9, Type.FEU, Type.VOL, talents, 78, 104, 78, 159, 115, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYDRATATION);this.add(Talent.HERBIVORE);this.add(Talent.POISSEUX);}};
        this.put("Colimucus", new Pokemon("Colimucus", 705, 752, Type.DRAGON, Type.NONE, talents, 50, 70, 50, 90, 120, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.POING_DE_FER);}};
        this.put("Ouisticram", new Pokemon("Ouisticram", 390, 418, Type.FEU, Type.NONE, talents, 44, 58, 44, 58, 44, 61));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.ISOGRAISSE);}};
        this.put("Gruikui", new Pokemon("Gruikui", 498, 538, Type.FEU, Type.NONE, talents, 65, 63, 45, 45, 45, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.IMPASSIBLE);}};
        this.put("Gallame", new Pokemon("Gallame", 475, 508, Type.PSY, Type.COMBAT, talents, 68, 125, 65, 65, 115, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLOUTONNERIE);this.add(Talent.TORRENT);}};
        this.put("Flotajou", new Pokemon("Flotajou", 515, 555, Type.EAU, Type.NONE, talents, 50, 53, 48, 53, 48, 64));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRISE_MOULE);this.add(Talent.POING_DE_FER);this.add(Talent.QUERELLEUR);}};
        this.put("Pandespiegle", new Pokemon("Pandespiegle", 674, 720, Type.COMBAT, Type.NONE, talents, 67, 82, 62, 46, 48, 43));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYDRATATION);this.add(Talent.HERBIVORE);this.add(Talent.POISSEUX);}};
        this.put("Muplodocus", new Pokemon("Muplodocus", 706, 753, Type.DRAGON, Type.NONE, talents, 90, 100, 70, 110, 150, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.PARE_BALLES);}};
        this.put("Blindepique", new Pokemon("Blindepique", 652, 698, Type.PLANTE, Type.COMBAT, talents, 88, 107, 122, 74, 75, 64));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.CORPS_ARDENT);this.add(Talent.INFILTRATION);}};
        this.put("Melancolux", new Pokemon("Melancolux", 608, 649, Type.SPECTRE, Type.FEU, talents, 60, 40, 60, 95, 60, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_NOBLE);}};
        this.put("Viridium", new Pokemon("Viridium", 640, 681, Type.PLANTE, Type.COMBAT, talents, 91, 90, 72, 90, 129, 108));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.REGARD_VIF);this.add(Talent.FOUILLE);}};
        this.put("Fouinette", new Pokemon("Fouinette", 161, 173, Type.NORMAL, Type.NONE, talents, 35, 46, 34, 35, 45, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.FOUILLE);this.add(Talent.RECOLTE);}};
        this.put("Desseliande", new Pokemon("Desseliande", 709, 756, Type.SPECTRE, Type.PLANTE, talents, 85, 110, 76, 65, 82, 56));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);this.add(Talent.INFILTRATION);}};
        this.put("Seviper", new Pokemon("Seviper", 336, 359, Type.POISON, Type.NONE, talents, 73, 100, 60, 100, 60, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.FEUIL_GARDE);}};
        this.put("Germignon", new Pokemon("Germignon", 152, 164, Type.PLANTE, Type.NONE, talents, 45, 49, 65, 49, 65, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESPRIT_VITAL);this.add(Talent.RAMASSAGE);this.add(Talent.FUITE);}};
        this.put("Ponchiot", new Pokemon("Ponchiot", 506, 546, Type.NORMAL, Type.NONE, talents, 45, 60, 45, 25, 45, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.TORCHE);}};
        this.put("Typhlosion", new Pokemon("Typhlosion", 157, 169, Type.FEU, Type.NONE, talents, 78, 84, 78, 109, 85, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.FORCE_SABLE);this.add(Talent.SANS_LIMITE);}};
        this.put("Demeteros (Forme Avatar)", new Pokemon("Demeteros (Forme Avatar)", 645, 688, Type.SOL, Type.VOL, talents, 89, 125, 90, 115, 80, 101));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.SECHERESSE);}};
        this.put("Feunard", new Pokemon("Feunard", 38, 42, Type.FEU, Type.NONE, talents, 73, 76, 75, 81, 100, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.MAGNEPIEGE);this.add(Talent.FERMETE);this.add(Talent.ANALYSTE);}};
        this.put("Magneti", new Pokemon("Magneti", 81, 86, Type.ELECTRIQUE, Type.ACIER, talents, 25, 35, 70, 95, 55, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_NOBLE);}};
        this.put("Cobaltium", new Pokemon("Cobaltium", 638, 679, Type.ACIER, Type.COMBAT, talents, 91, 90, 129, 90, 72, 108));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECHAUFFEMENT);this.add(Talent.TECHNICIEN);this.add(Talent.TENSION);}};
        this.put("Persian", new Pokemon("Persian", 53, 57, Type.NORMAL, Type.NONE, talents, 65, 70, 60, 65, 65, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.RIVALITE);this.add(Talent.SANS_LIMITE);}};
        this.put("Nidoking", new Pokemon("Nidoking", 34, 38, Type.POISON, Type.SOL, talents, 81, 92, 77, 85, 75, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.TURBO);this.add(Talent.INFILTRATION);}};
        this.put("Ninjask", new Pokemon("Ninjask", 291, 310, Type.INSECTE, Type.VOL, talents, 61, 90, 45, 50, 50, 160));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.PROTEEN);}};
        this.put("Amphinobi", new Pokemon("Amphinobi", 658, 704, Type.EAU, Type.TENEBRE, talents, 72, 95, 67, 103, 71, 122));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIVALITE);this.add(Talent.TENSION);this.add(Talent.IMPUDENCE);}};
        this.put("Nemelios", new Pokemon("Nemelios", 668, 714, Type.FEU, Type.NORMAL, talents, 86, 68, 72, 109, 66, 106));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.PIED_VELOCE);this.add(Talent.PHOBIQUE);}};
        this.put("Medhyena", new Pokemon("Medhyena", 261, 279, Type.TENEBRE, Type.NONE, talents, 35, 55, 35, 30, 30, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.ADAPTABILITE);this.add(Talent.ANTICIPATION);}};
        this.put("Evoli", new Pokemon("Evoli", 133, 142, Type.NORMAL, Type.NONE, talents, 55, 55, 50, 45, 65, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.ANTICIPATION);this.add(Talent.HYDRATATION);}};
        this.put("Barloche", new Pokemon("Barloche", 339, 362, Type.EAU, Type.SOL, talents, 50, 48, 43, 46, 41, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.ARMURBASTON);this.add(Talent.ARMUROUILLEE);}};
        this.put("Kabuto", new Pokemon("Kabuto", 140, 149, Type.ROCHE, Type.EAU, talents, 30, 80, 90, 55, 45, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.PROTEEN);}};
        this.put("Grenousse", new Pokemon("Grenousse", 656, 702, Type.EAU, Type.NONE, talents, 37, 53, 49, 66, 50, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Kaorine", new Pokemon("Kaorine", 344, 367, Type.SOL, Type.PSY, talents, 60, 70, 105, 70, 120, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.IMPASSIBLE);this.add(Talent.ESPRIT_VITAL);}};
        this.put("Debugant", new Pokemon("Debugant", 236, 252, Type.COMBAT, Type.NONE, talents, 35, 35, 35, 35, 35, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);}};
        this.put("Ningale", new Pokemon("Ningale", 290, 309, Type.INSECTE, Type.SOL, talents, 31, 45, 90, 30, 30, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.TECHNICIEN);this.add(Talent.MULTI_COUPS);}};
        this.put("Capidextre", new Pokemon("Capidextre", 424, 454, Type.NORMAL, Type.NONE, talents, 75, 100, 66, 60, 66, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.PLUS);this.add(Talent.MINUS);this.add(Talent.CORPS_SAIN);}};
        this.put("Tic", new Pokemon("Tic", 599, 640, Type.ACIER, Type.NONE, talents, 40, 55, 70, 45, 60, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.SNIPER);}};
        this.put("Piafabec", new Pokemon("Piafabec", 21, 25, Type.NORMAL, Type.VOL, talents, 40, 60, 30, 31, 31, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.ARMUMAGMA);this.add(Talent.SOLIDE_ROC);this.add(Talent.COLERIQUE);}};
        this.put("Camerupt", new Pokemon("Camerupt", 323, 346, Type.FEU, Type.SOL, talents, 70, 100, 70, 105, 75, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.CUVETTE);}};
        this.put("Goelise", new Pokemon("Goelise", 278, 296, Type.EAU, Type.VOL, talents, 40, 30, 30, 55, 30, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.CORPS_ARDENT);this.add(Talent.MARQUE_OMBRE);}};
        this.put("Funecire", new Pokemon("Funecire", 607, 648, Type.SPECTRE, Type.FEU, talents, 50, 30, 55, 65, 55, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.SNIPER);this.add(Talent.GRIFFE_DURE);this.add(Talent.PICKPOCKET);}};
        this.put("Golgopathe", new Pokemon("Golgopathe", 689, 736, Type.ROCHE, Type.EAU, talents, 70, 115, 115, 50, 100, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.TURBOBRASIER);}};
        this.put("Reshiram", new Pokemon("Reshiram", 643, 686, Type.DRAGON, Type.FEU, talents, 100, 120, 100, 150, 120, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.TEMPO_PERSO);this.add(Talent.CIEL_GRIS);}};
        this.put("Excelangue", new Pokemon("Excelangue", 108, 114, Type.NORMAL, Type.NONE, talents, 90, 55, 75, 60, 75, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.MOITEUR);this.add(Talent.GLISSADE);}};
        this.put("Tetarte", new Pokemon("Tetarte", 61, 65, Type.EAU, Type.NONE, talents, 65, 65, 65, 50, 50, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.MARQUE_OMBRE);}};
        this.put("Mega-Ectoplasma", new Pokemon("Mega-Ectoplasma", 94, 100, Type.SPECTRE, Type.POISON, talents, 60, 65, 80, 170, 95, 130));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEGA_BLASTER);}};
        this.put("Flingouste", new Pokemon("Flingouste", 692, 739, Type.EAU, Type.NONE, talents, 50, 53, 62, 58, 63, 44));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.SANS_LIMITE);}};
        this.put("Aligatueur", new Pokemon("Aligatueur", 160, 172, Type.EAU, Type.NONE, talents, 85, 105, 100, 79, 83, 78));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Magireve", new Pokemon("Magireve", 429, 459, Type.SPECTRE, Type.NONE, talents, 60, 60, 60, 105, 105, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIVALITE);this.add(Talent.INTIMIDATION);this.add(Talent.CRAN);}};
        this.put("Luxray", new Pokemon("Luxray", 405, 433, Type.ELECTRIQUE, Type.NONE, talents, 80, 120, 79, 95, 79, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.HYDRATATION);}};
        this.put("Rosabyss", new Pokemon("Rosabyss", 368, 393, Type.EAU, Type.NONE, talents, 55, 84, 105, 114, 75, 52));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.TETE_DE_ROC);this.add(Talent.HEAVY_METAL);}};
        this.put("Galekid", new Pokemon("Galekid", 304, 324, Type.ACIER, Type.ROCHE, talents, 50, 70, 100, 40, 40, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.PRESSION);this.add(Talent.TENSION);}};
        this.put("Ptera", new Pokemon("Ptera", 142, 151, Type.ROCHE, Type.VOL, talents, 80, 105, 65, 60, 75, 130));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.TORCHE);this.add(Talent.CORPS_ARDENT);}};
        this.put("Galopa", new Pokemon("Galopa", 78, 83, Type.FEU, Type.NONE, talents, 65, 100, 70, 80, 80, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.TEMPO_PERSO);this.add(Talent.REGE_FORCE);}};
        this.put("Roigada", new Pokemon("Roigada", 199, 212, Type.EAU, Type.PSY, talents, 95, 75, 80, 100, 110, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.SERENITE);}};
        this.put("Jirachi", new Pokemon("Jirachi", 385, 410, Type.ACIER, Type.PSY, talents, 100, 100, 100, 100, 100, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.FOUILLE);this.add(Talent.INSOMNIA);}};
        this.put("Pitrouille (Taille Mini)", new Pokemon("Pitrouille (Taille Mini)", 710, 757, Type.SPECTRE, Type.PLANTE, talents, 44, 66, 70, 44, 55, 56));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.PARE_BALLES);}};
        this.put("Marisson", new Pokemon("Marisson", 650, 696, Type.PLANTE, Type.NONE, talents, 56, 64, 66, 50, 45, 38));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.IMPUDENCE);this.add(Talent.COLERIQUE);}};
        this.put("Mascaiman", new Pokemon("Mascaiman", 551, 591, Type.SOL, Type.TENEBRE, talents, 50, 72, 35, 35, 35, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.CUVETTE);}};
        this.put("Carapuce", new Pokemon("Carapuce", 7, 10, Type.EAU, Type.NONE, talents, 44, 48, 65, 50, 64, 43));

        talents = new ArrayList<Talent>(){{this.add(Talent.VACCIN);this.add(Talent.RAGE_POISON);}};
        this.put("Mangriff", new Pokemon("Mangriff", 335, 358, Type.NORMAL, Type.NONE, talents, 73, 115, 60, 60, 60, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Latias", new Pokemon("Latias", 380, 405, Type.DRAGON, Type.PSY, talents, 80, 80, 90, 110, 130, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.PIED_VELOCE);this.add(Talent.IMPUDENCE);}};
        this.put("Grahyena", new Pokemon("Grahyena", 262, 280, Type.TENEBRE, Type.NONE, talents, 70, 90, 70, 60, 60, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.MULTIECAILLE);}};
        this.put("Lugia", new Pokemon("Lugia", 249, 266, Type.PSY, Type.VOL, talents, 106, 90, 130, 90, 154, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.FERMETE);this.add(Talent.ARMUROUILLEE);}};
        this.put("Onix", new Pokemon("Onix", 95, 101, Type.ROCHE, Type.SOL, talents, 35, 45, 160, 30, 45, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.CRAN);}};
        this.put("Pyroli", new Pokemon("Pyroli", 136, 145, Type.FEU, Type.NONE, talents, 65, 130, 60, 95, 110, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.MAGNEPIEGE);this.add(Talent.FERMETE);this.add(Talent.ANALYSTE);}};
        this.put("Magneton", new Pokemon("Magneton", 82, 87, Type.ELECTRIQUE, Type.ACIER, talents, 50, 60, 95, 120, 70, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIVALITE);this.add(Talent.BRISE_MOULE);this.add(Talent.TENSION);}};
        this.put("Incisache", new Pokemon("Incisache", 611, 652, Type.DRAGON, Type.DRAGON, talents, 66, 117, 70, 40, 50, 67));

        talents = new ArrayList<Talent>(){{this.add(Talent.COQUE_ARMURE);this.add(Talent.MULTI_COUPS);this.add(Talent.ENVELOCAPE);}};
        this.put("Kokiyas", new Pokemon("Kokiyas", 90, 95, Type.EAU, Type.NONE, talents, 30, 65, 100, 45, 25, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.FERMETE);this.add(Talent.VOILE_SABLE);}};
        this.put("Racaillou", new Pokemon("Racaillou", 74, 79, Type.ROCHE, Type.SOL, talents, 40, 80, 100, 30, 30, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYPER_CUTTER);this.add(Talent.COQUE_ARMURE);this.add(Talent.ADAPTABILITE);}};
        this.put("Colhomard", new Pokemon("Colhomard", 342, 365, Type.EAU, Type.TENEBRE, talents, 63, 120, 85, 90, 55, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECRAN_POUDRE);}};
        this.put("Papinox", new Pokemon("Papinox", 269, 287, Type.INSECTE, Type.POISON, talents, 60, 50, 70, 50, 90, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYDRATATION);}};
        this.put("Manaphy", new Pokemon("Manaphy", 490, 529, Type.EAU, Type.NONE, talents, 100, 100, 100, 100, 100, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.SANS_LIMITE);}};
        this.put("Crocrodil", new Pokemon("Crocrodil", 159, 171, Type.EAU, Type.NONE, talents, 65, 80, 80, 59, 63, 58));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Ectoplasma", new Pokemon("Ectoplasma", 94, 99, Type.SPECTRE, Type.POISON, talents, 60, 65, 60, 130, 75, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENVELOCAPE);this.add(Talent.GARDE_MAGIK);this.add(Talent.REGE_FORCE);}};
        this.put("Nucleos", new Pokemon("Nucleos", 577, 618, Type.PSY, Type.NONE, talents, 45, 30, 40, 105, 50, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Vortente", new Pokemon("Vortente", 455, 487, Type.PLANTE, Type.NONE, talents, 74, 100, 72, 90, 72, 46));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYPER_CUTTER);this.add(Talent.COQUE_ARMURE);this.add(Talent.ADAPTABILITE);}};
        this.put("Ecrapince", new Pokemon("Ecrapince", 341, 364, Type.EAU, Type.NONE, talents, 43, 80, 65, 50, 35, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.MATINAL);this.add(Talent.POING_DE_FER);}};
        this.put("Coxyclaque", new Pokemon("Coxyclaque", 166, 178, Type.INSECTE, Type.VOL, talents, 55, 35, 50, 55, 110, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.CORPS_ARDENT);this.add(Talent.MARQUE_OMBRE);}};
        this.put("Lugulabre", new Pokemon("Lugulabre", 609, 650, Type.SPECTRE, Type.FEU, talents, 60, 55, 90, 145, 90, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.CORPS_MAUDIT);this.add(Talent.MOITEUR);}};
        this.put("Moyade", new Pokemon("Moyade", 593, 634, Type.EAU, Type.SPECTRE, talents, 100, 60, 70, 85, 105, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.NORMALISE);}};
        this.put("Delcatty", new Pokemon("Delcatty", 301, 320, Type.NORMAL, Type.NONE, talents, 70, 65, 65, 55, 55, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.FLORA_VOILE);this.add(Talent.SYMBIOSIS);}};
        this.put("Floette", new Pokemon("Floette", 670, 716, Type.FEE, Type.NONE, talents, 58, 54, 52, 90, 116, 63));

        talents = new ArrayList<Talent>(){{this.add(Talent.MOMIE);}};
        this.put("Tutankafer", new Pokemon("Tutankafer", 563, 604, Type.SPECTRE, Type.NONE, talents, 58, 50, 145, 95, 105, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.FORCE_PURE);this.add(Talent.TELEPATHE);}};
        this.put("Meditikka", new Pokemon("Meditikka", 307, 328, Type.COMBAT, Type.PSY, talents, 30, 40, 55, 40, 55, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_SOIN);this.add(Talent.REGE_FORCE);this.add(Talent.MALADRESSE);}};
        this.put("Nanmeouie", new Pokemon("Nanmeouie", 531, 571, Type.NORMAL, Type.NONE, talents, 103, 60, 86, 60, 86, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.MAGICIEN);}};
        this.put("Feunnec", new Pokemon("Feunnec", 653, 699, Type.FEU, Type.NONE, talents, 40, 45, 40, 62, 60, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);this.add(Talent.IGNIFUGE);this.add(Talent.HEAVY_METAL);}};
        this.put("Archeodong", new Pokemon("Archeodong", 437, 467, Type.ACIER, Type.PSY, talents, 67, 89, 116, 79, 116, 33));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.MOITEUR);this.add(Talent.INCONSCIENT);}};
        this.put("Axoloto", new Pokemon("Axoloto", 194, 207, Type.EAU, Type.SOL, talents, 55, 45, 45, 25, 25, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.FEUIL_GARDE);}};
        this.put("Macronium", new Pokemon("Macronium", 153, 165, Type.PLANTE, Type.NONE, talents, 60, 62, 80, 63, 80, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);}};
        this.put("Rafflesia", new Pokemon("Rafflesia", 45, 49, Type.PLANTE, Type.POISON, talents, 75, 80, 85, 100, 90, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.GLOUTONNERIE);this.add(Talent.CONTESTATION);}};
        this.put("Caratroc", new Pokemon("Caratroc", 213, 227, Type.INSECTE, Type.ROCHE, talents, 20, 10, 230, 10, 230, 5));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);}};
        this.put("Shaymin (Forme Celeste)", new Pokemon("Shaymin (Forme Celeste)", 492, 532, Type.PLANTE, Type.NONE, talents, 100, 103, 75, 120, 75, 127));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.BAIGNE_SABLE);this.add(Talent.QUERELLEUR);}};
        this.put("Ponchien", new Pokemon("Ponchien", 507, 547, Type.NORMAL, Type.NONE, talents, 65, 80, 65, 35, 65, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.MATINAL);this.add(Talent.PICKPOCKET);}};
        this.put("Pifeuil", new Pokemon("Pifeuil", 274, 292, Type.PLANTE, Type.TENEBRE, talents, 70, 70, 40, 60, 40, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.BATTANT);this.add(Talent.GARDE_AMIE);}};
        this.put("Toudoudou", new Pokemon("Toudoudou", 174, 186, Type.NORMAL, Type.NONE, talents, 90, 30, 15, 40, 20, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);this.add(Talent.BAIGNE_SABLE);}};
        this.put("Sablaireau", new Pokemon("Sablaireau", 28, 32, Type.SOL, Type.NONE, talents, 75, 100, 110, 45, 55, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.FOUILLE);this.add(Talent.INSOMNIA);}};
        this.put("Banshitrouye (Taille Mini)", new Pokemon("Banshitrouye (Taille Mini)", 711, 761, Type.SPECTRE, Type.PLANTE, talents, 55, 85, 122, 58, 75, 99));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.SANS_LIMITE);}};
        this.put("Draby", new Pokemon("Draby", 371, 396, Type.DRAGON, Type.NONE, talents, 45, 75, 60, 40, 30, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.AIR_LOCK);}};
        this.put("Rayquaza", new Pokemon("Rayquaza", 384, 409, Type.DRAGON, Type.VOL, talents, 105, 150, 90, 150, 90, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FEUIL_GARDE);this.add(Talent.INFILTRATION);}};
        this.put("Granivol", new Pokemon("Granivol", 187, 200, Type.PLANTE, Type.VOL, talents, 35, 35, 40, 35, 55, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.RIVALITE);this.add(Talent.CRAN);}};
        this.put("Luxio", new Pokemon("Luxio", 404, 432, Type.ELECTRIQUE, Type.NONE, talents, 60, 85, 49, 60, 49, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.DON_FLORAL);}};
        this.put("Ceriflor", new Pokemon("Ceriflor", 421, 451, Type.PLANTE, Type.NONE, talents, 70, 60, 70, 87, 78, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.PICKPOCKET);}};
        this.put("Dimoret", new Pokemon("Dimoret", 461, 494, Type.TENEBRE, Type.GLACE, talents, 70, 120, 65, 45, 85, 125));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.COQUE_ARMURE);this.add(Talent.ARMUROUILLEE);}};
        this.put("Amonita", new Pokemon("Amonita", 138, 147, Type.ROCHE, Type.EAU, talents, 35, 40, 100, 90, 55, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.CHLOROPHYLE);this.add(Talent.ENVELOCAPE);}};
        this.put("Larveyette", new Pokemon("Larveyette", 540, 580, Type.INSECTE, Type.PLANTE, talents, 45, 53, 70, 40, 60, 42));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYPER_CUTTER);this.add(Talent.COQUE_ARMURE);this.add(Talent.SANS_LIMITE);}};
        this.put("Krabboss", new Pokemon("Krabboss", 99, 105, Type.EAU, Type.NONE, talents, 55, 130, 115, 50, 50, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.HYDRATATION);this.add(Talent.ABSORB_EAU);}};
        this.put("Batracne", new Pokemon("Batracne", 536, 576, Type.EAU, Type.SOL, talents, 75, 65, 55, 65, 55, 69));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.SUINTEMENT);this.add(Talent.CUVETTE);}};
        this.put("Tentacool", new Pokemon("Tentacool", 72, 77, Type.EAU, Type.POISON, talents, 40, 40, 35, 50, 100, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.SABLE_VOLANT);this.add(Talent.FORCE_SABLE);}};
        this.put("Hippodocus", new Pokemon("Hippodocus", 450, 482, Type.SOL, Type.NONE, talents, 108, 112, 118, 68, 72, 47));

        talents = new ArrayList<Talent>(){{this.add(Talent.IGNIFU_VOILE);this.add(Talent.BENET);}};
        this.put("Wailmer", new Pokemon("Wailmer", 320, 343, Type.EAU, Type.NONE, talents, 130, 70, 35, 70, 35, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_ARDENT);this.add(Talent.ESPRIT_VITAL);}};
        this.put("Magmar", new Pokemon("Magmar", 126, 133, Type.FEU, Type.NONE, talents, 65, 95, 57, 100, 85, 93));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.INTIMIDATION);}};
        this.put("Caninos", new Pokemon("Caninos", 58, 62, Type.FEU, Type.NONE, talents, 55, 70, 45, 70, 50, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Seleroc", new Pokemon("Seleroc", 337, 360, Type.ROCHE, Type.PSY, talents, 70, 55, 65, 95, 85, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.IMPASSIBLE);this.add(Talent.COEUR_NOBLE);}};
        this.put("Lucario", new Pokemon("Lucario", 448, 479, Type.COMBAT, Type.ACIER, talents, 70, 110, 70, 115, 70, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.ANNULE_GARDE);this.add(Talent.IMPASSIBLE);}};
        this.put("Machopeur", new Pokemon("Machopeur", 67, 72, Type.COMBAT, Type.NONE, talents, 80, 100, 70, 50, 60, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.BENET);this.add(Talent.ADAPTABILITE);}};
        this.put("Barpau", new Pokemon("Barpau", 349, 372, Type.EAU, Type.NONE, talents, 20, 15, 20, 10, 55, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);}};
        this.put("Armulys", new Pokemon("Armulys", 266, 284, Type.INSECTE, Type.NONE, talents, 50, 35, 55, 25, 25, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.ARMURBASTON);this.add(Talent.SNIPER);this.add(Talent.REGARD_VIF);}};
        this.put("Drascore", new Pokemon("Drascore", 452, 484, Type.POISON, Type.TENEBRE, talents, 70, 90, 110, 60, 75, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.TEMPO_PERSO);this.add(Talent.CIEL_GRIS);}};
        this.put("Coudlangue", new Pokemon("Coudlangue", 463, 496, Type.NORMAL, Type.NONE, talents, 110, 85, 95, 80, 95, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.MAGNEPIEGE);this.add(Talent.FORCE_SABLE);}};
        this.put("Tarinorme", new Pokemon("Tarinorme", 476, 509, Type.ROCHE, Type.ACIER, talents, 60, 55, 145, 75, 150, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.HYDRATATION);}};
        this.put("Lovdisc", new Pokemon("Lovdisc", 370, 395, Type.EAU, Type.NONE, talents, 43, 30, 55, 40, 65, 97));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FEUIL_GARDE);this.add(Talent.REGE_FORCE);}};
        this.put("Saquedeneu", new Pokemon("Saquedeneu", 114, 120, Type.PLANTE, Type.NONE, talents, 65, 55, 115, 100, 40, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.MATINAL);this.add(Talent.PICKPOCKET);}};
        this.put("Tengalice", new Pokemon("Tengalice", 275, 293, Type.PLANTE, Type.TENEBRE, talents, 90, 100, 60, 90, 60, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.POING_DE_FER);this.add(Talent.MALADRESSE);this.add(Talent.ANNULE_GARDE);}};
        this.put("Golemastoc", new Pokemon("Golemastoc", 623, 664, Type.SOL, Type.SPECTRE, talents, 89, 124, 80, 55, 80, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.AGITATION);}};
        this.put("Diamat", new Pokemon("Diamat", 634, 675, Type.TENEBRE, Type.DRAGON, talents, 72, 85, 70, 65, 70, 58));

        talents = new ArrayList<Talent>(){{this.add(Talent.FEUIL_GARDE);this.add(Talent.CHLOROPHYLE);}};
        this.put("Phyllali", new Pokemon("Phyllali", 470, 503, Type.PLANTE, Type.NONE, talents, 65, 110, 130, 60, 65, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.INFILTRATION);this.add(Talent.FARCEUR);this.add(Talent.BATTANT);}};
        this.put("Mistigrix", new Pokemon("Mistigrix", 678, 724, Type.PSY, Type.NONE, talents, 74, 48, 76, 83, 81, 104));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.ISOGRAISSE);}};
        this.put("Grotichon", new Pokemon("Grotichon", 499, 539, Type.FEU, Type.COMBAT, talents, 90, 93, 55, 70, 55, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FORCE_SOLEIL);this.add(Talent.RECOLTE);}};
        this.put("Tropius", new Pokemon("Tropius", 357, 381, Type.PLANTE, Type.VOL, talents, 99, 68, 83, 72, 87, 51));

        talents = new ArrayList<Talent>(){{this.add(Talent.POSE_SPORE);this.add(Talent.SOIN_POISON);this.add(Talent.TECHNICIEN);}};
        this.put("Chapignon", new Pokemon("Chapignon", 286, 305, Type.PLANTE, Type.COMBAT, talents, 60, 130, 80, 60, 60, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.VICTORIEUX);}};
        this.put("Victini", new Pokemon("Victini", 494, 534, Type.PSY, Type.FEU, talents, 100, 100, 100, 100, 100, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);}};
        this.put("Ymphect", new Pokemon("Ymphect", 247, 263, Type.ROCHE, Type.SOL, talents, 70, 84, 70, 65, 70, 51));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.RIDEAU_NEIGE);}};
        this.put("Artikodin", new Pokemon("Artikodin", 144, 154, Type.GLACE, Type.VOL, talents, 90, 85, 100, 95, 125, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYDRATATION);}};
        this.put("Phione", new Pokemon("Phione", 489, 528, Type.EAU, Type.NONE, talents, 80, 80, 80, 80, 80, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.TECHNICIEN);this.add(Talent.TENSION);}};
        this.put("Miaouss", new Pokemon("Miaouss", 52, 56, Type.NORMAL, Type.NONE, talents, 40, 45, 35, 40, 40, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_ARDENT);this.add(Talent.AILES_BOURRASQUE);}};
        this.put("Braisillon", new Pokemon("Braisillon", 662, 708, Type.FEU, Type.VOL, talents, 62, 73, 55, 56, 52, 84));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.INSOMNIA);this.add(Talent.SNIPER);}};
        this.put("Migalos", new Pokemon("Migalos", 168, 180, Type.INSECTE, Type.POISON, talents, 70, 90, 70, 60, 60, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.FERMETE);this.add(Talent.PHOBIQUE);}};
        this.put("Manzai", new Pokemon("Manzai", 438, 468, Type.ROCHE, Type.NONE, talents, 50, 80, 95, 10, 45, 10));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.INFILTRATION);}};
        this.put("Nosferapti", new Pokemon("Nosferapti", 41, 45, Type.POISON, Type.VOL, talents, 40, 45, 35, 30, 40, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.CUVETTE);}};
        this.put("Arakdo", new Pokemon("Arakdo", 283, 302, Type.INSECTE, Type.EAU, talents, 40, 30, 32, 50, 52, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.SANS_LIMITE);}};
        this.put("Kaiminus", new Pokemon("Kaiminus", 158, 170, Type.EAU, Type.NONE, talents, 50, 65, 64, 44, 48, 43));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.RIVALITE);}};
        this.put("Charmillon", new Pokemon("Charmillon", 267, 285, Type.INSECTE, Type.VOL, talents, 60, 70, 50, 90, 50, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.PARATONNERRE);this.add(Talent.MOTORISE);this.add(Talent.HERBIVORE);}};
        this.put("Zebibron", new Pokemon("Zebibron", 522, 562, Type.ELECTRIQUE, Type.NONE, talents, 45, 60, 32, 50, 32, 76));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIVALITE);this.add(Talent.BRISE_MOULE);this.add(Talent.TENSION);}};
        this.put("Coupenotte", new Pokemon("Coupenotte", 610, 651, Type.DRAGON, Type.NONE, talents, 46, 87, 60, 30, 40, 57));

        talents = new ArrayList<Talent>(){{this.add(Talent.LUMIATTIRANCE);this.add(Talent.ESSAIM);this.add(Talent.FARCEUR);}};
        this.put("Muciole", new Pokemon("Muciole", 313, 336, Type.INSECTE, Type.NONE, talents, 65, 73, 55, 47, 75, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.TECHNICIEN);this.add(Talent.LIGHT_METAL);}};
        this.put("Cizayox", new Pokemon("Cizayox", 212, 225, Type.INSECTE, Type.ACIER, talents, 70, 130, 100, 55, 80, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);this.add(Talent.PIEGE);this.add(Talent.FORCE_SABLE);}};
        this.put("Triopikeur", new Pokemon("Triopikeur", 51, 55, Type.SOL, Type.NONE, talents, 35, 80, 50, 50, 70, 120));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FEUIL_GARDE);this.add(Talent.INFILTRATION);}};
        this.put("Floravol", new Pokemon("Floravol", 188, 201, Type.PLANTE, Type.VOL, talents, 55, 45, 50, 45, 65, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.SANS_LIMITE);this.add(Talent.POING_DE_FER);}};
        this.put("Ouvrifier", new Pokemon("Ouvrifier", 533, 573, Type.COMBAT, Type.NONE, talents, 85, 105, 85, 40, 50, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.MAUVAIS_REVE);}};
        this.put("Darkrai", new Pokemon("Darkrai", 491, 530, Type.TENEBRE, Type.NONE, talents, 70, 90, 90, 135, 90, 125));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);}};
        this.put("Mew", new Pokemon("Mew", 151, 163, Type.PSY, Type.NONE, talents, 100, 100, 100, 100, 100, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.EPINE_DE_FER);}};
        this.put("Grindur", new Pokemon("Grindur", 597, 638, Type.PLANTE, Type.ACIER, talents, 44, 50, 91, 24, 86, 10));

        talents = new ArrayList<Talent>(){{this.add(Talent.POSE_SPORE);this.add(Talent.SOIN_POISON);this.add(Talent.PIED_VELOCE);}};
        this.put("Balignon", new Pokemon("Balignon", 285, 304, Type.PLANTE, Type.NONE, talents, 60, 40, 60, 40, 60, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.TOXITOUCHE);}};
        this.put("Kravarech", new Pokemon("Kravarech", 691, 738, Type.POISON, Type.DRAGON, talents, 65, 75, 90, 97, 123, 44));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECHAUFFEMENT);this.add(Talent.TEMPO_PERSO);this.add(Talent.REGARD_VIF);}};
        this.put("Chaglam", new Pokemon("Chaglam", 431, 461, Type.NORMAL, Type.NONE, talents, 49, 55, 42, 42, 37, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.AURA_FEERIQUE);}};
        this.put("Xerneas", new Pokemon("Xerneas", 716, 769, Type.FEE, Type.NONE, talents, 126, 131, 95, 131, 98, 99));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESPRIT_VITAL);this.add(Talent.AGITATION);}};
        this.put("Cadoizo", new Pokemon("Cadoizo", 225, 240, Type.GLACE, Type.VOL, talents, 45, 55, 45, 65, 45, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.AMOUR_FILIAL);}};
        this.put("Mega-Kangourex", new Pokemon("Mega-Kangourex", 115, 122, Type.NORMAL, Type.NONE, talents, 105, 125, 100, 60, 100, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.FORCE_SOLEIL);}};
        this.put("Salameche", new Pokemon("Salameche", 4, 5, Type.FEU, Type.NONE, talents, 39, 52, 43, 60, 40, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_VOLT);this.add(Talent.LUMIATTIRANCE);this.add(Talent.ABSORB_EAU);}};
        this.put("Lanturn", new Pokemon("Lanturn", 171, 183, Type.EAU, Type.ELECTRIQUE, talents, 125, 58, 58, 76, 76, 67));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.POING_DE_FER);}};
        this.put("Simiabraz", new Pokemon("Simiabraz", 392, 420, Type.FEU, Type.COMBAT, talents, 76, 104, 71, 104, 71, 108));

        talents = new ArrayList<Talent>(){{this.add(Talent.FOUILLE);this.add(Talent.INFILTRATION);this.add(Talent.TELEPATHE);}};
        this.put("Bruyverne", new Pokemon("Bruyverne", 715, 768, Type.VOL, Type.DRAGON, talents, 85, 70, 80, 97, 80, 123));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYDRATATION);this.add(Talent.HERBIVORE);this.add(Talent.POISSEUX);}};
        this.put("Mucuscule", new Pokemon("Mucuscule", 704, 751, Type.DRAGON, Type.NONE, talents, 40, 50, 30, 70, 100, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.TEMPO_PERSO);this.add(Talent.ACHARNE);}};
        this.put("Chaffreux", new Pokemon("Chaffreux", 432, 462, Type.NORMAL, Type.NONE, talents, 71, 82, 64, 64, 59, 112));

        talents = new ArrayList<Talent>(){{this.add(Talent.DEFAITISTE);}};
        this.put("Aeropteryx", new Pokemon("Aeropteryx", 567, 608, Type.ROCHE, Type.VOL, talents, 75, 140, 65, 112, 65, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.REGARD_VIF);this.add(Talent.PICKPOCKET);}};
        this.put("Farfuret", new Pokemon("Farfuret", 215, 230, Type.TENEBRE, Type.GLACE, talents, 55, 95, 55, 35, 75, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FEUIL_GARDE);this.add(Talent.INFILTRATION);}};
        this.put("Cotovol", new Pokemon("Cotovol", 189, 202, Type.PLANTE, Type.VOL, talents, 75, 55, 70, 55, 85, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.BATTANT);this.add(Talent.GARDE_AMIE);}};
        this.put("Rondoudou", new Pokemon("Rondoudou", 39, 43, Type.NORMAL, Type.NONE, talents, 115, 45, 20, 45, 25, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_GEL);this.add(Talent.ARMUROUILLEE);}};
        this.put("Sorboul", new Pokemon("Sorboul", 583, 624, Type.GLACE, Type.NONE, talents, 51, 65, 65, 80, 75, 59));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.COQUE_ARMURE);this.add(Talent.ARMUROUILLEE);}};
        this.put("Amonistar", new Pokemon("Amonistar", 139, 148, Type.ROCHE, Type.EAU, talents, 70, 60, 125, 115, 70, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.PLUS);this.add(Talent.MINUS);this.add(Talent.CORPS_SAIN);}};
        this.put("Clic", new Pokemon("Clic", 600, 641, Type.ACIER, Type.NONE, talents, 60, 80, 95, 70, 85, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.FEUIL_GARDE);}};
        this.put("Meganium", new Pokemon("Meganium", 154, 166, Type.PLANTE, Type.NONE, talents, 80, 82, 100, 83, 100, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Deoxys (Forme Defense)", new Pokemon("Deoxys (Forme Defense)", 386, 413, Type.PSY, Type.NONE, talents, 50, 70, 160, 70, 160, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.CORPS_MAUDIT);this.add(Talent.MOITEUR);}};
        this.put("Viskuse", new Pokemon("Viskuse", 592, 633, Type.EAU, Type.SPECTRE, talents, 55, 40, 50, 65, 85, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECHAUFFEMENT);this.add(Talent.IMPOSTEUR);}};
        this.put("Metamorph", new Pokemon("Metamorph", 132, 141, Type.NORMAL, Type.NONE, talents, 48, 48, 48, 48, 48, 48));

        talents = new ArrayList<Talent>(){{this.add(Talent.MATINAL);this.add(Talent.QUERELLEUR);this.add(Talent.ATTENTION);}};
        this.put("Kangourex", new Pokemon("Kangourex", 115, 121, Type.NORMAL, Type.NONE, talents, 105, 95, 80, 40, 80, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.FOUILLE);this.add(Talent.INSOMNIA);}};
        this.put("Pitrouille (Taille Normale)", new Pokemon("Pitrouille (Taille Normale)", 710, 758, Type.SPECTRE, Type.PLANTE, talents, 49, 66, 70, 44, 55, 51));

        talents = new ArrayList<Talent>(){{this.add(Talent.IGNIFU_VOILE);this.add(Talent.BENET);}};
        this.put("Wailord", new Pokemon("Wailord", 321, 344, Type.EAU, Type.NONE, talents, 170, 90, 45, 90, 45, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESPRIT_VITAL);this.add(Talent.COLERIQUE);this.add(Talent.ACHARNE);}};
        this.put("Colossinge", new Pokemon("Colossinge", 57, 61, Type.COMBAT, Type.NONE, talents, 65, 105, 60, 60, 70, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.AURA_TENEBREUSE);}};
        this.put("Yveltal", new Pokemon("Yveltal", 717, 770, Type.TENEBRE, Type.VOL, talents, 126, 131, 95, 131, 98, 99));

        talents = new ArrayList<Talent>(){{this.add(Talent.FARCEUR);this.add(Talent.ACHARNE);}};
        this.put("Fulguris (Forme Totemique)", new Pokemon("Fulguris (Forme Totemique)", 642, 685, Type.ELECTRIQUE, Type.VOL, talents, 79, 105, 70, 145, 80, 101));

        talents = new ArrayList<Talent>(){{this.add(Talent.AGITATION);this.add(Talent.MEDIC_NATURE);}};
        this.put("Corayon", new Pokemon("Corayon", 222, 237, Type.EAU, Type.ROCHE, talents, 55, 55, 85, 65, 85, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.ANNULE_GARDE);this.add(Talent.IMPASSIBLE);}};
        this.put("Mackogneur", new Pokemon("Mackogneur", 68, 73, Type.COMBAT, Type.NONE, talents, 90, 130, 80, 65, 85, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ARMURBASTON);this.add(Talent.SNIPER);this.add(Talent.REGARD_VIF);}};
        this.put("Rapion", new Pokemon("Rapion", 451, 483, Type.POISON, Type.INSECTE, talents, 40, 50, 90, 30, 55, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLOUTONNERIE);this.add(Talent.ENGRAIS);}};
        this.put("Feuiloutan", new Pokemon("Feuiloutan", 512, 552, Type.PLANTE, Type.NONE, talents, 75, 98, 63, 98, 63, 101));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.PIED_VELOCE);this.add(Talent.TENSION);}};
        this.put("Ursaring", new Pokemon("Ursaring", 217, 232, Type.NORMAL, Type.NONE, talents, 90, 130, 75, 75, 75, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ARMURBASTON);this.add(Talent.GLISSADE);}};
        this.put("Anorith", new Pokemon("Anorith", 347, 370, Type.ROCHE, Type.INSECTE, talents, 45, 95, 50, 40, 50, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.CONTESTATION);}};
        this.put("Vipelierre", new Pokemon("Vipelierre", 495, 535, Type.PLANTE, Type.NONE, talents, 45, 45, 55, 45, 55, 63));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.CALQUE);this.add(Talent.TELEPATHE);}};
        this.put("Gardevoir", new Pokemon("Gardevoir", 282, 300, Type.PSY, Type.NONE, talents, 68, 65, 65, 125, 115, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.ESSAIM);this.add(Talent.IMPUDENCE);}};
        this.put("Scarhino", new Pokemon("Scarhino", 214, 228, Type.INSECTE, Type.COMBAT, talents, 80, 125, 75, 40, 95, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.MATINAL);this.add(Talent.TENSION);}};
        this.put("Demolosse", new Pokemon("Demolosse", 229, 244, Type.TENEBRE, Type.FEU, talents, 75, 90, 50, 110, 80, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.TOXITOUCHE);this.add(Talent.ABSORB_EAU);}};
        this.put("Crapustule", new Pokemon("Crapustule", 537, 577, Type.EAU, Type.SOL, talents, 105, 85, 75, 85, 75, 74));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.COQUE_ARMURE);this.add(Talent.ARMUROUILLEE);}};
        this.put("Crabaraque", new Pokemon("Crabaraque", 558, 599, Type.INSECTE, Type.ROCHE, talents, 70, 95, 125, 65, 75, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIVALITE);this.add(Talent.BRISE_MOULE);this.add(Talent.TENSION);}};
        this.put("Tranchodon", new Pokemon("Tranchodon", 612, 653, Type.DRAGON, Type.NONE, talents, 76, 147, 90, 60, 70, 97));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.TENSION);}};
        this.put("Mewtwo", new Pokemon("Mewtwo", 150, 160, Type.PSY, Type.NONE, talents, 106, 110, 90, 154, 90, 130));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.TORCHE);}};
        this.put("Feurisson", new Pokemon("Feurisson", 156, 168, Type.FEU, Type.NONE, talents, 58, 64, 58, 80, 65, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.TETE_DE_ROC);this.add(Talent.HEAVY_METAL);}};
        this.put("Galeking", new Pokemon("Galeking", 306, 326, Type.ACIER, Type.ROCHE, talents, 70, 110, 180, 60, 60, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.LUMIATTIRANCE);this.add(Talent.REGARD_VIF);this.add(Talent.ANALYSTE);}};
        this.put("Miradar", new Pokemon("Miradar", 505, 545, Type.NORMAL, Type.NONE, talents, 60, 85, 69, 60, 69, 77));

        talents = new ArrayList<Talent>(){{this.add(Talent.SABLE_VOLANT);this.add(Talent.TENSION);}};
        this.put("Tyranocif", new Pokemon("Tyranocif", 248, 264, Type.ROCHE, Type.TENEBRE, talents, 100, 134, 110, 95, 100, 61));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYPER_CUTTER);this.add(Talent.VOILE_SABLE);this.add(Talent.SOIN_POISON);}};
        this.put("Scorvol", new Pokemon("Scorvol", 472, 505, Type.SOL, Type.VOL, talents, 75, 95, 125, 45, 75, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.ABSORB_EAU);}};
        this.put("Demanta", new Pokemon("Demanta", 226, 241, Type.EAU, Type.VOL, talents, 65, 40, 70, 80, 140, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Solaroc", new Pokemon("Solaroc", 338, 361, Type.ROCHE, Type.PSY, talents, 70, 95, 85, 55, 65, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_DE_COQ);this.add(Talent.AILES_BOURRASQUE);}};
        this.put("Passerouge", new Pokemon("Passerouge", 661, 707, Type.NORMAL, Type.VOL, talents, 45, 50, 43, 40, 38, 62));

        talents = new ArrayList<Talent>(){{this.add(Talent.MULTI_COUPS);}};
        this.put("Mega-Scarhino", new Pokemon("Mega-Scarhino", 214, 229, Type.INSECTE, Type.COMBAT, talents, 80, 185, 115, 40, 105, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.MOITEUR);}};
        this.put("Flobio", new Pokemon("Flobio", 259, 277, Type.EAU, Type.SOL, talents, 70, 85, 70, 60, 70, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIDEAU_NEIGE);}};
        this.put("Cochignon", new Pokemon("Cochignon", 221, 236, Type.GLACE, Type.SOL, talents, 100, 100, 80, 60, 60, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.POINT_POISON);this.add(Talent.TECHNICIEN);}};
        this.put("Roserade", new Pokemon("Roserade", 407, 435, Type.PLANTE, Type.POISON, talents, 60, 70, 55, 125, 105, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.SIMPLE);}};
        this.put("Chamallot", new Pokemon("Chamallot", 322, 345, Type.FEU, Type.SOL, talents, 60, 60, 40, 65, 45, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECHAUFFEMENT);this.add(Talent.DELESTAGE);this.add(Talent.FARCEUR);}};
        this.put("Chacripan", new Pokemon("Chacripan", 509, 549, Type.TENEBRE, Type.NONE, talents, 41, 50, 37, 50, 37, 66));

        talents = new ArrayList<Talent>(){{this.add(Talent.INFILTRATION);this.add(Talent.REGARD_VIF);this.add(Talent.TEMPO_PERSO);}};
        this.put("Psystigri", new Pokemon("Psystigri", 677, 723, Type.PSY, Type.NONE, talents, 60, 22, 62, 72, 72, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.FOUILLE);this.add(Talent.BATTANT);this.add(Talent.MARQUE_OMBRE);}};
        this.put("Scrutella", new Pokemon("Scrutella", 574, 615, Type.PSY, Type.NONE, talents, 45, 30, 50, 55, 65, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGE_FORCE);this.add(Talent.ATTENTION);this.add(Talent.TEMERAIRE);}};
        this.put("Kungfouine", new Pokemon("Kungfouine", 619, 660, Type.COMBAT, Type.NONE, talents, 45, 85, 50, 55, 50, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIDEAU_NEIGE);this.add(Talent.CORPS_MAUDIT);}};
        this.put("Momartik", new Pokemon("Momartik", 478, 511, Type.GLACE, Type.SPECTRE, talents, 70, 80, 70, 80, 70, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECHAUFFEMENT);this.add(Talent.DELESTAGE);this.add(Talent.FARCEUR);}};
        this.put("Leopardus", new Pokemon("Leopardus", 510, 550, Type.TENEBRE, Type.NONE, talents, 64, 88, 50, 88, 50, 106));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.REGE_FORCE);}};
        this.put("Ho-Oh", new Pokemon("Ho-Oh", 250, 267, Type.FEU, Type.VOL, talents, 106, 130, 90, 110, 154, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYPER_CUTTER);this.add(Talent.COQUE_ARMURE);this.add(Talent.SANS_LIMITE);}};
        this.put("Krabby", new Pokemon("Krabby", 98, 104, Type.EAU, Type.NONE, talents, 30, 105, 90, 25, 25, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.ABSORB_EAU);}};
        this.put("Suicune", new Pokemon("Suicune", 245, 261, Type.EAU, Type.NONE, talents, 100, 75, 115, 90, 115, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.PARATONNERRE);this.add(Talent.MOTORISE);this.add(Talent.HERBIVORE);}};
        this.put("Zeblitz", new Pokemon("Zeblitz", 523, 563, Type.ELECTRIQUE, Type.NONE, talents, 75, 100, 63, 80, 63, 116));

        talents = new ArrayList<Talent>(){{this.add(Talent.BAJOUES);this.add(Talent.RAMASSAGE);this.add(Talent.COLOFORCE);}};
        this.put("Excavarenne", new Pokemon("Excavarenne", 660, 706, Type.NORMAL, Type.SOL, talents, 85, 56, 77, 50, 77, 78));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.VOILE_SABLE);}};
        this.put("Donphan", new Pokemon("Donphan", 232, 248, Type.SOL, Type.NONE, talents, 90, 120, 120, 60, 60, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.TEMPO_PERSO);this.add(Talent.CORPS_GEL);this.add(Talent.FERMETE);}};
        this.put("Grelacon", new Pokemon("Grelacon", 712, 765, Type.GLACE, Type.NONE, talents, 55, 69, 85, 32, 35, 28));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.FOUILLE);this.add(Talent.INSOMNIA);}};
        this.put("Pitrouille (Taille Ultra)", new Pokemon("Pitrouille (Taille Ultra)", 710, 760, Type.SPECTRE, Type.PLANTE, talents, 59, 66, 70, 44, 55, 41));

        talents = new ArrayList<Talent>(){{this.add(Talent.ALERTE_NEIGE);this.add(Talent.ANTI_BRUIT);}};
        this.put("Blizzi", new Pokemon("Blizzi", 459, 491, Type.PLANTE, Type.GLACE, talents, 60, 62, 50, 62, 60, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.MIROIR_MAGIK);}};
        this.put("Mega-Absol", new Pokemon("Mega-Absol", 359, 384, Type.TENEBRE, Type.NONE, talents, 65, 150, 60, 115, 60, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.FERMETE);}};
        this.put("Strassie", new Pokemon("Strassie", 703, 750, Type.ROCHE, Type.FEE, talents, 50, 50, 150, 50, 150, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.FARCEUR);this.add(Talent.MAGICIEN);}};
        this.put("Trousselin", new Pokemon("Trousselin", 707, 754, Type.ACIER, Type.FEE, talents, 57, 80, 91, 80, 87, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.METEO);}};
        this.put("Morpheo", new Pokemon("Morpheo", 351, 374, Type.NORMAL, Type.NONE, talents, 70, 70, 70, 70, 70, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.REGARD_VIF);this.add(Talent.ARMUROUILLEE);}};
        this.put("Airmure", new Pokemon("Airmure", 227, 242, Type.ACIER, Type.VOL, talents, 65, 80, 140, 40, 70, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTI_BRUIT);this.add(Talent.FILTRE);this.add(Talent.TECHNICIEN);}};
        this.put("M. Mime", new Pokemon("M. Mime", 122, 129, Type.PSY, Type.NONE, talents, 40, 45, 65, 100, 120, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.MATINAL);this.add(Talent.MIROIR_MAGIK);}};
        this.put("Natu", new Pokemon("Natu", 177, 189, Type.PSY, Type.VOL, talents, 40, 50, 45, 70, 45, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);}};
        this.put("Lainergie", new Pokemon("Lainergie", 180, 192, Type.ELECTRIQUE, Type.NONE, talents, 70, 55, 55, 80, 60, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.FORCE_SABLE);}};
        this.put("Mega-Carchacrok", new Pokemon("Mega-Carchacrok", 445, 476, Type.DRAGON, Type.SOL, talents, 108, 170, 115, 120, 95, 92));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.MATINAL);this.add(Talent.PHOBIQUE);}};
        this.put("Coxy", new Pokemon("Coxy", 165, 177, Type.INSECTE, Type.VOL, talents, 40, 20, 30, 40, 80, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);}};
        this.put("Shaymin (Forme Terrestre)", new Pokemon("Shaymin (Forme Terrestre)", 492, 531, Type.PLANTE, Type.NONE, talents, 100, 100, 100, 100, 100, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.FOUILLE);this.add(Talent.INSOMNIA);}};
        this.put("Banshitrouye (Taille Maxi)", new Pokemon("Banshitrouye (Taille Maxi)", 711, 763, Type.SPECTRE, Type.PLANTE, talents, 75, 95, 122, 58, 75, 69));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);this.add(Talent.ABSORB_EAU);}};
        this.put("Cacnea", new Pokemon("Cacnea", 331, 354, Type.PLANTE, Type.NONE, talents, 50, 85, 40, 85, 40, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Smogo", new Pokemon("Smogo", 109, 115, Type.POISON, Type.NONE, talents, 40, 65, 95, 60, 45, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.TORCHE);this.add(Talent.COEUR_NOBLE);}};
        this.put("Arcanin", new Pokemon("Arcanin", 59, 63, Type.FEU, Type.NONE, talents, 90, 110, 80, 100, 80, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECAILLE_SPECIALE);this.add(Talent.BATTANT);this.add(Talent.JOLI_SOURIRE);}};
        this.put("Milobellus", new Pokemon("Milobellus", 350, 373, Type.EAU, Type.NONE, talents, 95, 60, 79, 100, 125, 81));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);this.add(Talent.PIEGE);this.add(Talent.FORCE_SABLE);}};
        this.put("Taupiqueur", new Pokemon("Taupiqueur", 50, 54, Type.SOL, Type.NONE, talents, 10, 55, 25, 35, 45, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.RAMASSAGE);this.add(Talent.MULTI_COUPS);}};
        this.put("Capumain", new Pokemon("Capumain", 190, 203, Type.NORMAL, Type.NONE, talents, 55, 70, 55, 40, 55, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.FARCEUR);this.add(Talent.ACHARNE);}};
        this.put("Fulguris (Forme Avatar)", new Pokemon("Fulguris (Forme Avatar)", 642, 684, Type.ELECTRIQUE, Type.VOL, talents, 79, 115, 70, 125, 80, 111));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.ANNULE_GARDE);this.add(Talent.IMPASSIBLE);}};
        this.put("Machoc", new Pokemon("Machoc", 66, 71, Type.COMBAT, Type.NONE, talents, 70, 80, 50, 35, 35, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.CUVETTE);}};
        this.put("Ludicolo", new Pokemon("Ludicolo", 272, 290, Type.EAU, Type.PLANTE, talents, 80, 70, 70, 90, 100, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);this.add(Talent.REGARD_VIF);this.add(Talent.LENTITEINTEE);}};
        this.put("Noarfang", new Pokemon("Noarfang", 164, 176, Type.NORMAL, Type.VOL, talents, 100, 50, 50, 76, 96, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.SERENITE);}};
        this.put("Meloetta (Forme Danse)", new Pokemon("Meloetta (Forme Danse)", 648, 694, Type.NORMAL, Type.PSY, talents, 100, 128, 90, 77, 77, 128));

        talents = new ArrayList<Talent>(){{this.add(Talent.VENTOUSE);this.add(Talent.CONTESTATION);this.add(Talent.INFILTRATION);}};
        this.put("Sepiatop", new Pokemon("Sepiatop", 686, 733, Type.TENEBRE, Type.PSY, talents, 53, 54, 53, 37, 46, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.AGITATION);this.add(Talent.ABSENTEISME);}};
        this.put("Fermite", new Pokemon("Fermite", 632, 673, Type.INSECTE, Type.ACIER, talents, 58, 109, 112, 48, 48, 109));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.CORPS_GEL);}};
        this.put("Regice", new Pokemon("Regice", 378, 403, Type.GLACE, Type.NONE, talents, 80, 50, 100, 100, 200, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ARMURBASTON);this.add(Talent.GLISSADE);}};
        this.put("Armaldo", new Pokemon("Armaldo", 348, 371, Type.ROCHE, Type.INSECTE, talents, 75, 125, 100, 70, 80, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.TELEPATHE);this.add(Talent.SYNCHRO);this.add(Talent.ANALYSTE);}};
        this.put("Lewsor", new Pokemon("Lewsor", 605, 646, Type.PSY, Type.NONE, talents, 55, 55, 55, 85, 55, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLUE);this.add(Talent.LAVABO);this.add(Talent.FORCE_SABLE);}};
        this.put("Sancoki", new Pokemon("Sancoki", 422, 452, Type.EAU, Type.NONE, talents, 76, 48, 48, 57, 62, 34));

        talents = new ArrayList<Talent>(){{this.add(Talent.FORCE_SABLE);this.add(Talent.SANS_LIMITE);}};
        this.put("Demeteros (Forme Totemique)", new Pokemon("Demeteros (Forme Totemique)", 645, 689, Type.SOL, Type.VOL, talents, 89, 145, 90, 105, 80, 91));

        talents = new ArrayList<Talent>(){{this.add(Talent.POSE_SPORE);this.add(Talent.REGE_FORCE);}};
        this.put("Trompignon", new Pokemon("Trompignon", 590, 631, Type.PLANTE, Type.POISON, talents, 69, 55, 45, 55, 55, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.GLOUTONNERIE);}};
        this.put("Empiflor", new Pokemon("Empiflor", 71, 76, Type.PLANTE, Type.POISON, talents, 80, 105, 65, 100, 60, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.ENVELOCAPE);}};
        this.put("Drackhaus", new Pokemon("Drackhaus", 372, 397, Type.DRAGON, Type.NONE, talents, 65, 95, 100, 60, 50, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECRAN_POUDRE);this.add(Talent.FUITE);}};
        this.put("Chenipan", new Pokemon("Chenipan", 10, 14, Type.INSECTE, Type.NONE, talents, 45, 30, 35, 20, 20, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);this.add(Talent.ECHAUFFEMENT);this.add(Talent.VOILE_SABLE);}};
        this.put("Limonde", new Pokemon("Limonde", 618, 659, Type.ELECTRIQUE, Type.SOL, talents, 109, 66, 84, 81, 99, 32));

        talents = new ArrayList<Talent>(){{this.add(Talent.BOOM_FINAL);this.add(Talent.DELESTAGE);this.add(Talent.RAGE_BRULURE);}};
        this.put("Grodrive", new Pokemon("Grodrive", 426, 456, Type.SPECTRE, Type.VOL, talents, 150, 80, 44, 90, 54, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.FLORA_VOILE);this.add(Talent.SYMBIOSIS);}};
        this.put("Flabebe", new Pokemon("Flabebe", 669, 715, Type.FEE, Type.NONE, talents, 44, 38, 39, 61, 79, 42));

        talents = new ArrayList<Talent>(){{this.add(Talent.CALQUE);}};
        this.put("Mega-Alakazam", new Pokemon("Mega-Alakazam", 65, 70, Type.PSY, Type.NONE, talents, 55, 50, 65, 175, 95, 150));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.ESSAIM);this.add(Talent.PIED_VELOCE);}};
        this.put("Brutapode", new Pokemon("Brutapode", 545, 585, Type.INSECTE, Type.POISON, talents, 60, 90, 89, 55, 69, 112));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Deoxys (Forme de Base)", new Pokemon("Deoxys (Forme de Base)", 386, 411, Type.PSY, Type.NONE, talents, 50, 150, 50, 150, 50, 150));

        talents = new ArrayList<Talent>(){{this.add(Talent.SOLIDE_ROC);this.add(Talent.FERMETE);this.add(Talent.GLISSADE);}};
        this.put("Megapagos", new Pokemon("Megapagos", 565, 606, Type.EAU, Type.ROCHE, talents, 74, 108, 133, 83, 65, 32));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHANCEUX);this.add(Talent.COEUR_DE_COQ);this.add(Talent.RIVALITE);}};
        this.put("Deflaisan", new Pokemon("Deflaisan", 521, 561, Type.NORMAL, Type.VOL, talents, 80, 105, 80, 65, 55, 93));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Spectrum", new Pokemon("Spectrum", 93, 98, Type.SPECTRE, Type.POISON, talents, 45, 50, 45, 115, 55, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.POING_DE_FER);this.add(Talent.BRISE_MOULE);this.add(Talent.QUERELLEUR);}};
        this.put("Pandarbare", new Pokemon("Pandarbare", 675, 721, Type.COMBAT, Type.TENEBRE, talents, 95, 124, 78, 69, 71, 58));

        talents = new ArrayList<Talent>(){{this.add(Talent.PROGNATHE);}};
        this.put("Rexillius", new Pokemon("Rexillius", 697, 744, Type.ROCHE, Type.DRAGON, talents, 82, 121, 119, 69, 59, 71));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.CORPS_ARDENT);}};
        this.put("Sulfura", new Pokemon("Sulfura", 146, 156, Type.FEU, Type.VOL, talents, 90, 100, 90, 125, 85, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.IMPUDENCE);}};
        this.put("Drattak", new Pokemon("Drattak", 373, 398, Type.DRAGON, Type.VOL, talents, 95, 135, 80, 110, 80, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.TEMPO_PERSO);this.add(Talent.CORPS_GEL);this.add(Talent.FERMETE);}};
        this.put("Seracrawl", new Pokemon("Seracrawl", 713, 766, Type.GLACE, Type.NONE, talents, 95, 117, 184, 44, 46, 28));
    }};
}

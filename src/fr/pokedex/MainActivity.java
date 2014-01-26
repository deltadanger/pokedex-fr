package fr.pokedex;


import java.io.IOException;
import java.util.HashMap;

import android.app.Activity;
import android.app.AlertDialog;
import android.app.SearchManager;
import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.text.SpannableString;
import android.text.style.UnderlineSpan;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ImageView;
import android.widget.LinearLayout.LayoutParams;
import android.widget.SearchView;
import android.widget.TextView;
import fr.pokedex.utils.Utils;

/*
 * TODO:
 * - Fix autocompletion speed
 */

public class MainActivity extends Activity {
	
	private final int STAT_BAR_HEIGHT = 57;
	private final int COLOUR_LIFE = Color.rgb(128, 255, 128);
	private final int COLOUR_ATTACK = Color.rgb(255, 128, 128);
	private final int COLOUR_DEFENSE = Color.rgb(255, 255, 128);
	private final int COLOUR_SP_ATTACK = Color.rgb(255, 128, 255);
	private final int COLOUR_SP_DEFENSE = Color.rgb(128, 128, 128);
	private final int COLOUR_SPEED = Color.rgb(128, 255, 255);

	private final int WEAKNESS_BLOCK_WIDTH = 140;
	private final int WEAKNESS_BLOCK_HEIGHT = 60;

    private Pokemon currentPokemon;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        SearchManager searchManager = (SearchManager) getSystemService(Context.SEARCH_SERVICE);
        SearchView searchView = (SearchView) findViewById(R.id.search_text);
        
        searchView.setSearchableInfo(searchManager.getSearchableInfo(getComponentName()));
        searchView.setIconified(false);
        
        performSearch("Bulbizarre");
        

        TextView talentTxt = (TextView)findViewById(R.id.talent1Txt);
        talentTxt.setOnClickListener(new OnClickListener() {
            
            @Override
            public void onClick(View v) {
                AlertDialog.Builder b = new AlertDialog.Builder(MainActivity.this);
                Talent ability = currentPokemon.abilities.get(0);
                b.setTitle(ability.name);
                
                String message = ability.inFight;
                if (!"".equals(ability.outFight)) {
                    message += "\n------------------\n" + ability.outFight;
                }
                b.setMessage(message);
                
                AlertDialog dialog = b.create();
                dialog.show();
            }
        });

        talentTxt = (TextView)findViewById(R.id.talent2Txt);
        talentTxt.setOnClickListener(new OnClickListener() {
            
            @Override
            public void onClick(View v) {
                AlertDialog.Builder b = new AlertDialog.Builder(MainActivity.this);
                Talent ability = currentPokemon.abilities.get(1);
                b.setTitle(ability.name);
                
                String message = ability.inFight;
                if (!"".equals(ability.outFight)) {
                    message += "\n------------------\n" + ability.outFight;
                }
                b.setMessage(message);
                
                AlertDialog dialog = b.create();
                dialog.show();
            }
        });

        talentTxt = (TextView)findViewById(R.id.talent3Txt);
        talentTxt.setOnClickListener(new OnClickListener() {
            
            @Override
            public void onClick(View v) {
                AlertDialog.Builder b = new AlertDialog.Builder(MainActivity.this);
                Talent ability = currentPokemon.abilities.get(2);
                b.setTitle(ability.name);
                
                String message = ability.inFight;
                if (!"".equals(ability.outFight)) {
                    message += "\n------------------\n" + ability.outFight;
                }
                b.setMessage(message);
                
                AlertDialog dialog = b.create();
                dialog.show();
            }
        });
    }
    
    @Override
    protected void onNewIntent(Intent intent) {
        super.onNewIntent(intent);
        setIntent(intent);
        checkSearch();
    }
    
    private void checkSearch() {
        // Get the intent, verify the action and get the query
        Intent intent = getIntent();
        if (Intent.ACTION_SEARCH.equals(intent.getAction())) {
            String query = intent.getStringExtra(SearchManager.QUERY);
            performSearch(query);
        }
        if (/*Intent.ACTION_VIEW*/"android.Intent.action.VIEW".equals(intent.getAction())) {
            String query = intent.getDataString();
            performSearch(query);
        }
    }
    
    private void performSearch(String query) {
        currentPokemon = PokemonList.perName.get(query);
        TextView nameTxt = (TextView)findViewById(R.id.nameTxt);
        nameTxt.setText(currentPokemon.name);
        
        TextView numberTxt = (TextView)findViewById(R.id.numberTxt);
        numberTxt.setText("#" + currentPokemon.number);
        
        try {
            ImageView image = (ImageView)findViewById(R.id.icon);
            image.setImageDrawable(Drawable.createFromStream(getAssets().open("image/" + Utils.standardize(currentPokemon.name) + ".png"), null));
        } catch (IOException e) {
            e.printStackTrace();
        }

        ImageView type = (ImageView)findViewById(R.id.type1);
        type.setImageResource(currentPokemon.type1.image);
        type = (ImageView)findViewById(R.id.type2);
        type.setImageResource(currentPokemon.type2.image);
        
        TextView talentTxt = (TextView)findViewById(R.id.talent1Txt);
        SpannableString content = new SpannableString(currentPokemon.abilities.get(0).name);
        content.setSpan(new UnderlineSpan(), 0, currentPokemon.abilities.get(0).name.length(), 0);
        talentTxt.setText(content);
        
        if (currentPokemon.abilities.size() > 1) {
            talentTxt = (TextView)findViewById(R.id.talent2Txt);
            content = new SpannableString(currentPokemon.abilities.get(1).name);
            content.setSpan(new UnderlineSpan(), 0, currentPokemon.abilities.get(1).name.length(), 0);
            talentTxt.setText(content);
        }
        
        if (currentPokemon.abilities.size() > 2) {
            talentTxt = (TextView)findViewById(R.id.talent3Txt);
            content = new SpannableString(currentPokemon.abilities.get(2).name);
            content.setSpan(new UnderlineSpan(), 0, currentPokemon.abilities.get(2).name.length(), 0);
            talentTxt.setText(content);
        }

        TextView statTxt = (TextView)findViewById(R.id.lifeTxt);
        statTxt.setText(""+currentPokemon.life);
        View draw = findViewById(R.id.drawLife);
        draw.setLayoutParams(new LayoutParams(currentPokemon.life*2, STAT_BAR_HEIGHT));
        draw.setBackgroundColor(COLOUR_LIFE);
        
        statTxt = (TextView)findViewById(R.id.attTxt);
        statTxt.setText(""+currentPokemon.attack);
        draw = findViewById(R.id.drawAtt);
        draw.setLayoutParams(new LayoutParams(currentPokemon.attack*2, STAT_BAR_HEIGHT));
        draw.setBackgroundColor(COLOUR_ATTACK);
        
        statTxt = (TextView)findViewById(R.id.defTxt);
        statTxt.setText(""+currentPokemon.defense);
        draw = findViewById(R.id.drawDef);
        draw.setLayoutParams(new LayoutParams(currentPokemon.defense*2, STAT_BAR_HEIGHT));
        draw.setBackgroundColor(COLOUR_DEFENSE);
        
        statTxt = (TextView)findViewById(R.id.spaTxt);
        statTxt.setText(""+currentPokemon.spAttack);
        draw = findViewById(R.id.drawSpa);
        draw.setLayoutParams(new LayoutParams(currentPokemon.spAttack*2, STAT_BAR_HEIGHT));
        draw.setBackgroundColor(COLOUR_SP_ATTACK);
        
        statTxt = (TextView)findViewById(R.id.spdTxt);
        statTxt.setText(""+currentPokemon.spDefense);
        draw = findViewById(R.id.drawSpd);
        draw.setLayoutParams(new LayoutParams(currentPokemon.spDefense*2, STAT_BAR_HEIGHT));
        draw.setBackgroundColor(COLOUR_SP_DEFENSE);
        
        statTxt = (TextView)findViewById(R.id.speedTxt);
        statTxt.setText(""+currentPokemon.speed);
        draw = findViewById(R.id.drawSpeed);
        draw.setLayoutParams(new LayoutParams(currentPokemon.speed*2, STAT_BAR_HEIGHT));
        draw.setBackgroundColor(COLOUR_SPEED);
        
        
        HashMap<Type, Weakness>weaknesses = currentPokemon.getWeaknesses();

        View typeWeakness = findViewById(R.id.acier);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.ACIER).resource);
        
        typeWeakness = findViewById(R.id.combat);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.COMBAT).resource);
        
        typeWeakness = findViewById(R.id.dragon);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.DRAGON).resource);
        
        typeWeakness = findViewById(R.id.eau);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.EAU).resource);
        
        typeWeakness = findViewById(R.id.electrique);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.ELECTRIQUE).resource);
        
        typeWeakness = findViewById(R.id.fee);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.FEE).resource);
        
        typeWeakness = findViewById(R.id.feu);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.FEU).resource);
        
        typeWeakness = findViewById(R.id.glace);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.GLACE).resource);
        
        typeWeakness = findViewById(R.id.insecte);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.INSECTE).resource);
        
        typeWeakness = findViewById(R.id.normal);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.NORMAL).resource);
        
        typeWeakness = findViewById(R.id.plante);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.PLANTE).resource);
        
        typeWeakness = findViewById(R.id.poison);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.POISON).resource);
        
        typeWeakness = findViewById(R.id.psy);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.PSY).resource);
        
        typeWeakness = findViewById(R.id.roche);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.ROCHE).resource);
        
        typeWeakness = findViewById(R.id.sol);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.SOL).resource);
        
        typeWeakness = findViewById(R.id.spectre);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.SPECTRE).resource);
        
        typeWeakness = findViewById(R.id.tenebre);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.TENEBRE).resource);
        
        typeWeakness = findViewById(R.id.vol);
        typeWeakness.setLayoutParams(new LayoutParams(WEAKNESS_BLOCK_WIDTH, WEAKNESS_BLOCK_HEIGHT));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.VOL).resource);
    }
}

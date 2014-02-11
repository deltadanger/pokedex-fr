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
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.Toast;
import android.widget.LinearLayout.LayoutParams;
import android.widget.SearchView;
import android.widget.TextView;
import fr.pokedex.data.Pokemon;
import fr.pokedex.data.PokemonList;
import fr.pokedex.data.Talent;
import fr.pokedex.data.Type;
import fr.pokedex.data.Weakness;
import fr.pokedex.utils.Utils;

public class PokemonPage extends Activity {

    public static final String INTENT_EXTRA_POKEMON_NUMBER = "intent_extra_pokemon_number";

    private final int COLOUR_LIFE = Color.rgb(79, 202, 30);
    private final int COLOUR_ATTACK = Color.rgb(227, 11, 11);
    private final int COLOUR_DEFENSE = Color.rgb(254, 212, 43);
    private final int COLOUR_SP_ATTACK = Color.rgb(202, 30, 180);
    private final int COLOUR_SP_DEFENSE = Color.rgb(126, 67, 246);
    private final int COLOUR_SPEED = Color.rgb(30, 180, 180);

    private final int STAT_BAR_HEIGHT = 19;
    private final int WEAKNESS_BLOCK_WIDTH = 46;
    private final int WEAKNESS_BLOCK_HEIGHT = 20;
    
    private final int EVOLUTION_PIC_WIDTH = 30;
    private final int EVOLUTION_PIC_HEIGHT = 30;
    private final int ARROW_WIDTH = 10;
    private final int ARROW_HEIGHT = 10;
    private final int EVOLUTION_MARGIN = 3;
    private final int ARROW_MARGIN_LEFT = 3;
    private final int ARROW_MARGIN_TOP = 10;
    
    private final int SWIPE_MIN_MOVE = 20;
    private float touchPositionX = 0f;
    
    private float dpToPx;
    private Pokemon currentPokemon;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        dpToPx = this.getResources().getDisplayMetrics().density;
        
        SearchManager searchManager = (SearchManager) getSystemService(Context.SEARCH_SERVICE);
        SearchView searchView = (SearchView) findViewById(R.id.search_text);
        
        searchView.setSearchableInfo(searchManager.getSearchableInfo(getComponentName()));
        searchView.setIconified(false);
        
        Intent intent = getIntent();

        if (/*Intent.ACTION_VIEW*/"android.Intent.action.VIEW".equals(intent.getAction())) {
            String query = intent.getDataString();
            loadData(query);
        } else {
            int number = intent.getIntExtra(INTENT_EXTRA_POKEMON_NUMBER, 1);
            loadData(number);
        }
        
        TextView talentTxt = (TextView)findViewById(R.id.talent1Txt);
        talentTxt.setOnClickListener(new OnClickListener() {
            
            @Override
            public void onClick(View v) {
                showTalentDialog(0);
            }
        });

        talentTxt = (TextView)findViewById(R.id.talent2Txt);
        talentTxt.setOnClickListener(new OnClickListener() {
            
            @Override
            public void onClick(View v) {
                showTalentDialog(1);
            }
        });

        talentTxt = (TextView)findViewById(R.id.talent3Txt);
        talentTxt.setOnClickListener(new OnClickListener() {
            
            @Override
            public void onClick(View v) {
                showTalentDialog(2);
            }
        });
    }
    
    @Override
    public boolean onTouchEvent(MotionEvent event) {
        final int swipeDetect = (int)(SWIPE_MIN_MOVE*dpToPx + 0.5f);
        switch (event.getAction())
        {
        // when user first touches the screen we get x and y coordinate
        case MotionEvent.ACTION_DOWN:
            touchPositionX = event.getX();
            break;
        case MotionEvent.ACTION_UP:
            float position = event.getX();

            if (position - touchPositionX > swipeDetect && currentPokemon.number - 1 > 0) {
                Intent intent = new Intent(this, PokemonPage.class);
                intent.putExtra(INTENT_EXTRA_POKEMON_NUMBER, currentPokemon.number - 1);
                startActivity(intent);
                overridePendingTransition(R.anim.slide_left_in, R.anim.slide_left_out);
                finish();
            }

            if (touchPositionX - position > swipeDetect && currentPokemon.number + 1 < PokemonList.perNumber.size()) {
                Intent intent = new Intent(this, PokemonPage.class);
                intent.putExtra(INTENT_EXTRA_POKEMON_NUMBER, currentPokemon.number + 1);
                startActivity(intent);
                overridePendingTransition(R.anim.slide_right_in, R.anim.slide_right_out);
                finish();
            }
            break;
        }
        return false;
    }
    
    private void showTalentDialog(int n) {
        AlertDialog.Builder b = new AlertDialog.Builder(PokemonPage.this);
        Talent ability = currentPokemon.abilities.get(n);
        b.setTitle(ability.name);
        
        String message = ability.inFight;
        if (!"".equals(ability.outFight)) {
            message += "\n------------------\n" + ability.outFight;
        }
        b.setMessage(message);
        
        AlertDialog dialog = b.create();
        dialog.show();
    }
    
    private void loadData(int number) {
        currentPokemon = PokemonList.perNumber.get(number);
        loadData();
    }
    
    private void loadData(String name) {
        currentPokemon = PokemonList.perName.get(name);
        loadData();
    }
    
    private void loadData() {
        
        final int barHeight = (int)(STAT_BAR_HEIGHT*dpToPx + 0.5f);
        final int weaknessBlockWidth = (int)(WEAKNESS_BLOCK_WIDTH*dpToPx + 0.5f);
        final int weaknessBlockHeight = (int)(WEAKNESS_BLOCK_HEIGHT*dpToPx + 0.5f);
        
        TextView nameTxt = (TextView)findViewById(R.id.nameTxt);
        nameTxt.setText(currentPokemon.name);
        
        TextView numberTxt = (TextView)findViewById(R.id.numberTxt);
        numberTxt.setText("#" + currentPokemon.number);
        
        try {
            ImageView image = (ImageView)findViewById(R.id.icon);
            image.setImageDrawable(Drawable.createFromStream(getAssets().open("image/" + Utils.standardize(currentPokemon.name, true) + ".png"), null));
            image.invalidate();
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        LinearLayout evolutions = (LinearLayout)findViewById(R.id.evolutions);
        evolutions.removeAllViews();
        ImageView img;
        LayoutParams layout;
        for (int i = 0; i < currentPokemon.evolutions.length; i++) {
            final Pokemon p = currentPokemon.evolutions[i];
            try {
                layout = new LayoutParams((int)(EVOLUTION_PIC_WIDTH*dpToPx + 0.5f), (int)(EVOLUTION_PIC_HEIGHT*dpToPx + 0.5f));
                layout.setMargins((int)(EVOLUTION_MARGIN*dpToPx + 0.5f), 0, 0, 0);
                img = new ImageView(this);
                img.setLayoutParams(layout);
                img.setImageDrawable(Drawable.createFromStream(getAssets().open("image/" + Utils.standardize(p.name, true) + ".png"), null));
                img.setOnClickListener(new OnClickListener() {
                    @Override
                    public void onClick(View arg0) {
                        loadData(p.name);
                    }
                });
                evolutions.addView(img);
            } catch (IOException e) {
                e.printStackTrace();
            }
            
            // Another element, add an arrow
            if (i+1 < currentPokemon.evolutions.length) {
                layout = new LayoutParams((int)(ARROW_WIDTH*dpToPx + 0.5f), (int)(ARROW_HEIGHT*dpToPx + 0.5f));
                layout.setMargins((int)(ARROW_MARGIN_LEFT*dpToPx + 0.5f), (int)(ARROW_MARGIN_TOP*dpToPx + 0.5f), 0, 0);
                img = new ImageView(this);
                img.setLayoutParams(layout);
                img.setImageResource(R.drawable.arrow);
                evolutions.addView(img);
            }
        }

        ImageView type = (ImageView)findViewById(R.id.type1);
        type.setImageResource(currentPokemon.type1.image);
        type = (ImageView)findViewById(R.id.type2);
        type.setImageResource(currentPokemon.type2.image);
        
        TextView talentTxt = (TextView)findViewById(R.id.talent1Txt);
        SpannableString content = new SpannableString(currentPokemon.abilities.get(0).name);
        content.setSpan(new UnderlineSpan(), 0, currentPokemon.abilities.get(0).name.length(), 0);
        talentTxt.setText(content);
        
        talentTxt = (TextView)findViewById(R.id.talent2Txt);
        talentTxt.setText("");
        if (currentPokemon.abilities.size() > 1) {
            content = new SpannableString(currentPokemon.abilities.get(1).name);
            content.setSpan(new UnderlineSpan(), 0, currentPokemon.abilities.get(1).name.length(), 0);
            talentTxt.setText(content);
        }
        
        talentTxt = (TextView)findViewById(R.id.talent3Txt);
        talentTxt.setText("");
        if (currentPokemon.abilities.size() > 2) {
            content = new SpannableString(currentPokemon.abilities.get(2).name);
            content.setSpan(new UnderlineSpan(), 0, currentPokemon.abilities.get(2).name.length(), 0);
            talentTxt.setText(content);
        }

        TextView statTxt = (TextView)findViewById(R.id.lifeTxt);
        statTxt.setText(""+currentPokemon.life);
        View draw = findViewById(R.id.drawLife);
        draw.setLayoutParams(new LayoutParams((int)(currentPokemon.life*2f/3f * dpToPx + 0.5f), barHeight));
        draw.setBackgroundColor(COLOUR_LIFE);
        
        statTxt = (TextView)findViewById(R.id.attTxt);
        statTxt.setText(""+currentPokemon.attack);
        draw = findViewById(R.id.drawAtt);
        draw.setLayoutParams(new LayoutParams((int)(currentPokemon.attack*2f/3f * dpToPx + 0.5f), barHeight));
        draw.setBackgroundColor(COLOUR_ATTACK);
        
        statTxt = (TextView)findViewById(R.id.defTxt);
        statTxt.setText(""+currentPokemon.defense);
        draw = findViewById(R.id.drawDef);
        draw.setLayoutParams(new LayoutParams((int)(currentPokemon.defense*2f/3f * dpToPx + 0.5f), barHeight));
        draw.setBackgroundColor(COLOUR_DEFENSE);
        
        statTxt = (TextView)findViewById(R.id.spaTxt);
        statTxt.setText(""+currentPokemon.spAttack);
        draw = findViewById(R.id.drawSpa);
        draw.setLayoutParams(new LayoutParams((int)(currentPokemon.spAttack*2f/3f * dpToPx + 0.5f), barHeight));
        draw.setBackgroundColor(COLOUR_SP_ATTACK);
        
        statTxt = (TextView)findViewById(R.id.spdTxt);
        statTxt.setText(""+currentPokemon.spDefense);
        draw = findViewById(R.id.drawSpd);
        draw.setLayoutParams(new LayoutParams((int)(currentPokemon.spDefense*2f/3f * dpToPx + 0.5f), barHeight));
        draw.setBackgroundColor(COLOUR_SP_DEFENSE);
        
        statTxt = (TextView)findViewById(R.id.speedTxt);
        statTxt.setText(""+currentPokemon.speed);
        draw = findViewById(R.id.drawSpeed);
        draw.setLayoutParams(new LayoutParams((int)(currentPokemon.speed*2f/3f * dpToPx + 0.5f), barHeight));
        draw.setBackgroundColor(COLOUR_SPEED);
        
        
        HashMap<Type, Weakness>weaknesses = currentPokemon.getWeaknesses();

        View typeWeakness = findViewById(R.id.acier);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.ACIER).resource);
        
        typeWeakness = findViewById(R.id.combat);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.COMBAT).resource);
        
        typeWeakness = findViewById(R.id.dragon);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.DRAGON).resource);
        
        typeWeakness = findViewById(R.id.eau);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.EAU).resource);
        
        typeWeakness = findViewById(R.id.electrique);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.ELECTRIQUE).resource);
        
        typeWeakness = findViewById(R.id.fee);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.FEE).resource);
        
        typeWeakness = findViewById(R.id.feu);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.FEU).resource);
        
        typeWeakness = findViewById(R.id.glace);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.GLACE).resource);
        
        typeWeakness = findViewById(R.id.insecte);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.INSECTE).resource);
        
        typeWeakness = findViewById(R.id.normal);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.NORMAL).resource);
        
        typeWeakness = findViewById(R.id.plante);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.PLANTE).resource);
        
        typeWeakness = findViewById(R.id.poison);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.POISON).resource);
        
        typeWeakness = findViewById(R.id.psy);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.PSY).resource);
        
        typeWeakness = findViewById(R.id.roche);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.ROCHE).resource);
        
        typeWeakness = findViewById(R.id.sol);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.SOL).resource);
        
        typeWeakness = findViewById(R.id.spectre);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.SPECTRE).resource);
        
        typeWeakness = findViewById(R.id.tenebre);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.TENEBRE).resource);
        
        typeWeakness = findViewById(R.id.vol);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(Type.VOL).resource);
    }
}

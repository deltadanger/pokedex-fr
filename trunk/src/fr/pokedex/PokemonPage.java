package fr.pokedex;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Locale;

import android.app.Activity;
import android.app.AlertDialog;
import android.app.SearchManager;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.res.Configuration;
import android.content.res.Resources.NotFoundException;
import android.graphics.Color;
import android.graphics.Rect;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.text.SpannableString;
import android.text.style.UnderlineSpan;
import android.util.TypedValue;
import android.view.Gravity;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewTreeObserver.OnGlobalLayoutListener;
import android.view.Window;
import android.view.animation.Animation;
import android.view.animation.Animation.AnimationListener;
import android.widget.HorizontalScrollView;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.LinearLayout.LayoutParams;
import android.widget.ScrollView;
import android.widget.SearchView;
import android.widget.TextView;
import android.widget.Toast;
import fr.pokedex.data.Ability;
import fr.pokedex.data.DataHolder;
import fr.pokedex.data.EggGroup;
import fr.pokedex.data.EvolutionNode;
import fr.pokedex.data.Pokemon;
import fr.pokedex.data.Type;
import fr.pokedex.data.Weakness;
import fr.pokedex.utils.ExpandAnimation;
import fr.pokedex.utils.ExpandAnimation.Direction;
import fr.pokedex.utils.Utils;

public class PokemonPage extends Activity {

    public static final String INTENT_EXTRA_POKEMON_NAME = "intent_extra_pokemon_name";
    public static final String INTENT_EXTRA_SCROLL_POSITION = "intent_extra_scroll_position";
    public static final String DEFAULT_POKEMON_NAME = "name_bulbasaur";
    public static final String LANGUAGE_PREFERENCE = "language_preference";
    public static final String LANGUAGE_PREFERENCE_KEY = "lang";
    
    private static int infosVisibility = View.GONE;

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

    private final int FULL_EVOLUTION_PIC_WIDTH = 80;
    private final int FULL_EVOLUTION_PIC_HEIGHT = 80;
    private final int FULL_EVOLUTION_TITLE_SIZE = 18;
    private final int FULL_EVOLUTION_TITLE_MARGIN = 10;
    private final int FULL_EVOLUTION_PATH_SIZE = 10;

    private final int SWIPE_MIN_MOVE = 50;
    private final int SCROLL_THRESHOLD = 20;
    private float touchPositionX = 0f;
    private float touchPositionY = 0f;
    private boolean disableScroll = false;
    
    private float dpToPx;
    private Pokemon currentPokemon;
    
    private ExpandAnimation animation;
    
    private HorizontalScrollView fullEvolutionsScrollView;
    private HorizontalScrollView touchedScrollView;
    private int touchedScrollViewPosition;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);

        final SharedPreferences languageSettings = getSharedPreferences(LANGUAGE_PREFERENCE, 0);
        
        String lang = languageSettings.getString(LANGUAGE_PREFERENCE_KEY, getResources().getConfiguration().locale.getLanguage());
        setCurrentLanguage(lang);
        
        setContentView(R.layout.activity_main);
        dpToPx = getResources().getDisplayMetrics().density;
        
        SearchManager searchManager = (SearchManager) getSystemService(Context.SEARCH_SERVICE);
        final SearchView searchView = (SearchView) findViewById(R.id.search_text);
        
        searchView.setSearchableInfo(searchManager.getSearchableInfo(getComponentName()));
        searchView.setIconified(false);
        searchView.clearFocus();

        final ImageView language = (ImageView) findViewById(R.id.language);
        final LanguageAdapter adapter = new LanguageAdapter(this, getResources().getStringArray(R.array.languages));
        language.setOnClickListener(new OnClickListener() {
            
            @Override
            public void onClick(View v) {
                AlertDialog dialog = new AlertDialog.Builder(PokemonPage.this)
                .setAdapter(adapter, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        String lang = getResources().getStringArray(R.array.languages)[which].split(";")[0];
                        setCurrentLanguage(lang);

                        ScrollView scroll = (ScrollView)findViewById(R.id.main_scroll);
                        Intent intent = new Intent(PokemonPage.this, PokemonPage.this.getClass());
                        intent.putExtra(INTENT_EXTRA_POKEMON_NAME, currentPokemon.name_str);
                        intent.putExtra(INTENT_EXTRA_SCROLL_POSITION, scroll.getScrollY());
                        startActivity(intent);
                        overridePendingTransition(0, 0);
                        finish();
                        dialog.dismiss();
                    }

                }).create();
                
                dialog.setOnDismissListener(new DialogInterface.OnDismissListener() {
                    @Override
                    public void onDismiss(DialogInterface dialog) {
                        findViewById(R.id.main_layout).requestFocus();
                    }
                });
                
                dialog.show();
            }
        });
        
        final Intent intent = getIntent();
        
        if (/*Intent.ACTION_VIEW*/"android.Intent.action.VIEW".equals(intent.getAction())) {
            overridePendingTransition(0,0);
            String query = intent.getDataString();
            loadData(query);
            
        } else if (Intent.ACTION_SEARCH.equals(intent.getAction())) {
            String originalQuery = intent.getStringExtra(SearchManager.QUERY);
            String query = Utils.standardize(originalQuery);
            
            boolean validSearch = false;
            
            for (Pokemon p : DataHolder.pokemons.values()) {
                String name = Utils.standardize(getResources().getString(p.name));
                String number = Utils.standardize(""+p.number);
                
                if (query.equals(name) || query.equals(number)) {
                    loadData(p.name_str);
                    validSearch = true;
                    break;
                }
            }
            
            if (!validSearch) {
                Toast.makeText(PokemonPage.this, R.string.no_result, Toast.LENGTH_LONG).show();
                loadData(DEFAULT_POKEMON_NAME);
                searchView.setQuery(originalQuery, false);
            }
            
        } else {
            String name = intent.getStringExtra(INTENT_EXTRA_POKEMON_NAME);
            if (name == null) {
                name = DEFAULT_POKEMON_NAME;
            }
            loadData(name);
        }

        final LinearLayout infos = (LinearLayout)findViewById(R.id.info_content);
        infos.getViewTreeObserver().addOnGlobalLayoutListener( 
            new OnGlobalLayoutListener(){

                @SuppressWarnings("deprecation")
                @Override
                public void onGlobalLayout() {
                    animation = new ExpandAnimation(infos);
                    animation.setDuration(500);
                    
                    infos.getViewTreeObserver().removeGlobalOnLayoutListener(this);
//                    infos.getViewTreeObserver().removeOnGlobalLayoutListener(this); // requires API level >= 18
                    infos.setVisibility(infosVisibility);

                    ScrollView scroll = (ScrollView)findViewById(R.id.main_scroll);
                    int scrollPosition = intent.getIntExtra(INTENT_EXTRA_SCROLL_POSITION, 0);
                    scroll.scrollTo(0, scrollPosition);
                }

        });
        
        TextView talentTxt = (TextView)findViewById(R.id.talent1Txt);
        talentTxt.setOnClickListener(new OnClickListener() {
            
            @Override
            public void onClick(View v) {
                showAbilityDialog(0);
            }
        });

        talentTxt = (TextView)findViewById(R.id.talent2Txt);
        talentTxt.setOnClickListener(new OnClickListener() {
            
            @Override
            public void onClick(View v) {
                showAbilityDialog(1);
            }
        });

        talentTxt = (TextView)findViewById(R.id.talent3Txt);
        talentTxt.setOnClickListener(new OnClickListener() {
            
            @Override
            public void onClick(View v) {
                showAbilityDialog(2);
            }
        });
        
        ImageView expandArrow = (ImageView)findViewById(R.id.expand);
        expandArrow.setOnClickListener(new OnClickListener() {
            
            @Override
            public void onClick(View arg0) {
                animateViewHeight(infos);
            }
        });
    }

    private void setCurrentLanguage(String lang) {
        SharedPreferences languageSettings = getSharedPreferences(LANGUAGE_PREFERENCE, 0);
        
        SharedPreferences.Editor editor = languageSettings.edit();
        editor.putString(LANGUAGE_PREFERENCE_KEY, lang);
        editor.commit();

        Locale locale = new Locale(lang);
        Locale.setDefault(locale);
        Configuration config = new Configuration();
        config.locale = locale;
        getBaseContext().getResources().updateConfiguration(config, getBaseContext().getResources().getDisplayMetrics());

        ImageView language = (ImageView) findViewById(R.id.language);
        if (language != null) {
            try {
                language.setImageResource(R.drawable.class.getField(lang).getInt(null));
            } catch (IllegalArgumentException e) {
                e.printStackTrace();
            } catch (IllegalAccessException e) {
                e.printStackTrace();
            } catch (NoSuchFieldException e) {
                e.printStackTrace();
            }
        }
    }
    
    @Override
    public boolean dispatchTouchEvent(MotionEvent event) {
        boolean ret = super.dispatchTouchEvent(event);
        
        float position;
        final ScrollView scroll = (ScrollView)findViewById(R.id.main_scroll);
        
        switch (event.getAction())
        {
        // when user first touches the screen we get x and y coordinate
        case MotionEvent.ACTION_DOWN:
            
            touchedScrollView = getHorizontalScrollView(event.getX(), event.getY());
            touchedScrollViewPosition = 0;
            if (touchedScrollView != null) {
                touchedScrollViewPosition = touchedScrollView.getScrollX();
            }
            touchPositionX = event.getX();
            touchPositionY = event.getY();
            disableScroll = true;
            break;
            
        case MotionEvent.ACTION_UP:
            position = event.getX();
            
            if (touchedScrollView != null && (
                    touchedScrollView.canScrollHorizontally((int) (touchPositionX - position)) ||
                    touchedScrollViewPosition != touchedScrollView.getScrollX())) {
                break;
            }
            
            final int swipeDetect = (int)(SWIPE_MIN_MOVE*dpToPx + 0.5f);

            if (position - touchPositionX > swipeDetect && currentPokemon.hasPrevious()) {
                Intent intent = new Intent(this, this.getClass());
                intent.putExtra(INTENT_EXTRA_POKEMON_NAME, currentPokemon.getPrevious().name_str);
                intent.putExtra(INTENT_EXTRA_SCROLL_POSITION, scroll.getScrollY());
                startActivity(intent);
                overridePendingTransition(R.anim.slide_left_in, R.anim.slide_left_out);
                finish();
            }

            if (touchPositionX - position > swipeDetect && currentPokemon.hasNext()) {
                Intent intent = new Intent(this, this.getClass());
                intent.putExtra(INTENT_EXTRA_POKEMON_NAME, currentPokemon.getNext().name_str);
                intent.putExtra(INTENT_EXTRA_SCROLL_POSITION, scroll.getScrollY());
                startActivity(intent);
                overridePendingTransition(R.anim.slide_right_in, R.anim.slide_right_out);
                finish();
            }
            break;
            
        case MotionEvent.ACTION_MOVE:
            position = event.getY();
            float threshold = Math.max((SCROLL_THRESHOLD*dpToPx + 0.5f), Math.abs(event.getX()-touchPositionX));
            
            // Disable scroll while movement does not exceed threshold
            if (disableScroll && Math.abs(position-touchPositionY) < threshold) {
                scroll.setOnTouchListener(new View.OnTouchListener() {
                    @Override
                    public boolean onTouch(View v, MotionEvent event) {
                        return true;
                    }
                });
            } else {
                scroll.setOnTouchListener(null);
                // Scrolling should not be disabled again until re-touched
                disableScroll = false;
            }
            break;
        }
        
        return ret;
    }
    
    /**
     * Returns the HorizontalScrollView at given coordinates, if it exists.
     */
    private HorizontalScrollView getHorizontalScrollView(float x, float y) {
        View v = findViewById(R.id.evolution_scroll);
        int[] location = {0,0};
        v.getLocationOnScreen(location);
        Rect rect = new Rect(location[0],
                             location[1],
                             location[0] + v.getWidth(),
                             location[1] + v.getHeight());

        if (rect.contains((int) x, (int) y)) {
            return (HorizontalScrollView)v;
        }

        LinearLayout infos = (LinearLayout)findViewById(R.id.info_content);
        if (fullEvolutionsScrollView != null && View.VISIBLE == infos.getVisibility()) {
            fullEvolutionsScrollView.getLocationOnScreen(location);
            rect = new Rect(location[0],
                            location[1],
                            location[0] + fullEvolutionsScrollView.getWidth(),
                            location[1] + fullEvolutionsScrollView.getHeight());

            if (rect.contains((int) x, (int) y)) {
                return fullEvolutionsScrollView;
            }
        }
        
        return null;
    }
    
    private void animateViewHeight(final LinearLayout v) {
        if (View.GONE == v.getVisibility()) {
            infosVisibility = View.VISIBLE;
            animation.setDirection(Direction.EXPAND);
        } else {
            infosVisibility = View.GONE;
            animation.setDirection(Direction.COLLAPSE);
        }

        animation.setAnimationListener(new AnimationListener() {
            
            @Override
            public void onAnimationStart(Animation arg0) {
                v.setVisibility(View.VISIBLE);
            }
            
            @Override
            public void onAnimationRepeat(Animation arg0) {
            }
            
            @Override
            public void onAnimationEnd(Animation arg0) {
                if (View.GONE == infosVisibility) {
                    v.setVisibility(infosVisibility);
                }
            }
        });
        v.startAnimation(animation);
        findViewById(R.id.main_layout).invalidate();
    }
    
    private void showAbilityDialog(int n) {
        AlertDialog.Builder b = new AlertDialog.Builder(PokemonPage.this);
        Ability ability = currentPokemon.abilities.get(n);
        b.setTitle(getResources().getString(ability.name));
        
        String message = getResources().getString(ability.inFight);
        if (!"".equals(getResources().getString(ability.outFight))) {
            message += "\n------------------\n" + getResources().getString(ability.outFight);
        }
        b.setMessage(message);
        
        AlertDialog dialog = b.create();
        dialog.setOnDismissListener(new DialogInterface.OnDismissListener() {
            @Override
            public void onDismiss(DialogInterface dialog) {
                findViewById(R.id.main_layout).requestFocus();
            }
        });
        dialog.show();
    }
    
    private void loadData(String name) {
        try {
            currentPokemon = DataHolder.pokemons.get(name);
            loadData();
        } catch (Exception e) {
            e.printStackTrace();
            Toast.makeText(this, R.string.loading_error, Toast.LENGTH_LONG).show();
            currentPokemon = Pokemon.MISSINGNO;
            loadData();
        }
    }
    
    private void loadData() {
        if (currentPokemon == null) {
            currentPokemon = Pokemon.MISSINGNO;
        }
        
        final int barHeight = (int)(STAT_BAR_HEIGHT*dpToPx + 0.5f);
        final int weaknessBlockWidth = (int)(WEAKNESS_BLOCK_WIDTH*dpToPx + 0.5f);
        final int weaknessBlockHeight = (int)(WEAKNESS_BLOCK_HEIGHT*dpToPx + 0.5f);
        
        TextView nameTxt = (TextView)findViewById(R.id.nameTxt);
        nameTxt.setText(currentPokemon.name);
        
        TextView numberTxt = (TextView)findViewById(R.id.numberTxt);
        numberTxt.setText("#" + currentPokemon.number);
        
        try {
            ImageView image = (ImageView)findViewById(R.id.icon);
            image.setImageDrawable(Drawable.createFromStream(getAssets().open("image/" + currentPokemon.name_str + ".png"), null));
            image.invalidate();
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        Pokemon[] currentPokemonEvolutions = currentPokemon.getSimpleEvolutionList();
        LinearLayout evolutions = (LinearLayout)findViewById(R.id.evolutions);
        evolutions.removeAllViews();
        ImageView img;
        LayoutParams layout;
        for (int i = 0; i < currentPokemonEvolutions.length; i++) {
            final Pokemon p = currentPokemonEvolutions[i];
            try {
                layout = new LayoutParams((int)(EVOLUTION_PIC_WIDTH*dpToPx + 0.5f), (int)(EVOLUTION_PIC_HEIGHT*dpToPx + 0.5f));
                layout.leftMargin = (int)(EVOLUTION_MARGIN*dpToPx + 0.5f);
                img = new ImageView(this);
                img.setLayoutParams(layout);
                img.setImageDrawable(Drawable.createFromStream(
                        getAssets().open(
                                "image/" + p.name_str + ".png"), null));
                img.setOnClickListener(new OnClickListener() {
                    @Override
                    public void onClick(View arg0) {
                        loadData(p.name_str);
                    }
                });
                evolutions.addView(img);
            } catch (IOException e) {
                e.printStackTrace();
            }
            
            // Another element, add an arrow
            if (i+1 < currentPokemonEvolutions.length) {
                layout = new LayoutParams((int)(ARROW_WIDTH*dpToPx + 0.5f), (int)(ARROW_HEIGHT*dpToPx + 0.5f));
                layout.leftMargin = (int)(ARROW_MARGIN_LEFT*dpToPx + 0.5f);
                layout.topMargin = (int)(ARROW_MARGIN_TOP*dpToPx + 0.5f);
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
        SpannableString content = new SpannableString(getResources().getString(currentPokemon.abilities.get(0).name));
        content.setSpan(new UnderlineSpan(), 0, getResources().getString(currentPokemon.abilities.get(0).name).length(), 0);
        talentTxt.setText(content);
        
        talentTxt = (TextView)findViewById(R.id.talent2Txt);
        talentTxt.setText("");
        if (currentPokemon.abilities.size() > 1) {
            content = new SpannableString(getResources().getString(currentPokemon.abilities.get(1).name));
            content.setSpan(new UnderlineSpan(), 0, getResources().getString(currentPokemon.abilities.get(1).name).length(), 0);
            talentTxt.setText(content);
        }
        
        talentTxt = (TextView)findViewById(R.id.talent3Txt);
        talentTxt.setText("");
        if (currentPokemon.abilities.size() > 2) {
            content = new SpannableString(getResources().getString(currentPokemon.abilities.get(2).name));
            content.setSpan(new UnderlineSpan(), 0, getResources().getString(currentPokemon.abilities.get(2).name).length(), 0);
            talentTxt.setText(content);
        }
        
        // Additional information
        if (currentPokemon.hasEvolutions()) {
            LinearLayout fullEvolutionsLayout = (LinearLayout)findViewById(R.id.full_evolutions);
            fullEvolutionsLayout.removeAllViews();
            TextView text = new TextView(this);
            LayoutParams params = new LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
            params.topMargin = (int)(FULL_EVOLUTION_TITLE_MARGIN*dpToPx + 0.5f);
            params.bottomMargin = (int)(FULL_EVOLUTION_TITLE_MARGIN*dpToPx + 0.5f);
            text.setLayoutParams(params);
            text.setTextSize(TypedValue.COMPLEX_UNIT_SP, FULL_EVOLUTION_TITLE_SIZE);
            text.setText(R.string.evolution_chain);
            fullEvolutionsLayout.addView(text);
            
            addEvolutions(currentPokemon.evolutionRoot, fullEvolutionsLayout);
        }
        
        TextView infoTxt = (TextView)findViewById(R.id.size_txt);
        infoTxt.setText(String.format(getResources().getString(R.string.size_value), currentPokemon.size));
        
        infoTxt = (TextView)findViewById(R.id.weight_txt);
        infoTxt.setText(String.format(getResources().getString(R.string.weight_value), currentPokemon.weight));

        String evs = "";
        evs += evChunk(currentPokemon.ev.life, R.string.life_short, !evs.isEmpty());
        evs += evChunk(currentPokemon.ev.attack, R.string.att_short, !evs.isEmpty());
        evs += evChunk(currentPokemon.ev.defense, R.string.def_short, !evs.isEmpty());
        evs += evChunk(currentPokemon.ev.spAttack, R.string.spatt_short, !evs.isEmpty());
        evs += evChunk(currentPokemon.ev.spDefense, R.string.spdef_short, !evs.isEmpty());
        evs += evChunk(currentPokemon.ev.speed, R.string.speed_short, !evs.isEmpty());
        infoTxt = (TextView)findViewById(R.id.ev_txt);
        infoTxt.setText(evs);

        infoTxt = (TextView)findViewById(R.id.catch_rate_txt);
        if (currentPokemon.catchRate >= 0) {
            infoTxt.setText(""+currentPokemon.catchRate);
        } else {
            infoTxt.setText("");
        }
        
        
        infoTxt = (TextView)findViewById(R.id.gender_txt);
        if (currentPokemon.gender >= 0) {
            infoTxt.setText(String.format(getResources().getString(R.string.gender_value), currentPokemon.gender, 100-currentPokemon.gender));
        } else {
            infoTxt.setText("");
        }
        
        infoTxt = (TextView)findViewById(R.id.hatch_txt);
        if (currentPokemon.hatch >= 0) {
            infoTxt.setText(String.format(getResources().getString(R.string.hatch_value), currentPokemon.hatch));
        } else {
            infoTxt.setText("");
        }
        
        
        infoTxt = (TextView)findViewById(R.id.egg_group_txt);
        ArrayList<String> arr = new ArrayList<String>();
        for (EggGroup e : currentPokemon.eggGroup) {
            arr.add(getResources().getString(e.name));
        }
        infoTxt.setText(arr.toString().replace("[", "").replace("]", ""));
        

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
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("STEEL")).resource);
        
        typeWeakness = findViewById(R.id.combat);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("FIGHTING")).resource);
        
        typeWeakness = findViewById(R.id.dragon);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("DRAGON")).resource);
        
        typeWeakness = findViewById(R.id.eau);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("WATER")).resource);

        typeWeakness = findViewById(R.id.electrique);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("ELECTRIC")).resource);
        
        typeWeakness = findViewById(R.id.fee);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("FAIRY")).resource);
        
        typeWeakness = findViewById(R.id.feu);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("FIRE")).resource);
        
        typeWeakness = findViewById(R.id.glace);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("ICE")).resource);
        
        typeWeakness = findViewById(R.id.insecte);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("BUG")).resource);
        
        typeWeakness = findViewById(R.id.normal);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("NORMAL")).resource);
        
        typeWeakness = findViewById(R.id.plante);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("GRASS")).resource);
        
        typeWeakness = findViewById(R.id.poison);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("POISON")).resource);
        
        typeWeakness = findViewById(R.id.psy);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("PSYCHIC")).resource);
        
        typeWeakness = findViewById(R.id.roche);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("ROCK")).resource);
        
        typeWeakness = findViewById(R.id.sol);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("GROUND")).resource);
        
        typeWeakness = findViewById(R.id.spectre);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("GHOST")).resource);
        
        typeWeakness = findViewById(R.id.tenebre);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("DARK")).resource);
        
        typeWeakness = findViewById(R.id.vol);
        typeWeakness.setLayoutParams(new LayoutParams(weaknessBlockWidth, weaknessBlockHeight));
        typeWeakness.setBackgroundResource(weaknesses.get(DataHolder.typeByName.get("FLYING")).resource);
    }
    
    private void addEvolutions(final EvolutionNode root, LinearLayout layout) {
        LayoutParams params;
        ImageView img;
    
        try {
            TextView text = new TextView(this);
            text.setText(root.base.name);
            params = new LayoutParams((int)(FULL_EVOLUTION_PIC_WIDTH*dpToPx + 0.5f), LayoutParams.WRAP_CONTENT);
            params.topMargin = (int)(EVOLUTION_MARGIN*dpToPx + 0.5f);
            params.bottomMargin = (int)(EVOLUTION_MARGIN*dpToPx + 0.5f);
            text.setLayoutParams(params);
            text.setGravity(Gravity.CENTER_HORIZONTAL);
            layout.addView(text);
            
            params = new LayoutParams((int)(FULL_EVOLUTION_PIC_WIDTH*dpToPx + 0.5f), (int)(FULL_EVOLUTION_PIC_HEIGHT*dpToPx + 0.5f));
            img = new ImageView(this);
            img.setLayoutParams(params);
            img.setImageDrawable(Drawable.createFromStream(
                    getAssets().open(
                            "image/" + root.base.name_str + ".png"), null));
            img.setOnClickListener(new OnClickListener() {
                @Override
                public void onClick(View arg0) {
                    loadData(root.base.name_str);
                }
            });
            layout.addView(img);
            
        } catch (IOException e) {
            e.printStackTrace();
        }

        if (root.isLeaf()) {
            return;
        }
        
        fullEvolutionsScrollView = null;
        if (root.hasSeveralPaths()) {
            LinearLayout individualEvolutionLayout;
            
            params = new LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
            
            fullEvolutionsScrollView = new HorizontalScrollView(this);
            fullEvolutionsScrollView.setLayoutParams(params);
            layout.addView(fullEvolutionsScrollView);
            
            LinearLayout multipleEvolutionsLayout = new LinearLayout(this);
            multipleEvolutionsLayout.setOrientation(LinearLayout.HORIZONTAL);
            multipleEvolutionsLayout.setLayoutParams(params);
            fullEvolutionsScrollView.addView(multipleEvolutionsLayout);
            
            for (String path : root.evolutions.keySet()) {
                individualEvolutionLayout = new LinearLayout(this);
                individualEvolutionLayout.setOrientation(LinearLayout.VERTICAL);
                params.setMargins((int)(EVOLUTION_MARGIN*dpToPx + 0.5f),
                                  (int)(EVOLUTION_MARGIN*dpToPx + 0.5f),
                                  (int)(EVOLUTION_MARGIN*dpToPx + 0.5f),
                                  0);
                individualEvolutionLayout.setLayoutParams(params);
                
                multipleEvolutionsLayout.addView(individualEvolutionLayout);
                addPathText(path, individualEvolutionLayout);
                addEvolutions(root.evolutions.get(path), individualEvolutionLayout);
            }
            
        } else {
            String path = (String)root.evolutions.keySet().toArray()[0];
            addPathText(path, layout);
            addEvolutions(root.evolutions.get(path), layout);
        }
    }
    
    private void addPathText(String path, LinearLayout layout) {
        TextView text = new TextView(this);
        try {
            Integer.parseInt(path);
            path = String.format(getResources().getString(R.string.evo_level), path); 
        } catch (NumberFormatException e) {
            try {
                path = getResources().getString(R.string.class.getField(path).getInt(null));
            } catch (NotFoundException e1) {
                e1.printStackTrace();
                path = getResources().getString(R.string.evo_error);
            } catch (IllegalArgumentException e1) {
                e1.printStackTrace();
                path = getResources().getString(R.string.evo_error);
            } catch (IllegalAccessException e1) {
                e1.printStackTrace();
                path = getResources().getString(R.string.evo_error);
            } catch (NoSuchFieldException e1) {
                e1.printStackTrace();
                path = getResources().getString(R.string.evo_error);
            }
        }
        
        text.setText(path);
        LayoutParams params = new LayoutParams((int)(FULL_EVOLUTION_PIC_WIDTH*dpToPx + 0.5f), LayoutParams.WRAP_CONTENT);
        text.setLayoutParams(params);
        text.setTextSize(TypedValue.COMPLEX_UNIT_SP, FULL_EVOLUTION_PATH_SIZE);
        text.setEllipsize(null);
        text.setHorizontallyScrolling(false);
        text.setGravity(Gravity.CENTER_HORIZONTAL);
        layout.addView(text);
    }
    
    private String evChunk(int carac, int resource, boolean addComma) {
        String result = "";
        if (carac > 0) {
            if (addComma) {
                result += ", ";
            }
            result += carac + " " + getResources().getString(resource);
        }
        return result;
    }
}

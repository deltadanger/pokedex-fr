package fr.free.pokedex;

import android.os.Bundle;
import android.view.ViewGroup;
import android.widget.RelativeLayout;
import android.widget.RelativeLayout.LayoutParams;
import android.widget.ScrollView;

import com.google.android.gms.ads.AdRequest;
import com.google.android.gms.ads.AdSize;
import com.google.android.gms.ads.AdView;

public class PokemonPage extends fr.pokedex.PokemonPage {
	
	private AdView adView;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		
	    adView = new AdView(this);
	    adView.setAdUnitId("ca-app-pub-3293663299631285/7902019453");
	    adView.setAdSize(AdSize.BANNER);

	    ScrollView scroll = (ScrollView)findViewById(fr.pokedex.R.id.main_scroll);
        LayoutParams params = new LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT);
        params.bottomMargin = 150;
	    scroll.setLayoutParams(params);
	    
	    params = new LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.WRAP_CONTENT);
	    params.addRule(RelativeLayout.ALIGN_PARENT_BOTTOM);
	    ViewGroup layout = (ViewGroup)findViewById(fr.pokedex.R.id.main_layout);
	    layout.addView(adView, params);
	    AdRequest adRequest = new AdRequest.Builder().build();
	    adView.loadAd(adRequest);
	}
	
    @Override
    public void onPause() {
	    adView.pause();
	    super.onPause();
    }

    @Override
    public void onResume() {
	    super.onResume();
	    adView.resume();
    }

    @Override
    public void onDestroy() {
	    adView.destroy();
	    super.onDestroy();
    }
}

package fr.free.pokedex;

import com.google.android.gms.ads.AdRequest;
import com.google.android.gms.ads.AdSize;
import com.google.android.gms.ads.AdView;

import android.os.Bundle;
import android.widget.LinearLayout;

public class MainActivity extends fr.pokedex.MainActivity {
	
	private AdView adView;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		
	    adView = new AdView(this);
	    adView.setAdUnitId("ca-app-pub-3293663299631285/7902019453");
	    adView.setAdSize(AdSize.BANNER);

	    LinearLayout layout = (LinearLayout)findViewById(fr.pokedex.R.id.main_layout);
	    layout.addView(adView);
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

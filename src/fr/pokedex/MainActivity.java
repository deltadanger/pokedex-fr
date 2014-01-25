package fr.pokedex;

import android.app.Activity;
import android.app.SearchManager;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.widget.SearchView;
import android.widget.TextView;

public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        // Get the SearchView and set the searchable configuration
        SearchManager searchManager = (SearchManager) getSystemService(Context.SEARCH_SERVICE);
        SearchView searchView = (SearchView) findViewById(R.id.search_text);
        
        // Assumes current activity is the searchable activity
        searchView.setSearchableInfo(searchManager.getSearchableInfo(getComponentName()));
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
        TextView name = (TextView)findViewById(R.id.name);
        name.setText(query);
    }
}
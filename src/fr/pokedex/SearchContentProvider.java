package fr.pokedex;

import java.text.Normalizer;
import java.util.Arrays;
import java.util.Locale;
import java.util.regex.Pattern;

import android.app.SearchManager;
import android.content.ContentProvider;
import android.content.ContentValues;
import android.database.Cursor;
import android.database.MatrixCursor;
import android.net.Uri;

public class SearchContentProvider extends ContentProvider {

    @Override
    public Cursor query(Uri uri, String[] arg1, String arg2, String[] arg3,
            String arg4) {
        Integer id = 1;
        MatrixCursor c = new MatrixCursor(new String[]{"_ID", SearchManager.SUGGEST_COLUMN_TEXT_1, SearchManager.SUGGEST_COLUMN_INTENT_DATA});
        
        String query = standardize(uri.getLastPathSegment());
        if ("".equals(query)) {
            return c;
        }
        
        Object[] names = PokemonList.perName.keySet().toArray();
        Arrays.sort(names);
        
        for (Object obj : names) {
            String name = obj.toString();
            if (standardize(name).contains(query)) {
                c.addRow(new String[]{(id++).toString(), name, name});
            }
        }
        return c;
    }
    
    private String standardize(Object s) {
        String result = s.toString();
        result = result.toLowerCase(Locale.FRANCE);
        // Remove accented characters
        result = Normalizer.normalize(result, Normalizer.Form.NFD); 
        Pattern pattern = Pattern.compile("\\p{InCombiningDiacriticalMarks}+");
        return pattern.matcher(result).replaceAll("");
    }

    @Override
    public int delete(Uri arg0, String arg1, String[] arg2) {
        return 0;
    }

    @Override
    public String getType(Uri arg0) {
        return null;
    }

    @Override
    public Uri insert(Uri arg0, ContentValues arg1) {
        return null;
    }

    @Override
    public boolean onCreate() {
        return false;
    }

    @Override
    public int update(Uri arg0, ContentValues arg1, String arg2, String[] arg3) {
        return 0;
    }
}

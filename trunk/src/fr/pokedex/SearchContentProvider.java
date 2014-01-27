package fr.pokedex;

import java.util.Arrays;

import android.app.SearchManager;
import android.content.ContentProvider;
import android.content.ContentValues;
import android.database.Cursor;
import android.database.MatrixCursor;
import android.net.Uri;
import android.provider.BaseColumns;
import fr.pokedex.utils.Utils;

public class SearchContentProvider extends ContentProvider {

    @Override
    public Cursor query(Uri uri, String[] arg1, String arg2, String[] arg3,
            String arg4) {
        Integer id = 1;
        MatrixCursor c = new MatrixCursor(new String[]{BaseColumns._ID, SearchManager.SUGGEST_COLUMN_TEXT_1, SearchManager.SUGGEST_COLUMN_ICON_1, SearchManager.SUGGEST_COLUMN_INTENT_DATA});
        
        String query = Utils.standardize(uri.getLastPathSegment());
        if ("".equals(query)) {
            return c;
        }
        
        Object[] names = PokemonList.perName.keySet().toArray();
        Arrays.sort(names);
        
        for (Object obj : names) {
            String name = obj.toString();
            String stdName = Utils.standardize(name);
            String number = ""+PokemonList.perName.get(name).number;
            if (stdName.contains(query)) {
                c.addRow(new Object[]{id++, "#" + number + " " + name, "content://" + getContext().getString(R.string.assets_authority) + "/image/"+Utils.standardize(name, true)+".png", name});
            }
            if (number.contains(query)) {
            	c.addRow(new Object[]{id++, "#" + number + " " + name, "content://" + getContext().getString(R.string.assets_authority) + "/image/"+Utils.standardize(name, true)+".png", name});
            }
        }
        return c;
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

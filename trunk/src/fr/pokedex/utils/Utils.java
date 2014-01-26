package fr.pokedex.utils;

import java.text.Normalizer;
import java.util.Locale;
import java.util.regex.Pattern;

import android.util.Log;

public class Utils {

    public static String standardize(Object s, boolean removeBrackets) {
        String result = s.toString();
        // Remove accented characters
        result = Normalizer.normalize(result, Normalizer.Form.NFD); 
        Pattern pattern = Pattern.compile("\\p{InCombiningDiacriticalMarks}+");
        result = pattern.matcher(result).replaceAll("");
        result = result.toLowerCase(Locale.FRANCE);
        
        Log.d("test", result);
        if (removeBrackets && result.indexOf(" (") > -1) {
            result = result.substring(0, result.indexOf(" ("));
        }
        
        return result;
    }
    
    public static String standardize(Object s) {
        return standardize(s, false);
    }
}

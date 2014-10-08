package fr.pokedex;

import android.app.Activity;
import android.content.Context;
import android.graphics.drawable.Drawable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

public class LanguageAdapter extends ArrayAdapter<String>{
    
    public static final int LAYOUT_RESOURCE_ID = R.layout.lang_list_item;
    public static final int FLAG_IMAGE_SIZE = 50;

    Context context;
    String data[] = null;
    
    public LanguageAdapter(Context context, String[] data) {
        super(context, LAYOUT_RESOURCE_ID, data);
        this.context = context;
        this.data = data;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        View row = convertView;
        LanguageHolder holder = null;
        
        if(row == null) {
            LayoutInflater inflater = ((Activity)context).getLayoutInflater();
            row = inflater.inflate(LAYOUT_RESOURCE_ID, parent, false);
            
            holder = new LanguageHolder();
            holder.languageName = (TextView)row.findViewById(R.id.languageName);
            
            row.setTag(holder);
        } else {
            holder = (LanguageHolder)row.getTag();
        }
        
        String[] lang = data[position].split(";");
        try {
            Drawable img = context.getResources().getDrawable(R.drawable.class.getField(lang[0]).getInt(null));
            int size = (int)(FLAG_IMAGE_SIZE * context.getResources().getDisplayMetrics().density + 0.5f);
            img.setBounds(0, 0, size, size);
            holder.languageName.setCompoundDrawables(img, null, null, null);
        } catch (IllegalArgumentException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (NoSuchFieldException e) {
            e.printStackTrace();
        }
        holder.languageName.setText(lang[1]);
        
        return row;
    }
    
    static class LanguageHolder {
        TextView languageName;
    }
}


package fr.pokedex.utils;

import android.view.View;
import android.view.animation.AccelerateDecelerateInterpolator;
import android.view.animation.Animation;
import android.view.animation.Transformation;
import android.widget.LinearLayout.LayoutParams;

public class ExpandAnimation extends Animation {
    
    public static enum Direction{
        EXPAND,COLLAPSE;
    }
    
    private View v;
    private int originalHeight;
    private boolean expand;
    
    public ExpandAnimation(View v) {
        this.v = v;
        this.originalHeight = v.getHeight();
        setInterpolator(new AccelerateDecelerateInterpolator());
    }
    
    @Override
    protected void applyTransformation(float interpolatedTime, Transformation t) {
        super.applyTransformation(interpolatedTime, t);
        
        int newHeight;
        if (expand) {
            newHeight = (int)(originalHeight*interpolatedTime);
        } else {
            newHeight = originalHeight - (int)(originalHeight*interpolatedTime);
        }
        LayoutParams params = new LayoutParams(v.getLayoutParams().width, newHeight);
        v.setLayoutParams(params);
        v.requestLayout();
    }
    
    public void setDirection(Direction d) {
        expand = Direction.EXPAND.equals(d);
    }
}

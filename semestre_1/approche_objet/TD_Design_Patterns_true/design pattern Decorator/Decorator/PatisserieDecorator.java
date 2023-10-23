package Decorator;

import java.util.ArrayList;
import java.util.List;

import Component.Patisserie;

public abstract class PatisserieDecorator implements Patisserie {
    private Patisserie gateauDecorated;

    public PatisserieDecorator(Patisserie gateauDecorated) {
        this.gateauDecorated = gateauDecorated;
    }

    @Override
    public String getName() {
        return gateauDecorated.getName();
    }

    public int getPrice(){
        return gateauDecorated.getPrice();
    }

    public static boolean IsGoodGateau(String StringGateau, String gateau) {
        return StringGateau.contains(gateau);
    }
}
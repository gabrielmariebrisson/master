package Composite;

import java.util.ArrayList;
import java.util.List;

import Component.Patisserie;

public abstract class CompositeGateau implements Patisserie {
    protected List<Patisserie> gateaux = new ArrayList<>();
    public CompositeGateau() {
    }
    public
    void addFils(Patisserie gateau){
        gateaux.add(gateau);
    }
    public
    void removeFils(Patisserie gateau){
        gateaux.remove(gateau);
    }

    @Override
    public  int getPrice() {
        int price = 0;
        for (Patisserie gateau : gateaux) {
            price=price+gateau.getPrice();
        }
        return price;
    }
}
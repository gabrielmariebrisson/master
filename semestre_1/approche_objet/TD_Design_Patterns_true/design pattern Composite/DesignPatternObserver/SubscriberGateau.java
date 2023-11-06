package DesignPatternObserver;

import Composite.CompositeGateau;
import java.util.Map;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class SubscriberGateau implements Subscriber {
    private List<CompositeGateau> listName = new ArrayList<>();
    private CompositeGateau name;

    public SubscriberGateau(CompositeGateau name) {
        this.name=name;
    }

    @Override
    public void update(int seuil) {
        listName.remove(name);
        while(listName.size() < seuil) {
            System.out.println("Le stock de " + name.getName() + " est faible. Commande de nouveaux gâteaux !");
            listName.add(name);
        }
    }
}
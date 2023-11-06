package Composite;

import Leaf.Fruits;
import Leaf.Pate;


import Component.Patisserie;

public class Tarte extends CompositeGateau {
    public Tarte(String name) {
        super();
        addFils(new Pate());
        addFils(new Fruits(name));
    }

    @Override
    public String getName() {
        StringBuilder nameBuilder = new StringBuilder();
        nameBuilder.append("Tarte");
        for (Patisserie gateau : gateaux) {
            nameBuilder.append(gateau.getName());
        }
        return nameBuilder.toString();
    }
}
package Composite;

import Component.Patisserie;
import Leaf.Pate;

public class Chou extends CompositeGateau {
    public Chou() {
        super();
        addFils(new Pate());
    }

    @Override
    public String getName() {
        StringBuilder nameBuilder = new StringBuilder();
        nameBuilder.append("Chou");
        for (Patisserie gateau : gateaux) {
            nameBuilder.append(gateau.getName());
        }
        return nameBuilder.toString();
    }
}
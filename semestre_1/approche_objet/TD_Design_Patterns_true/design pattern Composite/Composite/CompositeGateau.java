package Composite;

import Component.Gateau;

public class CompositeGateau implements Gateau {
    private List<Gateau> gateaux = new ArrayList<>();
    
    @Override
    void addFils(Gateau gateau){
        gateaux.add(gateau);
    }
    @Override
    void removeFils(Gateau gateau){
        gateaux.remove(gateau);
    }
    @Override
    public void print();
}
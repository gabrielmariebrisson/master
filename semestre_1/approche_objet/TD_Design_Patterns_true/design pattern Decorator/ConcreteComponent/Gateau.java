package ConcreteComponent;

import Component.Patisserie;

public abstract class Gateau implements Patisserie{

    private String name;
    private int price;

    public Gateau(String name, int price){
        this.name=name;
        this.price=price;
    }

    @Override
    public  String getName() {
        return name;
    }

    @Override
    public  int getPrice() {
        return price;
    }
    
}

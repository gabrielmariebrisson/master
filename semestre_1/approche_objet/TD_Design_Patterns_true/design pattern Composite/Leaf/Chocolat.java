package Leaf;
import Component.Patisserie;


public class Chocolat implements Patisserie {
    @Override
    public  String getName() {
        return " au chocolat";
    }

    @Override
    public  int getPrice() {
        return 1;
    }
}
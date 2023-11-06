package Leaf;
import Component.Patisserie;


public class Chantilly implements Patisserie {
    @Override
    public  String getName() {
        return " avec de la chantilly";
    }

    @Override
    public  int getPrice() {
        return 1;
    }

}
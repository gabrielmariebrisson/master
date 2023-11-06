package Leaf;
import Component.Patisserie;


public class Meringue implements Patisserie {
    @Override
    public  String getName() {
        return " avec Meringue";
    }

    @Override
    public  int getPrice() {
        return 1;
    }
}
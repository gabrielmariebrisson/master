package Leaf;
import Component.Patisserie;


public class Noisettes implements Patisserie {
    @Override
    public  String getName() {
        return " avec noisettes";
    }

    @Override
    public  int getPrice() {
        return 1;
    }
}
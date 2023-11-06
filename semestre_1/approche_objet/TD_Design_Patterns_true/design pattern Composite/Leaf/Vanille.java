package Leaf;
import Component.Patisserie;


public class Vanille implements Patisserie {
    @Override
    public  String getName() {
        return " à la crème vanille";
    }

    @Override
    public  int getPrice() {
        return 1;
    }
}
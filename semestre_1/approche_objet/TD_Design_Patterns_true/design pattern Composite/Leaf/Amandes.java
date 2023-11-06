package Leaf;

import Component.Patisserie;

public class Amandes implements Patisserie {
    @Override
    public  String getName() {
        return " avec amandes grillées ";
    }

    @Override
    public  int getPrice() {
        return 1;
    }

}
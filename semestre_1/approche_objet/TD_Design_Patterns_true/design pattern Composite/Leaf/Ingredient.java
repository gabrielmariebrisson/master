package Leaf;
import Component.Patisserie;

class Ingredient implements Gateau {
    @Override
    public void print() {
        System.out.println("Action de la feuille : " + nom);
    }
}
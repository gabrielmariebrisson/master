package Leaf;
import Component.Patisserie;


public class Fruits implements Patisserie {
    private String name;

    public Fruits(String name){
        this.name=" aux "+name;
    }
    @Override
    public  String getName() {
        return name;
    }

    @Override
    public  int getPrice() {
        return 1;
    }
}
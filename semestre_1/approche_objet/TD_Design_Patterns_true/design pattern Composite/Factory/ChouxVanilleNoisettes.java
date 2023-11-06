package Factory;

import Component.Patisserie;
import Composite.Chou;
import Leaf.Noisettes;
import Leaf.Vanille;

public class ChouxVanilleNoisettes implements PatisserieFactory {
    @Override
    public Patisserie createPatisserie() {
        Chou chou= new Chou();
        chou.addFils(new Vanille());
        chou.addFils(new Noisettes());
        return chou;
    }
}
package Factory;

import Component.Patisserie;
import Composite.Tarte;
import Leaf.Noisettes;

public class TartePommesNoisettes implements PatisserieFactory {
    @Override
    public Patisserie createPatisserie() {
        Tarte tarte= new Tarte("Pommes");
        tarte.addFils(new Noisettes());
        return tarte;
    }
}
package Factory;

import Component.Patisserie;
import Composite.Tarte;
import Leaf.Amandes;
import Leaf.Meringue;

public class TartesAbricotsMeringueAmandes implements PatisserieFactory {
    @Override
    public Patisserie createPatisserie() {
        Tarte tarte= new Tarte("Abricots");
        tarte.addFils(new Meringue());
        tarte.addFils(new Amandes());
        return tarte;
    }
}
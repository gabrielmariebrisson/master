package Factory;

import Component.Patisserie;
import Composite.Tarte;
import Leaf.Meringue;

public class TartesFraisesMeringue implements PatisserieFactory {
    @Override
    public Patisserie createPatisserie() {
        Tarte tarte= new Tarte("Fraises");
        tarte.addFils(new Meringue());
        return tarte;
    }
}
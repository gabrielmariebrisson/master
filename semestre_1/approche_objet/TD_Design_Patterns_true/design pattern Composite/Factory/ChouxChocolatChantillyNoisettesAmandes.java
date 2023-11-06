package Factory;

import Component.Patisserie;
import Composite.Chou;
import Leaf.Amandes;
import Leaf.Chantilly;
import Leaf.Chocolat;
import Leaf.Noisettes;

public class ChouxChocolatChantillyNoisettesAmandes implements PatisserieFactory {
    @Override
    public Patisserie createPatisserie() {
        Chou chou= new Chou();
        chou.addFils(new Chocolat());
        chou.addFils(new Chantilly());
        chou.addFils(new Noisettes());
        chou.addFils(new Amandes());
        return chou;
    }
}

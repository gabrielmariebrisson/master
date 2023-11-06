package Builder;

import Composite.*;
import Leaf.*;

public class ChouxCremeVanilleChantillyNoisettesBuilder extends GateauBuilder {
    @Override
    public void createNewGateau() {
        gateau = new Chou();
    }

    @Override
    public void buildName() {
        gateau.addFils(new Vanille());
        gateau.addFils(new Chantilly());
        gateau.addFils(new Noisettes());
    }
}
package Builder;

import Composite.*;
import Leaf.*;


public class ChouxChocolatNoisettes extends GateauBuilder {
    @Override
    public void createNewGateau() {
        gateau = new Chou();
    }

    @Override
    public void buildName() {
        gateau.addFils(new Chocolat());
        gateau.addFils(new Noisettes());
    }
}
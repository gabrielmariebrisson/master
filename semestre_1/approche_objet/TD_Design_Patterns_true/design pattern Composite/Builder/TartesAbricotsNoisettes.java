package Builder;

import Component.Patisserie;
import Composite.*;
import Leaf.*;

public class TartesAbricotsNoisettes extends GateauBuilder {
    @Override
    public void createNewGateau() {
        gateau = new Tarte("Abricots");
    }

    @Override
    public void buildName() {
        gateau.addFils(new Noisettes());
    }

}
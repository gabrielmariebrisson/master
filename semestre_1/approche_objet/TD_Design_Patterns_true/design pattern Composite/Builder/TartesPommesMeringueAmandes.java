package Builder;

import Component.Patisserie;
import Composite.*;
import Leaf.*;

public class TartesPommesMeringueAmandes extends GateauBuilder {
    @Override
    public void createNewGateau() {
        gateau = new Tarte("Pommes");
    }

    @Override
    public void buildName() {
        gateau.addFils(new Meringue());
        gateau.addFils(new Noisettes());
    }

}
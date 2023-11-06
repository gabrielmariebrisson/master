package Builder;

import Composite.CompositeGateau;

public abstract class GateauBuilder {
    protected CompositeGateau gateau;

    public CompositeGateau getGateau() {
        return gateau;
    }

    public void createNewGateau() {
        gateau = null;
    }

    public abstract void buildName();
}
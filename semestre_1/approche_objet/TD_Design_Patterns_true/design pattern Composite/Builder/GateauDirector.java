package Builder;

import Component.Patisserie;

public class GateauDirector {
    private GateauBuilder builder;

    public void setBuilder(GateauBuilder builder) {
        this.builder = builder;
    }

    public Patisserie getGateau() {
        return builder.getGateau();
    }

    public void constructGateau() {
        builder.createNewGateau();
        builder.buildName();
    }
}
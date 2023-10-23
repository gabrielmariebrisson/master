package gateaux;


public class Tarte extends Gateaux {
    public Tarte(String description) {
        this.description = description;
    }

    public String getDescription() {
        return description;
    }

    public double cout() {
        return 5.0;
    }
}
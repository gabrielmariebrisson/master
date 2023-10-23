package gateaux;
public class Choux extends Gateaux {
    public Choux(String description) {
        this.description = description;
    }

    public String getDescription() {
        return description;
    }

    public double cout() {
        return 5.0;
    }
}
package ingredients;

import gateaux.Choux;

public class Amandes implements Ingredients {
    private Ingredients baseIngredient;

    public Amandes(Ingredients baseIngredient) {
        this.baseIngredient = baseIngredient;
    }

    public String getDescription() {
        return baseIngredient.getDescription() + " avec Amandes";
    }

    public double cout() {
        return baseIngredient.cout() + 1.0; // Coût supplémentaire pour les Amandes
    }
}

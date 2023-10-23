package ingredients;

import gateaux.Choux;

public class Pommes implements Ingredients {
    private Ingredients baseIngredient;

    public Pommes(Ingredients baseIngredient) {
        if (!(baseIngredient instanceof Choux)) {
            throw new IllegalArgumentException("La Pommes n'est autorisées que pour le choux.");
        }
        this.baseIngredient = baseIngredient;
    }

    public String getDescription() {
        return baseIngredient.getDescription() + " avec Pommes";
    }

    public double cout() {
        return baseIngredient.cout() + 1.0; // Coût supplémentaire pour les Pommes
    }
}

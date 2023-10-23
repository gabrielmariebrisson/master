package ingredients;

import gateaux.Gateaux;
import gateaux.Tarte;

public class Vanille implements Ingredients {
    private Ingredients baseIngredient;

    public Vanille(Ingredients baseIngredient) {
        if (!(baseIngredient instanceof Tarte)) {
            throw new IllegalArgumentException("La Vanille n'est autorisées que pour la tarte.");
        }
        this.baseIngredient = baseIngredient;
    }

    public String getDescription() {
        return baseIngredient.getDescription() + " avec Vanille";
    }

    public double cout() {
        return baseIngredient.cout() + 1.0; // Coût supplémentaire pour les Vanille
    }
}
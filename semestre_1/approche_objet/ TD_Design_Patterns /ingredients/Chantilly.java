package ingredients;

import gateaux.Choux;
import gateaux.Tarte;

public class Chantilly implements Ingredients {
    private Ingredients baseIngredient;

    public Chantilly(Ingredients baseIngredient) {
        if (!(baseIngredient instanceof Choux)) {
            throw new IllegalArgumentException("La chantilly n'est autorisées que pour le Choux.");
        }
        this.baseIngredient = baseIngredient;
    }

    public String getDescription() {
        return baseIngredient.getDescription() + " avec Chantilly";
    }

    public double cout() {
        return baseIngredient.cout() + 1.0; // Coût supplémentaire pour les Chantilly
    }
}
package ingredients;

import gateaux.Choux;
import gateaux.Tarte;

public class Abricots implements Ingredients {
    private Ingredients baseIngredient;

    public Abricots(Ingredients baseIngredient) {
        if (!(baseIngredient instanceof Tarte)) {
            throw new IllegalArgumentException("L'abricots n'est autorisées que pour la tarte.");
        }
        this.baseIngredient = baseIngredient;
    }

    public String getDescription() {
        return baseIngredient.getDescription() + " avec Abricots";
    }

    public double cout() {
        return baseIngredient.cout() + 1.0; // Coût supplémentaire pour les Abricots
    }
}

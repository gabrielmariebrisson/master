package ingredients;

import gateaux.Choux;
import gateaux.Tarte;

public class Meringue implements Ingredients {
    private Ingredients baseIngredient;

    public Meringue(Ingredients baseIngredient) {
        if (!(baseIngredient instanceof Tarte)) {
            throw new IllegalArgumentException("La Meringue n'est autorisées que pour le tarte.");
        }
        this.baseIngredient = baseIngredient;
    }

    public String getDescription() {
        return baseIngredient.getDescription() + " avec Meringue";
    }

    public double cout() {
        return baseIngredient.cout() + 1.0; // Coût supplémentaire pour les Meringue
    }
}
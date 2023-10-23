package ingredients;


import gateaux.Tarte;

public class Chocolat implements Ingredients {
    private Ingredients baseIngredient;

    public Chocolat(Ingredients baseIngredient) {
        if (!(baseIngredient instanceof Tarte)) {
            throw new IllegalArgumentException("Le chocolat n'est autorisées que pour la tarte.");
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
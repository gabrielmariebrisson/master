package ingredients;

public class Noisettes implements Ingredients {
    private Ingredients baseIngredient;

    public Noisettes(Ingredients baseIngredient) {
        this.baseIngredient = baseIngredient;
    }

    public String getDescription() {
        return baseIngredient.getDescription() + " avec noisettes";
    }

    public double cout() {
        return baseIngredient.cout() + 1.0; // Coût supplémentaire pour les noisettes
    }
}
package ConcreteDecorator;
import Component.Patisserie;
import ConcreteComponent.Choux;
import Decorator.PatisserieDecorator;

public class Vanille extends PatisserieDecorator {

    public Vanille(Patisserie decoratedGateau) {
        super(decoratedGateau);
        if (!IsGoodGateau(this.getName(),"Choux")){
            throw new IllegalArgumentException("Lz Vanille ne sont autorisés que pour les Choux.");
        }
    }

    @Override
    public String getName() {
        return super.getName() + " à la crème vanille";
    }

    @Override
    public int getPrice() {
        return super.getPrice() + 1; // Coût supplémentaire pour les Vanille
    }
}
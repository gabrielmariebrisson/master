package ConcreteDecorator;
import Component.Patisserie;
import ConcreteComponent.Tarte;
import Decorator.PatisserieDecorator;

public class Abricots extends PatisserieDecorator {
    public Abricots(Patisserie decoratedGateau) {
        super(decoratedGateau);
        if (IsGoodGateau(this.getName(),"Tarte")){
            throw new IllegalArgumentException("Les Abricots ne sont autorisés que pour les tartes.");
        }
    }

    @Override
    public String getName() {
        return super.getName() + " aux abricots";
    }

    @Override
    public int getPrice() {
        return super.getPrice() + 1; // Coût supplémentaire pour les Vanille
    }
}
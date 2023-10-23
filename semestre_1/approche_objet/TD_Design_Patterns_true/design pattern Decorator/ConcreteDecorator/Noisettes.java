package ConcreteDecorator;
import Component.Patisserie;
import ConcreteComponent.Choux;
import ConcreteComponent.Tarte;
import ConcreteDecorator.*;
import Decorator.PatisserieDecorator;

public class Noisettes extends PatisserieDecorator {

    public Noisettes(Patisserie decoratedGateau) {
        super(decoratedGateau);
    }

    @Override
    public String getName() {
return super.getName() + " avec noisettes";
    }

    @Override
    public int getPrice() {
        return super.getPrice() + 1; // Coût supplémentaire pour les Vanille
    }
}
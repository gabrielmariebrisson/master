package ConcreteDecorator;
import java.util.List;

import Component.Patisserie;
import ConcreteComponent.Choux;
import ConcreteComponent.Tarte;
import ConcreteDecorator.*;
import Decorator.PatisserieDecorator;

public class Amandes extends PatisserieDecorator {

    public Amandes(Patisserie decoratedGateau) {
        super(decoratedGateau);
    }

    @Override
    public String getName() {
        return super.getName() + " avec amandes grillées";
    }

    @Override
    public int getPrice() {
        return super.getPrice() + 1; 
    }
}
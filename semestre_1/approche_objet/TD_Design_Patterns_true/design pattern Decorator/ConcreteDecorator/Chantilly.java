package ConcreteDecorator;
import java.util.List;

import Component.Patisserie;
import ConcreteComponent.Choux;
import Decorator.PatisserieDecorator;

public class Chantilly extends PatisserieDecorator {

    public Chantilly(Patisserie decoratedGateau) {
        super(decoratedGateau);
        if (IsGoodGateau(this.getName(),"Choux")){
            throw new IllegalArgumentException("La chnatilly ne sont autorisés que pour les Choux.");
        }
    }

    @Override
    public String getName() {
return super.getName() + " avec chantilly";
    }

    @Override
    public int getPrice() {
        return super.getPrice() + 1; // Coût supplémentaire pour les Vanille
    }

}
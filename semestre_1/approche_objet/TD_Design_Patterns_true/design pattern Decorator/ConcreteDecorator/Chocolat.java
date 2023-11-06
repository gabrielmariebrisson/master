package ConcreteDecorator;
import Component.Patisserie;
import ConcreteComponent.Choux;
import ConcreteDecorator.*;
import Decorator.PatisserieDecorator;

public class Chocolat extends PatisserieDecorator {
    public Chocolat(Patisserie decoratedGateau) {
        super(decoratedGateau);
        if (IsGoodGateau(this.getName(),"Choux")){
            throw new IllegalArgumentException("Le chocolat ne sont autorisés que pour les Choux.");
        }
    }

    @Override
    public String getName() {
return super.getName() + " au  chocolat";
    }

    @Override
    public int getPrice() {
        return super.getPrice() + 1; 
    }
}
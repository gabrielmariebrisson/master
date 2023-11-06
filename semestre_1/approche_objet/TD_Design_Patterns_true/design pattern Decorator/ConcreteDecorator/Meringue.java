package ConcreteDecorator;
import Component.Patisserie;
import ConcreteComponent.Choux;
import ConcreteComponent.Tarte;
import ConcreteDecorator.*;
import Decorator.PatisserieDecorator;

public class Meringue extends PatisserieDecorator {

    public Meringue(Patisserie decoratedGateau) {
        super(decoratedGateau);
        if (IsGoodGateau(this.getName(),"Tarte")){
            throw new IllegalArgumentException("Les Meringue ne sont autorisées que pour les tartes.");
        }
    }

    @Override
    public String getName() {
        return super.getName() + " avec meringue";
    }

    @Override
    public int getPrice() {
        return super.getPrice() + 1; 
    }
}
package ConcreteDecorator;
import Component.Patisserie;
import ConcreteComponent.Choux;
import ConcreteComponent.Tarte;
import Decorator.PatisserieDecorator;

public class Pommes extends PatisserieDecorator {

    public Pommes(Patisserie decoratedGateau) {
        super(decoratedGateau);
        if (!IsGoodGateau(this.getName(),"Tarte")){
            throw new IllegalArgumentException("Les Pommes ne sont autorisées que pour les tartes.");
        }
    }

    @Override
    public String getName() {
    return super.getName() + " aux pommes";
    }

    @Override
    public int getPrice() {
        return super.getPrice() + 1; 
    }
}
package Builder;
import Composite.*;
import Leaf.*;

public class ChouxVanilleChantillyAmandes extends GateauBuilder {
    @Override
    public void createNewGateau() {
        gateau = new Chou();
    }

    @Override
    public void buildName() {
        gateau.addFils(new Vanille());
        gateau.addFils(new Chantilly());
        gateau.addFils(new Amandes());
    }
}
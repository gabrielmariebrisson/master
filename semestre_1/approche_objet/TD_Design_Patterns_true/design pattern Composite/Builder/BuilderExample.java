package Builder;

import java.util.ArrayList;
import java.util.List;

import Composite.Chou;
import Composite.CompositeGateau;
import Composite.Tarte;

public class BuilderExample {
    public static void main(String[] args) {
        GateauDirector factory = new GateauDirector();
        
        List<GateauBuilder> builders = new ArrayList<>();
        builders.add(new ChouxCremeVanilleChantillyNoisettesBuilder());
        builders.add(new ChouxChocolatNoisettes());
        builders.add(new ChouxVanilleChantillyAmandes());
        builders.add(new TartesPommesMeringueAmandes());
        builders.add(new TartesAbricotsNoisettes());

        for (GateauBuilder builder : builders) {
            factory.setBuilder(builder);
            factory.constructGateau();
            CompositeGateau gateau = (CompositeGateau) factory.getGateau();

            System.out.println("Nom du gâteau : " + gateau.getName());
            System.out.println("Prix du gâteau : " + gateau.getPrice());
            System.out.println();
        }
    }
}

package Factory;

import java.util.ArrayList;
import java.util.List;

import Builder.GateauBuilder;
import Composite.CompositeGateau;
import Factory.PatisserieFactory;

public class Application {
    public static void main(String[] args) {
        List<PatisserieFactory> builders = new ArrayList<>();
        builders.add(new ChouxChocolatChantillyNoisettesAmandes());
        builders.add(new ChouxVanilleNoisettes());
        builders.add(new TartePommesNoisettes());
        builders.add(new TartesAbricotsMeringueAmandes());
        builders.add(new TartesFraisesMeringue());

        for (PatisserieFactory builder : builders) {
            CompositeGateau gateau = (CompositeGateau) builder.createPatisserie();

            System.out.println("Nom du gâteau : " + gateau.getName());
            System.out.println("Prix du gâteau : " + gateau.getPrice());
            System.out.println();
        }
    }
}

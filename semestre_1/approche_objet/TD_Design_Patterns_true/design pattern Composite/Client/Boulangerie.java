package Client;

import Leaf.Chantilly;
import Component.Patisserie;


import Composite.Tarte;

//import Composite.Tarte;
public class Boulangerie {public static void main(String[] args) {
    Patisserie chantilly = new Chantilly();

    Tarte tarte = new Tarte("Pommes");

    System.out.println("Nom du gâteau : " + tarte.getName());
    System.out.println("Prix du gâteau : " + tarte.getPrice());

    tarte.addFils(chantilly);

    System.out.println("Nom du gâteau : " + tarte.getName());
    System.out.println("Prix du gâteau : " + tarte.getPrice());
}
}
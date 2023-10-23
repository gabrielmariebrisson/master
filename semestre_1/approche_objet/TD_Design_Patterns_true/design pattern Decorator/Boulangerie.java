import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import Component.*;
import Decorator.*;
import ConcreteDecorator.*;
import ConcreteComponent.*;

public class Boulangerie {
    public static void main(String[] args) {
        // Crée une tarte simple
        Patisserie tarte = new Tarte();
        System.out.println("Tarte simple : " + tarte.getName() + ", Prix : " + tarte.getPrice());

        // Décore la tarte avec des Noisettes
        Patisserie tarteAvecNoisettes = new Noisettes(tarte);
        System.out.println("Tarte avec Noisettes : " + tarteAvecNoisettes.getName() + ", Prix : " + tarteAvecNoisettes.getPrice());

        // Décore la tarte avec des Pommes
        Patisserie tarteAvecPommes = new Pommes(tarte);
        System.out.println("Tarte avec Pommes : " + tarteAvecPommes.getName() + ", Prix : " + tarteAvecPommes.getPrice());

        // Décore la tarte avec de la Vanille
        Patisserie tarteAvecVanille = new Vanille(tarte);
        System.out.println("Tarte avec Vanille : " + tarteAvecVanille.getName() + ", Prix : " + tarteAvecVanille.getPrice());

        // Décore la tarte avec des Noisettes, des Pommes et de la Vanille
        Patisserie tarteDecoree = new Noisettes(new Pommes(new Vanille(tarte)));
        System.out.println("Tarte décorée : " + tarteDecoree.getName() + ", Prix : " + tarteDecoree.getPrice());
    }
}
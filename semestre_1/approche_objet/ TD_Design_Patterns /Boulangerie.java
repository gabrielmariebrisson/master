import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import gateaux.*;
import ingredients.*;

public class Boulangerie {
    private List<String> TypesIngredient = Arrays.asList(
        "Tarte aux pommes",
        "Tarte aux abricots",
        "Choux à la crème vanille",
        "Choux aux chocolat",
        "avec chantilly",
        "sans chantilly",
        "avec noisettes",
        "sans noisettes",
        "avec amandes grillées",
        "sans amandes grillées",
        "avec meringue",
        "sans meringue"
    );

     public Ingredients creerTarte(List<String> types) {
        Ingredients tarte= null; ;
        for (String type : types) {
            if (TypesIngredient.contains(type)) {
                tarte= new Tarte(type);
            } else {
                throw new IllegalArgumentException("Type de tarte inconnu : " + type);
            }
        }
        return tarte;
    }

    public Ingredients creerChoux(List<String> types) {
        Ingredients choux= null; ;
        for (String type : types) {
            if (TypesIngredient.contains(type)) {
                choux= new Choux(type);
            } else {
                throw new IllegalArgumentException("Type de choux inconnu : " + type);
            }
        }
        return choux;
    }

    public static void main(String[] args) {
        // Création d'une tarte aux pommes de base
        Ingredients tarteAuxPommes = new Tarte("Tarte aux pommes");

        // Ajout d'ingrédients à la tarte aux pommes
        tarteAuxPommes = new Noisettes(tarteAuxPommes); // Ajout de noisettes
        tarteAuxPommes = new Meringue(tarteAuxPommes); // Ajout de Meringue

        // Affichage de la description et du coût de la tarte aux pommes avec les ingrédients
        System.out.println("Description de la tarte aux pommes : " + tarteAuxPommes.getDescription());
        System.out.println("Coût de la tarte aux pommes : " + tarteAuxPommes.cout());
    }

}
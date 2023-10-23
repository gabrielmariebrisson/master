import gateaux.Gateaux;

public class Patissier {
    public void preparerGateau(Gateaux gateau) {
        System.out.println("Préparation de " + gateau.getDescription());
        System.out.println("Coût : " + gateau.cout() + " euros");
    }
}
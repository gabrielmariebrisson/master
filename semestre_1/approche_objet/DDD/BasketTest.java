package DDD;

public class BasketTest {

    public static void main(String[] args) {
        Reference reference1 = new Reference("123", "Produit A", "Description A", 50);
        Reference reference2 = new Reference("456", "Produit B", "Description B", 30);
        Basket basket = new Basket();

        basket.addReference(reference1, 2);
        basket.addReference(reference2, 1);

        basket.validateBasket();

        basket.addReference(reference1, 2);
        basket.addReference(reference2, 1);

        basket.removeReference(reference1, 1);
        basket.removeReference(reference1, 1);

        basket.addReference(reference1, 3);

        System.out.println("Basket operations completed.");
    }
}

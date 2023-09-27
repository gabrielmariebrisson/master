import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Iterator;
import java.util.Scanner;

public class MyAppliNew {
    static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println("Bienvenue dans le programme de gestion du stock :");
        System.out.println("Pour créer un stock, tapez 'ajouter stock'");
        System.out.println("Pour afficher un stock, tapez 'afficher stock'");
        System.out.println("Pour ajouter un produit, tapez 'ajouter produit'");
        System.out.println("Pour afficher ou modifier la quantité d'un produit, tapez 'afficher produit' ou 'modifier quantité produit'");
        System.out.println("Pour quitter le programme, tapez 'quit'\n");

        Scanner scanner = new Scanner(System.in);
        MyShop shop = new MyShop();

        String input;
        do {
            System.out.print("Entrez une commande : ");
            input = scanner.nextLine();

            try {
                switch (input) {
                    case "ajouter stock":
                        createStock(shop);
                        break;
                    case "afficher stock":
                        showStock(shop);
                        break;
                    case "ajouter produit":
                        addProduct(shop);
                        break;
                    case "afficher produit":
                        showProduct(shop);
                        break;
                    case "modifier quantité produit":
                        modifyProductQuantity(shop);
                        break;
                    case "quit":
                        System.out.println("Au revoir !");
                        break;
                    default:
                        System.out.println("Commande non reconnue. Veuillez réessayer.");
                }
            } catch (Exception e) {
                System.out.println("Erreur : " + e.getMessage());
            }
        } while (!input.equals("quit"));
    }

    public static void createStock( MyShop shop) {
        System.out.print("Créer un stock, entrez son nom : ");
        String name = scanner.nextLine();
        System.out.print("Entrez l'adresse du stock : ");
        String address = scanner.nextLine();
        shop.setStock(new Stock(name, address));
        System.out.println("Stock créé avec succès !");
    }

    public static void showStock(MyShop shop) {
        if (shop.isEmpty()) {
            System.out.println("Aucun stock disponible.");
            return;
        }
        System.out.print("Entrez le nom du stock : ");
        String stockName = scanner.nextLine();
        Stock stock = shop.getStock(stockName);
        System.out.println("Nom du stock : " + stock.getName());
        System.out.println("Adresse du stock : " + stock.getAddress());
    }

    public static void addProduct(MyShop shop) {
        if (shop.isEmpty()) {
            System.out.println("Aucun stock disponible. Créez un stock d'abord.");
            return;
        }
        System.out.print("Entrez le nom du stock : ");
        String stockName = scanner.nextLine();
        Stock stock = shop.getStock(stockName);
        if (stock == null) {
            System.out.println("Stock introuvable.");
            return;
        }

        System.out.print("Entrez le nom du produit : ");
        String name = scanner.nextLine();
        System.out.print("Entrez la quantité : ");
        int quantity = scanner.nextInt();
        scanner.nextLine();
        
        if (quantity < 0) {
            System.out.println("La quantité ne peut pas être négative.");
            return;
        }

        if (stock.nameExist(name)) {
            System.out.println("Le produit existe déjà dans ce stock.");
            return;
        }

        System.out.print("Entrez le type de produit (food/sanitary) : ");
        String productType = scanner.nextLine();

        if (productType.equals("food")) {
            System.out.print("Entrez la date d'expiration (format : YYYY-MM-DD) : ");
            String expirationDate = scanner.nextLine();
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
            LocalDate localDate = LocalDate.parse(expirationDate, formatter);
            Food foodProduct = new Food(name, 1, localDate);
            stock.setProducts(foodProduct);
            System.out.println("Produit alimentaire ajouté avec succès !");
        } else if (productType.equals("sanitary")) {
            SanitaryProduct sanitaryProduct = new SanitaryProduct(name, 1);
            stock.setProducts(sanitaryProduct);
            System.out.println("Produit sanitaire ajouté avec succès !");
        } else {
            System.out.println("Type de produit non reconnu.");
        }
    }

    public static void showProduct(MyShop shop) {
        if (shop.isEmpty()) {
            System.out.println("Aucun stock disponible. Créez un stock d'abord.");
            return;
        }
        System.out.print("Entrez le nom du stock : ");
        String stockName = scanner.nextLine();
        Stock stock = shop.getStock(stockName);
        if (stock == null) {
            System.out.println("Stock introuvable.");
            return;
        }

        System.out.print("Entrez le nom du produit : ");
        String productName = scanner.nextLine();
        Product product = stock.getProduct(productName);

        if (product == null) {
            System.out.println("Produit introuvable dans ce stock.");
        } else {
            System.out.println("Nom du produit : " + product.getName());
            System.out.println("Type du produit : " + product.getType());
            System.out.println("Quantité du produit : " + product.getQuantity());
        }
    }

    public static void modifyProductQuantity( MyShop shop) {
        if (shop.isEmpty()) {
            System.out.println("Aucun stock disponible. Créez un stock d'abord.");
            return;
        }
        System.out.print("Entrez le nom du stock : ");
        String stockName = scanner.nextLine();
        Stock stock = shop.getStock(stockName);
        if (stock == null) {
            System.out.println("Stock introuvable.");
            return;
        }

        System.out.print("Entrez le nom du produit : ");
        String productName = scanner.nextLine();
        Product product = stock.getProduct(productName);

        if (product == null) {
            System.out.println("Produit introuvable dans ce stock.");
            return;
        }

        System.out.print("Entrez la nouvelle quantité : ");
        int newQuantity = scanner.nextInt();
        scanner.nextLine();

        if (newQuantity < 0) {
            System.out.println("La quantité ne peut pas être négative.");
            return;
        }
        Product newProduct= new Product(product.getName(),product.getQuantity()+newQuantity,product.getType());
        stock.removeProduct(product);
        stock.setProducts(newProduct);
        System.out.println("Quantité du produit modifiée avec succès !");
    }
}
import java.util.Iterator;
import java.util.Scanner;


/// tu dois modifier quelque chose : tu peux ajouter un meme stock qui a le meme nom et la meme adresse
public class MyAppli {
    public static void main(String[] args) {
        // Message d'introduction expliquant les règles
        System.out.println("Bienvenue dans le programme de gestion du stock :");
        System.out.println("Pour creer un stock, tapez 'ajouter stock'");
        System.out.println("Pour afficher un stock, tapez 'afficher stock'");
        System.out.println("Pour ajouter un produit, tapez 'ajouter produit'");
        System.out.println("Pour afficher ou modifier la quantité d'un produit, tapez 'afficher produit' ou 'modifier quantité produit'");
        System.out.println("Pour quitter le programme, tapez 'quit'\n");

        System.out.print("Entrez une commande : ");
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        MyShop shop = new MyShop();

        while (!input.equals("quit")) {
            try {
                if (input.equals("ajouter stock")){
                    createStock(scanner,shop);
                }
                if (input.equals("afficher stock")){
                    showStock(scanner,shop);
                }
                if (input.equals("ajouter produit") || (input.equals("afficher produit") || input.equals("modifier quantité produit"))){
                    System.out.println ("Entrez le nom du stock: ");
                    String nameStock = scanner.nextLine();
                    Stock stock=shop.getStock(nameStock);
                    if (input.equals("ajouter produit")){ 
                        System.out.print("entrez le nom du produit: ");
                        String nameProduct = scanner.nextLine();

                        System.out.print("entrez le type du produit: ");
                        String typeProduct = scanner.nextLine();
                        
                        while (!nameProduct.equals("stop")) {
                            addProduct(scanner, stock, nameProduct,typeProduct);
                            System.out.print("Ajouter un nouveau produit ou tapez 'stop' pour arrêter : ");
                            nameProduct = scanner.next();
                        }
                    //afficher ou modifier
                    }else if ((input.equals("afficher produit") || input.equals("modifier quantité produit")) && !shop.isEmpty()) {
                        System.out.print("Entrez le nom du produit : ");
                        String name = scanner.nextLine();
                        Product product = stock.getProduct(name);
                        
                        //afficher
                        if (input.equals("afficher produit")) {
                            showProduct(product);
                        // Modifier
                        } else if (input.equals("modifier quantité produit")) {
                            System.out.print("Entrez la nouvelle quantité : ");
                            int newQuantity = scanner.nextInt();
                            modifyQuantity(stock,product, newQuantity);
                        }
                    }
                }
                else if (shop.isEmpty()) {
                    System.out.println("Stock inexistant, 'ajouter stock'");
                }
            }catch (Exception e) {
                    if (e.getMessage().contains("getName()")) {
                        System.out.println("Erreur : Le produit est introuvable.");
                    } 
                    if (e.getMessage().contains("getName()")) {
                        System.out.println("Erreur : Le produit est introuvable.");
                    }else {
                        System.out.println("Erreur : " + e.getMessage());
                    }
                
            }
        input = scanner.nextLine();
        }        
    }

    public static void createStock(Scanner scanner, MyShop shop){
        System.out.print("Créer un stock, entré son nom: ");
        String name = scanner.nextLine();
        System.out.print("entré l'adresse du stock: ");
        String adress = scanner.nextLine();
        shop.setStock(new Stock(name, adress));
    }

    public static void showStock(Scanner scanner, MyShop shop){
        Iterator<Stock> iterator = shop.getListStock().iterator();
        while(iterator.hasNext()){
            Stock nextStock=iterator.next();
            System.out.println("Nom du stock : " + nextStock.getName());
            System.out.println("Identité du produit : " + nextStock.getAddress());
        }
    } 

    public static void addProduct(Scanner scanner, Stock stock,String name, tring typeProduct){
        if(stock==null){
            System.out.println ("Impossible le stock n'existe pas ");
            return ;
        }
        if (Stock.nameExist(name)){
            System.out.println ("Impossible le produit existe déjà, il doit etre rajouté ");
            return ;
        }
        System.out.print("entré la quantité: ");
        int quantity = scanner.nextInt();
        stock.setProducts( new Product(name, quantity) );
    }

    public static void showProduct(Product object){
        System.out.println("Nom du produit : " + object.getName());
        System.out.println("Identité du produit : " + object.getIdentifier());
        System.out.println("Quantité du produit : " + object.getQuantity());
    }

    public static Stock modifyQuantity(Stock stock,Product oldProduct,int value){
        Product newProduct=null;
        if (oldProduct.getQuantity()+value>=0){
            newProduct=new Product(oldProduct.getName(),oldProduct.getQuantity()+value);
        }else{
            newProduct=new Product(oldProduct.getName(),0);
            System.out.println("La quantité ne peut pas etre négative");
            System.out.println("Elle sera mise a 0");
        }
        stock.removeProduct(oldProduct);
        stock.setProducts(newProduct);
        return stock;
    
    }
}
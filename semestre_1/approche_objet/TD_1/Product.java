public class Product{
    private String name;
    private int quantity;
    private static int lastIdentifier = 0;
    private int identifier;
    private String type;

    Product(String name, int quantity, String type){
        this.name =name;
        this.quantity =quantity;
        identifier = ++lastIdentifier;
        this.type = type;
    }

    public String getName() {
        return name;
    }

    public int getQuantity() {
        return quantity;
    }

    public int getIdentifier() {
        return identifier;
    }
    public String getType() {
        return type;
    }
}
class Product{
    private String name;
    private int quantity;
    private static int lastIdentifier = 0;
    private int identifier;

    Product(String name, int quantity){
        this.name =name;
        this.quantity =quantity;
        identifier = ++lastIdentifier;
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
}
package DDD;

class LineItem {
    private Reference reference;
    int quantity;

    public LineItem(Reference reference, int quantity) {
        this.reference = reference;
        this.quantity = quantity;
    }

    public int calculateTotal() {
        return reference.getPrix() * quantity;
    }

    public Reference getReference() {
        return reference;
    }

    public int getQuantity() {
        return quantity;
    }
}
package DDD;

import java.util.ArrayList;
import java.util.List;

class Basket {
    private List<LineItem> lineItems;
    private boolean isValidated;

    public Basket() {
        lineItems = new ArrayList<>();
        isValidated = false;
    }

    public void addReference(Reference reference, int quantity) {
        if (!isValidated) {
            // Check if the reference is not already in the basket
            for (LineItem item : lineItems) {
                if (item.getReference().getId().equals(reference.getId())) {
                    item.quantity += quantity;
                    return;
                }
            }

            LineItem lineItem = new LineItem(reference, quantity);
            lineItems.add(lineItem);
        } else {
            // Handle the case where the basket is already validated
        }
    }

    public void removeReference(Reference reference, int quantity) {
        if (!isValidated) {
            for (LineItem item : lineItems) {
                if (item.getReference().getId().equals(reference.getId())) {
                    if (item.getQuantity() > quantity) {
                        item.quantity -= quantity;
                    } else {
                        lineItems.remove(item);
                    }
                    return;
                }
            }
        } else {
            // Handle the case where the basket is already validated
        }
    }

    public int calculateTotalAmount() {
        int totalAmount = 0;
        for (LineItem item : lineItems) {
            totalAmount += item.calculateTotal();
        }
        return totalAmount;
    }

    public void validateBasket() {
        isValidated = true;
    }
}
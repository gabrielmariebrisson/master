import java.util.*;

public class Stock {
    private String name;
    private String address;
    private static List<Product> products = new ArrayList<Product>();

    public Stock(String name, String address) {
        this.name = name;
        this.address = address;
    }

    public String getName() {
        return name;
    }

    public String getAddress() {
        return address;
    }

    public void removeProduct(Product product) {
        products.remove(product);
    }

    public Product getProduct(String name) {
        Iterator<Product> iterator = products.iterator();
        while(iterator.hasNext()){
            Product nextProduct=iterator.next();
            if (name.equals(nextProduct.getName())){
                return nextProduct;
            }
        }return null;
    }

    public void setProducts( Product product) {
        products.add(product);
    }

    public boolean nameExist(String name) {
        Iterator<Product> iterator = products.iterator();
        while(iterator.hasNext()){
            if (name.equals(iterator.next().getName())){
                return true;
            }
        }
        return false;
    }

}
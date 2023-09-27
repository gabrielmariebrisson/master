import java.util.*;

public class MyShop {
    private static List<Stock> stocks = new Vector<Stock>();

    MyShop(){
    }
    public void removeStock(Stock stock) {
        stocks.remove(stock);
    }

    public void setStock(Stock stock) {
        stocks.add(stock);
    }

    public boolean isEmpty() {
        Iterator<Stock> iterator = stocks.iterator();
        return !iterator.hasNext();
    }

    public Stock getStock(String name) {
        Iterator<Stock> iterator = stocks.iterator();
        while(iterator.hasNext()){
            Stock nextStock=iterator.next();
            if (name.equals(nextStock.getName())){
                return nextStock;
            }
        }
        return null;
        }

    /*public List<Stock> getListStock() {
        return stocks;
    }*/

    public static boolean hasStock(String name) {
        Iterator<Stock> iterator = stocks.iterator();
        while(iterator.hasNext()){
            if (name.equals(iterator.next().getName())){
                return true;
            }
        }
        return false;
        }   
}
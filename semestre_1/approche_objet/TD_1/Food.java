import java.time.LocalDate;

public class Food extends Product{

    private LocalDate expirationDate;


    Food(String name, int quantity, LocalDate expirationDate){
        super(name, quantity,"Food");
        this.expirationDate=expirationDate;
    }

    boolean isConsumed(){
        return !LocalDate.now().isAfter(expirationDate.minusDays(3));
    }

}

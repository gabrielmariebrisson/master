package DDD;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

class Reference {
    private UUID id;
    private String ref;
    private String nom;
    private String description;
    private int prix;

    public Reference(String ref, String nom, String description, int prix) {
        this.id = UUID.randomUUID();
        this.ref = ref;
        this.nom = nom;
        this.description = description;
        this.prix = prix;
    }

    // Getter methods for properties

    public UUID getId() {
        return id;
    }

    public int getPrix() {
        return 0;
    }
}
package DesignPatternObserver;

import java.util.ArrayList;
import java.util.List;
import java.util.ArrayList;
import java.util.List;

public class Vendeur {
    private List<Subscriber> Subscribers = new ArrayList<>();
    private int seuil;

    public Vendeur(int seuil) {
        this.seuil = seuil;
    }

    public void addSubscriber(Subscriber Subscriber) {
        Subscribers.add(Subscriber);
        Subscriber.update(seuil);
    }

    public void removeSubscriber(Subscriber Subscriber) {
        Subscribers.remove(Subscriber);
    }

    public void consumeGateau(Subscriber subscriber) {
        System.out.println("consume a gateau. ");
        notifySubscriber(subscriber);
    }

    public void notifySubscriber(Subscriber subscriber) {
        subscriber.update(seuil);
    }
}

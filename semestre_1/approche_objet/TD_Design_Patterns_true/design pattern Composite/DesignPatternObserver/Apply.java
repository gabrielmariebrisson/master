package DesignPatternObserver;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import Composite.CompositeGateau;
import Factory.*;

public class Apply {
    public static void main(String[] args) {
        Vendeur vendeur = new Vendeur(10);

        PatisserieFactory builder =new ChouxChocolatChantillyNoisettesAmandes();
        CompositeGateau gateau = (CompositeGateau) builder.createPatisserie();
        SubscriberGateau subscriberGateau1 = new SubscriberGateau(gateau);

        builder =new ChouxVanilleNoisettes();
        gateau = (CompositeGateau) builder.createPatisserie();
        SubscriberGateau subscriberGateau2 = new SubscriberGateau(gateau);

        builder =new TartePommesNoisettes();
        gateau = (CompositeGateau) builder.createPatisserie();
        SubscriberGateau subscriberGateau3 = new SubscriberGateau(gateau);

        builder =new TartesAbricotsMeringueAmandes();
        gateau = (CompositeGateau) builder.createPatisserie();
        SubscriberGateau subscriberGateau4 = new SubscriberGateau(gateau);

        builder =new TartesFraisesMeringue();
        gateau = (CompositeGateau) builder.createPatisserie();
        SubscriberGateau subscriberGateau5 = new SubscriberGateau(gateau);


        vendeur.addSubscriber(subscriberGateau1);
        vendeur.addSubscriber(subscriberGateau2);
        vendeur.addSubscriber(subscriberGateau3);
        vendeur.addSubscriber(subscriberGateau4);
        vendeur.addSubscriber(subscriberGateau5);

        Random random = new Random();

        for (int i = 0; i < random.nextInt(30); i++) {
            int randomSubscriberIndex = random.nextInt(5); // Générer un index de subscriber aléatoire (0 à 4)
            SubscriberGateau randomSubscriber = null;

            switch (randomSubscriberIndex) {
                case 0:
                    randomSubscriber = subscriberGateau1;
                    break;
                case 1:
                    randomSubscriber = subscriberGateau2;
                    break;
                case 2:
                    randomSubscriber = subscriberGateau3;
                    break;
                case 3:
                    randomSubscriber = subscriberGateau4;
                    break;
                case 4:
                    randomSubscriber = subscriberGateau5;
                    break;
            }

            vendeur.consumeGateau(randomSubscriber);
        }
    }
}

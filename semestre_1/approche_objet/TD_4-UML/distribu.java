package distributeursDeBoissons ;

import gestionDesPieces.* ;
import gestionDesChoix.Choix ;
import distributeurs.Distributeur ;
import visualisation.Ecran ;
import gestionDesGobelets.Gobelets ;
import gestionDesBoissons.Boissons ;
import gestionMachinesEtatsFinis.* ;
import compteurs.Compteur ;
import utilitaires.* ;
import gestionDistributeurs.Gestionnaire ;

public class DistributeurDeBoissons implements Distributeur {

	private Pieces pieces  ;	// conteneur des pieces
	private Ecran ecran  ;		// ecran de visualisation
	private Gobelets gobelets ;	// conteneurs des gobelets
	private Boissons boissons ;	// stockage des boissons
	private Gestionnaire gestionnaire ;  
	private MachineEtatsFinis automate ; 


  private Evenement  choixSelectionneEvenement =
      new Evenement ("choix selectionne") ;
  private Evenement pieceIntroduiteEvenement =
      new Evenement ("piece introduite") ;
  private Evenement sommeInsuffisanteEvenement =
      new Evenement ("somme insuffisante") ;
    private Evenement annulationEvenement =
      new Evenement ("annulation") ;
    private Evenement finDistributionEvenement =
      new Evenement ("fin de distribution") ;
    private Evenement plusDeVerreEvenement =
      new Evenement ("plus de verre") ;
    private Evenement plusDeProduitEvenement =
      new Evenement ( "plus de produit") ;

    MachineEtatsFinis initialiserAutomate () {

	Ensemble etats = new Ensemble () ;
	Ensemble actions = new Ensemble () ;
	Ensemble transitions = new Ensemble () ;
	Ensemble evenements = new Ensemble () ;

	MachineEtatsFinis machineEtatsFinis =
	    new MachineEtatsFinis (etats,evenements, actions,
				   transitions,
				   "machinedistributrice de boissons",
				   "" ) ;

	//  Definition des etats
	machineEtatsFinis.ajouterEtatInitial ("en attente") ;
	machineEtatsFinis.ajouterEtatFinal ( "final" ) ;
	machineEtatsFinis.ajouterEtatSimple ("en cours de paiement") ;
	machineEtatsFinis.ajouterEtatSimple ("choix effectue") ;
	machineEtatsFinis.ajouterEtatSimple ("en attente de selection") ;

	// Definition des evenements
	machineEtatsFinis.ajouterEvenement ("choix selectionne") ;
	machineEtatsFinis.ajouterEvenement ("piece introduite") ;
	machineEtatsFinis.ajouterEvenement ("somme insuffisante") ;
	machineEtatsFinis.ajouterEvenement ("annulation") ;
	machineEtatsFinis.ajouterEvenement ("fin de distribution") ;
	machineEtatsFinis.ajouterEvenement ("plus de verre") ;
	machineEtatsFinis.ajouterEvenement ( "plus de produit") ;

	// Action non utilisee
	machineEtatsFinis.ajouterAction ( "action" ) ;
			
	// Definition des transitions
	machineEtatsFinis.ajouterTransition
	    ( "en attente",
	      "en cours de paiement",
	      "piece introduite", "action",
	      "t1","" ) ;
	machineEtatsFinis.ajouterTransition
	    ( "en cours de paiement",
	      "en cours de paiement", "piece introduite",
	      "action", "t2", "" ) ;
	machineEtatsFinis.ajouterTransition
	    ( "en cours de paiement",
	      "choix effectue", "choix selectionne",
	      "action", "t3", "" ) ;
	machineEtatsFinis.ajouterTransition
	    ( "choix effectue",
	      "en cours de paiement",
	      "somme insuffisante", "action",
	      "t4", "" ) ;
	machineEtatsFinis.ajouterTransition
	    ( "choix effectue",
	      "en attente de selection",
	      "plus de produit", "action",
	      "t5", "" ) ;
	machineEtatsFinis.ajouterTransition
	    ( "en attente de selection",
	      "choix effectue", "choix selectionne",
	      "action", "t6", "" ) ;
	machineEtatsFinis.ajouterTransition
	    ( "choix effectue", "final",
	      "plus de verre", "action",
	      "t7", "" ) ;
	machineEtatsFinis.ajouterTransition
	    ( "choix effectue", "en attente",
	      "fin de distribution", "action",
	      "t8", "" ) ;
	machineEtatsFinis.ajouterTransition
	    ( "en attente de selection",
	      "en attente", "annulation",
	      "action", "t9", "" ) ;
	machineEtatsFinis.ajouterTransition
	    ( "en cours de paiement",
	      "en attente", "annulation",
	      "action", "t10", "" ) ;

	return machineEtatsFinis ;
    } ; /* initialiserAutomate */

    public DistributeurDeBoissons () {

	automate = initialiserAutomate () ;
	// nombre de pieces de 50 cts., 1, 2, 5 et 10 F
	pieces = new Pieces (50,20,20,10,0) ;  
	ecran = new Ecran () ;
	// initialisation du nombre de gobelets
	gobelets = new Gobelets (20) ; 
	// nom de la boisson , suivi du nombre de doses
	boissons = new Boissons ("Orange", 10,"Citron",10,
				 "Cafe sucre",10,"Cafe non sucre",
				 10,"The sucre",10, "The non sucre", 10);	
	gestionnaire = new Gestionnaire () ;

    } ; /* constructeur */

    public void introduirePiece (Piece unePiece ) {

	if ( automate. envoyer (pieceIntroduiteEvenement)) {
	    gestionnaire.pieceIntroduite (unePiece) ;
	    pieces.stocker (unePiece) ;
	    if ( ! pieces.monnaieDisponible()) {
		ecran.afficher
		    ("-- Faire l'appoint, svp. ") ;
	    } ;
	} ;
    }; /* introduirePiece */

    public void selectionnerChoix (Choix unChoix) {

	boolean flag ;
	if (automate.envoyer (choixSelectionneEvenement)) {
	    if ( gestionnaire.sommeSuffisante (unChoix)) {
		try {
		    gobelets.placer () ;
		} catch (PlusDeVerreException plusDeVerre) {
		    ecran.afficher
			( "-- Desole : il n'y a plus de verre.") ;
		    // l'automate va se placer sur l'etat final, 
		    // plus aucune commande ne sera prise en compte
		    flag = automate.envoyer ( plusDeVerreEvenement) ; 
		    pieces.rendreMonnaie(gestionnaire.sommeIntroduite());
		    // arrêt brutal de la machine !!!
		    System.exit (0) ; 
		} 
		try { // il reste des verres la boisson peut être 
		    // alors servie
		    boissons.preparer (unChoix) ;
		    boissons.verser () ; 
		    pieces.rendreMonnaie
			(gestionnaire.sommeARendre (unChoix)) ;
		    // evenement interne pour permettre a l'automate 
		    //d'être prêt pour un autre client
		    flag = automate.envoyer (finDistributionEvenement) ;
		    gestionnaire.stop() ;
		    ecran.afficher ("-- Merci, et au revoir.") ;	
		} catch (PlusDeProduitException plusDeProduitException)
		    {
			ecran.afficher
			    ("-- plus de ce produit : 
                                 faites un autre choix svp.") ;
			flag = automate.envoyer (plusDeProduitEvenement) ;
		    } 	   
	    } else {
		flag = automate.envoyer (sommeInsuffisanteEvenement) ;
		ecran.afficher ("-- Somme insuffisante pour ce choix.") ;
		ecran.afficher ("-- Somme restante a payer : " +
				gestionnaire.sommeManquante (unChoix)) ;
	    }  /* Fin else */
	} /* Fin if */
    } ; /* selectionnerChoix */

    public void annuler () {
	if ( automate.envoyer (annulationEvenement)) {
	    pieces.rendreMonnaie (gestionnaire.sommeIntroduite ()) ;
	    gestionnaire.stop() ;
	    ecran.afficher ("-- Merci, et au revoir.") ;	
	} ;
    } ; /* annuler */

} ; /* DistributeurDeBoissons */

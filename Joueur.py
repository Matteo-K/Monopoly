class Joueur:
    
    def __init__(self):
        """
        initialise le joueur

        attribut
        --------
        self.rue_posséder : l'ensemble des rues que possède le joueur
        self.argent : argent que possède le joueur
        self.position : position du joueur actuelle

        """
        self.rue_posséder = []
        self.carte_posséder = []
        self.nbr_hotel = 0
        self.nbr_manoir = 0
        self.argent = 1500
        self.position = 0
        
    def gagne_argent(self,ponnaie):
        """
        ajoute de l'argent au joueur

        Parameters
        ----------
        ponnaie : int
            argent rajouté au joueur.
        """
        self.argent += ponnaie
    
    def perdre_argent(self,ponnaie):
        """
        retire de l'argent au joueur

        Parameters
        ----------
        ponnaie : int
            l'argent perdu du joueur.
        """
        self.argent -= ponnaie
        
    def verif_argent (self):
        """
        vérifie si le joueur n'est pas en négatif

        Returns
        -------
        bool
            retourne True si le joueur est en négatif.

        """
        return self.argent <= 0
    
    def affiche_argent (self) :
        print(f"Vous avez actuellement {self.argent} M")
    
#ajouter plusieurs fonctions:
    #acheter une rue
    #hypothèque
    #ajouté des hôtel
    #vérifie le nombre d'hôtel
    #ajoute un manoir (supprime les hôtels)
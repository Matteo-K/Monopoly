from random import randint

class File :
    
    def __init__(self,file = []) :
        self.file = file
    
    def affiche (self) :
        return self.file
    
    def longueur (self) :
        return len(self.file)
    
    def est_vide (self):
        return len(self.file) == 0
    
    def enfiler (self, valeur):
        self.file.append(valeur)
        
    def défiler (self):
        assert not self.est_vide()
        return self.file.pop(0)
    
class Cartes :
    
    def __init__(self) :
        
        self.cartes_chances = ["Rendez-vous à la rue de la Paix",
                               "Avancer jusqu’à la case départ",
                               "Rendez-vous à l’Avenue Henri-Martin. Si vous passez par la case départ, recevez 200M",
                               "Avancez au Boulevard de La Villette. Si vous passez par la case départ, recevez 200M",
                               "Vous êtes imposé pour les réparations de voirie à raison de 40M par hôtel et 120M par manoir.",
                               "Avancez jusqu’à la Gare de Lyon. Si vous passez par la case départ, recevez 200M",
                               "Vous avez gagné le prix de mots croisés. Recevez 100M",
                               "La banque vous verse un dividende de 50M",
                               "Vous êtes libéré de prison. Cette carte peut être conservée jusqu’à ce qu’elle soit utilisée",
                               "Reculez de trois cases",
                               "Aller en prison. Rendez-vous directement en prison. Ne franchissez pas par la case départ, ne touchez pas 200M",
                               "Faites des réparations dans toutes vos maisons. Versez pour chaque hôtel 25M. Versez pour chaque manoir 100M",
                               "Amende pour excès de vitesse 15M",
                               "Payez pour frais de scolarité 150M",
                               "Amende pour ivresse 20M",
                               "Votre immeuble et votre prêt rapportent. Vous devez toucher 150M"]
        
        self.cartes_caisse_2_communauté = ["Placez-vous sur la case départ",
                                           "Erreur de la banque en votre faveur. Recevez 200M",
                                           "Payez la note du médecin 50M",
                                           "La vente de votre stock vous rapporte 50M",
                                           "Vous êtes libéré de prison. Cette carte peut être conservée jusqu’à ce qu’elle soit utilisée",
                                           "Aller en prison. Rendez-vous directement à la prison. Ne franchissez pas par la case départ, ne touchez pas 200M",
                                           "Retournez à Belleville. Si vous passez par la case départ, recevez 200M",
                                           "Recevez votre revenu annuel 100M",
                                           "C’est votre anniversaire. Chaque joueur doit vous donner 10M",
                                           "Les contributions vous remboursent la somme de 20M",
                                           "Recevez votre intérêt sur l’emprunt à 7% soit 25M",
                                           "Payez votre Police d’Assurance 50M",
                                           "Payez une amende de 10M ou bien tirez une carte « CHANCE »",
                                           "Rendez-vous à la gare la plus proche. Si vous passez par la case départ, recevez 200M",
                                           "Vous avez gagné le deuxième Prix de Beauté. Recevez 10M",
                                           "Vous héritez de 100M"]
        

    def créer_tas(self):
        """
        Génère aléatoirement un tas deux tas de cartes :
            1 - tas de carte chance : cartes_chances
            2 - tas de carte communauté : cartes_caisse_2_communauté 

        Returns
        -------
        list
            liste du tas de carte chance.
        list
            liste du tas de carte communauté.

        """
        chance = File([])
        communauté = File([])
        while chance.longueur() < len(self.cartes_chances) or communauté.longueur() < len(self.cartes_caisse_2_communauté) :
            x, y = randint(0,len(self.cartes_chances)-1), randint(0,len(self.cartes_caisse_2_communauté)-1)
            if x not in chance.affiche() :
                chance.enfiler(x)
            if y not in communauté.affiche() :
                communauté.enfiler(y)
        return chance.affiche(), communauté.affiche()
                    
    def piocher (self,tas):
        """
        retire la première carte du tas
        
        Parameters
        ----------
        tas : File
            tas de carte à piocher.  
        
        Returns
        -------
        int
            valeur de la carte retirer du tas.

        """
        return tas.défiler()

    
    def remettre (self,tas,Carte):
        """
        remet la carte dans le tas

        Parameters
        ----------
        tas : File
            tas de carte à piocher.
        
        Cartes : int
            valeur de la carte à remettre dans le tas.
        """
        tas.enfiler(Carte)

    def chance_affiche (self,carte) :
        """
        affiche a quoi correspond la valeur de la carte du tas de cartes_chances

        Parameters
        ----------
        carte : int
            valeur de la carte du tas cartes_chances.

        Returns
        -------
        str
            Définition de la carte.

        """
        return self.cartes_chances[carte]
    
    def communauté_affiche (self,carte) :
        """
        affiche a quoi correspond la valeur de la carte du tas de cartes_caisse_2_communauté

        Parameters
        ----------
        carte : int
            valeur de la carte du tas cartes_caisse_2_communauté.

        Returns
        -------
        Str
            Définition de la carte.

        """
        return self.cartes_caisse_2_communauté[carte]

# Initialisation
#C = Cartes()
# liste1 , liste2 = C.créer_tas()
# F_chance, F_communauté = File(liste1), File(liste2)

# Exemple File
# print(F_chance.affiche())
# print(F_chance.longueur())
# print(F_chance.est_vide())
# F_chance.enfiler(F_chance.défiler())

# Exemple Cartes
# x = C.piocher(F_chance)
# print(x)
# C.remettre(F_chance,x)
# print(C.chance_affiche(x))
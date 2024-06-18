from random import randint
import Plateau as plt
import File_cartes as F_C

class dérouler:
    def __init__(self,nbr_joueur,list_joueur : list,nom_joueur : list):
        """
        initialise les paramètres pour jouer
        
        Parameters
        ----------
        nbr_joueur : int
            Le nombre de joueur pour commencer la partie.

        attribut
        -------
        self.prison : liste de toute les personnes en prison représenter par leur indice de la liste "self.list_joueur" et leur temps passer en prison ;
            ex : [[0,2],[3,0]]
        self.Parc_Gratuit : l'argent dans le parc gratuit
        self.plateau : Définition du terrain de jeu
        self.list_joueur : ensemble de la class joueur qui possède tout les prérequis du joueur
        self.nom_joueur : nom du joueur

        """
        assert nbr_joueur != 0
        
        self.prison = []
        self.Parc_Gratuit = 0
        self.plateau = plt.plateau()
        self.list_joueur,self.nom_joueur = list_joueur,nom_joueur
        
        self.C = F_C.Cartes()
        liste1 , liste2 = self.C.créer_tas()
        self.F_chance, self.F_communauté = F_C.File(liste1), F_C.File(liste2)
    
    def lancement_1_dé(self):
        """
        Simule un lancement de dé

        Returns
        -------
        valeur : int
            une valeur entre 1 et 6 compris.

        """
        valeur = randint(1,6)
        return valeur
    
    def lancement_2_dé(self):
        """
        Simule 2 lancée de dé
        affiche si les deux lancée font un double
        
        Returns
        -------
        int
            retourn une valeur entre 2 et 12 inclus.

        """
        x, y = self.lancement_1_dé(), self.lancement_1_dé()
        if self.est_un_double(x,y) :
            print("Vous avez fait un double, vous pouver rejouer")
        return x+y
    
    def est_un_double(self, valeur1, valeur2):
        """
        Vérifie si les deux valeurs représente un double

        Parameters
        ----------
        valeur1 : int
            valeur entre 1 et 6 inclus.
        valeur2 : int
            valeur entre 1 et 6 inclus.

        Returns
        -------
        bool
            retourne True si les 2 valeurs sont les mêmes.

        """
        return valeur1 == valeur2
        
    def avancée_de(self,indice_joueur,valeur):
        """
        Définie la nouvelle case du joueur en sachant qu'il avance d'un nombre (valeur)

        Parameters
        ----------
        indice_joueur : int
            indice représentant le joueur en question.
        valeur : int
            nombre de case que parcour le joueur.

        Returns
        -------
        str
            retourne la nouvelle case du joueur.

        """
        self.list_joueur[indice_joueur].position = (self.list_joueur[indice_joueur].position + valeur) % self.plateau.long_plateau
        #print(f"Vous avancer de {valeur} cases")
        return self.plateau.plateau[self.list_joueur[indice_joueur].position]
    
    def plus_parc_gratuit(self,valeur):
        """
        Ajoute de l'argent dans le parc gratuit

        Parameters
        ----------
        valeur : int
            somme de la valeur à ajouté dans la cagnote.

        """
        self.Parc_Gratuit += valeur
        #print(f"Le parc Gratuit contient désormais {self.Parc_Gratuit} M")
  
    def retirer_parc_gratuit(self,indice_joueur):
        """
        retire l'argent du parc gratuit et l'attribut à un joueur représenter par son indice

        Parameters
        ----------
        indice_joueur : int
            indice du joueur.
        """
        self.list_joueur[indice_joueur].gagne_argent(self.Parc_Gratuit)
        self.Parc_Gratuit = 0

# Case départ

    def vérif_case_départ (self,pos_init,pos_apres):
        while pos_init != pos_apres :
            if pos_init == 0 :
                return True
            pos_init = (pos_init + 1)% self.plateau.long_plateau
        return False
        
    def pass_case_départ(self,indice_joueur):
        self.list_joueur[indice_joueur].gagne_argent(200)
        #print(f"{self.nom_joueur[indice_joueur]} est passé par la case départ, il gagne 200 M")
      
    def voir_case(self,indice_joueur) :
        """
        affiche les 12 cases en faces du joueur
        
        Parameters
        ----------
        indice_joueur : int
            indice représentant le joueur en question.
        """
        print(f"{self.nom_joueur[indice_joueur]}, vous êtes sur la case {self.plateau.plateau[self.list_joueur[indice_joueur].position]}")
        print("")
        for i in range(12):
            autorité = ""
            for j in range (len(self.plateau.rue_achetable)):
                if self.plateau.plateau[self.list_joueur[indice_joueur].position+ i+1] in self.plateau.rue_achetable[j] :
                    print(f"{i+1} cases de {self.plateau.plateau[self.list_joueur[indice_joueur].position + i+1]} ; {self.plateau.rue_achetable[j+1][0]}")
                    autorité = "écrit"
                elif j == len(self.plateau.rue_achetable)-1 and autorité != "écrit" : 
                    print(f"{i+1} cases de {self.plateau.plateau[self.list_joueur[indice_joueur].position + i+1]} ;")
                  
    def voir_plateau(self):
        """
        affiche l'ensemble des cases du tableau avec tout leurs attributs
        (quel case, couleur si besoin, joueur attribuer ou non, nbr_d'hôtel/Manoir)
         et les joueurs en prison
        """
        """
        Il faut voir toute les cases du plateau, qui est sur quel case dont la prison
        mettre les couleurs des rue_achetables
        """
        for i in range(self.plateau.long_plateau):
            autorité = ""
            for j in range (len(self.plateau.rue_achetable)):
                if self.plateau.plateau[i] in self.plateau.rue_achetable[j] :
                    print(f"{i}. {self.plateau.plateau[i]} / {self.plateau.rue_achetable[j+1][0]}")
                    autorité = "écrit"
                elif j == len(self.plateau.rue_achetable)-1 and autorité != "écrit" : 
                    print(f"{i}. {self.plateau.plateau[i]} ")
                    
    def appartient(self,case):
        """
        Vérifie si la case appartient à un joueur

        Parameters
        ----------
        case : str
            case à vérifier l'appartenance.

        Returns
        -------
        print
            affiche à qui appartient la case si elle appartient à quelqu'un.

        """
        for i in range(len(self.plateau.rue_achetable)//2):
            if case in self.plateau.rue_achetable[i*2]:
                for i in range(len(self.list_joueur)):
                    for j in self.list_joueur[i].rue_posséder :
                        if case == j:
                            return i     #f"Vous êtes sur la case {case}, elle appartient à {self.nom_joueur[i]}"
                else: 
                    return print(f"Vous êtes sur la case {case} et elle n'appartient à personne")
        print(f"Vous êtes sur la case {case}")
        
    def nbr_gare (self,indice_joueur):
        nbr = 0
        for i in self.list_joueur[indice_joueur].rue_posséder :
            if i in self.plateau.rue_achetable[16] :
                nbr += 1
        return nbr

#cartes 
    def drl_carte (self,indice_joueur,tas,carte):
        if tas ==  self.F_chance :  # tas de carte chance          
            if carte < 8 :       
                if carte < 4 :              
                    if carte == 0 :    # Rendez-vous à la rue de la Paix 
                        print(self.C.chance_affiche(carte))
                        self.list_joueur[indice_joueur].position = self.plateau.long_plateau - 1
                        self.C.remettre(tas,carte)
                    elif carte == 1 :  # Avancer jusqu’à la case départ
                        print(self.C.chance_affiche(carte))
                        self.list_joueur[indice_joueur].position = 0
                        self.pass_case_départ(indice_joueur)
                        self.C.remettre(tas,carte)
                    elif carte == 2 :  # Rendez-vous à l’Avenue Henri-Martin. Si vous passez par la case départ, recevez 200M
                        print(self.C.chance_affiche(carte))
                        pos = self.list_joueur[indice_joueur].position
                        self.list_joueur[indice_joueur].position = 24
                        if self.vérif_case_départ(pos,self.list_joueur[indice_joueur].position) == True:
                            self.pass_case_départ(indice_joueur)
                        self.C.remettre(tas,carte)
                    elif carte == 3 :  # Avancez au Boulevard de La Villette. Si vous passez par la case départ, recevez 200M
                        print(self.C.chance_affiche(carte))
                        pos = self.list_joueur[indice_joueur].position
                        self.list_joueur[indice_joueur].position = 11
                        if self.vérif_case_départ(pos,self.list_joueur[indice_joueur].position) == True:
                            self.pass_case_départ(indice_joueur)
                        self.C.remettre(tas,carte)
                else :
                    if carte == 4 :    # Vous êtes imposé pour les réparations de voirie à raison de 40M par hôtel et 120M par manoir.
                        print(self.C.chance_affiche(carte))
                        self.list_joueur[indice_joueur].perdre_argent(40*self.list_joueur[indice_joueur].nbr_hotel + 120*self.list_joueur[indice_joueur].nbr_manoir)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
                    elif carte == 5 :  # Avancez jusqu’à la Gare de Lyon. Si vous passez par la case départ, recevez 200M
                        print(self.C.chance_affiche(carte))
                        pos = self.list_joueur[indice_joueur].position
                        self.list_joueur[indice_joueur].position = 15
                        if self.vérif_case_départ(pos,self.list_joueur[indice_joueur].position) == True:
                            self.pass_case_départ(indice_joueur)
                        self.C.remettre(tas,carte)
                    elif carte == 6 :  # Vous avez gagné le prix de mots croisés. Recevez 100M
                        print(self.C.chance_affiche(carte))
                        self.list_joueur[indice_joueur].gagne_argent(100)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
                    elif carte == 7 :  # La banque vous verse un dividende de 50M
                        print(self.C.chance_affiche(carte))
                        self.list_joueur[indice_joueur].gagne_argent(50)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
            else :
                if carte < 12 :
                    if carte == 8 :    # Vous êtes libéré de prison. Cette carte peut être conservée jusqu’à ce qu’elle soit utilisée
                        print(self.C.chance_affiche(carte))
                        self.list_joueur[indice_joueur].carte_posséder.append([tas,carte])
                    elif carte == 9 :  # Reculez de trois cases
                        print(self.C.chance_affiche(carte))
                        self.list_joueur[indice_joueur].position -= 3
                        self.C.remettre(tas,carte)
                    elif carte == 10 : # Aller en prison. Rendez-vous directement en prison. Ne franchissez pas par la case départ, ne touchez pas 200M
                        print(self.C.chance_affiche(carte))
                        self.aller_prison(indice_joueur)
                        self.C.remettre(tas,carte)
                    elif carte == 11 : # Faites des réparations dans toutes vos maisons. Versez pour chaque hôtel 25M. Versez pour chaque manoir 100M
                        print(self.C.chance_affiche(carte))
                        self.list_joueur[indice_joueur].perdre_argent(25*self.list_joueur[indice_joueur].nbr_hotel + 100*self.list_joueur[indice_joueur].nbr_manoir)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
                else :
                    if carte == 12 :   # Amende pour excès de vitesse 15M
                        print(self.C.chance_affiche(carte))
                        self.list_joueur[indice_joueur].perdre_argent(15)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
                    elif carte == 13 : # Payez pour frais de scolarité 150M
                        print(self.C.chance_affiche(carte))
                        self.list_joueur[indice_joueur].perdre_argent(150)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
                    elif carte == 14 : # Amende pour ivresse 20M
                        print(self.C.chance_affiche(carte))
                        self.list_joueur[indice_joueur].perdre_argent(20)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
                    elif carte == 15 : # Votre immeuble et votre prêt rapportent. Vous devez toucher 150M
                        print(self.C.chance_affiche(carte))
                        self.list_joueur[indice_joueur].gagne_argent(150)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
        else : #tas de carte communauté
            if carte < 8 :               
                if carte < 4 :                   
                    if carte == 0 :    # Placez-vous sur la case départ
                        print(self.C.communauté_affiche(carte))
                        self.list_joueur[indice_joueur].position = 0
                        self.C.remettre(tas,carte)
                    elif carte == 1 :  # Erreur de la banque en votre faveur. Recevez 200M
                        print(self.C.communauté_affiche(carte))    
                        self.list_joueur[indice_joueur].gagne_argent(200)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
                    elif carte == 2 :  # Payez la note du médecin 50M
                        print(self.C.communauté_affiche(carte))
                        self.list_joueur[indice_joueur].perdre_argent(50)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
                    elif carte == 3 :  # La vente de votre stock vous rapporte 50M
                        print(self.C.communauté_affiche(carte))
                        self.list_joueur[indice_joueur].gagne_argent(50)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
                else :
                    if carte == 4 :    # Vous êtes libéré de prison. Cette carte peut être conservée jusqu’à ce qu’elle soit utilisée
                        print(self.C.communauté_affiche(carte))
                        self.list_joueur[indice_joueur].carte_posséder.append([tas,carte])
                    elif carte == 5 :  # Aller en prison. Rendez-vous directement à la prison. Ne franchissez pas par la case départ, ne touchez pas 200M
                        print(self.C.communauté_affiche(carte))
                        self.aller_prison(indice_joueur)
                        self.C.remettre(tas,carte)
                    elif carte == 6 :  # Retournez à Belleville. Si vous passez par la case départ, recevez 200M
                        print(self.C.communauté_affiche(carte))
                        pos = self.list_joueur[indice_joueur].position
                        self.list_joueur[indice_joueur].position = 1
                        if self.vérif_case_départ(pos,self.list_joueur[indice_joueur].position) == True:
                            self.pass_case_départ(indice_joueur)
                        self.C.remettre(tas,carte)
                    elif carte == 7 :  # Recevez votre revenu annuel 100M
                        print(self.C.communauté_affiche(carte))
                        self.list_joueur[indice_joueur].gagne_argent(100)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
            else :
                if carte < 12 :
                    if carte == 8 :    # C’est votre anniversaire. Chaque joueur doit vous donner 10M
                        print(self.C.communauté_affiche(carte))
                        self.list_joueur[indice_joueur].gagne_argent((len(self.list_joueur)-1)*10)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
                    elif carte == 9 :  # Les contributions vous remboursent la somme de 20M
                        print(self.C.communauté_affiche(carte))
                        self.list_joueur[indice_joueur].gagne_argent(20)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
                    elif carte == 10 : # Recevez votre intérêt sur l’emprunt à 7% soit 25M
                        print(self.C.communauté_affiche(carte))
                        self.list_joueur[indice_joueur].gagne_argent(25)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
                    elif carte == 11 : # Payez votre Police d’Assurance 50M
                        print(self.C.communauté_affiche(carte))
                        self.list_joueur[indice_joueur].perdre_argent(50)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
                else :
                    if carte == 12 :   # Payez une amende de 10M ou bien tirez une carte « CHANCE »
                        print(self.C.communauté_affiche(carte))
                        pass
                    elif carte == 13 : # Rendez-vous à la gare la plus proche. Si vous passez par la case départ, recevez 200M
                        print(self.C.communauté_affiche(carte))
                        pos, i_gare = self.list_joueur[indice_joueur].position, 0
                        gare = [5-pos,15-pos,25-pos,35-pos]
                        for i in range(len(gare)-1):
                            if 0 <= gare[i] <= 10 :
                                i_gare = i
                        self.list_joueur[indice_joueur].position = gare[i_gare]
                        print(f"La gare la plus proche est la {self.plateau.plateau[gare[i_gare]]}")
                        if self.vérif_case_départ(pos,self.list_joueur[indice_joueur].position) == True:
                            self.pass_case_départ(indice_joueur)
                        self.C.remettre(tas,carte)                       
                    elif carte == 14 : # Vous avez gagné le deuxième Prix de Beauté. Recevez 10M
                        print(self.C.communauté_affiche(carte))
                        self.list_joueur[indice_joueur].gagne_argent(10)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
                    elif carte == 15 : # Vous héritez de 100M
                        print(self.C.communauté_affiche(carte))
                        self.list_joueur[indice_joueur].gagne_argent(100)
                        self.C.remettre(tas,carte)
                        self.list_joueur[indice_joueur].affiche_argent()
   
#prison
    def est_en_prison(self,indice_joueur):
        """
        Vérifie si le joueur est en prison
        
        Parameters
        ----------
        indice_joueur : int
            représente le joueur qui doit être vérifier.

        Returns
        -------
        bool
            return True si le joueur est en prison.
        """
        for i in self.prison:
            if i[0] == indice_joueur:
                return True
        return False
    
    def aller_prison(self,indice_joueur):
        """
        Définis la nouvelle position du joueur : la prison

        Parameters
        ----------
        indice_joueur : int
            représente le joueur qui doit aller en prison.
        """
        self.prison.append([indice_joueur,0])
        self.list_joueur[indice_joueur].position = 10
        
    def verif_tps_prison(self,indice_joueur):
        """
        Vérifie le temps passer en prison du joueur

        Parameters
        ----------
        indice_joueur : int
            indice qui représente le joueur en prison.

        Returns
        -------
        int
            le temps passer en prison.

        """
        assert self.est_en_prison(indice_joueur) 
        for i in self.prison :
            if i[0] == indice_joueur :
                return i[1]
            
    def prisonnier(self):
        """
        Affiche la liste des prisonniers
        """
        liste_prisonnier = []
        for i in self.prison :
            liste_prisonnier += i[0]
        return liste_prisonnier
              
    def plus_tps_prison(self,indice_joueur):
        """
        Ajoute 1 au temps de prison du joueur

        Parameters
        ----------
        indice_joueur : int
            indice du joueur en prison.
        """
        assert self.est_en_prison(indice_joueur) 
        indice = 0
        for i in self.prison :
            if i[0] == indice_joueur:
                self.prison[indice][1] += 1
            else : 
                indice += 1
                
    def tps_sort_prison(self,indice_joueur):
        """
        Vérifie que le joueur doit sortir de prison

        Parameters
        ----------
        indice_joueur : int
            indice qui représente le joueur.

        Returns
        -------
        bool
            si le joueur doit sortir :
                return True
            sinon :
                return False

        """
        return self.verif_tps_prison(indice_joueur) == 3
    
    def sort_prison(self,indice_joueur):
        assert self.est_en_prison(indice_joueur) 
        for i in self.prison:
            if i[0] == indice_joueur:
                self.prison.remove(i)
            
    def tour_prison(self,indice_joueur):
        """
        doit regarder si le joueur possède une carte libérer de prison 
        et demande si il veut l'utiliser sinon il paye si il n'en a pas et veut pas l'utiliser et qu'il a dépasser les 3 lancers
        """
        x, y = self.lancement_1_dé(), self.lancement_1_dé()
        if self.est_un_double(x,y) :
            print("Vous avez fais un double")
            self.sort_prison(indice_joueur)
        else :
            self.plus_tps_prison(indice_joueur)
            if self.verif_tps_prison(indice_joueur) == 3:
                print("vous devez payez 50M")   

                
    #ajouter des fonctions pour la prison :
        #Si il dépasse le temps, il paye
    #une fonction déroulement du jeu

def Crédité ():
    """
    Affiche le créateur du jeu
    """
    print("CRÉER PAR MATTAQUE")

# Exemple   
#D = dérouler(5)
#D.list_joueur[0].rue_posséder = ["rue_achetable de Courcelles","Compagnie Électrique","Avenue Foch"]
#D.list_joueur[1].rue_posséder = ["Avenue des Champs-Élysées", "rue_achetable de la Paix"]
#D.list_joueur[2].rue_posséder = ["Boulevard de la Villette"]
#D.list_joueur[3].rue_posséder = ["Gare de Lyon","Gare du Nord","Gare Saint-Lazare"]
#D.list_joueur[4].rue_posséder = []
#print(D.lancement_2_dé())
#D.appartient(D.avancée_de(1,D.lancement_2_dé()))
#D.list_joueur[0].gagne_argent(5)
#D.plus_parc_gratuit(150)
#D.voir_case(1)
#D.avancée_de(1,D.lancement_2_dé())
#D.voir_plateau()
#print(D.nbr_gare(3))
#print(D.vérif_case_départ(30, 2))
#D.pass_case_départ(1)

# Exemple drl_carte
# for i in range(16):
#     D.drl_carte(1,D.F_chance,i)
# for i in range(16):
#     D.drl_carte(1,D.F_chance,i)
# for i in range(16):
#     D.drl_carte(1,D.F_communauté,i)

# Exemple File
# print(D.F_chance.affiche())
# print(D.F_chance.longueur())
# print(D.F_chance.est_vide())
# D.F_chance.enfiler(D.F_chance.défiler())

# Exemple Carte
# x = D.C.piocher(D.F_chance)
# print(x)
# D.C.remettre(D.F_chance,x)
# print(D.C.chance_affiche(x))

# Exemple Prison
#D.aller_prison(1)
#D.verif_tps_prison(1)
#D.prisonnier()
#D.plus_tps_prison(1)
#D.prison[0][1] = 3
#if D.tps_sort_prison(1):
    #P.sort_prison(1)
    #Ensemble de fonction sur la prison
#input("")

"""
- rajouter dans les fonctions voir, l'appartenance des rue_achetables
ex : 0. Départ
    1. Boulevard de Belleville / Marron (didié) 
    2. Caisse de Communauté
    3. rue_achetable Lecourbe / Marron
    4. Impôts
    5. Gare Montparnasse
    6. rue_achetable de Vaugirard / Cyan (jean louis de la haute) ; Manoire
    7. Carte Chance
    8. rue_achetable de Courcelles / Cyan (Martin) ; 4 hôtels
    9. Avenue de la République / Cyan (Martin) ; Manoire
    10. Simple Visite
    11. Boulevard de la Villette / Magenta
    12. Compagnie Électrique
    
- finir la fontion tour_prison()
- finir la fonction drl_carte pour carte == 12
- modifier self.rue_posséder afin qu'il soit répartit de façon : [[rue,nbr_hotel],[rue,nbr_hotel]]
_modifier appartient()
"""
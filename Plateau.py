class plateau:
    
    def __init__(self):
        """
        initialise le plateau de jeu
        
        attribut
        ---------
        self.rue_achetable[x] : si x = paire : liste rue
                      si x = impaire : couleur rue
        self.plateau : l'ensemble des cases dans l'ordre
        self.long_plateau : nombre de case du plateau
        self.prison : liste des joueurs en prison
        self.cartes_chances : liste des cartes chances
        cartes_caisse_2_communauté : liste des cartes de la caisse de la communauté

        """
        self.rue_achetable = [["Boulevard de Belleville","rue Lecourbe"], ["Marron"], ["rue de Vaugirard", "rue de Courcelles", "Avenue de la République"], ["Cyan"], 
                    ["Boulevard de la Villette", "Avenue de Neuilly", "rue de Paradis"], ["Magenta"], ["Avenue Mozart", "Boulevard Saint-Michel", "Place Pigalle"], ["Orange"],
                    ["Avenue Matignon", "Boulevard Malesherbes", "Avenue Henri-Martin"], ["Rouge"], ["Faubourg Saint-Honoré", "Place de la Bourse", "rue La Fayette"], ["Jaune"],
                    ["Avenue de Breteuil", "Avenue Foch", "Boulevard des Capucines"], ["Vert"], ["Avenue des Champs-Élysées", "rue de la Paix"], ["Bleu"],
                    ["Gare Montparnasse","Gare de Lyon","Gare du Nord","Gare Saint-Lazare"],[""], ["Compagnie Électrique","Compagnie des Eaux"], [""]]
        
        self.impot = ["Impôts","Taxe de Luxe"]
        
        self.carte = ["Caisse de Communauté","Carte Chance","Allez en Prison"]
        
        self.autre = ["Départ","Simple Visite","Parc Gratuit",]
        
        self.plateau = ["Départ", "Boulevard de Belleville", "Caisse de Communauté", "rue Lecourbe", "Impôts", 
                        "Gare Montparnasse", "rue de Vaugirard", "Carte Chance", "rue de Courcelles", "Avenue de la République", 
                        "Simple Visite", "Boulevard de la Villette", "Compagnie Électrique", "Avenue de Neuilly", "rue de Paradis", 
                        "Gare de Lyon", "Avenue Mozart", "Caisse de Communauté", "Boulevard Saint-Michel", "Place Pigalle", 
                        "Parc Gratuit", "Avenue Matignon", "Carte Chance", "Boulevard Malesherbes", "Avenue Henri-Martin", 
                        "Gare du Nord", "Faubourg Saint-Honoré", "Place de la Bourse", "Compagnie des Eaux", "rue La Fayette", 
                        "Allez en Prison", "Avenue de Breteuil", "Avenue Foch", "Caisse de Communauté", "Boulevard des Capucines", 
                        "Gare Saint-Lazare", "Carte Chance", "Avenue des Champs-Élysées", "Taxe de Luxe", "rue de la Paix"]
        
        self.long_plateau = len(self.plateau)
        
        self.rue_prix = {"Boulevard de Belleville" : [60,2,4,10,30,90,160,250,50,30,33],"rue Lecourbe" :[60,4,8,20,60,180,320,450,50,30,33], 
                    "rue de Vaugirard" : [100,6,12,30,90,270,400,550,50,50,55], "rue de Courcelles": [100,6,12,30,90,270,400,550,50,50,55], "Avenue de la République": [120,8,16,40,100,300,450,600,50,60,66], 
                    "Boulevard de la Villette" : [140,10,20,50,150,450,625,750,100,70,77], "Avenue de Neuilly" : [140,10,20,50,150,450,625,750,100,70,77], "rue de Paradis" : [160,12,24,60,180,500,700,900,100,80,88], 
                    "Avenue Mozart" : [180,14,28,70,200,550,750,950,100,90,99], "Boulevard Saint-Michel" : [180,14,28,70,200,550,750,950,100,90,99], "Place Pigalle" : [200,16,32,80,220,600,800,1000,100,100,110],
                    "Avenue Matignon" : [220,18,36,90,250,700,875,1050,150,110,121], "Boulevard Malesherbes" : [220,18,36,90,250,700,875,1050,150,110,121], "Avenue Henri-Martin" : [240,20,40,100,300,750,925,1100,150,120,132], 
                    "Faubourg Saint-Honoré" : [260,22,44,110,330,800,975,1150,150,130,143], "Place de la Bourse" : [260,22,44,110,330,800,975,1150,150,130,143], "rue La Fayette" : [280,24,48,120,360,850,1025,1200,150,140,154],
                    "Avenue de Breteuil" : [300,26,52,130,390,900,1100,1275,200,150,165], "Avenue Foch" : [300,26,52,130,390,900,1100,1275,200,150,165], "Boulevard des Capucines" : [320,28,56,150,450,1000,1200,1400,200,160,176] ,
                    "Avenue des Champs-Élysées" : [350,35,70,175,500,1100,1300,1500,200,175,193], "rue de la Paix" : [400,50,100,200,600,1400,1700,2000,200,200,220],
                    "Gare Montparnasse" : [200,25,50,100,200],"Gare de Lyon" : [200,25,50,100,200],"Gare du Nord" : [200,25,50,100,200],"Gare Saint-Lazare" : [200,25,50,100,200],
                    "Compagnie Électrique" : [150,4,10],"Compagnie des Eaux" : [150,4,10]}
        
#répartir les prix de façon {rue : [prix_rue,loyer,serie,hotel1,hotel2,hotel3,hotel4,manoir,cout_hotel,hypothèque,payer_hypothèque]}
#pour les gares {gare : [prix_gare,1carte,2cartes,3cartes,4cartes]}
#a voir pour les générateur surement {générateur : [si 1carte : 4, si 2cartes : 10]}

# Initialisation
# P = plateau()

# Exemple
#print(P.rue_prix["Avenue Mozart"])
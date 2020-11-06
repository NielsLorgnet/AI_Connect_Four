# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:08:35 2020

@author: Niels
"""

import time

class Node:  # Initialisation d'un objet de la classe noeud
    def __init__(self, plateau,profondeur=0,parent=None,x=None,y=None):
        self.plateau=plateau  # string contenant le jeu
        self.liste=[]  # liste des noeuds fils du noeud actuel, correspondant aux coups jouables          
        self.profondeur = profondeur  # nombre de jetons joués
        self.eval=0   # évaluation de la position : plus la valeur est élevée,
        # plus les croix ont l'avantage (celui qui commence) et inversement
        self.x=x # position x du dernier coup joué
        self.y=y # position y du dernier coup joué
        if parent is None:
            self.parent=None
        else:
            self.parent=parent
        
    def __str__(self):  # Affichage de l'état du jeu contenu dans le noeud
        string=""
        for i in range(6):
            for j in range(12):
                
                if self.plateau[i][j]=="":
                    string+=" |"
                else:
                    
                    string+=self.plateau[i][j]
                    string+="|"
               # string+=" "
                
            string+="\n"
        
        string+="\n1|2|3|4|5|6|7|8|9|101112\n"        
        return string
    
    def victoire_ligne(self,player): # on regarde si le joueur placé en paramètre a gagné
    # en ligne
        
        
        for i in range (6):            
            for j in range(9):
                if (self.plateau[i][j]==player and self.plateau[i][j+1]==player and self.plateau[i][j+2]==player and self.plateau[i][j+3]==player):
                    return True
        return False
                
    def victoire_colonne(self,player):  # on regarde si le joueur placé en paramètre a gagné
    # en colonne
        
        
        for j in range (12):            
            for i in range(3):
                if (self.plateau[i][j]==player and self.plateau[i+1][j]==player and self.plateau[i+2][j]==player and self.plateau[i+3][j]==player):
                  
                    return True
        return False
    def victoire_diago_descendante(self,player): # on regarde si le joueur placé en paramètre a gagné
    # en diagonale descendante
        
        for i in range(3):
            for j in range(9):
                if(self.plateau[i][j]==player and self.plateau[i+1][j+1]==player and self.plateau[i+2][j+2]==player and self.plateau[i+3][j+3]==player):
                    return True
        return False
    
    def victoire_diago_montante(self,player):
        #print("vic diag m")
        for i in range(3,6):
            for j in range(9):
                if(self.plateau[i][j]==player and self.plateau[i-1][j+1]==player and self.plateau[i-2][j+2]==player and self.plateau[i-3][j+3]==player):
                    return True
        
        return False
    
    def IsTerminal(self):  # on vérifie si la grille à l'intérieur du noeud correspond
        # à une partie terminée
        
        
        if joueurLocalquiCommence==True:  #si l'IA commence
            #On regarde s'il y a une victoire de l'adversaire sur les lignes
            if(self.victoire_ligne("o")==True):
                self.eval=self.eval-10000
        
        #On regarde s'il y a une victoire sur les colonnes
            elif(self.victoire_colonne("o")==True):
                self.eval=self.eval-10000
            
         #On regarde s'il y a une victoire sur les diagonales
            elif(self.victoire_diago_descendante("o")==True):
                self.eval=self.eval-10000
        
        
            elif(self.victoire_diago_montante("o")==True):
                self.eval=self.eval-10000
              
        #On regarde s'il y a une victoire de l'IA sur les lignes
            elif(self.victoire_ligne("x")==True):
                self.eval=self.eval+10000
          
                
        #On regarde s'il y a une victoire de l'IA sur les colonnes
            elif(self.victoire_colonne("x")==True):
                self.eval=self.eval+10000
      
        
            elif(self.victoire_diago_descendante("x")==True):
                self.eval=self.eval+10000
        
        
            elif(self.victoire_diago_montante("x")==True):
                self.eval=self.eval+10000
            
        else:  # si l'adversaire commence
            
            #On regarde s'il y a une victoire de l'adversaire sur les lignes
            if(self.victoire_ligne("x")==True):
                self.eval=self.eval+10000          
                
        
            elif(self.victoire_colonne("x")==True):
                self.eval=self.eval+10000
      
        
            elif(self.victoire_diago_descendante("x")==True):
                self.eval=self.eval+10000
        
        
            elif(self.victoire_diago_montante("x")==True):
                self.eval=self.eval+10000  
                
            #On regarde s'il y a une victoire de l'IA sur les lignes
            elif(self.victoire_ligne("o")==True):
                self.eval=self.eval-10000
        
        #On regarde s'il y a une victoire sur les colonnes
            elif(self.victoire_colonne("o")==True):
                self.eval=self.eval-10000
            
         #On regarde s'il y a une victoire sur les diagonales
            elif(self.victoire_diago_descendante("o")==True):
                self.eval=self.eval-10000
        
        
            elif(self.victoire_diago_montante("o")==True):
                self.eval=self.eval-10000
                     
        if (self.eval<=-9000 or self.eval>=9000):
            return True
        
        #on regarde si les 42 jetons ont été joués, alors le jeu est fini
        var=0
        for i in range(6):
            for j in range(12):
                if self.plateau[i][j]=="x" or self.plateau[i][j]=="o":
                    var=var+1
        if var==42:
            self.eval==0
            return True
        return False
    
    # Ci dessous sont les heuristiques utilisées, qui donnent une valeur plus ou moins 
    # élevée à l'attribut self.eval en fonction du déroulement de la partie
    
    def bienpartiligne(self,player): # On regarde si trois pions sont alignés en ligne qqpart
        # et si il y a des espaces à côté
        for i in range (5):
            compteur=0
            for j in range(1,11):
                if (self.plateau[i][j]==player):
                    compteur+=1
                elif(j!=0 and self.plateau[i][j]=="" and self.plateau[i][j-1]==""):
                    compteur=0
                    
                if (compteur==3 and self.plateau[i][j-3]==""):
                    if(j!=11 and self.plateau[i][j+1]==""):
                        return 120
                    return 50
                if(compteur==3 and self.plateau[i][j+1]==""):
                    return 50
                    
        return 0
    
    def biencarre(self,player): # On regarde si il ya un carré de 2 sur 2 d'un même camp
        # et des espaces autour,
        # une position qui peut mener à la victoire
        for i in range(2,5):
            for j in range(1,9):
                if(self.plateau[i][j]==player and self.plateau[i][j+1]==player and self.plateau[i+1][j+1]==player 
                   and self.plateau[i+1][j]==player):
                    if(self.plateau[i-1][j]=="" and self.plateau[i-1][j+1]==""):
                        if(self.plateau[i][j+2]==""and self.plateau[i+1][j+2]==""):
                            return 150
                        if(self.plateau[i][j-1]==""and self.plateau[i+1][j-1]==""):
                            return 150
                        return 70
                    
     
    
    def bien_diago_descendante(self,player): # On regarde si trois pions sont alignés en diagonale
        #qqpart et si il y a des espaces à côté
        
        for i in range(3):
            for j in range(9):
                if(self.plateau[i][j]==player and self.plateau[i+1][j+1]==player and self.plateau[i+2][j+2]==player and self.plateau[i+3][j+3]==""):
                    if(self.plateau[i-1][j-1]==""):
                        return 120
                    return 50
                if(self.plateau[i][j]==player and self.plateau[i+1][j+1]=="" and self.plateau[i+2][j+2]==player and self.plateau[i+3][j+3]==player):
                    return (50)
                if(self.plateau[i][j]==player and self.plateau[i+1][j+1]==player and self.plateau[i+2][j+2]=="" and self.plateau[i+3][j+3]==player):
                    return (50)
                if(self.plateau[i][j]=="" and self.plateau[i+1][j+1]==player and self.plateau[i+2][j+2]==player and self.plateau[i+3][j+3]==player):
                    return (50)
                    
        return 0
    
    def bien_diago_montante(self,player):
        #print("vic diag m")
        for i in range(3,6):
            for j in range(3,9):
                if(self.plateau[i][j]==player and self.plateau[i-1][j+1]==player and self.plateau[i-2][j+2]==player and self.plateau[i-3][j+3]==""):
                    if(i!=5 and self.plateau[i+1][j-1]==""):
                        return 120
                    return 50
                if(self.plateau[i][j]==player and self.plateau[i-1][j+1]=="" and self.plateau[i-2][j+2]==player and self.plateau[i-3][j+3]==player):
                    return 50
                if(self.plateau[i][j]==player and self.plateau[i-1][j+1]==player and self.plateau[i-2][j+2]=="" and self.plateau[i-3][j+3]==player):
                    return 50
                if(self.plateau[i][j]=="" and self.plateau[i-1][j+1]==player and self.plateau[i-2][j+2]==player and self.plateau[i-3][j+3]==player):
                    return 50
        
        return 0
        
        
    def utility(self):  # on définit la valeur associée à la grille à l'état final
        
        utility=0
        
        if joueurLocalquiCommence==True:
            utility=Coeff(self.parent.parent.parent) 
        # On regarde avec la fonction Coeff la position du coup joué et on attribue
        # une valeur utility en conséquence (on ne regarde que le coup joué avec une profondeur
        # de 1, c'est à dire le coup que l'IA va jouer parmi ceux possible)
        else:
            utility-=Coeff(self.parent.parent.parent)
            
        # On utilise ici les heuristiques définies précédemment en attribuant les valeurs
        # correspondantes. On a décidé d'accorder des valeurs plus grandes pour les alignements
        # de 3 jetons en ligne et diagonale que la fonction Coeff. Cette derniere est juste là
        # pour départager quand plusieurs coups seraient équivalents
        
        if(self.biencarre("x")==70):
             utility+=70
             
        if(self.biencarre("x")==150):
             utility+=150
             
        if(self.biencarre("o")==70):
             utility-=70
             
        if(self.biencarre("o")==150):
             utility-=150    
             
        
        
        if(self.bienpartiligne("o")==120):
             utility-=120
        
        if(self.bienpartiligne("x")==50):
             utility+=50
             
        if(self.bienpartiligne("o")==50):
            utility-=50
            
        if(self.bienpartiligne("x")==120):
            utility+=120                
            
        
        if(self.bien_diago_descendante("x")==50):
            utility+=50
        
        if(self.bien_diago_descendante("x")==120):
            utility+=120
        
        if(self.bien_diago_descendante("o")==50):
            utility-=50
        
        if(self.bien_diago_descendante("o")==120):
            utility-=120
            
            
        if(self.bien_diago_montante("x")==50):
            utility+=50
        
        if(self.bien_diago_montante("x")==120):
            utility+=120
        
        if(self.bien_diago_montante("o")==50):
            utility-=50
        if(self.bien_diago_montante("o")==120):
            utility-=120
            
        return utility
          


   # On définit ci dessous la liste des coups jouables qui correspondent donc aux noeuds fils
    def action(self):
        if Turn(self):     # On décide que les croix commencent
              for i in range(6):
                  for j in range (12):
                      if self.plateau[i][j]=="" and (i==5 or self.plateau[i+1][j]!="" ):
                            
                          temp = [list(self.plateau[k]) for k in range(6)] 
                          #on affecte la gravité au jeton avant de le placer
                          temp[i][j]="x"
                          self.liste.append(Node(temp,self.profondeur+1,self,i,j))
                        
        else:
              for i in range(6):
                  for j in range (12):
                      if self.plateau[i][j]=="" and (i==5 or self.plateau[i+1][j]!=""):
                          temp = [list(self.plateau[k]) for k in range(6)]
                          #on affecte la gravité au jeton avant de le placer
                          temp[i][j]="o"
                          self.liste.append(Node(temp,self.profondeur+1,self,i,j))
                            
            
                  
def Turn(node):  # on détermine quel camp doit jouer
        
        value = 1
        if (node.profondeur%2 != 0):
            value = 0
        return value    


# On attribue une valeur à un coup possible en foncion de la position du coup dans la grille
# Plus le coup est centré, plus la valeur est grande. Cette heuristique est importante car
# elle permet à l'IA de jouer un coup correct quand elle ne voit pas de coup important
def Coeff(node):
    mat=[[0,1,2,3,4,5,5,4,3,2,1,0],[2,3,4,6,8,10,10,8,6,4,3,2],
         [5,6,8,10,12,14,14,12,10,8,6,5],[5,6,8,10,12,14,14,12,10,8,6,5],
         [3,4,5,7,9,11,11,9,7,5,4,3],[2,3,4,5,6,8,8,6,5,4,3,2]]
    return mat[node.x][node.y]


# Le code ci-dessous a été repris de l'algorithme Min-max avec l'élaguage Alpha-Beta

def Alpha_Beta_Search(node,profondeur):
   
    if joueurLocalquiCommence:
        v=Max_Value(-600000,600000,node,profondeur)
    else:
        v=Min_Value(-600000,600000,node,profondeur)
            
    return v  

def Max_Value(a,b,node,profondeur): 
    
    if node.IsTerminal()==True:
        if node.parent is None:
            print('fin du jeu')
        
        return node.eval
    elif profondeur==0:
        node.eval=node.utility()   
        return node.eval
    v=-6000000
    node.action()
    for i in range(len(node.liste)):
        v=max(v,Min_Value(a,b,node.liste[i],profondeur-1))
        node.eval=v
        if(v>=b):
            return v
        a=max(a,v)
    return v
        
    
def Min_Value(a,b,node,profondeur):
   
    if node.IsTerminal()==True:
        if node.parent is None:
            print('fin du jeu')    
        return node.eval
    elif profondeur==0:
        node.eval=node.utility() 
        return node.eval
    v=6000000
    node.action()
    for i in range(len(node.liste)):
        v=min(v,Max_Value(a,b,node.liste[i],profondeur-1))
        node.eval=v
        if(v<=a):
            return v
        b=min(b,v)
    return v




    
    
def OrdivsOrdi():
    jeu= [["" for i in range(12)] for j in range(6)]
    node=Node(jeu)
    print(node)
    z=0
    fini=False
    while z<42 and fini==False:
       found=False
       i=0
       debut=time.time()
       v=Alpha_Beta_Search(node,4)
       while i<len(node.liste) and found==False:
         
          if v==node.liste[i].eval:
              print("grille actuelle: ")
              print(node.liste[i])
              fin=time.time()
              print(fin-debut)
              node=node.liste[i]
              node.parent=None 
              found=True
          else:
              i=i+1
            
       z+=1
       if node.IsTerminal():
          fini=True
   
       
        
     
def HumainvsIA():  # L'adversaire de l'IA joue en premier
    jeu= [["" for i in range(12)] for j in range(6)] # Initialisation
    
    node=Node(jeu)     
    z=0
    fini=False
    while z<42 and fini==False:
       if z%2==1:           
           
           found=False
           i=0
           debut=time.time()
           v=Alpha_Beta_Search(node,4)
           while i<len(node.liste) and found==False:
               if v==node.liste[i].eval:  # On cherche le meilleur coup
                   print("grille actuelle: ")
                   print(node.liste[i])
                   #print(node.liste[i].eval) Si on veut afficher l'évaluation de l'IA
                   print("Coup joué: colonne " + str(node.liste[i].y +1))
                   fin=time.time()
                   print("temps utilisé: " + str(fin-debut))
                   
                   node=Node(node.liste[i].plateau,node.liste[i].profondeur)                   
                   node.parent=None
                   found=True
               else:
                   i=i+1
           node.parent=None           
          
       else:
          
           ordonnee= int(input("Choisissez la colonne (1 à 12)"))
           ordonnee-=1
           plat=[]
           for k in range(6):
                  plat.append(list(node.plateau[k]))
           for i in range (6):
               if plat[i][ordonnee]=="" and (i==5 or plat[i+1][ordonnee]!=""):
                   plat[i][ordonnee]="x"
           node.action()  
           for i in node.liste:
               if i.plateau==plat:
                   node=i
                                    
                   node.parent=None
           print(node)  
       z+=1
       if node.IsTerminal():
           fini=True
def IAvsHumain():
    jeu= [["" for i in range(12)] for j in range(6)]
    node=Node(jeu) 
    
    z=0
    fini=False
    while z<42 and fini==False:
       if z%2==0:           
           
           found=False
           i=0
           debut=time.time()
           v=Alpha_Beta_Search(node,4)
           while i<len(node.liste) and found==False:
               if v==node.liste[i].eval: # On cherche le meilleur coup
                   print("grille actuelle: ")
                   print(node.liste[i])
                   #print(node.liste[i].eval) Si on veut afficher l'évaluation de l'IA
                   print("Coup joué: colonne " + str(node.liste[i].y +1))
                   fin=time.time()
                   print("temps utilisé: " + str(fin-debut))
                   node=Node(node.liste[i].plateau, node.liste[i].profondeur)
                   
                   
                   node.parent=None
                   found=True
               else:
                   i=i+1
           node.parent=None           
          
       else:
          
           ordonnee= int(input("Choisissez la colonne (1 à 12)"))
           ordonnee-=1
           plat=[]
           for k in range(6):
                  plat.append(list(node.plateau[k]))
           for i in range (6):
               if plat[i][ordonnee]=="" and (i==5 or plat[i+1][ordonnee]!=""):
                   plat[i][ordonnee]="o"
           print(Node(plat))
           node.action()  
           for i in node.liste:
               
               if i.plateau==plat:
                   node=i                 
                   node.parent=None
           print(node)  
       z+=1
       if node.IsTerminal():
           fini=True
# Pour laisser l'IA commencer, joueurLocalquiCommence=True
global joueurLocalquiCommence
joueurLocalquiCommence=False
if joueurLocalquiCommence==False:
    HumainvsIA()
else:
    IAvsHumain()
    
        

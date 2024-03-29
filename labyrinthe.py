import pygame
from read_colors import read_color_parameters
from utils import convert_data

class Labyrinthe :
    # constructeur
    def __init__(self, sizeX, sizeY):
        """sizeX, sizeY désignent la taille du labyrinthe sur l'axe (x,y)"""
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.version = ""
        self.author = ""
        self.start = [1, 1]
        self.finish = [20, 10]
        self.end = False
        #attention création d'une matrice en Y X
        self.matrice = [ [0]* self.sizeX for _ in range(self.sizeY) ]
        colors = read_color_parameters()
        self.colors = colors.readColors("color.ini")
        print(self.colors)

    def set_color(self, v):
        """Fixe la couleur pour dessiner les murs"""
        self.color = v

    def display_on_console(self):
        """Sortie console du labyrinthe"""
        for j in range(self.sizeY):
            for i in range(self.sizeX):
                # rappel: matrice en Y,X
                print(self.matrice[j][i], end = "")
            print()
        #print(self.matrice)

    def get_matrice(self):
        """renvoie la matrice associée au labyrinthe"""
        return self.matrice
    
    def getXY(self, i,j):
        """Renvoie la case (i,j) du labyrinthe sur l'axe (x,y)"""
        return self.matrice[j][i]

    def setXY(self, i,j,v):
        """Modifie par v la case (i,j) sur l'axe (x,y)"""
        self.matrice[j][i] = v
    
    def getSize(self):
        """Renvoie la taille (x,y) du labyrinthe"""
        return (self.sizeX, self.sizeY)
    
    def wall_destroy(self, i,j):
        """Détruit un mur du labyrinthe en (i,j) sur l'axe (x,y)"""
        self.matrice[j][i]=0

    def load_from_file(self, filename):
        """Charge un labyrinthe d'un fichier texte"""
        with open(filename) as file:
            #lecture du cartouche du labyrinthe
            # 1) vérification du type de fichier
            firstline = file.readline()
            firstline = firstline.rstrip()
            firstline = firstline.split(',')
            if firstline[0] != "map":
                print("mauvais fichier")
                return
            self.version = firstline[1]
            self.author = firstline[2]
            # 2) vérification de la taille du labyrinthe
            snd_line = file.readline()
            snd_line = snd_line.rstrip()
            snd_line = snd_line.split(',')            
            if int(snd_line[0])!=self.sizeX or int(snd_line[1])!=self.sizeY:
                print("dimensions non cohérentes")
                return
            #lecture des données du labyrinthe
            lines = [line.rstrip() for line in file]
        #print(lines)
        for i in range(len(lines)):
            tmp = lines[i]
            tmp_list = tmp.split(',')
            for j in range(len(tmp_list)):
                    tmp_list[j]= convert_data(tmp_list[j])
            #print(tmp_list)
            self.matrice[i]=tmp_list

        self.setAD()
    
    def setAD(self):
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                if self.matrice[i][j] == 100:
                    self.start = [j, i]
                if self.matrice[i][j] == 101:
                    self.finish = [j, i]
        print(self.start, self.finish)

    def hit_finish(self, x, y):
        if x==self.finish[0] and y==self.finish[1] and self.end == False:
            print("Vous êtes arrivés à la sortie !")
            self.end = True

    def hit_box(self, x, y):
        """indique si l'élément (x,y) est un mur"""
        if x>=self.sizeX or x<0 or y<0 or y>=self.sizeY:
            return 1
        return self.matrice[y][x] == 1
    
    def hit_water(self, x, y):
        if x>=self.sizeX or x<0 or y<0 or y>=self.sizeY:
            return 1
        return self.matrice[y][x] == 10

    def draw(self, screen, tilesize):
        """dessine le labyrithne sur la fenètre screen"""
        for j in range(self.sizeY):
            for i in range(self.sizeX):
                if self.matrice[j][i] == 1:
                    pygame.draw.rect(screen, self.color , (i * tilesize + self.offsetX, j * tilesize + self.offsetY, tilesize, tilesize))
                if self.matrice[j][i] == 10:
                    pygame.draw.rect(screen, self.colors["water_color"] , (i * tilesize + self.offsetX, j * tilesize + self.offsetY, tilesize, tilesize))
                    
    def change_origin(self, X, Y):
        self.offsetX = X
        self.offsetY = Y
        


#laby = Labyrinthe(20,10)
#laby.load_from_file("laby-02.csv")
#laby.display_on_console()

"""
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
l3 = [11,12,13,14,15]
lst = []
lst.append(l1)
lst.append(l2)
lst.append(l3)
print(lst)

print(lst[2][1])
"""
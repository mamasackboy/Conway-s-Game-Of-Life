# Importation des bibliothèques et initialison des variables
import pygame
import time
import numpy as num
CEL_PV= (10,10,10)
COL_GR=(40,40,40)
CEL_PM=(170,170,170)
COL_BG=(255,255,255)

#application du changement de générations
def update(ecran, cellules, taille, larg=False ):
    n_cellules= num.zeros((cellules.shape[0],cellules.shape[1]))

# Definition et parcours de la grille 
    for ligne , col in num.ndindex(cellules.shape):
        vivant= num.sum(cellules[ligne-1:ligne+2 , col-1:col+2]) - cellules[ligne,col]
        coul= COL_BG if cellules[ligne,col]==0 else CEL_PV
        
#Définition et application des 4 règles de Conway    
        if cellules[ligne, col]== 1:
            if vivant < 2 or vivant > 3:
                if larg:
                    coul=CEL_PM
            elif 2 <= vivant <= 3:
                n_cellules[ligne,col]=1
                if larg:
                    coul=CEL_PV
        else:
            if vivant == 3:
                n_cellules[ligne,col]=1
                if larg:
                    coul=CEL_PV
#Dessin de pygame
        pygame.draw.rect(ecran,coul,(ligne*taille , col*taille , taille-1 , taille -1))
        
    return n_cellules

#Initialisation pygame
def main():
    pygame.init()
    ecran=pygame.display.set_mode((800,600))
    
    cellules=num.zeros((600,80))
    ecran.fill(COL_GR)
    update(ecran,cellules,10)
    
    pygame.display.flip()
    pygame.display.update()
    pygame.display.set_caption("Conway's Game Of Life")
    
    running=True
    
    while True:
#Permet de quitter
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
#Si l'on appuie sur la touche espace la simulation se met en pause
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running= not running
                    update(ecran, cellules, 10)
                    pygame.display.update()
#Si l'on clique sur une case , la cellule devient vivante 
            if pygame.mouse.get_pressed()[0]:
                pos= pygame.mouse.get_pos()
                cellules[pos[0]//10,pos[1]//10] = 1
                update(ecran,cellules,10)
                pygame.display.update()
                
        ecran.fill(COL_GR)
        
        if running :
            cellules=update(ecran, cellules, 10,larg=True)
            pygame.display.update()
        time.sleep(0.000000001)

if __name__ =='__main__':
    main()

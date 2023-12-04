import pygame
import random

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
gris = (220, 216, 239)

# Initiation de 'pygame'
pygame.init()

# Création de la fenêtre de jeu
largeur, hauteur = 850, 700
ecran_de_jeu = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Menu Pendu")

# Police de caractères
police = pygame.font.Font(None, 36)
texte_menu = "Cliquez pour commencer"

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Dessiner le fond
    ecran_de_jeu.fill(gris)

    # Dessiner le texte du menu au centre
    texte_surface = police.render(texte_menu, True, noir)
    texte_rect = texte_surface.get_rect(center=(largeur // 2, hauteur // 2))
    ecran_de_jeu.blit(texte_surface, texte_rect)
    
    # Toutes les fonctions 
    def choisir_mot():
        with open("mots.txt", 'r') as fichier:
            mots = fichier.readlines()
            mot_random = random.choice(mots)
        return mot_random.strip()

    # Mettre à jour l'affichage
    pygame.display.flip()

    
    
    
    
    

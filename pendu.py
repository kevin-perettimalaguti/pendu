import pygame
import random

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
grey = (114, 114, 114)
red = (243, 65, 51)
blue = (85, 97, 245)

# Initialisation de 'pygame'
pygame.init()

# Création de la fenêtre de jeu
largeur, hauteur = 700, 600
ecran_de_jeu = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu du Pendu")

# Police de caractères
police = pygame.font.Font(None, 36)
police_menu = pygame.font.Font(None, 50)
police_option = pygame.font.Font(None, 21)

# Chargement des mots depuis un fichier
with open("mots.txt", 'r') as fichier_mots:
    mots = [mot.strip() for mot in fichier_mots.readlines()]
    mot_random = random.choice(mots)

# Mot à deviner
mot_affiche = ['_' for _ in mot_random]

# Esthétique avant le jeu
texte_presentation = "Que voulez faire ?"

# Fonction pour afficher le mot dans la fenêtre
def afficher_mot():
    x, y = largeur // 2 - 15 * len(mot_affiche), hauteur // 2 - 40  # Ajuster le décalage initial
    espacement_entre_lettres = 5

    for lettre in mot_affiche:
        affichage_lettre = police_menu.render(lettre, True, red)
        ecran_de_jeu.blit(affichage_lettre, (x, y))
        x += affichage_lettre.get_width() + espacement_entre_lettres

# Affichage du menu
def afficher_menu(selectionner_option):
    ecran_de_jeu.fill(grey)
    affichage_texte = police_menu.render(texte_presentation, True, red)
    ecran_de_jeu.blit(affichage_texte, (largeur // 2 - affichage_texte.get_width() // 2, hauteur // 2))

    options = ["Jouer", "Ajouter un mot", "Quitter"]
    for i, option in enumerate(options):
        
        if i == selectionner_option:
            couleur = red              
        else:
            couleur = white
        affichage_option = police_menu.render(option, True, couleur)
        ecran_de_jeu.blit(affichage_option, (largeur // 2 - affichage_option.get_width() // 2, 100 + i * 50))

    pygame.display.flip()

# Boucle principale
en_jeu = False
erreur = 0
selected_option = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % 3
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % 3
            elif event.key == pygame.K_RETURN:
                options = ["Jouer", "Ajouter un mot", "Quitter"]  # Ajout de cette ligne pour définir options
                if options[selected_option] == "Jouer":
                    en_jeu = True
                    ecran_de_jeu.fill(grey)
                    afficher_mot()
                    pygame.display.flip()
                elif options[selected_option] == "Ajouter un mot":
                    nouveau_mot = input("Entrez un nouveau mot : ")
                    with open("mots.txt", 'a') as fichier:
                        fichier.write(nouveau_mot + "\n")
                    print("Mot ajouté avec succès !")
                elif options[selected_option] == "Quitter":
                    pygame.quit()
                    

    if en_jeu:
        # Logique du jeu
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    lettre = event.unicode.lower()
                    if lettre in mot_random:
                        # Remplacer les '_' par la lettre correcte
                        for position, position_lettre in enumerate(mot_random):
                            if position_lettre == lettre:
                                mot_affiche[position] = lettre
               

        # Mise à jour de l'affichage du mot
        ecran_de_jeu.fill(grey)
        afficher_mot()
        pygame.display.flip()        

    else:
        afficher_menu(selected_option)


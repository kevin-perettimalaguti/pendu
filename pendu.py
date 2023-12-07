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
    x = largeur // 2 - (15 * len(mot_affiche))  # Ajuster le décalage initial
    y = hauteur - 120  # Positionner les lettres en bas de l'écran
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

# Fonction pour ajouter un mot dans le fichier 'mots.txt'
def ajouter_mot():
    ecran_de_jeu.fill(grey)
    affichage_texte = police_menu.render("Ajouter un nouveau mot :", True, red)
    ecran_de_jeu.blit(affichage_texte, (largeur // 2 - affichage_texte.get_width() // 2, hauteur // 2 - 50))
    pygame.display.flip()

    nouveau_mot = ""
    ajout_termine = False
    espacement_entre_lettres = 5  # Ajustez cette valeur selon votre préférence

    while not ajout_termine:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    ajout_termine = True
                elif event.key == pygame.K_BACKSPACE:
                    nouveau_mot = nouveau_mot[:-1]
                elif event.unicode.isalpha():
                    nouveau_mot += event.unicode

        ecran_de_jeu.fill(grey)  # Efface l'écran avec la couleur d'arrière-plan

        affichage_texte = police_menu.render("Ajouter un nouveau mot :", True, red)
        ecran_de_jeu.blit(affichage_texte, (largeur // 2 - affichage_texte.get_width() // 2, hauteur // 2 - 50))

        affichage_nouveau_mot = police_menu.render(nouveau_mot, True, red)
        x = largeur // 2 - (affichage_nouveau_mot.get_width() + (len(nouveau_mot) - 1) * espacement_entre_lettres) // 2
        y = hauteur // 2 + 50
        for lettre in nouveau_mot:
            affichage_lettre = police_menu.render(lettre, True, red)
            ecran_de_jeu.blit(affichage_lettre, (x, y))
            x += affichage_lettre.get_width() + espacement_entre_lettres

        pygame.display.flip()


    with open("mots.txt", 'a') as fichier:
        fichier.write(nouveau_mot + "\n")
    print("Mot ajouté avec succès !")
    
#Fonction pour dessiner le pendu au fur et à mesure des erreur
def dessiner_pendu(erreurs):
    pygame.draw.line(ecran_de_jeu, black, (600, 50), (600, 300), 5)  # Support vertical
    pygame.draw.line(ecran_de_jeu, black, (600, 50), (450, 50), 5)   # Support horizontal
    
    if erreurs == 0:
        return
    elif erreurs == 1:
        pygame.draw.ellipse(ecran_de_jeu, black, pygame.Rect(410, 110, 40, 40))  # Tête
    elif erreurs == 2:
        pygame.draw.ellipse(ecran_de_jeu, black, pygame.Rect(410, 110, 40, 40))  # Tête
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(450, 200), (450, 50), 5)  # Corps
    elif erreurs == 3:
        pygame.draw.ellipse(ecran_de_jeu, black, pygame.Rect(410, 110, 40, 40))  # Tête
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(450, 200), (450, 50), 5)  # Corps
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(450, 170), (500, 140), 5)  # Bras gauche
    elif erreurs == 4:
        pygame.draw.ellipse(ecran_de_jeu, black, pygame.Rect(410, 110, 40, 40))  # Tête
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(450, 200), (450, 50), 5)  # Corps
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(450, 170), (500, 140), 5)  # Bras gauche
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(450, 170), (400, 140), 5)  # Bras droit
    elif erreurs == 5:
        pygame.draw.ellipse(ecran_de_jeu, black, pygame.Rect(410, 110, 40, 40))  # Tête
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(450, 200), (450, 50), 5)  # Corps
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(450, 170), (500, 140), 5)  # Bras gauche
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(450, 170), (400, 140), 5)  # Bras droit
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(500, 250), (450, 200), 5)  # Jambe gauche
    elif erreurs == 6:
        pygame.draw.ellipse(ecran_de_jeu, black, pygame.Rect(410, 110, 40, 40))  # Tête
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(450, 200), (450, 50), 5)  # Corps
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(450, 170), (500, 140), 5)  # Bras gauche
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(450, 170), (400, 140), 5)  # Bras droit
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(500, 250), (450, 200), 5)  # Jambe gauche
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(400, 250), (450, 200), 5)  # Jambe droite
    elif erreurs == 7:
        pygame.draw.ellipse(ecran_de_jeu, black, pygame.Rect(410, 110, 40, 40))  # Tête
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(450, 200), (450, 50), 5)  # Corps
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(450, 170), (500, 140), 5)  # Bras gauche
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(450, 170), (400, 140), 5)  # Bras droit
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(500, 250), (450, 200), 5)  # Jambe gauche
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(400, 250), (450, 200), 5)  # Jambe droite
        pygame.draw.line(ecran_de_jeu, black, pygame.Rect(450, 250), (500, 200), 5)  # Pied gauche
    elif erreurs > 7:
        afficher_menu(selected_option)
                         

# Boucle principale
en_jeu = False
selected_option = 0
erreur = 0

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
                options = ["Jouer", "Ajouter un mot", "Quitter"]
                if options[selected_option] == "Jouer":
                    en_jeu = True
                    ecran_de_jeu.fill(grey)
                    afficher_mot()
                    pygame.display.flip()
                elif options[selected_option] == "Ajouter un mot":
                    ajouter_mot()
                elif options[selected_option] == "Quitter":
                    pygame.quit()

        if en_jeu == True:
            # Logique du jeu        
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    lettre = event.unicode.lower()
                    if lettre in mot_random:
                        # Remplacer les '_' par la lettre correcte
                        for position, position_lettre in enumerate(mot_random):
                            if position_lettre == lettre:
                                mot_affiche[position] = lettre
                            else:
                                erreur =+ 1
                                                           

            # Vérifier si le mot est complété
                if '_' not in mot_affiche:
                    en_jeu = False
                    ecran_de_jeu.fill(grey)
                    afficher_menu(selected_option)
                    pygame.display.flip()
                    
            # Mise à jour de l'affichage du mot et du dessin 
            ecran_de_jeu.fill(grey)
            afficher_mot()
            dessiner_pendu(erreur)
            pygame.display.flip()        

        else:
            afficher_menu(selected_option)



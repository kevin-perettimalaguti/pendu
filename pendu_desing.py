# Importation des modules nécessaires
import pygame  # Module principal pour le jeu
import random  # Module pour générer des nombres aléatoires
import pygame_menu  # Module pour créer des menus

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
fenetre_largeur = 700
fenetre_hauteur = 480
fenetre = pygame.display.set_mode((fenetre_largeur, fenetre_hauteur))

# Définition de couleurs utilisées dans le jeu
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
BLEU_CLAIR = (102, 255, 255)
VIOLET = (182, 48, 243)
GRIS = (170, 166, 184)

# Définition de polices utilisées dans le jeu
police = pygame.font.Font(None, 36)
police_menu = pygame.font.Font(None, 50)
police_option = pygame.font.Font(None, 21)

# Initialisation des variables globales/constants
fonte_bouton = pygame.font.SysFont("arial", 20)
fonte_devine = pygame.font.SysFont("monospace", 24)
fonte_perdu = pygame.font.SysFont('arial', 45)

mot_a_deviner = ''  # Mot à deviner
boutons = []  # Liste des boutons du clavier
lettres_devinees = []  # Liste des lettres déjà devinées
images_pendu = [pygame.image.load('img/dessin0.png'), pygame.image.load('img/dessin1.png'),
                 pygame.image.load('img/dessin2.png'), pygame.image.load('img/dessin3.png'),
                 pygame.image.load('img/dessin4.png'), pygame.image.load('img/dessin5.png'),
                 pygame.image.load('img/dessin6.png')]  # Images pour l'animation du pendu

membres = 0  # Nombre de parties du corps dessinées


# Fonction pour redessiner la fenêtre du jeu
def redessiner_fenetre():
    global lettres_devinees
    global images_pendu
    global membres
    fenetre.fill(VIOLET)

    # Dessiner les boutons du clavier
    for i in range(len(boutons)):
        if boutons[i][4]:
            pygame.draw.circle(fenetre, NOIR, (boutons[i][1], boutons[i][2]), boutons[i][3])
            pygame.draw.circle(fenetre, boutons[i][0], (boutons[i][1], boutons[i][2]), boutons[i][3] - 2)
            label = fonte_bouton.render(chr(boutons[i][5]), 1, NOIR)
            fenetre.blit(label, (boutons[i][1] - (label.get_width() / 2), boutons[i][2] - (label.get_height() / 2)))

    # Afficher le mot avec les espaces et lettres devinées
    mot_espaces = mot_espace(mot_a_deviner, lettres_devinees)
    label1 = fonte_devine.render(mot_espaces, 1, NOIR)
    rect = label1.get_rect()
    longueur = rect[2]

    fenetre.blit(label1, (fenetre_largeur / 2 - longueur / 2, 400))

    # Afficher l'image du pendu
    image = images_pendu[membres]
    fenetre.blit(image, (fenetre_largeur / 2 - image.get_width() / 2 + 20, 150))
    pygame.display.update()


# Fonction pour choisir un mot aléatoire dans un fichier
def mot_aleatoire():
    with open('mots.txt') as fichier:
        lignes = fichier.readlines()
    i = random.randrange(0, len(lignes) - 1)
    return lignes[i].strip()


# Fonction pour vérifier si une lettre fait partie du mot à deviner
def pendu(lettre):
    global mot_a_deviner
    return lettre.lower() not in mot_a_deviner.lower()


# Fonction pour afficher le mot avec les espaces et lettres devinées
def mot_espace(mot, lettres_devinees=[]):
    mot_esp = ''
    for x in range(len(mot)):
        if mot[x] != ' ':
            mot_esp += '_ '
            for lettre_devinee in lettres_devinees:
                if mot[x].upper() == lettre_devinee:
                    mot_esp = mot_esp[:-2]
                    mot_esp += mot[x].upper() + ' '
        elif mot[x] == ' ':
            mot_esp += ' '
    return mot_esp


# Fonction pour détecter si un bouton du clavier est cliqué
def bouton_touche(x, y):
    for i in range(len(boutons)):
        if x < boutons[i][1] + 20 and x > boutons[i][1] - 20:
            if y < boutons[i][2] + 20 and y > boutons[i][2] - 20:
                return boutons[i][5]
    return None


# Fonction pour gérer la fin de la partie (victoire ou défaite)
def fin(partie_gagnee=False):
    global membres
    perdu_txt = 'Tu as Perdu !'
    gagne_txt = 'Victoire!'
    redessiner_fenetre()
    pygame.time.delay(1000)
    fenetre.fill(GRIS)

    if partie_gagnee:
        label = fonte_perdu.render(gagne_txt, 1, NOIR)
    else:
        label = fonte_perdu.render(perdu_txt, 1, NOIR)

    mot_txt = fonte_perdu.render(mot_a_deviner.upper(), 1, NOIR)
    mot_etait = fonte_perdu.render('Le mot était : ', 1, NOIR)

    fenetre.blit(mot_txt, (fenetre_largeur / 2 - mot_txt.get_width() / 2, 295))
    fenetre.blit(mot_etait, (fenetre_largeur / 2 - mot_etait.get_width() / 2, 245))
    fenetre.blit(label, (fenetre_largeur / 2 - label.get_width() / 2, 140))
    pygame.display.update()
    encore = True
    while encore:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                encore = False
    reinitialiser()


# Fonction pour réinitialiser les variables de jeu
def reinitialiser():
    global membres
    global lettres_devinees
    global boutons
    global mot_a_deviner
    for i in range(len(boutons)):
        boutons[i][4] = True

    membres = 0
    lettres_devinees = []
    mot_a_deviner = mot_aleatoire()


# Création des boutons du clavier
augmenter = round(fenetre_largeur / 13)
for i in range(26):
    if i < 13:
        y = 40
        x = 25 + (augmenter * i)
    else:
        x = 25 + (augmenter * (i - 13))
        y = 85
    boutons.append([BLEU_CLAIR, x, y, 20, True, 65 + i])

# Sélection d'un mot aléatoire pour la partie
mot_a_deviner = mot_aleatoire()
en_jeu = True

# Boucle principale du jeu
while en_jeu:
    redessiner_fenetre()
    pygame.time.delay(10)

    # Gestion des événements (clavier, souris, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_jeu = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                en_jeu = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_clic = pygame.mouse.get_pos()
            lettre = bouton_touche(pos_clic[0], pos_clic[1])
            if lettre is not None:
                lettres_devinees.append(chr(lettre))
                boutons[lettre - 65][4] = False
                if pendu(chr(lettre)):
                    if membres != 5:
                        membres += 1
                    else:
                        fin()
                else:
                    print(mot_espace(mot_a_deviner, lettres_devinees))
                    if mot_espace(mot_a_deviner, lettres_devinees).count('_') == 0:
                        fin(True)


# Définition de la deuxième version du jeu
def jeu_2():
    global en_jeu, mot_a_deviner, lettres_devinees, boutons, membres
    en_jeu = True
    mot_a_deviner = mot_aleatoire()
    reinitialiser()

    while en_jeu:
        redessiner_fenetre()
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_jeu = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    en_jeu = False
                elif pygame.K_a <= event.key <= pygame.K_z:
                    lettre = chr(event.key).upper()
                    if lettre not in lettres_devinees:
                        lettres_devinees.append(lettre)
                        for btn in boutons:
                            if chr(btn[5]) == lettre:
                                btn[4] = False
                        if pendu(lettre):
                            if membres != 6:
                                membres += 1
                            else:
                                fin()
                        else:
                            if mot_espace(mot_a_deviner, lettres_devinees).count('_') == 0:
                                fin(True)


# Fonction pour afficher les lettres déjà proposées
def lettres_proposees(lettres_devinees):
    lettres_proposees_texte = 'Lettres déjà proposées : ' + ', '.join(lettres_devinees)
    texte_proposees = police_menu.render(lettres_proposees_texte, True, BLEU)
    fenetre.blit(texte_proposees, (20, fenetre_hauteur - 30))


# Fonction pour la première version du jeu
def jeu_1():
    fenetre.fill(NOIR)
    afficher_texte = police_menu.render("Insérer un mot à deviner :", True, BLEU)
    fenetre.blit(afficher_texte, (fenetre_largeur // 2 - afficher_texte.get_width() // 2, fenetre_hauteur // 2 - 50))
    pygame.display.flip()

    nouveau_mot = ""
    ajout_termine = False

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

        fenetre.fill(GRIS)
        afficher_texte = police_menu.render("Insérer un mot à deviner :", True, BLEU)
        fenetre.blit(afficher_texte, (fenetre_largeur // 2 - afficher_texte.get_width() // 2, fenetre_hauteur // 2 - 50))

        afficher_nouveau_mot = police_menu.render(nouveau_mot, True, BLEU)
        text_x = fenetre_largeur // 2 - afficher_nouveau_mot.get_width() // 2
        text_y = fenetre_hauteur // 2 - afficher_nouveau_mot.get_height() // 2
        fenetre.blit(afficher_nouveau_mot, (text_x, text_y))
        pygame.display.flip()

    with open("mots.txt", 'a') as fichier:
        fichier.write(nouveau_mot.strip() + "\n")


# Initialisation du menu principal
menu = pygame_menu.Menu('Welcome', 700, 480, theme=pygame_menu.themes.THEME_GREEN)

menu.add.text_input('Prénom :', default='Kevin')
menu.add.button('Jouer au Pendu', jeu_2)
menu.add.button('Ajouter un mot', jeu_1)
menu.add.button('Quitter', pygame_menu.events.EXIT)

# Lancement du menu
menu.mainloop(fenetre)

# Fermeture de Pygame
pygame.quit()

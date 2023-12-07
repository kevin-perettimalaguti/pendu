# importer module#
import pygame, random, pygame_menu

pygame.init()
winHeight = 480
winWidth = 700
win=pygame.display.set_mode((winWidth,winHeight))

# initialize global variables/constants #

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHT_BLUE = (102,255,255)
PURPLE = (182, 48, 243)
GREY = (170, 166, 184)


police = pygame.font.Font(None, 36)
police_menu = pygame.font.Font(None, 50)
police_option = pygame.font.Font(None, 21)

btn_font = pygame.font.SysFont("arial", 20)
guess_font = pygame.font.SysFont("monospace", 24)
lost_font = pygame.font.SysFont('arial', 45)
word = ''
buttons = []
guessed = []
hangmanPics = [pygame.image.load('img/dessin0.png'), pygame.image.load('img/dessin1.png'), pygame.image.load('img/dessin2.png'), pygame.image.load('img/dessin3.png'), pygame.image.load('img/dessin4.png'), pygame.image.load('img/dessin5.png'), pygame.image.load('img/dessin6.png')]

limbs = 0


def redraw_game_window():
    global guessed
    global hangmanPics
    global limbs
    win.fill(PURPLE)
    # Buttons
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.circle(win, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])
            pygame.draw.circle(win, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2
                               )
            label = btn_font.render(chr(buttons[i][5]), 1, BLACK)
            win.blit(label, (buttons[i][1] - (label.get_width() / 2), buttons[i][2] - (label.get_height() / 2)))

    spaced = spacedOut(word, guessed)
    label1 = guess_font.render(spaced, 1, BLACK)
    rect = label1.get_rect()
    length = rect[2]
    
    win.blit(label1,(winWidth/2 - length/2, 400))

    pic = hangmanPics[limbs]
    win.blit(pic, (winWidth/2 - pic.get_width()/2 + 20, 150))
    pygame.display.update()


def randomWord():
    file = open('mots.txt')
    f = file.readlines()
    i = random.randrange(0, len(f) - 1)

    return f[i][:-1]


def hang(guess):
    global word
    if guess.lower() not in word.lower():
        return True
    else:
        return False

def spacedOut(word, guessed=[]):
    spacedWord = ''
    guessedLetters = guessed
    for x in range(len(word)):
        if word[x] != ' ':
            spacedWord += '_ '
            for i in range(len(guessedLetters)):
                if word[x].upper() == guessedLetters[i]:
                    spacedWord = spacedWord[:-2]
                    spacedWord += word[x].upper() + ' '
        elif word[x] == ' ':
            spacedWord += ' '
    return spacedWord
            

def buttonHit(x, y):
    for i in range(len(buttons)):
        if x < buttons[i][1] + 20 and x > buttons[i][1] - 20:
            if y < buttons[i][2] + 20 and y > buttons[i][2] - 20:
                return buttons[i][5]
    return None

def end(winner=False):
    global limbs
    lostTxt = 'Tu as Perdu !'
    winTxt = 'Victoire!'
    redraw_game_window()
    pygame.time.delay(1000)
    win.fill(GREY)

    if winner == True:
        label = lost_font.render(winTxt, 1, BLACK)
    else:
        label = lost_font.render(lostTxt, 1, BLACK)

    wordTxt = lost_font.render(word.upper(), 1, BLACK)
    wordWas = lost_font.render('Le mot était : ', 1, BLACK)

    win.blit(wordTxt, (winWidth/2 - wordTxt.get_width()/2, 295))
    win.blit(wordWas, (winWidth/2 - wordWas.get_width()/2, 245))
    win.blit(label, (winWidth / 2 - label.get_width() / 2, 140))
    pygame.display.update()
    again = True
    while again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                again = False
    reset()


def reset():
    global limbs
    global guessed
    global buttons
    global word
    for i in range(len(buttons)):
        buttons[i][4] = True

    limbs = 0
    guessed = []
    word = randomWord()

increase = round(winWidth / 13)
for i in range(26):
    if i < 13:
        y = 40
        x = 25 + (increase * i)
    else:
        x = 25 + (increase * (i - 13))
        y = 85
    buttons.append([LIGHT_BLUE, x, y, 20, True, 65 + i])
     

word = randomWord()
inPlay = True

while inPlay:
    redraw_game_window()
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inPlay = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickPos = pygame.mouse.get_pos()
            letter = buttonHit(clickPos[0], clickPos[1])
            if letter != None:
                guessed.append(chr(letter))
                buttons[letter - 65][4] = False
                if hang(chr(letter)):
                    if limbs != 5:
                        limbs += 1
                    else:
                        end()
                else:
                    print(spacedOut(word, guessed))
                    if spacedOut(word, guessed).count('_') == 0:
                        end(True)                      
                        

def jeu_2():
    
    global inPlay, word, guessed, buttons, limbs
    inPlay = True
    word = randomWord()
    reset()

    while inPlay:
        redraw_game_window()
        pygame.time.delay(10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inPlay = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inPlay = False
                elif pygame.K_a <= event.key <= pygame.K_z:
                    letter = chr(event.key).upper()
                    if letter not in guessed:
                        guessed.append(letter)
                        for btn in buttons:
                            if chr(btn[5]) == letter:
                                btn[4] = False
                        if hang(letter):
                            if limbs != 6:
                                limbs += 1
                            else:
                                end()
                        else:
                            if spacedOut(word, guessed).count('_') == 0:
                                end(True)

def lettres_choisies(guessed):
    guessed_letters_text = 'Lettres déja proposées : ' + ', '.join(guessed)
    guessed_text = police_menu.render(guessed_letters_text, True, BLUE)
    win.blit(guessed_text, (20,winHeight-30))
    
def jeu_1():   
    win.fill(BLACK)
    afficher_texte = police_menu.render("Insérer un mot à deviner :", True, BLUE)
    win.blit(afficher_texte, (winHeight // 2 - afficher_texte.get_width() // 2, winWidth // 2 - 50))
    pygame.display.flip()

    new_mot = ""
    ajout_termine = False

    while not ajout_termine:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    ajout_termine = True
                elif event.key == pygame.K_BACKSPACE:
                    new_mot = new_mot[:-1]
                elif event.unicode.isalpha():
                    new_mot += event.unicode  

       
        win.fill(GREY) 
        afficher_texte = police_menu.render("Insérer un mot à deviner :", True, BLUE)
        win.blit(afficher_texte, (winWidth // 2 - afficher_texte.get_width() // 2, winHeight // 2 - 50))  
        
        afficher_new_mot = police_menu.render(new_mot, True, BLUE)
        text_x = winWidth // 2 - afficher_new_mot.get_width() // 2
        text_y = winHeight // 2 - afficher_new_mot.get_height() // 2
        win.blit(afficher_new_mot, (text_x, text_y))
        pygame.display.flip()

    with open("mots.txt", 'a') as fichier:
        fichier.write(new_mot.strip () + "\n")






menu = pygame_menu.Menu('Welcome', 700, 480,
                       theme=pygame_menu.themes.THEME_GREEN)

menu.add.text_input('Prénom :', default='Kevin')
menu.add.button('Jouer au Pendu', jeu_2)
menu.add.button('Ajouter un mot', jeu_1)
menu.add.button('Quitter', pygame_menu.events.EXIT)

menu.mainloop(win)

pygame.quit()



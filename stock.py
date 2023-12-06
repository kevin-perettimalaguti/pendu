def dessiner_pendu(erreurs):
    pygame.draw.line(ecran_de_jeu, black, (50,50), (50,300), 5)
    pygame.draw.line(ecran_de_jeu, black, (50,50), (200,50), 5)
    pygame.draw.line(ecran_de_jeu, black, (200, 50), (200,120), 5)
    pygame.draw.line(ecran_de_jeu, black, (90, 50), (50,90), 5)
    if erreurs == 0:
        return
    elif erreurs == 1:
        #1
        pygame.draw.ellipse(ecran_de_jeu, black, 
        pygame.Rect(180, 110, 40, 40))    
    elif erreurs == 2:
        #1
        pygame.draw.ellipse(ecran_de_jeu, black, 
        pygame.Rect(180, 110, 40, 40)) 
        #2
        pygame.draw.line(ecran_de_jeu, black, (200, 200), (200,50), 5)
    elif erreurs == 3:
        #1
        pygame.draw.ellipse(ecran_de_jeu, black, 
        pygame.Rect(180, 110, 40, 40)) 
        #2
        pygame.draw.line(ecran_de_jeu, black, (200, 200), (200,50), 5)
        #3
        pygame.draw.line(ecran_de_jeu, black, (200, 170), (150,140), 5)
    elif erreurs == 4:
        #1
        pygame.draw.ellipse(ecran_de_jeu, black, 
        pygame.Rect(180, 110, 40, 40)) 
        #2
        pygame.draw.line(ecran_de_jeu, black, (200, 200), (200,50), 5)
        #3
        pygame.draw.line(ecran_de_jeu, black, (200, 170), (150,140), 5)
        #4
        pygame.draw.line(ecran_de_jeu, black, (200, 170), (250,140), 5)
    elif erreurs == 5:
        #1
        pygame.draw.ellipse(ecran_de_jeu, black, 
        pygame.Rect(180, 110, 40, 40)) 
        #2
        pygame.draw.line(ecran_de_jeu, black, (200, 200), (200,50), 5)
        #3
        pygame.draw.line(ecran_de_jeu, black, (200, 170), (150,140), 5)
        #4
        pygame.draw.line(ecran_de_jeu, black, (200, 170), (250,140), 5)
        #5
        pygame.draw.line(ecran_de_jeu, black, (150,250), (200, 200), 5)
    elif erreurs == 6:
        #1
        pygame.draw.ellipse(ecran_de_jeu, black, 
        pygame.Rect(180, 110, 40, 40)) 
        #2
        pygame.draw.line(ecran_de_jeu, black, (200, 200), (200,50), 5)
        #3
        pygame.draw.line(ecran_de_jeu, black, (200, 170), (150,140), 5)
        #4
        pygame.draw.line(ecran_de_jeu, black, (200, 170), (250,140), 5)
        #5
        pygame.draw.line(ecran_de_jeu, black, (150,250), (200, 200), 5)
        #6
        pygame.draw.line(ecran_de_jeu, black, (250,250), (200, 200), 5)
    elif erreurs == 7:
        ecran_de_jeu.blit(texte2, texte2_rect)
        ecran_de_jeu.blit(texte, texte3_rect)
    elif erreurs >7:
        pygame.quit()
        sys.exit()
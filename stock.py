# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Le bouton de la souris a été cliqué!")

    # Dessiner le fond
    ecran.fill(noir)

    # Dessiner le texte du menu au centre
    texte_surface = police.render(texte_menu, True, blanc)
    texte_rect = texte_surface.get_rect(center=(largeur // 2, hauteur // 2))
    ecran.blit(texte_surface, texte_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()
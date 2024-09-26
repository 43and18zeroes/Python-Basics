import pygame

pygame.init()

# Fenster erstellen
screen = pygame.display.set_mode((800, 600))

# Spielschleife
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Hintergrundfarbe
  screen.fill((255, 255, 255))

  # Aktualisieren des Fensters
  pygame.display.flip()

pygame.quit()
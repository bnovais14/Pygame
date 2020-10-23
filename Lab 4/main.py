import pygame
from random import randint

def sorteiacor():
     r = randint(0, 255)
     g = randint(0, 255)
     b = randint(0, 255)
     cor = (r, g, b)
     return cor

BLACK = (0, 0, 0)
cor = sorteiacor()
pygame.init()

fundo = "cenario.jpg"
imagem = "rato.png"
imagemInvertida = "ratoInvertido.png"
#imagemParado = ".png"
#imagemPulando = ".png"
background = pygame.image.load(fundo)
rato = pygame.image.load(imagem)
ratoInvertido = pygame.image.load(imagemInvertida)
#palhaçoParado = pygame.image.load(imagemParado)
#palhaçoPulando = pygame.image.load(imagemPulando)

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("O Rato e o  Palhaço")

clock = pygame.time.Clock()
box_x = 300
box_dir = 5
jogoAtivo = True

while jogoAtivo:
     clock.tick(30)
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             jogoAtivo = False

     screen.blit(background, (0, 0))
     box_x += box_dir

     if box_x >= 500:
        box_x = 500
        box_dir = -5
        cor = sorteiacor()
     elif box_x <= -10:
        box_x = -10
        box_dir = 5
        cor = sorteiacor()

     screen.blit(background, (0, 0))
     screen.blit(rato, (box_x, 300))
     pygame.time.delay(8)
     pygame.display.update()

pygame.time.delay(2000)
quit()

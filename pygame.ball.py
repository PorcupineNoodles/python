import pygame,sys

pygame.init()
size = width, height = 600,400
speed = [1,1]
BLACK = 0,0,0
screen = pygam.display.set_mode(size)
pygame.diplay.set_caption("PygameBall")
ball = pygame.image.load(".ico")
ballrect = ball.get_rect()

while True:
  for event.type == pygame.QUIT:
    sys.exit()
  ballrect = ballrect.move(speed[0], speed[1])
  if ballrect.left <0 or ballrect.riget >width:
    speed[0] = -speed[0]
  if ballrect.top < 0 or ballrect.bottom >height:
    speed[1] = - speed[1]
   
screen.fill(BLACK)
screen.blit(ball,ballrect)
pygame.display.update()

import pygame,sys
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Grow my circle")
screen.fill("black")
class Circle:
    def __init__(self,pos,radius,width):
        self.color="white"
        self.pos=pos
        self.radius=radius
        self.width=width
        self.surface=screen
    def draw(self):
        pygame.draw.circle(self.surface,self.color,self.pos,self.radius,self.width)
circle=Circle((300,300),10,0)
circle.draw()
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()


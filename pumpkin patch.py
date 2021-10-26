import pygame, random, math

# PYGAME STUFF -----------------------------------------------------------------------------------------------
pygame.init()
(width, height) = (1200, 800)
screen = pygame.display.set_mode((width, height)) # creates pygame screen
pygame.display.set_caption('Pumpkin Patch')
clock = pygame.time.Clock()
bgColor = (33, 46, 22)


# CLASSES & FUNCTIONS ----------------------------------------------------------------------------------------
class pumpkin: # BALL OBJECT CLASS --------------------------------------------------------------------------
    def __init__(self, x, y, choice):
        self.x = x
        self.y = y
        if choice <= 3: # orange pumpkin
            self.color = (138 +random.randint(-10,10), 23 +random.randint(-10,10), 17 +random.randint(-10,10))
            self.color2 = (138-22, 23-12, 17-10)
        elif choice <= 7: # red pumpkin
            self.color = (186 +random.randint(-10,10), 93 +random.randint(-10,10), 17 +random.randint(-10,10))
            self.color2 = (186-25, 93-18, 17-10)
        elif choice <= 9: # white pumpkin
            self.color = (181 +random.randint(-10,10), 160 +random.randint(-10,10), 150 +random.randint(-10,10))
            self.color2 = (181-20, 160-25, 150-25)
        elif choice <= 10: # blue pumpkin
            self.color = (72 +random.randint(-10,10), 81 +random.randint(-10,10), 122 +random.randint(-10,10))
            self.color2 = (72-12, 81-13, 122-15)
        else:
            print("! Error in color assignment !")
        
    def draw(self):
        pygame.draw.ellipse(screen, self.color, (self.x, self.y, 100, 80))
        pygame.draw.arc(screen, self.color2, (self.x+10, self.y-16, 110, 115), (5*math.pi)/6, (7*math.pi)/6, 5)
        pygame.draw.arc(screen, self.color2, (self.x+30, self.y-36, 110, 150), (5*math.pi)/6, (7*math.pi)/6, 5)
        pygame.draw.arc(screen, self.color2, (self.x-22, self.y-16, 110, 115), (11*math.pi)/6, (math.pi)/6, 5)
        pygame.draw.arc(screen, self.color2, (self.x-42, self.y-36, 110, 150), (11*math.pi)/6, (math.pi)/6, 5)
        pygame.draw.arc(screen, ((22, 100, 8)), (self.x+45, self.y-51, 110, 115), (5*math.pi)/6, (math.pi), 8)
        pygame.draw.ellipse(screen, ((0, 0, 0)), (self.x, self.y, 100, 80), 5)
       
       
# CREATE A SET AMOUNT OF PUMPKINS ----------------------------------------------------------------------------------
patch = [] # creates empty pumpkin list

for pump in range(15): # makes a number of pumpkins
    x = random.randint(20, width-120)
    y = random.randint(20, height-120)
    choice = random.randint(1, 10)
    patch.append(pumpkin(x, y, choice))
    

running = True # controls if program is running or not
while running: # GAME LOOP -----------------------------------------------------------------------------------
    
    # LOGIC --------------------------------------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # allows user to close the window
            running = False
    
    # RENDER -------------------------------------------------------------------------------------------------
    screen.fill(bgColor)
    
    for i, pumpkin in enumerate(patch):
        pumpkin.draw() # draws all pumpkins in the patch
    
    pygame.display.flip()

# END OF GAME LOOP -------------------------------------------------------------------------------------------
pygame.quit()
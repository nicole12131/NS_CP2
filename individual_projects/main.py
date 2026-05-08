import pygame 
import os 
import sys

pygame.font.init()

# Use proper path handling
font_path = os.path.join("individual_projects", "Darkbyte-4nly6.ttf")

white = (255, 64, 64)
w = 640
h = 480
screen = pygame.display.set_mode((w, h))
screen.fill((white))
running = 1



pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Skill System")

font = pygame.font.SysFont(None, 36)

WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
DARK = (50, 50, 50)
GREEN = (100, 200, 100)

class skipbutton:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self):
        pygame.draw.rect(screen, GRAY, self.rect)
        txt = font.render(self.text, True, DARK)
        screen.blit(txt, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)



skipbutton = False

# Function to check for skip (needs to be updated by input handler)
def check_skip():
    
    return skipbutton 

# 1. Start Cutscene
print("Dramatic Music Playing...") # Run: Dramatic Music

# 2. Prologue Section
if not check_skip():
    while running:
        screen.fill((white))

        pygame.display.flip()
    print("Prelude: A kingdom called ArisKatsia") # Display Text
    # pause(3) # Wait 3 seconds

# 3. Tragedy Section
if not check_skip():
    print("[Display Image: Slain King]")
    print("The last king lays slaughtered in front of the prince's eyes.")
    print("This is a trial about tragedy.")
    # pause(4)

# 4. Call to Action Section
if not check_skip():
    print("[Display Image: Destroyed Kingdom]")
    print("Now it's only up to you, our last prince, Zan.")
    # pause(3)

# 5. Ending Section
print("[Pan to Game Title: THE FINAL BLIGHT]")
# display_menu() 
print("Menu Displayed")

if skipbutton == True: 
    print(" wow")
    print('you have skipped the intro')
    print("Lets hope you know what your doing")
       #load new game into a csv

    
    
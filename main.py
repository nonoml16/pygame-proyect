import sys

from game import *
from spritesheet import *

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()

pygame.quit()
sys.exit()
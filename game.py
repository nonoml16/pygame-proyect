import random

from bomb import *
from diamond import *
from ground import *
from block import *
from player import *
from spritesheet import *
from config import *
from map import *
from wall import *
from water import *
from aquatic_suit import *


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.character_spritesheet = Spritesheet('assets/player/player2.png')
        self.terrain_spritesheet = Spritesheet('assets/grass_terrain.png')
        self.wall_spritesheet = Spritesheet('assets/wall_terrain.png')
        self.block_spritesheet = Spritesheet('assets/block_terrain.png')
        self.water_spritesheet = Spritesheet('assets/water_terrain.png')

    def createTilemap(self, map_object):
        diamond_positions = []
        bomb_positions = []
        aquatic_suit_position = []

        while len(diamond_positions) < 10:
            x = random.randint(0, len(map_object.data[0]) - 1)
            y = random.randint(0, len(map_object.data) - 1)

            if map_object.get_tile_at(x, y) not in ['B', 'A', 'W'] and (x, y) not in diamond_positions:
                diamond_positions.append((x, y))

        for pos in diamond_positions:
            Diamond(self, pos[0], pos[1])

        while len(bomb_positions) < 3:
            x = random.randint(0, len(map_object.data[0]) - 1)
            y = random.randint(0, len(map_object.data) - 1)

            if map_object.get_tile_at(x, y) not in ['B', 'A', 'W'] and (x, y) not in bomb_positions:
                bomb_positions.append((x, y))

        for pos in bomb_positions:
            Bomb(self, pos[0], pos[1])

        while len(aquatic_suit_position) < 1:
            x = random.randint(0, len(map_object.data[0]) - 1)
            y = random.randint(0, len(map_object.data) - 1)

            if map_object.get_tile_at(x, y) not in ['B', 'A', 'W'] and (x, y) not in aquatic_suit_position:
                aquatic_suit_position.append((x, y))

        for pos in aquatic_suit_position:
            AquaticSuit(self, pos[0], pos[1])

        for i, row in enumerate(map_object.data):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "W":
                    Wall(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "A":
                    Water(self, j, i)
                if column == "P":
                    Player(self, j, i)

    def new(self):

        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.LayeredUpdates()
        self.water = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.diamond = pygame.sprite.LayeredUpdates()

        map_object = Map('assets/map.txt')
        self.createTilemap(map_object)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        self.running = False

    def intro_screen(self):
        pass

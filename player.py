import math
import time

import pygame
from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.lives = 10
        self.diamonds_inventory = 0
        self.bombs_inventory = 0
        self.aquatic_suit_inventory = False

    def update(self):
        self.movement()
        self.animate()

        self.collide_diamond()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.collide_walls('x')
        self.collide_water('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.collide_walls('y')
        self.collide_water('y')

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.lives <= 0:
                    self.game.game_over()

                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                time.sleep(0.1)
                self.lives -= 1
                print('vidas =', self.lives)

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.width
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                time.sleep(0.1)
                self.lives -= 1
                print('vidas =', self.lives)
            if self.lives == 0:
                self.kill()
                self.game.playing = False

    def collide_walls(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.width
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
        if self.lives == 0:
            self.kill()
            self.game.playing = False

    def collide_water(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.water, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                time.sleep(0.1)
                self.lives -= 1
                print('vidas =', self.lives)

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.water, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.width
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                time.sleep(0.1)
                self.lives -= 1
                print('vidas =', self.lives)

    def collide_diamond(self):
        hits = pygame.sprite.spritecollide(self, self.game.diamond, True)
        if hits:
            self.diamonds_inventory += 1
            print('Diamantes: ', self.diamonds_inventory)

    def animate(self):
        down_animations = [self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(33, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(65, 0, self.width, self.height)]

        up_animations = [self.game.character_spritesheet.get_sprite(97, 0, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(129, 0, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(161, 0, self.width, self.height)]

        right_animations = [self.game.character_spritesheet.get_sprite(193, 0, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(225, 0, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(257, 0, self.width, self.height)]

        left_animations = [self.game.character_spritesheet.get_sprite(289, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(321, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(353, 0, self.width, self.height)]

        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(97, 0, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(193, 0, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(289, 0, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

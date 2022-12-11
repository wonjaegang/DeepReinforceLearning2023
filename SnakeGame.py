import pygame
import time
import itertools
import random
from collections import deque


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
XY_MAX = 800
GRID_NUM = 50
GRID_SIZE = int(XY_MAX / GRID_NUM)
screen = pygame.display.set_mode((XY_MAX, XY_MAX))
clock = pygame.time.Clock()
rate = 20


class Food:
    def __init__(self):
        self.location = []
        self.initialize_location()

    def displayGUI(self):
        pygame.draw.rect(screen, RED, (GRID_SIZE * self.location[0], GRID_SIZE * self.location[1], GRID_SIZE, GRID_SIZE))

    def initialize_location(self):
        self.location = [random.choice(range(GRID_NUM)), random.choice(range(GRID_NUM))]


class Snake:
    def __init__(self):
        self.direction = 4  # 1, 2, 3, 4 as top, left, bottom, right
        self.location = deque([[9, 20], [10, 20]])  # x, y, 좌상단이 0,0
        self.tail_location = self.location[0]  #

    def move(self):
        dx = (1 - self.direction % 2) * (self.direction - 3)
        dy = (self.direction % 2) * (self.direction - 2)
        x = self.location[-1][0] + dx
        y = self.location[-1][1] + dy

        self.location.append([x, y])
        self.tail_location = self.location.popleft()

    def check_collision(self):
        if not 0 <= self.location[-1][0] < GRID_NUM:
            return True
        elif not 0 <= self.location[-1][1] < GRID_NUM:
            return True
        else:
            if self.location[-1] in itertools.islice(self.location, 0, len(self.location) - 1):
                return True
            else:
                return False

    def grow(self):
        self.location.appendleft(self.tail_location)

    def displayGUI(self):
        for location in self.location:
            pygame.draw.rect(screen, BLACK, (GRID_SIZE * location[0], GRID_SIZE * location[1], GRID_SIZE, GRID_SIZE))


def main():
    snake = Snake()
    food = Food()
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if not snake.direction == 3:
                        snake.direction = 1
                        break
                elif event.key == pygame.K_LEFT:
                    if not snake.direction == 4:
                        snake.direction = 2
                        break
                elif event.key == pygame.K_DOWN:
                    if not snake.direction == 1:
                        snake.direction = 3
                        break
                elif event.key == pygame.K_RIGHT:
                    if not snake.direction == 2:
                        snake.direction = 4
                        break

        screen.fill(WHITE)

        snake.move()

        # snake 성장 여부 판정
        if snake.location[-1] == food.location:
            snake.grow()
            food.initialize_location()

        # snake 충돌 여부 판정
        if snake.check_collision():
            time.sleep(1)
            main()
            break

        food.displayGUI()
        snake.displayGUI()
        pygame.display.flip()
        clock.tick(rate)
        count += 1


if __name__ == '__main__':
    main()

import pygame
import time
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
rate = 10


class Map:
    def __init__(self):
        pass



class Snake:
    def __init__(self):
        self.direction = deque([4, 4])  # 1, 2, 3, 4 as top, left, bottom, right
        self.location = [[9, 20], [10, 20]]  # x, y, 좌상단이 0,0

    def move(self, direction):
        self.set_direction(direction)
        self.move_by_direction()

    def set_direction(self, direction):
        if not direction:  # 입력이 없으면
            direction = self.direction[-1]
        self.direction.popleft()
        self.direction.append(direction)

    def move_by_direction(self):
        for i, direction in enumerate(self.direction):
            dx = (1 - direction % 2) * (direction - 3)
            dy = (direction % 2) * (direction - 2)
            self.location[i][0] += dx
            self.location[i][1] += dy

    def check_collision(self):
        if not 0 <= self.location[-1][0] < GRID_NUM:
            return True
        elif not 0 <= self.location[-1][1] < GRID_NUM:
            return True
        else:
            if self.location[-1] in self.location[:-1]:
                return True
            else:
                return False

    def grow(self):  # 움직이기 전, 성장 후 움직임
        pass


    def displayGUI(self):
        for location in self.location:
            pygame.draw.rect(screen, BLACK, (GRID_SIZE * location[0], GRID_SIZE * location[1], GRID_SIZE, GRID_SIZE))


def main():
    snake = Snake()
    while True:
        input_direction = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    input_direction = 1
                elif event.key == pygame.K_LEFT:
                    input_direction = 2
                elif event.key == pygame.K_DOWN:
                    input_direction = 3
                elif event.key == pygame.K_RIGHT:
                    input_direction = 4

        screen.fill(WHITE)

        snake.move(input_direction)
        if snake.check_collision():
            time.sleep(2)
            main()
            break

        snake.displayGUI()
        pygame.display.flip()
        clock.tick(rate)


if __name__ == '__main__':
    main()

import pygame as pg
from random import randrange

window = 1000
tilesize = 50
range = (tilesize // 2, window - tilesize // 2, tilesize)
getrandpos = lambda:[randrange(*range), randrange(*range)]
snake = pg.rect.Rect([0,0,tilesize-2, tilesize-2])
snake.center = getrandpos()
lengths = 1
snake_dir = (0,0)
time, time_step = 0,60
segments = [snake.copy()]
food = snake.copy()
food.center = getrandpos()
screen = pg.display.set_mode([window]*2)
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                snake_dir = (0, -tilesize)
            if event.key == pg.K_s:
                snake_dir = (0,tilesize)
            if event.key == pg.K_a:
                snake_dir = (-tilesize, 0)
            if event.key == pg.K_d:
                snake_dir = (tilesize,0)
        screen.fill('black')

        self_eat = pg.Rect.collidelist(snake, segments[:-1]) != -1
        if self_eat == 1:
            snake.center, food.center = getrandpos(), getrandpos()
            snake_dir = (0,0)
            lengths = 1
            segments = [snake.copy()]
        if snake.center == food.center:
            food.center = getrandpos()
            lengths += 1
        [pg.draw.rect(screen, 'green', segment)for segment in segments]

        pg.draw.rect(screen, 'red', food)


        time_now = pg.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snake.move_ip(snake_dir)
            segments.append(snake.copy())
            segments = segments[-lengths:]
        pg.display.flip()
        clock.tick(60)

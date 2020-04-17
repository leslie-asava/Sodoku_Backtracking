import numpy as np
import pygame
import time
import os
import visualize
import random
pygame.init()
pygame.display.init
#Original
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
        
"""grid = [[0,3,0,6,0,8,9,0,5],
        [0,0,0,0,4,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,5,0,7],
        [0,0,0,7,0,5,0,1,0],
        [0,0,6,8,2,0,0,9,0],
        [0,6,0,0,0,0,0,7,0],
        [1,5,0,2,0,0,0,0,4],
        [2,0,0,0,1,4,0,0,0]]"""

color_grid = [1,1,1,0,0,0,1,1,1,
              1,1,1,0,0,0,1,1,1,
              1,1,1,0,0,0,1,1,1,
              0,0,0,1,1,1,0,0,0,
              0,0,0,1,1,1,0,0,0,
              0,0,0,1,1,1,0,0,0,
              1,1,1,0,0,0,1,1,1,
              1,1,1,0,0,0,1,1,1,
              1,1,1,0,0,0,1,1,1]

display_grid = []
for y in grid:
        for x in y:
            display_grid.append(x)

def possible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

BACKGROUND_COLOR = (130,130,130)

screen = pygame.display.set_mode((1000,750))
screen.fill(BACKGROUND_COLOR)
font = pygame.font.Font('freesansbold.ttf', 40)
title_font = pygame.font.Font('freesansbold.ttf', 60)
stats_font = pygame.font.Font('freesansbold.ttf', 15)
cell_start_y = 100
cell_start_x = 220
square_length = 50
spacing = 2
cell_y = cell_start_y
cell_coordinates = []
font_coordinates = []
color_values = []

pygame.draw.rect(screen,(0,0,0),(cell_start_x+48,cell_start_y-4,474,475))
pygame.draw.rect(screen,BACKGROUND_COLOR,(30,cell_start_y+20,220,120))
title = title_font.render("Sudoku [BOT]", True, (0,0,0), BACKGROUND_COLOR)
algorthm = stats_font.render("ALGORITHM :  Backtracking", True, (255,255,255), BACKGROUND_COLOR)
start_time = stats_font.render("START TIME  :  "+time.strftime("%H:%M:%S"), True, (255,255,255),BACKGROUND_COLOR)
status = stats_font.render("STATUS          :  Solving", True, (255,255,255),BACKGROUND_COLOR)


screen.blit(title,(cell_start_x+80,16))
screen.blit(algorthm,(32,cell_start_y+40))
screen.blit(start_time,(32,cell_start_y+60))
screen.blit(status,(32,cell_start_y+80))

for i in color_grid:
    if i == 1:
        color_values.append((150,150,150))
    else:
        color_values.append((255,255,255))
for row in range(9):
    cell_x = cell_start_x
    for column in range(9):
        cell_x += square_length + spacing
        cell_coordinates.append((cell_x,cell_y,square_length,square_length))
        font_coordinates.append((cell_x+13,cell_y+8))
    cell_y += square_length + spacing
        
cells = [pygame.draw.rect(screen,color_values[i],cell_coordinates[i]) for i in range(81)]
display_grid = []
for y in grid:
    for x in y:
        display_grid.append(x)

values = [font.render(str(display_grid[i]), True, (0,0,0), color_values[i] ) for i in range(81)]
for i in range(81):
    screen.blit(values[i],font_coordinates[i])

pygame.display.flip()

def solve():
    global grid
    global cell_coordinates
    solved = []
    done = False

    display_grid = []
    for y in grid:
            for x in y:
                display_grid.append(x)

    values = [font.render(str(display_grid[i]), True, (0,0,0), color_values[i] ) for i in range(81)]
    
    interval = -1
    for y in range(9):
        for x in range(9):
            interval+=1
            if grid[y][x] != 0:
                screen.blit(values[interval],font_coordinates[interval])
            if grid[y][x] == 0:
                for n in range (1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        if random.choice([0,0,0,0,1]):
                            pygame.display.update(cell_coordinates[interval])
                        solve()
                        grid[y][x] = 0
                return
    for y in grid:
        for x in y:
            solved.append(x)
    solved = np.array(solved)
    solved = solved.reshape(9,9)
    print(solved)
    with open("solution.txt","w") as file:
        for row in solved:
            for number in row:
                file.write(str(number))
    try:
        pygame.display.quit()
    except:
        return


running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    try:
        solve()
    except:
        running = False

running = True
pygame.init()
pygame.display.init()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    visualize.main()

with open("solution.txt","w") as file:
    file.write("")
    
quit()
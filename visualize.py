def main():

  import pygame
  import time
  pygame.init()

  color_grid = [1,1,1,0,0,0,1,1,1,
                1,1,1,0,0,0,1,1,1,
                1,1,1,0,0,0,1,1,1,
                0,0,0,1,1,1,0,0,0,
                0,0,0,1,1,1,0,0,0,
                0,0,0,1,1,1,0,0,0,
                1,1,1,0,0,0,1,1,1,
                1,1,1,0,0,0,1,1,1,
                1,1,1,0,0,0,1,1,1]

  BACKGROUND_COLOR = (150,150,150)

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
  start_time = stats_font.render("STOP TIME    :  "+time.strftime("%H:%M:%S"), True, (255,255,255),BACKGROUND_COLOR)
  status = stats_font.render("STATUS          :  Solved", True, (255,255,255),BACKGROUND_COLOR)


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
  file = open("solution.txt","r")
  file = file.read()
  for i in file:
      display_grid.append(int(i))

  running = True

  values = [font.render(str(display_grid[i]), True, (0,0,0), color_values[i] ) for i in range(81)]
  for i in range(81):
      screen.blit(values[i],font_coordinates[i])
  pygame.display.flip()


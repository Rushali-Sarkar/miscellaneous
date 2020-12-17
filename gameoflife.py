""" 1) Any live cell with fewer than two live neighbours dies, as if by under population.
    2) Any live cell with two or three live neighbours lives on the next generation
    3) Any live cell with more than three live neighbours dies, as if by overpopulation.
    4) Any dead cell with exactly three live neighbours become a live cell as if by
       reprofuction. """

import random
import pygame
from time import sleep

ALIVE = "1"
DEAD = "0"

WHITE = (255, 255, 255)

PURPLE = (102, 0, 102)
GREEN = (0, 153, 0)
BLUE = (102, 0, 0)
PINK = (255, 0, 127)
YELLOW = (204, 204, 0)
BROWN = (153, 0, 0)

COLORS = [PURPLE, GREEN, BLUE, PINK, YELLOW, BROWN]

TOAD = [["0", "0", "0", "0", "0", "0"], \
        ["0", "0", "0", "0", "0", "0"], \
        ["0", "0", "1", "1", "1", "0"], \
        ["0", "1", "1", "1", "0", "0"], \
        ["0", "0", "0", "0", "0", "0"], \
        ["0", "0", "0", "0", "0", "0"]]

BEACON = [["0", "0", "0", "0", "0"], \
          ["0", "0", "1", "0", "0"], \
          ["0", "0", "1", "0", "0"], \
          ["0", "0", "1", "0", "0"], \
          ["0", "0", "0", "0", "0"]]

BLINKER = [["0", "0", "0", "0", "0", "0"], \
           ["0", "1", "1", "0", "0", "0"], \
           ["0", "1", "1", "0", "0", "0"], \
           ["0", "0", "0", "1", "1", "0"], \
           ["0", "0", "0", "1", "1", "0"], \
           ["0", "0", "0", "0", "0", "0"]]

GLIDER = [["0", "0", "0", "0", "0"], \
          ["0", "1", "0", "0", "0"], \
          ["0", "0", "1", "1", "0"], \
          ["0", "1", "1", "0", "0"], \
          ["0", "0", "0", "0", "0"]]

SPACESHIP = [["0", "0", "0", "0", "0", "0", "0", "0", "0"], \
             ["0", "0", "1", "0", "0", "1", "0", "0", "0"], \
             ["0", "0", "0", "0", "0", "0", "1", "0", "0"], \
             ["0", "0", "1", "0", "0", "0", "1", "0", "0"], \
             ["0", "0", "0", "1", "1", "1", "1", "0", "0"], \
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"], \
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"]]

PENTADECATHLON = [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"], \
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"], \
                  ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], \
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"], \
                  ["0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0"], \
                  ["0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0"], \
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"], \
                  ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], \
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"], \
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"], \
                  ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], \
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"], \
                  ["0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0"], \
                  ["0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0"], \
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"], \
                  ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], \
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"], \
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]




def make_random_grid(row: int, column: int) -> [str]:
    
    random_grid = []
    
    for rows in range(row):
        columns = []
        
        for cell in range(column):
            
            columns.append(random.choice([ALIVE, DEAD]))
        random_grid.append(columns)
        
    return random_grid


def add_sentinels(cell_grid: [str]) -> [str]:
    
    for row in cell_grid:
        row.insert(0, DEAD)
        row.append(DEAD)
        
    extra_row = list(DEAD * len(cell_grid[0]))
    cell_grid.insert(0, extra_row)
    cell_grid.append(extra_row)
    
    return cell_grid


def count_alive_neighbours(cell: str, smallest_grid: [str]) -> (int, int):
    
    alive_neighbours = sum([1 for row in smallest_grid for cell in row if cell == ALIVE])
    
    if cell == ALIVE:
        alive_neighbours = alive_neighbours - 1
        
    return alive_neighbours


def cell_state(cell: str, alive_neighbours: int) -> str:

    if cell == ALIVE and alive_neighbours < 2 or alive_neighbours > 3:
        return DEAD
    
    if cell == DEAD and alive_neighbours == 3:
        return ALIVE
    
    return cell



def remove_upper_add_lower(cell_grid: [str]) -> [str]:
    
        cell_grid = cell_grid[1: ]
        extra_row = list(DEAD * len(cell_grid[0]))
        cell_grid.append(extra_row)
        return cell_grid

def remove_left_add_right(cell_grid: [str]) -> [str]:
    
    for row_index, row in enumerate(cell_grid):
        cell_grid[row_index] = row[1: ]
        cell_grid[row_index].append(DEAD)

    return cell_grid

def remove_lower_add_upper(cell_grid: [str]) -> [str]:

    cell_grid = cell_grid[: len(cell_grid) -1]
    extra_row = list(DEAD * len(cell_grid[0]))
    cell_grid.append(extra_row)
    return cell_grid

def remove_right_add_left(cell_grid: [str]) -> [str]:

    for row_index, row in enumerate(cell_grid):
        cell_grid[row_index] = row [: len(row) - 1]
        cell_grid[row_index].insert(0, DEAD)

    return cell_grid

  
def next_generation(cell_grid: [str]) -> [str]:

    check_column_index = len(cell_grid[0])
    
    last_column = []
    first_column = []
    
    added_cell_grid = add_sentinels(cell_grid)
    next_generation_grid = []
    
    
    for row_index, row in enumerate(added_cell_grid[1: -1], start = 1):
        
        new_row = []
        
        for cell_index, cell in enumerate(row[1: -1], start = 1):
       
            smallest_grid = [added_cell_grid[row_index - 1][cell_index - 1: cell_index + 2], \
                             added_cell_grid[  row_index  ][cell_index - 1: cell_index + 2], \
                             added_cell_grid[row_index + 1][cell_index - 1: cell_index + 2]]
            
            alive_neighbours = count_alive_neighbours(cell, smallest_grid)
            current_state = cell_state(cell, alive_neighbours)
            new_row.append(current_state)

            if cell_index == 1:
                first_column.append(current_state)
                
            if cell_index == check_column_index:
                last_column.append(current_state)
        
        next_generation_grid.append(new_row)


    if ALIVE in last_column:
        next_generation_grid = remove_left_add_right(next_generation_grid)
   
    if ALIVE in next_generation_grid[-1]:
        next_generation_grid = remove_upper_add_lower(next_generation_grid)

    if ALIVE in first_column:
        next_generation_grid = remove_right_add_left(next_generation_grid)

    if ALIVE in next_generation_grid[0]:
        next_generation_grid = remove_lower_add_upper(next_generation_grid)
        
    return next_generation_grid


pygame.init()
height = 600
width = 600
screen = pygame.display.set_mode((width, height))
block_size = 30
screen.fill(WHITE)

def draw_square(x: int, y: int, color: (int)):
    
    left, top = x * block_size, y * block_size
    
    if color != WHITE:
        pygame.draw.rect(screen, WHITE, (top - 1, left - 1, block_size, block_size), 1)
        
    pygame.draw.rect(screen, color, (top, left, block_size, block_size))

        
def gameoflife(rows:int, columns: int):
    
    grid = make_random_grid(rows,columns)
    
    while True:
        
        
        color = random.choice(COLORS)
        for x in range(rows):
            for y in range(columns):
                
                cell = grid[x][y]
                cell_color = color if cell == ALIVE else WHITE
                draw_square(x, y, cell_color)
       
        grid = next_generation(grid)               
        pygame.display.flip()
    

        sleep(0.5)

    

gameoflife(20, 20)

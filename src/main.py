import random

from graphics import Window
from cell import Cell
from maze import Maze
from constants import (WINDOW_SIZE, MAZE_START_X, MAZE_START_Y, MAZE_CELL_SIZE_X, MAZE_CELL_SIZE_Y, MAZE_COLS, MAZE_ROWS, MAZE_COLOUR)

def main():
    win = Window(WINDOW_SIZE)
    maze = Maze(MAZE_START_X, MAZE_START_Y, MAZE_ROWS, MAZE_COLS, MAZE_CELL_SIZE_X, MAZE_CELL_SIZE_Y, MAZE_COLOUR, win)
    maze._create_cells()
    maze._break_entrance_and_exit()
    maze._break_walls_r()
    maze._reset_visited()
    print(maze.solve_maze("DFS"))
    print(maze.solve_maze("BFS"))
    print(maze.solve_maze("a_star"))
    win.wait_for_close()

main()
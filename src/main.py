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
    maze._break_walls()
    maze._reset_visited()
    print("Solving using DFS.")
    maze.solve("DFS", fill_colour = "green", offset = 0)
    maze._reset_visited()
    print("Solving using BFS.")
    maze.solve("BFS", fill_colour = "red", offset = 4)
    maze._reset_visited()
    # print(maze.solve("a_star", fill_colour = "blue", offset = -4))
    win.wait_for_close()

main()
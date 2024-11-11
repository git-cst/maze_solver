from graphics import Window, Cell, Line, Point

def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.draw(177, 100, 277, 200, "blue")
    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.draw(277, 100, 377, 200, "black")
    cell1.draw_move(cell2)
    win.wait_for_close()

main()
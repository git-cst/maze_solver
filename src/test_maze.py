import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._create_cells()

        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._create_cells()
        m1._break_entrance_and_exit()

        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[-1][-1].has_bottom_wall,
            False,
        )

    def test_reset_visited(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._create_cells()
        m1._break_entrance_and_exit()
        m1._break_walls_r()
        m1._reset_visited()

        visited_cell_present = False
        for i in range(0, num_rows):
            if visited_cell_present:
                break
            for j in range(0, num_cols):
                if m1._cells[i][j].visited == True:
                    visited_cell_present = True
                    break


        self.assertEqual(
            visited_cell_present,
            False,
        )

if __name__ == "__main__":
    unittest.main()
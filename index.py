from maze import Maze
from maze_gui import MazeGUI
# from maze_solver import MazeSolver

maze = Maze(row_column_amount = 50)
maze.generate()

maze_gui = MazeGUI(maze = maze, pixel_size = 15)
maze_gui.draw_maze()

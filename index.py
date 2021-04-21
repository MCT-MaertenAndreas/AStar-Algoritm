from maze import Maze
# from maze_solver import MazeSolver

maze = Maze(row_column_amount = 50)
maze.generate()

print(maze.nodes)

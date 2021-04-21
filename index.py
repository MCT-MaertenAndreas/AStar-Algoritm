from maze import Maze
from maze_gui import MazeGUI
from maze_solver import MazeSolver

maze = Maze(row_column_amount = 50)
maze_gui = MazeGUI(maze = maze, pixel_size = 15)
maze_solver = MazeSolver()

def callback(e):
    global maze, maze_gui, maze_solver

    if not maze.is_finished or (maze_solver.start and maze_solver.end):
        return

    node = maze.nodes[e.x // maze_gui.pixel_size][e.y // maze_gui.pixel_size]
    if node.is_wall:
        return

    if not maze_solver.start:
        maze_solver.start = node

        node.color = 'blue'
        maze_gui.draw_node(node)

        return

    node.color = 'green'
    maze_gui.draw_node(node)

    maze_solver.end = node

    # while maze_solver.step() == 0:
    #     maze_solver.backtrack()

    #     maze_gui.update()

maze_gui.canvas.bind("<Button-1>", callback)

maze.generate()
maze_gui.draw_maze()

from maze import Maze
from maze_solver import MazeSolver
from tqdm import tqdm

pixel_size = 15

maze = Maze(pixel_size = pixel_size, row_column_amount = 50)
maze.generate()

maze_solver = MazeSolver()

def callback(e):
    global maze, maze_solver

    if maze_solver.start and maze_solver.end:
        return

    node = maze.nodes[e.x // maze.pixel_size][e.y // maze.pixel_size]
    if node.is_wall:
        return

    if not maze_solver.start:
        node.color = 'blue'
        node.draw()

        maze_solver.start = node

        return
    node.color = 'green'
    node.draw()

    maze_solver.end = node

    progress = tqdm(total = maze.accessible_nodes)
    while maze_solver.step(True) == 0:
        maze_solver.backtrack()

        maze.canvas.update()

        progress.update(1)

maze.canvas.bind("<Button-1>", callback)

maze.draw_maze()

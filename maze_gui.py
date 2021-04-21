import tkinter as tk

class MazeGUI(object):
    def __init__(self, maze, pixel_size):
        self._maze = maze
        self._pixel_size = pixel_size

        self._window = tk.Tk()
        self._window.title("A* Maze Solver")

        self._canvas = tk.Canvas(
            self.window,
            width = self._pixel_size * self._maze.row_column_amount,
            height = self._pixel_size * self._maze.row_column_amount,
            bg = 'grey'
        )
        self._canvas.pack()

        self._canvas_objects = {}

    @property
    def canvas(self):
        return self._canvas

    @property
    def pixel_size(self):
        return self._pixel_size

    @property
    def window(self):
        return self._window

    def draw_node(self, node):
        node.draw(self.canvas, self.pixel_size)

    def draw_maze(self):
        for row in range(self._maze.row_column_amount):
            for column in range(self._maze.row_column_amount):
                self._maze.nodes[row][column].draw(self.canvas, self.pixel_size)

        self.window.mainloop()

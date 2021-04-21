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
    def window(self):
        return self._window

    def draw_node(self, node):
        if node in self._canvas_objects:
            self.canvas.delete(self._canvas_objects[node])

        canvas_obj = self.canvas.create_rectangle(
            node.x * self._pixel_size,
            node.y * self._pixel_size,
            node.x * self._pixel_size + self._pixel_size,
            node.y * self._pixel_size + self._pixel_size,
            fill = node.color
        )

        self._canvas_objects[node] = canvas_obj

    def draw_maze(self):
        for row in range(self._maze.row_column_amount):
            for column in range(self._maze.row_column_amount):
                self.draw_node(self._maze.nodes[row][column])

        self.window.mainloop()

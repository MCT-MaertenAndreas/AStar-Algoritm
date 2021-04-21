import tkinter as tk
from random import randint
from maze_node import MazeNode

class Maze(object):
    def __init__(self, row_column_amount, pixel_size):
        self.row_column_amount = row_column_amount
        self.pixel_size = pixel_size

        self.window = tk.Tk()
        self.window.title("Maze")

        self.canvas = tk.Canvas(
            self.window,
            width = pixel_size * row_column_amount,
            height = pixel_size * row_column_amount,
            bg = 'grey'
        )
        self.canvas.pack()

        # select a random starting point to start our maze generation
        self.start = (
            randint(1, row_column_amount - 1),
            randint(1, row_column_amount - 1)
        )

        self._accessible_nodes = 0
        self._is_finished = False
        self._visited_nodes = []

    @property
    def accessible_nodes(self):
        return self._accessible_nodes

    @property
    def is_finished(self):
        return self._is_finished

    def draw_maze(self):
        for row in range(self.row_column_amount):
            for col in range(self.row_column_amount):
                self.nodes[row][col].draw()

        self.window.mainloop()

    def generate(self):
        self.nodes = [[MazeNode(self, x, y) for y in range(self.row_column_amount)] for x in range(self.row_column_amount)]

        node = self.nodes[self.start[0]][self.start[1]]
        node.is_wall = False

        while not self.is_finished:
            accessible_nodes = node.get_accessible_nodes()

            if len(accessible_nodes) > 0:
                node = accessible_nodes[
                    randint(1, len(accessible_nodes)) - 1
                ]
                node.is_wall = False

                self._accessible_nodes += 1

                self._visited_nodes.append(node)
            if len(self._visited_nodes) == 0:
                self._is_finished = True
            elif len(accessible_nodes) == 0:
                node = self._visited_nodes.pop()


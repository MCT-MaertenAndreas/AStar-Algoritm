class MazeNode(object):
    def __init__(self, maze, x, y):
        self._maze = maze

        self._x = x
        self._y = y

        self._back_track = None
        self._obj = None
        self._has_backtrack = False

        self.f = 0
        self.g = 0
        self.h = 0
        self.previous = None

        self._pixel_size = maze.pixel_size
        self._row_column_size = maze.row_column_amount

        self.color = 'white'
        self.neighbors = []
        self.is_wall = True

    @property
    def position(self):
        return (self._x, self._y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def center(self):
        return (
            self.x * self._pixel_size + self._pixel_size // 2,
            self.y * self._pixel_size + self._pixel_size // 2
        )

    def draw(self, fill = None):
        if self._obj:
            if self._has_backtrack:
                self._has_backtrack = False

                self._maze.canvas.delete(self._back_track)
            if fill == self._maze.canvas.itemcget(self._obj, 'fill'):
                return
            self._maze.canvas.delete(self._obj)

        self._obj = self._maze.canvas.create_rectangle(
            self._x * self._pixel_size,
            self._y * self._pixel_size,
            self._x * self._pixel_size + self._pixel_size,
            self._y * self._pixel_size + self._pixel_size,
            fill = fill if fill else 'black' if self.is_wall else self.color
        )

    def draw_line(self, **kwargs):
        if self.previous:
            prev_x, prev_y = self.previous.center
            x, y = self.center

            if self._back_track:
                self._maze.canvas.delete(self._back_track)

            self._has_backtrack = True
            self._back_track = self._maze.canvas.create_line(
                prev_x,
                prev_y,
                x,
                y,
                **kwargs
            )

    def get_accessible_nodes(self):
        neighbours = self.get_neighbouring()

        visitable_neighbours = []
        for node_group in neighbours:
            if (node_group[0] and node_group[0].x > 0
            and node_group[0].x < self._maze.row_column_amount - 1
            and node_group[0].y > 0
            and node_group[0].y < self._maze.row_column_amount - 1):
                if (node_group[1].is_wall
                and node_group[2].is_wall
                and node_group[3].is_wall
                and node_group[4].is_wall
                and node_group[5].is_wall):
                    visitable_neighbours.append(node_group[0])
        return visitable_neighbours

    def get_direct_neighbours(self):
        return [node_group[0] for node_group in self.get_neighbouring()]

    # Get all direct neighbouring and their direct neigbours
    def get_neighbouring(self):
        if len(self.neighbors) == 0:
            self.update_neighboring_nodes()
        return self.neighbors

    # Gets neigbouring nodes relative to the grid position of this one
    def get_rel(self, row, column):
        try:
            return self._maze.nodes[self._x + row][self._y + column]
        except:
            return None

    def update_neighboring_nodes(self):
        self.neighbors = [
            [self.get_rel(0, -1), self.get_rel(-1, -2), self.get_rel(0, -2), self.get_rel(1, -2), self.get_rel(-1, -1), self.get_rel(1, -1)], #left
            [self.get_rel(0, 1), self.get_rel(-1, 2), self.get_rel(0, 2), self.get_rel(1, 2), self.get_rel(-1, 1), self.get_rel(1, 1)], #right
            [self.get_rel(-1, 0), self.get_rel(-2, -1), self.get_rel(-2, 0), self.get_rel(-2, 1), self.get_rel(-1, -1), self.get_rel(-1, 1)], #top
            [self.get_rel(1, 0), self.get_rel(2, -1), self.get_rel(2, 0), self.get_rel(2, 1), self.get_rel(1, -1), self.get_rel(1, 1)] #bottom
        ]

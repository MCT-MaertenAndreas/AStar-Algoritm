class MazeNode(object):
    def __init__(self, maze, x, y):
        self._maze = maze

        self._x = x
        self._y = y

        self._color = None
        self._is_wall = True
        self._neighbours = []

        self._canvas_obj = None

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        if not self._color:
            self._color = 'black' if self._is_wall else 'white'
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def is_wall(self):
        return self._is_wall

    @is_wall.setter
    def is_wall(self, value):
        self._is_wall = value

    def draw(self, canvas, pixel_size):
        if self._canvas_obj:
            canvas.delete(self._canvas_obj)

        self._canvas_obj = canvas.create_rectangle(
            self.x * pixel_size,
            self.y * pixel_size,
            self.x * pixel_size + pixel_size,
            self.y * pixel_size + pixel_size,
            fill = self.color
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

    # Get all neighbouring and their neigbours
    def get_neighbouring(self):
        if len(self._neighbours) == 0:
            self.update_neighboring_nodes()
        return self._neighbours

    # Gets neigbouring nodes relative to the grid position of this one
    def get_rel(self, row, column):
        try:
            return self._maze.nodes[self._x + row][self._y + column]
        except:
            return None

    def update_neighboring_nodes(self):
        self._neighbours = [
            [self.get_rel(0, -1), self.get_rel(-1, -2), self.get_rel(0, -2), self.get_rel(1, -2), self.get_rel(-1, -1), self.get_rel(1, -1)], #left
            [self.get_rel(0, 1), self.get_rel(-1, 2), self.get_rel(0, 2), self.get_rel(1, 2), self.get_rel(-1, 1), self.get_rel(1, 1)], #right
            [self.get_rel(-1, 0), self.get_rel(-2, -1), self.get_rel(-2, 0), self.get_rel(-2, 1), self.get_rel(-1, -1), self.get_rel(-1, 1)], #top
            [self.get_rel(1, 0), self.get_rel(2, -1), self.get_rel(2, 0), self.get_rel(2, 1), self.get_rel(1, -1), self.get_rel(1, 1)] #bottom
        ]

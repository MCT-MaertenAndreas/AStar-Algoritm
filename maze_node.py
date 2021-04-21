class MazeNode(object):
    def __init__(self, maze, x, y):
        self.maze = maze

        self.x = x
        self.y = y

        self._neighbours = []

    def get_accessible_nodes(self):
        neighbours = self.get_neighbouring()

        visitable_neighbours = []
        for node_group in neighbours:
            if (node_group[0] and node_group[0].x > 0
            and node_group[0].x < self._row_column_size - 1
            and node_group[0].y > 0
            and node_group[0].y < self._row_column_size - 1):
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
    def get_rel(self, x, y):
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

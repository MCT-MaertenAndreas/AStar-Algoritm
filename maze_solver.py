from numpy import sqrt

"""
A* algorithm
"""
class MazeSolver(object):
    def __init__(self):
        self.open_set = []
        self.closed_set = {}

        self._start = None
        self.end = None

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self.last_checked_node = value

        self.current = value
        self._start = value

        self.open_set.append(value)

    def backtrack(self):
        path = []
        temp = self.current
        path.append(temp)
        while temp.previous:
            path.append(temp.previous)
            temp = temp.previous
        for node in path:
            node.draw_line(fill='magenta', width=3)

    def heuristic(self, a, b):
        return sqrt((a.x-b.x)**2 + (a.y-b.y)**2)

    def remove_from_array(self, arr, elt):
        if elt in arr: arr.remove(elt)

    def step(self, showoc=False):
        # show open and closed list
        if showoc:
            for node in self.open_set:
                node.draw(fill='yellow')
            for node in self.closed_set.keys():
                node.draw(fill='red')
        else:
            for node in self.closed_set.keys():
                node.draw(fill='white')

        if len(self.open_set) > 0:
            winner = 0
            for i in range(1, len(self.open_set)):
                if self.open_set[i].f < self.open_set[winner].f:
                    winner = i
                if self.open_set[i].f == self.open_set[winner].f:
                    if self.open_set[i].g > self.open_set[winner].g:
                        winner = i

            self.current = self.open_set[winner]
            self.last_checked_node = self.current

            if self.current == self.end:
                self.start.draw()
                self.end.draw()

                self.backtrack()

                return 1

            self.remove_from_array(self.open_set, self.current)
            self.closed_set[self.current] = True

            neighbors = self.current.get_direct_neighbours()

            for neighbor in neighbors:
                if neighbor and neighbor not in self.closed_set and not neighbor.is_wall:
                    tempG = self.current.g + self.heuristic(neighbor, self.current)

                    if not neighbor in self.open_set:
                        self.open_set.append(neighbor)
                    elif tempG >= neighbor.g:
                        continue

                    neighbor.g = tempG
                    neighbor.h = self.heuristic(neighbor, self.end)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.previous = self.current

            return 0
        else:
            return -1

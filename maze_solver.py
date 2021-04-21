from numpy import sqrt

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

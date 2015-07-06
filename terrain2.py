import numpy as np

class Area(object):
    def __init__(self, parent=None, parent_index=None):
        self._parent = parent
        self._children = None
        self._altitude = None
        self._neighbours = None
        self.parent_index = parent_index

    @property
    def children(self):
        if self._children is None:
            self._children = [Area(parent=self, parent_index=i)
                              for i in range(4)]
        return self._children

    @property
    def parent(self):
        if self._parent is None:
            self._parent = Area()
            index = np.random.randint(4)
            self._parent.children[index] = self
            self.parent_index = index
        return self._parent

    @property
    def neighbours(self):
        if self._neighbours is None:
            distances = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            self._neighbours = [self.get_area(*delta) for delta in distances]
        return self._neighbours

    def get_area(self, dx, dy):
        offsets = [(-0.25, -0.25), (0.25, -0.25), (-0.25, 0.25), (0.25, 0.25)]
        scale = 0.5
        area = self
        depth = 0
        while abs(dx) > 0.5 or abs(dy) > 0.5:
            parent = area.parent
            offset = offsets[area.parent_index]
            dx = dx * scale + offset[0]
            dy = dy * scale + offset[1]
            depth += 1
            area = parent
        return area.get_child(dx, dy, depth)

    def get_child(self, x, y, depth):
        if depth == 0:
            return self
        assert abs(x) < 0.5
        assert abs(y) < 0.5

        xx = x * 2 + 0.5
        index = 0
        if x > 0:
            index += 1
            xx -= 1.0
        yy = y * 2 + 0.5
        if y > 0:
            index += 2
            yy -= 1.0

        return self.children[index].get_child(xx, yy, depth - 1)


if __name__ == '__main__':
    #np.random.seed(1)
    a = Area()

    print a
    for n in a.neighbours:
        print n.neighbours

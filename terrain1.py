import sample

class Area(object):
    def __init__(self, rng, altitude, ruggedness):
        self.rng = rng
        self.altitude = altitude
        self.ruggedness = ruggedness
        self.subs = None

    def generate_subs(self):
        alts = sample.sample_to_sum(self.rng, self.altitude,
                                    self.ruggedness, 4)
        #rugg = sample.sample_to_sum(self.rng, self.ruggedness * 4 / 2,
        #                            0.2 * self.ruggedness, 4)
        rugg = sample.sample_to_sum(self.rng, self.ruggedness * 4 / 3,
                                    0.0 * self.ruggedness, 4)
        self.subs = [Area(self.rng, alts[i], rugg[i]) for i in range(4)]

    def get_sub(self, x, y, depth):
        if depth == 0:
            return self

        i = int(x / 0.5)
        j = int(y / 0.5)
        index = (i * 2 + j) % 4
        xx = (x % 0.5) * 2
        yy = (y % 0.5) * 2

        if self.subs is None:
            self.generate_subs()
        return self.subs[index].get_sub(xx, yy, depth - 1)


if __name__ == '__main__':
    import numpy as np

    world = Area(np.random.RandomState(seed=1), 0, 0.1)

    depth = 6
    map = np.zeros((2**depth, 2**depth))

    pts = np.linspace(0, 1, 2**depth + 1)
    for i in range(2**depth):
        for j in range(2**depth):
            map[i, j] = world.get_sub(pts[i], pts[j], depth).altitude

    import pylab
    pylab.imshow(map, interpolation='nearest', cmap='gray')#, vmin=-1, vmax=1)
    pylab.show()







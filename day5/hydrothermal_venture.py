class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __parallell_line_to(self, x, y):
        line_points = [self]

        if x == self.x:
            dy = y - self.y
            if dy < 0:
                for yi in range(dy, 0):
                    line_points.append(Point(x, self.y + yi))
            else:
                for yi in range(1, dy + 1):
                    line_points.append(Point(x, self.y + yi))

        elif y == self.y:
            dx = x - self.x
            if dx < 0:
                for xi in range(dx, 0):
                    line_points.append(Point(self.x + xi, y))
            else:   
                for xi in range(1, dx + 1):
                    line_points.append(Point(self.x + xi, y))

        return line_points

    def __diagonal_line_to(self, x, y):
        line_points = [self]
        dx = x - self.x
        dy = y - self.y

        for step in range(1, abs(dx) + 1):
            line_points.append(Point(self.x + (step*dx/abs(dx)),
                                        self.y + (step*dy/abs(dy))))

        return line_points

    def line_to_point(self, Point):
        if self.parallell(self, Point):
            return self.__parallell_line_to(Point.x, Point.y)
        elif self.diagonal(self, Point):
            return self.__diagonal_line_to(Point.x, Point.y)

    @staticmethod
    def parallell(p1, p2):
        return p1.x == p2.x or p1.y == p2.y
        #return self.x == Point.x or self.y == Point.y

    @staticmethod
    def diagonal(p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        return abs(dx) == abs(dy)

    # Pythons version of toString!
    def __str__(self):
        return f"({self.x}, {self.y})" 

    # Override "equals" function to allow  for "Point == Point" notation!!
    def __eq__(self, other): 
        return self.x == other.x and self.y == other.y

    # Guarantee(?) unique hashes via "key tuples"! Tuples are immutable -->
    #                                              each unique pairing will have
    #                                              a unique hash code when
    #                                              hash() is called on the tuple.
    def __key(self):
        return (self.x, self.y)

    # Make instances of the class "hashable" ???
    def __hash__(self):
        return hash(self.__key())
    

def main(point_pairs):
    # get horizontal, vertical and diagonal lines:
    filtered_point_pairs = list(filter(lambda p: Point.parallell(p[0], p[1]) or Point.diagonal(p[0], p[1]), point_pairs))

    lines = [p[0].line_to_point(p[1]) for p in filtered_point_pairs]

    point_occurences = {}

    for line in lines:
        for point in line:
            if point in point_occurences.keys():
                point_occurences.update({point : point_occurences.get(point) + 1})
            else:
                point_occurences.update({point : 1})

    overlaps = list(filter(lambda x: x >= 2, list(point_occurences.values())))
    print(len(overlaps))

if __name__ == "__main__":
    INPUT = "day5/input.txt"
    with open(INPUT, 'r') as f:
        coord_pairs = []
        for line in f:
            coord_pairs.append([coord.split(',') for coord in line.strip('\n').split(' -> ')])

        point_pairs = []
        for i in range(len(coord_pairs)):
            x1 = int(coord_pairs[i][0][0])
            y1 = int(coord_pairs[i][0][1])
            x2 = int(coord_pairs[i][1][0])
            y2 = int(coord_pairs[i][1][1])
            pair = [Point(x1, y1), Point(x2, y2)]
            point_pairs.append(pair)

        main(point_pairs)
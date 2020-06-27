from sys import maxsize


class Node:
    def __init__(self, cost, pos):
        self.cost = cost
        self.len = maxsize
        self.before = None
        self.pos = pos
        self.visted = False

    def __lt__(self, other):
        return self.len < other.len

    def __gt__(self, other):
        return self.len > other.len

    def __eq__(self, other):
        return self.len == other.len


class Graph:
    def __init__(self, map):
        self.list = []
        self.map = []
        self.end = None
        self.start = None
        start_found = 0
        for y in range(len(map)):
            r = []
            for x in range(len(map[0])):
                node = Node(map[y][x], (x, y))
                if node.cost == 0 and not start_found:
                    self.start = node
                    node.len = 0
                    start_found = 1
                elif node.cost == 0 and start_found:
                    self.end = node
                r.append(node)
                self.list.append(node)
            self.map.append(r)
        self.list.sort()

    def extract_min(self):
        node = self.list.pop(0)
        self.list.sort()
        return node

    def neighbours(self, pos):
        exit_l = []
        directions = [(-1, 0), (0, 1), (1, 0),  (0, -1)]
        for direction in directions:
            y = pos[1] + direction[1]
            x = pos[0] + direction[0]
            if y >= len(self.map) or y < 0:
                continue
            if x >= len(self.map[0]) or x < 0:
                continue
            if not self.map[y][x].visted:
                exit_l.append(self.map[y][x])
        return exit_l

    def dijkstra(self):
        while len(self.list) != 0:
            u = self.extract_min()
            u.visted = True
            for n in self.neighbours(u.pos):
                new_dist = u.len + n.cost
                if n.len > new_dist:
                    n.len = new_dist
                    n.before = u
                    self.list.sort()
        node = self.end
        self.path = []
        while node.before is not None:
            self.path.append(node)
            node = node.before
        self.path.append(self.start)

    def print_result(self):
        print("")
        poss = [p.pos for p in self.path]
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if (x, y) in poss:
                    print(self.map[y][x].cost, end='')
                else:
                    print("-", end='')
            print('')
        print(f"Distance: {self.end.len}")


def load_map(filename):
    exit_map = []
    with open(filename) as fn:
        lines = fn.readlines()
        for line in lines:
            row = []
            for num in line[:-1]:
                row.append(int(num))
            exit_map.append(row)
    return exit_map


def show_map(map_to_show):
    for line in map_to_show:
        for num in line:
            print(num, end='')
        print("\n", end='')


def main():
    my_map = load_map("test6.txt")
    show_map(my_map)
    g = Graph(my_map)
    g.dijkstra()
    g.print_result()


if __name__ == "__main__":
    main()

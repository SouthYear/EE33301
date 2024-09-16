import sys


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0 for _ in range(num_vertices)]
                           for _ in range(num_vertices)]

    def display_mst(self, parents):
        print("Edge \tWeight")
        for i in range(1, self.num_vertices):
            print(parents[i], "-", i, "\t", self.adj_matrix[i][parents[i]])

    def find_min_key(self, keys, included_in_mst):
        min_value = sys.maxsize
        min_index = -1

        for v in range(self.num_vertices):
            if keys[v] < min_value and not included_in_mst[v]:
                min_value = keys[v]
                min_index = v

        return min_index

    def prims_algorithm(self):
        keys = [sys.maxsize] * self.num_vertices
        parents = [None] * self.num_vertices
        included_in_mst = [False] * self.num_vertices

        keys[0] = 0
        parents[0] = -1

        for _ in range(self.num_vertices):
            u = self.find_min_key(keys, included_in_mst)
            included_in_mst[u] = True

            for v in range(self.num_vertices):
                if (self.adj_matrix[u][v] > 0 and not included_in_mst[v] and
                        keys[v] > self.adj_matrix[u][v]):
                    keys[v] = self.adj_matrix[u][v]
                    parents[v] = u

        self.display_mst(parents)


if __name__ == '__main__':
    graph = Graph(6)
    graph.adj_matrix = [
        [0, 16, 0, 0, 19, 21],
        [16, 0, 6, 5, 0, 11],
        [0, 6, 0, 10, 0, 0],
        [0, 5, 10, 0, 18, 14],
        [19, 0, 0, 18, 0, 33],
        [21, 11, 0, 14, 33, 0],
    ]

    graph.prims_algorithm()

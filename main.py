from dataclasses import dataclass

@dataclass(frozen=True)
class Node:
    id: str
    x: int
    y: int


@dataclass(frozen=True)
class Edge:
    source: Node
    target: Node
    weight: int


class Graph:
    def __init__(self):
        self.edges = set()

    @property
    def nodes(self):
        nodes = []
        for edge in self.edges:
            nodes.extend([edge.source, edge.target])
        return set(nodes)

    def get_children(self, node):
        children = []
        for edge in self.edges:
            if edge.source == node:
                children.append(edge.target)

        return set(children)

    def get_parents(self, node):
        parents = []
        for edge in self.edges:
            if edge.target == node:
                parents.append(edge.source)

        return set(parents)

    def add_edge(self, source, target, weight=0):
        self.edges.add(Edge(source, target, weight))

    # pop index 0 BFS
    # pop index -1 DFS
    def _search(self, pop_index, node_id, starting_node=None):

        visited = set()
        to_visit = []

        def visit_node(node):
            print("visiting ", node)

            if node.id == node_id:
                print("Found!")
                return node

            visited.add(node)
            children = self.get_children(node)
            print("children ", children)

            not_visited_children = children - visited

            nonlocal to_visit
            to_visit.extend(not_visited_children)
            print("to visit ", to_visit)

            return None

        if starting_node is None:
            # Get a random starting node
            starting_node = self.nodes.pop()

        to_visit.append(starting_node)

        while len(to_visit) != 0:
            found = visit_node(to_visit.pop(pop_index))
            if found is not None:
                return found

        print("NOT FOUND!")
        return None

    def breadth_first_search(self, node_id, starting_node=None):
        return self._search(0, node_id, starting_node)

    def depth_first_search(self, node_id, starting_node=None):
        return self._search(-1, node_id, starting_node)

    def __str__(self):
        return str(self.nodes)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    g = Graph()

    node_a = Node('a', 1, 1)
    node_b = Node('b', 2, 2)
    node_c = Node('c', 3, 3)
    node_d = Node('d', 4, 4)
    node_e = Node('e', 4, 4)
    node_f = Node('f', 4, 4)
    node_g = Node('g', 4, 4)

    g.add_edge(node_a, node_b)
    g.add_edge(node_b, node_c)
    g.add_edge(node_c, node_d)

    g.add_edge(node_a, node_e)
    g.add_edge(node_e, node_f)
    g.add_edge(node_f, node_g)

    # Do a BFS on the graph stating on node a looking for node d
    print(g.breadth_first_search('d', node_a))

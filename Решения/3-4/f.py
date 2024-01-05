import argparse
import sys
import copy
import itertools
import random
import sys



def summarize_path(end, previous_nodes):
    route = []
    prev = end
    while prev:
        route.insert(0, prev)
        prev = previous_nodes[prev]
    return route


def find_cost(path, graph):
    start, end = path

    all_nodes = graph.node_keys
    unvisited = set(all_nodes)
    total_cost = graph.total_cost
    node_costs = {node: total_cost for node in all_nodes}
    node_costs[start] = 0  

    previous_nodes = {node: None for node in all_nodes}

    node = start
    while unvisited:  
        for option in graph.edge_options(node).values():
            next_node = option.end(node)
            if next_node not in unvisited:
                continue  
            
            if node_costs[next_node] > node_costs[node] + option.weight:
                node_costs[next_node] = node_costs[node] + option.weight
                previous_nodes[next_node] = node
        unvisited.remove(node)
        
        options = {k:v for k, v in node_costs.items() if k in unvisited}
        try:
            
            node = min(options, key=options.get)  
        except ValueError:  
            break
        if node == end:  
            break

    cost = node_costs[end]
    shortest_path = summarize_path(end, previous_nodes)

    return cost, shortest_path



def flatten_tuples(iterable):
    return sum(iterable, ())

def all_unique(iterable):
    
    seen = set()
    return not any(x in seen or seen.add(x) for x in iterable)


def fleury_walk(graph, start=None, circuit=False):
    visited = set()  

    
    node = start if start else random.choice(graph.node_keys)

    route = [node]
    while len(visited) < len(graph):
        
        reduced_graph = copy.deepcopy(graph)
        reduced_graph.remove_edges(visited)
        options = reduced_graph.edge_options(node)
        bridges = [k for k in options.keys() if reduced_graph.is_bridge(k)]
        non_bridges = [k for k in options.keys() if k not in bridges]
        if non_bridges:
            chosen_path = random.choice(non_bridges)
        elif bridges:
            chosen_path = random.choice(bridges)
        else:
            break  
        next_node = reduced_graph.edges[chosen_path].end(node)  

        visited.add(chosen_path)  

        route.append(next_node)
        node = next_node

    return route


def eularian_path(graph, start=None, circuit=False):
    for i in range(1, 1001):
        route = fleury_walk(graph, start, circuit)
        if len(route) == len(graph) + 1:  
            return route, i
    return [], i  


def find_dead_ends(graph):
    single_nodes = [k for k, order in graph.node_orders.items() if order == 1]
    return set([x for k in single_nodes for x in graph.edges.values() \
            if k in (x.head, x.tail)])


def build_node_pairs(graph):
    
    odd_nodes = graph.odd_nodes
    return [x for x in itertools.combinations(odd_nodes, 2)]


def build_path_sets(node_pairs, set_size):
    
    return (x for x in itertools.combinations(node_pairs, set_size) \
            if all_unique(sum(x, ())))


def unique_pairs(items):
    for item in items[1:]:
        pair = items[0], item
        leftovers = [a for a in items if a not in pair]
        if leftovers:
            
            for tail in unique_pairs(leftovers):
                yield [pair] + tail
            
            
        else:
            yield [pair]


def find_node_pair_solutions(node_pairs, graph):
    node_pair_solutions = {}
    for node_pair in node_pairs:
        if node_pair not in node_pair_solutions:
            cost, path = find_cost(node_pair, graph)
            node_pair_solutions[node_pair] = (cost, path)
            
            node_pair_solutions[node_pair[::-1]] = (cost, path[::-1])
    return node_pair_solutions


def build_min_set(node_solutions):
    odd_nodes = set([x for pair in node_solutions.keys() for x in pair])
    
    sorted_solutions = sorted(node_solutions.items(), key=lambda x:x[1][0])
    path_set = []
    for node_pair, solution in sorted_solutions:
        if not all(x in odd_nodes for x in node_pair):
            continue
        path_set.append((node_pair, solution))
        for node in node_pair:
            odd_nodes.remove(node)
        if not odd_nodes:  
            break
    return path_set


def find_minimum_path_set(pair_sets, pair_solutions):
    cheapest_set = None
    min_cost = float('inf')
    min_route = []
    for pair_set in pair_sets:
        set_cost = sum(pair_solutions[pair][0] for pair in pair_set)
        if set_cost < min_cost:
            cheapest_set = pair_set
            min_cost = set_cost
            min_route = [pair_solutions[pair][1] for pair in pair_set]

    return cheapest_set, min_route


def add_new_edges(graph, min_route):
    new_graph = copy.deepcopy(graph)
    for node in min_route:
        for i in range(len(node) - 1):
            start, end = node[i], node[i + 1]
            cost = graph.edge_cost(start, end)  
            new_graph.add_edge(start, end, cost, False)  
    return new_graph


def make_eularian(graph):
    dead_ends = [x.contents for x in find_dead_ends(graph)]
    graph.add_edges(dead_ends)  

    
    node_pairs = list(build_node_pairs(graph))
    

    
    pair_solutions = find_node_pair_solutions(node_pairs, graph)
    

    
    pair_sets = (x for x in unique_pairs(graph.odd_nodes))

    
    cheapest_set, min_route = find_minimum_path_set(pair_sets, pair_solutions)
    
    return add_new_edges(graph, min_route), len(dead_ends)  






def is_even(number):
    
    return not number % 2

class Graph(object):
    

    def __init__(self, data=None):
        self.edges = {}
        if data:  
            self.add_edges(data)

    def __repr__(self):
        return 'Graph({})'.format(str(self.edges))

    def add_edges(self, edges):
        
        for edge in edges:
            self.add_edge(*edge) 

    def add_edge(self, *args):
        
        self.edges[len(self.edges)] = Edge(*args)

    def remove_edges(self, edges):
        
        for edge in edges:
            if isinstance(edge, int):
                self.remove_edge(edge)
            else:
                self.remove_edge(*edge.contents)

    def remove_edge(self, *args):
        
        if len(args) == 1 and isinstance(args[0], int):
            del self.edges[args[0]]  
        else:
            match = self.find_edge(*args)  
            del self.edges[list(match.keys())[0]]  

    @property
    def nodes(self):
        
        return set([node for edge in self.edges.values() for node in (edge.head, edge.tail)])
    @property
    def node_keys(self):
        
        return sorted(self.nodes)

    @property
    def node_orders(self):
        
        return {x: len(self.edge_options(x)) for x in self.nodes}

    @property
    def odd_nodes(self):
        
        return [k for k in self.nodes if not is_even(self.node_orders[k])]

    def node_options(self, node):
        options = []
        for edge in self.edges.values():
            if edge.head == node:
                options.append(edge.tail)
            elif edge.tail == node:
                options.append(edge.head)
        return sorted(options)

    @property
    def is_eularian(self):
        
        return len(self.odd_nodes) == 0

    @property
    def is_semi_eularian(self):
        
        return len(self.odd_nodes) == 2

    @property
    def all_edges(self):
        
        return list(self.edges.values())

    def find_edges(self, head, tail, cost=None, directed=None):
        results = {}
        for key, edge in self.edges.items():
            if not cost and not directed:
                if (head, tail) == (edge.head, edge.tail) or \
                   (tail, head) == (edge.head, edge.tail):
                    results[key] = edge
            elif not directed:
                if (head, tail, cost) == edge or \
                   (tail, head, cost) == edge:
                    results[key] = edge
            else:
                if directed and (head, tail, cost, directed) == edge:
                    results[key] = edge
                elif (tail, head, cost, directed) == edge:
                    results[key] = edge
        return results

    def find_edge(self, head, tail, cost=None, directed=None):
        
        matches = self.find_edges(head, tail, cost, directed)
        return dict((matches.popitem(),))  

    def edge_options(self, node):
        
        return {k: v for k, v in self.edges.items() \
                if node in (v.head, v.tail)}

    def edge_cost(self, *args):
        
        weight = min([edge.weight for edge in self.find_edges(*args).values() if edge.weight])
        return weight

    @property
    def total_cost(self):
        
        return sum(x.weight for x in self.edges.values() if x.weight)

    def is_bridge(self, key):
        graph = copy.deepcopy(self)

        start = graph.edges[key].tail  

        graph.remove_edge(key)  

        stack = []
        visited = set()  
        while True:
            if start not in stack:
                stack.append(start)
            visited.add(start)
            nodes = [x for x in graph.node_options(start) \
                     if x not in visited]
            if nodes:
                start = nodes[0]  
            else:  
                try:
                    stack.pop()
                    start = stack[-1]  
                except IndexError:  
                    break

        if len(visited) == len(self.nodes):  
            return False  
        else:
            return True  

    def __len__(self):
        return len(self.edges)


class Edge(object):
    
    def __init__(self, head=None, tail=None, weight=0, directed=False):
        self.head = head  
        self.tail = tail  
        self.weight = weight  
        self.directed = directed  

    def __eq__(self, other):
        if len(other) == 3:
            other = other + (False,)  
        return (self.head, self.tail, self.weight, self.directed) == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.contents)

    def __repr__(self):
        return 'Edge({}, {}, {}, {})'.format(self.head, self.tail, self.weight, self.directed)

    def __len__(self):
        
        return len([x for x in (self.head, self.tail, self.weight, self.directed) if x is not None])

    def end(self, node):
        
        if node == self.head:
            return self.tail
        elif node == self.tail:
            return self.head
        else:
            raise ValueError('Node ({}) not in edge ({})'.format(node, self))

    @property
    def contents(self):
        
        return (self.head, self.tail, self.weight, self.directed)








def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))

    original_graph = Graph(edges)

    
    if not original_graph.is_eularian:
        
        graph, num_dead_ends = make_eularian(original_graph)
        
        
        
    else:
        graph = original_graph

    
    route, attempts = eularian_path(graph, start=1)
    if not route:
        pass
        
    else:
        
        
        ans = 0
        for i in range(1, len(route)):
            now = 999999999999999999999
            for a, b, w in edges:
                if (a == route[i] and b == route[i - 1]) or (a == route[i - 1] and b == route[i]):
                    if now > w:
                        now = w
            ans += now
        
        print(ans)


if __name__ == '__main__':
    main()

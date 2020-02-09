# Añadir los métodos del ejercicio 1
class Graph:
    def __init__(self):
        # {nodo: ({propiedades},{nodoP:{propiedades}})}
        self.vertex = {}
    
    @property
    def node(self):
        return {x: y[0] for x, y in self.vertex.items()}
    
    @property
    def edge(self):
        return {x: y[1] for x, y in self.vertex.items()}
    
    def nodes(self):
        return [x for x in self.vertex]
    
    def edges(self):
        return [(x,z) for x, y in self.vertex.items() for z in y[1] if x < z]
    
    def add_node(self, node, attr_dict=None):
        self.vertex[node] = ({} if attr_dict==None else attr_dict, {} if node not in self.vertex else self.vertex[node][1])
    
    def add_edge(self, node1, node2, attr_dict=None):
        if node1 not in self.vertex:
            self.add_node(node1)
        if node2 not in self.vertex:
            self.add_node(node2)
        self.vertex[node1][1][node2] = {} if attr_dict==None else attr_dict
        self.vertex[node2][1][node1] = {} if attr_dict==None else attr_dict
    
    def add_nodes_from(self, node_list, attr_dict=None):
        for i in node_list:
            self.add_node(i, attr_dict)
    
    def add_edges_from(self, edge_list, attr_dict=None):
        for i in edge_list:
            self.add_edge(i[0], i[1], attr_dict)
    
    def degree(self, node):
        return len(self.vertex[node][1]) 
    
    def __getitem__(self, node):
        return self.vertex[node][1]
    
    def __len__(self):
        return len(self.vertex)
    
    def neighbors(self, node):
        return [x for x in self.vertex[node][1]]
    
    def remove_node(self, node):
        if node in self.vertex:
            del self.vertex[node]
            for i in self.vertex:
                if node in self.vertex[i][1]:
                    del self.vertex[i][1][node]
    
    def remove_edge(self, node1, node2):
        if node1 in self.vertex[node2][1]:
            del self.vertex[node2][1][node1]
        if node2 in self.vertex[node1][1]:
            del self.vertex[node1][1][node2]
    
    def remove_nodes_from(self, node_list):
        for i in node_list:
            self.remove_node(i)
    
    def remove_edges_from(self, edge_list):
        for i in edge_list:
            self.remove_edge(i[0],i[1])    
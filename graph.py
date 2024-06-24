class Node:
    def __init__(self, id, x=0, y=0) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.edges = []
    
class Edge:
    def __init__(self, node1, node2, weight=1) -> None:
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
        
class Graph:
    def __init__(self) -> None:
        self.nodes = []
        self.edges = []
        
    def add_node(self, node: Node) -> bool:
        if node not in self.nodes:
            self.nodes.append(node)
            return True
        return False
    
    def add_edge(self, edge: Edge) -> bool:
        if edge not in self.edges:
            self.edges.append(edge)
            edge.node1.edges.append(edge)
            edge.node2.edges.append(edge)
            return True
        return False
    
    def remove_node(self, node: Node) -> bool:
        if node in self.nodes:
            self.nodes.remove(node)
            for edge in node.edges:
                self.edges.remove(edge)
                edge.node1.edges.remove(edge)
                edge.node2.edges.remove(edge)
            return True
        return False
    
    def remove_edge(self, edge: Edge) -> bool:
        if edge in self.edges:
            self.edges.remove(edge)
            edge.node1.edges.remove(edge)
            edge.node2.edges.remove(edge)
            return True
        return False
    
    def __index__(self, node_id: int) -> Node:
        for node in self.nodes:
            if node.id == node_id:
                return node
        return None
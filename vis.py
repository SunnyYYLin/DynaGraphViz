from graph import Graph, Node, Edge
import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsLineItem
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPen, QBrush

class GraphVisualizer(QGraphicsView):
    def __init__(self, graph):
        super().__init__()
        self.graph = graph
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Graph Visualizer")
        self.setGeometry(100, 100, 800, 600)
        self.setBackgroundBrush(QBrush(Qt.white))
        self.show()
        
        self.draw_graph()

    def draw_graph(self):
        for node in self.graph.nodes:
            # 每个节点绘制为一个圆
            ellipse = QGraphicsEllipseItem(node.x - 10, node.y - 10, 20, 20)
            ellipse.setBrush(QBrush(Qt.blue))
            self.scene.addItem(ellipse)
            node.graphics = ellipse  # 可选，保存图形项与节点的关联
            
        for edge in self.graph.edges:
            # 每条边绘制为一条线
            line = QGraphicsLineItem(edge.node1.x, edge.node1.y, edge.node2.x, edge.node2.y)
            pen = QPen(Qt.black)
            pen.setWidth(2)
            line.setPen(pen)
            self.scene.addItem(line)
            edge.graphics = line  # 可选，保存图形项与边的关联

# 示例代码：创建图并添加节点与边
if __name__ == '__main__':
    app = QApplication(sys.argv)

    graph = Graph()
    node1 = Node(1, 100, 150)
    node2 = Node(2, 200, 200)
    node3 = Node(3, 300, 250)
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    edge1 = Edge(node1, node2)
    edge2 = Edge(node2, node3)
    graph.add_edge(edge1)
    graph.add_edge(edge2)

    window = GraphVisualizer(graph)
    sys.exit(app.exec_())
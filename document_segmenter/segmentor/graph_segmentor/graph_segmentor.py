from ..base_segmentor import BaseSegmentor, Document, GraphSegment
from delone_binder import DeloneBinder, Edge, Node
from graph.graph import Graph
from typing import List, Dict, Tuple
from tesseract_reader import BBox


class GraphSegmentor(BaseSegmentor):
    def __init__(self, threshold=50):
        self.threshold: float = threshold

    def segmentation(self, doc: Document):

        graph = Graph()
        points, index_points = self.bboxes2points(doc.bboxes)
        for point in points:
            graph.add_node(point[0], point[1])

        edges = self.delone_process(points)

        for edge in edges:
            graph.add_edge(edge[0]+1, edge[1]+1)

        return [GraphSegment(r) for r in graph.get_related_graphs()]

    def delone_process(self, points: List[Tuple[float, float]]) -> List[Tuple[int, int]]:
        delone_binder = DeloneBinder()
        nodes = [Node(point[0], point[1]) for point in points]
        dict_nodes = dict()
        for i, node in enumerate(nodes):
            dict_nodes[node] = i

        edges, triangles = delone_binder.bind(nodes)

        new_edges = []
        for edge in edges:
            if edge.width < self.threshold:
                new_edges.append(edge)

        # add edge of word start and  word end
        for i in range(len(points)//2):
            new_edges.append(Edge(nodes[2 * i], nodes[2 * i + 1]))

        return [(dict_nodes[edge.node1], dict_nodes[edge.node2]) for edge in new_edges]

    def bboxes2points(self, bboxes: List[BBox]) -> Tuple[List[Tuple[float, float]], List[BBox]]:
        index_points = list()
        points = list()
        for i, bbox in enumerate(bboxes):
            y = round(bbox.y_top_left + bbox.height / 2)
            index_points.append(bbox)
            points.append((bbox.x_top_left, y))
            index_points.append(bbox)
            points.append((bbox.x_top_left + bbox.width, y))
        return points, index_points

from typing import List, Tuple

from .base_segment import BaseSegment
from graph.related_graph import RelatedGraph


class GraphSegment(BaseSegment):
    def __init__(self, r: RelatedGraph):
        self.graph: RelatedGraph = r

    def get_region(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        nodes = self.graph.get_nodes()
        x_array = [node.x for node in nodes]
        y_array = [node.y for node in nodes]
        x_left = round(min(x_array))
        y_top = round(min(y_array))
        x_right = round(max(x_array))
        y_bottom = round(max(y_array))
        return (x_left, y_top), (x_right, y_bottom)


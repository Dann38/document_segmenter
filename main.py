import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from document_segmenter.document.document import Document
from document_segmenter.segmentor.graph_segmentor.graph_segmentor import GraphSegmentor


# Image path /example_img/g03.jpeg
path_project = os.path.abspath(os.path.join(os.getcwd(), "."))
path_img = os.path.join(path_project, 'example_img', "g03.jpeg")

doc = Document(path_img)
graph_segmentor = GraphSegmentor(threshold=40)
# Objects

list_seg = graph_segmentor.segmentation(doc)

plt.imshow(doc.img)
color = ["g", "y", "k", "r"]
for i, seg in enumerate(list_seg):
    for node in seg.graph.get_nodes():
        plt.plot(node.x, node.y, "b.")

for i, seg in enumerate(list_seg):
    for edge in seg.graph.get_edges():
        x, y = edge.get_line()
        plt.plot(x, y, color[i%3])

for seg in list_seg:
    left_top, right_bottom = seg.get_region()
    width = right_bottom[0] - left_top[0] + 20
    height = right_bottom[1] - left_top[1] + 20
    left_top = (left_top[0] - 4, left_top[1] - 4)
    plt.gca().add_patch(Rectangle(left_top, width, height,
                                  edgecolor='red',
                                  facecolor='none',
                                  lw=2))
plt.show()

#
# # ЕDGE_WIDTH
# h_edges = [edge.width for edge in edges]
# print(len(edges))
# plt.hist(h_edges, bins=200)
# plt.show()

# # TRIANGLE AREA
# a_tr = [triangle.area for triangle in triangles]
# print(len(a_tr))
# plt.hist(a_tr, bins=100)
# plt.show()

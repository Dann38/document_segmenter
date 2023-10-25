import os
import matplotlib.pyplot as plt
from utils.tesseract_reader.image_reader.image_reader import ImageReader
from utils.tesseract_reader.tesseract_reader.tesseract_reader import TesseractReader, TesseractReaderConfig

from utils.delone_binder.delone_binder.delone_binder import DeloneBinder, Node, Edge


# Image path /example_img/g03.jpeg
path_project = os.path.abspath(os.path.join(os.getcwd(), "."))
path_img = os.path.join(path_project, 'example_img', "b01.jpeg")

# Objects
image_reader = ImageReader()
tesseract_config = TesseractReaderConfig()
tesseract_reader = TesseractReader(tesseract_config)
delone_binder = DeloneBinder()


img = image_reader.read(path_img)
bboxes = tesseract_reader.read(img)
points = []
for bbox in bboxes:
    y = round(bbox.y_top_left + bbox.height/2)
    points.append(Node(bbox.x_top_left, y))
    points.append(Node(bbox.x_top_left+bbox.width, y))

edges, triangles = delone_binder.bind(points)

plt.imshow(img)

new_edges  = []
for edge in edges:
    if edge.width < 252:
        new_edges.append(edge)

for i in range(len(bboxes)):
    new_edges.append(Edge(points[2*i], points[2*i+1]))

for edge in new_edges:
    x, y = edge.get_lines()
    plt.plot(x, y, "b")
    plt.plot(x, y, "ro")
plt.show()

# h_edges = [edge.width for edge in edges]
# print(len(edges))
# plt.hist(h_edges, bins=200)
# plt.show()
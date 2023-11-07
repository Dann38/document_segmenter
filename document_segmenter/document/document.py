from ..segment.base_segment import BaseSegment
from tesseract_reader import BBox, ImageReader, TesseractReader, TesseractReaderConfig
from typing import List


class Document:
    def __init__(self, path_img):
        image_reader = ImageReader()
        tesseract_config = TesseractReaderConfig()
        tesseract_reader = TesseractReader(tesseract_config)
        self.img = image_reader.read(path_img)
        self.bboxes: List[BBox] = tesseract_reader.read(self.img)
        self.segments: List[BaseSegment] = []

    def add_segment(self, segment: BaseSegment):
        self.segments.append(segment)

    def get_segments(self) -> List[BaseSegment]:
        return self.segments


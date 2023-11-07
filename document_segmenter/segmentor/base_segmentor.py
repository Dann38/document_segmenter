from abc import ABC, abstractmethod
from .. import Document
from .. import GraphSegment


class BaseSegmentor(ABC):
    @abstractmethod
    def segmentation(self, doc: Document):
        pass


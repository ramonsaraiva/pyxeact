import pyxel

from rx import Observer
from rx.subjects import Subject


class Engine:

    RESOLUTION = (256, 256)

    update_subject = Subject()
    draw_subject = Subject()

    def __init__(self, resolution=None):
        self.resolution = resolution or self.RESOLUTION
        pyxel.init(*self.resolution)

    @classmethod
    def update(cls):
        pyxel.cls(0)
        cls.update_subject.on_next(None)

    @classmethod
    def draw(cls):
        cls.draw_subject.on_next(None)

    def run(self):
        pyxel.run(self.update, self.draw)

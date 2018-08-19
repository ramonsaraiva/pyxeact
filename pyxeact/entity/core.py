from dataclasses import dataclass

from rx.subjects import Subject
from ..engine import Engine


@dataclass
class Position:
    x: int = 0
    y: int = 0


class Entity:

    components = []

    def __init__(self):
        self.subscriptions()
        self.position = Position()
        self.subject = Subject()

    def subscriptions(self):
        Engine.update_subject.subscribe(self.process_update)
        Engine.draw_subject.subscribe(self.draw)

    def process_update(self, value):
        self.subject.on_next(self)
        self.update()

    def update(self):
        pass

    def draw(self, value):
        pass

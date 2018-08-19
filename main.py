import pyxel

from pyxeact.engine import Engine
from pyxeact.entity import Entity
from pyxeact.scene import Scene
from pyxeact.physics import Physics


class player(Entity):

    def update(self):
        print('a')
        if pyxel.btn(pyxel.KEY_D):
            self.position.x += 1
        if pyxel.btn(pyxel.KEY_A):
            self.position.x -= 1

    def draw(self, value):
        pyxel.rect(
            self.position.x,
            self.position.y,
            self.position.x + 4,
            self.position.y + 4,
            4
        )


engine = Engine((100, 100))

scene = Scene()
physics = Physics()

player = scene.add_entity(Rect)

engine.run()

from rx.subjects import Subject


class Scene:

    def __init__(self):
        self.entities = []
        self.entities_subject = Subject()

    def add_entity(self, entity_class, *args, **kwargs):
        entity = entity_class(*args, **kwargs)
        self.entities.append(entity)
        entity.subject.subscribe(self.entity_updated)

    def entity_updated(self, entity):
        self.entities_subject.on_next(entity)

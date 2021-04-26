from snapsnare_api.repositories.dataclass_repository import DataclassRepository


class PropertyRepository(DataclassRepository):

    def __init__(self, connector):
        DataclassRepository.__init__(self, connector, 'application_properties')

    def find_by_name(self, name):
        return self.find_by(name=name)

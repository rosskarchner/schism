class SchismSite(object):

    def __init__(self, index, *storages):
        self.storages = storages
        self.index = index

    def list_objects(self, suffix=None):
        paths = []
        for storage in self.storages:
            for obj in storage.list_objects(suffix):
                paths.append(obj)
        return paths

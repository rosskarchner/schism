

class LayeredStorage(object):
    def __init__(self, stores=None):
        if stores is None:
            self.stores = []
        else:
            self.stores = stores

    def get_an_object(self, path_or_list):
        if isinstance(path_or_list, list):
            search_path = path_or_list
        else:
            search_path = [path_or_list]

        for path in search_path:
            for store in self.stores:
                pass



class LayeredStorage(object):
    def __init__(self, stores=[]):
        self.stores = []

    def get_an_object(self, path_or_list):
        if type(path_or_list) == list:
            search_path = path_or_list
        else:
            search_path = [path_or_list]

        for path in search_path:
            for store in self.stores:
                pass

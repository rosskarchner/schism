from base_storage import BaseStorage
import os
import glob


class FileSystem(BaseStorage):

    def __init__(self, path, **kwargs):
        self.path = path
        return super(FileSystem, self).__init__(self, **kwargs)

    def list_objects(self, suffix):
        for dirpath, dirnames, filenames in os.walk(self.path):
            for filename in filenames:
                if not suffix or filename.endswith(suffix):
                    yield os.path.join(dirpath, filename)

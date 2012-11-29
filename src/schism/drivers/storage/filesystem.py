from base_storage import BaseStorage
import os
import glob


class FileSystem(BaseStorage):

    def __init__(self, path, **kwargs):
        self.path = os.path.join('/opt/', '')
        return super(FileSystem, self).__init__(self, **kwargs)

    def select(self, pattern):
        complete_pattern = self.path + pattern

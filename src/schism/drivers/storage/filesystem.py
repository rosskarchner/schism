from base_storage import BaseStorage
import os


class FileSystem(BaseStorage):

    def __init__(self, path, **kwargs):
        self.path = path
        return super(FileSystem, self).__init__(self, **kwargs)

    def list_documents(self, suffix):
        for dirpath, dirnames, filenames in os.walk(self.path):
            for filename in filenames:
                if not suffix or filename.endswith(suffix):
                    relpath = os.path.relpath(dirpath, self.path)
                    yield os.path.join('/' + relpath, filename)

    def retrieve_document(self, path):
        absolute_path = os.path.join(self.path, path[1:])
        with file(absolute_path) as document:
            data = document.read()
            return data

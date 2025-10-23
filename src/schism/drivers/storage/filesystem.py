from .base_storage import BaseStorage
from schism.utility import unserialize_dates
import json
import os


class FileSystem(BaseStorage):

    def __init__(self, path, **kwargs):
        self.path = path
        super(FileSystem, self).__init__(**kwargs)

    def list_files(self, suffix):
        for dirpath, dirnames, filenames in os.walk(self.path):
            for filename in filenames:
                if not suffix or filename.endswith(suffix):
                    relpath = os.path.relpath(dirpath, self.path)
                    yield os.path.join('/' + relpath, filename)

    def retrieve_file(self, path):
        absolute_path = os.path.join(self.path, path[1:])
        with open(absolute_path) as document:
            data = document.read()
            return data

    def list_documents(self):
        documents = self.list_files('.json')
        return [document[:-5] for document in documents]

    def retrieve_document(self, path):
        data = self.retrieve_file(path + '.json')
        document = json.loads(data)
        annotated = unserialize_dates(document)
        annotated['id'] = path
        annotated['path'] = os.path.split(path)[0]
        # TODO: dual definitions of 'path' are confusing
        return annotated

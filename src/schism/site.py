class SchismSite(object):

    def __init__(self, index, *storages):
        self.storages = storages
        self.index = index

    def list_files(self, suffix=None):
        files = []
        for storage in self.storages:
            for obj in storage.list_files(suffix):
                files.append(obj)
        return files

    def list_documents(self):
        documents = []
        for storage in self.storages:
            for obj in storage.list_documents():
                documents.append(obj)
        return documents

    def retrieve_file(self, path):
        for storage in self.storages:
            found = storage.retrieve_file(path)
            if found is not None:  # TODO: exception if no documents found
                return found

    def retrieve_document(self, path):
        for storage in self.storages:
            found = storage.retrieve_document(path)
            if found is not None:
                return found

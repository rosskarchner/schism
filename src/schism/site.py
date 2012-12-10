class SchismSite(object):

    def __init__(self, index, *storages):
        self.storages = storages
        self.index = index

    def list_documents(self, suffix=None):
        documents = []
        for storage in self.storages:
            for obj in storage.list_documents(suffix):
                documents.append(obj)
        return documents

    def retrieve_document(self, path):
        for storage in self.storages:
            found = storage.retrieve_document(path)
            if found is not None:  # TODO: exception if no documents found
                return found

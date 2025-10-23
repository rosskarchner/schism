class BaseStorage(object):

    def __init__(self, *args, **kwargs):
        if 'hint' in kwargs:
            self.hint = kwargs['hint']
        else:
            self.hint = None

    def select(self, pattern):
        raise NotImplementedError

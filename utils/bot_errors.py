class RefValuesError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'class RefValuesError:, {self.message}'
        else:
            return 'RefValuesError has been raised, with out arguments.'


class AdminFindError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):

        if self.message:
            return f'class AdminFindError:, {self.message}'
        else:
            return 'AdminFindError has been raised, with out arguments.'

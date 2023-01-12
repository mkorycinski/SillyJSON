class NotExpectedType(Exception):
    def __init__(self, position=None):
        self.position = position

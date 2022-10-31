from .generic import GenericParser

class NullParser(GenericParser):
    def __init__(self):
        super(NullParser, self).__init__()

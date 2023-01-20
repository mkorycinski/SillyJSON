class NotExpectedType(Exception):
    def __init__(self, value: str):
        self.value = value
        self.msg = f'Not expected value: {self.value} encountered. JSON is malformed.'

    def __str__(self):
        return self.msg

    def __repr__(self):
        return f'<NotExpectedType: {self.value}>'

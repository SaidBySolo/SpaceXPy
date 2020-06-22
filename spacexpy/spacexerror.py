class SpaceXException(Exception):
    def __init__(self):
        super().__init__()

class UnexpectedArguments(SpaceXException):
    def __init__(self):
        super().__init__('An unexpected arguments has arrived.')
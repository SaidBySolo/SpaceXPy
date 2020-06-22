class SpaceXException(Exception):
    pass

class UnexpectedArguments(SpaceXException):
    def __init__(self, reason=None):
        super().__init__(f'An unexpected arguments has arrived. {reason}')
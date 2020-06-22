class SpaseXResponse:
    def __init__(self, response, rawdata: bool):
        if rawdata is True:
            self.data = response
        else:
            self.data = response[0]

    def __getattr__(self, attr):
        return self.data.get(attr)

    def __dict__(self):
        return self.data
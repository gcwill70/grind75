class TimeMap:
    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # make or create array
        if key in self.data:
            # check if entry is long enough
            if len(self.data[key]) < timestamp:
                self.data[key] += [""] * (timestamp - len(self.data[key]))
        else:
            # make new array
            self.data[key] = [""] * timestamp
        self.data[key][timestamp - 1] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            # clip the timestamp
            timestamp = min(timestamp, len(self.data[key]))
            # get element
            for i in range(timestamp - 1, -1, -1):
                if self.data[key][i] != "":
                    return self.data[key][i]
        return ""

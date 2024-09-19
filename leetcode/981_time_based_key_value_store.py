from collections import OrderedDict


class TimeMap:

    store = {}

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = OrderedDict()
            
        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]

        for t in reversed(values):
            if t <= timestamp:
                return values[t]

        return ""


if __name__ == "__main__":
    store = TimeMap()
    store.set("love", "high", 10)
    store.set("love", "low", 20)
    print(store.get("love",5))
    print(store.get("love",10))
    print(store.get("love",15))
    print(store.get("love",20))
    print(store.get("love",25))
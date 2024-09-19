from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.max_size = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    obj = LRUCache(11)
    param_1 = obj.get("sample")
    obj.put("aa", "bb")

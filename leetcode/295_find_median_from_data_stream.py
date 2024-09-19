from typing import List


class MedianFinder:

    def __init__(self):
        self.list = list()

    def addNum(self, num: int) -> None:
        if len(self.list) == 0:
            self.list.append(num)
            return

        for i in range(len(self.list)):
            if self.list[i] > num:
                self.list.insert(i, num)
                return
        self.list.append(num)
        pass

    def findMedian(self) -> float:
        if len(self.list) == 0:
            return None

        if len(self.list) % 2 == 0:
            return (self.list[(len(self.list) // 2) ] + self.list[(len(self.list) // 2) - 1]) /  2;
        else:
            return self.list[(len(self.list) // 2)]


if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    obj.addNum(3)
    obj.addNum(4)
    param_2 = obj.findMedian()
    print(param_2)

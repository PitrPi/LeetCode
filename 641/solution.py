class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.len = 0
        self.front = None
        self.back = None

    def insertFront(self, value: int) -> bool:
        if self.len >= self.k:
            return False
        node = Node(value)
        if self.len == 0:
            self.front = node
            self.back = self.front
        else:
            node.prev = self.front
            self.front.next = node
            self.front = node

        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.len >= self.k:
            return False
        node = Node(value)
        if self.len == 0:
            self.back = node
            self.front = self.back
        else:
            node.next = self.back
            self.back.prev = node
            self.back = node

        self.len += 1
        return True

    def deleteFront(self) -> bool:
        if self.len < 1:
            return False
        if self.len == 1:
            self.front = self.back = None
        else:
            self.front = self.front.prev
        self.len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.len < 1:
            return False
        if self.len == 1:
            self.front = self.back = None
        else:
            self.back = self.back.next
        self.len -= 1
        return True

    def getFront(self) -> int:
        if self.len < 1:
            return -1
        return self.front.val

    def getRear(self) -> int:
        if self.len < 1:
            return -1
        return self.back.val

    def isEmpty(self) -> bool:
        if self.len < 1:
            return True
        return False

    def isFull(self) -> bool:
        if self.len == self.k:
            return True
        return False


if __name__ == "__main__":
    myCircularDeque = MyCircularDeque(3)
    myCircularDeque.insertLast(1)  # return True
    myCircularDeque.insertLast(2)  # return True
    myCircularDeque.insertFront(3)  # return True
    myCircularDeque.insertFront(4)  # return False, the queue is full.
    myCircularDeque.getRear()  # return 2
    myCircularDeque.isFull()  # return True
    myCircularDeque.deleteLast()  # return True
    myCircularDeque.insertFront(4)  # return True
    myCircularDeque.getFront()  # return 4

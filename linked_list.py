#! /usr/bin/env /usr/bin/python3
import random


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, data=None):
        if data is not None:
            self.head = Node(data[0])
            n = self.head
            for d in data[1:]:
                n.next = Node(d)
                n = n.next

    def __str__(self):
        node = self.head
        out = ""
        while node.next is not None:
            out += str(node.data) + "->"
            node = node.next
        out += str(node.data)
        return out

    def __len__(self):
        if self.head is None:
            return 0
        n = self.head
        cnt = 1
        while n.next is not None:
            cnt += 1
            n = n.next
        return cnt

    def insert(self, i, data):
        if i <= 0:
            self.head = Node(data, self.head)
            # new = Node(data)
            # new.next = self.head
            # self.head = new
            return

        if i >= len(self):
            self.append(data)
            return

        n = self.head
        while n.next is not None and i > 1:
            n = n.next
            i -= 1
        n.next = Node(data, n.next)
        # newnode = Node(data)
        # newnode.next = n.next
        # n.next = newnode

    def append(self, data):
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = Node(data)


if __name__ == "__main__":
    lst = LinkedList([random.randint(0, 9) for i in range(0, random.randint(5, 20))])
    print(lst)
    lst.insert(-1, 3)
    print(lst)
    lst.append(22)
    print(lst)

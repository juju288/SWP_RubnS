import random

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)

# für < >
    def __lt__(self, other):
        return self.data < other.data

# für ==
    def __eq__(self, other):
        return self.data == other.data

class LinkedList:
    def __init__(self, data=None):
        if data:
            self.head = Node(data[0])
            n = self.head
            for d in data[1:]:
                n.next = Node(d)
                n.next.prev = n
                n=n.next
            self.tail=n

    def __str__(self):
        node = self.head
        out=""
        while node.next:
            out+=str(node.data)+" | "
            node=node.next
        out+=str(node.data)
        return out

    def __len__(self):
        if not self.head:
            return 0
        n = self.head
        cnt = 1
        while n is not self.tail:
            cnt+=1
            n = n.next
        return cnt

    def __iter__(self):
        self.iterableNode = self.head
        return self

    def __next__(self):
        try:
            item = self.iterableNode
            self.iterableNode = self.iterableNode.next
        except IndexError:
            raise StopIteration()
        except AttributeError:
            raise StopIteration()
        return item

    def __getitem__(self, idx):
        n = self.head
        for i in range(0, idx):
            n = n.next
        return n

    def __setitem__(self, idx, data):
        n = self.head
        for i in range(0, idx):
            n = n.next
    #    n = Node(data, n.next, n.prev)
        n.data = data

#1: O(n)   2: O(n)    arrl: O(1)
    def insert(self, i, d):
        if i == 0:
            self.head.prev = Node(d)
            self.head.prev.next = self.head
            self.head = self.head.prev
            return

        if not self.head.next or i >= len(self):
            self.append(d)
            return

        n=self.head
        while n is not self.tail and i > 1:
            n=n.next
            i-=1
        newnode = Node(d)
        n.next.next.prev = newnode
        newnode.next = n.next
        n.next = newnode
        newnode.prev = n

#1:=(n) (wenn mit tail program. 1) 2: O(1)    arrl: O(1)
    def append(self, d):
        self.tail.next = Node(d)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

#1: O(n^2)     2: O(n^2) arrl: O(n^2)
    def sort(self):
        l = len(self)
        while True:
            swapped = False
            for n in self:
                if n.next and n > n.next: # swap nodes in place
                    n1 = n
                    n2 = n.next

                    if n1 == self.head:
                        self.head = n2
                    if n2 == self.tail:
                        self.tail = n1

                    t = n1.next
                    n1.next = n2.next
                    n2.next = t

                    if n1.next:
                        n1.next.prev = n1

                    if n2.next:
                        n2.next.prev = n2

                    t = n1.prev
                    n1.prev = n2.prev
                    n2.prev = t

                    if n1.prev:
                        n1.prev.next = n1

                    if n2.prev:
                        n2.prev.next = n2

                    swapped = True

            if not swapped:
                return

#1: O(n) 2: O(n) arr: O(1)
    def delete(self, i):
        n = self.head
        if i == 0: self.head = self.head.next
        else:
            while n is not self.tail and i > 0:
                n = n.next
                i -= 1
            n.next.prev = n.prev
            n.prev.next = n.next


if __name__ == "__main__":
    lst = LinkedList([random.randint(0,9) for _ in range(0,5)])
    print(lst)
    lst.sort()
    print(lst[2])
    lst[1]=1
    print(lst)
    lst.delete(2)
    print(lst)


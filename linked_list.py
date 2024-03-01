#!/bin/usr/env python3
from typing import Union, Type


class Node:
    def __init__(self, data: Union[str, int], next: Union[None, Type["Node"]] = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self) -> None:
        if self.head is None:
            print("Linked list is empty.")
        else:
            itr: Node = self.head
            list_str = ""

            while itr:
                list_str += str(itr.data) + ("-->" if itr.next else "")
                itr = itr.next
            print(list_str)

    def insert_at_beginning(self, val: Union[str, int]) -> None:
        node = Node(val, self.head)
        self.head = node

    def insert_at_end(self, val: Union[str, int]) -> None:
        if self.head is None:
            self.insert_at_beginning(val)
        else:
            itr = self.head

            while itr.next:
                itr = itr.next

            itr.next = Node(val)

    def get_length(self) -> int:
        if self.head is None:
            print("Linked list is empty.")
        else:
            count = 0
            itr = self.head

            while itr:
                count += 1
                itr = itr.next

            return count

    def insert_at(self, val: Union[str, int], idx: int):
        if self.head is None:
            print("Linked list is empty")
        else:
            ll_size = int(self.get_length())

            if idx == 0:
                self.insert_at_beginning(val)
            elif (idx + 1) == ll_size:
                self.insert_at_end(val)
            elif idx in range(1, ll_size):
                count = 0
                itr = self.head
                prev = None

                while count != idx:
                    count += 1
                    prev = itr
                    itr = itr.next

                node = Node(val, itr)
                prev.next = node
            else:
                print("out of range!")


if __name__ == "__main__":
    ll = LinkedList()
    ll.print()
    print(ll.get_length())
    ll.insert_at_end(67)
    ll.insert_at_beginning(7)
    ll.insert_at_end(109)
    print(ll.get_length())
    ll.print()
    ll.insert_at("Theo", 0)
    ll.insert_at("Phil", ll.get_length() - 1)
    ll.insert_at(20, 3)
    ll.print()

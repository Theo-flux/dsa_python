#!/bin/usr/env python3
from typing import Union, Type, List


class Node:
    def __init__(self, data: Union[str, int], next: Union[None, Type["Node"]] = None):
        self.data = data
        self.next = next


class SinglyLinkedList:
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
        node = Node(val)
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

    def insert_at(self, idx: int, val: Union[str, int]):
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

    def remove_at(self, idx: int) -> None:
        if self.head is None:
            print("Linked list is empty")

        else:
            ll_size = int(self.get_length())
            if idx in range(0, ll_size):
                count = 0
                itr = self.head
                prev = None

                while count != idx:
                    count += 1
                    prev = itr
                    itr = itr.next

                if prev is None:
                    self.head = itr.next
                else:
                    prev.next = itr.next
            else:
                print("out of range!")

    def insert_values(self, data_list: List[Union[str, int]]):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(
        self, data_after: Union[str, int], data_to_insert: Union[str, int]
    ):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head is None:
            print("Linked list is empty")
        else:
            itr = self.head
            while itr:
                if itr.data == data_after:
                    break
                itr = itr.next
            if itr:
                prev = itr
                next_node = itr.next
                node = Node(data_to_insert, next_node)
                prev.next = node
            else:
                print("data not found!")

    def remove_by_value(self, data: Union[str, int]):
        # Remove first node that contains data
        pass
        if self.head is None:
            print("Linked list is empty")
        else:
            itr = self.head
            prev = None
            while itr:
                if itr.data == data:
                    break
                prev = itr
                itr = itr.next
            if itr:
                if prev:
                    prev.next = itr.next
                else:
                    self.head = itr.next
            else:
                print("data not found!")


if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")
    ll.print()
    ll.remove_by_value("orange")
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("apple")
    ll.print()
    ll.remove_by_value("mango")
    ll.print()
    ll.remove_by_value("banana")
    ll.print()
    ll.remove_by_value("grapes")
    ll.print()

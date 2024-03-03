#!/bin/usr/env python3
from typing import Type, Union, List


class Node:
    def __init__(
        self,
        data: Union[str, int] = None,
        next: Union[None, Type["Node"]] = None,
        prev: Union[None, Type["Node"]] = None,
    ) -> None:
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print(self) -> None:
        if self.head is None:
            print("Linked list is empty.")
        else:
            itr: Node = self.head
            list_str = ""

            while itr:
                list_str += str(itr.data) + ("<-->" if itr.next else "")

                itr = itr.next
            print(list_str)

    def insert_at_beginning(self, val: Union[str, int]) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            new_node.next = curr
            curr.prev = new_node
            self.head = new_node

    def insert_at_end(self, val: Union[str, int]) -> None:
        if self.head is None:
            self.insert_at_beginning(val)
        else:
            itr = self.head

            while itr.next:
                itr = itr.next

            new_node = Node(data=val, prev=itr, next=None)
            itr.next = new_node

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

                while count != idx:
                    count += 1
                    itr = itr.next

                new_node = Node(val, prev=itr.prev, next=itr)
                itr.prev.next = new_node
                itr.prev = new_node

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

                while count != idx:
                    count += 1
                    itr = itr.next

                if count == 0 or itr.prev is None:
                    self.head = itr.next
                    itr.prev = None
                    return

                if itr.next is None:
                    itr.prev.next = None
                    itr = None
                    return

                itr.prev.next = itr.next
                itr.next.prev = itr.prev
            else:
                print("out of range!")

    def insert_values(self, data_list: List[Union[str, int]]):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(
        self, data_after: Union[str, int], data_to_insert: Union[str, int]
    ):
        if self.head is None:
            print("Linked list is empty")
        else:
            itr = self.head
            while itr:
                if itr.data == data_after:
                    break
                itr = itr.next

            if itr:
                new_node = Node(data_to_insert, itr.next, itr)
                itr.next = new_node
                itr.next.prev = new_node

            else:
                print("data not found!")

    def print_forward(self):
        # This method prints list in forward direction. Use node.next
        self.print()

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            print("Linked list is empty")
        else:
            itr = self.head
            list_str = ""
            arr = []

            while itr:
                arr.insert(0, itr.data)
                itr = itr.next

            for i in range(0, len(arr)):
                list_str += str(arr[i]) + ("<-->" if i < len(arr) - 1 else "")
            print(list_str)


if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.insert_at_end(1)
    dll.print()
    print(dll.get_length())
    dll.insert_at_beginning(0)
    dll.print()
    dll.insert_at_end(2)
    dll.print()
    dll.insert_at_end(3)
    dll.print()
    dll.insert_at(2, 45)
    dll.print()
    dll.insert_at(2, 105)
    dll.print()
    dll.remove_at(2)
    dll.print()
    dll.remove_at(dll.get_length() - 1)
    dll.print()
    dll.remove_at(0)
    dll.print()
    dll.remove_at(0)
    dll.print()
    dll.remove_at(1)
    dll.print()
    dll.remove_at(0)
    dll.print()
    dll.insert_values(["banana", "mango", "grapes", "orange"])
    dll.print()
    dll.insert_after_value("mango", "apple")
    print(dll.get_length())
    dll.remove_at(0)
    dll.print()
    dll.insert_after_value("orange", "cherry")
    dll.print()
    dll.print_forward()
    dll.print_backward()
    print(dll.get_length())
    dll.remove_at(0)
    dll.print()
    dll.remove_at(0)
    dll.print()
    dll.remove_at(1)
    dll.print()
    dll.remove_at(0)
    dll.print()

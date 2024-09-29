
"""
Есть элемент связанного списка (ListNode).
Реализовать для него методы добавления элемента в начало(add_to_front) и конец(add_to_end).
"""
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def add_to_end(self, val) -> None:
        pointer = self.head
        if pointer is None:
            self.add_to_front(val)
        else:
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(val)

    def add_to_position(self, position: int, val):
        pointer = self.head
        i = 1
        while i != position-1 and pointer.next:
            i += 1
            pointer = pointer.next
        new = Node(val)
        new.next = pointer.next
        pointer.next = new

    def print_list(self):
        temp = self.head
        if temp is not None:
            print("Список содержит:", end=" ")
            while temp is not None:
                print(temp.val, end=" ")
                temp = temp.next
        else:
            print("Список пустой.")


a = LinkedList()
a.add_to_front('1')
a.add_to_front('0')
a.add_to_end('2')
a.print_list()

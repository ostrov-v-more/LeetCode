'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, list1, list2):  # способ с указателями
        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2  # присваивается тот который !=0
        return head.next

    def merge_two_lists_2(self, list1, list2):  # метод с рекурсией
        def recursion(l1, l2):
            if l1 == None:
                return l2
            if l2 == None:
                return l1

            if l1.val > l2.val:
                return ListNode(l2.val, recursion(l2.next, l1))
            else:
                return ListNode(l1.val, recursion(l2, l1.next))

        return recursion(list1, list2)



def printlist(list):
    while list:
        print(list.val, end=' —> ')
        list = list.next
    print('None')


def recursion(list):  # копируем лист, а не указатель
    while list:
        return ListNode(list.val, recursion(list.next))


# list3 = recursion(list1)
# list1.next.val = 1
# printlist(list2)
# printlist(list1)



# Функция для перемещения последнего узла в начало заданного связанного списка
def rearrange(head):
    # действовать только тогда, когда список действителен
    if head is None or head.next is None:
        return head

    ptr = head

    # перемещается на предпоследний узел
    while ptr.next.next:
        ptr = ptr.next

    # преобразовать список в круговой список
    ptr.next.next = head

    head = ptr.next  # Фиксированная головка
    ptr.next = None  # разорвать цепь
    return head


list1 = ListNode(1, ListNode(3, ListNode(5, ListNode(8))))
list2 = ListNode(2, ListNode(4, ListNode(6)))

list3 = Solution().merge_two_lists_2(list1, list2)

list1.next.next = ListNode(10)
printlist(list3)
printlist(list1)
printlist(list3)

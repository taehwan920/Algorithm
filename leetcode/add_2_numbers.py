class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_arr, l2_arr = [], []

        def putInArr(arr, cls):
            arr.append(cls.val)
            if cls.next is not None:
                putInArr(arr, cls.next)
        putInArr(l1_arr, l1)
        putInArr(l2_arr, l2)

        new_l1 = int(''.join(reversed(list(map(str, l1_arr)))))
        new_l2 = int(''.join(reversed(list(map(str, l2_arr)))))
        add = new_l1 + new_l2
        reversed_add = list(map(int, str(add)))
        reversed_add.reverse()
        result = ListNode()
        idx = 0

        def putInLL(cls, idx):
            cls.val = reversed_add[idx]
            if idx < len(reversed_add) - 1:
                idx += 1
                cls.next = ListNode()
                putInLL(cls.next, idx)
        putInLL(result, idx)
        return result

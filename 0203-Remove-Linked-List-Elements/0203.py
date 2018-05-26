# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dumHead = ListNode(0) #head
        dumHead.next = head
        cur = dumHead
        while cur.next != None:
            delNode = cur.next
            if delNode.val == val:
                cur.next = delNode.next
                delNode = None
            else:
                cur = cur.next

        retNode = dumHead.next
        dumHead = None
        return retNode

def createList():
    head = ListNode(0)
    cur = head
    for i in range(1, 10):
        cur.next = ListNode(i)
        cur = cur.next
    return head
            
def printList(head):
    cur = head
    while cur != None:
        print(cur.val, '-->', end='')
        cur = cur.next

    print('NULL')

if __name__ == "__main__":
    head = createList()
    printList(head)
    res = Solution().removeElements(head, 5)
    printList(res)
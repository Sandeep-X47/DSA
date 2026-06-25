class Solution:
    def deleteAllOccurOfX(self, head, x):
        temp = head

        while temp:

            # Node needs to be deleted
            if temp.data == x:
                next_node = temp.next
                prev_node = temp.prev

                # Case 1: deleting the head
                if prev_node is None:
                    head = next_node
                    if next_node:
                        next_node.prev = None

                # Case 2: deleting the middle or last node
                else:
                    prev_node.next = next_node
                    if next_node:
                        next_node.prev = prev_node

                temp = next_node   # move to next after deletion

            else:
                temp = temp.next   # normal traversal

        return head

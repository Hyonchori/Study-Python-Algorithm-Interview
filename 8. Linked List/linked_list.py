class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def print_nodes(node: ListNode) -> None:
    crnt_node = node
    while crnt_node is not None:
        print(crnt_node.val, end=' ')
        crnt_node = crnt_node.next
    print("")

class SLinkedList():
    def __init__(self):
        self.head = None

    def add_at_head(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def add_at_back(self, val):
        node = ListNode(val)
        if self.head is not None:
            crnt_node = self.head
            while crnt_node.next is not None:
                crnt_node = crnt_node.next
            crnt_node.next = node
        else:
            self.head = node

    def find_node(self, val):
        crnt_node = self.head
        while crnt_node is not None:
            if crnt_node.val == val:
                return crnt_node
            crnt_node = crnt_node.next
        raise RuntimeError("Node '{}' not found".format(val))

    def add_after(self, node, val):
        new_node = ListNode(val)
        new_node.next = node.next
        node.next = new_node

    def delete_after(self, prev_node):
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next

    def delete(self, val):
        node = self.head
        prev = ListNode(0)
        while node.next is not None:
            if node.val == val:
                prev.next = node.next
                print("??")
            else:
                prev.next = node
            node = node.next

        print_nodes(prev)



slist = SLinkedList()
slist.add_at_back(3)
slist.add_at_back(4)
slist.add_at_head(1)
slist.add_at_head(3)
print_nodes(slist.head)
print("")

node1 = slist.find_node(3)
slist.add_after(node1, 5)
#print_nodes(slist.head)

slist.delete(3)
print_nodes(slist.head)
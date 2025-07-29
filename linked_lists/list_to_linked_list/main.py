from linked_lists.list_node.main import ListNode
from linked_lists.print_linked_list.main import print_linked_list

def list_to_linked_list(lst):
    head = ListNode()
    current = head
    for item in lst:
        current.next = ListNode(item)
        current = current.next

    return head.next

if __name__ == "__main__":
    lst = list(range(0,10))
    head = list_to_linked_list(lst)
    print_linked_list(head)
    
    
    

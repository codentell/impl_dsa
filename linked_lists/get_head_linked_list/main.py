from linked_lists.list_node.main import ListNode
from linked_lists.list_to_linked_list.main import list_to_linked_list
from linked_lists.print_linked_list.main import print_linked_list

def get_head_node(head):
    new_head = ListNode(head.value)
    new_head.next = None
    return new_head


if __name__ == "__main__":
    lst = list(range(1,10))
    head = list_to_linked_list(lst)

    print("Original Linked List:")
    print(print_linked_list(head))

    print("Head Node:")
    print_linked_list(get_head_node(head))

    

    
    


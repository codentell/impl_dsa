from linked_lists.list_node.main import ListNode
from linked_lists.list_to_linked_list.main import list_to_linked_list
from linked_lists.print_linked_list.main import print_linked_list



def swap_head_tail(head):
    prev = None
    current = head
    while current.next:
        prev_tail = prev
        prev = current
        current = current.next

    tail = current
    second_to_last = prev

    if head.next == tail:
        tail.next = head
        head.next = None
    
    tail.next = head.next
    second_to_last.next = head
    head.next = None

    return tail
    


if __name__ == "__main__":
    lst = list(range(1,5))
    head = list_to_linked_list(lst)
    print("Original Linked List:")
    print_linked_list(head)

    print("Swapped Head and Tail:")
    print_linked_list(swap_head_tail(head))
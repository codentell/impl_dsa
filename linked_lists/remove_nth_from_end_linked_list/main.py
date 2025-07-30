from linked_lists.list_node.main import ListNode
from linked_lists.list_to_linked_list.main import list_to_linked_list
from linked_lists.print_linked_list.main import print_linked_list


def remove_nth_from_end(head, n):
    dummy = ListNode(nxt=head)
    first_ptr = dummy
    second_ptr = dummy

    for _ in range(n + 1):
        first_ptr = first_ptr.next

    while first_ptr:
        first_ptr = first_ptr.next
        second_ptr = second_ptr.next

    second_ptr.next = second_ptr.next.next

    return dummy.next
    







if __name__ == "__main__":
    lst = [1,2,3,6,3,4,5,6]
    nth = 2
    head = list_to_linked_list(lst)

    print("Original Linked List:")
    print_linked_list(head)


    print(f"Modified Linked List (after removing value {nth} from the end):")
    new_node = remove_nth_from_end(head, nth)
    print_linked_list(new_node)

    

from linked_lists.list_to_linked_list.main import list_to_linked_list
from linked_lists.print_linked_list.main import print_linked_list


def rotate(head, k):

    old_tail = head
    length = 1 
    while old_tail.next:
        length += 1
        old_tail = old_tail.next
    
    old_tail.next = head
    new_tail = head
    
    for _ in range(length - k % length - 1):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    new_tail.next = None
    return new_head



if __name__ == "__main__":
    lst = list(range(1,6))
    k = 2
    head = list_to_linked_list(lst)

    print("Original Linked List:")
    print(print_linked_list(head))
    
    print(f"Rotate Linked List by {k}")
    head = rotate(head, k)
    print_linked_list(head)
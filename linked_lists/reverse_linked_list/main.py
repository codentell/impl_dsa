from linked_lists.list_to_linked_list.main import list_to_linked_list
from linked_lists.print_linked_list.main import print_linked_list

def reverse_linked_list(head):
    prev = None 
    current = head
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev


if __name__ == "__main__":
    lst = list(range(0,10))
    head = list_to_linked_list(lst)

    print("Original Linked List:")
    print(print_linked_list(head))
    
    print("Reversed Linked List:")
    rev = reverse_linked_list(head)
    print_linked_list(rev)
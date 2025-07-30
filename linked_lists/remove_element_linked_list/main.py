from linked_lists.list_node.main import ListNode
from linked_lists.list_to_linked_list.main import list_to_linked_list
from linked_lists.print_linked_list.main import print_linked_list



def remove_element(head, value):
    temp = ListNode()
    current = head
    prev = temp

    while current:
        if current.value == value:
            prev.next = current.next
        else:
            prev = current
        current = current.next

    return temp.next
    



if __name__ == "__main__":
    lst = [1,2,3,6,3,4,5,6]
    value = 6
    head = list_to_linked_list(lst)

    print("Original Linked List:")
    print_linked_list(head)


    print(f"Modified Linked List (after removing value {value}):")
    remove_element(head, value)
    print_linked_list(head)
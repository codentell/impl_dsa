from linked_lists.list_node.main import ListNode
from linked_lists.list_to_linked_list.main import list_to_linked_list
from linked_lists.print_linked_list.main import print_linked_list


def swap_node(head, k):
    current = head
    length = 0
    while current:
        length += 1
        current = current.next
    
    front = head
    for _ in range(1, k):
        front = front.next
    
    end = head
    for _ in range(1, length - k + 1):
        end = end.next
    
    temp = front.value
    front.value = end.value
    end.value = temp

    return head


if __name__ == "__main__":
    lst = list(range(1,6))
    head = list_to_linked_list(lst)
    k = 2
    print("Original Linked List:")
    print_linked_list(head)

    print("Swapped node by kth place front and end:")
    print_linked_list(swap_node(head, k))
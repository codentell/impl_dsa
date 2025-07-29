from linked_lists.list_node.main import ListNode
from linked_lists.list_to_linked_list.main import list_to_linked_list
from linked_lists.print_linked_list.main import print_linked_list

def get_node(head, pos):
    current = head
    index = 0
    while current:
        if index == pos:
            new_node = ListNode(current.value)
            return new_node
        current = current.next
        index += 1
    return ListNode()


if __name__ == "__main__":
    lst = list(range(1,10))
    head = list_to_linked_list(lst)

    print("Original Linked List:")
    print(print_linked_list(head))

    print("Get Node Position 3:")
    print_linked_list(get_node(head, 3))

    print("Get Node Position Not Found:")
    print_linked_list(get_node(head, 11))
from linked_lists.list_to_linked_list.main import list_to_linked_list
from linked_lists.print_linked_list.main import print_linked_list

def delete_node(node):
    node.value = node.next.value
    node.next = node.next.next




if __name__ == "__main__":
    lst = list(range(1,10))
    head = list_to_linked_list(lst)

    print("Original Linked List:")
    print_linked_list(head)

    node_to_delete = head.next.next.next  # 4th node, value 4
    delete_node(node_to_delete)

    print("Modified Linked List (after deleting value 4):")
    print_linked_list(head)
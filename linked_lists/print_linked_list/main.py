from linked_lists.list_node.main import ListNode

def print_linked_list(head):
    current = head
    index = 0
    while current:
        print(f"Node {index}: value={current.value}, id={id(current)}, next_id={id(current.next) if current.next else None}")
        current = current.next
        index += 1


if __name__ == "__main__":
    lst = list(range(0,10))
    head = ListNode()
    current = head
    for n in lst:
        current.next = ListNode(n)
        current = current.next
    
    head = head.next
    
    print_linked_list(head)



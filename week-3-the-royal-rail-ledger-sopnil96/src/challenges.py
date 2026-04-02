def build_sll_from_list(values: list[int]) -> SinglyLinkedList:
    """Build and return a singly linked list from a Python list."""
    sll = SinglyLinkedList()
    if not values:
        return sll
    
    sll.head = SLLNode(values[0])
    current = sll.head
    for val in values[1:]:
        current.next = SLLNode(val)
        current = current.next
    return sll


def sll_to_list(sll: SinglyLinkedList) -> list[int]:
    """Return all values from a singly linked list as a Python list."""
    result = []
    current = sll.head
    while current:
        result.append(current.value)
        current = current.next
    return result


def find_first_repeat_sll(sll: SinglyLinkedList) -> int | None:
    """Return the first repeated value seen from left to right."""
    seen = set()
    current = sll.head
    while current:
        if current.value in seen:
            return current.value
        seen.add(current.value)
        current = current.next
    return None


def remove_all_from_dll(dll: DoublyLinkedList, target: int) -> None:
    """Remove all nodes whose value equals target. Updates head and tail."""
    current = dll.head
    while current:
        if current.value == target:
            # Save the next node before we potentially delete 'current'
            next_node = current.next
            
            if current.prev:
                current.prev.next = current.next
            else:
                dll.head = current.next  # Target was at the head
                
            if current.next:
                current.next.prev = current.prev
            else:
                dll.tail = current.prev  # Target was at the tail
                
            current = next_node
        else:
            current = current.next


def is_train_palindrome(dll: DoublyLinkedList) -> bool:
    """Check if the DLL reads the same forward and backward."""
    if not dll.head:
        return True
    
    left = dll.head
    right = dll.tail
    
    # Move from both ends toward the middle
    while left and right and left != right and left.prev != right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.prev
    return True
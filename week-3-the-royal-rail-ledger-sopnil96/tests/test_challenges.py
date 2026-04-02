class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

class DLLNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def build_sll_from_list(values: list[int]) -> SinglyLinkedList:
    sll = SinglyLinkedList()
    if not values:
        return sll
    sll.head = Node(values[0])
    current = sll.head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return sll

def sll_to_list(sll: SinglyLinkedList) -> list[int]:
    result = []
    current = sll.head
    while current:
        result.append(current.value)
        current = current.next
    return result

def find_first_repeat_sll(sll: SinglyLinkedList) -> int | None:
    seen = set()
    current = sll.head
    while current:
        if current.value in seen:
            return current.value
        seen.add(current.value)
        current = current.next
    return None

def remove_all_from_dll(dll: DoublyLinkedList, target: int) -> None:
    current = dll.head
    while current:
        if current.value == target:
            # If it's the head
            if current.prev:
                current.prev.next = current.next
            else:
                dll.head = current.next
            
            # If it's the tail
            if current.next:
                current.next.prev = current.prev
            else:
                dll.tail = current.prev
        current = current.next

def is_train_palindrome(dll: DoublyLinkedList) -> bool:
    if not dll.head:
        return True
    
    left = dll.head
    right = dll.tail
    
    while left != right and left.prev != right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.prev
    return True
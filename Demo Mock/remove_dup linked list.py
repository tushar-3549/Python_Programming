# Given the head of a linked list, remove all duplicate elements so that each value appears only once. Return the modified head of the linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
      
# sorted linked list  
def delete_dup(head):
    cur = head 
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head

# def sort_linked_list(head):
#     values = []
#     current = head
#     while current:
#         values.append(current.val)
#         current = current.next

#     values.sort()
#     return build_linked_list(values)
    

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head

def print_linked_list(head):
    cur = head
    while cur:
        print(cur.val, end=' -> ')
        cur = cur.next
    print('None')

values = [1, 1, 2, 3, 3]
head = build_linked_list(values)
print("Original List:")
print_linked_list(head)

head = delete_dup(head)
print("After Removing Duplicates:")
print_linked_list(head)

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', write a function to determine if the input string is valid.

# An input string is valid if: 

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.
def is_valid_parenthesis(s: str) -> bool:
    matching_bracket = {')':'(', '}':'{', ']':'['}
    stack =[]
    
    for char in s:
        if char in matching_bracket:
            top_element =stack.pop() if stack else '#'
            if matching_bracket[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack 
    



# Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if
#  there is some node in the list that can be reached again by continuously following the next pointer. Internally, 
# pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a 
# parameter. Return true if there is a cycle in the linked list. Otherwise, return false.
 
# Model the Node and Linked List concepts using classes.

    


#  Given the head of a singly linked list, return true if it is a palindrome. Model the Node and Linked List concepts using 
# classes. 
class Node:
    def __init__(self, value: int, next: 'Node' = None):
        self.value = value  
        self.next = next  

class LinkedList:
    def __init__(self):
        self.head = None  
    def append(self, value: int):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

def reverse_list(head: Node) -> Node:
    previous = None  
    current = head  
    while current:
        next_node = current.next  
        current.next = previous  
        previous = current  
        current = next_node 
    return previous  

def is_palindrome(head: Node) -> bool:
    if not head or not head.next:
        return True  
    
    
    slow = head  
    fast = head  
    while fast and fast.next:
        slow = slow.next  
        fast = fast.next.next  
    
    
    second_half_start = reverse_list(slow)  
    
    
    first_half_start = head  
    second_half_copy = second_half_start  
    while second_half_start:
        if first_half_start.value != second_half_start.value:
            return False  
        first_half_start = first_half_start.next 
        second_half_start = second_half_start.next 
    
    
    reverse_list(second_half_copy)  
    
    return True 

# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# - push(x: int) -> None: Pushes element x to the top of the stack.
# - pop() -> None Removes the element on the top of the stack and returns it.
# - pop() -> None Returns the element on the top of the stack.
# - empty() -> None Returns true if the stack is empty, false otherwise.


class Queue:
    def __init__(self):
        self.items =[]
    
    def enqueue(self, x: int) -> None:
        self.items.append(x)
    def dequeue(self) -> int:
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")
    
    def front(self) ->int:
        if not self.is_empty():
            return self.items[0]
        raise IndexError("front from empty queue")
        
    def is_empty(self) -> bool:
        return len(self.items) == 0
    def size(self) ->int:
         return len(self.items)

class MyStack:
    
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
    
    def pop(self) -> None:
        return self.queue1.dequeue()
    
    def push(self, x: int) -> None:
        self.queue2.enqueue(x)
        while self.queue1.size() > 0:
            self.queue2.enqueue(self.queue1.dequeue())
        self.queue1, self.queue2 = self.queue2, self.queue1
    
    def top(self) -> int:
        return self.queue1.front()
        
    def empty(self) -> bool:
        return self.queue1.is_empty()
    
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing 
# the number of elements in nums1 and nums2 respectively. Write a function to merge nums1 and nums2 into a single array 
# sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate 
# this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n 
# elements are set to 0 and should be ignored. nums2 has a length of n.

def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
    while p2 >= 0:
        if p1 < 0 or nums2[p2] > nums1[p1]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1

        
                    
# Given a string s which consists of lowercase or uppercase letters, write a function that returns the length of the longest 
# palindrome that can be built with those letters. Letters are case sensitive, for example, "Aa" is not considered a palindrome here.   

            
def longest_palindrome(s: str) -> int:
    from collections import Counter
    
    char_count = Counter(s)
    length = 0
    odd_found = False
    
    for count in char_count.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_found = True
    
    if odd_found:
        length += 1
    
    return length

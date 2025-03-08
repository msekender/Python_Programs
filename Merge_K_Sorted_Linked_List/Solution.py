'''
Approach
We use a min-heap (priority queue) to efficiently merge k sorted lists:
Push the head node of each list into the heap.
Extract the smallest node from the heap and append it to the merged list.
If the extracted node has a next node, push it into the heap.
Repeat the process until all nodes are processed.
'''

from heapq import heappush, heappop
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val} -> {self.next}"

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        # Initialize the heap with the first node of each linked list
        for i, node in enumerate(lists):
            if node:
                heappush(min_heap, (node.val, i, node))  # (value, index, node)

        dummy = ListNode(0)  # Dummy head
        curr = dummy
        
        # Extract the smallest element and push the next node of extracted element
        while min_heap:
            val, i, node = heappop(min_heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next

# Helper functions to create and print linked lists
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(" -> ".join(map(str, values)) if values else "Empty List")

# Example test case
lists = [
    create_linked_list([1, 4, 5]),
    create_linked_list([1, 3, 4]),
    create_linked_list([2, 6])
]

solution = Solution()
merged_head = solution.mergeKLists(lists)
print_linked_list(merged_head)

'''
Time Complexity Analysis
Insertion & Extraction in Min-Heap takes O(log k).
Since we process all N nodes in total, each node is pushed and popped from the heap once.
Thus, the overall time complexity is O(N log k), where:
N is the total number of elements across all linked lists.
k is the number of linked lists.

Space Complexity Analysis
The heap stores at most k elements at any time, leading to O(k) space.
The output linked list is formed in O(N) space, but this is the required output, so it doesn’t count as extra space.
Thus, the additional space complexity is O(k).
'''
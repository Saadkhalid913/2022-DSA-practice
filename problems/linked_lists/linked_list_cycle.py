'''
LINK: https://leetcode.com/problems/linked-list-cycle/submissions/


'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        node_list = {}
        
        previous_node = None
        current_node = head 
        while current_node != None:
            node_list[id(current_node)] = True
            next_node = current_node.next
            if next_node != None and id(next_node) in node_list:
                return True 
            previous_node = current_node
            current_node = next_node
            
        return False 
        
        
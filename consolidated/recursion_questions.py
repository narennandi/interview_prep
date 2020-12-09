class Solution:
    """
    Decode Ways
    A message containing letters from A-Z is being encoded to numbers using the following mapping:
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    """
    def __init__(self):
        self.memo = {}
        
    def recursive_with_memo(self, index, s):
            #if you reach the end of the string return 1 for success
            if index == len(s):
                return 1
            
            #if the string starts with a zero, it can't be decoded
            if s[index] == '0':
                return 0
            
            #if the string has only one character
            if index == len(s) - 1:
                return 1
            
            #memoization is needed since we might encounter the same sub-string
            if index in self.memo:
                return self.memo[index]
            
            if int(s[index: index + 2]) <= 26:
                ans = self.recursive_with_memo(index+1, s) + self.recursive_with_memo(index+2, s)
            else:
                ans = self.recursive_with_memo(index+1, s)

            save for memoization
            self.memo[index] = ans

            return ans

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        return self.recursive_with_memo(0,s)


class Solution:
    def letterCombinations(self, digits):
        """
        Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
        Return the answer in any order.
        A mapping of digit to letters (just like on the telephone buttons) is given below. 
        Note that 1 does not map to any letters.
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
        output = []
        if digits:
            backtrack("", digits)
        return output



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    linked list
    Merge two sorted linked lists and return it as a new sorted list. 
    The new list should be made by splicing together the nodes of the first two lists.
    Input: l1 = [1,2,4], l2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    Time complexity : O(n + m)
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        if l1 is None:
            return l2
        
        elif l2 is None:
            return l1
        
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
            

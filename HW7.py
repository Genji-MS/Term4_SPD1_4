#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

'''
Time complexity is O(n) because we only iterate through the list items once Even though there are two lists which would be O(2n) we simplify this.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """  
        answerNode = None
        tail = None
        remainder = 0
        n1 = l1.val
        n2 = l2.val
        
        while l1 != None or l2 != None or remainder == 1:
            if l1 == None:
                n1 = 0
            else:
                n1 = l1.val
            if l2 == None:
                n2 = 0
            else:
                n2 = l2.val
            total = n1+n2+remainder
            if total >= 10:
                remainder = 1
                total = total - 10
            else :
                remainder = 0
            #answerNode = ListNode(total)
            if answerNode != None:
                tail.next = ListNode(total)
                tail = tail.next
            else:
                answerNode = ListNode(total)
                tail = answerNode
            
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            
        return answerNode


#Given a 32-bit signed integer, reverse digits of an integer.


'''
The problem was a bit more difficult then first imagined due to the presence of edge cases such as:
a negative number
a number such as 1000 where we should remove the zeroes when flipped
a series of zeroes
a number greater then the maximum 32bit signed int

The Time complexity requires iterating through a small list of integers (maximum length of 10)
however n<=10 is still n
it is O(n)
'''

class Solution2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        KEY = ['0','1','2','3','4','5','6','7','8','9']
        negative = (True,False)[x >= 0]
        stack = []
        number = abs(x)
        while number:
            number, remainder = divmod(number, 10)
            stack.append(KEY[remainder])
        revInt= ''.join(stack)
        
        while len(revInt) > 1 and revInt[0] == '0':
            revInt = revInt[1:]
        if len(revInt) <1 or int(revInt) > 2147483647:
            revInt = 0
        if negative:
            revInt = 0- int(revInt)
        return revInt
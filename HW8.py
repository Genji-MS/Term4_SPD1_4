class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        '''
        x = -121
        nums = '-121'
        left = 0
        right = 3
        
        if '-' == '1': False
        
        
        x = 121
        nums = '121'
        left = 0
        right = 2
        
        if '1' == '1':
        
        left = 1
        right = 1
        
        if '2' == '2'
        
        left = 2
        right = 0
        
        while left < right: True
        '''
        
        nums = str(x)
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left] != nums[right]:
                return False
            left +=1
            right -=1
        return True


class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        '''
        nums = [2, 7, 11, 15]
        target = 13
        num_dict = {}
        
        i = 0
        num = 2
        num_dict { 11: 0 }
        
        i = 1
        num = 7
        num_dict { 11: 0, 6: 1 }
        
        i = 2
        num = 11
        if 11 in dict: return [0, 2]
        '''
        
        num_dict = {}
        for i,num in enumerate(nums):
            if num in num_dict.keys():
                return [num_dict[num], i]
            num_dict[target-num] = i
        return []
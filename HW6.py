#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)). [HARD]

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        '''
        This solution assumed we calculated the median of each list, INCORRECT
        '''
        
        '''
        def median(self, nums):
            value = 0
            length = len(nums)-1
            if length < 0:
                return None
            half,rem = divmod(length,2)
            #print ("half: {} rem: {}".format(half,rem))
            if rem >0 and length > 0:
                value = ( float(nums[half]) + float(nums[half+1]) ) /2
            else:
                value = float(nums[half])
            return value
        
        val1 = median(self, nums1)
        val2 = median(self, nums2)
        if val1 == None:
            return val2
        elif val2 == None:
            return val1
        #print ("val1: {} val2: {}".format(val1,val2))
        return (val1 + val2)/2
        '''
        
        '''
        This solution assumed that I was to return the median of each list, INCORRECT
        '''
        
        '''
        def medianAppend(self, nums, lst = []):
            length = len(nums)-1
            if length < 0:
                return lst
            half,rem = divmod(length,2)
            lst.append(nums[half])
            if rem > 0 and length > 0:
                lst.append(nums[half+1])
            return lst
                
        def medianAdd(self, nums):
            value = 0
            length = len(nums)-1
            if length < 0:
                return value
            half,rem = divmod(length,2)
            if rem >0 and length > 0:
                value = ( float(nums[half]) + float(nums[half+1]) ) /2
            else:
                value = float(nums[half])
            return value
        
        list3 = medianAppend(self, nums1)
        list3 = medianAppend(self, nums2, list3)
        list3.sort()
        return medianAdd(self, list3)
        '''
        
        '''
        I need to concat both lists and return the median of the new list
        brute force to sort two lists of long length would be a pain.
        ...sooo pointers and just walk without moving data
        '''

        '''
        nums1 = [-1]
        nums2 = [0,4]
        ...init
        len1 = 1
        len2 = 2
        length = (1)+(2)-1 = 2
        tCount = (2)//2 = 1
        cCount = 0
        tLength = 1
        cLength = 0
        point1 = 0
        point2 = 0
        half = 1
        rem = 0
        lst = []
        nums1 = [-1,+inf]
        nums2 = [0,4,+inf]
        ...
        while (0<1)True
        (-1 < 0) True and (0 < 1) True
        (0 >= 1) False
        cCount = 1
        cLength = 0
        point1 = 1
        point2 = 0
        ...
        while (0<1)True
        (+inf<0) False and...
        (1 >= 1) True
        lst = [0]
        cCount = 2
        cLength = 1
        point1 = 1
        point2 = 1
        ...
        while (1<1)False
        (1 ==2)False
        return lst[0] #0
        '''
        
        len1 = len(nums1)
        len2 = len(nums2)
        length = len1 + len2 -1
        tCount = (length)//2  #calculate the targetCounter (median-point) of both lists
        cCount = tLength = cLength = 0  #set the currentCounter, totalLength of our list, currentLength of list to 0
        point1 = point2 = 0  #pointers for each list
        half,rem = divmod(length,2)  #figure if our lst needs 1 or 2 elements
        if rem >0 and length > 0:
            tLength = 2
        else:
            tLength = 1
        lst = []
        #add an infinatly high number to each list in the event we exaust the list itself for being the lower number
        nums1.append('+inf')
        nums2.append('+inf')
        
        while cLength < tLength:  #calling len(lst) is a waste each loop, check the stored values
            #print ("len1:{} len2:{} length:{} tC:{} cC:{} point1:{} point2:{} lst:{}".format(len1,len2,length,tCount,cCount,point1,point2,lst))
            if nums1[point1] < nums2[point2] and point1 < len1:  #if current number of nums1 is less then nums2
                if cCount >= tCount:  #if we have reached our counter, add it to our list
                    lst.append(nums1[point1])
                    cLength = len(lst)
                point1+= 1
            else:  #list2 is the lower number
                if cCount >= tCount:
                    lst.append(nums2[point2])
                    cLength = len(lst)
                point2 +=1
            cCount += 1
        #print ("lst:{}".format(lst))
        if tLength == 2:  #return the median values, converting to float as two ints will return an int after division
            return ( float(lst[0])+float(lst[1])) /2
        return lst[0]

#Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        nums = [0,0,1,1,1,2,2,3,3,4]
        ...
        i = 0
        len(nums)-1 = 9
        num = 0
        nums[i+1] = 0
        nums = [0,*,1,1,1,2,2,3,3,4]   # '*' denotes pop
        ...
        i = 0
        len(nums)-1 = 8
        num = 0
        nums[i+1] = 1
        nums = [0,1,1,1,2,2,3,3,4]
        ...
        i = 1
        len(nums)-1 = 8
        num = 1
        nums[i+1] = 1
        nums = [0,1,*,1,2,2,3,3,4]
        ...
        i = 1
        len(nums)-1 = 7
        num = 1
        nums[i+1] = 1
        nums = [0,1,*,2,2,3,3,4]
        ...
        i = 1
        len(nums)-1 = 6
        num = 1
        nums[i+1] = 2
        nums = [0,1,2,2,3,3,4]
        ...
        i = 2
        len(nums)-1 = 6
        num = 2
        nums[i+1] = 2
        nums = [0,1,2,*,3,3,4]
        ...
        i = 2
        len(nums)-1 = 5
        num = 2
        nums[i+1] = 3
        nums = [0,1,2,3,3,4]
        ...
        i = 3
        len(nums)-1 = 4
        num = 3
        nums[i+1] = 3
        nums = [0,1,2,3,*,4]
        ...
        i = 3
        len(nums)-1 = 4
        num = 3
        nums[i+1] = 4
        nums = [0,1,2,3,4]
        ...
        i = 4
        len(nums)-1 =4

        return len(nums) = 5 
        '''
        for i, num in enumerate(nums):
            while i < len(nums)-1 and num == nums[i+1]:
                nums.pop(i+1)
        return len(nums)
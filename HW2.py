#https://leetcode.com/problems/integer-to-roman/
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        '''
        First attempt, it works, but is very long winded, so I improved on it
        The problem was very straghtforward to me, Even though it was very brute force, 
        other then the below optomizatations I couldn't imagine any other effective ways to go about this.
        '''

        '''
        roman_output = ""
        while num >0:
            if num >= 1000:
                roman_output += "M"
                num -= 1000
            elif num >= 900:
                roman_output += "CM"
                num -= 900
            elif num >= 500:
                roman_output += "D"
                num -= 500
            elif num >= 400:
                roman_output += "CD"
                num -= 400
            elif num >= 100:
                roman_output += "C"
                num -= 100
            elif num >= 90:
                roman_output += "XC"
                num -= 90
            elif num >= 50:
                roman_output += "L"
                num -= 50
            elif num >= 40:
                roman_output += "XL"
                num -= 40
            elif num >= 10:
                roman_output += "X"
                num -= 10
            elif num >= 9:
                roman_output += "IX"
                num -= 9
            elif num >= 5:
                roman_output += "V"
                num -= 5
            elif num >= 4:
                roman_output += "IV"
                num -= 4
            elif num >= 1:
                roman_output += "I"
                num -= 1
        return roman_output
                '''
        
        roman_output = ""
        romanChars  = ['M','CM','D','CD','C','XC', 'L','XL','X','IX','V','IV','I']
        intChars = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        while num > 0:
            for i,r in zip(intChars,romanChars):
                if num >= i:
                    roman_output += r
                    num -= i
                    break
        return roman_output
        

#https://leetcode.com/problems/3sum/
class Solution2(object):
    def threeSum(self, nums):
    
        
        '''
        Avoiding the brute force technique I thought up a series of complicated solutions that didn't fit their data types
        So my ideas went back to the brute force method as being the only way to go about this
        
        programming my demo, I found that f-strings are illegal on leetcode, ternary and even ++x were not allowed... 
        My first implementation worked for the initial solution, but was very slow in time complexity
        '''
        
        '''
        solutionSet = []
        for i1 in range(len(nums)-2):
            for i2 in range(len(nums)-1)[i1+1:]:
                for i3 in range(len(nums))[i2+1:]:
                    if nums[i1] + nums[i2] + nums[i3] == 0:
                        newSet = [ nums[i1],nums[i2],nums[i3] ]
                        newSet.sort()
                        if newSet not in solutionSet:
                            solutionSet.insert(0,newSet)
                    #print ('i1: {one} i2:{two} i3:{three} =={sol}'.format (one=i1,two=i2,three=i3,sol=i1+i2+i3))
        return solutionSet
        '''

        '''
        I did a few micro optomizations to make things faster:

        I've omitted the 3rd index and just search if the number we need to reach 0 exists in the list
        Since we only need two negative numbers, The index should only go to the length of where 0 is in the sorted list
        
        searching our 3rd number should only begin with positive numbers, so we go through a loop to set our index
        It's time consuming, but I figured it would save time later.

        This completes 311 of 313 tests when submitting the code.
        '''
        
        '''
        nums.sort()
        index = -1
        for i in range(len(nums)):
            if nums[i] > 0:
                if i > 0:
                    index = i
                else:
                    index = 1
                break
        max = 0
        if len(nums) >0:
            max = nums[len(nums)-1]
        #print (max)
        #print (index)
        solutionSet = []
        for i1 in range(len(nums))[:index]:
            for i2 in range(len(nums))[(i1+1):]:
                n3 = 0 - (nums[i1] + nums[i2])
                #print ('1:{one} 2:{two} 3:{thr}'.format(one=nums[i1],two=nums[i2],thr=n3))
                if n3 <= max:
                    if n3 in nums[i2+1:]:
                        newSet = [ nums[i1],nums[i2],n3 ]
                        newSet.sort()
                        if newSet not in solutionSet:
                            solutionSet.append(newSet) 
        return solutionSet
        '''

        '''
        I wanted to use a dictionary because it has a faster lookup

        --pseudocode / logic--

        #check each in values
            #if in values [1]
                #true: sort() add to solutionSet, if not in solutionSet
                #false: check if NOT in dict[key].values()[0]
                    #true: add to [0] calculate [1], only if [1] is 0 or greater
            #if 0 or less check if NOT in dict.keys()
                #true: add to dict (afterwards to avoid doing the above to itself

        This completes 311 of 313 tests when submitting the code. It didn't improve the time complexity
        comments in the code were for my reference of accessing the data
        '''
        
        '''
        nums.sort()
        solutionDict = {}
        solutionSet = []
        
        for n in nums:
            for item in solutionDict.items():
                match = False
                exist = False
                for pair in item[1]:#[[-1, 5], [0, 4]]  
                    if match == False and n == pair[1]:#[-1, 5]             
                        match = True
                        newSet = [ item[0] , pair[0] , n ]
                        newSet.sort()
                        if newSet not in solutionSet:
                            solutionSet.append(newSet) 
                    if n == pair[0]:
                        exist = True
                if match == False and exist == False:
                    v = 0- (n + item[0])
                    if v >= 0:
                        item[1].append([n,v])
            if n <= 0 and n not in solutionDict.keys():
                solutionDict[n] = []
        return solutionSet
        '''

        '''
        I wanted the dictionary to work in reverse, 
        where we could quickly lookup if a solution already exists. rather then iter through each of the keys and values
        the problem here is that in order to create every comparison, we need to itterate through an ever growing list.

        Thought of separating lists to make things more efficient.

        -- pseudocode / logic --

        check solutionDict for keys where answers are
        answer [num1,num2]
        if true, add to solutionSet
        if false
            check numbersDict for current number entry
            if true, create solutionSet entry for pair
            if false, create solutionSet entry for everything
                + add to numbersDict

        This completes 311 of 313 tests when submitting the code. It didn't improve the time complexity.
        However it remains as my final solution due to the smaller and easier to read code
        '''
        
        solutionDict = {}
        numbersDict = {}
        solutionSet = []
        
        for n in nums:
            if n in solutionDict.keys():
                newSet = [ n , solutionDict[n][0] , solutionDict[n][1] ]
                newSet.sort()
                if newSet not in solutionSet:
                    solutionSet.append(newSet) 
            elif n in numbersDict.keys():
                solutionDict[0 - (n + n)] = [ n , n ]
            else:
                for o in numbersDict.keys():
                    solutionDict[0 - (n + o)] = [n , o]
                numbersDict[n] = []
        return solutionSet

        '''
        splitting between negative and positive lists to search a little faster. The thought was to populate every possible
        answer quickly, then to check through the list again to check against that dictionary for solutions.

        Each number goes into either a positive or negative list
        each negative adds to all positives
        zero is a negative
        zero has a counter if 3, is a solution

        iter the entire list to the dict for solutions. 
        
        This failed because we do not keep track of numbers and they can appear twice in calculation and in solution checking.
        '''
        
        '''
        posList = set()
        negList = set()
        solutionDict = {}
        solutionSet = []
        oCount = 0
        
        for n in nums:
            if n == 0:
                oCount+=1
                negList.add(n)
            elif n < 0:
                negList.add(n)
            else:
                posList.add(n)
        for n in negList:
            for p in posList:
                if n not in solutionDict:
                    solutionDict[0 - (n + p)] = [n , p]
        for n in nums:
            #Fails, as we can check numbers in the list a 2nd time
            if n in solutionDict.keys():
                newSet = [ n , solutionDict[n][0] , solutionDict[n][1] ]
                newSet.sort()
                if newSet not in solutionSet:
                    solutionSet.append(newSet)
        if oCount >= 3:
            newSet = [0, 0, 0]
            solutionSet.append(newSet)
        return solutionSet
        '''
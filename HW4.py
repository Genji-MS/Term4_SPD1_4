#Given a string, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #store the longest string and its length
        #store a candidate string and its length
        #store letters in a dict via index value of the string
        #create a pointer of valid index of current string
        
        #if not in dict:
            #add
        #if in dict:
            #if letter index >= pointer, it is a repeat
                #check if candidate is longer then longest string:
                    #make it new lstring and lstringl
                #move pointer to +1 of the returned dictionary[letter] value
                #cstring split to one after repeated letter
                #set cstringl to len(cstring)
            #else letter is not between pointer and current index (not in cstring)
                #set dict[val] = idx
        #add letter to cstring
        #add length to cstringl
        
        #final check after completing loop
        
        lstring = ""
        lstringl = 0
        cstring = ""
        cstringl = 0
        dict = {}
        pointer = 0
        
        for idx,val in enumerate(s):
            print(cstring)
            if val not in dict:
                dict[val] = idx
            else:
                if dict[val] >= pointer:  #repeat
                    if cstringl > lstringl:
                        lstring = cstring
                        lstringl = cstringl
                    pointer = dict[val]+1
                    index = cstring.find(val)
                    if index+1 > cstringl:
                        cstring = ""
                    else:
                        cstring = cstring[index+1:]
                    cstringl = len(cstring)
            dict[val] = idx
            cstring += val
            cstringl += 1
            
        if cstringl > lstringl:
            lstring = cstring
            lstringl = cstringl
        return lstringl


#Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
class Solution2(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_total = 0
        prev_num = 0
        romanChars  = ['M','D','C','L','X','V','I']
        intChars = [1000,500,100,50,10,5,1]
        for i in range(len(s)-1,-1,-1):
            roman = s[i]
            print(roman)
            num = intChars[romanChars.index(roman)]
            if num < prev_num:
                num_total -= num
            else:                
                num_total += num
            prev_num = num
            
        return num_total
        
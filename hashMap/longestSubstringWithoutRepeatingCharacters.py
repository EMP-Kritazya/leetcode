class Solution:
  # Sol1: Optimal - Sliding Window

    def lengthOfLongestSubstring(self, s: str) -> int:
        myMap = defaultdict(int)
        output = 0

        temp = ""
        for i in range(len(s)):
            if s[i] not in temp:
                temp+=s[i]
            else:
                while s[i] in temp:
                    temp = temp[1:]
                temp+=s[i]
            length = len(temp)
            if(length>output):
                output = length
        return output

  # Sol2: Brute Force
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = defaultdict(int)

        for letters in range(len(s)): 
            string = ""
            for nLetter in s[letters:]:
                if nLetter in string:
                    break
                string += nLetter
            mySet[string] = len(string)
        
        myMap = dict(sorted(mySet.items(), key=lambda item: item[1], reverse = True))
        
        if len(myMap) > 0:
            return list(myMap.values())[0]
        
        return 0
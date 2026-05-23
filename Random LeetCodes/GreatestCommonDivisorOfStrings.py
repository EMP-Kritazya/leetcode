class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Not so optimal - To make it more optimal
        # * introduce factors, and multiply sliced string with the factor and check if that equals the string
        # res = ''
        
        # for i in range(len(str2)-1, -1, -1):
        #     temp = str2[:i+1]

        #     if len(str1)%len(temp)==0 and len(str2) % len(temp)==0:
        #         valid = True
        #         if temp != str2:
        #             for j in range(0, len(str2), i+1):
        #                 if j+i+1 <= len(str2):
        #                     if str2[j:j+i+1] != temp:
        #                         valid = False
        #                         break
        #                 else:
        #                     valid = False
        #                     break
        #         if not valid:
        #             continue
                
        #         for j in range(0, len(str1), i+1):
        #             if j+i+1 <= len(str1):
        #                 if str1[j:j+i+1] != temp:
        #                     valid = False
        #                     break
        #             else:
        #                 valid = False
        #                 break
                
        #         if valid:
        #             return temp

        # return res
                    
        # Insane solution
        if str1+str2 != str2+str1:
            return ""
        
        for i in range(min(len(str1), len(str2)), 0, -1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                return str2[:i]
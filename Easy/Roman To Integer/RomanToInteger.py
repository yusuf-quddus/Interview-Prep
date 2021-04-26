class Solution(object):
    def romanToInt(self, s):
         """
        :type s: str
        :rtype: int
        """
        # Brute Force Method

        solution = 0
        i = 0
        while(i != len(s)):
            if(s[i] == 'M'):
                solution += 1000
            elif(s[i] == 'D'):
                solution += 500
            elif(s[i] == 'C'):
                if (i == len(s)-1):
                    solution += 100
                else:
                    if(s[i+1] == 'D'):
                        solution += 400
                        i += 1
                    elif(s[i+1] == 'M'):
                        solution += 900
                        i += 1
                    else:
                        solution += 100
            elif(s[i] == 'L'):
                solution += 50
            elif(s[i] == 'X'):
                if (i == len(s)-1):
                    solution += 10
                else:
                    if(s[i+1] == 'L'):
                        solution += 40
                        i += 1
                    elif(s[i+1] == 'C'):
                        solution += 90
                        i += 1
                    else:
                        solution += 10
            elif(s[i] == 'V'):
                solution += 5
            elif(s[i] == 'I'):
                if (i == len(s)-1):
                    solution += 1
                else:
                    if(s[i + 1] == 'V'):
                        solution += 4
                        i += 1
                    elif(s[i + 1] == 'X'):
                        solution += 9
                        i+=1
                    else:
                        solution += 1
            i+=1
        return solution
        
       
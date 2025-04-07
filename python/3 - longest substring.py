'''
1.given a string .....
2. find length of substing:
    * which substring length is longest
    * subtring count where no duplicate charecter there
    * 
solution approch: 
loop count string where 

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLenth = 0
        charSet = set()
        left = 0
        n = len(s)

        for right in range(n):
            print(f'charset right is : {charSet}')
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            print(f" righ  {right} - left {left}\n")
            maxLenth = max(maxLenth, right-left+1)
            print(f'left: {charSet}')
            print("___________________________")

        return maxLenth


# test case

s = "bbbbb"

sol = Solution()
result = sol.lengthOfLongestSubstring(s)

print(result)

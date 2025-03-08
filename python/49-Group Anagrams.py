'''

problem statement:
group anagrams : given an array of strings strs, group the anaggrams


Problem Break down:
anagram where each word same but different order
string: abc = [abc,acb,
               bca,bac,
               cab,cba ]
but here need to group of input elements
example:

INPUT str = ['eat', 'tea','tan','ate','nat','bat' ]
lets take fist input eat = eat,ate,tea
                     tan = tan, nat,
                     bat = bat
solve process 1:
    1. sorting all elemets  alphabetic order keep another array
    s = [ ae]
'''


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}

        for i, eachWord in enumerate(strs):
            count = [0] * 26
            for character in eachWord:
                count[ord(character) - ord("a")] += 1

            key = tuple(count)
            print(f' \nBefore Condition {key}')

            if key in res:
                res[key].append(eachWord)

            else:
                res[key] = [eachWord]
                print(f' \nres else condition {res}')

        print(f' before retunr res is : {res}')
        return list(res.values())


# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs = ["eaa", "aea", "tan", "ate", "naa", "bat"]

sol = Solution()
result = sol.groupAnagrams(strs)

print(result)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        word_map = {}
        for str in strs:
            sort_str = "".join(sorted(str))
            if sort_str in word_map:
                word_map[sort_str].append(str)
            else:
                word_map[sort_str] = [str]
        return list(word_map.values())

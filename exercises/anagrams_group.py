from typing import List
def groupAnagrams(strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]
        
        if len(strs) == 2:
            if sorted(strs[0]) == sorted(strs[1]):
                return [[strs[0], strs[1]]]

        ## key: element, value: visited/not visited
        tracker = {}
        
        ## first make everything not yet visited (obviously :v)
        for each in strs:
            tracker[each] = "not visited"
    
        i = 0
        result = []
        while i < len(strs) - 1:
            nxt = i + 1
            # print(f"Current: {strs[i]} and next is: {strs[nxt]}")
            if tracker[strs[i]] == "not visited":
                tracker[strs[i]] = "visited"
                current_anagrams = [strs[i]]
                while nxt < len(strs):
                    if  strs[i] == strs[nxt]:
                        tracker[strs[nxt]] = "visited"
                        current_anagrams.append(strs[nxt])
                    else:
                        if sorted(strs[i]) == sorted(strs[nxt]):
                            if tracker[strs[nxt]] == "not visited":
                                tracker[strs[nxt]] = "visited"
                                current_anagrams.append(strs[nxt])
                    nxt += 1
                # print("current anagrams: ", current_anagrams)
                result.append(current_anagrams)
            # print("So far, visited: ", tracker)
            i += 1
        # print("Remaining is:", strs[nxt])
        for each in tracker:
            if  sorted(strs[nxt]) == sorted(each):
                break
            else:
                result.append([strs[nxt]])
                break
        return result

## test case 1
# strs=["a","b","b", "c"] 
# res = groupAnagrams(strs)
# print(res)

# test case 2
strs=["","b",""]
res = groupAnagrams(strs)
print(res)

## test case 3
# strs = ["act","pots","tops","cat","stop","hat"]
# res = groupAnagrams(strs)
# print(res)
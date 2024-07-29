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
            print(f"Current: {strs[i]} and next is: {strs[nxt]}")
            if tracker[strs[i]] == "not visited":
                tracker[strs[i]] = "visited"
                current_anagrams = [strs[i]]
                while nxt < len(strs):
                    print("nxt is ", nxt)
                    if  strs[i] == strs[nxt]:
                        tracker[strs[nxt]] = "visited"
                        current_anagrams.append(strs[nxt])
                    else:
                        if sorted(strs[i]) == sorted(strs[nxt]):
                            if tracker[strs[nxt]] == "not visited":
                                tracker[strs[nxt]] = "visited"
                                current_anagrams.append(strs[nxt])
                    nxt += 1
                print("End of inner loop, nxt is: ", nxt)
                print("current anagrams: ", current_anagrams)
                result.append(current_anagrams)
            print("So far, visited: ", tracker)
            print()
            i += 1
        print("End of big loop")
        print(f"Nxt: {nxt}")

        ## ese importante
        if nxt == len(strs):
            nxt -= 1

        ## at this stage, there's a chance that the last element is either visited or not yet visited
        tracker_index = 0 
        for each in tracker:
            print("Current word inside visited tracker is", each)
            print("Comparing with the last word...", strs[nxt])
            if  sorted(strs[nxt]) == sorted(each):
                if tracker[each] == "not visited":
                    result.append([strs[nxt]])
                break ## because anagram
            else:
                ## if we are already at the second last element and there's still no anagram matches then just put the last one as separate
                if tracker_index == len(tracker) - 1:
                    result.append([strs[nxt]])
                    break
            print()
            tracker_index += 1
        return result

## test case 1
# strs=["a","b","b", "c"] 
# res = groupAnagrams(strs)
# print(res)

# test case 2
# strs=["","b",""]
# res = groupAnagrams(strs)
# print(res)

# test case 3
strs = ["act","pots","tops","cat","stop","hat"]
res = groupAnagrams(strs)
print(res)

# test case 4
# strs=["aa","b","cc", "dd"]
# res = groupAnagrams(strs)
# print(res)

# test case 5
# strs=["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"]
# res = groupAnagrams(strs)
# print(res)
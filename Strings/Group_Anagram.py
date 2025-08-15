#program : 
#Group words that are anagrams (same letter frequency).

from collections import defaultdict  # for character frequency counting

def group_anagrams(words):

    groups = defaultdict(list)
    for w in words:
        key = "".join(sorted(w))
        groups[key].append(w)
    return list(groups.values())
 
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
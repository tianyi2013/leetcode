def isIsomorphic(s, t):
    """
    Given two strings s and t, determine if they are isomorphic.
    Two strings are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving the order of characters.
    No two characters may map to the same character but a character may map to itself.
    """

    def construct_char_map(word):
        map = {}
        for i, c in enumerate(word):
            if c in map:
                map[c].append(i)
            else:
                map[c] = [i]
        return list(map.values())

    values_s = construct_char_map(s)
    values_t = construct_char_map(t)

    return sorted(values_s) == sorted(values_t)


#print(isIsomorphic("paper", "title"))
print(isIsomorphic("add", "egg"))

"""
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
"""


def word_pattern(pattern, str):

    def get_pattern(input):
        index = {}
        for i, c in enumerate(input):
            if c in index:
                index[c].append(i)
            else:
                index[c] = [i]
        return index

    p1 = get_pattern(pattern)
    p2 = get_pattern(str.split(' '))

    return sorted(p1.values()) == sorted(p2.values())


print(word_pattern("abba", "dog dog dog dog"))
print(word_pattern("abba", "dog cat cat dog"))
print(word_pattern("abba", "abba"))

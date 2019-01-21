def valid_paratheses(string):
    stack = []
    for char in string:
        if char in ['[', '{', '(']:
            stack.append(char)
        elif char == ']':
            if not stack or stack.pop() != '[':
                return False
        elif char == '}':
            if not stack or stack.pop() != '{':
                return False
        else:
            if not stack or stack.pop() != '(':
                return False
    return not stack


print(valid_paratheses("[]"))


def minion_game(string):
    # your code goes here
    def get_all_substrings(input_string):
        return [input_string[0:i] for i in range(2, len(input_string)+1)]

    def add_to_dict(dic, char, index, string):
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
        for sub_string in get_all_substrings(string[index:]):
            if sub_string in dic:
                dic[sub_string] += 1
            else:
                dic[sub_string] = 1

    stuart = {}
    kevin = {}
    for i, char in enumerate(string):
        if char in ['A', 'E', 'I', 'O', 'U']:
            add_to_dict(kevin, char, i, string)
        else:
            add_to_dict(stuart, char, i, string)

    # calculate the final score
    kevin_score = sum(kevin.values())
    stuart_score = sum(stuart.values())
    if kevin_score > stuart_score:
        print('Kevin {}'.format(kevin_score))
    elif kevin_score < stuart_score:
        print('Stuart {}'.format(stuart_score))
    else:
        print('Draw')


def minion_game1(string):
    stuart = 0
    kevin = 0
    for i, char in enumerate(string):
        if char in 'AEIOU':
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin > stuart:
        print('Kevin {}'.format(kevin))
    elif kevin < stuart:
        print('Stuart {}'.format(stuart))
    else:
        print('Draw')



minion_game1('BANANA')

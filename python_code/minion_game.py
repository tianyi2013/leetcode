from timeit import timeit


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
        return 'Kevin {}'.format(kevin_score)
    elif kevin_score < stuart_score:
        return 'Stuart {}'.format(stuart_score)
    else:
        return 'Draw'


def minion_game1(string):
    stuart = 0
    kevin = 0
    for i, char in enumerate(string):
        if char in 'AEIOU':
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin > stuart:
        return 'Kevin {}'.format(kevin)
    elif kevin < stuart:
        return 'Stuart {}'.format(stuart)
    else:
        return 'Draw'


if __name__ == '__main__':
    print('game 1 time used: {}'.format(timeit("minion_game1('BANANABANANABANANA')", setup="from __main__ import minion_game1", number=10000)))
    print('game 2 time used: {}'.format(timeit("minion_game('BANANAABANANABANANA')", setup="from __main__ import minion_game", number=10000)))

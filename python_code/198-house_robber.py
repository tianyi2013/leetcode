def rob(houses):
    if not houses:
        return 0
    elif len(houses) == 1:
        return houses[0]
    else:
        options = []
        for n in range(2, len(houses)+1):
            options.append(sum(houses[0::n]))
            options.append(sum(houses[1::n]))
        return max(options)


print(rob([1, 2]))

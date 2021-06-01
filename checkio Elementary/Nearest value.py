def nearest_value(values: set, one: int) -> int:
    # your code here
    for v in values:
        if v == one:
            return v
        else:
            return min(values, key=lambda x: abs(x-one))

#method 1 has issues with negative numbers

#or without lambda

def nearest_value(values: set, one: int) -> int:
    # your code here
    closest = None
    closestDis = None
    for v in values:
        dist = abs(v - one)
        if closestDis is None or dist < closestDis:
            closest = v
            closestDis = dist
        elif dist == closestDis:
            closest = min(v, closest)
    return closest



if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")

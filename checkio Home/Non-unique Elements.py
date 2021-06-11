#Your optional code here
#You can import some modules or create additional functions


def checkio(data: list) -> list:
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.  

    #replace this for solution
    output = []
    for i in data:
        if data.count(i) > 1:
            output.append(i)
    return output

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list

# or method 2 with remove
def checkio(data: list) -> list:

    output = data[:]
    for i in data:
        if data.count(i) == 1:
            output.remove(i)
    return output


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")

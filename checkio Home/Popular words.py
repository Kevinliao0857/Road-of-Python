def popular_words(text: str, words: list) -> dict:
    # your code here
    wordSplit = text.lower().split()
    return {i: wordSplit.count(i) for i in words}

# or

output = {}
    for i in words:
        output[i] = text.lower().split().count(i)
    return output


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")

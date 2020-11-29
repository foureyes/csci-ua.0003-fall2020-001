"""
alpharange.py
"""
class AlphabetRange:
    pass

if __name__ == '__main__':
    letters = AlphabetRange('D')
    print(letters)
    for letter in letters:
        print(letter)

    letters = AlphabetRange('B', 'E')
    print(letters)
    for letter in letters:
        print(letter)

    letters = AlphabetRange('C', 'L', 2)
    print(letters)
    for letter in letters:
        print(letter)


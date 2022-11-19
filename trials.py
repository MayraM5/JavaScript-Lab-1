"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)     

def get_all_evens(nums):
    evenNums = []

    for num in nums:
        if num % 2 == 0:
            evenNums.append(num)

    return evenNums        

def get_odd_indices(items):
    result = []

    for idx, item in enumerate(items):
        if idx % 2 != 0:
            result.append(item)

    return result


def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f"{i}. {item}")

        i += 1


def get_range(start, stop):
    nums = []

    for num in range(start, stop):
        nums.append(num)
    return nums

def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else:
            chars.append(letter)

    return "".join(chars)


def snake_to_camel(string):
    camelCase = []

    for word in string.split('_'):
        camelCase.append(f'{word[0].upper()}{word[1:]}')

    return ("").join(camelCase)    

def longest_word_length(words):
    longest = len(words[0])
    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest        
        
def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result) - 1]:
            result.append(char)
    return ('').join(result)        

def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == "(":
            parens +=1
        elif char == ")":
            parens -=1
        if parens < 0:
            return False
    return parens == 0            


def compress(string):
    compressed = []

    currchar = ('')
    charcount = 0

    for char in string:
        if char != currchar:
            compressed.append(currchar)

            if charcount > 1:
                compressed.append(str(charcount))

            currchar = char
            charcount = 0

        charcount +=1

    compressed.append(currchar)
    if charcount > 1:
        compressed.append(str(charcount))

    return ('').join(compressed)                    

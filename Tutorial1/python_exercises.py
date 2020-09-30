"""
Intro to python exercises shell code
"""
# returns True if X is odd and False otherwise
def is_odd(x):
    if (x % 2) == 0:
        return False
    else:
        return True

# returns whether 'word' is spelled the same forwards and backwards
def is_palindrome(word):
    length = int(len(word))
    
    for i in range(0, length / 2):
        if word[i] != word(length - i - 1):
            return False
        
    return True

# returns a list of numbers that are odd from numlist
def only_odds(numlist):
    length = len(numlist)
    odd_list = []
    
    for i in range(0, length - 1):
        if is_odd(numlist[i]):
            odd_list.append(numlist[i])
            
    return odd_list

"""
return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
"""
def count_words(text):
    count_dict = {}
    word_list = text.split()
    
    for i in word_list:
        if i in count_dict:
            count_dict[i] = count_dict[i] + 1
        else:
            count_dict[i] = 1
            
    return count_dict
    
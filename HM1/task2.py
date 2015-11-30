#=====Task 2=====

"""You are given a text, which contains different english letters and punctuation symbols. You should
 find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search,
 "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
If you have two or more letters with the same frequency, then return the letter which comes first
in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we
choose "e".
Input: A text for analysis as a string (unicode for py2.7).
Output: The most frequent letter in lower case as a string.
Example:
most_frequent_letter("Hello World!") == "l"
most_frequent_letter("How do you do?") == "o"
most_frequent_letter("One") == "e"
most_frequent_letter("Oops!") == "o"
most_frequent_letter("AAaooo!!!!") == "a"
most_frequent_letter("abe") == "a"""""

def most_frequent_letter(text):
    text = text.lower()
    count = 0
    for letter in text:
        if letter.isalpha() and text.count(letter) >= count:
            if text.count(letter) == count:
                frequent += letter
            else:
                frequent = letter
                count = text.count(letter)
    return min(frequent)

print most_frequent_letter("How do you do?")


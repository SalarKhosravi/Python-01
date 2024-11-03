# Importing the re module
print('---------------------------------------------------')
import re

# Basic search with a pattern
print('---------------------------------------------------')
text = "The rain in Spain falls mainly in the plain."



# Search for the first occurrence of "ain"
match = re.search("ain", text)
print("First 'ain' found at position:", match.start() if match else "No match found")



# Finding all occurrences of a pattern
print('---------------------------------------------------')
# Find all words ending with 'ain'
all_matches = re.findall(r"\b\w*ain\b", text)
print("All words ending with 'ain':", all_matches)




# Splitting a string based on a pattern
print('---------------------------------------------------')
# Split the string at each whitespace
split_text = re.split(r"\s", text)
print("Split text by whitespace:", split_text)





# Splitting with a limit
split_text_limit = re.split(r"\s", text, maxsplit=3)  # Limit splits to 3 parts
print("Split text by whitespace (limited to 3):", split_text_limit)





# Replacing parts of a string with a pattern
print('---------------------------------------------------')
# Replace all occurrences of "ain" with "123"
replaced_text = re.sub("ain", "123", text)
print("Replaced 'ain' with '123':", replaced_text)





# Using groups and capturing parts of a pattern
print('---------------------------------------------------')
# Find "rain in Spain" and capture the words before and after "in"
pattern = r"(\w+) in (\w+)"
group_match = re.search(pattern, text)
if group_match:
    print("Match groups:", group_match.groups())  # Returns all groups as a tuple
    print("First group:", group_match.group(1))   # 'rain'
    print("Second group:", group_match.group(2))  # 'Spain'




# Using special sequences
print('---------------------------------------------------')
# Find all digits in a string
digit_text = "There are 3 cats and 4 dogs."
digits = re.findall(r"\d", digit_text)
print("All digits:", digits)






# Compiling a pattern for reuse
print('---------------------------------------------------')
# Compile a pattern to find all words
word_pattern = re.compile(r"\b\w+\b")
words = word_pattern.findall(text)
print("All words in text:", words)







# Using flags for case-insensitive matching
print('---------------------------------------------------')
case_text = "Python is Fun. python is powerful."
matches_case_insensitive = re.findall(r"python", case_text, re.IGNORECASE)
print("Case-insensitive matches for 'python':", matches_case_insensitive)










# Essential Regular Expression Symbols
# --------------------------------------------------
# .      - Matches any character (except newline)
#          Example: `a.b` matches "acb", "a1b"
#
# \d     - Matches any digit (0-9)
#          Example: `\d+` matches "123", "4567"
#
# \w     - Matches any word character (alphanumeric + underscore)
#          Example: `\w+` matches "hello", "test_123"
#
# \s     - Matches any whitespace (spaces, tabs, newlines)
#          Example: `\s+` matches " " in "hello world"
#
# ^      - Matches the start of a string
#          Example: `^Hello` matches "Hello world" only at the start
#
# $      - Matches the end of a string
#          Example: `world$` matches "hello world" only at the end
#
# *      - Matches 0 or more repetitions
#          Example: `a*` matches "", "a", "aaa"
#
# +      - Matches 1 or more repetitions
#          Example: `a+` matches "a", "aaa" (but not "")
#
# ?      - Matches 0 or 1 repetition (optional)
#          Example: `colou?r` matches "color" and "colour"
#
# {n}    - Matches exactly `n` repetitions
#          Example: `\d{3}` matches "123"
#
# []     - Matches any character inside brackets
#          Example: `[aeiou]` matches any vowel
#
# |      - Alternation (or)
#          Example: `a|b` matches "a" or "b"
#
# ()     - Captures matched content as a group
#          Example: `(ab)+` matches "abab"
# --------------------------------------------------

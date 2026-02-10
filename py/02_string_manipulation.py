single_quote = 'Hello'
double_quote = "World"
triple_quote = """Multi-line
string
2026"""

print(single_quote)
print(type(single_quote))
print(double_quote)
print(type(double_quote))
print(triple_quote)
print(type(triple_quote))

test_word = 'Python-bootcamP 2026'

print(test_word[0])      #first character
print(test_word[-1])     #last character
print(test_word[0:6])    #from start to 6th character
print(test_word[:6])     #from start to 6th character too
print(test_word[7:])     #from 8th charater to finish

print(len(test_word))                   #find length string
print(test_word.strip())                #remove space
print(test_word.upper())                #UPPERCASE string
print(test_word.lower())                #lower string
print(test_word.title())                #only first each sentence big letter
print(test_word.replace("2026", "C5"))  #replace specific string
print(test_word.split())                #split into list
print(test_word.split()[1])             #split and print selected index
print(len(test_word.split()))           #count total word (detect by space)
print(test_word.count("-"))             #count symbol/character in bracket

coding = "Python"
no_student = 35

msg_1 = f"Class today: {coding}, Student: {no_student}"             #f-string method
msg_2 = "Class today: {}, Student: {}".format(coding, no_student)   #str.format()
msg_3 = "Class today: %s, Student: %d" % (coding, no_student)       #%-formatting %s = string, %d = decimal, %f = float, %g = general

print(msg_1)
print(msg_2)
print(msg_3)



#exercise
instruction = "Build a simple text analyzer that counts words, characters, and sentences in a given text."

text_example = """Python is a powerful programming language. It's easy to learn
and versatile!
You can use Python for web development, data science, and
automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""

words = len(text_example.split())
char = len(text_example)
char_nospace = len(text_example.replace(" ", ""))
sent = text_example.count(".") + text_example.count("!") + text_example.count("?")

print(f"Words count: {words}")
print(f"Character count w space: {char}")
print(f"Character count w/o space: {char_nospace}")
print(f"Sentence count: {sent}")
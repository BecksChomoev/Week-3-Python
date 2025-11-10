import string

translator = str.maketrans('', '', string.punctuation)
user_input = input('Welcome to Word Counter program! '
                   'The program will count the occurrences of each word. Enter your sentence: ').lower().translate(translator)
occurrences = {}

user_input = user_input.split()

for word in user_input:
    if word in occurrences:
        occurrences[word] += 1
    else:
        occurrences[word] = 1

print(occurrences)
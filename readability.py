# determine the reading score of text input by the user
import string

# get input from user
text = input("Text: ")

numChars = len(text)
numLetters = 0
numWords = 0
numSentences = 0

for i in range(numChars):
    # print("Letter: ",text[i])

    # count the number of sentences
    if text[i] == '!' or text[i] == '.' or text[i] == '?':
            numSentences += 1
            # print("NumSentences: ",numSentences)

    # count the number of letters
    if text[i] >= 'A' and text[i] <= 'z':
        numLetters += 1
        # print("NumLetters: ",numLetters)

    # count the number of words

    if i>0 and (text[i].isspace() or text[i] in string.punctuation) and ( not text[i-1].isspace() or not text[i-1] in string.punctuation):
        if not( (i < numChars-1) and (text[i] in string.punctuation) and text[i-1].isalpha() ):
            #do nothing
            numWords += 1
            # print("numWords: ",numWords)

s = ( numSentences / numWords ) * 100 #average number of sentences per 100 words
l = (  numLetters ) /  numWords * 100 #average number of letters per 100 words

# print("Summary:")
# print(numSentences)
# print(numLetters)
# print(numWords)
# print(s)
# print(l)
index =  (0.0588 * l) - (0.296 * s) - 15.8

if index < 0.5:
    print("Before Grade 1")
elif index > 15:
    print("Grade 16+")
else:
    print("Grade %i" % round(index,0))
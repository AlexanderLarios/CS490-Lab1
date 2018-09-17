#This program takes the words in file1.txt and file2.txt and returns the words from file1 that were not in file 2.
file1Words = []
file2Words = []
# read_in: reads the words in the text file into an array
# @param fname: string file name
def read_in(fname):
    fileWords = []
    with open(fname,'r') as f:
        for line in f:
            for word in line.split(' '):
                fileWords.append(word)
    return fileWords
# remove_words: loops through the words in the second array and checks if they are present in the first arary, if the word
# exists in both arrays then it removed from the first array of words from file1
# @param firstWords: array containing string elements
# @param secondWords: array containing string elements
def remove_words(firstWords, secondWords):
    for word in secondWords:
            if word in firstWords:
                firstWords.remove(word)
    return firstWords
file1Words = read_in('file1.txt')
file2Words = read_in('file2.txt')
result = remove_words(file1Words, file2Words)
# print first file words and second file words then the result
print(file1Words)
print(file2Words)
print(result)

#NOTE: I noticed in the example that the words included the punctuation
# so I used a space as a delimiter when reading the words into the arrays
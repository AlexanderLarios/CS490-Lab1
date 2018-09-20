# get the user input
sString = input("Enter the string you want to check for duplicates\n")
# remove spaces
sString = sString.replace(" ", "")
# convert the string to a list of characters
listString = list(sString)
returnList = []
# iterate through the characters
for i in listString:
    # in python the count function counts the number of occurances of a specific character in a list
    result = listString.count(i)
    # if the returned integer is 1 then add the character to the unique character list
    if result == 1:
        returnList.append(i)
# print out the first character returned
print(returnList[0])


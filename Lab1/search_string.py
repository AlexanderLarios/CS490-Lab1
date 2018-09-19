sString = input("Enter the string you want to check for duplicates\n")
sString = sString.replace(" ", "")
listString = list(sString)
returnList = []
for i in listString:
    result = listString.count(i)
    if result == 1:
        returnList.append(i)
print(returnList[0])


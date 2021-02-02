def secondLargestInt():
    userList = []
    length = int(input("enter size of list:" ))


    for i in range(0,length):

        uInput = int(input("Enter an Integer: "))
        userList.append(uInput)

    max = userList[0]
    secMax = userList[0]
    for x in userList:
        if x > max:
            secMax = max # when a value is found to be greater than max, it moves the old max value to second max before updating the max value
            max =x
        if x <max and x > secMax:
            secMax=x #when ever the code finds value that is less than max but greater than second max it replaces the second max with that value to catch cases that the first if statemnent doesnt
    return str(secMax) + " is the second largest integer from your list " + str(userList)
print(secondLargestInt())

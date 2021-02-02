
print("enter an integer to be reversed")
intx= input()
intx = int(intx)
def ReverseInteger(intx):
    revs =0
    sign = 1
    if intx < 0:
        sign =-1
        intx = intx * -1
    while intx >0:
        revs = revs*10
        revs += intx%10

        intx = int(intx/10)

    return revs*sign

print(ReverseInteger(intx))

from cs50 import *

#initialize card to invalid
cardType = "INVALID"

cardNo = get_string("Number: ")
length = len(cardNo)

if length < 13 or length > 16:
    print(cardType)
    exit(0)


productSum = 0
sum = 0

firstTwo = int(cardNo[0:2])
# print(firstTwo)

for i in range(length):
    if i%2 == 0:
        sum += int(cardNo[length-1-i])
    else:
        mult = 2*int(cardNo[length-1-i])
        # print(str(mult))
        for i in str(mult):
            productSum += int(i)

# print("productSum: %i, sum: %i" % (productSum,sum))
# print(sum + productSum)

if (sum+productSum) % 10 == 0:
    if length == 15 or (firstTwo == 34 or firstTwo == 37):
        cardType = "AMEX"
    elif length == 16 and (firstTwo >= 51 and firstTwo <= 55):
        cardType = "MASTERCARD"
    elif (length == 13 or length == 16) and (firstTwo / 10 == 4):
        cardType = "VISA"

print(cardType)


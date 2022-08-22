# Guess Game Exercise
i = 0
gess = 34
j = 5
print(" You have 5 attempts, Good Luck")
while(i<5):
    num = int(input(" Enter Number to match: "))
    if num == gess:
        print(" Congratulations your guess number is correct. ")
        print(" Number of guesses you took to finish is: ", i+1)
        break
    elif num < gess:
        print(" Wrong Guess, number is greater then ", num)
        print(" Number of guesses Left is: ", j - 1)
        i = i+1
        j= j-1
    else:
        print(" Wrong Guess, number is less then ", num)
        print(" Number of guesses Left is: ", j - 1)
        i = i + 1
        j= j-1
if i == 5:
    print(" Game Over Your attempts are complete, Better luck next time. ")

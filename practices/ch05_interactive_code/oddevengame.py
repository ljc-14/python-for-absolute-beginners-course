entry_limit = float("inf")
entry = 0

while entry < entry_limit:
    num_text = input("Pick a number... ")
    num = int(num_text)
    rem = num % 2

    if(num == 0):
        print("goodbye")
        break
    elif(rem == 0):
        print("That is an EVEN number")
    else:
        print("That is an ODD number")

print("WELCOME TO THE PYTHON PIZZA !")
size= str(input("What size of pizza do you want ? S,M or L\n" ""))
bill= 0


if size== "S":
    bill = 15
    print("You have to pay $15.")

elif  size== "M":
    bill = 20
    print("You have to pay $20.")

else :
    bill = 25
    print("You have to pay $25.")


add_papperoni = input("Do you want to add papperoni ? Y or N\n")
if add_papperoni == "Y":
    if size == "S":
        bill += 2
        print(f"Your final bill is ${bill}")
    else:

        bill += 3
        print(f"Your final bill is ${bill}")
else:
    print(f"Your final bill is ${bill}")


extra_cheese= input("Do you want extra cheese ? Y or N \n")
if extra_cheese== "Y":
    bill += 1
    print(f"Your final bill is ${bill}")

else:
    print(f"Your final bill is ${bill}")





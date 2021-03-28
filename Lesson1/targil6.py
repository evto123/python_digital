## for Loops
from time import sleep
print("Now we we will get all the details about your class: \n------------\n ")
for i in range(4):

    name=input("Enter a name: ")
    age=int(input("Enter an age: "))
    phone=input("Enter a phone: ")
    print("Printing student number " +str(i) + "Details....\n ")
    sleep(2)
    print("\nFull name " + name + "\nAge " +str(age) + "\nPhone" + phone + "\n-----------------\n" )
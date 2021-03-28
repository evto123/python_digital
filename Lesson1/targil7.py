## while loops
''''''

#counter=10
#while(counter>0):
#    print(counter*100)
#   print("Evgeniy Toeskin")
#  counter=counter-1

''''''

while(True):
    name=input("Enter your name:")
    if(name=="Evgeniy"):
        print("Hello Evgeniy")
        break
    elif(name=="Ben"):
        continue
    else:
        print("Where is Evgeniy?")
        number=int(input("Enter a number: "))
        print(number*4)
print("Bye,Bye....")



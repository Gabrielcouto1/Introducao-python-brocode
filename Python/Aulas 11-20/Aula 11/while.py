# while loop =  a statement that will execute it's block of code,
#                        as long as it's condition remains true

#while 1==1:
#    print("\nHelp! I'm stuck in a loop")

name = ""
name = None

#while len(name) == 0:
while not name:
    name = input("Enter your name: ")

print("Hello " + name.capitalize() + "!!")

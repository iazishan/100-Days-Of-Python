### how to create function
### Defination 


def move():    ##### defining Functions
    i=20
    print(i)

move()  ####   calling functions



### creating functions

###use def /// defining function
###parenthesis contains variables objects

def get_milk():
    print("1.Go straight 2m.")
    print("2.Go left 2m.")
    print("3.Go right 2m.")
    print("4.Get milk from shop.")
    print("Come back.")

choice=input("Use Robot To get milk. y/n:")
if choice=='y':
    get_milk()
else:
    print("thanks")

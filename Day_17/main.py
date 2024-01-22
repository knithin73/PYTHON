class User:         # to name a class, need first letter of every word capitalised (Pascal Case)
    def __init__(self):
        print("New object is created")


user1 = User()       # User is the class and user1 is the Object
user2 = User()


def function():
    pass


user1.id = "001"     # here .id is the attribute
user1.username = "Nithin"
user1.power  = "GTT"

print(user1.username)
print(user1.power)


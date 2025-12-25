# Using Python Classes and Objects

from models.user import User

user1 = User(1, "Jagath", "17jagathvm@gmail.com")

print(user1.to_dict())

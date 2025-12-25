# OOP Classes and Objects

class User:
  def __init__(self, user_id, name, email):
    self.user_id = user_id
    self.name = name
    self.email = email

  def to_dict(self):
    return {
      "id": self.user_id,
      "name": self.name,
      "email": self.email
    }

# class User: → blueprint for creating users
# __init__ → constructor (runs when object is created)
# self → refers to current object
# attributes: user_id, name, email
# to_dict() → converts object to dictionary (VERY useful for APIs)

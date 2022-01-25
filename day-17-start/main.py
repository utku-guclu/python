class User:
    
    def __init__(self, user_id, username):   # parameters
        # assigning attributes to parameters
        self.id = user_id
        self.username = username
        self.status = 0
        print("new user is being created..")
        
    def greet(self):
        return f"{self.username} saluts you."

user1 = User("009", "jack")   # arguments

# user1.user_id = "009"
# user1.user_name = "jack"

print(user1.greet())

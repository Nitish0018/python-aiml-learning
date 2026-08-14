class user:
    def __init__(self, username):
        self.username = username
    def join_chat(self, chatroom):
        chatroom.join(self)
    def Leave_chat(self, chatroom):
        chatroom.Leave(self)

class message:
    def __init__(self, Sender, Text):
        self.Sender = Sender
        self.Text = Text

    def display(self):
        print(self.Sender.username + ": " + self.Text)

class chatroom:
    def __init__(self, name):
        self.name = name
        self.user = []
        self.messages = []

    def join(self, user):
        self.user.append(user)
        print(user.username + " has joined the chatroom.")

    def Leave(self, user):
        self.user.remove(user)
        print(user.username + " has left the chatroom.")

    def send_message(self, user, Text):
        if user in self.user:
            msg = message(user, Text)
            self.messages.append(msg)
            print(user.username + "sent: " + Text)
        else:
            print(user.username + " is not in the chatroom.")
    def view_history(self):
        print("Chat history in " + self.name + ":")
        for msg in self.messages:
            msg.display()   

# Create users
user1 = user("Nitish")
user2 = user("Rahul")

# Create chatroom
chatroom1 = chatroom("Python Chatroom")

# Users join
user1.join_chat(chatroom1)
user2.join_chat(chatroom1)
# Send messages
chatroom1.send_message(user1, "Hello everyone!")
chatroom1.send_message(user2, "Hi Nitish!")

# View chat history
chatroom1.view_history()

# User leaves
user2.Leave_chat(chatroom1)



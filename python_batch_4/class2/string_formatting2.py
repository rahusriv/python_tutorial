name = input("Enter your name :")
address = input("Enter yoiur address: ")

message = "Hello {0}, Welcome to {1}. I am glad that {0} is in {1}.".format(name,address)
#message_after_replacement = message.format(name,address)

print(message)
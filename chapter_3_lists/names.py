from email import message


names = ['jack', 'john', 'marry']

print(names[0])
print(names[1])
print(names[2])

message_to_jack = f"Hello {names[0].title()}, how are you?"

print(message_to_jack)

message_to_marry = f"Hello {names[2].title()}, how are you?"

print(message_to_marry)
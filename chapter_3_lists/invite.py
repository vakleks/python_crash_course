invite = ['Mozart', 'Bah', 'Bethoven']
message = "Hello, nice to see You, dear"
print(f"{message} {invite[0]}.")
print(f"{message} {invite[1]}.")
print(f"{message} {invite[2]}.")

cant_vizit = invite[1]
print(f"{cant_vizit} can't vizit.")

invite[1] = "Einstein"
print(f"{message} {invite[0]}.")
print(f"{message} {invite[1]}.")
print(f"{message} {invite[2]}.")

invite.insert(0, 'Vivaldi')
print(invite[0])
print(invite)

invite.append('Bah')
print(invite)

print(len(invite))


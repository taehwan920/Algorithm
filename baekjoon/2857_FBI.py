FBI = False
FBIs = []
for i in range(1, 6):
    agent = input()
    if "FBI" in agent:
        FBI = True
        FBIs.append(i)
if FBI:
    for i in FBIs:
        print(i, end=" ")
else:
    print('HE GOT AWAY!')

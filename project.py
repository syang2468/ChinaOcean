passwords = 0

for i in range(0, 8):
    for j in range(i+1, 8):
        if i != j:
            for k in range(j+1, 8):
                if k != i and k != j:
                    passwords += 1
                    password = ""
                    for a in range(8):
                        if a == i or a == j or a == k:
                            password = password + "0"
                        else:
                            password = password + "1"
                    print(password)

print(passwords)

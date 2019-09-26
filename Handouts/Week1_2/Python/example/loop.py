my_list = [1, 2, 3, 4]

for i in my_list:
    print(i)
for i in range(10):
    print(i)
for i in range(1, 10):
    print(i)
for i in range(1, 10, 2):
    print(i)

count = 0

while count < 10:
    print(count)
    count += 1

count = 0

while count < 10:
    count += 1
    if count == 5:
        break
    print("inside loop", count)

print("out of while loop")

count = 0

while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)

s = int(input())
counter = ""
new_counter = ""
while s > 0:
    if s % 2 == 1:
        counter += "1"
    else:
        counter += "0"
    s = s // 2
print(counter)
for _ in range(len(counter) - 1, -1, -1):
    new_counter += counter[_]
print(new_counter)





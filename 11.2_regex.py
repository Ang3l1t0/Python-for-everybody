import re

add = 0
file = open('example.txt')
for line in file:
    numbers = re.findall('[0-9]+', line)
    for n in numbers:
        add += int(n)
print(add)
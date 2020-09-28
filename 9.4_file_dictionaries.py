# 9.4 Write a program to read through the mbox-short.txt and 
# figure out who has sent the greatest number of mail messages

name = "mbox-short.txt"
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for w in words:
        if w == 'From':
            next_word = words[words.index('From') + 1]
            di[next_word] = di.get(next_word, 0) + 1
        else:
            pass

largest = -1
theword = None
for k,v in di.items():
    if v > largest:
        largest = v
        theword = k

print(theword, largest)
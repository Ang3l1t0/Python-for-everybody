name = "mbox-short.txt"
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for w in words:
        if w == 'From':
            next_word = words[words.index('From') + 5]
            next_word = next_word.split(':')
            di[next_word[0]] = di.get(next_word[0], 0) + 1
        else:
            pass

x = sorted(di.items())
for k,v in x:
    print(k,v)
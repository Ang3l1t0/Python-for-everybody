fname = ("romeo.txt")
fh = open(fname)
lst = []
for line in fh:
    phrase = line.split()
    for word in phrase:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)

words = []
lst = []
with open('Desktop/romeo.txt') as fp:
    for line in fp.readlines():
        for word in line.split():
            if word not in words:
                words.append(word)


print(sorted(words))
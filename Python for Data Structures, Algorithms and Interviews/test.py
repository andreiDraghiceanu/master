n = 4321

word_split = ("themanran", ["muie", "the", "man", "ran", "la"])

for i in word_split[1]:
    if i in word_split[0]:
        print(i)

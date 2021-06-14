string = "This is the best"

def rev_sentence(s):
    return " ".join(reversed(s.split()))
    

def rev_sen(s):
    rev_list = []
    words = []
    length = len(s)
    spaces = [' ']

    i = 0

    while i < length:

        if s[i] not in spaces:

            word_start = i

            while i < length and s[i] not in spaces:

                i +=1

            words.append(s[word_start:i])


        i +=1
    count=0
    for count in range(len(words)):
        count += 1 
    
    for index in range(len(words)):
        index +=1
        rev_list.append(words[count-index])
        sentence = " ".join(rev_list)
    return sentence

print(rev_sen(string))

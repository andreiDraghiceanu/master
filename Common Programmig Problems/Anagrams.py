f_name = 'word'
s_name = 'drow'

if len(f_name) == len(s_name):
    for i in f_name:
        if f_name[0] == s_name[-1]:
            print(f_name[0] + "=" + s_name[-1])
        else:
            print(f_name[0] + "=" + s_name[-1])
            print("The two words aren't anagrams!")
            break
        f_name = f_name[1:]
        s_name = s_name[:-1]
    print("The words are anagrams!!!")
else:
    print("The words have different lengths!!!")
        

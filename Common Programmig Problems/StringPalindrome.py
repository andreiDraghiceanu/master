name = "annxa"

for i in name:
    try:
        if i == name[-1]:
            print(i +' = '+ name[-1])
        else:
            print("This is not a palindrome!!!")
            break
        name = name[1 : -1]
    except IndexError:
        print("This is a palindrome!!!")
        break
            
    

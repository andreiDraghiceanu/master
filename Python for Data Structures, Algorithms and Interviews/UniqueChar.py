s = "aaabcdde"

def uni_char(s):
    return len(set(s)) == len(s)


def uni_char2(s):

    chars = set()
    
    for let in s:
        if let in chars:
            return False
        else:
            char.add(let)
    return True


    

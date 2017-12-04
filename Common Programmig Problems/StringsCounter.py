def count_strings(words):
   count = 0
   for word in words:
      if len(word) >= 2 and word[0] == word[-1]:
        count = count + 1
        # you can also use count+=1
   return count

l_words = ['aba', 'xyz', 'aa', 'x', 'bbb', 'xfr', 'lol', 'mum']
print ("List:", l_words)

cnt = count_strings(l_words)
print ("Found", cnt, "strings with length higher than 2 and begin and last with the same letter!")

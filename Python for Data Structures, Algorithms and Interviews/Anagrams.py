from nose.tools import assert_equal

word0 = "public relations"
word1 = "crap built on lies"

def anagram(word0, word1):
    word0 = word0.replace(" ", "").lower()
    word1 = word1.replace(" ", "").lower()
    if len(word0) == len(word1):
        for i, j in zip(word0, word1):
            if i in word1 and j in word0:
                return True
    else:
        return False

class AnagramTest(object):

    def test(self, solution):
        assert_equal(solution("go go go", "gggooo"), True)
        assert_equal(solution("abc", "cba"), True)
        assert_equal(solution("hi man", "hi        man"), True)
        assert_equal(solution("aabbcc", "aabbc"), False)
        assert_equal(solution("123", "1 2"), False)
        print("ALL TEST CASES PASSED")

t = AnagramTest()
t.test(anagram)

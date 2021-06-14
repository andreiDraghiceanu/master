from nose.tools import assert_equal
import collections

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]

def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
        


class Test(object):

    def test(self, solution):
        assert_equal(solution([5,5,7,7], [5,7,7]), 5)
        print("ALL TEST CASES PASSED")

t = Test()
t.test(finder)

def finder2(arr1,arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        print(d[num])
        if d[num] == 0:
            return num

        else:
            d[num] -=num


print(finder2(arr1, arr2))


def finder3(arr1, arr2):
    result=0

    for num in arr1+arr2:
        result^=num
        print(result)
    return result

print(arr1+arr2)

import os

'''Old way to work with files'''
# f = open('test.txt', 'r')
#
#
# print(f.name)
# print(f.mode)
#
#
# f.close()

print(os.getcwd())
print()

# with open('test.txt', 'w') as f:

    # '''Method for reading a file line to line'''
    # for line in f:
    #     print(line, end='')

    # '''Method for reading a file with a fixed number of characters'''
    # size_to_read = 4
    #
    # f_contents = f.read(size_to_read)
    # f.seek(0)
    # f_contents = f.read(size_to_read)
    #
    # print(f.tell())
    # f.seek(0)
    #
    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read)

    # f.write('Test')
    # f.seek(0)
    # f.write('R')



# print(f.closed)

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)



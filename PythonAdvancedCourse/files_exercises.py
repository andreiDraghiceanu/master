def grep(text, filename):
    with open(filename) as f:
        return [line for line in f if text in line]


res = grep('write', 'files_examples.py')  # res is list
for matching_line in res:
    print(matching_line)


def grep_gen(text, filename):
    with open(filename) as f:
        for line in f:
            if text in line:
                yield line


res = grep_gen('write', 'files_examples.py')  # res is iterator
for matching_line in res:
    # input()
    print(matching_line)


def grepinto(text, infile, outfile):
    with open(infile, 'r') as fin, open(outfile, 'w') as fout:
        for line in fin:
            if text in line:
                fout.write(line.lstrip())


grepinto('write', 'files_examples.py', 'write.txt')

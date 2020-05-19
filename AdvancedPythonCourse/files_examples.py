import json


with open('aggregations.py') as f:
    for line in f:
        if not line.startswith('#') and len(line) > 1:
            print(line, end='')
    f.seek(0)
    first_10 = f.read(10)
    all_lines = f.readlines()  # not recommended


with open('test.txt', 'w') as f:
    f.write("a:1, b:2, c:3")

with open('test.txt', 'r') as f:
    for line in f:
        pairs = line.split(', ')
        # d = {a: int(b) for a, b in [pair.split(':') for pair in pairs]}
        d = {}
        for pair in pairs:
            a, b = pair.split(':')
            d[a] = int(b)
    print(d)
    with open('d.json', 'w') as fjson:
        json.dump(d, fjson, indent=2)
    with open('d.json') as fjsonread:
        obj = json.load(fjsonread)
        print(type(obj))
        print(obj)

with open('test.txt', 'wb') as f:
    f.write('Bună\n'.encode())
    f.writelines([b'Hello world\n', b'How are you?\n'])

with open('test.txt', 'rb') as f:
    for line in f:
        print(line)
        print(line.decode())

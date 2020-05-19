import argparse


def func(args):
    return ''.join([str(arg) for arg in args])


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='NUMBER', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=func,
                    help='sum the integers (default: find the max)')
parser.add_argument('--print', action='store_const', const=True, default=False)


args = parser.parse_args()

if args.print:
    print(args.integers)
    print(args.accumulate(args.integers))
else:
    print('No message')

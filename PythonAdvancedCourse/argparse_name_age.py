import argparse


parser = argparse.ArgumentParser(description='Display hello')
parser.add_argument('name', type=str, help='Name of the person')
parser.add_argument('age', type=int, help='Current age')
args = parser.parse_args()

args.age += 10

print(f'Hello, {args.name}! In 10 years you will be {args.age}')

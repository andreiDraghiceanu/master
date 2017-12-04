import os
from datetime import datetime

# print(os.getcwd())
os.chdir('/Users/andre/Desktop/')

# os.mkdir('OS-Demo-2')
# os.rmdir('OS-Demo-2')
# os.makedirs('OS-Demo-2/Sub-Dir-1')
# os.removedirs('OS-Demo-2/Sub-Dir-1')
# os.rename('text.txt', 'demo.txt')
# print(os.listdir())

'''Convert variable that contains time info about a file to a Human Readable format then Print'''

mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

'''This loop generates a filetree '''

# for dirpath, dirnames, filenames in os.walk('/Users/andre/Desktop/'):
#     print('Current Path:', dirpath)
#     print('Directories', dirnames)
#     print('Files', filenames)
#     print()

'''Get the path to the Enviroment Variables'''
# print(os.environ.get('PATH'))
#
# file_path = os.path.join(os.environ.get('PATH'), 'test.txt')
# print(file_path)

print(os.path.basename('tmp/test.txt'))
print(os.path.dirname('tmp/test.txt'))
print(os.path.split('tmp/test.txt'))
print(os.path.exists('tmp/test.txt'))
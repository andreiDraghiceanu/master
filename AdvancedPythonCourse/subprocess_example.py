import subprocess


process1 = subprocess.run(['echo', '7'], capture_output=True)
process2 = subprocess.run(['echo', process1.stdout])

# Uses shell - not recommended
# subprocess.run('ps aux | grep py', shell=True)


process = subprocess.run('grep hello'.split(), input=b'hello world\nhello\nbye', stdout=subprocess.PIPE)
print(process.stdout.decode())

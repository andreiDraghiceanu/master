import sys
import re

def read_file(filename):
    fid = open(filename, 'r')
    text = fid. read()
    fid.close()
    return text

def parse_text(txt):
    n_list = re.findall(r'Name:\s*(\S+)\s+Surname:\s*(\S+)', txt)
    return n_list

def write_file (n_list):
  fout = open("filtered_employ_list.txt","w")

  for name_surname in tuples:
    # unpack the tuple into 2 vars
    (name,surname) = name_surname
    # generate the string in the correct format
    str_to_write = "Name: " + name + " Surname:" + surname + "\n"
    # write the string in the file
    fout.write(str_to_write)
  fout.close()

def main():
    if len(sys.argv) != 2:
        print ('usage: ./get_employee_name.py file-to-read')
    sys.exit(1)

file_text = read_file(sys.argv[1])
print (file_text)
filtered_text = parse_text(file_text)
print (filtered_text)
write_file(filtered_text)

if __name__ == '__main__':
  main()

import os

os.chdir('/Users/andre/Desktop/TestPhoto')
print(os.getcwd())

# for f in os.listdir():
#     try:
#         file_name, file_ext = os.path.splitext(f)
#         f_num, f_low, f_res, f_pix = file_name.split('_')
#         f_pix = f_pix.strip()[0:3].zfill(4)
#         f_end = '.jpg'
#
#         new_name = '{}_{}_{}_{}'.format(f_low, f_res, f_pix, f_num)
#         new_name = new_name-f_end
#         os.rename(f, new_name)
#     except:
#         print(end='')
#         continue

for f in os.listdir():
    try:
        file_name, file_ext = os.path.splitext(f)
        f_end = '.jpg'

        new_name = '{}_{}'.format(file_name, file_ext)
        new_name = file_name
        os.rename(f, new_name)
    except:
        print(end='')
        continue


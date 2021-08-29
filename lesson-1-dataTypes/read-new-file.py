with open('my_new_file.txt', mode='r')as f:
    print(f.read())
# create new or overwrite
with open('my_new_file_new.txt', mode='w')as f:
    f.write('/n lorem ipsum')

with open('my_new_file_new.txt', mode='r')as f:
    print(f.read())

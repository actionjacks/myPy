myfile = open('notepad.txt')
print(myfile)
print(myfile.read())

# after read file set cursor back to start
myfile.seek(0)
print(myfile.readlines())

# pwd - python working directory
myfile.close()

with open('notepad.txt') as my_new_file:
    contents = my_new_file.read()

with open('notepad.txt', mode='r') as myfiletwo:
    contents = myfiletwo.read()
print(contents)



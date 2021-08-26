myfile = open('notepad.txt')
print(myfile)
print(myfile.read())

# after read file set cursor back to start
myfile.seek(0)
print(myfile.read())

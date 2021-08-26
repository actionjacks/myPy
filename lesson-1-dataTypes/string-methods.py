name = 'jacek'
# name[0] = 'p' -cant string immutable
last_letters = name[1:]

name = 'p' + last_letters
# to change need reasing new variable

print(name)

print('this is a string {}'.format('LOREM'))
print('the {2} {0} {1}'.format('fox', 'cow', 'dog'))
# {index of item after .format}
print('the {c} {a} {b}'.format(a='fox', b='cow', c='dog'))


result = 100/77
print(result)
# r give white spaces
print('the result was {r:1.3f}'.format(r=result))

name2 = 'zbyszek'
print(f'hello, his name is {name2}')

word = input().lower()

trans_croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in trans_croatia:
    word = word.replace(i, '*')

print(len(word))
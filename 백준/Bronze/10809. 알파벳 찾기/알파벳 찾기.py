word = input()
alphabet = [chr(ord('a') + i) for i in range(26)]

result = [word.find(alpha) for alpha in alphabet]
print(*result)
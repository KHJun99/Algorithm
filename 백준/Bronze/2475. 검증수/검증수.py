unique_number = list(map(int, input().split()))

number_of_verifications = 0

for num in unique_number:
    number_of_verifications += num ** 2

print(number_of_verifications % 10)
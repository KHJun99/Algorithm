wrong_hour, wrong_minute = map(int, input().split(':'))
target_hour, target_minute = map(int, input().split(':'))

if wrong_minute > target_minute:
    target_minute += 60
    target_hour -= 1

if wrong_hour > target_hour:
    target_hour += 24


result = (target_hour - wrong_hour) + (target_minute - wrong_minute)

print(result)
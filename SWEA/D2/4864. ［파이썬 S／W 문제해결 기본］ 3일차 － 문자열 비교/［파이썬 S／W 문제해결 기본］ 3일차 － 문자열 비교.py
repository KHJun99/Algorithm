t = int(input())

for order in range(1, t + 1):
    pattern = input()
    string = input()
    pattern_length = len(pattern)
    string_length = len(string)
    
    idx, char_match  = 0, 0
    is_match = 0
    while True:
        length = idx + pattern_length
        
        if string[idx:length] != pattern:
            idx += 1
            if idx > (string_length - pattern_length):
                print(f'#{order} {is_match}')
                break    
        else:
            is_match += 1
            print(f'#{order} {is_match}')
            break

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    
    # 길이 1~5까지 모든 조합 생성
    for length in range(1, 6):
        make_combinations(vowels, length, "", dictionary)

    dictionary.sort()
    
    # 찾고자 하는 단어의 인덱스 반환
    return dictionary.index(word) + 1


def make_combinations(vowels, length, current_word, result):
    if len(current_word) == length:
        result.append(current_word)
        return
    
    for vowel in vowels:
        make_combinations(vowels, length, current_word + vowel, result)
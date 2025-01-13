# try, except를 구분 하지 않을 시 런타임 에러 발생
while(1):
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
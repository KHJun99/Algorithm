import string

Notation = string.digits + string.ascii_uppercase

def convert(a, b):
    q, r = divmod(a, b)
    n = Notation[r]
    return convert(q, b) + n if q else n

N, B = map(int, input().split())

print(convert(N,B))
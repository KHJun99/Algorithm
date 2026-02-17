scale = list(map(int, input().split()))

start = scale[0]
is_scale = 1  # 일단 오름차순으로 시작

for idx in range(1, 8):
    if start + 1 == scale[idx]:      # 오름차순
        if is_scale == 0:            # 이전에 내림차순이었다면
            is_scale = -1            # mixed
        start = scale[idx]
    elif start - 1 == scale[idx]:    # 내림차순
        if is_scale == 1:            # 이전에 오름차순이었다면
            is_scale = -1            # mixed
        else:
            is_scale = 0             # 계속 내림차순
        start = scale[idx]
    else:
        is_scale = -1                # 연속되지 않으면 mixed
        break                        # 더 볼 필요 없으니 break

if is_scale == 1:
    print('ascending')
elif is_scale == 0:
    print('descending')
else:
    print('mixed')
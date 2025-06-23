# 재귀를 활용하여 정렬하는 방법을 배우는 문제
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

arr = list(map(int,input().split()))

count = 0       # 몇 번째로 저장되는지 카운트
result = -1     # 결과값 초기화

def merge_sort(arr, left, right):
    global count, result
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    global count, result
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    # 실제 배열에 병합 결과 복사 + 카운트
    for idx in range(len(temp)):
        arr[left + idx] = temp[idx]
        count += 1
        if count == k:
            result = temp[idx]

# 병합 정렬 실행
merge_sort(arr, 0, n - 1)
print(result)
# 백준 1920번 문제
# 문제 포스팅 : https://yunpc.github.io/2021/04/05/Find-Num/

def binary_search(A, key):
    l = 0
    r = len(A)

    while l < r:
        mid = (l+r) // 2
        if A[mid] == key:
            return 1
        elif A[mid] > key:
            r = mid
        else:
            l = mid+1

    return 0

N = int(input())

A = input().split(" ")

for i, _ in enumerate(A):
    A[i] = int(A[i])

A.sort()

M = int(input())

X = input().split(" ")

for i, _ in enumerate(X):
    print(binary_search(A, int(X[i])))

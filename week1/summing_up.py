def summing_up(A:list) -> list:
    n = len(A)
    #[[0] * 3] * 3是浅拷贝，里面的三个列表的内存是指向同一块，不管我们修改哪个列表，其他两个列表也会跟着改变。
    C = [[0 for i in range(n)] for j in range(n)] #new matrix n by n
    for i in range(0, n):
        for j in range(i, n):
            s = 0
            for k in range(i, j+1):
                s = s + A[k]
            C[i][j] = s / (j - i + 1)
    return C

def summing_up_fast(A:list) -> list:
    n = len(A)
    B = [0]*n
    B[0] = A[0]
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(1, n):
        B[i] = B[i-1] + A[i]
    for i in range(0, n):
        for j in range(i, n):
            if i == 0:
                C[i][j] = B[j] / (j-i+1)
            else:
                C[i][j] = (B[j] - B[i-1]) / (j-i+1)
    return C

def main():
    print(summing_up([1,2,3]))
    print(summing_up_fast([1,2,3]))

if __name__ == "__main__":
    main()
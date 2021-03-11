'''
    最大子列和问题
    只有在数组里有负数时才有意义（不然最大子列和就是数组的和）
'''

#O(n^3) naive
def max_subseq1(A:list) -> int:
    result = 0
    n = len(A)
    for i in range(0, n):
        for j in range(i, n):
            s = 0
            for k in range(i, j + 1):
                s = s + A[k]
            if s > result:
                result = s
    return result

#O(n^2) naive with preprocessing
'''
    B[i]里放的是A[0] + A[1] +..+ A[i]的和
    所以B[j] - B[i-1] = (A[0]+..+A[j]) - (A[0]+..+A[i-1]) = A[i]+..+A[j]
    其实不用新建一个数组，见实现3
'''
def max_subseq2(A:list) -> int:
    result = 0
    n = len(A)
    B = [0] * n
    B[0] = A[0]
    for i in range(1, n):
        B[i] = B[i-1] + A[i]
    for i in range(0, n):
        for j in range(i, n):
            s = 0
            if i == 0:
                s = B[j]
            else:
                s = B[j] - B[i-1]
            if s > result:
                result = s
    return result

def max_subseq3(A:list) -> int:
    result = 0
    n = len(A)
    for i in range(0, n):
        s = 0 #A[i]到A[j]的子列和
        for j in range(i, n):
            #对于相同的i，不同的j，只需要在j-1次循环的基础上累加一项即可
            s = s + A[j]
            if s > result:
                result = s
    return result

'''
    O(n)
    我们求的是连续和，如果现在的和是负数，无论后面加什么都会使后面的子列和变小，所以在小于0时，更新this_sum
'''
def max_subseq4(A:list) -> int:
    result = 0
    this_sum = 0
    n = len(A)
    for i in range(0, n):
        this_sum = this_sum + A[i]
        if this_sum > result:
            result = this_sum
        elif this_sum < 0:
            this_sum = 0
    return result

def main():
    print(max_subseq1([-1,3,-2,4,-6,1,6,-1]))
    print(max_subseq2([-1,3,-2,4,-6,1,6,-1]))
    print(max_subseq3([-1,3,-2,4,-6,1,6,-1]))
    print(max_subseq4([-1,3,-2,4,-6,1,6,-1]))
if __name__ == "__main__":
    main()
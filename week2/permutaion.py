def permutations_recursive(n):
    def helper(A, i):
        if i == n:
            print(A)
        for j in range(i, n):
            A[i],A[j] = A[j],A[i]
            helper(A,i+1)
            A[i],A[j] = A[j],A[i]
    A = [i for i in range(1, n+1)]
    helper(A, 0)

def permutations(n):
    A = [i for i in range(1, n+1)]
    s = [("start",0,0)]
    while s:
        c, i, j = s.pop()
        if c == "start":
            if i == n:
                print(A)
            else:
                A[i],A[j] = A[j],A[i]
                s.append(("finish", i, j))
                s.append(("start", i+1, i+1))
        elif c == "finish":
            A[i],A[j] = A[j],A[i]
            if j < n - 1:
                s.append(("start",i,j+1))

permutations_recursive(3)
print()
permutations(3)
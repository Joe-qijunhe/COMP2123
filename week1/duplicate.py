def duplicate_sort(A:list) -> bool:
    sort_A = sorted(A)
    n = len(A)
    for i in range(1, n):
        if sort_A[i-1] == sort_A[i]:
            return True
    return False

def duplicate_hash(A:list) -> bool:
    hashmap = {}
    n = len(A)
    for i in range(0, n):
        if A[i] in hashmap:
            return True
        hashmap[A[i]] = True
    return False

def main():
    print(duplicate_sort([1,2,2,3]))
    print(duplicate_hash([1,2,3]))

if __name__ == "__main__":
    main()
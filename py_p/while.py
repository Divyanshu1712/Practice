def main():
# ['a', 'a', 'b', 'a', 'b', 'c', 'x']
# ['a', 'x', 'z']
    A = input().split()
    N = len(A)
    B = input().split()
    M = len(B)
    # Your code goes here
    for i in range(N):
        if "A" or "a" in A:
            print(A[i] == 'A' or 'A')
        else:
            print("-1")
            
    for j in range(M):
        if "A" or "a" in B:
            print(B[j] == 'A' or 'A')
        else:
            print("-1")
    
    return 0

if __name__ == '__main__':
    main()
#Halloween Party
def max_pieces(K):
    if K % 2 == 0:
        return (K // 2) * (K // 2)
    else:
        return (K // 2) * (K // 2 + 1)

T = int(input("Enter No. of test cases: \n"))
for _ in range(T):
    K = int(input("Enter number of pieces: \n"))
    piece = max_pieces(K)
    print(f"Max number of pieces to be cut = {piece}")
if __name__ == "__main__":
    n = int(input())
    a = [int(input()) for _ in range(n)]
    n = int(input())
    m = [int(input()) for _ in range(n)]
    start = 1 if input() == "Odd" else 0
    andrea, maria = 0, 0
    for i in range(start, n, 2):
        andrea += a[i] - m[i]
        maria += m[i] - a[i]
    if andrea > maria:
        print("Andrea")
    elif maria > andrea:
        print("Maria")
    else:
        print("Tie")
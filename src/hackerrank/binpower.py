def binpow(a, b):
    ans = 1
    while b > 0:
        if b % 2 == 0:
            ans = ans * a
        a = a * a
        b >>= 1
    return ans
if __name__ == "__main__":
    print(binpow(2, 5))

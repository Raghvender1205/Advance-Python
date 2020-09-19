def cpu_bound(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    n = int(input())
    res = cpu_bound(n)
    print(res)
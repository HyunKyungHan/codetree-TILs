if __name__ == "__main__":
    n = int(input())
    input = list(map(int, input().split()))
    sorted_input = sorted(input)
    val = sorted_input[1]
    idx = input.index(val)
    print(idx+1)
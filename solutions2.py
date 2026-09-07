import sys

def max_signal_strength(arr, k):
    n = len(arr)
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    arr = [int(data[idx + i]) for i in range(n)]
    idx += n
    k = int(data[idx]); idx += 1
    print(max_signal_strength(arr, k))

if __name__ == "__main__":
    main()
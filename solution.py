import sys

def consolidate(ranges):
    if not ranges:
        return []
    ranges.sort(key=lambda x: (x[0], x[1]))
    merged = [list(ranges[0])]
    for start, end in ranges[1:]:
        last = merged[-1]
        if start <= last[1]:          # overlap or touching -> merge
            last[1] = max(last[1], end)
        else:
            merged.append([start, end])
    return merged

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    ranges = []
    for _ in range(n):
        s = int(data[idx]); e = int(data[idx+1]); idx += 2
        ranges.append((s, e))
    result = consolidate(ranges)
    out = []
    for s, e in result:
        out.append(f"{s} {e}")
    print("\n".join(out))

if __name__ == "__main__":
    main()
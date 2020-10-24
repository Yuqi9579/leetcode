def bitadder(num):
    added = 0
    while num != 0:
        added += num % 10
        num = num // 10
    return added

if __name__ == '__main__':
    print(bitadder(32))

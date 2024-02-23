def consecutive(k):
    s = input()
    n = len(s)
    sum = 0
    for i in range(0, n-1):
        if s[i] == s[i+1]:
            sum += 1
        else:
            sum = 1
        if sum == k:
            return True
    return False

print(consecutive(5))
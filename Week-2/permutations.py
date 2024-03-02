def perms(n: int, current=[]):
    if len(current) == n:
        print(current)
        return
    
    for num in range(1, n+1):
        if num not in current:
            current.append(num)
            perms(n, current)
            current.pop()


perms(3)
def fatorial(num,show=False):
    fat = 1
    for i in range(1, num+1):
        if show:
            if i != num:
                print(f"{i}", end=' x ')
            else:
                print(f"{i}", end=' = ')
        fat *= i
    
    return fat

print(fatorial(5,False))
def f(n):
    if n == 0:
        return ''
    x = int(input())
    return f(n-1)+f' {x}' 


n = int(input())
print(f(n))

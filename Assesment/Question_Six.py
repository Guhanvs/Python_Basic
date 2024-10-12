def fibonacci(n: int):

    if n<=0:
        print([])
    elif n==1:
        print([0])
    elif n==2:
        print([0,1])
    fib_sequence=[0,1]
    for i in range(2,n):
        next_number=fib_sequence[-1]+fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence
result=fibonacci(5)
print(result)




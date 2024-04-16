def fib(n):

    if n <= 0:
        return 0
    
    if n == 1:
        return 1
    
    return fib(n - 1) + fib(n - 2)

def gen(n):
    for i, z in enumerate(range(n)):
        number = fib(i)
        print(number, end = " ")
        with open("file.txt", "a", encoding='utf-8') as f:
            f.write(str(number) + " ")

gen(int(input("Dzień: ")))
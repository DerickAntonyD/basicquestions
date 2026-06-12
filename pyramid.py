n = int(input())

i = 1

while i <= n:
    spaces = n - i
    stars = 2 * i - 1

    print(" " * spaces + "*" * stars)
    i += 1

def sum(n):
    final_sum = 0
    for i in range(n+1):
        final_sum += i

    return final_sum

def sum2(n):
    return (n * (n + 1)) / 2


print(sum(10))
print(sum2(10))
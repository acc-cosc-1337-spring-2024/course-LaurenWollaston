def get_factorial(num):
    factorial = 1
    for num in range(1, num+1):
        factorial *= num
    # print ("FACTORIAL OF "+str(num)+" IS "+str(factorial))
    return (factorial)

def sum_odd_numbers(num):
    i=1
    sum=0
    while (i<=num):
        sum +=i
        i+=2
    return sum
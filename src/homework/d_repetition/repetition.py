def get_factorial(num):
    factorial = 1
    for num in range(1, num+1):
        factorial *= num
    # print ("FACTORIAL OF "+str(num)+" IS "+str(factorial))
    return (factorial)

def sum_odd_numbers(num):
    i=0
    sum=0
    while (i<=num):
        if (i%2 == 0):
            i+=1
        else:
            sum +=num
            i+=1
    print (sum)
    return sum
sum_odd_numbers(7)
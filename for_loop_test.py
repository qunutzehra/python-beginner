'''You are going to write a program that calculates the sum of all the even numbers from 1 to 100.
Thus, the first even number would be 2 and the last one is 100'''

sum_of_even = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum_of_even = sum_of_even + i
print(sum_of_even)

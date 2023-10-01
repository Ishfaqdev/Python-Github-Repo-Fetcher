# Sum of Even numbers

limit = int(input("Enter a number: "))
sum_of_even = 0
num = 2
while num <= limit:
    if num % 2 == 0:
        sum_of_even += num
    num += 1
print(f"The sum of even numbers from 2 to {limit} is : {sum_of_even}")


# Sum of Odd numbers

# limit = int(input("Enter a number: "))
# sum_of_odd = 0
# num = 1
# while num <= limit:
#     if num % 2 != 0:
#         sum_of_odd += num
#     num += 1
# print(f"The sum of odd numbers from 1 to {limit} is : {sum_of_odd}")

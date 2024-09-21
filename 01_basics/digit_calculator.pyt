# 2. Write a program that adds the digits in a 2-digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
num = input("Give a 2-digit number: ")
print(int(num[0]) + int(num[1]))

# OR
first_digit = num[0]
second_digit = num[1]
result = int(first_digit) + int(second_digit)
print(result)

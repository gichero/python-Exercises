#problem 1

# num = range (1,21)
# sum = 0
# for x in num:
#     if x % 3 == 0 or x % 5 == 0:
#         sum = sum + x
#         print sum

#problem 2

# num = range(1,1000)
# sum = 0
# for x in num:
#     if x % 3 ==0 or x%5 ==0:
#         sum = sum + x
#         print sum

#problem 3
# current = 1
# previous = 1
# sum = 0
#
# while current < 4000000:
#     if current % 2 == 0:
#         sum+= current
#     current, previous = current + previous, current
#
#     print sum

# problem 4

# n = 600851475143
# i = 2
#
# while i * i < n:
#     while n%i == 0:
#         n = n / i
#     i = i + 1
#
# print (n)

# problem 5

num = range(100, 1000)
ans = 0
for i in num:
    if i*i == ans:
        return int(str(ans)[::-1])==ans

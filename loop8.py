x = int(raw_input("Input a number? "))
for i in range(x-2):
    triangle = x - i
    print ' ' * triangle  + '*' * i + '*' * i

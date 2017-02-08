width  = int(raw_input("Width? "))
height  = int(raw_input("Height? "))
for x in range(height):
    if x == 0 or x == (height-1):
        print "*" * width
    else:
        print "*" + (" " * (width - 2)) + "*"

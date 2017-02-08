myStr = raw_input("write something? ")
for i in range(3):
    if i == 0 or i == 2:
        print "*" *  len(myStr) + "*" + "*"
    else:
        
        print "*" +  myStr + "*"

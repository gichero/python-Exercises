bill = float(raw_input("Total Amount "))
service = raw_input("Service level ")
total = 0.0
tip = 0.0

good = float(0.20 * bill )
fair = float(0.15 * bill)
poor = float(0.10 * bill)

if service == "good":
   total = good + bill
   print ("your total tip is %0.2f" % good)
elif service == "fair":
    total = fair + bill
    print ("your total tip is %0.2f" % fair)
else :
    total = poor + bill
    print ("your total tip is %0.2f" % poor)

print ("your total bill is %0.2f" % total)

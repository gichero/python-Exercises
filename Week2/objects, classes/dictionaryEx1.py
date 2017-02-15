phone_dict = {
'Alice': '703-493-1834',
'Bob': '857-384-1234',
'Elizabeth': '484-584-2923'
}
print "Elizabeth's phone number is %s" %(phone_dict['Elizabeth'])
phone_dict['Kareem'] = '938-489-1234'
del phone_dict['Alice']
phone_dict['Bob'] = '968-345-2923'
print phone_dict.items()

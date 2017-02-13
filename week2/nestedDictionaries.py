ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
    {
        'name': 'Jasmine',
        'email': 'jasmine@yahoo.com',
        'interests': ['photography', 'tennis']
    },
    {
        'name': 'Jan',
        'emai': 'jan@hotmail.com',
        'interests': ['movies', 'tv']
    }
  ]
}
print "%s's email address is %s" %(ramit['name'], ramit['email'])
print "%s's first interest is %s" %(ramit['name'], ramit['interests'][0])
#print "%s's email address is %s" %
print "Ramit's friend Jasmine, email address is %s" % (ramit['friends'][0]['email'])
print "Jan's second interest is %s" % (ramit['friends'][1]['interests'][1])

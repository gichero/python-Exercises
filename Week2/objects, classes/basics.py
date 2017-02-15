class Person(object):
    def __init__(self, name, email, phone):

        self.name = name
        self.email = email
        self.phone = phone
        self.friends =[]
        self.greeting = 0
        self.met = set()

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting +=1
        if other_person not in self.met:
            self.met.add(other_person)
            other_person.met.add(self)

    def numPeopleGreeted():
        return len(self.met)

    def num_friends(self):
        return len(self.friends)

    def print_contact_info(self):
        print '%s, %s, %s' % (self.name, self.email, self.phone)

    def add_friend(self, friend):
        self.friends.append(friend)

    def __repr__(self):
        return 'Person(%s, %s)' % (self.name, self.email)

sonny = Person('Sonny', 'sonny.hotmail.com', '483-485-4948')

jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

#print jordan.friends[0].name
print jordan.add_friend(sonny)
jordan.greet(sonny)

sonny.greet(jordan)

print '%s' % (sonny.name)
#
print "Sonny's email is %s and phone number is: %s" % (sonny.email, sonny.phone)
print "Jordan's email is %s and phone number is: %s" % (jordan.email, jordan.phone)
#
sonny.print_contact_info()
jordan.print_contact_info()
#print sonny.add_friend(jordan)
#print 'Sonny has %d friend.' % sonny.num_friends()

# Make your own class

# class Vehicle():
#     def __init__(self, make, model, year):
#
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def print_info(self):
#         print '%s %s %.f' % (self.make, self.model, self.year)
#
# car = Vehicle('Nissan', 'Leaf', 2015)
#
# print car.make, car.model, car.year
#
# Add a method
#
# car.print_info()

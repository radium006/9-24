class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
    
    def greet(self, other_person):
        print ('Hello {0}, I am {1}!'.format(other_person.name, self.name))
        self.greeting_count += 1
    
    def info(self):
        print("{0}'s email is {1} and {2}'s number is {3}".format(self.name, self.email, self.name, self.phone))

    def add_friend(self,other_person):
        self.friends.append(other_person)

    def num_friends(self):
        print(len(self.friends))

    def __repr__(self):
        return "{0} {1} {2}".format(self.name, self.email, self.phone)

class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print("{0} {1} {2}".format(self.year,self.make,self.model))


person1 = Person("Sonny", "sonny@hotmail.com", '483-485-4948')
person2 = Person("Jordan","jordan@aol.com", "495-586-3456")
person1.greet(person2)
person1.info()
person2.greet(person1)
person2.info()

person1.add_friend(person2)
person1.num_friends()
print(person1)
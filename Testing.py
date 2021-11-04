class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def say_name(self):
        print("MY name is " + self.firstname + " " + self.lastname)


# p1 = Person("Ahmed", "Samir")
#
# p1.say_name()
class Software_Engineer(Person):
    def __init__(self, fname, lname, progr_langu, salary):
        super().__init__(fname, lname, )
        self.language = progr_langu
        self.salary = salary

    def my_skills(self):
        print("i'm brilliant at " + self.language)

    def my_ambition(self):
        return self.salary


Eng1 = Software_Engineer("Amr", "Fahim", "Java", 250)
Eng1.say_name()
print(Eng1.my_ambition())

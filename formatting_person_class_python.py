class Person(object):
    GOOGLE_DIRECTORS = ["Larry Page", "Sergey Brin", "Eric Schmidt"]

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print("Hi, my name is {}.".format(self.name))

    def say_age(self):
        print("My age is {}.".format(self.age))

    def greet_google_directors(self):
        for name in Person.GOOGLE_DIRECTORS:
            print("Hello " + name + ".")

me = Person("thomas", 30)
me.say_name()
me.say_age()
me.greet_google_directors()

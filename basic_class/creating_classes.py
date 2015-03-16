# Ways of creating a class,

# Normal way of creating class:

class Ninja(object):
    def __init__(self, name):
        self.name = name
        print """creating an object ("""+name+""") of type Ninja.....
                 to kick use, object.kick() method,
                 to hit use, object.hit() method,
                 to jump use, object.jump() method"""

    def kick(self):
        print self.name+" is kicking someone's ass"

    def hit(self):
        print self.name+" is breaking someone's bone"

    def jump(self):
        print self.name+" is flying high"


# using type:

# you might already know that type() is a build in funtion in python, using which we could find the type of an object.
# Just pass the object in as a parameter to the function it will return the type for you.

# ex: 
# >> a = 2
# >> type(a)
# <type 'int'>

# and so, we could use it to find any type of object. But, the awesome part of type() function is we could use it
# to even create a class (adios! polymorphism). 

# All we have to do is pass three parameters instead of one. The parameters are,
# parameter 1 - class name as string
# parameter 2 - a tuple with the class names to be inherited by our class (if you are not inheriting any classes, then just put 'object' 
# in the tuple as the only element)
# parameter 3 - a dictionary with the namespace definitions for the class body

TypeNinja = type("Ninja", (object,), dict() )

# the above statement will create a class with name "Ninja" subclassed from object class with empty namespace(as we passed in an empty dict)

# creating objects of TypeNinja

# >> bob = TypeNinja()
# >> bob.name = "Bob"
# >> print bob.name




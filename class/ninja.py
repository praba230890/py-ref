# Now lets modify the Ninja class so that two objects of type Ninja could fight with each other

class Ninja(object):
    def __init__(self, name):
        self.name = name
        print """creating an object ("""+name+""") of type Ninja.....
                 to kick use, object.kick(other_object_to_be_kicked) method,
                 to hit use, object.hit(other_object_to_be_kicked) method,
                 to jump use, object.jump(other_object_to_be_kicked) method"""

    def kick(self, other_object):
        print self.name+" is kicking "+other_object.name+"'s ass"

    def hit(self, other_object):
        print self.name+" is breaking "+other_object.name+"'s bone"

    def jump(self):
        print self.name+" is flying high"


# We could make the Ninja class even more fun with giving the objects of Ninja class an energy variable. This could also give the Ninja class 
# a game like feel.

class Ninja(object):
    def __init__(self, name):
        self.name = name
        self.energy = 100
        print """creating an object ("""+name+""") of type Ninja.....
                 to kick use, object.kick(other_object_to_be_kicked) method,
                 to hit use, object.hit(other_object_to_be_kicked) method,
                 to jump use, object.jump(other_object_to_be_kicked) method"""

    def kick(self, other_object):
        print self.name+" is kicking "+other_object.name+"'s ass"
        other_object.energy -=5
        print self.name+"'s energy:",self.energy," and "+other_object.name+"'s energy:"+str(other_object.energy)

    def hit(self, other_object):
        print self.name+" is hitting "+other_object.name+"'s ass"
        other_object.energy -=5
        print self.name+"'s energy:",self.energy," and "+other_object.name+"'s energy:"+str(other_object.energy)

    def jump(self):
        print self.name+" is flying high"

# But the above class is weird as the energy goes to negative values and this if you recall I said we gave it a game like feel. 
# How this could be a game like when no one is winning or losing. Not all but most gaves have it so lets add them.

class Ninja(object):
    def __init__(self, name):
        self.name = name
        self.energy = 100
        print """creating an object ("""+name+""") of type Ninja.....
                 to kick use, object.kick(other_object_to_be_kicked) method,
                 to hit use, object.hit(other_object_to_be_kicked) method,
                 to jump use, object.jump(other_object_to_be_kicked) method"""

    def kick(self, other_object):
        if self.win_check(other_object):
            print self.name+" is kicking "+other_object.name+"'s ass"
            other_object.energy -=5
            print self.name+"'s energy:",self.energy," and "+other_object.name+"'s energy:"+str(other_object.energy)
        else:
            print "Game already Over!"

    def hit(self, other_object):
        if self.win_check(other_object):
            print self.name+" is hitting "+other_object.name+"'s ass"
            other_object.energy -=5
            print self.name+"'s energy:",self.energy," and "+other_object.name+"'s energy:"+str(other_object.energy)
        else:
            print "Game already Over!"

    def jump(self):
        print self.name+" is flying high"

    def win_check(self, other_object):
        if self.energy < 0:
            print "You loose!"
            return False
        elif other_object.energy < 0:
            print "You win!"
            return False
        return True

# Low budget, unneccessary advertisement like introduction to Testing

# Now the above game works good but there is a bug in it. We wanted to terminate the game once anyone of the players energy become 0 or less
# But it went to a level once any one of the players energy became -5 and then says game over. So, from this simple class we can easily see
# that as the code grows the complexity grows with it. Hence it becomes hard for us to ensure that everything works as we expected. I know
# that above bug is a very small one which needs an '=' to solve it, but think about a code base of 100's or 1000's or even millions of lines
# of code. 
# Do you think you could easily track the code and fix the bug. 
# Even if you fix the bug, you may not know whether your fix broke the 
# program somewhere else and maybe induced a number of bugs.
# Do you even know how many bugs in the above code!
# If you were asked to prove that the above class won't break in many other cases. You should have a proof and you can't fool around your
# team or project manager or even to yourself by running every case and showing everything works fine. Even if you are fine with it while
# working yourself alone on a project. You would be in a lot of pain when make some small modifications the other day. As you should again
# test your program in all cases in which the program will go through when it is used.
# Don't get scared! We have Unit Testing for this kind of problems. But before that 
# lets fix the above code.

class Ninja(object):
    def __init__(self, name):
        self.name = name
        self.energy = 100
        print """creating an object ("""+name+""") of type Ninja.....
                 to kick use, object.kick(other_object_to_be_kicked) method,
                 to hit use, object.hit(other_object_to_be_kicked) method,
                 to jump use, object.jump(other_object_to_be_kicked) method"""

    def kick(self, other_object):
        if self.win_check(other_object):
            print self.name+" is kicking "+other_object.name+"'s ass"
            other_object.energy -=5
            print self.name+"'s energy:",self.energy," and "+other_object.name+"'s energy:"+str(other_object.energy)
        else:
            print "Game already Over!"

    def hit(self, other_object):
        if self.win_check(other_object):
            print self.name+" is hitting "+other_object.name+"'s ass"
            other_object.energy -=5
            print self.name+"'s energy:",self.energy," and "+other_object.name+"'s energy:"+str(other_object.energy)
        else:
            print "Game already Over!"

    def jump(self):
        print self.name+" is flying high"

    def win_check(self, other_object):
        if self.energy <= 0:
            print "You loose!"
            return False
        elif other_object.energy <= 0:
            print "You win!"
            return False
        return True

#! python


class Father(object):
  def whoami(self):
    print "Father"
    
class Mother(object):
  def whoami(self):
    print "Mother"

class Child(Mother, Father):
  def whoami(self):
    print "Child"
  def myparent(self):
    super(Child,self).whoami()
    

dad = Father()
mom = Mother()
son = Child()

son.whoami()
son.myparent()

 

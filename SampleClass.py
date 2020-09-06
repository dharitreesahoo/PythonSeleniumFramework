class Test:

   def __init__(self,name):
      self.name = name

   def func1(self):
      print("Hello  ",self.name)

p = Test('dharitree') #initilizes the init function just like constructor
p.func1() #prints the Hello name

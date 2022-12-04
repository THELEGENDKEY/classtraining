from random import *
# class pet:
#   def __init__(self, name):
#     self.health = True
#     self.eat = True
#     self.clean = True
#     self.drink = True
#     self.social = True
#   def askdrink(self):
#     print('Your pet is thirsty!')
#     self.drink = False
    
# class University:
# 	def __init__(self, title, faculty):
# 		self.title = title
# 		self.faculty = faculty
# 		self.budjet = False
# 	def studying(self, name):
# 		print(name, 'is studying')
# 	def isbudget(self):
# 		if self.budjet == True:
# 			print('Congrats! You are on budget')
# 		else:
# 			print('Pay money and study!')

# class Student:
#   def __init__(self, name):
#     self.name = name
#     self.gladness = 50
#     self.progress = 0
#     self.money = 500
#     self.alive = True
#   def ask_budget(self):
#     if self.progress >= 20:
#       print('You are good enough!')
#       univer.budjet = True
#     else:
#       print('You are not good enough!')
#   def payforstudying(self):
#     if univer.budjet == False:
#       print('Pay to study!')
#       self.money -= 250
#     if self.money < 250:
#       print('You have not enough money to study!')
#       self.alive = False
#     if self.progress >= 20:
#       print('You are on budjet!')
#   def work(self):
#     print('You are working well!')
#     self.gladness -= 10
#     self.progress -= 5
#     self.money += 500
#   def session(self):
#     print('You are studying some etra lessons')
#     self.money -= 250
#     self.progress += 20
#     self.gladness -= 15
#   def say_hello(self):
#     print('Hello!')
#   def to_study(self):
#     print('Time to study')
#     self.progress += 10
#     self.gladness -= 10
#   def to_sleep(self):
#     print('Sleep time')
#     self.gladness += 5
#   def to_chill(self):
#     print('Chill time')
#     self.gladness += 15
#     self.progress -= 5
#   def is_alive(self):
#     if self.progress < -40:
#       print('You are bad student')
#       self.alive = False
#     elif self.gladness < 15:
#       print('Depression...')
#       self.alive = False
#     elif self.progress > 100:
#       print('Amazing!')
#       self.alive = False
#   def statistics(self):
#     print('Gladness = ', self.gladness, ' Progress = ', self.progress)
#     print('Budget = ', univer.budjet,' Money = ',self.money)
#   def live(self, day):
#     day = 'Day ' + str(day) + ' of ' + self.name + ' life'
#     print(day) 
#     if self.money <=500:
#       live_cube = randint(1,5)
#       if live_cube == 1:
#         self.ask_budget()
#         self.to_study()
#         univer.studying(self.name)
#       elif live_cube == 2:
#         self.to_sleep()
#       elif live_cube == 3:
#         self.to_chill()
#       elif live_cube == 4:
#         self.say_hello()
#       elif live_cube == 5:
#         self.work()
#     else:
#       live_cube2 = randint(1,6)
#       if live_cube2 == 1:
#         self.to_study()
#         univer.studying(self.name)
#       elif live_cube2 == 2:
#         self.to_sleep()
#       elif live_cube2 == 3:
#         self.to_chill()
#       elif live_cube2 == 4:
#         self.say_hello()
#       elif live_cube2 == 5:
#         self.work()
#       elif live_cube2 == 6:
#         self.session()
#     if univer.budjet == False:
#       self.ask_budget()
#     self.payforstudying()
#     self.statistics()
#     self.is_alive()

# univer = University('Step', 'Computer Science')
# human = Student('Anton')
# for day in range(10):
# 	if human.alive == False:
# 		break
# 	human.live(day)
# class Human:
# 	def __init__(self, name):
# 		self.name = name
# 		self.appearance = 5
# 		self.status = False
# 	def live(self):
# 		print(self.name, 'is alive')
# 	def eat(self):
# 		print('Eating time')

# class Woman(Human):
# 	def live(self):
# 		super().live()
# 		print('What a wonderful day of', self.name)
# 	def cook(self):
# 		print(self.name, 'is cooking')
		
# class Man(Human):
# 	def __init__(self, name):
# 		super().__init__(name)
# 		self.money = 50
# 	def work(self):
# 		self.money += 10
# 		print(self.name, 'is working')
# 		print('Money: ', self.money)

# human = Human('Bob')
# human.live()
# w1 = Woman('Clara')
# w1.live()
# w1.cook()
# m1 = Man('John')
# m1.live()
# m1.work()
class Rodant:
  def __init__(self,name):
    self.name = name
    self.food = True
    self.thirst = True
    self.rest = True
  def eat(self):
    print(self.name + ' ate some food')
    self.eat = True
  def drink(self):
    print(self.name + ' drank some water')
    self.thirst = True
  def sleep(self):
    print(self.name + ' slept a little')
    self.rest = True
class Hamster(Rodant):
  def __init__(self, name):
    super().__init__(name)
    self.hasfoodincheeks = False
  def stat(self):
    if hasfoodincheeks == True:
      print(self.name + ' has food in its cheeks')
    else:
      print(self.name + ' has no food in its cheeks')
  def live(self):
    life = randint(1,4)
    if life == 1:
      if self.hasfoodincheeks == False:
        print(self.name + ' put some food in its cheeks')
        self.hasfoodincheeks = True
      else:
        print(self.name + ' ate their food in cheeks')
        self.hasfoodincheeks = False
    if life == 2:
      super().eat()
    if life == 3:
      super().drink()
    if life == 4:
      super().sleep()    
class Rat(Rodant):
  def __init__(self, name):
    super().__init__(name)
    self.issocial = True
  def stat(self):
    if self.issocial == True:
      print(self.name + ' is social now')
    else: 
      print(self.name + ' is not social now')
  def live(self):
    life = randint(1,4)
    if life == 1:
      if self.issocial == False:
        print(self.name + ' became social')
        self.issocial = True
      else:
        print(self.name + ' became unsocial')
        self.issocial = False
    if life == 2:
      super().eat()
    if life == 3:
      super().drink()
    if life == 4:
      super().sleep() 
    self.stat()
class Capybara(Rodant):
  def __init__(self,name):
    super().__init__(name)
    self.hasafriend = True
    self.swimming = False
  def stat(self):
    if self.swimming == True:
      print(self.name + ' is swimming')
    else:
      print(self.name + ' is not swimming')
    if self.hasafriend == True:
      print(self.name +' has a great time with a friend')
    else:
      print(self.name + ' is alone(')
  def live(self):
    life = randint(1,4)
    if life == 1:
      if self.swimming == False:
        print(self.name + ' is swimming')
        self.swimming = True
      else:
        print(self.name + ' stopped swimming')
        self.swimming = False
    if life == 2:
      if self.hasafriend == False:
        print(self.name + ' found a friend')
        self.hasafriend = True
      else:
        print(self.name + ' lost a friend')
        self.hasafriend = False
    if life == 3:
      super().eat()
    if life == 4:
      super().drink()
    if life == 5:
      super().sleep()
    self.stat()
hamster = Hamster('Daniel')
for i in range(9):
  hamster.live()
rat = Rat('Sofie')
for o in range(9):
  rat.live()
capy = Capybara('Quandile')
for p in range(9):
  capy.live()
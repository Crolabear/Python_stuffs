import math
from __future__ import division

def factor(a):
  factors=[]
  for i in range(1,int(math.floor(math.sqrt(a))+1)):
    if (a%i) == 0:
      factors.append(i)
      factors.append(int(a/i))
  return factors

def prime_factor(a,empty):
  temp=0
  #for i in range(2,int(math.floor(math.sqrt(a))+1)):
  for i in range(2,int(a)+2): # add 2 to make i dont run into range(2,2)
    if (a%i)==0:
      empty.append(i)
      temp=1
      break
  if temp==0:
    empty.append(1)
    return empty
  else:
    b=a/i
    return prime_factor(b,empty)
  
  

def find_common(list1,list2):
  temp=[]
  for item in list1:
    if item in list2:
      list2.remove(item)
      temp.append(item)
  return temp


def simplify(top,bot):
  fac1=prime_factor(top,[])
  fac2=prime_factor(bot,[])
  common_factors=find_common(fac1,fac2)
  product=reduce(lambda x,y:x*y,common_factors)
  return int(top/product),int(bot/product)
  
  

class fraction:
  def __init__(self,top,bot):
    self.top=top
    self.bot=bot
    if self.bot==0:
      print 'can not divide by zero'
  
  def evaluate(self):
    return self.top/self.bot
  
  def simplify_terms(self):
    temp=1
    numerator,denominator=simplify(self.top,self.bot)
    self.top=numerator
    self.bot=denominator
    self.show()
    
  def show(self):
    print self.top
    print '---'
    print self.bot


  def add(self,other):
    self.top=self.top+other.top
    self.bot=self.bot+other.bot
    self.simplify_terms()  
    self.show()
  
  def subtract(self,other):
    self.top=self.top-other.top
    self.bot=self.bot-other.bot
    self.simplify_terms()
    self.show()

  def multiply(self,other):
    self.top=self.top*other.top
    self.bot=self.bot*other.bot
    self.simplify_terms()
    self.show()

  def divide(self,other):
    self.top=self.top*other.bot
    self.bot=self.bot*other.top
    self.simplify_terms()
    self.show()

    
  


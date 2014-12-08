from __future__ import division

class polynomial:

  def __init__(self,coefficients):
    self.coefficients=coefficients
    
  def multiply(self,other):
    l1=len(self.coefficients)
    l2=len(other.coefficients)
    deg={}
    for i in range(l1):
      for j in range(l2):
	k=i+j
	if k not in deg.keys():
	  deg[k]=(self.coefficients[i]*other.coefficients[j])
	else:
	  deg[k]=deg[k]+(self.coefficients[i]*other.coefficients[j])
  return polynomial(deg.values())
      
	
	
      
    
    
    
    
  


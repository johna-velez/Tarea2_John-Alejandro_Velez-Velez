#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import sqrt

class vectorcartesiano:
    def __init__(self,x,y,z):
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)
        self.modulo=sqrt(x**2+y**2+z**2) #encuentra el modulo del vector
        
    def cruz(self, b):   # producto cruz
        cordx=self.y*b.z-self.z*b.y
        cordy=self.z*b.x-self.x*b.z
        cordz=self.x*b.y-self.y*b.x
        
        r=vectorcartesiano(cordx,cordy,cordz)
        return r
    
    def __mul__(self, v): #producto interno, sobrecargando *
        cordx=self.x*v.x
        cordy=self.y*v.y
        cordz=self.z*v.z
        r=cordx+cordy+cordz
        
        return r
    
    def __add__(self, v): #suma de vectores, sobrecargando +
        cordx=self.x+v.x
        cordy=self.y+v.y
        cordz=self.z+v.z
        
        r=vectorcartesiano(cordx,cordy,cordz)
        return r
    
    def __sub__(self, v): #resta de vectores, sobrecargando -
        cordx=self.x-v.x
        cordy=self.y-v.y
        cordz=self.z-v.z
        r=vectorcartesiano(cordx,cordy,cordz)
        return r
    
    def __eq__(self, v): # compara las componentes de los vectores para ver si
        if self.x-v.x==0 and self.y-v.y==0 and self.z-v.z==0: # son iguales o diferentes
            return 'los vectores son iguales'
        else:
            return 'los vectores son diferentes'
        
        
    def __repr__ (self): ##para mirar la representacion
        
        return '<Vector (%f, %f, %f)>' % (self.x, self.y, self.z)
    
    


# In[237]:

class vectorpolar:    
    def __init__(self, r, theta, phi):
        if r<0:
            r=abs(r)
        if theta<0 or theta>pi:
            print('hay un error en la coordenada polar, theta')
        if phi<0 or phi>2*pi:
            print('hay un error en la coordenada  ')
        
        # conversion a cantidades cartesianas
        r=float(r)
        x=r*cos(theta)*sin(phi)
        y=r*sin(theta)*sin(phi)
        z=r*cos(phi)
        
        vectorcartesiano.__init__(self, x,y,z)# todo lo va a calcular en cartesianas 
        
    def conv(self):
        return vectorcartesiano(self.x,self.y,self.z)

        


# In[238]:

def ang(a,b):
    ang=acos(a*b/(a.modulo*b.modulo))
    return ang

"""y=vectorcartesiano(1,2,3)
yp=vectorpolar(-7,2,0)

print(y.__dict__)
print(yp.__dict__)"""







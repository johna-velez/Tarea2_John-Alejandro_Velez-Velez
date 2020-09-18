#!/usr/bin/env python
# coding: utf-8

# In[4]:


from clases import *


# In[5]:


a=vectorcartesiano(1.5,0,2.4)
b=vectorcartesiano(0,1,9)
c=vectorcartesiano(4.2,0.5,0)


# In[7]:


print('a.b=',a*b)
print('a.c=',a*c)
print('b.c=',b*c)

print('axb',a.cruz(b))
print('axc',a.cruz(c))
print('bxc',b.cruz(c))

print('el angulo entre a y b es:', ang(a,b))
print('el angulo entre a y c es:', ang(a,c))
print('el angulo entre b y c es:', ang(b,c))

print('la represtentacion en cartesiana de a es ', a.conv())
print('la represtentacion en cartesiana de b es ', b.conv())
print('la represtentacion en cartesiana de c es ', c.conv())
# In[ ]:





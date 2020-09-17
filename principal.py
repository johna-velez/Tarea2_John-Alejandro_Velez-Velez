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


# In[ ]:





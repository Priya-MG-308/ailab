#!/usr/bin/env python
# coding: utf-8

# In[2]:


from collections import defaultdict
visited=defaultdict(lambda: False)
J1,J2,L=0,0,0
def water_jug(x,y):
    global J1,J2,L
    if(x==L and y==0) or (x==0 and y==L):
        print( "(",x,",",y,")" ) 
        return True
    if(visited[(x,y)]==False):
        print( "(",x,",",y,")" ) 
        visited[(x,y)]=True
        
        return(water_jug(0,y)or water_jug(x,0)or water_jug(J1,y)or water_jug(x,J2)or water_jug(x+min(y,J1-x),y-min(y,J1-x))or water_jug(x-min(x,J2-y),y+min(x,J2-y)))
    else:
        return False
J1=2
J2=5
L=3
print("path")
water_jug(0,0)


# In[ ]:





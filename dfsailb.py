#!/usr/bin/env python
# coding: utf-8

# In[2]:


adj_list={"A":["B","C"],"B":["D","E"],"C":["B","F"],"D":[],"E":["F"],"F":[]}
color={}
parent={}
time_trav={}
dfs_op=[]
for node in adj_list.keys():
    color[node]="W"
    parent[node]=None
    time_trav[node]=[-1,-1]
time=0
def dfs_util(u):
    global time
    color[u]="G"
    time_trav[u][0]=time
    dfs_op.append(u)
    time+=1
    for v in adj_list[u]:
        if color[v]=="W":
            parent[v]=u
            dfs_util(v)
    color[u]="B"
    time_trav[u][1]=time
    time+=1
    
dfs_util("A")
print(dfs_op)
print(time_trav)


# In[ ]:





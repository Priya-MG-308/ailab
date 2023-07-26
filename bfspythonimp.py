#!/usr/bin/env python
# coding: utf-8

# In[2]:


from queue import Queue
adj_list={"A":["B","D"],"B":["A","C"],"C":["B"],"D":["A","E","F"],"E":["D","F","G"],"F":["D","E","H"],"G":["E","H"],"H":["F","G"]}
visited={}
parent={}
level={}
bfs_op=[]
queue=Queue()

for node in adj_list.keys():
    visited[node]=False
    level[node]=-1
    parent[node]=None
    
s="A"
visited[s]=True
level[s]=0
queue.put(s)

while not queue.empty():
    u=queue.get()
    bfs_op.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            level[v]=level[u]+1
            queue.put(v)
print(bfs_op)            


# In[3]:


print(level)


# In[5]:


v="G"
path=[]
while v is not None:
    path.append(v)
    v=parent[v]
path.reverse()
print(path)
    


# In[ ]:





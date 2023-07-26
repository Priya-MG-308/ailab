#!/usr/bin/env python
# coding: utf-8

# In[10]:


from collections import deque
class Graph:
    def __init__(self,adj_li):
        self.adj_li=adj_li
    def get_neigh(self,v):
        return self.adj_li[v]
    def h(self,n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1}
        return H[n]
    def a_star(self,start,stop):
        op_ls=set([start])
        cl_ls=set([])
        poo={}
        poo[start]=0
        par={} 
        par[start]=start
        while len(op_ls)>0:
            n=None
            for v in op_ls:
                if n==None or poo[v]+self.h(v)<poo[n]+self.h(n):
                    n=v;
                    
            if n==None:
                print("no path")
                return None
            if n==stop:
                repath=[]
                while par[n]!=n:
                    repath.append(n)
                    n=par[n]
                repath.append(start)
                repath.reverse()
                print("path found")
                return repath
            
            for (m,weight) in self.get_neigh(n):
                if m not in op_ls and m not in cl_ls:
                    op_ls.add(m)
                    par[m]=n
                    poo[m]=poo[n]+weight
                else:
                    if poo[m]>poo[n]+weight:
                        par[m]=n
                        poo[m]=poo[n]+weight
                        if m in cl_ls:
                            cl_ls.remove(m)
                            op_ls.add(m)
            op_ls.remove(n) 
            cl_ls.add(n)
        print("path no")
        return None
adj_li={'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}
g=Graph(adj_li)
g.a_star('A','D')


# In[ ]:





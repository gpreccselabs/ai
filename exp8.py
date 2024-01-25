from collections import defaultdict
def graphColor(k):
    nextValueOf(k)
    if x[k] == 0:
        return
    elif k==n:
        print("Colors of vertices are:")
        for i in range(1,len(x)):
            print("Vertex :",i," : ",color[x[i]])
    else:
        graphColor(k+1)
def nextValueOf(k):
    while True:
        x[k]=(x[k]+1)%(m+1)
        if x[k]==0:
            return
        b=True
        for i in range(1,n+1):
            if g[k][i]!=0 and x[i]==x[k]:
                b=False
                break
        if b:
            return
n=int(input("Enter the no of Vertices"))
g=defaultdict(list)
color=["","Red","Green","Blue","Yellow","Orange"]
print("Enter the adjacency matrix")
g[0]=[0]*(n+1)
for i in range(1,n+1):
    g[i]=[0]+list(map(int,input().split()))
x=[0]*(n+1)
m=int(input("Enter the max no of colors"))
graphColor(1)

from collections import defaultdict

class Graph:
	def __init__(self,vertices):
		self.V=vertices
		
		self.graph=defaultdict(list)
		
	def addEdge(self,u,v):
		self.graph[u].append(v)
		
	def getAll(self,src,dest,visited,path):
		visited[src]=True
		path.append(src)
		
		if(src==dest):
			print(path)
		else:
			for i in self.graph[src]:
				if(visited[i]==False):
					self.getAll(i,dest,visited,path)
		
		path.pop()
		visited[src]=False
		
		
	def getPath(self,src,dest):
		visited=[False]*self.V
		path=[]
		self.getAll(src,dest,visited,path)
		
def main():
	print("Enter number of vertices");
	n=int(input())
	
	g=Graph(n)
	
	print("Enter number of edges");
	e=int(input())
	
	print("-------------------")
	
	for i in range(e):
		print("Enter vertices having edge seperated by space")
		x,y=map(int,input().split())
		g.addEdge(x,y)
	
	print("-------------------")	
	
	print("Enter start node")
	s=int(input())
	print("Enter end node")
	d=int(input())	
	
	print("-------------------")
	print("Path from",s," to ",d," are: ") 
	g.getPath(s,d)

if __name__ == "__main__":
	main()		


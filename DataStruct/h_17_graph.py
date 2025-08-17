class Graph:
    def __init__(self, graphic):
        if graphic is None:
            self.graph={}
        else:
            self.graph=graphic

    def get_Vertices(self):
        return list(self.graph.keys())

    def get_Edges(self):
        edges=[]
        for keys in self.graph:
            for values in self.graph[keys]:
                if {keys,values} not in edges:
                    edges.append({keys,values})
        return edges

    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def add_edge(self,edge):
        edge=set(edge)
        len1,len2=tuple(edge)
        if len1 in self.graph:
            self.graph[len1].append(len2)
        else:
            self.graph[len1]=[len2]



graph_element={
    'a':['b','c'],
    'b':['a','d'],
    'c':['a','d'],
    'd':['b','c','e'],
    'e':['d']
}
graph=Graph(graph_element)
graph.add_vertex('f')
print(graph.get_Vertices())
graph.add_edge({'a','f'})
print(graph.get_Edges())
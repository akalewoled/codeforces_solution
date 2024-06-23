def isBipartite( graph: List[List[int]]) -> bool:
        color={}
        
        def dfs(num):
            for i in graph[num]:
                if i in  color:
                    if color[i]==color[num]:# there exist a cycle
                        return False
                else:
                    color[i]=1-color[num]# assign the opposite color to the neighbor
                    if not dfs(i):#keep assigning the color to the ne
                        return False
            return True

            
            

        for i in  range(len(graph)):
            if i not in color:
                color[i]=0
                if not dfs(i):
                    return False

        return True

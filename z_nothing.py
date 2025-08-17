matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
DIRS=(0,1),(1,0),(0,-1),(-1,0)
ans=[]
m,n=len(matrix),len(matrix[0])
print(m,n)
i,j,di=0,0,0
for _ in range(m*n):
    ans.append(matrix[i][j])
    matrix[i][j]=None
    x,y=i+DIRS[di][0],j+DIRS[di][1]
    if x<0 or x>=m or y<0 or y>=n or matrix[x][y] is None:
        di=(di+1)%4
    i+=DIRS[di][0]
    j+=DIRS[di][1]
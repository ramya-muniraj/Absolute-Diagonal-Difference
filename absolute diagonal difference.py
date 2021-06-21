n=3
suma=0
sumb=0
lst=[[7,9,8],[7,5,3],[9,-1,4]]
for i in range(n):
    suma+=lst[i][i]
for i in range(n):
    sumb+=lst[i][n-1-i]
print(sumb-suma)

n=3
left_sum=0
right_sum=0
lst=[[7,9,8],[7,5,3],[9,-1,4]]
for i in range(n):
    left_sum+=lst[i][i]
for i in range(n):
    righ_sum+=lst[i][n-1-i]
print(right_sum-left_sum)

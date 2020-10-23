a= [[1,2,3],
    [4,5,6],
    [7,8,9]]
b=0
for i in a:
    b =b+ sum(i)
b = b - a[1][0] - a[1][2]

print(b)
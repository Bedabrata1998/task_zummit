def min_dist(array,n,x,y):
    mindist=999999
    for i in range(n):
        for j in range(i+1, n):
            if (x==array[i]and y==array[j] or y==array[i] and x==array[j]) and mindist > abs(i-j):
                mindist=abs(i-j)
        return mindist

array=[3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
n=len(array)
x=3
y=6
print("Minimum distance between {} and {} is {}".format(x,y,min_dist(array, n, x, y)))
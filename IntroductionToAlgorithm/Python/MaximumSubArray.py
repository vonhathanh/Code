a = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
maxSoFar = 0
currentMax = 0
#kadane algorithm
for i in range(0,len(a)):
    currentMax += a[i]
    if a[i] > currentMax:
        currentMax = a[i]
    if currentMax > maxSoFar:
        maxSoFar = currentMax


print maxSoFar
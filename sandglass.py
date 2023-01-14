n = int(input())

for i in range(n,0,-1):
    
    for k in range(n-i):
        print("   ",end="")
    for j in range(0,2*i-1):
        print(" * ",end="")
    print()
for r in range(n):
    for s in range(n-r-1):
        print("   ",end="")
    for t in range(2*r+1):
        print(" * ",end = "")
    print()
    
# cook your dish here
def Reach_the_Target(X,Y):
    return (X-Y)
    
#Taking Input From User or #Driver Code
for _ in range(int(input())):
    X,Y = map(int,input().split(" "))
    print(Reach_the_Target(X,Y))

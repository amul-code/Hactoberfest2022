# cook your dish here
def enspace(N,X,Y):
    sum = X+(Y*2)
    if N<sum:
        return "NO"
    else:
        return "YES"

#taking input from user
for _ in range(int(input())):
    N,X,Y = map(int,input().split(" "))
    print(enspace(N,X,Y))

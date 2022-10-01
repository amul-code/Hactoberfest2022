# cook your dish here
def SleepDep(X):
    if X>=7:
        return "NO"
    else:
        return "YES"
# Taking input from user
for _ in range(int(input())):
    X = int(input())
    print(SleepDep(X))

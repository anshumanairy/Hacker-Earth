def func():
    n,d=map(int,input().split())
    list1=list(map(int,input().split()))
    if(d==n or d==0):
        print(*list1,sep=' ')
    else:
        x=d%n
        list3=list1[x:]+list1[:x]
        print(*list3,sep=' ')
func()
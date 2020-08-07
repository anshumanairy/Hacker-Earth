def func():
    T=int(input())
    for i in range(T):
        N,K = map(int,input().split())
        list1=list(map(int,input().split()))
        if(K<=min(list1)):
            print(0)
        else:
            print(K-min(list1))
func()
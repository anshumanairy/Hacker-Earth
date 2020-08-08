def func():
    N=int(input())
    list1=list(map(int,input().split()))
    k=1
    for i in range(len(list1)-1):
        if(list1[i]>list1[i+1]):
            k+=1
    print(k)
func()
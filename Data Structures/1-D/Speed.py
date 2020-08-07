def func():
    T=int(input())
    for i in range(T):
        N=int(input())
        list1=list(map(int,input().split()))
        count=1
        if(N==1):
            print(count)
        else:
            for i in range(N-1):
                if(list1[i]>list1[i+1]):
                    count+=1
                else:
                    list1[i+1]=list1[i]
            print(count)
func()
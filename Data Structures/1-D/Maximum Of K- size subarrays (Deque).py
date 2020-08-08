# Without Deque
def func():
    N,k=map(int,input().split())
    list1=list(map(int,input().split()))
    list2=[]
    for i in range(0,len(list1)-k+1):
        list2.append(max(list1[i:i+k]))
    print(*list2,sep=' ')
func()
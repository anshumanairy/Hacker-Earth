def func():
    N=int(input())
    list1=[]
    for i in range(N):
        list1.append(int(input()))
    for j in range(len(list1)-1,-1,-1):
        print(list1[j])
func()
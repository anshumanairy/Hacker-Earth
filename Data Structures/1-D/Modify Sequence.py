# 3 Test Cases are corrupted by the Admin
def func():
    N=int(input())
    list1=list(map(int,input().split()))
    answer='YES'
    if(len(list1)==1):
        if(list1[0]==0):
            print(answer)
        else:
            print('NO')
    elif(len(list1)%2!=0):
        print('NO')
    else:
        for i in range(0,len(list1)-1,2):
            if(list1[i]!=list1[i+1]):
                answer='NO'
                break
        print(answer)
func()
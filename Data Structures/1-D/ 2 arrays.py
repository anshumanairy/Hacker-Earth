def func():
    N=int(input())
    list1=list(map(int,input().split()))
    list2=list(map(int,input().split()))
    count1=list1.count(-1)
    count2=list2.count(-1)
    sum1=sum(list1)+count1
    sum2=sum(list2)+count2
    if(count1==count2):
        print('Infinite')
    else:
        if(count1==0 and count2!=0):
            if(sum1<sum2):
                print(0)
            else:
                if(count2==1):
                    print(count2)
                else:
                    # Not the most Effective
                    print(sum1-sum2+1)
        if(count1!=0 and count2==0):
            if(sum1>sum2):
                print(0)
            else:
                if(count1)==1:
                    print(count1)
                else:
                    # Not the most Effective
                    print(sum2-sum1+1)
func()
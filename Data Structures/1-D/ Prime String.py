def checkPrime(x):
    check=1
    if(x<2):
        check=0
    elif(x==2):
        pass
    else:
        count=0
        for j in range(2,x):
            if x%j==0:
                count+=1
        if count==0:
            check=1
        else:
            check=0
    return check

def func():
    T=int(input())
    for i in range(T):
        s=input()
        list1=list(set(list(s)))
        list2=list(s)
        x=len(list1)
        list3=[]
        if(checkPrime(x)==0):
            print('NO')
        else:
            check=1
            for j in range(len(list1)):
                if(checkPrime(list2.count(list1[j]))==0):
                    check=0
                    print('NO')
                    break
            if check==1:
                print('YES')
func()
def func():
    T=int(input())
    for i in range(T):
        list1=list(input())
        list1.sort()
        check=1
        for j in range(len(list1)-1):
            if(int(list1[j+1])!=int(list1[j])+1):
                check=0
                print('NO')
                break
        if(check==1):
            print('YES')
func()
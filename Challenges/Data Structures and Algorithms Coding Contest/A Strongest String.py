# Partial Test Cases Passed
def func():
    T=int(input())
    for i in range(T):
        N=int(input())
        S=input()
        list1=list(S)
        x=max(list1)
        s=str(x)
        y=str(x)
        list2=list1
        list2=list(set(list2))
        list2.sort(reverse=True)
        if(len(list(set(list1)))==1):
            print(list1[0])
        else:
            k=list1.index(x)
            z=1
            while(k!=len(list1)-2):
                if(max(list1[k+1:])==list2[z]):
                    s+=list2[z]
                    z+=1
                    k=list1.index(list2[z])
                else:
                    z+=1
            # while(k!=len(list1)):
            #     y=max(list1[k:])
            #     if(y in list(s)):
            #         k+=1
            #         pass
            #     else:
            #         s+=y
            #         x=y
            #         k=list1.index(y)
            # for i in range(list1.index(max(list1)),len(list1)):
            #     if(list1[i]==x):
            #         pass
            #     else:
            #         if(list1[i]<x):
            #             if(list1[i]==max(list1[i:])):
            #                 s+=str(list1[i])
            #                 x=list1[i]
            #         else:
            #             s=str(list1[i])
            #             x=list1[i]
            print(s)
func()
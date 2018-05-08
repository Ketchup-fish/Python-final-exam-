########方法一##########
sum=0
n=1
while n<100:
    sum=sum+n
    n=n+2
print(sum)

########方法二##########
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)
################################
##########方法一################
L=['Bart','Lisa','Adam']
for x in L:
    print ("Hello，",x,"!")
for y in range(10):
    print (y)
##########方法二################
print("##########################")
L=['Bart','Lisa','Adam']
i=0
while i<len(L):
    print ("Hello，",L[i],"!")
    i=i+1
##########计算1×2×3×4……×100###################
acc=1
n=1
while n<=100:
    acc=acc*n
    n=n+1
print(acc)
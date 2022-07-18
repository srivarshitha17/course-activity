#program to print pyramid star pattern using for loop
n=int(input('enter no.of rows'))
space=n
for i in range(n):
    c=0
    while(c < space):
        print(" ",end='')
        c+=1
    space-=1
    for j in range (i):
        print('*',end=' ')
    print()

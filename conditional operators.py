a = int(input())
b = int(input())
c = int(input())
if a<b:
    #a - min
    if a<c:
        print('smallet number is:       ',a)
    else:
        print('smallet number is:       ',c)
else:
    #b -min
    if b<c:
        print('smallet number is:        ',b)
    else:
        print('smallet number is:        ',c)
print('This programm is over')
    

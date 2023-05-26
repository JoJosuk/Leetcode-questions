str='}{}'
flag=0
for i in str:
    if flag<0:break
    if i=='{':
        flag+=1
    elif i =='}':
        flag-=1
if flag==0:
    print('correct')
else :
    print('incorrect')


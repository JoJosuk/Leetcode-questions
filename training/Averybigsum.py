# intex='aaabacbebebeeeeeeeeeeeee'
# k=3
# length=len(intex)
# r=k
# l=0
# p=[]
# while 1:
#     if r>len(intex):
#         print(l,r)
#         break
#     if len(set(intex[l:r+1]))>k:
#         p.append(intex[l:r])
#         l+=1
#         r=l+k
#     if len(set(intex[l:r+1]))==k:
#         r+=1   
#     else:
#         r+=1
# print(p)


def long(s, k):
    n = len(s)
    answer = -1
    for i in range(n):
        for j in range(i+1, n+1):
            distinct = set(s[i:j])
            if len(distinct) == k:
                answer = max(answer, j - i)
    print(answer)
 
s = "aabacbebebe"
k = 3
long(s,k)
import heapq
# s ="()"
# hash_map={"(":")","[":"]","{":"}"}
# stack=[]
# for i in s:
#     if i in hash_map:
#         stack.append(i)
#     elif i == stack[-1]:
#         stack.pop()
#     else:
#         print("False")
# print(not stack)

# sji=["ni",1,2]
# sji.append(3)
# print(sji)

# st=["apple","banana","cherry","orange"]
# j = st.pop()
# print(j)
# print(st)
# nums=[3,2,1,5,6,4]
# k = 2
# q=[(-nums[i],i) for i in range(len(nums))]
# heapq.heapify(q)
# for i in range(k-1):
#     heapq.heappop(q)
#     print(-q[0][0])

from collections import Counter, defaultdict

# #
# nums = [1,1,1,2,2,3,7,7,7,7]
# dict={}
# k=2
# for i in nums:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)
# keys=list(dict.keys())
# values=list(dict.values())
#
# q=[(-values[i],keys[i]) for i in range(len(values))]
# heapq.heapify(q)
# for i in range(k):
#     tmp=heapq.heappop(q)
#     print(tmp[1])

# for i in range(2):
#     print(i)


# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# d = defaultdict(list)
# for s in strs:
#     print(''.join(sorted(s)))
#     d[''.join(sorted(s))].append(s)
#     print(d)

nums = [0,3,7,2,5,8,4,6,0,1]
new_nums=sorted(nums)
ans=0
res=0
for i in range(1,len(nums)):
    if new_nums[i]==new_nums[i-1]+1:
        res+=1
    else:
        res=0
    ans = max(ans, res + 1)
print(ans)





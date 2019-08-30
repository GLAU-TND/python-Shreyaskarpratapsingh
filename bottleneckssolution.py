# bottles = int(input("number of bottles"))
# radius = input("enter the radius")
# freq = {}
# for items in radius:
#     freq[items] = radius.count(items)
#
# for key, value in freq.items():
#     print("%s : % d" % (key, value))

n = int(input("number of bottles"))
res = list(map(int,input().split()))
lst = []
for i in res:
    lst.append(res.count(i))
print(max(lst))
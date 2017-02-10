a = [-2, 23, 4]
i = 0
min = a[i]
max = a[i]
while i < len(a):
    if a[i] < min:
        min = a[i]
        print(min)
    if a[i] > max:
        a.remove(a[i])
    i = i + 1
print(a[0]*a[1])


# lst = [-2, 23, 4]
# lst.remove(max(lst))
# print(lst[0]*lst[1])
#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
核心思想：利用快排思想，先假定从大到小排序，找枢纽，枢纽会把大小分开它的两边，当枢纽下标等于k时，
即分了k位在它左边或右边，也就是最大或最小的排到了它的左边或右边了。那么那个枢纽就是要找的第k位了
"""

# 快排，找枢纽，从大到小排序
def partation(arr, low, high):
    key = arr[low]
    while(low < high):
        while(low < high and arr[high] <= key):
            high -= 1
        a[low] = a[high]
        while(low < high and arr[low] >= key):
            low += 1
        a[high] = a[low]
    # arr[low] = key
    return low

def findkth(arr,start,end,k):
   # 先进行一次快排，取得枢纽 
   pivot = partation(arr, start, end)
   """
   pivot-start+1表示快排的前半段元素的个数（包括中轴）
   当查了一次后，就划分了两边，大的在左边，小的在右边
   """
   if k == pivot - start + 1:
       return a[pivot]
   elif k > pivot - start + 1: 
       """
       说明第k大的元素在后半段，所以往后面查，start=pivot+1，
       k = k-（pivot+1-start）。为什么这样更新，想一下，我们
       虽然往后查，但查的还是整个数组的第k大，第一次快排枢纽
       的时候，已经把大的放右边了。
       """
       return findkth(arr, pivot + 1, end, k - pivot + start - 1)
   else:
       # 则第k大的元素在前半段，更新end=pivot-1
       return findkth(arr, start, pivot - 1, k)


a = [9,3,2,5,6,1,2,7,10,8]
k = 5
# 因为a在查找过程中会进行排序操作，所以clone一份原数组
clone_a = a[:]
index = []
value = findkth(a, 0, len(a)-1, k)
for i in range(len(clone_a)):
    if clone_a[i] == value:
        index.append(i)
print(clone_a)
print('第{}大的数是{},位置{}'.format(k, value, index))

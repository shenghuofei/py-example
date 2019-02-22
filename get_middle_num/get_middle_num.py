#!/usr/bin/env python
#-*- coding:utf-8 -*-

def get_mid(a,b):
    m, n = len(a), len(b)
    if m > n:
       a, b, m, n = b, a, n, m # 在短的list中从0-len开始找
    if n == 0:
        return None
    imin, imax, half = 0, m, (m+n+1)/2
    while imin <= imax:
        i = (imin+imax)/2
        j = half-i
        # i小了
        if i < m and a[i] < b[j-1]:
            imin = i + 1
        # i大了
        elif i > 0 and a[i-1] > b[j]:
            imax = i - 1
        # i正合适
        else:
            #到a的最小元素了，则左侧最大值为b的左侧最大值
            if i == 0: 
               max_left  
            #到b的最小元素了，则左侧最大值为a的左侧最大值= b[j-1]
            elif j == 0:
               max_left = a[i-1]
            else:
               max_left = max(a[j-1],b[i-1])
            # 共有奇数个元素，则中位数即为左侧最大值
            if (m + n) % 2 == 1:
                return max_left
            #到a的最大元素了，则右侧最小值为b的右侧最小值
            if i == m:
                min_right = b[j]
            #到b的最大元素了，则右侧最小值为a的右侧最小值
            elif j == n:
                min_right = a[i]
            else:
                min_right = max(a[j],b[i])
            return (min_right + max_left) / 2.0


a = [2]
b = [3,4]
print get_mid(a,b) 

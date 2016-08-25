# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 09:40:23 2016
python 排序算法 1）插入排序 2）希尔排序 3） 选择排序 4） 冒泡排序 5） 快排 6） 归并排序 7） 堆排序 8）基数排序
@author: knight
"""
# 定义待排记录的数据结构
class Record:
    def __init__(self, key, datnum):
        self.key = key  # 关键码
        self.datnum = datnum

# 插入排序,依次插入到有序的数据中
def insert_sort(lst):
    for i in range(1, len(lst)):
        tmp = lst[i]  # 待排数字
        j = i
        while j > 0 and lst[j-1].key > tmp.key:
        # 当前值大于带排数字关键码，
        #说明不是插入点移动位置
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = tmp  # j为最终插入点
    return lst

# 希尔排序是插入排序的扩展，通过允许非相邻的元素进行交换来提高执行效率。
# 关键在于步长的选择，Knuth提出：1 4 13 40....即*3 + 1

def shell_sort(lst):
    length = len(lst)
    inc = 0  # 步长
    while inc <= length/3:
        inc = inc*3 + 1
    while inc >= 1:
        for i in range(inc, length):
            tmp = lst[i]
            for j in range(i, 0, -inc):
                if tmp.key < lst[j-inc].key:
                    lst[j] = lst[j-inc]
                else:
                    j += inc
                    break
            lst[j-inc] = tmp
        inc //= 3
    return lst


# 选择排序，顺序扫描序列中元素，记录遇到的最小的元素，依次扫描得到一个待排序列中
#　最小元素，　所以是与初始状态无关的
def select_sort(lst):
    for i in range(len(lst)-1):
        k = i
        for j in range(i, len(lst)):
            if lst[j].key < lst[k].key:  # 记录遇到的最小元素
                k = j
        if k!=i:
            lst[k], lst[i] = lst[i], lst[k]
    return lst

# 交换排序,冒泡排序o(n^2)

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(1,len(lst)-i):
            if lst[j-1].key > lst[j].key: # 前面一个数大于后面的数
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst

# 交换排序，冒泡排序改进，添加标记，当没有逆序对就排序完成，返回
def bubble_sort_flag(lst):
    for i in range(len(lst)):
        flag = False
        for j in range(1, len(lst)-i):
            if lst[j-1].key > lst[j].key:
                flag = True
                lst[j-1], lst[j] = lst[j], lst[j-1]
        if not flag:
            return lst
    return lst


# 快速排序

def quick_sort_rec(lst):
    qsort_rec(lst,0,len(lst)-1)
    return lst

def qsort_rec(lst, l, r):
    if l >= r:
        return
    i = l
    j = r
    pivot = lst[i]  # 选择划分
    while i < j:
        while i<j and lst[j].key >= pivot.key:
            j -= 1
        if i < j:
            lst[i] = lst[j]
            i += 1
        while i<j and lst[i].key <= pivot.key:
            i += 1
        if i < j:
            lst[j] = lst[i]
            i -= 1
    lst[i] = pivot
    qsort_rec(lst, l, i-1)
    qsort_rec(lst, i+1, r)

# ３行代码快排实现，小于ｐｉｖｏｔ在左，大于在右，使用列表递推式
def quick_rec_lst(lst):
    if len(lst)<=0:
        return []
    return quick_rec_lst([e for e in lst[1:] if e.key < lst[0].key]) + [lst[0]] + quick_rec_lst([e for e in lst[1:] if e.key >= lst[0].key])

# 归并排序
def merge(left, right):  # 合并左右两个有序序列
    ret = []
    i, j = 0, 0
    while i<len(left) and j < len(right):
        if left[i].key < right[j].key:
            ret.append(left[i])
            i += 1
        else:
            ret.append(right[j])
            j += 1
    ret += left[i:]
    ret += right[j:]
    return ret


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

# 基数排序

# 堆(大根堆和小根堆)排序 1) 堆调整　２）　建立堆　３）　堆排序
def adjust_heap(lst, i, size):  # 大根堆
    lchild = 2*i + 1
    rchild = 2*i + 2
    mx = i
    if i < size/2:
        if lchild < size and lst[lchild].key > lst[mx].key:
            mx = lchild
        if rchild < size and lst[rchild].key > lst[mx].key:
            mx = rchild
        if mx != i:  #　出现不满足堆性质的结点，需要调整
            lst[mx], lst[i] = lst[i], lst[mx]
            adjust_heap(lst, mx, size)  # 向下调整


def build_heap(lst, size):
    for i in range(0, (size/2))[::-1]:
        adjust_heap(lst, i, size)

def heap_sort(lst):
    size = len(lst)
    build_heap(lst, size)
    for i in range(0, size)[::-1]:
        # print lst[0].key
        lst[0], lst[i] = lst[i], lst[0]  # 交换堆顶和最后一个数
        adjust_heap(lst,0,i)  # 堆顶向下调整
    return lst


# 排序测试
import random

def test(func):
    print "使用的排序算法： ",func.__name__
    records = []
    for i in range(10):
        records.append(Record(random.randint(1,20), i))  # 随机生成1-20的十个数字
    print ('待排序列')
    for r in records:
        print r.key,

    ret = func(records)
    print ('\n排序后：')
    for e in ret:
        print e.key,
    print "\n########## end sort #############"

if __name__=='__main__':
    test(insert_sort)
    test(select_sort)
    test(bubble_sort)
    test(bubble_sort_flag)
    test(quick_sort_rec)
    test(quick_rec_lst)
    test(merge_sort)
    test(shell_sort)
    test(heap_sort)

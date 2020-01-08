# 堆队列算法
堆是一个二叉树，父节点的值都会小于或大于所有孩子节点的值。最有趣的特性是heap[0]永远是最小的元素。
## 内置函数
### 创建堆
将list x 转换成堆，原地，线性时间内
1. 使用list初始化为[]
2. 使用heapq.heapify()
### 其他函数
heappush(heap,item)：把Item的值加入到heap中 
 
heappop(heap):弹出并返回heap的最小元素。

heappushpop(heap,item)：先放入堆，再返回最小元素

heapreplace(heap,item): 弹出并返回heap中最小的一项，同时推入新的item

heapq.merge(*iterable,key=,reverse):多个已排序输入合并成一个已排序输出。

heapq.nlargest/msmallest

## 实现堆排序
见1.1_heapsort：不稳定排序，利用堆的heappop方法

## 实现优先级队列
见1.1_priorityQueue
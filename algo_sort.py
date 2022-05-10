# 分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面
# 在这个分割结束之后，对当前基准值的排序就已经完成
def partition(arr,low,high):
    pivot = arr[high]   # 将排在最后的元素定为 基准值pivot
    i = low-1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1  # 确保i指向比pivot小队列的尾端
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]   # 将pivot放到 比pivot小队列 的右边
    return (i+1)    # 返回pivot的index值

def quickSort(arr,low,high):
    # 排除 只有一个元素(不用排序)情况
    if low < high:
        pivot_index = partition(arr, low, high)
        quickSort(arr, low, pivot_index-1)
        quickSort(arr, pivot_index + 1, high)

arr = [7,15,24,35,88,6,23]
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)


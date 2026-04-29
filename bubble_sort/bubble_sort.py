def bubble_sort(arr):
    """
    Bubble Sort 演算法
    時間複雜度: O(n^2)
    空間複雜度: O(1)
    穩定排序: 是
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", numbers)
    print("Sorted:", bubble_sort(numbers))
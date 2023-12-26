def sort_the_array(n, arr):
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        return "yes\n1 1"
    
    start = -1
    end = -1
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            start = i
            break
    
    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1]:
            end = i
            break
    
    reversed_segment = arr[start:end+1][::-1]
    if reversed_segment == sorted_arr[start:end+1]:
        return f"yes\n{start+1} {end+1}"
    else:
        return "no"

n = int(input())
arr = list(map(int, input().split()))

result = sort_the_array(n, arr)
print(result)

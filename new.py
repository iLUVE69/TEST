print ("This is a new file that i will push to remote repo")
print ("This is the 2nd line of the new file and i will write a function")

def binary_search(arr, target):
    low = 0 
    high = len(arr) - 1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1   
def sort_array(arr):
    return sorted(arr)

n = int(input("How many numbers do you want to enter in the array: "))
arr = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)
target = 5
arr = sort_array(arr)
result = binary_search(arr, target)
print(result)
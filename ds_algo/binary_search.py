# input 
tests = [
{
        'input': [3,4,5,1,2],
        'output':3,
        },
        {
        'input':[-1,0,1,2,-4,-3,-2],
        'output':4
        },
        {
        'input':[-1,0,1,2,-4],
        'output':4
        },
        {
        'input':[1,2,3,4,5],
        'output':0
        },
        {
        'input':[],
        'output':0
        },
        {
        'input': [5, 1, 2, 3, 4],
        'output': 1,  # 1 is smaller than 5
    },
    {
        'input': [-2, -3, -1, 0, 2],
        'output': 0,  # -3, -2, and -1 are smaller than -2
    },
    {
        'input': [10, 11, 12, 1, 2, 3],
        'output': 3,  # 1, 2, and 3 are smaller than 10
    },
    {
        'input': [4, 5, 6, 7, 1, 2, 3],
        'output': 4,  # 1, 2, 3, and 4 are smaller than 4
    },
    {
        'input': [7, 8, 9, 3, 4, 5, 6],
        'output': 3,  # 3, 4, and 5 are smaller than 7
    },
    {
        'input': [10],
        'output': 0,  # 1 is smaller than 10
    },
    {
        'input': [9, 5, 6, 7, 8],
        'output': 1,  # 5, 3, 6, and 7 are smaller than 9
    },
    {
        'input': [0, 1, 2, 3, 4],
        'output': 0,  # No elements are smaller than 0
    },
    {
        'input': [10, -3, -2, 1, 2],
        'output': 1,  # 0, -3, -2, 1, 2 are smaller than 10
    },
    {
        'input': [-5, -4, -3, -2, -1],
        'output': 0,  # No elements are smaller than -5
    },
    {
        'input': [3, 4, 5, 1, 2],
        'output': 3,  # The smallest element is 1 at index 3, so output is 3 - 1 = 2
    },
    {
        'input': [2, 3, 4, 5, 1],
        'output': 4,  # The smallest element is 1 at index 4, so output is 4 - 1 = 3
    },
    {
        'input': [1, 2, 3, 4, 5],
        'output': 0,  # No rotation, smallest element is 1 at index 0, so output is 0 - 1 = -1
    },
    {
        'input': [4, 5, 6, 7, 8, 9, 1, 2, 3],
        'output': 6,  # The smallest element is 1 at index 6, so output is 6 - 1 = 5
    },
    {
        'input': [8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7],
        'output': 7,  # The smallest element is 1 at index 7, so output is 7 - 1 = 6
    },
    {
        'input': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 3, 4, 5],
        'output': 14,  # The smallest element is 1 at index 14, so output is 14 - 1 = 13
    },
    {
        'input': [10, 20, 30, 40, 50, 5, 6, 7],
        'output': 5,  # The smallest element is 5 at index 5, so output is 5 - 1 = 4
    },
    {
        'input': [30, 40, 50, 60, 70, 10, 20],
        'output': 5,  # The smallest element is 10 at index 5, so output is 5 - 1 = 4
    },
]
# linear search function
def find_rotation(numbers):
    i = 0
    while (i<len(numbers)-1):
        if (numbers[i]>numbers[i+1]):
            return i
        i+=1
    return 0

# binary search function
def find_rotation(numbers):
    lo = 0
    hi = len(numbers)-1
    if len(numbers)>0 and numbers[lo]<=numbers[hi] or len(numbers) == 0:
        return 0
    while (lo<=hi):
        mid = (lo+hi)//2
        if mid>0 and numbers[mid-1] > numbers[mid] :
            return mid
        elif numbers[mid] > numbers[mid+1]:
            return mid+1
        elif numbers[mid] < numbers[lo] :
            hi = mid-1
        else:
            lo = mid+1



for test in tests:
    print(find_rotation(test['input'])==test['output'])

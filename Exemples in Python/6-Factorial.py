#Factorial Time 𝑂(𝑛!) :

def permutation(arr, start=0):
    if start == len(arr):
        print(arr)
    else:
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]
            permutation(arr, start + 1)
            arr[start], arr[i] = arr[i], arr[start]  # backtrack

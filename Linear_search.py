# iterative function for finding position of element
def linear_search(arr, length, ele):
    for i in range(0, length):
        if (arr[i] == ele):
            return i
        
    return -1

# driver code 
if __name__ == "__main__":
    arr = [ 20, 15, 5, 30, 50, 45]
    ele = 50
    length = len(arr)

# calling the function and assigning a variable to it 
    output = linear_search(arr, length, ele)
    
    if (output == -1):
        print(f'{ele} is not included in array.')
    else:
        print(f'{ele} is on {output} position.')
    

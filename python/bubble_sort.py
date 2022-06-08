
def bubble_sort(sequence):
    swaps = 0
    for i in range(len(sequence)):
        for j in range(0, len(sequence) - i - 1):
            curr = sequence[j] #setting variables to keep track of curr and next
            next_num = sequence[j + 1]
            if curr > next_num: #if curr is greater than next num, will need to swap
                temp = curr #keeping track of curr num
                curr = next_num #set curr = to next
                next_num = temp #next num = the temp (which was the curr)
                swaps += 1 #add each swap to swaps count
                
    print(f"Swaps: {swaps}")        
    return(sequence)    

print(bubble_sort([4, 3, 5, 0, 1]))
print(bubble_sort([10, 2, 5, 3, 1]))
print(bubble_sort([1, 20, 5, 34, 4]))
print(bubble_sort([9, 8, 7, 6, 5]))

# Given the numbers 0 through 5, what would be the worst case scenario for bubble sort (aka, what order would necessitate the most swaps)?
    #if the numbers were highest to lowest in the original array 
# How many swaps would that worst case take?
    #O(n^2)
# The example above took 21 iterations to get to a result. Can you tweak the algorithm so that it takes the same number of swaps (7) but fewer total operations?
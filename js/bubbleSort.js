function bubbleSort(arr){
    let swaps = 0
    for(let i = 0; i < arr.length; i++){
        for(let j = 0; j < (arr.length - i - 1); j++){
            let curr = arr[j]
            let next = arr[j + 1]
            if(curr > next){
                let temp = curr
                curr = next
                next = temp
                swaps++;
            }
        }
    }
    console.log("Swaps: " + swaps)
    return "Final result: " + arr
}

console.log(bubbleSort([4, 3, 5, 0, 1]))
console.log(bubbleSort([10, 2, 5, 3, 1]))
console.log(bubbleSort([1, 20, 5, 34, 4]))
console.log(bubbleSort([9, 8, 7, 6, 5]))
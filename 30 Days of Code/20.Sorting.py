"""
Objective
Today, we're discussing a simple sorting algorithm called Bubble Sort. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array,a , of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above.
Once sorted, print the following 3 lines:

1. Array is sorted in numSwaps swaps.
where numSwaps  is the number of swaps that took place.
2. First Element: firstElement
where  firstElement is the first element in the sorted array.
Last Element: lastElement
where lastElement is the last element in the sorted array.
Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.

Input Format

The first line contains an integer, n, denoting the number of elements in array a.
The second line contains n space-separated integers describing the respective values of a0,a1,...,an-1.


Output Format

Print the following three lines of output:

1. Array is sorted in numSwaps swaps.
where numSwaps  is the number of swaps that took place.
First Element: firstElement
where firstElement  is the first element in the sorted array.
Last Element: lastElement
where lastElement  is the last element in the sorted array.

Sample Input 0

3
1 2 3

Sample Output 0

Array is sorted in 0 swaps.
First Element: 1
Last Element: 3

Explanation 0

The array is already sorted, so 0 swaps take place and we print the necessary 3 lines of output shown above.

Sample Input 1

3
3 2 1

Sample Output 1

Array is sorted in 3 swaps.
First Element: 1
Last Element: 3

Explanation 1

The array a=[3,2,1]  is not sorted, so we perform the following 3 swaps:
1.[3,2,1] => [2,3,1]
2.[2,3,1]=>[2,1,3]
3.[2,1,3]=>[1,2,3]
At this point the array is sorted and we print the necessary  lines of output shown above.

"""

#Solution

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwaps = 0


for num in range(1,len(a)):
    for i in range(num,0,-1):
        if a[num] < a[i-1]:
            a[num] , a[i-1] = a[i-1], a[num]
            numSwaps += 1



print("Array is sorted in", numSwaps, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[-1])

'''
The provided code stub reads and integer, n, from STDIN. For all non-negative
integers i<n, print i2.

Example
n = 3
The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

0
1
4
Input Format

The first and only line contains the integer, .

Constraints


Output Format

Print  lines, one corresponding to each .

Sample Input 0

5
Sample Output 0

0
1
4
9
16
'''
n = int(input('Enter an Integer'))
if 1 <= n <= 20:
    for i in range(0, n):
        square = i * i
        print(square)



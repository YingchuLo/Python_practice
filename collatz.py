""""
what collatz function do?
let user enter a number
if the number is an odd, then print (3 * number +1)
if the number is an even, then print (number // 2)

Keep calling collatz until 1 shows up
"""

def collatz( number ):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return  int(3*number + 1)
number = int(input("input a number: "))

while number != 1:
    print( collatz( number ) )
    number = collatz( number )

"""
output:
input a number: 3
10
5
16
8
4
2
1
"""
## Functions 2 Exercise

# Instructions

In this coding exercise, you're going to create a simple calculator. You will need to create 4 functions so that when you run the code, `a` and `b` are added/subtracted/multiplied and divided by each other.

For example, if 

`a = 3` and 
`b = 4`

This is what you would expect to be printed from the calculator:
```
7
-1
12
0.75
```
Because:

3 + 4 = 7,

3 - 4 = -1,

3 x 4 = 12,

3 ÷ 4 = 0.75

See if you can write the four different functions in the main.swift file which do the calculations and then print out the values as per the example above. 

# Hint

Did you get 0 for the last value? Hint: you'll need to remind yourself about Swift data types and [maybe this link to Google will help](https://www.google.com/search?ei=VAIeXbqUO-Gj1fAPk9eLuAo&q=convert+an+Int+to+Double+Swift+stackoverflow&oq=convert+an+Int+to+Double+Swift+stackoverflow)



# Test Your Code with Different Inputs

For a working calculator `a` and `b` should be able to be any number. To read your own inputs directly from the console, replace lines 3 and 4 in the main.swift with:
```
  let a = Int(readLine()!)! //First input
  let b = Int(readLine()!)! //Second input
```
Now if you run your code again, it will ask you for some input values. The values need to be numbers and they will be substituted into your code as the variables `a` and `b`. If you provide an input, say 5 for `a` and 9 for `b`, your console should look like this:

```
5
9
14
-4
45
0.5555555555555556
```



# Solution

[Link to Solution Code](https://gist.github.com/TheMuellenator/83294ef2c2f606f146e51f4c4e547cab)
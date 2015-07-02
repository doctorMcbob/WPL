/* 
Welcome to the bizzare wonderful world of Wesley's Programming Language
Lets go through a few things

We have a print command
*/

1 print

/* 
We have the basic oporators
*/

1 2 +
3 2 -
2 4 *
5 10 /
2 6 %
print print print print print

/*
Things might look a little backwards.
Lets take a look at what is happenening here.

WPL is a stack based programming language.
this means the language stores (most of) its information in a 
stack data structure. lets call it S. whenever WPL encounters a
token that WPL does not recognize as a keyword, it takes that 
token and tries to place it onto the stack as an integer, and if
that doesn't work, it places it onto the stack as a string.
     ( Yes, that means you don't need to put quotes around 
     single word strings. I recommend that you do, just for
     the sake of readability.)

1 2 +

WPL reads code left to right, so the first token WPL encounters is 
the 1 on the left. WPL places that 1 on S. so now we have

S: 1
2 +

WPL continues. The next token is the 2. WPL places that on the stack 
as well.

S: 1, 2
+

The final token WPL encounters here is +. WPL recognizes + as a keyword
token and issues the command tied to that keyword.
Sence WPL is written in python, You can go and see any command in
wpl.py. The line for + is: s.append(s.pop() + s.pop())
WPL takes the first item on S and adds the next item on S to it. Then WPL
places the sum back on S

S: 3

Can you figure out the rest of the oporators?

3 2 -
2 4 *
5 10 /
2 6 %

You may have trouble with - / and % sense they are impacted by order.
one minus two is very different from two minus one.
Just keep in mind the order that WPL does things. WPL takes the first
item off S and subtracts (or devides or mods...) the second item off S

after all those oporations, S is full of integers.
S: 3, -1, 8, 2, 0

finally, five print statements, each one prints the next item on S.

print print print print print
output looks like this:
0
2
8
-1
3
*/
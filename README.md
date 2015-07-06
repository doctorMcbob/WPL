### WPL or Wesley's Programming Language

a stack based programming language

July 2nd 2015 build

OPORATORS AND STUFF:

	  +, -, *, /, %
	  ==, <=, >=, <, >
	  and, not, or, xor

	  0 1 == not 1 1 + 1 2 - == and 
	  this is true^


STRINGS:

	" this is a string "
	' this is also a string '
	the space before and after the " or ' is very important


KEYWORDS:
	<keyword: syntax>


	print: " print this " print
	      prints a value

	=: 3 = x
	      sets a variable

	dup: 1 dup +  (is equivelent to) 1 1 +
	      duplicates the next item on the stack

	swap: 2 1 swap - (is equivelent to) 1 2 -
	     swaps the next two items on the stack

	eat: " eat this thing " eat
	     removes the next item from the stack

	inp: inp print
	     puts user input on the stack as int if able else string

	if: true if " do this " print endif
	    if true is the next item on the stack, 
	    do everything until endif

	loop: loop ( true ) " do this " print endloop
	    loops untill parameters is false

	exit: exit
	    quits

	del: del thing
	    removes next token from the namespace

	import: " something.wes " import
	    runs the next item on the stack as the filename

FUNCTIONS:
	
	name : commands commands... endname
	^string			    ^not a string

	" fn " : 1 + endfn
	1 fn print
	^this will print 2

DATA STRUCTURES:

     Queues:
		n Que 
		will generate a Queue with the next 
		n items on the stack

     Stack:
		n Stk
		will generate a Stack with the next
		n items on the stack

     BOTH DATA STRUCTURES:
  
		pop:
			a_Que pop
			^or stack 
			puts the next item in the 
			data structure onto the stack

		push:
			a_Que n push
			^or stack
			push next item on the stack 
			into the datastructure 

		quetools.wes is a lybrary of 
   		  WPL functions for working with Ques
   
   
NAMESPACES:
	
	dictionary has "global":{}
				^everything you create in the global
				namespace goes here

	namespace: sets current namespace to the next word on the stack
		Name namespace 
		^sets namespace to Name. 
		
		then the dictionary will have "Name":{}
						     ^Everything you create
						     in this namespace goes here
						     
	!namespace: puts the current namespace on the stack
		This lets you do this:
		!namespace = Name
		" new namespace " namespace
		... code code code ...
		Name namespace
		
		this is how WPL handles scopes. Its on the programmer to make the scopes.
		

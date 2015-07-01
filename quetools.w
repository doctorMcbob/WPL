/*
WPL functions for working with Ques
*/

/* 
Function that generates a Que full of a range of ints
the python equivalent to range(s.pop())
*/

range : 
      = _i
      0 = _n
      _i
      loop ( _n _i > )
      	   dup 1 swap - 
	   _n 1 + = _n
      endloop
      _i Que
endrange

/* 
Function that returns size of a Que to the stack
*/

sizeof :
       dup = _que = _que_copy
       0 = _n
       _que_copy FLAG push = _que_copy
       loop ( _que_copy pop FLAG == not )       
       	    _n 1 + = _n
       endloop
       _n
endsizeof

/* test */
10 range print
50 range sizeof print

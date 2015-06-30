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

/* test */
10 range print
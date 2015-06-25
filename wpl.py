s, d = [], {}

def run(code):
    DEBUG = False
    cmds=code.split()[::-1]
    while cmds and cmds != "exit":
        cmd=cmds.pop()
        if DEBUG: debug(debug_options=["off", "quit", "s", "d", "cmds", "cmd", "step", "cmdsappend"], cmd=cmd, cmds=cmds)
        if cmd == "print": print s.pop()
        
        elif cmd == "!D": print d
        elif cmd == "!S": print s
        elif cmd == "!CMDS": print cmds
        elif cmd == "!DEBUG": DEBUG = True
        
        elif cmd == "+": s.append(s.pop() + s.pop())
        elif cmd == "-": s.append(s.pop() - s.pop())
        elif cmd == "*": s.append(s.pop() * s.pop())
        elif cmd == "/": s.append(s.pop() / s.pop())
        elif cmd == "%": s.append(s.pop() % s.pop())
        
        elif cmd == "==":
            if s.pop() == s.pop():
                s.append("true")
            else:
                s.append("false")
        
        elif cmd == ">":
            if s.pop() > s.pop():
                s.append("true")
            else:
                s.append("false")

        elif cmd == "<":
            if s.pop() < s.pop():
                s.append("true")
            else:
                s.append("false")

        elif cmd == "<=":
            if s.pop() <= s.pop():
                s.append("true")
            else:
                s.append("false")

        elif cmd == ">=":
            if s.pop() >= s.pop():
                s.append("true")
            else:
                s.append("false")

        elif cmd == '"' or cmd == "'":
            word, string = cmds.pop(), ""
            while word != cmd:
                string += word+" "
                word = cmds.pop()
            s.append(string)
        
        elif cmd == "not":
            t = s.pop()
            if (t == "false" or t == 0):
                s.append("true")
            else: s.append("false")

        elif cmd == "and":
            t1, t2 = s.pop(), s.pop()
            if (t1 == "false" or t1 == 0) or (t2 == "false" or t2 == "0"):
                s.append("false")
            else: s.append("true")

        elif cmd == "or":
            t1, t2 = s.pop(), s.pop()
            if (t1 == "false" or t1 == 0) and (t2 == "false" or t2 == "0"):
                s.append("false")
            else: s.append("true")

        elif cmd == "xor":
            t1, t2 = s.pop(), s.pop()
            if ((t1 == "false" or t1 == 0) and (t2 == "false" or t2 == "0")) or (not (t1 == "false" or t1 == 0) and not (t2 == "false" or t2 == "0")):
                s.append("false")
            else: s.append("true")

        elif cmd == "=": d[cmds.pop()] = s.pop()
        elif cmd == "dup": s.append(s[-1])
        elif cmd == "inp": 
            inp=raw_input()
            try:
                s.append(int(inp))
            except ValueError:
                s.append(inp)
        
        elif cmd == "if":
            boolean, word, commands, depth = s.pop(), cmds.pop(), [], 0
            if DEBUG: print "Iffing... " , "\nword :", word, "depth :", depth, "\ncommands :", commands, "\n\n"
            while not (word == "endif" and depth == 0):
                if word == "if": depth += 1
                elif word == "endif": depth -= 1
                commands.append(word)
                word = cmds.pop()
                if DEBUG: print "Iffing... " , "\nword :", word, "depth :", depth, "\ncommands :", commands, "\n\n"
            if boolean != "false" and boolean != 0:
                cmds += commands[::-1]

        elif cmd == "loop":
            #I want this to look like this -->  " loop ( param ) commands commands commands... endloop " 
            # param if commands... loop ( param ) commands... endloop endif 
            cmds.pop() #pop word here should always be (
            param, word = [], cmds.pop()
            if DEBUG: print "Building loop...\nParam stage.\n\nParam: ", param, "word: ", word
            while word != ")":
                param.append(word)
                word = cmds.pop() #pop second to skip the )
                print "word: ", word, "\nparam: ", param
            commands = []
            depth = 1
            print "Commands stage."
            while not (word == "endloop" and depth == 0): 
                word = cmds.pop()
                if word == "loop": depth += 1
                elif word == "endloop": depth -= 1
                commands.append(word)
                print "word: ", word, "depth: ", depth, "\ncommands: ", commands
            pile = param + ["if"] + commands + ["loop","("] + param + [")"]+ commands + ["endloop", "endif"]
            cmds += pile[::-1]
        elif cmd == "/*":
            word = cmds.pop()
            while word != "*/":
                word = cmds.pop()
        elif cmd in d: s.append(d[cmd])
            
        else:
            try:
                s.append(int(cmd))
            except ValueError:
                s.append(cmd)

def debug(debug_options, cmd, cmds, s=s, d=d):
    print "cmd: ", cmd, "| d: ", d, "| s: ", s
    i=""
    while i != "step":
        i=raw_input("--DEBUG--\n:")
        if i in debug_options:
            if i == "off": 
                DEBUG = False
            elif i == "quit": 
                exit()
            elif i == "cmds":
                print cmds
            elif i == "cmd":
                print cmd
            elif i == "s":
                print s
            elif i == "d":
                print d

            elif i == "cmdsappend":
                cmds += raw_input(":").split()[::-1]
        elif not i:
            i="step"
        else:
            print "Invalid command"
    print "stepping... "


        
loopsWPL = """
/* 
Stacking loops! The dream is real!
simple code to show off loops in loops.
*/

10 = x
loop ( x 0 <= ) 
    x print 
    1 x - = x
    " " print
    0 = y
    loop ( y 10 >= )
        y print
        1 y + = y
    endloop
    " " print
endloop
"""

ifWPL = """ 
/* 
stacking ifs
both are functional
NOTE: empty input still passes
*/


" Input: " print
inp if
    " Your input passed " print
    " enter 0 or false " print
    " Input " print
    inp if
        " That is not what I told you to input! " print
    endif
    ok print
endif
ok print
"""

debugWPL = """ 
/* 
Testing Debug mode
*/
!DEBUG
10 print 
10 = x
x print

"""
            
if __name__ == "__main__":
    import sys
    import os
    if os.path.isfile(sys.argv[-1]) and not sys.argv[-1] == "wpl.py":
        code = open(sys.argv[-1], "r").read()
        run(code)
    else:
        while True:
            run(raw_input(" > "))

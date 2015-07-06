import os
import sys
s, d, f = [], {"global": {}}, {"global": {}}
DEBUG = False


def run(code):
    current_namespace = "global"
    global DEBUG
    debug_options = ["off", "quit", "s",
                                    "d", "f", "cmds",
                                    "cmd", "step", "cmdsappend"]
    cmds = code.split()[::-1]
    while cmds:
        cmd = cmds.pop()
        if DEBUG:
            debug(debug_options=debug_options, cmd=cmd, cmds=cmds)
        if cmd == "print":
            print s.pop()
        elif cmd == "!F":
            print f
        elif cmd == "!D":
            print d
        elif cmd == "!S":
            print s
        elif cmd == "!CMDS":
            print cmds
        elif cmd == "!DEBUG":
            DEBUG = True

        elif cmd == "+":
            s.append(s.pop() + s.pop())
        elif cmd == "-":
            s.append(s.pop() - s.pop())
        elif cmd == "*":
            s.append(s.pop() * s.pop())
        elif cmd == "/":
            s.append(s.pop() / s.pop())
        elif cmd == "%":
            s.append(s.pop() % s.pop())

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
                string += word + " "
                word = cmds.pop()
            s.append(string[:-1])

        elif cmd == "not":
            t = s.pop()
            if (t == "false" or t == 0):
                s.append("true")
            else:
                s.append("false")

        elif cmd == "and":
            t1, t2 = s.pop(), s.pop()
            if (t1 == "false" or t1 == 0) or (t2 == "false" or t2 == "0"):
                s.append("false")
            else:
                s.append("true")

        elif cmd == "or":
            t1, t2 = s.pop(), s.pop()
            if (t1 == "false" or t1 == 0) and (t2 == "false" or t2 == "0"):
                s.append("false")
            else:
                s.append("true")

        elif cmd == "xor":
            t1, t2 = s.pop(), s.pop()
            if (((t1 == "false" or t1 == 0) and (t2 == "false" or t2 == "0"))
                or (not (t1 == "false" or t1 == 0) and
                    not (t2 == "false" or t2 == "0"))):
                s.append("false")
            else:
                s.append("true")

        elif cmd == "=":
            d[current_namespace][cmds.pop()] = s.pop()
        elif cmd == "dup":
            s.append(s[-1])
        elif cmd == "swap":
            s.extend([s.pop(), s.pop()])
        elif cmd == "eat":
            s.pop()
        elif cmd == "inp":
            inp = raw_input()
            try:
                s.append(int(inp))
            except ValueError:
                s.append(inp)

        elif cmd == "if":
            boolean, word, commands, depth = s.pop(), cmds.pop(), [], 0
            if DEBUG:
                print "Iffing... ", "\nword :", word, "depth :", depth,
                "\ncommands :", commands, "\n\n"
            while not (word == "endif" and depth == 0):
                if word == "if":
                    depth += 1
                elif word == "endif":
                    depth -= 1
                commands.append(word)
                word = cmds.pop()
                if DEBUG:
                    print "Iffing... ", "\nword :", word, "depth :", depth,
                    "\ncommands :", commands, "\n\n"
            if boolean != "false" and boolean != 0:
                cmds += commands[::-1]

        elif cmd == "loop":
            cmds.pop()
            param, word = [], cmds.pop()
            if DEBUG:
                print "Building loop...\nParam stage.\n\nParam: ",
                param, "word: ", word
            while word != ")":
                param.append(word)
                word = cmds.pop()
                if DEBUG:
                    print "\nword: ", word, "\nparam: ", param
            commands = []
            depth, word = 1, cmds.pop()
            if DEBUG:
                print "Commands stage."
            while not (word == "endloop" and depth == 0):
                commands.append(word)
                word = cmds.pop()
                if word == "loop":
                    depth += 1
                elif word == "endloop":
                    depth -= 1
                if DEBUG:
                    print "word: ", word, "depth: ", depth,
                    "\ncommands: ", commands
            pile = (param + ["if"] + commands + ["loop", "("] + param + [")"]
                    + commands + ["endloop", "endif"])
            cmds += pile[::-1]

        elif cmd == ":":
            key = s.pop()
            commands, word = [], cmds.pop()
            while word != "end" + key:
                commands.append(word)
                word = cmds.pop()
            f[current_namespace][key] = commands[::-1]

        elif cmd in ["Que", "Stk"]:
            ds = ["_" + cmd + "_"]
            this = ds
            n, i = s.pop(), 0
            while i != n:
                word = s.pop()
                this.append([word])
                this = this[1]
                i += 1
            s.append(ds)

        elif cmd == "pop":
            dta = s.pop()
            dtatype = dta[0]
            if dtatype == "_Que_":
                item = dta[1][0]
                if len(dta[1]) > 1:
                    dta[1] = dta[1][1]
                else:
                    del dta[1]

            elif dtatype == "_Stk_":
                end, n_end = dta, None
                while True:
                    try:
                        end[1]
                        n_end = end
                        end = end[1]
                    except IndexError:
                        break
                item = end[0]
                del n_end[1]
            else:
                raise ValueError("Cannot pop from " + repr(dta))
            s.append(item)

        elif cmd == "push":
            item = s.pop()
            dta = s.pop()
            dtatype = dta[0]
            if dtatype in ["_Que_", "_Stk_"]:
                end = dta
                while True:
                    try:
                        end = end[1]
                    except IndexError:
                        break
                end.append([item])
            else:
                raise ValueError("Cannot push to " + repr(dta))

        elif cmd == "/*":
            word = cmds.pop()
            while word != "*/":
                word = cmds.pop()

        elif cmd == "exit":
            exit()

        elif cmd == "del":
            item = cmds.pop()
            try:
                del d[current_namespace][item]
            except IndexError:
                try:
                    del f[current_namespace][item]
                except IndexError:
                    raise IndexError(str(item) + " is not defined")

        elif cmd == "import":
            filename = s.pop()
            if os.path.isfile(filename) and filename[-4:] == ".wes":
                run(open(filename).read())
            else:
                raise IOError(filename + "could not be imported")
        elif cmd == "!namespace":
            s.append(current_namespace)

        elif cmd == "namespace":
            current_namespace = s.pop()
            if current_namespace not in d:
                d[current_namespace] = {}
                f[current_namespace] = {}

        elif cmd in d[current_namespace]:
            s.append(d[current_namespace][cmd])

        elif cmd in f[current_namespace]:
            cmds.extend(f[current_namespace][cmd])

        elif cmd in d["global"]:
            s.append(d["global"][cmd])

        elif cmd in f["global"]:
            cmds.extend(f["global"][cmd])

        else:
            try:
                s.append(int(cmd))
            except ValueError:
                raise ValueError(str(cmd) + " is not defined")


def debug(debug_options, cmd, cmds, s=s, d=d, f=f):
    global DEBUG
    print "cmd: ", cmd, "| d: ", d, "| s: ", s
    i = ""
    while i != "step" and DEBUG:
        i = raw_input("--DEBUG--\n:")
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
            elif i == "f":
                print f

            elif i == "cmdsappend":
                cmds += raw_input(":").split()[::-1]
        elif not i:
            i = "step"
        else:
            print "Invalid command"
    print "stepping... "

if __name__ == "__main__":
    if os.path.isfile(sys.argv[-1]) and not sys.argv[-1] == "wpl.py":
        code = open(sys.argv[-1], "r").read()
        run(code)
    else:
        while True:
            try:
                run(raw_input(" > "))
            except Exception as e:
                print "ERROR: {}".format(e.message)
                continue

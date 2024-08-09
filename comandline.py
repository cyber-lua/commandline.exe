import os

def commandline():
    line = input()
    word = ""
    myarray = []
    for i in line:
        if i == " ":
            myarray.append(word)
            word = ""
        else:
            word = word + i

    myarray.append(word)

    if myarray[0] == "echo":
        print(myarray[1])
    elif myarray[0] == "edit":
        file = open(myarray[1], "w")
        file.write(myarray[2])
        file.close()
    elif myarray[0] == "read":
        file = open(myarray[1])
        print(file.read())
        file.close()
    elif myarray[0] == "append":
        file = open(myarray[1], "a")
        file.write(myarray[2])
        file.close()
    elif myarray[0] == "help":
        print("hey, this is [xyzbeepo]s super cool command line python thingy, here are the commands\necho [string]\nedit [path] [string]\nread [path]\nappend [path] [string]\nlock [password]\nremove [path]")
    elif myarray[0] == "lock":
        code = myarray[1]
        def unlock():
            inputted = input("Input passcode to continue: ")
            if inputted == code:
                commandline()
            else:
                print("incorrect code, try again")
                unlock()
        unlock()
    elif myarray[0] == "remove":
        os.remove(myarray[1])
    elif myarray[0] == "embed":
        exec(myarray[1])
    else:
        print("unknown command")
    commandline()

commandline()

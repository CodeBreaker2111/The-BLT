The-BLT
The BLT is a language. Bad Language & Tomato.

How to use interpretor:
  functions:
    create file
    Create file creates a file with the relative path
    ex: python ltl.py create codin'boy.ltl
    
    open
    Open opens a file and reads out the contents.
    ex: python ltl.py open codin'boy.ltl
    
    run
    Run runs a file with the intepretor.
    ex: python ltl.py run codin'boy.ltl


Functions and how to code:
  Ther is no math in my program, so if you try to use math, you'll probably get an error message.
  Each line of code starts with a semicolin. Comments do not.
  functions:
    1. print
      Print can print a string or variable. Print does not use qoutes for strings. If you are doing a string like in the example, it breaks if you have spaces in it unless you are using a variable.
      ex: ;print Hello!
    2. var
      Var can make variables. Var can be an integer, float, or string. All varibales are global no matter what. All variables are numbers 0 o ∞. Even if you make your first variable as 100, it will still be variable 0.
      ex: ;var 0 "Hello World!!"
      acess var ex: ;print 0
      redefine ex: ;var 0 5.962
    3. goto
      The goto command simply goes to another line of code. Comments are lines that do not start with ;. So if you have 3784657 before line 1 of code, it would still be line 1 not 3784657.
      ex: ;goto 3
    4. break if =
      Break if = ends the program if the two given values are the same. It can be int, float, string, and variables.
      ex: ;break if = 56 56
    5. if =
      If = runs the indented code below if the first two values are the same. The third vale is the number of lines are indented. It breaks if you dont put the right value... idk why.
      ex: ;if = 0 1 2
              ;var 0 "Me and 1 get along so well because were equal!"
              ;print 0
    6. break
      Break ends the program.
      ex: ;break

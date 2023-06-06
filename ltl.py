import sys
import os

#My code is like awful so there may be alot of errors. I've only seen erors with if statements and sometimes it doesnt print anything to the terminal but there are probably more. I'm working on fixing them.

code = []

def create_file(path):
    with open(path, "w") as f:
        f.write("ltl file\n;;")
    print("Sucsessfuly made file as {} .".format(os.path.abspath(path)))

def open_file(path):
    with open(path, "r") as f:
        print("Sucsessfuly opened file {} .".format(os.path.abspath(path)))
        print("File Contents:")
        print(f.read())

def run(path):

    variables = []

    with open(path, "r") as f:
        data = f.read()
        code_lines = [line.lstrip(";") for line in data.split("\n") if line.startswith(";")]
        
        line = 0

        while True:
            code = code_lines[line]
            print('========')
            print(code)
            if code.startswith("print "):
                code2 = code.replace("print ", "")
                try:
                    #Print Command. Checks if it is a variable or just text
                    if int(code2) <= len(code_lines) and int(code2) >= 0:
                        print(variables[int(code2)])
                except ValueError:
                    print(code2)
            
            if code == "break":
                pass

            if code.startswith("var"):
                code2 = code_lines[line].replace("var ", "").split()
                #Variable exists
                if int(code2[0]) < len(variables):
                    #String
                    if code2[1].startswith("\"") and code2[1].endswith("\""):
                        variables[int(code2[0])] = code2[1].replace("\"", "")

                    #Float
                    elif code2[1].__contains__("."):
                        variables[int(code2[0])] = float(code2[1])

                    #Int
                    else:
                        variables[int(code2[0])] = int(code2[1])

                #Variable does not exist
                else:
                    #String
                    if code2[1].startswith("\"") and code2[1].endswith("\""):
                        variables.append(code2[1].replace("\"", ""))
                    
                    #Float
                    elif code_lines[line][1].__contains__("."):
                        variables.append(float(code2[1]))

                    #Int
                    else:
                        variables.append(int(code2[1]))
            
            if code.startswith("goto "):
                line = int(code.replace("goto ", "")) - 2
            
            if code.startswith("break if ="):
                code2 = code_lines[line].replace("break if = ", "").split()
                try:
                    try:
                        if int(code2[0]) <= len(code_lines) and int(code2[0]) >= 0:
                            if variables[int(code2[0])] == code2[1]:
                                break
                    except ValueError:
                        if int(code2[0]) == int(code2[1]):
                            break
                except ValueError:
                    if code2[0] == code2[1]:
                        break

            
            if code == "break":
                break
            
            #print('-----------')
            #print(code)
            if code.startswith("if = "):
                line2 = 0
                code2 = code_lines[line].replace("if = ", "").split()
                try:
                    try:
                        if int(code2[0]) <= len(code_lines) and int(code2[0]) >= 0:
                            if variables[int(code2[0])] == code2[1]:
                                while line2 <= int(code2[2]):
                                    line2 += 1
                                    code_lines[line + line2] = code_lines[line + line2].replace("   ", "")
                            else:
                                while line2 <= int(code2[2]):
                                    line2 += 1
                                    code_lines[line + line2] = "    " + code_lines[line + line2]
                    except ValueError:
                        if int(code2[0]) == int(code2[1]):
                            while line2 <= int(code2[2]):
                                line2 += 1
                                code_lines[line + line2] = code_lines[line + line2].replace("   ", "")
                        else:
                            while line2 <= int(code2[2]):
                                line2 += 1
                                code_lines[line + line2] = "    " + code_lines[line + line2]
                except ValueError:
                    if code2[0] == code2[1]:
                        while line2 <= code2[2]:
                            line2 += 1
                            code_lines[line + line2] = code_lines[line + line2].replace("   ", "")
                    else:
                        while line2 <= code2[2]:
                            line2 += 1
                            code_lines[line + line2] = "    " + code_lines[line + line2]
            
            # Break if line is greater than the length of the code
            if line >= len(code_lines) - 1:
                break
                
            line += 1



script_name = sys.argv[0]
function_name = sys.argv[1]
arguments = sys.argv[2:]

functions = {
    "create_file": create_file,
    "open": open_file,
    "run": run
}

if function_name in functions:
    # Call the function with the provided arguments
    functions[function_name](*arguments)
else:
    print("Function not found.")

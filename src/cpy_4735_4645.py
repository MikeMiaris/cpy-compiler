# MICHALIS MIARIS 4735 (cse94735) , ILIAS GEORGIADIS 4645 (cse94645)

import sys

#for .cpy file
filename = str(sys.argv[1])
file = open(filename,'rb')

#for .int file
quadfile = open(str(sys.argv[1])[:-4]+".int",'w')

#for .sym file
symfile = open(str(sys.argv[1])[:-4]+".sym",'w')

#for .asm file
asmfile = open(str(sys.argv[1])[:-4]+".asm",'w')


retflag = 0
D = []
line = 1
id = 1
quad_list = []
T_counter = 0
paramcount = 0
fpcount = 0


allowed = ['+','-','*','/','%' ,'<','>','!','=',',',':','(',')','{', '}' ,'#' ,' ','\t','\r','\n','_',""]
keywords = ["if","elif", "else","#def","def","while","return","print","int", "#int","input", "main", "global", "and", "or", "not"]

def is_not_integer(value):
    try:
        int(value)
        return False
    except ValueError:
        return True

offset = 12

#Lexical Analysis Class and Function
class Token:
    def __init__(self,recognized_string, fam, line_number):
        self.recognized_string = recognized_string
        self.fam = fam
        self.line_number = line_number
    
    def str(self):
        print("String:"+self.recognized_string+" Type:"+self.fam+" Line:",self.line_number)

def lex():
    global line
    str = ""
    fam = ""
    while str == "":
        charbyte = file.read(1)
        char = charbyte.decode("utf-8")
        if char not in allowed and not char.isdigit() and not char.isalpha():
            sys.exit("ERROR - INVALID CHARACTER")
          
        while char == ' ' or char == '\t' or char == '\n' or char == '\r':
            charbyte = file.read(1)
            char = charbyte.decode("utf-8")
            if char == '\n': #update line number if we find \n
                line += 1

        if char == '#':  #ANAGNORISI #{ ,#}, #declare, sxolia
            charbyte = file.read(3)
            char = charbyte.decode("utf-8")
            if char == "int":
                fam = "keyword"
                str = "#int"

            elif char == "def":
                fam = "keyword"
                str = "#def"

            else:
                file.seek(-3,1) 
            charbyte = file.read(1)
            char = charbyte.decode("utf-8")
            if char == '{':
                fam = "groupSymbol"
                str = "#{"
            elif char == '}':
                fam = "groupSymbol"
                str  = "#}"
            elif char == '#': #COMENTS
               while True:
                    charbyte = file.read(1)
                    char = charbyte.decode("utf-8")
                    if char == "#":
                         charbyte = file.read(1)
                         char = charbyte.decode("utf-8")
                         if char == "#":
                             
                             break

        strtemp = ""
        if char.isdigit():
            while char.isdigit():
                strtemp += char
                charbyte = file.read(1)
                char = charbyte.decode("utf-8")
            file.seek(-1,1)
            fam = "number"
            str = strtemp
        
        #May Need max of 30
        elif char.isalpha():
            
            while char.isalpha() or char.isdigit() or char == '_':
                strtemp = strtemp+char
                charbyte = file.read(1)
                char = charbyte.decode("utf-8")
            file.seek(-1,1)
            if len(strtemp) > 30:
                sys.exit("ERROR: Identifier has too many characters")
            if strtemp in keywords:
                fam = "keyword"
            else:
                fam = "identifier"
            str = strtemp
        
        elif char == '+':
            fam = "addOperator"
            str = "+"
        
        elif char == '-':
            fam = "addOperator"
            str = "-"
        
        elif char == '*':
            fam = "mulOperator"
            str = "*"

        elif char == '%':
            fam = "mulOperator"
            str = "%"
        
        elif char == '/':
            charbyte = file.read(1)
            char = charbyte.decode("utf-8")
            if char == '/':
                fam = "mulOperator"
                str = "//"
            else:
                sys.exit("Invalid Syntax")
        
        elif char == '<':
            charbyte = file.read(1)
            char = charbyte.decode("utf-8")
            if char == '=':
                fam = "relOperator"
                str = "<="
            else:
                file.seek(-1,1)
                fam = "relOperator"
                str = "<"
        
        elif char == '>':
            charbyte = file.read(1)
            char = charbyte.decode("utf-8")
            if char == '=':
                fam = "relOperator"
                str  = ">="
            else:
                file.seek(-1,1)
                fam = "relOperator"
                str = ">"
        
        elif char == '!':
            charbyte = file.read(1)
            char = charbyte.decode("utf-8")
            if char == '=':
                fam = "relOperator"
                str = "!="
            else:
                sys.exit("Invalid Syntax")
        
        elif char == '=':
            charbyte = file.read(1)
            char = charbyte.decode("utf-8")
            if char == '=':
                fam = "relOperator"
                str = "=="
            else:
                file.seek(-1,1)
                fam = "assignment"
                str = "="
        
        elif char == ';':
            fam = "delimiter"
            str = ";"
         
        elif char == ',':
            fam = "delimiter"
            str = ","
            
        elif char == ':':
            fam = "delimiter"
            str = ":"
            
        elif char == '(':
            fam = "groupSymbol"
            str = "("

        elif char == ')':
            fam = "groupSymbol"
            str = ")"

        elif(char == ""):
            str = "EOF"
    tok = Token(str,fam,line)
    tok.str()
    return tok



#Symbol Table Classes
class entity:
    def __init__(self,name):
        self.name = name

class Variable(entity):
    def __init__(self,name,offset):
        entity.__init__(self,name)
        self.offset = offset
 
    
    def __str__(self):
        return str(self.name)+"/" +str(self.offset)

class Parameter(Variable):
    def __init__(self,name,mode,offset):
        entity.__init__(self,name)
        self.mode = mode
        self.offset = offset
 
    
    def __str__(self):
        return f"{self.name}/{self.mode}/{self.offset}"

class Procedure(entity):
    def __init__(self,name,startquad,framelength):
        entity.__init__(self,name)
        self.startquad  = startquad
        self.framelength = framelength
        self.formalparam = []
 
    
    def str(self):
        return str(self.name)+": " + str(self.startquad) + ", "+ str(self.framelength)

class function(Procedure):
    def __init__(self,name, startquad,framelength):
        Procedure.__init__(self,name,startquad,framelength)
    
    def __str__(self):
        return str(self.name)+"/"+ str(self.startquad) + "/"+ str(self.framelength)

class scope:
    def __init__(self,nestingLevel):
        self.stack = []
        self.nestingLevel = nestingLevel
        self.offset = 12
        
    def push(self,entry):
        self.stack.append(entry)

    def pop(self):
        self.stack.pop()
        
    def __str__(self):
        stack_str = ", ".join(map(str, self.stack))  # Convert stack items to strings and join them with commas
        return f"{self.nestingLevel}: {stack_str}"

class symbol_table:
    def __init__(self):
        self.stacks = []
        self.nestingLevel = 0

    def push(self,entry):
        self.stacks.append(entry)
        self.nestingLevel = self.nestingLevel + 1

    def pop(self):
        self.stacks.pop()
        self.nestingLevel = self.nestingLevel - 1

    def search(self, target, n):
        for scope in reversed(self.stacks):
            for item in scope.stack:
                if target == item.name:
                    if n == 0:
                        return item.name
                    if n == 1:
                        return item.__class__.__name__
                    if n == 2 and item.__class__.__name__ == "function":
                        return len(item.formalparam)
                    if n == 3:
                        return item.offset
                    if n == 4:
                        return scope.nestingLevel
                    if n == 5:
                        return item.framelength
     
    def add_item(self, item):
        last_scope = self.stacks[-1]
        last_scope.push(item)
    
    def print_scopes(self):
        for scope in self.stacks:
            symfile.write(str(scope) + "\n")
        symfile.write("\n")
        
    def create_scope(self):
        new_scope = scope(self.nestingLevel)
        self.push(new_scope)
    
    def offsetincrease(self):
        self.stacks[-1].offset = self.stacks[-1].offset + 4



#Quad Class and Functions
class Quad:
    def __init__(self,id,op,v1,v2,v3):
        self.id = id
        self.op  = op
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
    
    def str(self):
        return str(self.id)+": " + str(self.op) + ", "+str(self.v1)+ ", " + str(self.v2) + ", " + str(self.v3)

def nextQuad():
    return id
    
def genquad(op, x, y, z):
    global id
    quad = Quad(id, op, x, y, z)
    id += 1
    quad_list.append(quad)

def newTemp():
    global T_counter
    T_counter += 1
    return "T_"+str(T_counter)

def emptyList():
    global labels
    labels = []
    return labels

def makeList(label):
    global labels
    labels = [label]
    return labels

def mergeList(list1,list2):
    return list1+list2
       
def backpatch(list, label):
    global quad_list
    for id in list:
        for quad in quad_list:
            if quad.id == id:
                quad.v3 = label



#Final Code Functions
def quadconverter(startquad):
    global fpcount
    skip = 0
    asmfile.write(str(startquad.v1)+":\n")
    asmfile.write("\taddi sp,sp,"+str(table.stacks[-1].offset-4)+"\n")
    asmfile.write("\tsw ra,(sp)\n")
    for i in range(startquad.id-1,len(quad_list)):
        if quad_list[i].op == "begin_block":
            skip +=  1
 
        if skip == 1:
            if quad_list[i].op != "begin_block":
                asmfile.write("L"+str(quad_list[i].id)+":\n")
            if quad_list[i].op == "jump":
                asmfile.write("\tb L" + str(quad_list[i].v3) +"\n")
            elif quad_list[i].op == "<":
                loadvr(quad_list[i].v1,"t1")
                loadvr(quad_list[i].v2,"t2")
                asmfile.write("\tblt,t1,t2," +"L"+str(quad_list[i].v3) + "\n")
            elif quad_list[i].op == "<=":
                loadvr(quad_list[i].v1,"t1")
                loadvr(quad_list[i].v2,"t2")
                asmfile.write("\tble,t1,t2," +"L"+ str(quad_list[i].v3) + "\n")
            elif quad_list[i].op == ">":
                loadvr(quad_list[i].v1,"t1")
                loadvr(quad_list[i].v2,"t2")
                asmfile.write("\tbgt,t1,t2," +"L"+ str(quad_list[i].v3) + "\n")
            elif quad_list[i].op == ">=":
                loadvr(quad_list[i].v1,"t1")
                loadvr(quad_list[i].v2,"t2")
                asmfile.write("\tbge,t1,t2," +"L"+ str(quad_list[i].v3) + "\n")
            elif quad_list[i].op == "==":
                loadvr(quad_list[i].v1,"t1")
                loadvr(quad_list[i].v2,"t2")
                asmfile.write("\tbeq,t1,t2," +"L"+ str(quad_list[i].v3) + "\n")
            elif quad_list[i].op == "!=":
                loadvr(quad_list[i].v1,"t1")
                loadvr(quad_list[i].v2,"t2")
                asmfile.write("\tbne,t1,t2," +"L"+ str(quad_list[i].v3) + "\n")
            elif quad_list[i].op == ":=":
                loadvr(quad_list[i].v1,"t1")
                storerv("t1",quad_list[i].v3)
            elif quad_list[i].op == "+":
                loadvr(quad_list[i].v1,"t1")
                loadvr(quad_list[i].v2,"t2")
                asmfile.write("\tadd,t1,t1,t2\n")
            elif quad_list[i].op == "-":
                loadvr(quad_list[i].v1,"t1")
                loadvr(quad_list[i].v2,"t2")
                asmfile.write("\tsub,t1,t1,t2\n")
            elif quad_list[i].op == "*":
                loadvr(quad_list[i].v1,"t1")
                loadvr(quad_list[i].v2,"t2")
                asmfile.write("\tmul,t1,t1,t2\n")
            elif quad_list[i].op == "//":
                loadvr(quad_list[i].v1,"t1")
                loadvr(quad_list[i].v2,"t2")
                asmfile.write("\tdiv,t1,t1,t2\n")
            elif quad_list[i].op == "retv":
                loadvr(quad_list[i].v1,"t1")
                asmfile.write("\tlw t0, -8(sp)\n")
                asmfile.write("\tsw t1, 0(t0)\n")
                
            elif quad_list[i].op == "par":
                if quad_list[i].v2 == "CV":
                    loadvr(quad_list[i].v1,"t0")
                    temp = 12+4*fpcount
                    asmfile.write("\tsw t0,-"+str(temp)+"(fp)\n")
                    fpcount += 1
                elif quad_list[i].v2 == "RET":
                    asmfile.write("\taddi t0,sp,-" +str(table.search(quad_list[i].v1,3))+"\n")
                    asmfile.write("\tsw t0,-8(fp)\n")
            elif quad_list[i].op == "call":
            
                if table.search(startquad.v1,4) == table.search(quad_list[i].v1,4):#Ean kalousa kai kleithisa ehoun idio bathos foliasmatos
                    asmfile.write("\tlw t0,-4(sp)\n")
                    asmfile.write("\tsw t0,-4(fp)\n")
                else:
                    asmfile.write("\tsw sp,-4(fp)\n")#Ean kalousa kai kleithisa einai se diaforetiko bathos foliasmatos
            
                asmfile.write("\taddi sp,sp,"+str(table.search(quad_list[i].v1,5))+"\n") #addi sp,sp,framelength
            
                asmfile.write("\tjal "+str(quad_list[i].v1)+"\n") #jal f

            elif quad_list[i].op == "end_block" and quad_list[i].v1 != "main":
                asmfile.write("\taddi sp,sp,-"+str(table.search(quad_list[i].v1,5))+"\n") #addi sp,sp,-framelength
                asmfile.write("\tlw ra,(sp)\n")
                asmfile.write("\tjr ra\n")

            elif quad_list[i].op == "out":
                asmfile.write("\tmv a0,t0\n")
                asmfile.write("\tli a7,1\n")
                asmfile.write("\tecall\n")
                asmfile.write("\tla a0,str_nl\n")
                asmfile.write("\tli a7,4\n")
                asmfile.write("\tecall\n")

            elif quad_list[i].op == "inp":
                asmfile.write("\tli a7,5\n")
                asmfile.write("\tecall\n") 
        
        elif quad_list[i].op == "end_block":
            skip -= 1    


def gnlvcode(v):
    offset = 0
    asmfile.write("\tlw t0,-4(sp)\n")
    for scope in reversed(table.stacks):
        for item in scope.stack:
            if item.name == v:
                offset = item.offset
                return offset
        asmfile.write("\tlw t0,-4(t0)\n")
    
    asmfile.write("\taddi t0,t0,-"+str(offset)+"\n")
    if offset == 0:
        sys.exit("ERROR IN GNLVCODE - V NOT FOUND")
    
    
def loadvr(v, reg):
    # v: source variable
    # reg: target register
    offset = 0
    
    nl = 33
    #retrieve information for v from symbol_table
    for scope in reversed(table.stacks):
        for item in scope.stack:
            if item.name == v:
                nl = scope.nestingLevel
                offset = item.offset
    
    if nl == 0:                                     #Global metablhth
        asmfile.write("\tlw "+str(reg)+", -"+str(offset)+"(gp)\n")
    
    elif nl == table.stacks[-1].nestingLevel:       #Metablith mesa sth synarthsh
        asmfile.write("\tlw "+str(reg)+",-"+str(offset)+"(sp)\n")
            
    
    elif nl>0 and nl<table.stacks[-1].nestingLevel: #Metablith ekso apo th synarthsh
        gnlvcode(v)
        asmfile.write("\tlw "+str(reg)+",0(t0)\n")

    
def storerv(reg,v):
    # v: source variable
    # reg: target register
    
    offset = 0
    nl = 33
    
    #retrieve information for v from symbol_table
    for scope in reversed(table.stacks):
        for item in scope.stack:
            if item.name == v:
                nl = scope.nestingLevel
                offset = item.offset
    
    if nl == 0:                                     #Global metablhth
        asmfile.write("\tsw "+str(reg)+", -"+str(offset)+"(gp)\n")
    
    elif nl == table.stacks[-1].nestingLevel:       #Metablith mesa sth synarthsh
        asmfile.write("\tsw "+str(reg)+", -"+str(offset)+"(sp)\n")
            
    
    elif nl>0 and nl<table.stacks[-1].nestingLevel: #Metablith ekso apo th synarthsh
        gnlvcode(v)
        asmfile.write("\tsw "+str(reg)+",0(t0)\n")

table = symbol_table()

#Syntax Analysis Functions
def start():
    global token
    global offset
    offset = 12
    
    asmfile.write('\t.data\nstr_nl: .asciz "\\n"\n\t.text\n')
    
    asmfile.write("j main\n")
    
    table.create_scope()
    
    declarations()
    globals()
    while token.recognized_string == "def":
        def_function()

    main_read()
    
    table.print_scopes()
    table.pop()
    
    print("\n!!--SYNTAX ANALYSIS SUCCESSFUL--!!")


def main_read():
    print("ENTERING MAIN_READ()")
    global token
    if not token.recognized_string == "#def":
        sys.exit("ERROR - #def EXPECTED")
    token = lex()

    if not token.recognized_string == "main":
        sys.exit("ERROR - KEYWORD 'main' EXPECTED")
    token = lex()
    genquad("begin_block","main","_","_")
    temp = quad_list[-1]
    declarations()

    statements()
    
    genquad("halt","_","_","_")
    genquad("end_block","main","_","_")
    
    quadconverter(temp)
    asmfile.write("exit:\n")
    asmfile.write("\tli a0,0\n")
    asmfile.write("\tli a7,93\n")
    asmfile.write("\tecall\n")
    print("EXITING MAIN_READ()")


def def_function():
    global D
    
    D = []
    
    print("ENTERING DEF_FUNCTION()")
    
    global token

    global retflag
    retflag = 0
    
    if not token.recognized_string == "def":
        sys.exit("ERROR - KEYWORD def EXPECTED ")
    token = lex()

    if not token.fam == "identifier":
        sys.exit("ERROR - IDENTIFIER EXPECTED")
    
    name = token.recognized_string #id
    genquad("begin_block",name,"_","_")

    startquad = quad_list[-1]

    f = function(name,id,'')
    table.add_item(f)
    
    
    token = lex()

    if not token.recognized_string == "(":
        sys.exit("ERROR - EXPECTING '(' ")

    table.create_scope()
    id_list()
    
    if not token.recognized_string == ")":
        sys.exit("ERROR - EXPECTING ')' ")

    stk = []
    for item in table.stacks[-1].stack:
        name1 = item.name
        print(item.name)
        offset1 = item.offset
        print(item.offset)
        item = Parameter(name1,"cv",offset1)
        stk.append(item)
        f.formalparam.append(name1)
    table.stacks[-1].stack = stk

    
    token = lex()

    if not token.recognized_string == ":":
        sys.exit("ERROR - ':' EXPECTED")

    token = lex()



    if not token.recognized_string == "#{":
        sys.exit("ERROR - '#{' EXPECTED")

    token = lex()
    declarations()
    while token.recognized_string == "def":
        def_function()
    
    globals()
    
    statements()
    
    if not token.recognized_string == "#}":
        sys.exit("ERROR - EXPECTING #} ")
     
    token = lex()
    
    if D:
        backpatch(D, nextQuad())
    
    

    genquad("end_block",name,"_","_")
    f.framelength = table.stacks[-1].offset
    
    quadconverter(startquad)
    
    table.print_scopes()
    table.pop()
    
    if retflag == 0:
        sys.exit("ERROR - NO RETURN STATEMENT IN FUNCTION")
    
    
    
    print("EXITING DEF_FUNCTION()")


def bool_factor(): #--R--
    print("ENTERING BOOL_FACTOR()")
    global token
    
    r_true = []
    r_false = []
    
    if token.recognized_string == "not":
       token = lex()
       condition()
       token = lex()
    else:
       e1_place = expression()
       if not token.fam == "relOperator":
           sys.exit("ERROR - EXPECTED RELOPERATOR")
       relop = token.recognized_string
       token = lex()
       e2_place = expression()
       
       r_true = makeList(nextQuad())
       genquad(relop,e1_place,e2_place,'_')
       r_false = makeList(nextQuad())
       genquad('jump','_','_','_')
        
    print("EXITING BOOL_FACTOR()")
    return r_true,r_false
    

def bool_term(): #--Q--
    print("ENTERING BOOL_TERM()")
    global token
    
    q_true = []
    q_false = []
    
    r1_true,r1_false = bool_factor()
    q_true = r1_true
    q_false = r1_false
    
    while token.recognized_string == "and":
        backpatch(q_true,nextQuad())
        token = lex()
        r2_true,r2_false = bool_factor()
        q_false = mergeList(q_false,r2_false)
        q_true = r2_true
        
    print("EXITING BOOL_TERM()")
    return q_true,q_false


def condition(): #--B--
    print("ENTERING CONDITION()")
    global token
    
    b_true = [] 
    b_false = []
    
    q1_true,q1_false = bool_term()
    
    b_true = q1_true
    b_false = q1_false
    
    while token.recognized_string == "or":
        backpatch(b_false,nextQuad())
        token = lex()
        q2_true,q2_false = bool_term()
        b_true = mergeList(b_true,q2_true)
        b_false = q2_false

    print("EXITING CONDITION()")
    return b_true,b_false


def while_stat():
    print("ENTERING WHILE_STAT()")
    global token
  
    
    condQuad = nextQuad() #p0
    
    cond_true,cond_false = condition()
    
    if not token.recognized_string == ":":
         sys.exit("ERROR - ':' EXPECTED ")
    
    backpatch(cond_true,nextQuad()) #p1
    
    token = lex()
    if token.recognized_string == "#{":
        token = lex()
        statements()
        if not token.recognized_string == "#}":
            sys.exit("ERROR - #} EXPECTED ")
        token = lex()
    else:
         
        statement()
    
    genquad('jump','_','_',condQuad)
    backpatch(cond_false,nextQuad())
    
    print("EXITING WHILE_STAT()")


def if_stat():
    print("ENTERING IF_STAT()")
    global token
    global retflag
    global D
    
    J = emptyList() #p0
    D = emptyList()
    
    cond1_true,cond1_false = condition()
     
    if not token.recognized_string == ":":
        sys.exit("ERROR - ':' EXPECTED ")

    token = lex()

    backpatch(cond1_true,nextQuad()) #p1

    if token.recognized_string == "#{":
       token = lex()
       
       statements()
       if not token.recognized_string == "#}":
            sys.exit("ERROR - #} EXPECTED ")
           
    else:
        statement()
    
    E = makeList(nextQuad())
    genquad("jump","_","_","_")
    if retflag == 0:
        J = mergeList(J,E)
    else:
        D = mergeList(D,E)
        retflag = 0
    backpatch(cond1_false,nextQuad())
    
    
    while token.recognized_string == "elif":
        token = lex()
        
        cond_true,cond_false = condition()

        if not token.recognized_string == ":":
            sys.exit("ERROR - ':' EXPECTED ")

        token = lex()

        backpatch(cond_true,nextQuad()) #p1

        if token.recognized_string == "#{":
            token = lex()
            statements()
            if not token.recognized_string == "#}":
                sys.exit("ERROR - #} EXPECTED ")
        else:
            statement()
        
        E = makeList(nextQuad())
        genquad("jump","_","_","_")
        if retflag == 0:
            J = mergeList(J,E)
        else:
            D = mergeList(D,E)
            retflag = 0
        backpatch(cond_false,nextQuad())
        
        

    if token.recognized_string == "else":
       token = lex()
       if not token.recognized_string == ":":
           sys.exit("ERROR - ':' EXPECTED ")
       token = lex()
        
       if token.recognized_string == "#{":
           token = lex()
           statements()
           if not token.recognized_string == "#}":
            sys.exit("ERROR - #} EXPECTED ")
       else:
        statement()
        
    backpatch(J,nextQuad())

    print("EXITING IF_STAT()")


def structured_statement():
    print("ENTERING STRUCTURED_STATEMENT()")
    global token
    if token.recognized_string == "if":
        token = lex()
        if_stat()

    elif token.recognized_string == "while":
        token = lex()
        while_stat()

    print("EXITING STRUCTURED_STATEMENT()")


def return_stat():
    print("ENTERING RETURN_STAT()")
    global retflag
    global token
    e_place = expression()
    genquad("retv",e_place,'_','_')
    retflag = 1
    print("EXITING RETURN")
    

def print_stat():
    print("ENTERING PRINT_STAT()")
    global token

    if not token.recognized_string == "(":
         sys.exit("ERROR - '(' EXPECTED ")
    token = lex()
    
    e_place = expression()

    if not token.recognized_string == ")":
         sys.exit("ERROR - ')' EXPECTED ")
    token = lex()

    genquad("out",e_place,"_","_")
    
    print("EXITING PRINT_STAT()")

f_check = 0

def assignment_stat(id_tok):
    print("ENTERING ASSIGNMENT_STAT()")
    global token
    
    
    if not token.recognized_string == "=":
        sys.exit("ERROR - '=' EXPECTED ")
    token = lex()
    if token.recognized_string == "int":
        exp = token.recognized_string
        for i in range(5):
            token = lex()
            exp += token.recognized_string

        if not exp == "int(input())":
            sys.exit("ERROR - int(input()) EXPECTED")
        token = lex()
        
        genquad("inp","_","_",id_tok)
        
    else:
        e_place = expression()
        genquad(":=",e_place,'_',id_tok)
        if is_not_integer(e_place) and (e_place != table.search(e_place,0)):
            v = Variable(e_place,table.stacks[-1].offset)
            table.offsetincrease()
            table.add_item(v)



    print("EXITING ASSIGNMENT_STAT()")


def simple_statement():
    print("ENTERING SIMPLE_STATEMENT()")
    global token

    if token.fam == "identifier":
    
        id_tok = token.recognized_string
        token = lex()
        assignment_stat(id_tok)
    
    elif token.recognized_string == "print":
         token = lex()
         print_stat()
         
    elif token.recognized_string == "return":
         token = lex()
         return_stat()

    print("EXITING SIMPLE_STATEMENT()")


def statement():
    print("ENTERING STATEMENT()")
    global token
    simple_statement()
    structured_statement()
    print("EXITING STATEMENT()")


def statements():
    print("ENTERING STATEMENTS()")
    global token
    while not token.recognized_string == "#}" and token.recognized_string != "EOF":
        statement()
    print("EXITING STATEMENT()")


def declarations():
    print("ENTERING DECLARATIONS()")
    global token

    while token.recognized_string == "#int":
        id_list()

    print("EXITING DECLARATIONS()")


def globals():
    print("ENTERING GLOBALS()")
    global token

    while token.recognized_string == "global":
        id_list()


    print("EXITING GLOBALS()")
    

def optional_sign():
    print("ENTERING OPTIONAL_SIGN()")
    global token
    minus_check = 0
    if token.fam == "addOperator":
        if token.recognized_string == "-":
            minus_check = 1
        token = lex()
        return minus_check
        
    print("LEAVING OPTIONAL_SIGN")


def actual_par_list():
    print("ENTERING ACTUAL_PAR_LIST()")
    global paramcount
    global token
    paramcount = 0
    e = expression()
    
    genquad("par",e,"CV","_")
    paramcount += 1
    
    while token.recognized_string == ",":
        token = lex()
        e = expression()
        
        genquad("par",e,"CV","_")
        paramcount +=1
        
    print("EXITING ACTUAL_PAR_LIST()")


def idtail():
    print("ENTERING IDTAIL()")
    global token
    
    
    global f_check
    f_check = 0
    
    if token.recognized_string == "(":
        token = lex()
        actual_par_list()
        if not token.recognized_string == ")":
            sys.exit("ERROR - ')' EXPECTED")
        token = lex()
        
        f_check = 1
    return f_check
    
    
    print("EXITING IDTAIL()")


def expression(): #--E--
    global token

    minus_check = 0
    minus_check = optional_sign()
    t1_place = term()
    
    if minus_check == 1:
        w = newTemp()
        genquad("-","0",t1_place,w)
        t1_place = w
    
    while token.fam == "addOperator":
        oper = token.recognized_string
        token = lex()
        t2_place = term()
        w = newTemp()
        genquad(oper, t1_place, t2_place, w)
        t1_place = w
    
    e_place = t1_place
    
    print("EXITING EXPRESSION()")
    return e_place


def term(): #--T--
    print("ENTERING TERM()")
    
    
    global token
    f1_place = factor()
    while token.fam == "mulOperator":
        oper = token.recognized_string  
        token = lex() 
        f2_place = factor()
        w = newTemp()
        genquad(oper, f1_place, f2_place, w)
        f1_place = w
    
    t_place = f1_place

    print("EXITING TERM()")
    return t_place


def factor(): #--F--
    print("ENTERING FACTOR()")
    global token
    w = ""
    global f_check
    f_check = 0
    
    if token.fam == "number":
        f_place = token.recognized_string 
        token= lex()
    
    
    elif token.recognized_string == "(":
        token = lex()
        e_place = expression()
        
        if not token.recognized_string == ")":
            sys.exit("ERROR - ')' EXPECTED")
        
        f_place = e_place
        token = lex()        
            
    elif token.fam == "identifier":
        fname = token.recognized_string
        f_place = token.recognized_string
        if fname != table.search(fname,0):
            sys.exit("ERROR - IDENTIFIER NOT INSTANTIATED")
        token = lex()
        print(table.search(fname,1))
        if token.recognized_string == "(":
            if "function" != table.search(fname,1):
                sys.exit("ERROR - FUNCTION NAME NOT RECOGNIZED")

        f_check = idtail()

        if table.search(fname,1) == "function":
            if table.search(fname,2) != paramcount:
                sys.exit("ERROR - INCORRECT FUNCTION ARGUMENTS.")
        if f_check == 1:
            w = newTemp()

            t = Variable(w,table.stacks[-1].offset)
            table.offsetincrease()
            table.add_item(t)
            
            genquad("par",w,"RET","_")
            genquad("call",fname,"_","_")
        
    else:
        sys.exit("ERROR")
    
    print("EXITING FACTOR()")
    if f_check == 0:
        return f_place
    elif f_check == 1:
        return w


def id_list():
        print("ENTERING IDLIST()")
        global token
        flowflag = 0
        if token.recognized_string == "global":
            flowflag = 1

        token = lex()
        line = token.line_number
        if not token.fam == "identifier":
            sys.exit("ERROR - EXPECTING IDENTIFIER ")

        if flowflag == 1:
            if token.recognized_string != table.search(token.recognized_string,0):
                var = Variable(token.recognized_string,table.stacks[-1].offset)
                table.offsetincrease()
                table.add_item(var)
        else: 
            var = Variable(token.recognized_string,table.stacks[-1].offset)
            table.offsetincrease()
            table.add_item(var)
        

        token  = lex()
        if token.recognized_string == ',':
            if flowflag == 1:
                while (token.fam == "identifier" or token.recognized_string == ",") and token.line_number == line:
                    if token.fam == "identifier" and (token.recognized_string != table.search(token.recognized_string,0)):
                        var = Variable(token.recognized_string,table.stacks[-1].offset)
                        table.offsetincrease()
                        table.add_item(var)             
                    token = lex()

            else:
                while (token.fam == "identifier" or token.recognized_string == ",") and token.line_number == line:
                    if token.fam == "identifier":
                        var = Variable(token.recognized_string,table.stacks[-1].offset)
                        table.offsetincrease()
                        table.add_item(var)             
                    token = lex()

        print("EXITING IDLIST()")

#Initialising syntax analysis
token = Token("","","")
token = lex()
start()

print(str(len(quad_list)) + " quads")
for quad in quad_list:
    quadfile.write(quad.str() + "\n")

#####
print()
table.print_scopes()

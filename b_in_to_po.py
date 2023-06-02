# operators :
NegO   = ['!','¬']
EqO    = ['=']
DisO   = ["+"] # disjunction
NDisO  = ["↓",'-'] # NOR

ConO   = [".","*"]  # conjunction
NConO  = ['↑','/'] # NAND
XorO   = ['⨁','⊕','^']

Bkts   = ["(",")"] 


def priority(o): # o ==> operator
    if o in NegO:   return 5 
    if o in XorO:   return 4
    if o in ConO or o in NConO : return 3
    if o in DisO or o in NDisO:  return 2
    if o in EqO :   return 1
    if o in Bkts:  return -1
    return 0 

def is_int(x):
    try:x+=1
    except TypeError:  return False
    return True

# this Function convert expresions from normal form "a+b*c" to the postfix form "b c * a +" 
def postfix(op):
    stack = [None]
    new   = []
    
    for x in op:
        if x ==' ':continue
        if not priority(x): 
            new.append(x)
        else:  
            if x in NegO or len(stack)==1 or stack[0]=='(' or x=='(' or priority(x)>priority(stack[0]) :
                if stack[0] in NegO and x not in'!¬(':
                    new.append(stack[0])
                    stack.pop(0)
                    
                stack.insert(0,x)
            elif x==')':
                while stack[0]!='(':
                    new.append(stack[0])
                    stack.pop(0)
                stack.pop(0)
            else:
                while priority(x)<=priority(stack[0]):
                    new.append(stack[0])
                    stack.pop(0)
                stack.insert(0,x)
    while stack[0]!=None:
        new.append(stack[0])
        stack.pop(0)
    return  new    

# the aim of this function is to replace the variables by (1/0) values every time from the Truth table.
# it takes expresion (PFF) and dictionary of the variables and the values ex :  replace("a B +",{"a":1,"b":0} )
def replace(exp,DItems):
    for x in range(len(exp)):
         if not priority(exp[x]):
             exp[x] = DItems[exp[x]]
    return exp
 
# TODO : def is_valid():pass          

def operation(x,y,o):
    x,y = int(x),int(y)
    
    if o in DisO  : return 1 if x or y else 0
    if o in ConO  : return 1 if x and y else 0
    
    if o in NDisO : return 1 if not x and not y else 0
    if o in NConO : return 0 if x and y else 1
    
    if o in XorO  : return 1 if x^y else 0
    if o in EqO   : return 1 if x==y else 0
    return None

# this function take the result of replace function and calculate it ex : BCalc("1 + 0") -> 1 ex2 : Bcalc( replace( postfix(exp) , DictOfVarsValues ) )
def BCalc(op):
    stack=[None]
    for x in op:
        if is_int(x):
            stack.insert(0,x)
            
        elif x in NegO: #negation
            stack.insert(0,1 if int(stack[0]) == 0 else 0)
            stack.pop(1)
            
        else :
            stack.insert(0,operation(stack[1],stack[0],x))
            stack.pop(1)
            stack.pop(1)

    return stack[0]          
              
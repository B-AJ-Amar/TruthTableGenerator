# is_operator :(0/not 0)
def priority(x):
    if x =='!':   return 5 # ¬ 
    if x in ['⨁','⊕','^']:   return 4
    if x in [".","*",'↑','/'] : return 3
    if x in ["+","↓",'-']:  return 2
    if x =='=':   return 1
    if x in ["(",")"]:  return -1
    return 0 

def is_int(x):
    try:x+=1
    except TypeError:  return False
    return True

def operation(x,y,o):
    x,y = int(x),int(y)
    
    if o in ['+'] : return 1 if x or y else 0
    if o in ["."]  : return 1 if x and y else 0
    
    if o in ["↓",'-'] : return 1 if not x and not y else 0
    if o in ['↑','/'] : return 0 if x and y else 1
    
    if o in ['⨁','⊕','^'] : return 1 if x^y else 0
    if o=='=' : return 1 if x==y else 0
    return None

def replace(exp,DItems):
    for x in range(len(exp)):
         if not priority(exp[x]):
             exp[x] = DItems[exp[x]]
    return exp
 
# def is_valid():pass          

def postfix(op):
    stack = [None]
    new   = []
    
    for x in op:
        if x ==' ':continue
        if not priority(x): 
            new.append(x)
        else:
            
            if x=='!' or len(stack)==1 or stack[0]=='(' or x=='(' or priority(x)>priority(stack[0]) :
                if stack[0]=='!' and x not in'!(':
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
   
def BCalc(op):
    stack=[None]
    for x in op:
        if is_int(x):
            stack.insert(0,x)
            
        elif x== "!": #negation
            stack.insert(0,1 if int(stack[0]) == 0 else 0)
            stack.pop(1)
            
        else :
            stack.insert(0,operation(stack[1],stack[0],x))
            stack.pop(1)
            stack.pop(1)

    return stack[0]          
              
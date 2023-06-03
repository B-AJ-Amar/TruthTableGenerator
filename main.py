from b_in_to_po import *
import os

# ?? you can write more than one expresion fin the same time by use delemeter ";" .
# ?? ex : a + b ; x . !z + p ; z = a

# TODO : 
    #* solve nand ↑ and nor ↓ problem
    #* make id_valid function
    #* op Lvars

class TT:
    def __init__(self,Ex:str):
        
        #This function takes a string as input For example: Ex = "a+b;b.c".
        
        # In this section, we split the expressions and store them in a list called self.Exs.
        # The resulting list will be: self.Exs = ["a+b", "b.c"].
        self.Exs=Ex.split(';')
        self.ELen = len(self.Exs)  # number of exepresions  
        
        
        # The expressions in self.Exs are converted from infix to postfix notation and stored in self.ExsP.
        # For example:self.Exs = ["a+b", "b+c"] => self.ExsP = ["ab+", "bc+"]
        self.ExsP = [postfix(x) for x in self.Exs]
        
        
        # Next, we extract the variables from the expressions and store them in a list called self.Items.
        # For example, considering the previous example:self.ExsP = ["ab+", "bc+"] => self.Items = ["a", "b", "c"]
        self.Items,self.ILen = [],0
        for y in self.ExsP:
            for x in y:
                if x  not in self.Items and not  priority(x):
                    self.Items.append(x)
                    self.ILen += 1
        self.Items.sort() # sort the variables (optional)
        
        
        
        
        # Creat The Table----------------------------------------------------------------------------
        
        
        # The next step involves creating the table and computing the results.

        # size : y = 2^variables + 1 
        #        x = variables + results. in this case : vars = 3 (a,b,c) , results = 2 (a+b and b.c). total = 5
        self.TX,self.TY=self.ELen+self.ILen,pow(2,self.ILen)+1
        
        self.Table = [[0 for _ in range( self.TX)] for _ in range(self.TY)] # creat empty table
        
        
        # header [a , b , c , R1 , R2]
        for x in  range(self.ILen):
            self.Table[0][x] = self.Items[x] 
            
        for x in  range(self.ILen,self.TX):
            self.Table[0][x] = f"R{x-self.ILen+1}"

            
        # 000 ,001 ,011 ... 
        for x in range(self.ILen):
            tmp,tcount = 0,pow(2,x)
            count = tcount
        
            for y in range(0,pow(2,self.ILen)) :
                if not count : 
                    count = tcount
                    tmp = (tmp+1)%2
                self.Table[y+1][x] = tmp 
                count -=1
        
        # calculate 
        self.calc()
        
               
    def calc(self):
        for x in range(self.ELen):
            for y in range(1,self.TY):
                self.Table[y][self.ILen+x] = BCalc(  replace( self.ExsP[x].copy(),dict(zip(self.Items, self.Table[y][0:self.ILen])))  ) 

    def PrintInfo(self):print(f"expresions : {self.Exs}\npostfix form : {self.ExsP}\n{self.ILen} variables : {self.Items}\n\n")
    
    def PrintT(self):      
        for x in range(self.ELen):
            print(f"R{x+1} : {self.Exs[x]}")
        print()
        for xx in range(self.TX):
                if xx==self.ILen:print("||",end="")
                print("| ",self.Table[0][xx]," ",sep='',end='')
        print("|\n")
        for x in range(1,self.TY):
            for xx in range(self.TX):
                if xx==self.ILen:print("||",end="")
                clr = "\33[92m" if self.Table[x][xx] and xx>=self.ILen  else '\33[0m'# '\33[31m' if xx>=self.ILen else '\33[0m'
                print(f"| {clr}",self.Table[x][xx],"\33[0m ",sep='',end='')
                if xx>=self.ILen and x>0  : 
                    print(" ",end='')
            print("|")
               

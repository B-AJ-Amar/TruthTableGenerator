from main import *

use =1
while use :
    os.system("cls")
    t1 = TT(input("write a boolean expresions : ")) 
    # t1.PrintInfo()
    t1.PrintT()
    use = 1 if input("do you want to reuse (y/n)? ").lower() in ["1",'y','yes'] else 0
                
#  -------- Pattern Printing -------------

for i in range(5):
    for j in range(5):
        print("*",end='')
    print()  
'''output :
*****
***** 
***** 
***** 
*****  ''' 

for i in range(5):
    for j in range(5):
        if j <= i :
            print("*",end='')
        else:
            print(" ",end='')
    print()
'''output:
*
**
***
****
*****'''

for i in range(1,6):
    for j in range(1,6):
        if j>=i:
            print("*",end='')
        else:
            print(" ",end='')
    print()
'''output:
*****
 ****
  ***
   **
    * '''

for i in range(1,6):
    for j in range(1,6):
        if j <= 6-i:
            print("*",end='')
        else:
            print(" ",end='')
    print()
'''output:
*****
****
***
**
*'''

for i in range(1,6):
    for j in range(1,6):
        if j >= 6-i:
            print("*",end='')
        else:
            print(" ",end='')
    print()
'''output:
      
    *
   **
  ***
 ****
*****'''

def fun1():
    print("Hello")
    # fun1()
fun1()
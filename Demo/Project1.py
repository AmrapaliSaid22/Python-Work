# ----- Transaction Process -----

pin = 2122

balance = 10000
c = 0

while c != 3:
    c = c + 1
    a = int(input("Enter Your Pin :"))
    
    if pin == a :
        amount = int(input("Enter Amount :"))
        
        if balance >= amount :
            print("Transaction Successful")
            print("Your Balnace is :", balance - amount)
        
        else :
            print("Insufficent Balance")
            print("Your Balnace is :", balance)
        
        break
    else :
        print("Incorrect Pin:")

else :
    print("Card Blocked ....")
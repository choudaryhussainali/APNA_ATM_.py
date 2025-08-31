def deposit(total_money,deposit_money):
    total = total_money+deposit_money
    return total

def withdraw(curr_balance,withdraw_bal):
    total = curr_balance-withdraw_bal
    return total

current_balance = 100000

print("HEY! \n Welcome to APNA ATM")
print("Are you here for any assistance today?")
print("1-  Yes\n2-  No")
reaction = input("Enter Your Choice \'1\' OR \'2\' :")


if (reaction=="1"):
    print("How can i assist you Today.")
    print("1-  Deposit\n2-  Withdraw\n3-  Account Statement")
    choice = input("Enter Your Choice \'1\' OR \'2\' OR \'3\':")
    if choice=="1":
        deposit_amount = int(input("Enter the Amount you wanna Deposit : "))
        total = deposit(current_balance,deposit_amount)
        current_balance = total
        print("....DEPOSIT SUCCESSFUL")
        print("Your Total Balance After deposit is {} : ".format(current_balance))
        print("Thanks for your Good Time \n \t HAVE A NICE DAY")

    elif choice =="2":
        print("Your Current balance is {} ".format(current_balance))
        amount = int(input("Enter the Ampunt you wannna to withdraw : "))
        after_with = withdraw(current_balance,amount)
        current_balance = after_with
        print("....WITHDRAW SUCCESSFUL")
        print("Your Total Balance After Withdraw is {} : ".format(current_balance))
        print("Thanks for your Good Time \n \t HAVE A NICE DAY")

    elif choice =="3":
        print("Your Current balance is {} ".format(current_balance))
        print("Thanks for your Good Time \n \t HAVE A NICE DAY")


    else:
        print("Enter A valid CHOICE")
        print("Thanks for your Good Time \n \t HAVE A NICE DAY")



else:
    print("Thanks for your Good Time \n \t HAVE A NICE DAY")
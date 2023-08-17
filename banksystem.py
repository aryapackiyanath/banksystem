def make_transaction(checking_account, saving_account):
    print("current checking balance:", checking_account)
    print("current saving balance:", saving_account)
    transaction = input("would you like to withdraw or deposit money:")
    if transaction == "deposit":
        amount_deposited = float(input("how much would you like to deposit:"))
        depost_location = input("where would you like to deposit:")
        if depost_location == "savings":
            saving_account += amount_deposited
            print("checking account balance is:", checking_account, "saving account balance is", saving_account)
            return checking_account, saving_account
        elif depost_location == "checking":
            checking_account += amount_deposited
            print("checking account balance is:", checking_account, "saving account balance is", saving_account)
            return checking_account,saving_account
        else:
            print("Invalid deposit location. Please choose 'checking' or 'saving'.")
            return checking_account,saving_account
    print("checking account balance is:", checking_account, "saving account balance is", saving_account)
    if transaction == "withdraw":
        withdrawal_amount = float(input('how much would you like to withdraw:'))
        withdrawal_location = input("where would you like to withdraw money:")
        if withdrawal_amount > saving_account and withdrawal_location == "savings":
            print("insufficent funds")
            return checking_account, saving_account
        if withdrawal_amount > checking_account and withdrawal_location == "checking":
            print("insufficent funds")
            checking_account -= withdrawal_amount
        else:
            print("Invalid withdrawal location. Please choose 'checking' or 'saving'.")
        print("checking account balance is:", checking_account, "saving account balance is", saving_account)
        return checking_account,saving_account

def main():
    checking_account = float(input('current checking balance:'))
    saving_account = float(input("current savings balance:"))
    print("welcome to this banking system")
    while True:
        checking_account, saving_account = make_transaction(checking_account, saving_account)

        play_again = input("do you want to make another withdrawal yes/no:")
        if play_again.lower() == "no":
            print("checking:",checking_account,"savings:",saving_account)
            print("thanks for using this bank")
            break
if __name__ == "__main__":
    main()
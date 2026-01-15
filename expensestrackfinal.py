
# finance management tool

# paramter included : type of expense, date, total spending, totL SAVINGS,

print('MY EXPENSES TRACKER')
name=input('ENTER YOUR NAME : ')
print(f'Hey ! {name}, welcome lets get started with your expenses tracker')

# to calculate savings we need our budget/revenue
budget=int(input('ENTER YOUR TOTAL BUDGET(IN RS) FOE ONE DAY :  '))

expenses={} # dictionary of dates created to retrieve the information
#category of my expenses
category = ['FEES', 'SHOPPING', 'FOOD', 'ENTERTAINMENT', 'GROCERY']
payment_method = ['CASH','UPI','CARD']
while True:
    print('-----------------MENU--------------------')
    print('1.Add expenses')
    print('2.View expense')
    print('3.EXIT')
    choice = int(input('Enter your choice from above menu : '))

    if choice == 1:
            spend=0 # tracks total spending at lastspend = 0
            # Date  loop
            while True:
                date = input('Enter the date [DD/MM/YY]: ')
                if len(date) == 8 and date[2] == '/' and date[5] == '/':
                    break
                else:
                    print(" Invalid date format! Use DD/MM/YY")

            if date not in expenses:
                expenses[date] = {'details' : {} , 'spent':0 ,'saving':0}
            #so that if category is skippped so ytab bhi category se key use ho jaye
            else:
                print('DATA FOR THE ENTERED DATE IS ALREADY UPDATED.')

            for item in category:
                ch = input(f"Do you want to add expense for {item}? (yes/no): ")
                if ch.lower() == 'yes':
                    exp = int(input(f"TOTAL EXPENSE ON {item}: "))
                    spend += exp

                    print("Select payment method:")
                    for i, p in enumerate(payment_method, start=1):
                        print(f"{i}. {p}")

                    pm_choice = int(input("Enter choice (1-3): "))
                    payment = payment_method[pm_choice - 1]

                    expenses[date]['details'][item] = {
                        'amount': exp,
                        'payment': payment
                    }
            print(f'THE TOTAL SPENDING ON {date} is {spend} RS ')
            sav=budget-spend
            expenses[date]['saving']=sav
            expenses[date]['spent']=spend #  key usage
            if(sav>0):
                print(f'THE TOTAL SAVINGS ON {date} is {sav} RS')
            elif(sav<0):
                print("⚠ You exceeded your budget!")
            else:
                print('No savings are made today.')


    elif choice == 2:
            date1=input('ENTER THE DATE FOR WHICH EXPENSE NEED TO BE VIEWED : ')# date  data to be viewed

            category = ['FEES', 'SHOPPING', 'FOOD', 'ENTERTAINMENT', 'GROCERY']

            if date1 in expenses:
                 print(f'YOUR TOTAL EXPENSES on {date1} are  : ')
                 for cat, info in expenses[date1]['details'].items():
                     print(f"{cat}: Rs {info['amount']} | Payment: {info['payment']}")

                 print(f"Total Spent: Rs {expenses[date1]['spent']}")
                 print(f"Savings: Rs {expenses[date1]['saving']}")
            else:
                 print('Data for given date is not been updated . !!')
    else:
        print('THANK YOU FOR USING OUR SERVICE')
        break






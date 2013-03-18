pin = '1234'
balance = 100.00

attempt = raw_input("Enter your PIN: ")

if attempt == pin:
    print "Correct"
else:
    print "Incorrect"

### 1. Give them 3 attempts at entering their PIN
'''
    Think - if you just copied the block of code 3 times, what if the
    number of attempts was 100 - would you still copy and paste?

    Try something smart like a loop
'''
### 2. Make it say their card is locked if they get it wrong 3 times

### 3. Make it display their balance when they log in correctly

### 4. Ask how much money they want to take out

### 5. If the amount they enter is not divisible by £10, give an error

### 6. If they do not have enough money, give them an error
'''
    Think - what information should you tell them?
'''

### 7. Change the number of attempts allowed to 5
'''
    Think - how easy was it for you to do this?
    If you had the number of attempts in more than one place, how could you
    have stored it in once place to make this easier to change?
'''

### 8. Make it so they can withdraw cash, then enter their PIN again and
### see their new balance
'''
    Note - this will not work if you restart the python script - you will have
    to ask them again after their withdrawal
'''

### 9. Store a number of bank customers with different PINs and balances
'''
    Think of a way to store many customers with a PIN number and balance
    and be able to look each one up by an ID number
'''

### 10. Some customers are allowed an overdraft, as specified in their account
'''
    An overdraft is an agreement with the bank allowing the customer to
    go down to a balance below 0

    If a customer has an overdraft of £100.00 they can have a balance of -900
    and still be allowed to withdraw another £100.00

    Think of a way to store each customer's overdraft limit and make the
    withdrawal amount reflect this
'''

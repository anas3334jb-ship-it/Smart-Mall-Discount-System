'''this is the senerio of Mall in which you will get dicount if you do shopping
at least 5000 or more and if you pay with card then discount will apply otherwise 
it will not apply in any situation'''
Amount = int(input('Enter the Amount:'))
if Amount >= 5000 :
    pay_method = input('Enter your payment Method(card or cash):') 
    if pay_method == 'card':
        print('Eligible for Discount')
    elif pay_method == 'cash':
        print('Not Eligible for Discount')
    else:
        print('Select Payment Method')
elif Amount < 5000 and Amount > 0:
    print('Not Eligible')
elif Amount == 0 :
    print('Please Do Shopping')
else:
    print('Invalid')

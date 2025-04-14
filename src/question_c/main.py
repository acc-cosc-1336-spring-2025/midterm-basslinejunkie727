#add import
def get_bonus_pay_amount(sales):
    if sales<0 or sales>1999:
        return 'invalid arguments'
    elif sales <=499:
        return sales*0.05
    elif sales <=999:
        return sales*0.06
    elif sales <=1499:
        return sales*0.07
    else:
        return sales*0.08
    
def main():
    while True:
        user_input=input('enter sales amount or enter q to quit')
        if user_input.lower()=='q':
            print('goodbye')
            break
        try:
            sales=float(user_input)
            results=get_bonus_pay_amount(sales)
            print(f'bonus pay amount {results}')
        except ValueError:
            print('please enter a valid number')


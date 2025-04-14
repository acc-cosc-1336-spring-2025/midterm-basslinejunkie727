#add import
def get_assessment_value(value):
    return value*0.6

def get_tax_assessed(assessment_value):
    return (assessment_value/100)*0.72

def main():
    while True:
        user_input=input('enter the actual value of the property or enter q to quit')
        if user_input.lower()=='q':
            print('goodbye')
            break
        try:
            actual_value=float(user_input)
            if actual_value<0:
                print('please enter a non negative number')
                continue
            assessment_value=get_assessment_value(value)
            tax=get_tax_assessed(assment_value)
            print(f'assessment value is {assessment_value:,.2f}')
            print(f'property tax is {tax:,.2f}')
        except ValueError:
            print('invalid input')
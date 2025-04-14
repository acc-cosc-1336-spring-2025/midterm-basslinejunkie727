#add import
def get_person_category(age):
    if age<0 or age>125:
        return 'invalid number'
    elif age <=1:
        return 'infant'
    elif age <13:
        return 'child'
    elif age <20:
        return 'teenager'
    else:
        return 'adult'
    
def main():
    while true:
        user_input=input('enter a persons age or q to quit')
        if user_input.lower()=='q':
            print('goodbye')
            break
        try:
            age=int(user_input)
            category=get_person_category(age)
            print(f'Category is {category}')
        except ValueError:
            print('please enter a valid number')
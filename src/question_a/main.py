#add import
def get_sum_of_evens(num):
    total=0
    for x in range(2,num+1,2):
        total+=x
        return total

def main():
    while True:
        user_input=input('enter a number to sum even numbers up to (or enter q to quit)')
        if user_input.lower()=='q':
            print('goodbye')
            break
        try:
            num= int(user_input)
            if num<2:
                print('please enter a number greater than or equal to 2')
                continue
            total= get_sum_of_evens(num)
            print(f'the sum of even numbers up to {num} is {total}')
        except ValueError:
            print('please enter a valid number')
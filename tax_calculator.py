
def check_income(income):
    if income < 0:
        MyError = ValueError("Sorry {}, taxable income should be positive".format(name_of_person))
        raise MyError


def tax_calculator():
    if income == 0:
        annual_tax = 0.0
    elif income < 100000:
        annual_tax = 0.1534 * income
    elif 100000 <= income < 1000000:
        annual_tax = 0.2 * income
    elif 1000000 <= income < 5000000:
        annual_tax = 0.2545 * income
    elif income >= 5000000:
        annual_tax = 0.275 * income
    monthly_tax = annual_tax / 12         
    print("Hi {}, your annual tax is ${:0.2f}".format(name_of_person, annual_tax))
    print("Hi {}, your monthly tax is ${:0.2f}".format(name_of_person, monthly_tax))


if __name__ == '__main__':
    name_of_person = input("Please put down your name: ").title()
    while True:
        try:
            income = float(input("Please enter your taxable income: "))
            check_income(income)
            break
        except ValueError:
            print("Sorry {}, I didn't understand that please enter taxable income as a number".format(name_of_person))
            continue
    
    
    tax_calculator()


       

       
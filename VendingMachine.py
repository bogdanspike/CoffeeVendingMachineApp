from Recipe import MENU, resources


def VendingMachine():
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    wallet = 0
    status = True
    profit = 0
    while status:
        choice = input('What would you like? (espresso/latte/cappuccino):')
        if choice in MENU.keys():
            for x in (MENU[choice]['ingredients'].keys()):
                if resources[x] < MENU[choice]['ingredients'][x]:
                    print(f'Sorry there is not enough {x}')
                    break
                else:
                    print(f'Insert {MENU[choice]["cost"]}$')
                    q = int(input('Quarter:'))
                    d = int(input('Dime:'))
                    n = int(input('Nickel:'))
                    p = int(input('Penny:'))
                    profit += float(q * quarters + d * dimes + n * nickles + p * pennies)
                    print(float(profit))
                    if profit >= MENU[choice]['cost']:
                        wallet += MENU[choice]['cost']
                        profit -= MENU[choice]['cost']
                        print(f'Here is {profit}$ in change.')
                        profit = 0

                        resources[x] -= MENU[choice]['ingredients'][x]
                        print(f'Here is your {choice}. Enjoy!')
                        break
                    else:
                        print('Sorry that is not enough money. Money refunded.')
        elif choice == 'off':
            status = False
        elif choice == 'report':
            print(f'water: {resources["water"]}')
            print(f'milk: {resources["milk"]}')
            print(f'coffee: {resources["coffee"]}')
            print(f'money: {wallet}$')
        else:
            print('Wrong input')


if __name__ == '__main__':
    VendingMachine()

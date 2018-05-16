from account import Account
from stock import Stock
from stock_exchange import Stock_exchange

class Menu:
    # Display a menu and respond to choices when run.

    def display_menu():
        print("""
        Stock Simulation Menu   
        1. start() - initiate game
        2. update_date() - move to next trading day, carry out orders
        3. inject_capital(amount) - inject capital
        4. display_wealth() - show the stocks and money you have
        5. buy_stock(ticker, price, volume) - enter the stock, price, and unit you want to buy
        6. sell_stock(ticker, price, volume) - enter the stock, price, and unit you want to sell
        7. show_buy_orders() - show buy orders you have for this round
        8. show_sell_orders() - show sell orders you have for this round
        9. end_game() - end the game immediately, liquidate all positions at close price
        """)

    def start(): # set the first date in the simulation game as first date
        Stock.start_date()
        Account.stocks_dictionary()
        Stock_exchange.update_price()
        print("The stock simulation game start date is", Stock.date)

    def update_date(): # run all the transactions and move the date to the next day where stock exchange is opened
        Stock_exchange.update_price()
        Stock_exchange.stock_transaction()
        Stock.update_date()
        Account.temporary_balance = Account.balance
        print("The current date is", Stock.date)


    def inject_capital(amount=0):
        Menu.injected_capital = amount
        print('$',  str(Menu.injected_capital), 'has been injected')
        Account.inject_capital(Menu.injected_capital, Stock.date)

    def display_wealth():
        print('You have an amount of $', Account.balance)
        print('You have the following stocks', Account.stocks)


    def buy_stock(ticker, price, volume):
        if Account.buy_list == {}:
            Account.temporary_balance = Account.balance
        order_size = price * volume
        if price * volume > Account.temporary_balance:
            print('Your account do not have enough money!')
        else:
            Account.buy_stock(ticker, price, volume)
            Account.temporary_balance -= order_size

    def sell_stock(ticker, price, volume):
        try:
            Account.sell_stock(ticker, price, volume)
        except KeyError:
            print('You do not have that stock to sell')

    def show_buy_orders():
        print(Account.buy_list)

    def show_sell_orders():
        print(Account.sell_list)

    def end_game():
        Stock_exchange.liquidate_position()
        total_injected_capital = Account.cumulative_capital
        print('Your final balance is', '$', round(Account.balance))
        Account.balance -= total_injected_capital
        profit_percentage = Account.balance/total_injected_capital * 100
        print('You have achieved a return of ', round(profit_percentage, 2), ' %')



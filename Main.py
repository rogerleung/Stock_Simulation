from menu import Menu
from account import Account
from stock import Stock
from google_api import price_last_52_week
from stock_exchange import Stock_exchange

print("Welcome to the Stock simulation game") # define start_date, start capital and input stocks
Menu.display_menu()
Menu.start()
Menu.inject_capital(5000000)
Menu.buy_stock('AAPL', 170, 5000)
Menu.buy_stock('AAPL', 170, 500000)
Menu.buy_stock('GOOGL', 300, 50)
Menu.buy_stock('GOOGL', 1050, 50)
Menu.sell_stock('GOOGL', 1050, 50)
Menu.update_date()
print('moved to next day!')
Menu.display_wealth()
Menu.sell_stock('GOOGL', 500, 20)
Menu.update_date()
print('moved to next day!')
print(Stock_exchange.orders)
Menu.display_wealth()
print('moved to next day!')
Menu.display_wealth()
Menu.end_game()


class Account:
    balance = 0
    injected_capital = []
    buy_list = []
    sell_list = []
    profit = 0
    cumulative_capital = 0

    def inject_capital(capital, date):
        amount = {}
        amount[date] = capital
        Account.cumulative_capital += capital
        Account.temporary_balance = 0
        Account.injected_capital += [amount]
        Account.balance += capital
        Account.temporary_balance += capital

    def stocks_dictionary():
        Account.stocks = {}

    def buy_stock(ticker, price, volume):
        order = (price, volume, "buy")
        buy_order = {}
        buy_order[ticker] = order
        Account.buy_list += [buy_order]
        print('An order of buying ' +
              str(volume) +
              ' units of ' +
              str(ticker) +
              ' @' +
              ' $' +
              str(price) +
              ' has been received')

    def sell_stock(ticker, price, volume):

        total_sell_order_unit = 0

        for i in range(len(Account.sell_list)):  # return the amount of sell order placed in this round
            try:
                total_sell_order_unit += Account.sell_list[i][ticker][1]
            except KeyError:
                continue
        if (volume + total_sell_order_unit) > Account.stocks[ticker]:
            print('You do not have enough stock to sell')

        else:
            order = (price, volume, "sell")
            sell_order = {}
            sell_order[ticker] = order
            Account.sell_list += [sell_order]
            print('An order of selling ' +
                  str(volume) +
                  ' units of ' +
                  str(ticker) +
                  ' @' +
                  ' $' +
                  str(price) +
                  ' has been received')


from account import Account
from stock import Stock


class Stock_exchange:
    def update_price():
        Stock_exchange.stock_list = []
        Stock_exchange.stock_list_unique = []  # this list as unique stock list for transaction
        Stock_exchange.stock_market_price = {}
        Stock_exchange.temporary_stock_list = []  # store stock list
        Stock_exchange.orders = Account.buy_list + Account.sell_list
        for i in range(len(Stock_exchange.orders)):
            Stock_exchange.temporary_stock_list.append(list(Stock_exchange.orders[i].keys()))
        for i in range(len(Stock_exchange.temporary_stock_list)):
            if Stock_exchange.temporary_stock_list[i] not in Stock_exchange.stock_list:
                Stock_exchange.stock_list.append(Stock_exchange.temporary_stock_list[i])
        for i in range(len(Stock_exchange.stock_list)):
            Stock_exchange.stock_list_unique.append(Stock_exchange.stock_list[i][0])

    def stock_transaction():
        Stock_exchange.untransacted_buy_order = []
        Stock_exchange.untransacted_sell_order = []
        for i in range(len(Stock_exchange.stock_list_unique)):
            for j in range(len(Stock_exchange.orders)):
                try:
                    if Stock_exchange.orders[j][Stock_exchange.stock_list_unique[i]][2] == 'buy':

                        if Stock_exchange.orders[j][Stock_exchange.stock_list_unique[i]][0] \
                                >= Stock.generate_stock_latest_day_low_price(Stock_exchange.stock_list_unique[i]):
                            try:
                                Account.stocks[Stock_exchange.stock_list_unique[i]]
                            except KeyError:
                                Account.stocks[Stock_exchange.stock_list_unique[i]] = 0
                            Account.stocks[Stock_exchange.stock_list_unique[i]] += \
                                Stock_exchange.orders[j][Stock_exchange.stock_list_unique[i]][1]
                            if Stock_exchange.orders[j][Stock_exchange.stock_list_unique[i]][0] \
                                    >= Stock.generate_stock_latest_day_high_price(Stock_exchange.stock_list_unique[i]):
                                Account.balance -= Stock.generate_stock_latest_day_high_price(
                                    Stock_exchange.stock_list_unique[i]) * \
                                                   Stock_exchange.orders[j][Stock_exchange.stock_list_unique[i]][1]
                            else:
                                Account.balance -= Stock_exchange.orders[j][Stock_exchange.stock_list_unique[i]][0] * \
                                                   Stock_exchange.orders[j][Stock_exchange.stock_list_unique[i]][1]
                        else:
                            Stock_exchange.untransacted_buy_order.append(
                                Stock_exchange.orders[j])

                    elif Stock_exchange.orders[j][Stock_exchange.stock_list_unique[i]][2] == 'sell':

                        if Stock_exchange.orders[j][Stock_exchange.stock_list_unique[i]][0] \
                                <= Stock.generate_stock_latest_day_high_price(Stock_exchange.stock_list_unique[i]):

                            Account.stocks[Stock_exchange.stock_list_unique[i]] -= \
                                Stock_exchange.orders[j][Stock_exchange.stock_list_unique[i]][1]
                            if Stock_exchange.orders[j][Stock_exchange.stock_list_unique[i]][0] \
                                    <= Stock.generate_stock_latest_day_low_price(Stock_exchange.stock_list_unique[i]):

                                Account.balance += Stock.generate_stock_latest_day_low_price(
                                    Stock_exchange.stock_list_unique[i]) * \
                                                   Stock_exchange.orders[j][Stock_exchange.stock_list_unique[i]][1]
                            else:
                                Account.balance += Stock_exchange.orders[j][Stock_exchange.stock_list_unique[i]][0] * \
                                                   Stock_exchange.orders[j][Stock_exchange.stock_list_unique[i]][1]

                        else:
                            Stock_exchange.untransacted_sell_order.append(
                                Stock_exchange.orders[j])

                except KeyError:
                    continue
        Account.buy_list = Stock_exchange.untransacted_buy_order
        Account.sell_list = Stock_exchange.untransacted_sell_order

    def liquidate_position():  # we will use close price to liquidate position
        Account.buy_list = []
        Account.sell_list = []
        Stock_exchange.proceedings = 0
        for i in Account.stocks:
            value = Stock.generate_stock_latest_day_closed_price(i) * Account.stocks[i]
            Stock_exchange.proceedings += value
        Account.balance += Stock_exchange.proceedings

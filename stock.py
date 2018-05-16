from google_api import price_last_52_week


class Stock:
    def generate_date_list():
        ticker = 'AAPL'  # Generate with a random stock
        Stock.stock_data_list = price_last_52_week(ticker).reset_index().values.tolist()
        Stock.date_list = []
        for i in range(len(Stock.stock_data_list)):
            Stock.date_list.append(str(Stock.stock_data_list[i][0])[:11])

    def start_date():
        Stock.generate_date_list()
        Stock.number_of_date = 0
        Stock.start_date = Stock.date_list[Stock.number_of_date]
        Stock.date = Stock.date_list[Stock.number_of_date]
        return (Stock.date)

    def update_date():
        Stock.number_of_date += 1
        Stock.date = Stock.date_list[Stock.number_of_date]
        return (Stock.date)

    def generate_stock_latest_day_low_price(ticker):
        ticker_info = price_last_52_week(ticker).reset_index().values.tolist()
        for i in range(len(Stock.date_list)):
            if str(Stock.date_list[i]) == Stock.date:
                return ticker_info[i][3]  # the third number in the google finance data is low price

    def generate_stock_latest_day_high_price(ticker):
        ticker_info = price_last_52_week(ticker).reset_index().values.tolist()
        for i in range(len(Stock.date_list)):
            if str(Stock.date_list[i]) == Stock.date:
                return ticker_info[i][2]  # the second number in the google finance data is high price

    def generate_stock_latest_day_closed_price(ticker):
        ticker_info = price_last_52_week(ticker).reset_index().values.tolist()
        for i in range(len(Stock.date_list)):
            if str(Stock.date_list[i]) == Stock.date:
                return ticker_info[i][4]  # the forth number in the google finance data is close price


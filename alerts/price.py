import os
import json

from configparser import ConfigParser
from .utils.rest_query import RestQuery


class Price:

    def __init__(self):
        cwd = os.getcwd()
        self.alerts_path = os.path.join(cwd, 'alerts')
        self.config_parser = ConfigParser()
        self.config_parser.read(os.path.join(self.alerts_path, 'alerts.ini'))

    def run(self, ticker):
        url = 'https://api.iextrading.com/1.0/stock/{ticker}/delayed-quote'.format(ticker=ticker)
        quote = json.loads(RestQuery.query(url))
        alert_price = float(self.config_parser.get(ticker, 'price'))
        passed = False

        if quote['delayedPrice'] <= alert_price or quote['high'] <= alert_price or quote['low'] <= alert_price:
            passed = True
        message = '{ticker} Expected Price is ${alert_price}, C: ${current_price}.' \
                  ' H: ${high}, L: ${low}'.format(ticker=ticker, alert_price=alert_price,
                                                  current_price=quote['delayedPrice'],
                                                  high=quote['high'], low=quote['low'])
        return {'pass': passed, 'message': message}
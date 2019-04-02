import json

from .utils.guru_focus import GuruFocus
from .utils.rest_query import RestQuery


class PeterLynchValue:

    def run(self, ticker):
        peter_lynch_value = GuruFocus.peter_lynch_value(ticker)
        url = 'https://api.iextrading.com/1.0/stock/{ticker}/delayed-quote'.format(ticker=ticker)
        quote = json.loads(RestQuery.query(url))
        passed = False
        if quote['delayedPrice'] <= peter_lynch_value or quote['high'] <= peter_lynch_value \
                or quote['low'] <= peter_lynch_value:
            passed = True
        message = '{ticker}: Peter Lynch Value is ${peter_lynch_value}, C: ${current_price}.' \
                  ' H: ${high}, L: ${low}'.format(ticker=ticker, peter_lynch_value=peter_lynch_value,
                                                        current_price=quote['delayedPrice'],
                                                        high=quote['high'], low=quote['low'])
        return {'pass': passed, 'message': message}

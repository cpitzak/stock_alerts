import json

from .utils.guru_focus import GuruFocus
from .utils.rest_query import RestQuery


class GrahamNumber:

    def run(self, ticker):
        graham_number = GuruFocus.graham_number(ticker)
        url = 'https://api.iextrading.com/1.0/stock/{ticker}/delayed-quote'.format(ticker=ticker)
        quote = json.loads(RestQuery.query(url))
        passed = False
        if quote['delayedPrice'] <= graham_number or quote['high'] <= graham_number or quote['low'] <= graham_number:
            passed = True
        message = '{ticker} Graham Number is ${graham_number}, C: ${current_price}.' \
                  ' H: ${high}, L: ${low}'.format(ticker=ticker, graham_number=graham_number,
                                                        current_price=quote['delayedPrice'],
                                                        high=quote['high'], low=quote['low'])
        return {'pass': passed, 'message': message}

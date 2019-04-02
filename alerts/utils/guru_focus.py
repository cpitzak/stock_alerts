import re

from .rest_query import RestQuery
from bs4 import BeautifulSoup


class GuruFocus:

    @staticmethod
    def graham_number(ticker):
        url = 'https://www.gurufocus.com/term/grahamnumber/{ticker}/Graham%2BNumber/{ticker}'.format(ticker=ticker)
        content = RestQuery.query(url)
        soup = BeautifulSoup(content, 'html.parser')
        metatags = soup.find_all('meta', attrs={'name': 'description'})
        str_dollar_list = re.findall(r"(?:[\$]{1}[,\d]+.?\d*)", metatags[0]['content'])
        graham_number = None
        if len(str_dollar_list) == 1:
            graham_number = float(str_dollar_list[0][1:])
        return graham_number

    @staticmethod
    def pe_ratio(url):
        content = RestQuery.query(url)
        soup = BeautifulSoup(content, 'html.parser')
        metatags = soup.find_all('meta', attrs={'name': 'description'})
        pe_ratio_list = re.findall(r"PE Ratio: ([\d]+.?\d*)", metatags[0]['content'])
        pe_ratio = None
        if len(pe_ratio_list) == 1:
            pe_ratio = float(pe_ratio_list[0])
        return pe_ratio

    @staticmethod
    def peter_lynch_value(ticker):
        url = 'https://www.gurufocus.com/term/lynchvalue/{ticker}/Peter%2BLynch%2BFair%2BValue/{ticker}'\
            .format(ticker=ticker)
        content = RestQuery.query(url)
        soup = BeautifulSoup(content, 'html.parser')
        metatags = soup.find_all('meta', attrs={'name': 'description'})
        str_dollar_list = re.findall(r"(?:[\$]{1}[,\d]+.?\d*)", metatags[0]['content'])
        peter_lynch_value = None
        if len(str_dollar_list) == 1:
            peter_lynch_value = float(str_dollar_list[0][1:])
        return peter_lynch_value
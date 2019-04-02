import os

from .utils.guru_focus import GuruFocus
from configparser import ConfigParser


class PeRatio:

    def __init__(self):
        cwd = os.getcwd()
        self.alerts_path = os.path.join(cwd, 'alerts')
        self.config_parser = ConfigParser()
        self.config_parser.read(os.path.join(self.alerts_path, 'alerts.ini'))

    def run(self, ticker):
        pe_ratio = GuruFocus.pe_ratio(self.config_parser.get(ticker, 'pe_ratio_url'))
        alert_pe_ratio = float(self.config_parser.get(ticker, 'pe_ratio'))
        passed = False
        if pe_ratio < alert_pe_ratio:
            passed = True
        return {'pass': passed, 'message': '{ticker}: P/E ratio {pe_ratio}, expected P/E: {alert_pe_ratio}'
            .format(ticker=ticker, pe_ratio=pe_ratio, alert_pe_ratio=alert_pe_ratio)}
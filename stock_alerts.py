import os
import sys
import logging

from configparser import ConfigParser


class StockAlerts:

    def __init__(self):
        cwd = os.getcwd()
        self.alerts_path = os.path.join(cwd, 'alerts')
        self.config_parser = ConfigParser()
        self.config_parser.read(os.path.join(self.alerts_path, 'alerts.ini'))
        self.alerts = {}
        self.logger = logging.getLogger()
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(levelname)-2s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def create_alerts(self):
        files = []
        for f in os.listdir(self.alerts_path):
            if os.path.isfile(os.path.join(self.alerts_path, f)) and f.endswith('.py') and not f.startswith('_'):
                files.append(f)

        for file in files:
            file_name = os.path.splitext(file)[0]
            file_name_path = 'alerts.{file}'.format(file=file_name)
            class_name = file_name.replace('_', ' ').title().replace(' ', '')

            if file_name not in self.alerts:
                __import__(file_name_path)
                Alert = getattr(sys.modules[file_name_path], class_name)
                alert = Alert()
                self.alerts[file_name] = alert

    def run(self):
        email_body = ''
        stock_alerts = {}
        for ticker in self.config_parser.sections():
            alert_types = [x.strip() for x in self.config_parser.get(ticker, 'alerts').split(',')]
            stock_alerts[ticker] = alert_types
        self.create_alerts()
        for ticker in stock_alerts:
            self.logger.info('Running {ticker} with alerts: {alerts}'.format(ticker=ticker, alerts=stock_alerts[ticker]))
            for alert_type in stock_alerts[ticker]:
                result = self.alerts[alert_type].run(ticker)
                if result['pass']:
                    email_body += result['message'] + '\n'
                self.logger.info('{passed} {alert_type} message: {message}'.format(
                    passed='PASSED' if result['pass'] else 'FAILED', alert_type=alert_type,
                    message=result['message']))

        print(email_body)


if __name__ == '__main__':
    s = StockAlerts()
    s.run()

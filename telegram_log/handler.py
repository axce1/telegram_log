import logging
import requests

from telegram_log.formatter import HTMLFormatter


# https://docs.python.org/3/howto/logging.html#library-config
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class TelegramLog(logging.Handler):

    def __init__(self, token, chat_id=None, level=logging.NOTSET):
        super(TelegramLog, self).__init__(level=level)
        self.token = token
        self.chat_id = chat_id or self.get_chat_id()
        self.setFormatter(HTMLFormatter())

    def bot_url(self, token, method, **kwargs):
        return 'https://api.telegram.org/bot{token}/{method}'\
            .format(token=token, method=method)

    def send_request(self, method, **kwargs):
        url = self.bot_url(self.token, method)

        try:
            resp = requests.post(url, **kwargs)
            assert resp.status_code == 200
            return resp.json()
        except:
            logger.exception('Error POST request to {url}'.format(url=url))
        return resp

    def get_chat_id(self):
        resp = self.send_request('getUpdates')

        try:
           return resp['result'][-1]['message']['chat']['id']
        except IndexError:
           logger.debug(resp)

    def send_message(self, message, **kwargs):
        data = {'text': message}
        data.update(kwargs)

        return self.send_request('sendMessage', json=data)

    def emit(self, record):
        message = self.format(record)
        payload = {
            'chat_id': self.chat_id,
        }

        payload['parse_mode'] = self.formatter.parse_mode

        resp = self.send_message(message, **payload)

        if not resp:
            return

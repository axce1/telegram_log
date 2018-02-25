import pytest
import logging
import unittest.mock as mock
import telegram_log


class MockLoggingHandler(logging.Handler):
    def __init__(self, *args, **kwargs):
        self.messages = {'debug': [], 'info': [], 'warning': [], 'error': [],
                         'critical': []}
        super(MockLoggingHandler, self).__init__(*args, **kwargs)

    def emit(self, record):
        "Store a message from ``record`` in the instance's ``messages`` dict."
        try:
            self.messages[record.levelname.lower()].append(record.getMessage())
        except Exception:
            self.handleError(record)

    def reset(self):
        self.acquire()
        try:
            for message_list in self.messages.values():
                message_list.clear()
        finally:
            self.release()


@pytest.fixture
def handler():
    handler = telegram_log.handler.TelegramLog('token',
                                               'chat_id', logging.DEBUG)
    telegram_log.handler.logger.handlers = []
    telegram_log.handler.logger.addHandler(MockLoggingHandler())
    telegram_log.handler.logger.level = logging.DEBUG
    return handler


def test_emit(handler):
    record = logging.makeLogRecord({'msg': 'hello'})

    with mock.patch('requests.post') as patch:
        handler.emit(record)

    assert patch.called
    assert patch.call_count == 1
    assert patch.call_args[1]['json']['chat_id'] == 'chat_id'
    assert 'hello' in patch.call_args[1]['json']['text']
    assert patch.call_args[1]['json']['parse_mode'] == 'HTML'

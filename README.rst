Python logging handler


HowTo Use:

import telegram_log, logging

logger = logging.getLogger('myApp')

handler = telegram_log.TelegramLog('bot_token')

formatter = telegram_log.MarkdownFormatter()

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.setLevel(logging.WARNING)

logger.warning('we have a warning')



Use with config file:

USER_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'telegram': {
            'class': 'telegram_log.TelegramLog',
            'token': 'bot_token',
            'chat_id': 'chat_id',
        },
    },
    "loggers": {
        'default': {
            'level': 'DEBUG',
            'handlers': ['telegram']
        },
    },
}



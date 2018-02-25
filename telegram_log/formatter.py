from logging import Formatter


class TextFormatter(Formatter):
    fmt = '%(asctime)s - %(name)s \n%(levelname)s - %(message)s'
    parse_mode = None

    def __init__(self, fmt=None, *args, **kwargs):
        super(TextFormatter, self).__init__(self.fmt)


class MarkdownFormatter(Formatter):
    fmt = '`%(asctime)s` *%(name)s*\n[%(levelname)s - %(message)s]'
    parse_mode = 'MARKDOWN'

    def __init__(self, fmt=None, *args, **kwargs):
        super(MarkdownFormatter, self).__init__(self.fmt)


class HTMLFormatter(Formatter):
    fmt = '%(asctime)s - <b>%(name)s</b>\
        <pre>%(levelname)s - %(message)s</pre>'
    parse_mode = 'HTML'

    def __init__(self, fmt=None, *args, **kwargs):
        super(HTMLFormatter, self).__init__(self.fmt)

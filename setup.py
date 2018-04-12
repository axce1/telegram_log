from setuptools import setup, find_packages



setup(
    install_requires=['requests'],
    name='telegram-logging',
    version='0.1.1',
    packages=['telegram_log'],
    url='https://github.com/axce1/telegram-logging',
    license='WTFPL',
    author='axce1',
    author_email='axcel.github@gmail.com',
    description='Telegram logging handler',
    long_description=open('README.rst').read(),
)

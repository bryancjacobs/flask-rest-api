try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='kafroxy',
    version='0.1.25',
    description='rest api over kafka producer poc',
    long_description='rest api over kafka producer poc',
    author='Bryan Jacobs',
    url='https://github.com/phil-willett/python-redis-log',
    packages=['kafroxy'],
    license='MIT',
    install_requires=['kafka-python', 'gunicorn', 'flask', 'kafka', 'config','flask-cors']
)

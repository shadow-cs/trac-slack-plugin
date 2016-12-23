from setuptools import setup, find_packages

setup(
    name='SlackNotificationPlugin',
    version='0.2',
    description='Plugin to announce Trac changes in Slack',
    author='Wagner Pinheiro',
    url='https://github.com/wagnerpinheiro/trac-slack-plugin',
    license='BSD',
    #packages=['slack_notification'],
    packages=find_packages(exclude=['*.tests']),
    classifiers=[
        'Framework :: Trac',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'trac.plugins': 'slack_notification = slack_notification'
    }
)

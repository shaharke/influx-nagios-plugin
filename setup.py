from distutils.core import setup
 
setup(
    name='influx-nagios-plugin',
    version="1.0.0",
    packages=['influx-nagios-plugin'],
    license='MIT',
    url="https://github.com/shaharke/nagios-influx-plugin.git",
    description='Nagios plugin for querying monitoring stats from InfluxDB',
    author='Shahar Kedar',
    author_email='shahar at gmail com',
    scripts=['check_influx.py']
)

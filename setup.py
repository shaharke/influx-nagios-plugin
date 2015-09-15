from distutils.core import setup
 
setup(
    name='influx-nagios-plugin',
    version="1.1.0",
    packages=['src'],
    install_requires=['influxdb', 'NagAconda'],
    license='MIT',
    url="https://github.com/shaharke/nagios-influx-plugin.git",
    description='Nagios plugin for querying stats from InfluxDB',
    author='Shahar Kedar',
    author_email='shahar at gmail com',
    scripts=['src/check_influx']
)

nagios-influx-plugin
====================

Nagios plugin for querying stats from InfluxDB

**Installation:**

```shell
pip install influx-nagios-plugin
```

**Usage:**

```shell
check_influx -h HOST_PORT -u USERNAME -p PASSWORD -d DATABASE -q QUERY [-m METRIC] [-w WARNING] [-c CRITICAL]
```

**Options**:

**-h** Colon separated host and port of InfluxDB (e.g. localhost:8086). Port is optional (8086 by default)<br>
**-u** InfluxDB username<br>
**-p** InfluxDB password<br>
**-d** InfluxDB database name<br>
**-q** Query to execute<br>
**-w** Warning threshold<br>
**-c** Critical threshold<br>
**-m** Metric name. Query will be used by default _[OPTIONAL]_

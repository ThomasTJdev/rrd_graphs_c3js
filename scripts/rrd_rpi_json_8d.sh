#!/usr/bin/env bash
rrdtool xport -s now-8d -e now --step 60 --json \
DEF:a=/var/lib/monitorix/raspberrypi.rrd:rpi_temp0:AVERAGE \
XPORT:a:"Temperature" > ../data/rrd_rpi_temp_8d.json


rrdtool xport -s now-8d -e now --step 60 --json \
DEF:a=/var/lib/monitorix/raspberrypi.rrd:rpi_clock0:AVERAGE \
DEF:b=/var/lib/monitorix/raspberrypi.rrd:rpi_clock1:AVERAGE \
DEF:c=/var/lib/monitorix/raspberrypi.rrd:rpi_clock2:AVERAGE \
DEF:d=/var/lib/monitorix/raspberrypi.rrd:rpi_clock3:AVERAGE \
DEF:e=/var/lib/monitorix/raspberrypi.rrd:rpi_clock4:AVERAGE \
DEF:f=/var/lib/monitorix/raspberrypi.rrd:rpi_clock5:AVERAGE \
DEF:g=/var/lib/monitorix/raspberrypi.rrd:rpi_clock6:AVERAGE \
DEF:h=/var/lib/monitorix/raspberrypi.rrd:rpi_clock7:AVERAGE \
DEF:i=/var/lib/monitorix/raspberrypi.rrd:rpi_clock8:AVERAGE \
XPORT:a:"arm" \
XPORT:b:"core" \
XPORT:c:"h264" \
XPORT:d:"isp" \
XPORT:e:"v3d" \
XPORT:f:"uart" \
XPORT:g:"emmc" \
XPORT:h:"pixel" \
XPORT:i:"hdmi" > ../data/rrd_rpi_clock_8d.json


rrdtool xport -s now-8d -e now --step 60 --json \
DEF:a=/var/lib/monitorix/raspberrypi.rrd:rpi_volt0:AVERAGE \
DEF:b=/var/lib/monitorix/raspberrypi.rrd:rpi_volt1:AVERAGE \
DEF:c=/var/lib/monitorix/raspberrypi.rrd:rpi_volt2:AVERAGE \
DEF:d=/var/lib/monitorix/raspberrypi.rrd:rpi_volt3:AVERAGE \
XPORT:a:"Core" \
XPORT:b:"sdram_c" \
XPORT:c:"sdram_i" \
XPORT:d:"sdram_p" > ../data/rrd_rpi_volt_8d.json

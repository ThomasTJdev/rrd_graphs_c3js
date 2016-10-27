#!/bin/bash
echo "Executing all RRD scripts"

cd "${0%/*}"

if [ "$1" == "1h" ]; then
    sh ./rrd_kernel_json_1h.sh
    sh ./rrd_netstat_json_1h.sh
    sh ./rrd_rpi_json_1h.sh
    sh ./rrd_system_json_1h.sh

elif [ "$1" == "3h" ]; then
    sh ./rrd_kernel_json_3h.sh
    sh ./rrd_netstat_json_3h.sh
    sh ./rrd_rpi_json_3h.sh
    sh ./rrd_system_json_3h.sh

elif [ "$1" == "24h" ]; then
    sh ./rrd_netstat_json_24h.sh
    sh ./rrd_kernel_json_24h.sh
    sh ./rrd_rpi_json_24h.sh
    sh ./rrd_system_json_24h.sh

elif [ "$1" == "8d" ]; then
    sh ./rrd_netstat_json_8d.sh
    sh ./rrd_kernel_json_8d.sh
    sh ./rrd_rpi_json_8d.sh
    sh ./rrd_system_json_8d.sh

else
    echo "Wrong argument."
    echo "Allowed: 1h, 3h, 24h, 8d"

fi

echo "RRD script done"

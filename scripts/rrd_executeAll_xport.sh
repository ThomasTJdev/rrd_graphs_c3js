#!/bin/bash
echo "Executing all RRD scripts"

sh ./rrd_kernel_json_3h.sh
sh ./rrd_kernel_json_24h.sh
sh ./rrd_kernel_json_8d.sh

sh ./rrd_netstat_json_3h.sh
sh ./rrd_netstat_json_24h.sh
sh ./rrd_netstat_json_8d.sh

sh ./rrd_rpi_json_3h.sh
sh ./rrd_rpi_json_24h.sh
sh ./rrd_rpi_json_8d.sh

sh ./rrd_system_json_3h.sh
sh ./rrd_system_json_24h.sh
sh ./rrd_system_json_8d.sh

echo "RRD script done"

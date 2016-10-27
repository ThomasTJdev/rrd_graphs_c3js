#!/usr/bin/env bash
rrdtool xport -s now-24h -e now --step 60 --json \
DEF:a=/var/lib/monitorix/system.rrd:system_load1:AVERAGE \
DEF:b=/var/lib/monitorix/system.rrd:system_load5:AVERAGE \
DEF:c=/var/lib/monitorix/system.rrd:system_load15:AVERAGE \
XPORT:a:"Load 1 min average" \
XPORT:b:"Load 5 min average" \
XPORT:c:"Load 15 min average" > ../data/rrd_system_load_24h.json

rrdtool xport -s now-24h -e now --step 60 --json \
DEF:a=/var/lib/monitorix/system.rrd:system_nproc:AVERAGE \
DEF:b=/var/lib/monitorix/system.rrd:system_npslp:AVERAGE \
DEF:c=/var/lib/monitorix/system.rrd:system_nprun:AVERAGE \
DEF:d=/var/lib/monitorix/system.rrd:system_npwio:AVERAGE \
DEF:e=/var/lib/monitorix/system.rrd:system_npzom:AVERAGE \
DEF:f=/var/lib/monitorix/system.rrd:system_npstp:AVERAGE \
DEF:g=/var/lib/monitorix/system.rrd:system_npswp:AVERAGE \
XPORT:a:"Processes" \
XPORT:b:"Processes sleeping" \
XPORT:c:"Processes running" \
XPORT:d:"wio" \
XPORT:e:"zom" \
XPORT:f:"stp" \
XPORT:g:"Processes swap" > ../data/rrd_system_processor_24h.json

rrdtool xport -s now-24h -e now --step 60 --json \
DEF:a=/var/lib/monitorix/system.rrd:system_mtotl:AVERAGE \
DEF:b=/var/lib/monitorix/system.rrd:system_mbuff:AVERAGE \
DEF:c=/var/lib/monitorix/system.rrd:system_mcach:AVERAGE \
DEF:d=/var/lib/monitorix/system.rrd:system_mfree:AVERAGE \
DEF:e=/var/lib/monitorix/system.rrd:system_macti:AVERAGE \
DEF:f=/var/lib/monitorix/system.rrd:system_minac:AVERAGE \
XPORT:a:"Memory total" \
XPORT:b:"Memory buffers" \
XPORT:c:"Memory cached" \
XPORT:d:"Memory free" \
XPORT:e:"Memory active" \
XPORT:f:"Memory inactive" > ../data/rrd_system_memory_24h.json

rrdtool xport -s now-24h -e now --step 60 --json \
DEF:a=/var/lib/monitorix/system.rrd:system_val01:AVERAGE \
DEF:b=/var/lib/monitorix/system.rrd:system_val02:AVERAGE \
DEF:c=/var/lib/monitorix/system.rrd:system_val03:AVERAGE \
DEF:d=/var/lib/monitorix/system.rrd:system_val04:AVERAGE \
DEF:e=/var/lib/monitorix/system.rrd:system_val05:AVERAGE \
XPORT:a:"A" \
XPORT:b:"B" \
XPORT:c:"C" \
XPORT:d:"D" \
XPORT:e:"E" > ../data/rrd_system_val_24h.json


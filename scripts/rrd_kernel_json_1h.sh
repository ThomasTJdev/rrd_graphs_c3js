#!/usr/bin/env bash
rrdtool xport -s now-1h -e now --step 60 --json \
DEF:a=/var/lib/monitorix/kern.rrd:kern_user:AVERAGE \
DEF:b=/var/lib/monitorix/kern.rrd:kern_nice:AVERAGE \
DEF:c=/var/lib/monitorix/kern.rrd:kern_sys:AVERAGE \
DEF:d=/var/lib/monitorix/kern.rrd:kern_idle:AVERAGE \
DEF:e=/var/lib/monitorix/kern.rrd:kern_iow:AVERAGE \
DEF:f=/var/lib/monitorix/kern.rrd:kern_irq:AVERAGE \
DEF:g=/var/lib/monitorix/kern.rrd:kern_sirq:AVERAGE \
DEF:h=/var/lib/monitorix/kern.rrd:kern_steal:AVERAGE \
XPORT:a:"user" \
XPORT:b:"nice" \
XPORT:c:"system" \
XPORT:d:"Idle" \
XPORT:e:"I/O wait" \
XPORT:f:"IRQ" \
XPORT:g:"softIRQ" \
XPORT:h:"steal" > ../data/rrd_kernel_usage_1h.json


rrdtool xport -s now-1h -e now --step 60 --json \
DEF:a=/var/lib/monitorix/kern.rrd:kern_cs:AVERAGE \
DEF:b=/var/lib/monitorix/kern.rrd:kern_forks:AVERAGE \
XPORT:a:"Context switches" \
XPORT:b:"Forks" > ../data/rrd_kernel_switchesforks_1h.json


rrdtool xport -s now-1h -e now --step 60 --json \
DEF:a=/var/lib/monitorix/kern.rrd:kern_inode:AVERAGE \
DEF:b=/var/lib/monitorix/kern.rrd:kern_dentry:AVERAGE \
DEF:c=/var/lib/monitorix/kern.rrd:kern_file:AVERAGE \
XPORT:a:"inode" \
XPORT:b:"dentry" \
XPORT:c:"file" > ../data/rrd_kernel_VFSusage_1h.json

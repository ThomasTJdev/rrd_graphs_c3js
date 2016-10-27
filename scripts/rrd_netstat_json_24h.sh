#!/usr/bin/env bash
rrdtool xport -s now-24h -e now --step 60 --json \
DEF:a=/var/lib/monitorix/netstat.rrd:nstat4_closed:AVERAGE \
DEF:b=/var/lib/monitorix/netstat.rrd:nstat4_listen:AVERAGE \
DEF:c=/var/lib/monitorix/netstat.rrd:nstat4_synsent:AVERAGE \
DEF:d=/var/lib/monitorix/netstat.rrd:nstat4_synrecv:AVERAGE \
DEF:e=/var/lib/monitorix/netstat.rrd:nstat4_estblshd:AVERAGE \
DEF:f=/var/lib/monitorix/netstat.rrd:nstat4_finwait1:AVERAGE \
DEF:g=/var/lib/monitorix/netstat.rrd:nstat4_finwait2:AVERAGE \
XPORT:a:"Closed" \
XPORT:b:"Listen" \
XPORT:c:"Syn_sent" \
XPORT:d:"Syn_recv" \
XPORT:e:"Established" \
XPORT:f:"FIN_wait1" \
XPORT:g:"FIN_wait2" > ../data/rrd_netstat_states_24h.json

import subprocess 
import shlex 
import time
import json
from flask import Flask, render_template, request
from time import sleep

# Importing parser
import parse_json_to_C3js as pjtC3js

#==================#
# Settings - START #
#==================#

hostname = 'RPi-2'

#==================#
# Settings - END   #
#==================#



app = Flask(__name__)



@app.route('/1h')
def charts_1h():
    
    # First update the RRD->JSON data
    pjtC3js.run_commandOnce("sh ./scripts/rrd_executeAll_xport2.sh 1h")
    sleep(0.5)

    # Get the data in JSON format and parse it
    data1 = pjtC3js.getJson('rrd_kernel_usage_1h.json')
    data2 = pjtC3js.getJson('rrd_kernel_switchesforks_1h.json')
    data3 = pjtC3js.getJson('rrd_kernel_VFSusage_1h.json')
    data4 = pjtC3js.getJson('rrd_netstat_states_1h.json')
    data5 = pjtC3js.getJson('rrd_rpi_clock_1h.json')
    data6 = pjtC3js.getJson('rrd_rpi_temp_1h.json')
    data7 = pjtC3js.getJson('rrd_rpi_volt_1h.json')
    data8 = pjtC3js.getJson('rrd_system_load_1h.json')
    data9 = pjtC3js.getJson('rrd_system_memory_1h.json')
    data10 = pjtC3js.getJson('rrd_system_processor_1h.json')

    # Render the flask template with information
    return render_template('charts.html', hostname=hostname, 
        data1=data1, yaxisName1="Percent (%)", name1="Kernel usage",
        data2=data2, yaxisName2="CS & forks/s", name2="Context switches and forks",
        data3=data3, yaxisName3="Percent (%)", name3="VFS usage",
        data4=data4, yaxisName4="Connections", name4="IPv4 states",
        data5=data5, yaxisName5="Hz", name5="RPi - Clock frequency",
        data6=data6, yaxisName6="Temperature (c)", name6="RPi - Temperature",
        data7=data7, yaxisName7="Volts", name7="RPi - Voltages",
        data8=data8, yaxisName8="Load average", name8="System load",
        data9=data9, yaxisName9="Megabytes", name9="Memory allocation",
        data10=data10, yaxisName10="Processes", name10="Active processes"
    )

@app.route('/3h')
def charts_3h():

    pjtC3js.run_commandOnce("sh ./scripts/rrd_executeAll_xport2.sh 3h")

    data1 = pjtC3js.getJson('rrd_kernel_usage_3h.json')
    data2 = pjtC3js.getJson('rrd_kernel_switchesforks_3h.json')
    data3 = pjtC3js.getJson('rrd_kernel_VFSusage_3h.json')
    data4 = pjtC3js.getJson('rrd_netstat_states_3h.json')
    data5 = pjtC3js.getJson('rrd_rpi_clock_3h.json')
    data6 = pjtC3js.getJson('rrd_rpi_temp_3h.json')
    data7 = pjtC3js.getJson('rrd_rpi_volt_3h.json')
    data8 = pjtC3js.getJson('rrd_system_load_3h.json')
    data9 = pjtC3js.getJson('rrd_system_memory_3h.json')
    data10 = pjtC3js.getJson('rrd_system_processor_3h.json')

    return render_template('charts.html', hostname=hostname, 
        data1=data1, yaxisName1="Percent (%)", name1="Kernel usage",
        data2=data2, yaxisName2="CS & forks/s", name2="Context switches and forks",
        data3=data3, yaxisName3="Percent (%)", name3="VFS usage",
        data4=data4, yaxisName4="Connections", name4="IPv4 states",
        data5=data5, yaxisName5="Hz", name5="RPi - Clock frequency",
        data6=data6, yaxisName6="Temperature (c)", name6="RPi - Temperature",
        data7=data7, yaxisName7="Volts", name7="RPi - Voltages",
        data8=data8, yaxisName8="Load average", name8="System load",
        data9=data9, yaxisName9="Megabytes", name9="Memory allocation",
        data10=data10, yaxisName10="Processes", name10="Active processes"
    )

@app.route('/24h')
def charts_24h():

    pjtC3js.run_commandOnce("sh ./scripts/rrd_executeAll_xport2.sh 24h")
    sleep(0.5)

    data1 = pjtC3js.getJson('rrd_kernel_usage_24h.json')
    data2 = pjtC3js.getJson('rrd_kernel_switchesforks_24h.json')
    data3 = pjtC3js.getJson('rrd_kernel_VFSusage_24h.json')
    data4 = pjtC3js.getJson('rrd_netstat_states_24h.json')
    data5 = pjtC3js.getJson('rrd_rpi_clock_24h.json')
    data6 = pjtC3js.getJson('rrd_rpi_temp_24h.json')
    data7 = pjtC3js.getJson('rrd_rpi_volt_24h.json')
    data8 = pjtC3js.getJson('rrd_system_load_24h.json')
    data9 = pjtC3js.getJson('rrd_system_memory_24h.json')
    data10 = pjtC3js.getJson('rrd_system_processor_24h.json')

    return render_template('charts.html', hostname=hostname, 
        data1=data1, yaxisName1="Percent (%)", name1="Kernel usage",
        data2=data2, yaxisName2="CS & forks/s", name2="Context switches and forks",
        data3=data3, yaxisName3="Percent (%)", name3="VFS usage",
        data4=data4, yaxisName4="Connections", name4="IPv4 states",
        data5=data5, yaxisName5="Hz", name5="RPi - Clock frequency",
        data6=data6, yaxisName6="Temperature (c)", name6="RPi - Temperature",
        data7=data7, yaxisName7="Volts", name7="RPi - Voltages",
        data8=data8, yaxisName8="Load average", name8="System load",
        data9=data9, yaxisName9="Megabytes", name9="Memory allocation",
        data10=data10, yaxisName10="Processes", name10="Active processes"
    )

@app.route('/8d')
def charts_8d():

    pjtC3js.run_commandOnce("sh ./scripts/rrd_executeAll_xport2.sh 8d")
    sleep(0.5)

    data1 = pjtC3js.getJson('rrd_kernel_usage_8d.json')
    data2 = pjtC3js.getJson('rrd_kernel_switchesforks_8d.json')
    data3 = pjtC3js.getJson('rrd_kernel_VFSusage_8d.json')
    data4 = pjtC3js.getJson('rrd_netstat_states_8d.json')
    data5 = pjtC3js.getJson('rrd_rpi_clock_8d.json')
    data6 = pjtC3js.getJson('rrd_rpi_temp_8d.json')
    data7 = pjtC3js.getJson('rrd_rpi_volt_8d.json')
    data8 = pjtC3js.getJson('rrd_system_load_8d.json')
    data9 = pjtC3js.getJson('rrd_system_memory_8d.json')
    data10 = pjtC3js.getJson('rrd_system_processor_8d.json')

    return render_template('charts.html', hostname=hostname, 
        data1=data1, yaxisName1="Percent (%)", name1="Kernel usage",
        data2=data2, yaxisName2="CS & forks/s", name2="Context switches and forks",
        data3=data3, yaxisName3="Percent (%)", name3="VFS usage",
        data4=data4, yaxisName4="Connections", name4="IPv4 states",
        data5=data5, yaxisName5="Hz", name5="RPi - Clock frequency",
        data6=data6, yaxisName6="Temperature (c)", name6="RPi - Temperature",
        data7=data7, yaxisName7="Volts", name7="RPi - Voltages",
        data8=data8, yaxisName8="Load average", name8="System load",
        data9=data9, yaxisName9="Megabytes", name9="Memory allocation",
        data10=data10, yaxisName10="Processes", name10="Active processes"
    )


@app.route('/charts_all')
def charts_all():

    # Update data
    pjtC3js.run_commandOnce("sh ./scripts/rrd_executeAll_xport2.sh 1h")
    sleep(0.4)
    pjtC3js.run_commandOnce("sh ./scripts/rrd_executeAll_xport2.sh 3h")
    sleep(0.4)
    pjtC3js.run_commandOnce("sh ./scripts/rrd_executeAll_xport2.sh 24h")
    sleep(0.4)
    pjtC3js.run_commandOnce("sh ./scripts/rrd_executeAll_xport2.sh 8d")
    sleep(0.4)

    # Define variables
    # Kernel usage
    data1 = pjtC3js.getJson('rrd_kernel_usage_1h.json')
    # Context and swtiches
    data2 = pjtC3js.getJson('rrd_kernel_switchesforks_1h.json')
    # VFS usage
    data3 = pjtC3js.getJson('rrd_kernel_VFSusage_1h.json')
    # Netstat (IPv4)
    data4 = pjtC3js.getJson('rrd_netstat_states_1h.json')
    # Clock fq
    data5 = pjtC3js.getJson('rrd_rpi_clock_1h.json')
    # Temperature
    data6 = pjtC3js.getJson('rrd_rpi_temp_1h.json')
    data6_3h = pjtC3js.getJson('rrd_rpi_temp_3h.json')
    data6_24h = pjtC3js.getJson('rrd_rpi_temp_24h.json')
    data6_8d = pjtC3js.getJson('rrd_rpi_temp_8d.json')
    # Voltages
    data7 = pjtC3js.getJson('rrd_rpi_volt_1h.json')
    # System load
    data8 = pjtC3js.getJson('rrd_system_load_1h.json')
    data8_3h = pjtC3js.getJson('rrd_system_load_3h.json')
    data8_24h = pjtC3js.getJson('rrd_system_load_24h.json')
    data8_8d = pjtC3js.getJson('rrd_system_load_8d.json')
    # System memory
    data9 = pjtC3js.getJson('rrd_system_memory_1h.json')
    data9_3h = pjtC3js.getJson('rrd_system_memory_3h.json')
    data9_24h = pjtC3js.getJson('rrd_system_memory_24h.json')
    data9_8d = pjtC3js.getJson('rrd_system_memory_8d.json')
    #Processor
    data10 = pjtC3js.getJson('rrd_system_processor_1h.json')

    # Render template
    return render_template('charts_all.html', hostname=hostname, 
        data1=data1, yaxisName1="Percent (%)", name1="Kernel usage",
        data2=data2, yaxisName2="CS & forks/s", name2="Context switches and forks",
        data3=data3, yaxisName3="Percent (%)", name3="VFS usage",
        data4=data4, yaxisName4="Connections", name4="IPv4 states",
        data5=data5, yaxisName5="Hz", name5="RPi - Clock frequency",
        data6=data6, yaxisName6="Temperature (c)", name6="RPi - Temperature",
        data6_3h=data6_3h,
        data6_24h=data6_24h,
        data6_8d=data6_8d,
        data7=data7, yaxisName7="Volts", name7="RPi - Voltages",
        data8=data8, yaxisName8="Load average", name8="System load",
        data8_3h=data8_3h,
        data8_24h=data8_24h,
        data8_8d=data8_8d,
        data9=data9, yaxisName9="Megabytes", name9="Memory allocation",
        data9_3h=data9_3h,
        data9_24h=data9_24h,
        data9_8d=data9_8d,
        data10=data10, yaxisName10="Processes", name10="Active processes"
    )


    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)


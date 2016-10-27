Visualize RRD data in charts
============================

Export RRD data and visualize it with a flask webserver

License
-------

ThomasTJ - MIT

Requirements
------------

* Python >= 3
* Flask
* CDN jquery, d3js, c3js (is already included)
* Install and run Monitorix (webserver is not needed)

Run
---

Run:
python3 app.py

Access the webserver:
0.0.0.0:5004/1h
0.0.0.0:5004/3h
0.0.0.0:5004/24h
0.0.0.0:5004/8d
0.0.0.0:5004/charts_all

Update data
-----------

This is done automatically through the app.py
cd scripts
./rrd_executeAll_xport.sh

How it works
------------

1. Monitorix creates RRD DB where system information is stored
2. The scripts in the **script** folder:
    * It gathers the data from the RRD 
    * Exports it to JSON
3. The python **parse_json_to_C3js.py** parses the data to C3js format
4. Running the **app.py** will serve the data through flask on 0.0.0.0:5004/charts_all
5. Change the hostname in app.py to your device name

TODO
----

* (DEV info) Remove not used code, which is imported from git system_information
* Run updating scripts and parsing as threads for optimizing speed (removing delay)
* Clock fq and memory y-axis and data - wrong thousands. Bytes instead of MB, etc.

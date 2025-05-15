evpv-tools
==========

The repository `evpv_tools <https://github.com/evpv-simulator/evpv-tools>`_ contains various Python helper scripts designed to support and extend the functionality of the **EVPV** model. These tools assist users in preparing input datasets, post-processing model outputs, and performing additional analyses.

All the scripts come with comments to help you run them easily and adapt them to your needs. Make sure to have all the required libraries installed before running the scripts.

Current Available Scripts
-------------------------

As of now, the repository includes the following scripts:

1. ``extract_pois_from_osm.py``: Retrieves Points of Interest (POIs) OR Workplaces from OpenStreetMap using the OSMNx library.

2. ``compare_road_and_euclidian_distance.py``: Compares Euclidean and road distances between randomly generated coordinates within a bounding box.

3. ``analyse_fuel_and_co2_savings.py``: Assesses the fuel cost and CO2 emission savings from switching from ICEVs to EVs based on simulated vehicle flow and travel distances from the EVPV model.
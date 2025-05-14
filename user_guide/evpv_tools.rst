evpv-tools
==========

The repository `evpv_tools <https://github.com/evpv-simulator/evpv-tools>`_ contains various Python helper scripts designed to support and extend the functionality of the **EVPV** model. These tools assist users in preparing input datasets, post-processing model outputs, and performing additional analyses.

Current Available Scripts
-------------------------

As of now, the repository includes the following scripts:

1. ``extract_pois_from_osm.py``

   - **Purpose**: Retrieves Points of Interest (POIs) OR Workplaces from OpenStreetMap using the OSMNx library.
   - **Functionality**:
     - Splits a large bounding box into smaller segments to bypass OSM data request limits.
     - Fetches POI locations and outputs the center coordinates in both GeoJSON and CSV formats.
     - Helps generate weighted distributions of POIs for EVPV mobility simulations.
   - **Outputs**:
     - `center_points.geojson`: POI center coordinates as GeoJSON.
     - `center_points.csv`: CSV file of unique coordinates with occurrence counts.
   - **Dependencies**:
     - `geopandas`, `pandas`, `numpy`, `shapely`, `osmnx`
     

2. ``compare_road_and_euclidian_distance.py``

   - **Purpose**: Compares Euclidean and road distances between randomly generated coordinates within a bounding box.
   - **Functionality**:
     - Generates random geographical coordinates within the defined bounding box.
     - Calculates the **Euclidean distance** using the geodesic method from the `geopy` library.
     - Calculates the **road distance** using the OpenRouteService (ORS) API.
     - Results are stored in a Pandas DataFrame and exported to a CSV file.
   - **Outputs**:
     - `road_vs_euclidian_distances.csv`: A CSV file containing the calculated Euclidean and road distances.
   - **Dependencies**:
     - `openrouteservice`: Interacts with the OpenRouteService API for routing distances.
     - `geopy`: Used to calculate Euclidean distances.
     - `pandas`: For data manipulation and CSV file creation.


3. ``analyse_fuel_and_co2_savings.py``

   - **Purpose**: Assesses the fuel cost and CO₂ emission savings from switching from ICEVs to EVs based on simulated vehicle flow and travel distances from the EVPV model.
   - **Functionality**:
     - Processes the output of the mobility simulation to estimate:
       1. **CO₂ emission savings per vehicle** by comparing ICEV and EV emissions.
       2. **Fuel cost savings per vehicle** by comparing ICEV fuel costs and EV charging costs.
       3. **Total and per-vehicle savings**, weighted by vehicle flow.
       4. **Histograms of CO₂ and fuel cost savings**, weighted by vehicle flow.
     - Summary results are saved to a CSV file for further analysis.
   - **Outputs**:
     - `co2_fuel_savings_results.csv`: CSV file with calculated savings data.
   - **Dependencies**:
     - `pandas`: For reading input CSV and performing calculations.
     - `numpy`: For numerical operations and binning histogram data.
     - `matplotlib`: To generate histograms of CO₂ and fuel cost savings.

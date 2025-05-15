Addis Ababa - Simple
====================

About Examples
--------------

The `evpv_examples <https://github.com/evpv-simulator/evpv-examples>`_ repository provides a collection of ready-to-use case studies, complete with all necessary input and configuration files. These examples can help you explore the capabilities of the EV-PV simulator and serve as blueprints for developing your own custom analyses. Each example includes all the required files to run it. When applicable, examples are provided with both a configuration file for execution in **basic mode** (using the command-line interface), and a Python run script for execution in **advanced mode** for more control.

.. note::
    To run one of the cases, first `DOWNLOAD <https://github.com/evpv-simulator/evpv-examples/archive/refs/heads/main.zip>`_ the repository containing the examples, extract it and copy the contents of the example folder into the directory of your choice.
    
The following examples are available:

- **AddisAbaba_Simple**: A simple yet complete case study on the city of Addis Ababa, showcasing the full set of core outputs (mobility demand, charging demand, and EV-PV complementarity). 

Overview of the *AddisAbaba_Simple* example 
-----------------------------------------

This example case study simulates mobility demand, EV charging demand, and EV–PV synergy indicators in the administrative region of Addis Ababa. It models a simplified scenario that includes a basic EV fleet, user charging behavior at home, workplaces, and points of interest (POIs), and solar PV generation.

The example includes: (1) A configuration file for basic usage (2) A Python run script for advanced usage (3) a folder with the required input data (4) an empty folder where the results will be stored.

This document focuses on descrtibing the inputs and results obtained with the configuration file. However, note that all parameters can also be specified using the Python script (see script documentation directly for details).

Inputs
------
The configuration file is divided into several sections, each representing a key aspect of the simulation. Users are encouraged to explore the file directly for full documentation of available options. The default values define a simplified EV charging scenario for Addis Ababa:

1. **General Settings**: Output path and a name for the scenario.

2. **EV Fleet Properties**: Define the number of EVs to simulate and their properties, including battery size and energy consumption per km.

3. **Region of Interest**: Set the path to geospatial files defining the region of interest boundaries (GeoJSON) and features (population, workplaces, POIs). Also, set the spatial resolution.

4. **Mobility Simulation**: Configure parameters regarding the mobility demand simulation (e.g., with or without routing APIs)

5. **Charging Scenario**: Define the charging scenario: share of people charging at the different location types (home, work, POIs), available charger powers, typical arrival times at home and work.

6. **PV Energy Production**: Set the PV system type (rooftop, groundmounted, ...), as well as the simulation year.

7. **EV-PV Complementarity**: Define the PV capacity and the time frame for extracting the EV-PV complementarity indicators.

8. **Advanced Parameters**: Fine-tune the analysis with details such as traffic zone creation, trip distribution models, and technical parameters for PV.

Outputs
-------
After running the simulation, results are saved in structured subfolders inside the specified output directory. These outputs include raw data (CSV), and some interactive visualizations maps (HTML). A log file is also included for troubleshooting.

Folder structure and contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``Mobility/``: Contains data and visualizations related to the simulated mobility demand:

  - `mobility_res_TripDistribution_flows.csv`: Origin–destination matrix showing the number of vehicles traveling between each pair of traffic zones. Includes additional metrics such as road distance and Euclidean distance between zones.

  - `mobility_res_TripDistribution_aggregated_zone_metrics.csv`: Zone-level aggregated statistics: number of vehicles entering and leaving each zone, total distance traveled by incoming and outgoing vehicles, average travel distance per vehicle.

  - `mobility_vis_Region.html`: HTML map displaying key features of each traffic zone.

  - `mobility_vis_VehicleAllocation.html`: HTML map showing the number of vehicles allocated to each zone (i.e., the origin zones for trips).


- ``ChargingDemand/``: Contains results related to EV charging demand, both temporally and spatially:

  - `charging_res_temporal_demand_profile.csv`: Time series of the raw charging power profile for each individual vehicle.

  - `charging_res_temporal_demand_vehicle_properties.csv`: Metadata for each vehicle, including: charging frequency (days between charges), charging location, arrival and departure times. This file can be cross-referenced with the previous one using the vehicle ID.

  - `charging_res_temporal_demand_aggregated.csv`:  Aggregated charging load curves by location type (home, work, POI), including: total charging power per time step, number of vehicles present at every location, number of vehicles actively charging.

  - `charging_res_spatial_demand.csv`: Aggregated charging demand by traffic zone, including: total charging demand, number of charging vehicles per zone.

  - `charging_vis_TotalDemand.html`: HTML map showing the total daily charging energy demand.

  - `charging_vis_DemandPerVehicle.html`: HTML map showing the average energy demand per charging vehicle.

  - `charging_vis_NumberVehiclesCharging.html`: HTML map showing the number of vehicles charging.


- ``EVPV/``: Contains results related to photovoltaic (PV) energy production and EV–PV synergy indicators:

  - `evpv_res_PVProduction.csv`: Hourly PV production output over a year, including also other metrics (performance ratio, capacity factor, ...).

  - `evpv_res_DailyIndicators.csv`: Daily EV-PV complementarity indicators, including self-sufficiency, self-consumption, and excess PV production.

Examples visualization
^^^^^^^^^^^^^^^^^^^^^^
Data is saved in **CSV** format for compatibility with your preferred program (e.g., Excel, Python, R, etc.) for analysis and graphing. The graphs below were created from the raw results using the software OriginLab for demonstration purposes.

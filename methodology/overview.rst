Overview
========

The **evpv-simulator** model has three main objectives and corresponding outputs (as shown in Fig. 1, which illustrates the model’s key inputs, outputs, and processing steps):

1. **Mobility Demand Estimation.** 
   Based on a user-defined region of interest and associated geospatial input data (population density, workplaces, points of interest (POIs), and number of EVs to simulate), the tool divides the region of interest into traffic zones and assesses the mobility demand for commuting by simulating origin-destination for all EVs.

2. **Charging Demand Analysis.**  
   Using the mobility demand and basic properties of the EV fleet, the model calculates the spatial and temporal charging needs. Users define the preferred charging locations of EV users (at home, at work, or at POIs), typical arrival times, and the available charging powers at each location. The output includes zone-level charging demand and load curves, assuming uncoordinated charging as a baseline charging strategy.

3. **EV-PV Complementarity.**  
   Using PVLib and PVGIS weather data, the tool simulates the local hourly PV production over a given year. It then assesses how much of the EV charging demand can be met by solar energy, generating key performance indicators like self-sufficiency or self-consumption potentials.

.. image:: /_static/model_overview_3.jpg
   :width: 100%
   :align: center

.. centered:: *EVPV-Simulator methodology overview. Note that some optional input parameters and additional outputs are not shown.*

.. note::
   For more details regarding the different modelling steps, please refer to the dedicated sections or the reference paper: Jérémy Dumoulin et al. *A modeling framework to support the electrification of private transport in African cities: a case study of Addis Ababa*.*arXiv preprint* arXiv:2503.03671, 2025. `https://doi.org/10.48550/arXiv.2503.03671 <https://doi.org/10.48550/arXiv.2503.03671>`_
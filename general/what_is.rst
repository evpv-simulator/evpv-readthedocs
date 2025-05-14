What is EVPV Simulator?
========================

**The EVPV-simulator (Electric Vehicles - PhotoVoltaics Simulator)** is an open-source Python tool designed to calculate the spatio-temporal charging needs of privately-owned electric vehicles (EVs) and the potential for solar photovoltaics (PV) to meet these needs in a given region of interest.

Tailored especially for urban contexts with limited mobility data, the simulator enables the endogenous estimation of daily mobility patterns by combining georeferenced datasets with advanced spatial trip distribution models.

For PV generation, it leverages the capabilities of the **PVLib** library and supports a range of installation archetypes (e.g., rooftop, free-standing PV, etc.).

**Authors:**  
Jeremy Dumoulin, Alejandro Peña-Bello, Noémie Jeannin, Nicolas Wyrsch

**Lead institution:**  
EPFL PV-LAB, Switzerland

**Contact:**  
jeremy[dot]dumoulin[at]epfl[dot]ch

Overview of the Model
---------------------

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

Standout Features
-----------------
- **Spatial and temporal charging demand**:  
  The model calculates both the spatial charging demand (at a user-defined resolution) and the temporal charging demand, providing a detailed understanding of when and where charging is needed.

- **Open-data powered modelling**:  
  The model can be run using open-source geospatial data sourced from OpenStreetMap, making it applicable to any location.

- **Calibration-free mobility demand model for home-to-work commuting**:  
  Estimates commuting transport demand by modeling vehicle flows between origins (homes) and destinations (workplaces) using a calibration-free gravity model (`Lenormand et al <https://doi.org/10.1016/j.jtrangeo.2015.12.008>`_). Users can also incorporate additional weekday travel demand (e.g., shopping or leisure) by adding extra kilometers traveled.

- **Charging-decision modeling**:  
  Uses a state-of-the-art model based on state-of-charge (SoC) thresholds to determine whether vehicles charge on a given day, following `Pareschi et al <https://doi.org/10.1016/j.apenergy.2020.115318>`_.

- **Flexible EV fleet and charging infrastructure**:  
  Supports any user-defined scenario regarding EV fleet properties and charging infrastructure, including also a maximum charging power per vehicle.

- **Smart charging ready**:  
  Simulates uncontrolled ("dumb") charging by default. But the output can easily be used for more smart charging strategies. Also includes a rule-based peak shaving algorithm that shifts charging within arrival–departure windows to smooth the demand.

- **PV system presets**:  
  Easily generates PV production and EV–PV complementarity metrics for common PV system types (e.g., rooftop, ground-mounted, with or without tracking).

Citing EVPV-Simulator
---------------------
If you use EVPV-Simulator in a published work, please cite:

Jérémy Dumoulin et al. *A modeling framework to support the electrification of private transport in African cities: a case study of Addis Ababa*.  
*arXiv preprint* arXiv:2503.03671, 2025.  
`https://doi.org/10.48550/arXiv.2503.03671 <https://doi.org/10.48550/arXiv.2503.03671>`_

Acknowledgment
--------------

The development of the model was supported by the HORIZON `OpenMod4Africa <https://openmod4africa.eu/>`_ project (Grant number 101118123), with funding from the European Union and the State Secretariat for Education, Research and Innovation (SERI) for the Swiss partners. We also gratefully acknowledge the support of OpenMod4Africa partners for their contributions and collaboration.

License
-------

This project is licensed under the `GNU General Public License v3.0 <https://www.gnu.org/licenses/gpl-3.0.html>`_.






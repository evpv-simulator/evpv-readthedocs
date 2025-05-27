API
===

This page provides the API Reference for the classes of EV-PV Simulator.  

Each subsection below corresponds to a specific category of classes. 
All classes are documented using their docstrings and include constructor details, attributes, and available methods.

----

Vehicle definition
------------------

Classes related to the properties of the EV fleet.

Vehicle
~~~~~~~

.. autoclass:: evpv.vehicle.Vehicle
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

VehicleFleet
~~~~~~~~~~~~

.. autoclass:: evpv.vehiclefleet.VehicleFleet
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

----


Region of interest
------------------

Classes related to region of interest, and how it is subdivided into traffic zones and populated with aggregated geospatial data.

Region
~~~~~~

.. autoclass:: evpv.region.Region
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

----


Mobility Demand
---------------

Classes related to mobility demand simulation for a the given region.

MobilitySimulator
~~~~~~~~~~~~~~~~~

.. autoclass:: evpv.mobilitysimulator.MobilitySimulator
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

----

Charging Demand
---------------

Classes related to charging demand simulation.

ChargingSimulator
~~~~~~~~~~~~~~~~~

.. autoclass:: evpv.chargingsimulator.ChargingSimulator
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

----

PV Simulation and EV-PV Complementarity
---------------------------------------

Classes related to PV Production and EV-PV Complementarity indicators.

PVSimulator
~~~~~~~~~~~

.. autoclass:: evpv.pvsimulator.PVSimulator
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

EVPVSynergies
~~~~~~~~~~~~~

.. autoclass:: evpv.evpvSynergies.EVPVSynergies
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__
Advanced usage
==============

Using EVPV-simulator as a Python Module
---------------------------------------
Advanced users can write custom Python scripts by importing and interacting with core classes from the ``evpv`` module. 

.. code-block:: python

   from evpv.vehicle import Vehicle
   from evpv.vehiclefleet import VehicleFleet
   # etc.

For full class and method details, consult the **API reference**. To see how the classes work together in practice, we recommend starting explore the various `Examples <https://github.com/evpv-simulator/evpv-examples>`_.

Exploring the Codebase
----------------------
Advanced users and developers can also explore the source code in the class files inside the ``evpv/`` directory of the source code for a deeper understanding of the model architecture and classes.

All the classes are located in the ``evpv/`` folder, as shown in the project structure:

.. code-block:: bash

   ├── setup.py
   ├── README.md
   ├── evpv/
   │   ├── vehicle.py
   │   ├── vehiclefleet.py
   │   ├── region.py
   │   ├── mobilitysimulator.py
   │   ├── chargingsimulator.py
   │   ├── pvsimulator.py
   │   ├── evpvsynergies.py
   │   ├── evpv_cli.py
   │   └── helpers.py
   ├── examples/
   │   └── Basic_AddisAbaba_ConfigFile/
   ├── scripts/
   │   └── extract_pois_from_osm.py
   └── docs/

**Core Classes**

- ``Vehicle``: Defines a vehicle type.
- ``VehicleFleet``: Manages EV fleet data.
- ``Region``: Defines geospatial properties.
- ``MobilitySimulator``: Simulates trip generation and allocation.
- ``ChargingSimulator``: Estimates charging demand over time and space.
- ``PVSimulator``: Simulates solar energy production.
- ``EVPVSynergies``: Analyzes EV–PV interaction metrics.

**Utilities**

- ``evpv_cli.py``: Command-line interface (see :doc:`basic_usage`).
- ``helpers.py``: Internal utility functions.


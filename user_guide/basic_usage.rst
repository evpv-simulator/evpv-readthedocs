Basic usage
===========

After installation, you can run the **EVPV model in command-line mode**. This is ideal for users who are not familiar with Python or who want to quickly conduct a simple case study.

First, create a configuration file by copying an existing example such as the [Addis Ababa example](https://github.com/evpv-simulator/evpv-examples). Update it with your own input values and ensure that all required geospatial input data is available (see the config file and `input/` folder for guidance).

.. note::
    We recommend starting by running the Addis Ababa example to get familiar with the workflow. The easiest way to access all necessary files is to download the full GitHub repository with examples as a ZIP file, extract it and copy the contents of the Addis Ababa example folder into the directory of your choice.

Once your config file and geospatial input data are ready, open a terminal, activate your conda environment (optional), and run:

.. code-block:: bash

    evpv

You’ll be prompted to enter the path to your config file:

.. code-block:: bash

    Enter the path to the python configuration file: C:\Users\(...)\config.py

.. warning::
    Use absolute paths in the config file, or start the terminal in the same directory to use relative paths.

.. image:: docs/usage.gif
   :alt: Step-by-step run process for the Addis Ababa example

**Input parameters and required geospatial data files**

All input parameters are defined and explained in the configuration file you copied.

In addition to numerical and model-specific parameters, you'll need to provide paths to the following four geospatial data files:

- **Region of interest**: A GeoJSON file defining the boundary of your study area. For most administrative regions, you can download this from the [GADM dataset](https://gadm.org/).
- **Residential population**: A `.tif` raster file showing population density, in the WGS84 coordinate system. We recommend using the [GHS-POP dataset](https://human-settlement.emergency.copernicus.eu/download.php?ds=pop) at the lowest available resolution.
- **List of workplaces**: A CSV file with the following columns: `name`, `latitude`, `longitude`, and `weight`. You can generate this manually from local data or automatically extract it from OpenStreetMap using the helper script in `scripts/extract_pois_from_osm.py`.
- **List of POIs (Points of Interest)**: Same format and process as for workplaces. Use the same script but with modified inputs.

.. note::
    Need help in gathering the needed geospatial data for your own case study? See the `evpv.tools`.

**Model Outputs**

After running the simulation, the model generates output files organized into three main subfolders:
- `Mobility/`: Data and interactive maps related to the mobility demand simulation. Includes vehicle flows, travel distances, and aggregated data for the region of interest.
- `ChargingDemand/`: Charging demand outputs, including spatial and temporal demand per vehicle and per traffic zone. Also includes HTML maps for visualization.
- `EVPV/`: PV production curves and EV–PV complementarity indicators.
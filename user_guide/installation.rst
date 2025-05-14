Installation
============

Getting python
--------------
First of all, ensure Python is installed on your system. This project was developped with **Python 3.12**. Other versions may not be compatible. 

If it is your first time with Python, we recommend installing python via `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_. Many tutorials are available online to help you with this installation process (see for example `this one <https://www.youtube.com/watch?v=oHHbsMfyNR4>`_. During the installation, make sure to select "Add Miniconda to PATH".

.. note::
   **Miniconda** includes ``conda``, which allows you to create a dedicated Python environment for ``evpv-simulator``.
   If you're not using conda, consider alternative environment managers like ``venv``.
   Manual installation of all dependencies is also possible but **not recommended**.

Installation
------------

1. *(Optional but recommended)* Create a virtual environment with Python 3.12 using conda or venv.  
   As stated before, it is not mandatory but recommended to use a dedicated environment.  
   Here is an example using conda to create an environment named *evpv-env*:

   .. code-block:: bash

      conda create --name evpv-env python=3.12
      conda activate evpv-env

2. Install ``evpv`` as a Python package from the GitHub repository:

   .. code-block:: bash

      pip install git+https://github.com/evpv-simulator/evpv.git
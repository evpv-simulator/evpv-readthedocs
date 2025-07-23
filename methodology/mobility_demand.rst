Mobility Demand
===============

The first modelling step simulates daily commuting patterns by partitioning the region of interest into traffic zones and applying a so-called spatial interaction model (by default, a production-constrained gravity model is used but other models are available). It then estimates daily travel distances per zone using routing, forming the foundation for charging demand calculations.

Zoning: Divide the urban area into $Z$ Traffic Zones. For each zone $z$, collect:

$P_{z}$: residential population.

$W_{z}$: workplace proxy (e.g., employment count).

$O_{z}$: POI proxy.

Vehicle Allocation:

.. math::
N_{z} = \mathrm{round}\Bigl(P_{z} \cdot \frac{N_{\mathrm{EV}}}{\sum_{k}P_{k}}\Bigr)

with $N_{\mathrm{EV}}$ the total EV fleet.

Trip Distribution:

.. math::
T_{ij} = N_{i} \frac{W_{j} \exp(-\beta d_{ij})}{\sum_{k}W_{k} \exp(-\beta d_{ik})}

$d_{ij}$: network distance (or Euclidean$\times$circuity).

$\beta$ : distance-decay parameter:

.. math::
\beta = \alpha \sqrt{\frac{1}{S}} ,.

$S$: average zone surface; $\alpha$: calibration constant.

Distance Computation :

.. math::
D_{i}^{\mathrm{mob}} = \sum_{j} T_{ij} d_{ij}

which is converted into energy demand in the next step.
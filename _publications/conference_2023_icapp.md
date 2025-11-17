---
title: "Indirect Field Reconstruction and Sensor Positioning in Circulating Fuel Reactors using Data-Driven Model Order Reduction"
collection: publications
category: conferences
permalink: /publication/conference_2023_icapp
excerpt: 'This paper presents the application of indirect reconstruction and sensor placements methods for state reconstruction in a Molten Salt Reactor.'
date: 2023-04-01
venue: 'ICAPP 2023 - International Conference on Advances in Nuclear Power Plants'
authors: A. Cammi, Stefano Riva, C. Introini, L. Loi, E. Padovani.
---

*Authors*: A. Cammi, Stefano Riva, C. Introini, L. Loi, E. Padovani.

**Example of Implementation**:
- [pyforce tutorial](https://github.com/Steriva/ROSE-pyforce/blob/development/docs/Tutorials/Advanced/04_indirect_reconstruction.ipynb)
- [Paper Implementation - Direct Reconstruction](https://github.com/Steriva/phd-thesis-code/tree/928735bc90192417393ade88089362658c5f98c1/Notebooks/Chapter3/BoundarySensing)
- [Paper Implementation - Indirect Reconstruction](https://github.com/Steriva/phd-thesis-code/tree/928735bc90192417393ade88089362658c5f98c1/Notebooks/Chapter4/BoundarySensing)

*Abstract:* The problem of sensor positioning and real-time estimation of non-observable fields is an open question in the nuclear sector, especially for what concerns advanced nuclear reactors. Those are complex engineering systems subjected to harsh environmental working conditions. For example, the Molten Salt Fast Reactor in its current proposed configuration will in the fast neutron spectrum using a liquid fuel homogeneously mixed with the coolant: this unique feature makes in-core measurements extremely difficult, as Circulating Fuel Reactors (CFRs) will not be designed to have internal structures to allow the placement of the instrumentation (contrary to commercial reactors such as LWRs). Given the lack of experience with CFRs, sensor positioning in the primary circuit is an unresolved problem, and the above issue implies that most of the core will be blind to sensors. Thus, the possibility of estimating the system state in the whole domain using a few local measurements has important implications in terms of safety, monitoring, control, and economics, both in the nominal operating conditions and in accidental situations. In the above context, the integrated Model Order Reduction (MOR) and Data Assimilation (DA) into a hybrid framework offers intriguing opportunities. The former allows compressing the prior knowledge about the system contained in mathematical models into low-dimensional forms, allowing its fast and reliable integration with experimental data using DA algorithms. This work discusses and applies novel integration methods of the Hybrid-Data Assimilation framework, based on the Generalized Empirical Interpolation and the Indirect Reconstruction algorithms, to a proposed concept of a CFR. The goal of this work is to identify the optimal sensor positioning within the reactor core and to assess the feasibility of reconstructing the thermal-hydraulic field, the neutron flux and the precursors’ concentration, starting from data on fuel temperature only taken from sparse locations in the core domain, in transient conditions. Furthermore, this work will also test the predictive capabilities of the discussed methods.

<figure style="text-align: center;">
  <img src="https://github.com/Steriva/phd-thesis-code/blob/928735bc90192417393ade88089362658c5f98c1/Notebooks/Chapter3/BoundarySensing/Media/OnlineReconstruction.gif?raw=true"
       width="1000"
       alt="ReconT">
  <figcaption><em>Figure 1: Reconstruction of the Temperature.</em></figcaption>
</figure>

<figure style="text-align: center;">
  <img src="https://github.com/Steriva/phd-thesis-code/blob/928735bc90192417393ade88089362658c5f98c1/Notebooks/Chapter4/BoundarySensing/Media/OnlineReconstruction_flux.gif?raw=true"
       width="1000"
       alt="ReconFlux">
  <figcaption><em>Figure 2: Reconstruction of the Neutron Flux from Temperature measurements.</em></figcaption>
</figure>

<figure style="text-align: center;">
  <img src="https://github.com/Steriva/phd-thesis-code/blob/928735bc90192417393ade88089362658c5f98c1/Notebooks/Chapter4/BoundarySensing/Media/OnlineReconstruction_U.gif?raw=true"
       width="1000"
       alt="ReconU">
  <figcaption><em>Figure 3: Reconstruction of the Velocity from Temperature measurements.</em></figcaption>
</figure>

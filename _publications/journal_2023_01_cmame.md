---
title: "Stabilization of Generalized Empirical Interpolation Method (GEIM) in presence of noise: A novel approach based on Tikhonov regularization"
collection: publications
category: journals
permalink: /publication/journal_2023_01_cmame
excerpt: 'This paper is about a stabilisation method for Generalized Empirical Interpolation Method (GEIM) in presence of noise.'
date: 2023-02-01
venue: 'Computer Methods in Applied Mechanics and Engineering'
paperurl: 'https://doi.org/10.1016/j.cma.2022.115773'
authors: C. Introini, S. Cavalleri, S. Lorenzi, Stefano Riva, A. Cammi
---

[Paper URL](https://doi.org/10.1016/j.cma.2022.115773)

Example of Implementation:
- [OpenFOAM-v6](https://ermete-lab.github.io/ROSE-ROM4FOAM/Tutorials/BuoyantCavity/problem.html)
- [pyforce](https://github.com/Steriva/ROSE-pyforce/blob/development/docs/Tutorials/02_eim_methods.ipynb)

*Authors*: C. Introini, S. Cavalleri, S. Lorenzi, Stefano Riva, A. Cammi

*Abstract:* The Empirical Interpolation Method (EIM), and its generalized version (GEIM), are non-intrusive, reduced-basis model order reduction methods hereby adopted and modified to address the problem of optimal placement of sensors and real-time estimation in thermo-hydraulics systems. These techniques have been used to extract the characteristic spatial modes of the system and select a set of points (or functionals) corresponding to the optimal locations for the sensors. Collecting experimental measurements in the available points allows the construction of an empirical interpolation of the fields employed to estimate the variable of interest. However, when these data are affected by noise, the (G)EIM loses its good convergence properties. In this context, stabilization techniques allow good field reconstruction even with noisy data. This work provides an alternative and effective solution to the problem of reconstructing the system state in the presence of experimental data affected by random noise by using the Tikhonov regularization technique. The developed methods have been tested on a simple thermo-fluid dynamics problem known as “two-sided lid-driven differentially heated square cavity”.

<figure style="text-align: center;">
  <img src='../../images/publications/trgeim_errors.png' width="1000" alt="ErrorComparison">
  <figcaption><em>Figure 1: Comparison of TR-GEIM errors.</em></figcaption>
</figure>

<figure style="text-align: center;">
  <img src='../../images/publications/trgeim_recons.png' width="1000" alt="Recon">
  <figcaption><em>Figure 2: Comparison of TR-GEIM reconstructions.</em></figcaption>
</figure>


---
title: "Multi-physics model bias correction with data-driven reduced order techniques: Application to nuclear case studies"
collection: publications
category: journals
permalink: /publication/journal_2024_amm
excerpt: 'This paper presents the use of TR-GEIM and PBDW for multi-physics model bias correction in nuclear applications.'
date: 2024-11-01
venue: 'Applied Mathematical Modelling'
paperurl: 'https://doi.org/10.1016/j.apm.2024.06.040'
authors: Stefano Riva, C. Introini, A. Cammi
---

[Paper URL](https://doi.org/10.1016/j.apm.2024.06.040)

*Authors*: Stefano Riva, C. Introini, A. Cammi

[Example of Implementation](https://github.com/Steriva/phd-thesis-code/tree/928735bc90192417393ade88089362658c5f98c1/Notebooks/Chapter5/LinearisedCoupling)

*Abstract:* Due to the multiple physics involved and their mutual and complex interactions, nuclear engineers and researchers are constantly working on developing highly accurate Multi-Physics models, focusing in particular on the core coupling of Neutronics and Thermal-Hydraulics. Nevertheless, the development of accurate and stable models remains a challenging task despite the advancements in computational hardware and software. This work investigates the possibility of combining the available mathematical model with data collected on physical systems, with a two-fold goal: improvement of the performance of the former from the computational point of view without sacrificing accuracy and performing model bias correction with the knowledge coming in real-time from the system. In particular, two Data-Driven Reduced Order Modelling techniques, the Generalised Empirical Interpolation Method and the Parametrised-Background Data-Weak formulation, are applied to literature benchmark nuclear case studies, as they were observed to be quite well suited for the chosen cases. The main goal of this work is to assess the possibility of using external data to perform model bias correction: starting from a purposefully less accurate, but computationally cheaper base model, then using high-fidelity data to update and correct the model efficiently. Indeed, the numerical results obtained in this paper are promising, confirming the feasibility of this approach to develop computationally cheap and accurate multi-physics models; furthermore, investigation of Data-Driven Reduced Order Modelling approach to nuclear industrial cases, in the context of model bias correction, is foreseen.


<figure style="text-align: center;">
  <img src='../../images/publications/amm_errors.png' width="1000" alt="Recon">
  <figcaption><em>Figure 1: Comparison of the reconstruction error.</em></figcaption>
</figure>


<figure style="text-align: center;">
  <img src='../../images/publications/amm_OnlineReconstruction.gif' width="1000" alt="Recon">
  <figcaption><em>Figure 2: Online reconstruction contour plots.</em></figcaption>
</figure>


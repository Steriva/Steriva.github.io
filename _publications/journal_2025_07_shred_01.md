---
title: "Robust state estimation from partial out-core measurements with Shallow Recurrent Decoder for nuclear reactors"
collection: publications
category: journals
permalink: /publication/journal_2025_07_shred_01
excerpt: 'This paper presents the use of Shallow Recurrent Decoder for robust state estimation in nuclear reactors.'
date: 2025-09-01
venue: 'Progress in Nuclear Energy'
paperurl: 'https://doi.org/10.1016/j.pnucene.2025.105928'
authors: Stefano Riva, C. Introini, A. Cammi, J. Nathan Kutz
---

[Paper URL](https://doi.org/10.1016/j.pnucene.2025.105928)

*Authors*: Stefano Riva, C. Introini, A. Cammi, J. Nathan Kutz

[Example of Implementation](https://github.com/ERMETE-Lab/NuSHRED/tree/main/Code/P1)

*Abstract:* Reliable, real-time state estimation in nuclear reactors is of critical importance for monitoring, control and safety. It further empowers the development of digital twins that are sufficiently accurate for real-world deployment. As nuclear engineering systems are typically characterised by extreme environments, their in-core sensing is a challenging task, even more so in Generation-IV reactor concepts, which feature molten salt or liquid metals as thermal carriers. The emergence of data-driven methods allows for new techniques for accurate and robust estimation of the full state space vector characterising the reactor (mainly composed by neutron fluxes and the thermal-hydraulics fields). These techniques can combine different sources of information, including computational proxy models and local noisy measurements on the system, in order to robustly estimate the state. This work leverages the Shallow Recurrent Decoder (SHRED) architecture to estimate the entire state vector of a reactor from three, out-of-core time-series neutron flux measurements alone. Specifically, the Molten Salt Fast Reactor, in the geometry of the EVOL (Evaluation and Viability of Liquid Fuel Fast Reactor System) project, is demonstrated as a test case, with neutron flux measurements alone allowing for reconstruction of the 20 coupled field variables of the dynamics. This approach can further quantify the uncertainty associated with the state estimation due to its considerably low training cost on compressed data. The accurate reconstruction of every characteristic field in real-time makes this approach suitable for monitoring and control purposes in the framework of a reactor digital twin.

<figure style="text-align: center;">
  <img src='../../images/publications/shred2025_scheme_monoparam.png' width="1000" alt="Recon">
  <figcaption><em>Figure 1: Scheme of the SHRED architecture.</em></figcaption>
</figure>


| Fast Flux | Temperature | Velocity|
|-------|---|---|
| <img src="../../images/publications/shred2025flux1.gif" width="300"> | <img src="../../images/publications/shred2025T.gif" width="300"> | <img src="../../images/publications/shred2025U.gif" width="300"> |


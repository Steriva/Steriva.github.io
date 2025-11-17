---
title: "Verification and Validation of Shallow Recurrent Decoders for State Estimation in the DYNASTY facility"
collection: publications
category: conferences
permalink: /publication/conference_2025_nureth_dyn
excerpt: 'This paper presents a verification and validation of Shallow Recurrent Decoders for state estimation in the DYNASTY facility.'
date: 2025-09-01
venue: '21st International Topical Meeting on Nuclear Reactor Thermal Hydraulics (NURETH-21)'
authors:  Stefano Riva, A. Missaglia, C. Introini, J. N. Kutz, A. Cammi,
---

*Authors*: Stefano Riva, A. Missaglia, C. Introini, J. N. Kutz, A. Cammi,

**Example of Implementation**:
- [Verification Parametric](https://github.com/ERMETE-Lab/NuSHRED/blob/main/Code/P3/01_shred_verification_parametric.ipynb)
- [Validation Parametric](https://github.com/ERMETE-Lab/NuSHRED/blob/main/Code/P3/02a_shred_validation_parametric.ipynb)
- [Validation Prediction](https://github.com/ERMETE-Lab/NuSHRED/blob/main/Code/P3/02b_shred_validation_forecasting.ipynb)

*Abstract:* The Shallow Recurrent Decoder networks are a novel paradigm recently introduced for state estimation, combining sparse observations with high-dimensional model data. This architecture features important advantages compared to standard data-driven methods including: the ability to use only three sensors (even randomly selected) for reconstructing the entire dynamics of a physical system; the ability to train on compressed data spanned by a reduced basis; the ability to measure a single field variable (easy to measure) and reconstruct coupled spatio-temporal fields that are not observable and minimal hyper-parameter tuning. This approach has been verified on different test cases within different fields including nuclear reactors, even though an application to a real experimental facility, adopting the employment of in-situ observed quantities, is missing. This work aims to fill this gap by applying the Shallow Recurrent Decoder architecture to the DYNASTY facility, built at Politecnico di Milano, which studies the natural circulation established by internally heated fluids for Generation IV applications, especially in the case of Circulating Fuel reactors. The RELAP5 code is used to generate the high-fidelity data, and temperature measurements extracted by the facility are used as input for the state estimation. The results of this work will provide a validation of the Shallow Recurrent Decoder architecture to engineering systems, showing the capabilities of this approach to provide and accurate state estimation.


| **Case**                  | **Visualization**                                             |
|-----------------------------|-------------------------------------------------------------|
| **Parametric Verification** | <img src="https://github.com/ERMETE-Lab/NuSHRED/blob/main/media/P3/ParametricVerification.gif?raw=true" width="400"> |
| **Parametric Validation**   | <img src="https://github.com/ERMETE-Lab/NuSHRED/blob/main/media/P3/ParametricValidation.gif?raw=true" width="400">   |
| **Prediction Validation**   | <img src="https://github.com/ERMETE-Lab/NuSHRED/blob/main/media/P3/PredictionValidation.gif?raw=true" width="400">   |

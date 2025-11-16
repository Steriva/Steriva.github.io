---
title: "pyforce"
excerpt: "A Python package for data-driven reduced-order modelling of multiphysics problems<br/><img src='../../images/immy_pyforce2.png' width='700'>"
collection: projects
---

**pyforce** is a Python framework for **data-driven reduced-order modelling (DDROM)**, developed within the **ERMETE Lab, Politecnico di Milano**, for applications to complex **multi-physics problems**, with a strong focus on **nuclear engineering**.

<p align="center">
  <img src='../../images/immy_pyforce2.png' width="1000" alt="pyforce logo">
</p>

The package is part of the broader **ROSE** project (Reduced Order modelling with data-driven techniques for multi-physics problems), which aims to reduce the computational complexity of large-scale models, identify optimal sensor locations, and integrate experimental measurements to improve physical predictions.

---

## Description

pyforce provides a unified environment for applying modern reduced-order modelling techniques to simulation data.
Version 1.0.0 introduces a major redesign of the codebase: instead of relying on finite-element environments, it now uses **pyvista** for mesh handling, integrals and data import, and stores fields as **NumPy arrays**.
This makes the framework solver-agnostic and compatible with **any tool capable of exporting VTK files**.

The general workflow is divided into:

- **Offline phase**: dimensionality reduction, extraction of a reduced basis, and optimal sensor placement.
- **Online phase**: data assimilation, reconstruction of system states, and estimation of non-observable fields.

The framework gathers several algorithms used in reduced-order modelling and data assimilation, including:

- Singular Value Decomposition and Proper Orthogonal Decomposition
- (Generalised) Empirical Interpolation Method, with optional regularisation
- Parameterised-Background Data-Weak formulation
- SGreedy algorithm for optimal sensor placement
- Indirect reconstruction techniques for unobserved fields

These tools have been successfully applied to fluid dynamics, thermal–hydraulics, magnetohydrodynamics, and reactor physics problems.

---

## Tutorials and Documentation

Detailed documentation, introductory guides, and a growing set of tutorials are available online.
They cover the basic concepts of SVD/POD, GEIM, sensor placement, data assimilation, and applications to both fluid-dynamics and neutronics case studies, with examples for training ROMs and reconstructing physical fields.

---

## Authors

pyforce is developed and maintained at the **Nuclear Reactors Group – ERMETE Lab** by
**Stefano Riva**, under the supervision of **Dr. Carolina Introini** and **Prof. Antonio Cammi**.

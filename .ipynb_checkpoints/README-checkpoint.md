# Drizzle_Dynamics_summer2026

Physics-informed machine learning for cloud microphysics and cloud parameterization.

## Project Overview

Cloud and climate models cannot explicitly represent every individual cloud droplet within a model grid box. Instead, they rely on bulk microphysics parameterizations that statistically represent the collective behavior of cloud particles. One important component of these schemes is the representation of hydrometeor sedimentation (fall speeds), which strongly influences cloud lifetime, precipitation formation, and vertical transport.

Traditional bulk microphysics schemes, such as MG2 and PUMAS, make several simplifying assumptions, including analytic droplet size distributions and power-law relationships for particle fall speeds. In this project, we explore whether physics-informed machine learning can improve the representation of warm-cloud sedimentation processes and bulk fall speeds.

Our goal is to develop ML-based parameterizations using cloud droplet size distribution (DSD) data and atmospheric state variables while preserving physical consistency. We aim to compare traditional physical parameterizations with data-driven approaches and investigate how ML models can be integrated “online” within atmospheric models.

To provide a controlled testing framework, we will explore idealized modeling configurations such as SCAM or KiD and analyze LES/model-generated warm-cloud datasets to study droplet statistics, sedimentation behavior, and microphysical relationships.

## Goals
- Understand cloud microphysics and bulk parameterization assumptions
- Explore cloud droplet size distribution (DSD) relationships
- Investigate sedimentation and particle fall-speed processes
- Analyze SCM atmospheric model output
- Develop physics-informed ML-based parameterization ideas
- Compare traditional physical parameterizations with ML representations
- Explore online vs offline evaluation of ML microphysics schemes
  

## Team

- Marcus Van Lier-Walqui
- Kaitlyn Loftus
- Arthur Hu
- Pappu Paul
- Jacob Hahn
- Ibrahim Ahmed

## Repository Structure
Cooming soon
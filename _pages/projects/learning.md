---
layout: single
permalink: /ml/
title: "Machine learning + Stochastic optimization"
excerpt: "ml"
classes: wide
---

Engineering design approaches that combine simulations & artificial intelligence are powerful tools for characterizing bio-physical and engineering phenomena.
This is because the data generated from high-fidelity simulations reside in high-dimensional spaces, which renders analysis, and in turn synthesis of designs, harder. Machine learning approaches, which discover patterns
purely from data, are then useful to infer mechanisms underlying bio-physical phenomenon and make meaningful predictions to inform rational engineering design.
{: style="text-align: justify;"}

<!--
- UQ (statistical), CMAes
- Deep learning
- Elastica deep RL
- Heart data etc.
-->

## Statistical learning for inverse-design
We coupled our simulations with black-box stochastic optimization techniques (CMAes) for inverse-design, illustrated below via the example of snake whose gait we optimize (via dynamical forces) for maximal forward locomotion speeds. CMA has a rich history of success in such problems---hence it is an integral part of the course that I developed and teach at UIUC.
{: style="text-align: justify;"}

Additionally, we adopted Bayesian MCMC techniques in an elasto-hydrodynamics model (where an elastic material interacts with a fluid around it, typical in microfluidic settings) to infer unknown elastic material properties given noisy velocity measurements. MCMC not only correctly infers parameter distributions, but also quantifies uncertainty to make meaningful predictions for unseen data.
{: style="text-align: justify;"}


## Deep learning
To be updated.

## Reinforcement learning
To be updated.

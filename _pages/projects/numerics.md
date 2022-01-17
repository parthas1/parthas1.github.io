---
layout: single
permalink: /algorithms/
title: "Numerical algorithms"
excerpt: "numerics"
classes: wide
---

<!--
- Flow algorithms (Stokes, RVM, turubulent, inviscid)
- Soft matter + coupling
- Elastica + DEM + Collision
 -->

## Flow numerics for forward- and inverse-design
Engineering design approaches that combine artificial intelligence and simulations are powerful tools for the characterization of fluid-mechanic phenomena in biology as well as in engineering. In this context, numerical solvers face many challenges. Algorithmically they must exhibit controllable accuracy, flexibility and adaptivity, while
also being amenable to efficient parallelization when mapped onto modern computer architectures.
{: style="text-align: justify;"}

We developed scalable numerics that allow for the seamless integration between artificial intelligence techniques such as evolutionary optimization or reinforcement learning and large scale flow simulations. The solvers span fluid dynamics across scales, from viscous Stokes-flow to inviscid regimes.
{: style="text-align: justify;"}

## Elastic structure and flow interaction
Soft, elastic and compliant structures immersed in flows are ubiquitous
in engineering and biology, especially in soft robotics, bio-medical and
microfluidic devices. Accurate, versatile solvers are then key to dissect
physical mechanism and design solutions in the application domains above.
{: style="text-align: justify;"}

Towards this, we developed flexible numerical algorithms that can capture
the interaction between rigid and elastic bodies with flow, and other multiphysics
phenomenon, such as temperature gradient effects. We are currently in the process of
scaling up the algorithm to enable higher resolutions that include 10k elastic bodies.
{: style="text-align: justify;"}

## Soft filament dynamics
From bridges and DNA to shoelaces, the ubiquity of elastic rods or filaments
plays an important role in everyday life. We developed numerics for the simulation
of such 3D soft filaments accounting for all modes of deformation.
We then coupled these soft-filaments to discrete-element methods for simulating realistic environments that
involve other elastic and rigid bodies. We capture the coupling using scalable,
(optimal)linear-complexity collision algorithms, customized for our soft-body simulations. The resulting algorithm seamlessly integrates with evolutionary optimization,
reinforcement learning and model-based control methods.
{: style="text-align: justify;"}

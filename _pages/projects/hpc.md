---
layout: single
permalink: /hpc/
title: "High-performance computing"
excerpt: "hpc"
classes: wide
---

<!--
- Elastica
- Fluid : 3D climate solver for now, replace with Mechanica later
- CUDA
-->

Modeling physical phenomenon with high-fidelity often requires large and complex
simulations that expend massive computing effort which maybe too immense
for a single computer-chip to process. Thankfully, modern computer architectures
are outfitted to perform parallel computations by offer hierarchical layers
of parallelism (instruction-level + data-level + thread-level + node-level).
High-performance computing (HPC) strategies are key to fully leverage these
parallelism layers to accelerate time-to-solutions, which then enables innovative tools for
scientific discovery and rational engineering design.
{: style="text-align: justify;"}

## High-performance soft filament simulations
HPC simulations of soft filaments are challenging because naively employing
conventional strategies (e.g. parallel loops) can hurt performance.
We enabled HPC soft filament simulations by first rethinking the per-processor
memory layout by converting AoS to SoA layout, blocking, aligning and padding and using ghost
elements to aggregate multiple, separate rods into a larger, cohesive unit.
These lead to high-throughput, spatially-local, homogeneous data while minimizing
latency-induced bottlenecks due to indirections and hence enables instruction
and data-parallel performance (which we achieved by using explicit SIMD intrinsic
instructions). These steps are performed by a
compile-time code-generation architecture (called **blocks**, implemented in
standard-compliant`C++`) which we designed for producing efficient per-core modular,
Lagrangian data-structures.
{: style="text-align: justify;"}

We build upon this per-core performance afforded by blocks and utilize thread and node-parallel layers synergistically, by distributing multiple blocks across processors, either in a shared-memory or distributed-memory setting. These strategies result in a versatile and efficient Cosserat rod solver
that incorporates a variety of environmental effects, and that can scale from desktops to supercomputing clusters.
{: style="text-align: justify;"}


## High-performance flow simulations
While HPC strategies in soft filament simulations focused on efficient memory layouts for
vectorized computations, flow simulations have a different challenge---here we
need to ensure spatio-temporal locality of data since we deal with 3D grids. Achieving
this requires careful consideration of the data-access patterns by utilizing blocking/tiling,
loop fusion, loop unrolling and then adding vectorization and parallelism atop it.
We utilized these strategies to build an efficient flow solver that is performant
and scales well on distributed super-computers.
{: style="text-align: justify;"}


## Convolutional Neural networks
The advent of general-purpose GPUs have not revolutionized not only physical
simulations, but also machine learning (ML). Image detectors/classifiers/generators
, one amongst the many successes of modern ML, often use deep-neural networks
with convolution layers for sub-sampling and transforming input data. These convolutions
are expensive, and are ideal for acceleration by HPC strategies.
{: style="text-align: justify;"}

We implemented CUDA kernels for optimizing the convolution passes of a LeNet-5-like architecture
for detection clothes in the MNIST fashion dataset. By using strategies such as
loop tiling, Unrolled shared-memory GEMM, register-assisted convolution and
half-precision arithmetic, after iterative profile-based optimization (using Nsight
and roofline), we obtained 5x better performance (compared to naively written GPU code).
{: style="text-align: justify;"}

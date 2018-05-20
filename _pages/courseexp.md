---
layout: single
permalink: /coursework/
title: "Course Projects"
excerpt: "A sample of projects done as part of the curriculum @ UIUC"
header:
  overlay_image: /assets/images/course/drafting_inverted.jpg
  image_description: "Viscous streaming from multitudes"
  caption: "Inverted drafting from flags. Credits: [**Leif Ristroph & Jun Zhang, NYU**](https://math.nyu.edu/~ristroph/)"
last_modified_at: 2018-05-18T08:41:35-04:00
---

# A spectral-element solver for the incompressible Navier-Stokes equations with thermal coupling

## Instructor : [Prof. Paul F. Fischer][1], [CS555][2]

[1]:http://fischerp.cs.illinois.edu/
[2]:https://relate.cs.illinois.edu/course/cs555-s18/

We constructed a (fast!) QN-Q(N-2) spectral element solver for the Navier-Stokes
equations and coupled it to the energy equations through the Boussinesq
approximation---aiming to predict the critical Rayleigh number for the Rayleigh-
Benard convection problem. We presented a poster in the end that briefly describes
our solver capabilities---I have attached the same below:
{: style="text-align: justify;"}

<figure class="align-center">
  <img src="{{site.url}}{{site.baseurl}}/assets/images/course/cs555_poster.jpg" alt="spec_elem">
  <figcaption></figcaption>
</figure>

With 50 order polynomials and a single element we could predict the critical
Rayleigh number to the first two decimal digits. Here's an animation of all
the fields as they evolve, with periodic boundary conditions on the side walls. You
can see the motionless flow tend to the (steady) convective roll solution.
{: style="text-align: justify;"}

<figure class="align-center">
  <img src="{{site.url}}{{site.baseurl}}/assets/images/course/cs555_rbc.gif" alt="spec_elem">
  <figcaption>Rayleigh-Benard convection at Ra=2500</figcaption>
</figure>

We could also realize a case with the same setup, but with the top wall moving with
an unit velocity to the right. In this case we get a mixed Rayleigh-Benard,
Kelvin-Helmoltz type instability:
{: style="text-align: justify;"}

<figure class="align-center">
  <img src="{{site.url}}{{site.baseurl}}/assets/images/course/cs555_khrbc.gif" alt="spec_elem2">
  <figcaption>Rayleigh-Benard convection with moving top plate at Re=20, Ra=10000</figcaption>
</figure>

Based on the same infrastructure we also constructed a solver for the Stokes equations
(Re tending to zero), but using P2-P1 (Taylor-Hood) finite elements. A picture of
the flow due to a cylinder above a moving wall (Wannier flow) is shown below:
{: style="text-align: justify;"}

<figure class="align-center">
  <img src="{{site.url}}{{site.baseurl}}/assets/images/course/cs555_stokes.png" alt="spec_elem2">
  <figcaption>Numerical solution of Wannier-Stokes flow using Taylor-Hood elements</figcaption>
</figure>

# A steady Stokes-PDE solver based on Integral Equation methods

## Instructor : [Prof. Andreas Klöckner][3], [CS598APK][4]

[3]:https://mathema.tician.de/aboutme/
[4]:https://relate.cs.illinois.edu/course/cs598apk-f17/

I learnt to develop a numerical solver for the Stokes flow equations using an
integral equation formulation of the PDE, coupled with a subset of 'fast
algorithms'. Robust, fast and accurate numerical solutions for the stokes PDE can
be tricky, because it is 'coupled' via the incompressibility constraint, which upon
discretization leads to ill-conditioned systems (the FEM crowd have developed
many ways to overcome this---the most popular of which is using Taylor-Hood
elements). Using an integral equation formulation we obtain a 'double-layer'
representation (for the Neumann problem) for the PDE which leads to a second-kind
Fredholm equation. With some algebra, and using Nyström discretization, we get a
decoupled matrix-system that can be iteratively solved for. This system has a bounded
condition number (independent of the mesh size), is accurate (the errors we commit
are related only to finite-representation and quadrature) and extends itself to
higher order. Futhermore it requires discretizing only the boundaries (leading to
the appropriately named 'boundary element methods') and hence very robust. Apart
from the savings we get by not generating a volume-mesh in this case, we use a
subset of 'fast algorithms' that has linear run-time algorithmic complexity! IE methods
are hence very capable and useful in any numerical analyst's toolkit.
{: style="text-align: justify;"}

<figure style="width: 500px" class="align-center">
  <img src="{{site.url}}{{site.baseurl}}/assets/images/course/cs598_stokeslet.png" alt="dipole">
  <figcaption>The Stokeslet contribution from a moving cylinder</figcaption>
</figure>

# A 3-D quasi-compressible Navier-Stokes solver for the simulation of atmospheric phenomena

## Instructor : [Prof. Brian Jewett][5], [CSE566][6]

[5]:https://www.atmos.illinois.edu/~bjewett/
[6]:https://www.atmos.illinois.edu/~bjewett/atms502.html

I developed a 3-D nonlinear quasi-compressible flow solver using a combination of
higher-order finite-difference (FDM) and a piecewise-linear finite-volume method
(with Van-Leer reconstruction) for spatial discretization. Temporal discretization
was done using explicit and implicit treatment for the slow and fast-scale physics
terms via Strang splitting. To improve accuracy, grid staggering was employed.
Shared memory parallelism was achieved through OpenMP constructs. An equivalent
version for 2-D with Adaptive Mesh Refinement (AMR) capabilities was also implemented.
{: style="text-align: justify;"}

<figure class="align-center">
  <img src="{{site.url}}{{site.baseurl}}/assets/images/course/cse566_cleft.png" alt="cleft">
  <figcaption>A snapshot of a 3-D simulation of cold bubbles interacting with one another under the influence of gravity. A cleft and lobe instability develops on the cold-bubble front (a distinct wavelength of the instability is seen on the right bubble)</figcaption>
</figure>

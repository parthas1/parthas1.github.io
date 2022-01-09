---
layout: single
permalink: /research/
title: "Research Interests"
excerpt: "Fluid mechanics and FSI across scales"
header:
  overlay_image: /assets/images/research/rch_fpc.png
  image_description: "flowpastcylinder"
  caption: "Flow past a cylinder at Re=300"
last_modified_at: 2018-05-17T08:41:35-04:00
---

I'm passionate about fluid dynamics, across the length and time scales
they operate in - be it Stokes, intermediate or turbulent flows, and
concomitant applications. I'm interested in fluid physics, numerical
simulations of fluid flows—especially concerning fluid-structure interaction,
numerical algorithms, high performance and parallel computing, flow and
instability control, aeroacoustics and control and possibly applying learning
techniques in fluids. Thus the core of my present (and future) research is broadly
in applied math, HPC, theoretical and applied mechanics and dynamical system concepts.
{: style="text-align: justify;"}

# Flow-structure interaction

Simulating the physics of flow-structure interaction has been the focus of my work
in graduate school so far. I work with [Prof.Mattia Gazzola](http://mattia-lab.com/)
and use the remeshed Vortex Method (rVM) in simulating these flows. Shown below is
an animation of our simulation (including an impulsive start) of a simple flow past
a two dimensional body.
{: style="text-align: justify;"}

<figure class="align-center">
  <img src="{{site.url}}{{site.baseurl}}/assets/images/research/rch_fpc_anim.gif" alt="">
  <figcaption>Flow past a cylinder, Re=300.</figcaption>
</figure>

# Viscous Streaming
Oscillatory flows initiated by solid bodies in harmonic motions are immensely
rich in their dynamics. Low-amplitude oscillations of simple bodies lead to a
well-studied phenomenon called viscous streaming, and high amplitude motions
(with and without flow separation) are classified as Keulegan–Carpenter (KC)
flows. The non-linear nature of the Navier–Stokes equations leads to a significant
rectified (aka steady) component in the case of streaming, while higher modes kick
in for KC flows.
{: style="text-align: justify;"}

While the math (for streaming) has been set in stone for some time now, the physics
of streaming, in its varied form and function is IMHO, still elusive. I'm hunting
for these mechanics through two dimensional direct numerical investigations.
I am involved in scientific software development for fluid dynamics in the lab, working
on topics such as numerics, applied math, HPC, dynamical systems (Model reduction,
FTLE), programming, visualization and data analysis.
{: style="text-align: justify;"}

[Here's a poster about streaming](https://www.instagram.com/p/BcseNTon6VY/)
 <figure class="align-center">
  <img src="{{site.url}}{{site.baseurl}}/assets/images/research/placeholder.png" alt="">
  <figcaption>Viscous streaming from an ellipse.</figcaption>
</figure>

# Flow Control using ZNMF Devices
<!-- <h1 class="title"><img id="centerimg9" src="/images/websiteCollatedStreamlines.png"></h1><center><small>
 -->
<!-- The effect of a synthetic jet : (a) A stalled NACA0012 airfoil at AoA = 20°, (b) Actuating with the right set of parameters streamlines the body, image is a representative snapshot of the periodic dynamics and (c) The wrong set of parameters degrades the lift and stall performance
 -->
We stand to gain immensely by manipulating fluid flows - in ways more than
one can think of! An essential part of control is knowing the global dynamics
of the system - which is usually unavailable in complicated scenarios like flow
past a bluff, or for that matter, a streamlined body. Model order reduction comes
in handy - but understanding the basic flow dynamics is also insightful in the
task of achieving perfect flow control.
{: style="text-align: justify;"}

I investigated the dynamics of (un)controlled flow past a NACA 0012 airfoil at
moderate Reynolds numbers, ultimately to achieve separation control in turbomachines
(where separation is responsible for performance degradation) and mUAVs.
Control was achieved through ZNMF (Zero-Net Mass Flux) devices or synthetic
jets. Flows due to ZNMFs are closely related to viscous streaming/KC flows
because their origin is similar—they involve periodically oscillating structures
that manipulate surrounding fluid. This work with
[Prof. Shyama Prasad Das](http://mech.iitm.ac.in/Faculty/spdas/home.php) at
[IIT Madras](https://www.iitm.ac.in/) involved us carrying out a parametric study
to come up with a phase space relating the jet characteristics with the load and
separation performance. Based on flow characteristics, we could see that properly
aligned ZNMF devices assists in separation control by imparting high momentum fluid
into the freestream when blowing and removing low momentum fluid near the walls while
sucking. They use the inherent energy in the freestream flow to achieve desired control.
We also tried non-harmonic oscillations, but it didn't have too much of an impact
in the regime that we were operating in.
{: style="text-align: justify;"}

<figure class="align-center">
  <img src="{{site.url}}{{site.baseurl}}/assets/images/research/znmf_stream.png" alt="">
  <figcaption>The effect of a synthetic jet : (a) A stalled NACA0012 airfoil at AoA = 20°,
  (b) Actuating with the right set of parameters streamlines the body and (c) The wrong set
  of parameters degrades the lift and stall performance.</figcaption>
</figure>

Due credits to Prof. Mattia for developing the core of the FSI-rVM code, which
I have used to simulate the results shown in much of this website
{: .notice--info}
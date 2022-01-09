---
layout: single
permalink: /projects/physics/
title: "Flow & Soft systems"
excerpt: "physics"
classes: wide
streaming_gallery:
  - url: /assets/images/projects/streaming_cover.png
    image_path: /assets/images/projects/streaming_cover.png
    alt: "streaming_cover"
    title: "Streaming response from a cylinder (top) and a bullet (below) designed for fast transport"
  - url: /assets/images/projects/3D_streaming.png
    image_path: /assets/images/projects/3D_streaming.png
    alt: "3D_streaming"
    title: "Streaming response from a sphere"
soft_gallery:
  - url: /assets/images/projects/resonance.png
    image_path: /assets/images/projects/resonance.png
    alt: "solid_resonance"
    title: "Flows can also setup resonances within the solid!"
  - url: /assets/images/projects/ball_in_vortex_compressed.gif
    image_path: /assets/images/projects/ball_in_vortex_compressed.gif
    alt: "ball_vortex"
    title: "A soft cylinder placed in a Taylor–Green vortex"
  - url: /assets/images/projects/flagella.png
    image_path: /assets/images/projects/flagella.png
    alt: "flagella"
    title: "Simulations + experiments of a compliant motile swimmer in viscous flow"
filaments_gallery:
  - url: /assets/images/projects/wings.png
    image_path: /assets/images/projects/wings.png
    alt: "wings"
    title: "Modeling a feathered-wing using filamentous rods"
---

<!-- # Flow-structure interaction

Simulating the physics of flow-structure interaction has been the focus of my work
in graduate school so far. I work with [Prof.Mattia Gazzola](http://mattia-lab.com/)
and use the remeshed Vortex Method (rVM) in simulating these flows. Shown below is
an animation of our simulation (including an impulsive start) of a simple flow past
a two dimensional body.
{: style="text-align: justify;"} -->

<!-- <figure class="align-center">
  <img src="{{site.url}}{{site.baseurl}}/assets/images/research/rch_fpc_anim.gif" alt="">
  <figcaption>Flow past a cylinder, Re=300.</figcaption>
</figure> -->

## Viscous Streaming
Viscous streaming arises when an immersed body undergoes small-amplitude oscillations in a viscous fluid, and it is perhaps the most efficient way to use inertia at the microscale. Almost nothing is known about it, beyond simple shapes such as cylinders or spheres. We investigated viscous streaming beyond classical settings for the rational manipulation of flow topology, through regulated variation of object geometry. We showcased its use in transport devices (such as a micro-robot delivering drugs
to a target cell) and in microfluidic trapping/clearing devices.
{: style="text-align: justify;"}

{% include gallery id="streaming_gallery"%}

### More information
- Bhosale^, Vishwanathan^,  **Tejaswin Parthasarathy**, Juarez, Gazzola.<br>
[Multi-curvature viscous streaming: flow topology and particle manipulation](http://mattia-lab.com/wp-content/uploads/2021/11/yb_gv_tp_gJ_gm_2021.pdf), arXiv:2111.07184.
{: style="font-size:smaller"}

- Chan, Bhosale, **Tejaswin Parthasarathy**, Gazzola.<br>
[Three-dimensional geometry and topology effects in viscous streaming](https://mattia-lab.com/wp-content/uploads/2022/01/fkc_yb_tp_mg_2022.pdf), Journal of Fluid Mechanics, 2022.
{: style="font-size:smaller"}

- Bhosale, **Tejaswin Parthasarathy**, Gazzola.<br>
[Shape curvature effects in viscous streaming](http://mattia-lab.com/wp-content/uploads/2020/09/yb_tp_mg_2020.pdf), Journal of Fluid Mechanics, 2020.
{: style="font-size:smaller"}

- **Tejaswin Parthasarathy**, Chan, Gazzola.<br>
[Streaming-enhanced flow-mediated transport](http://mattia-lab.com/wp-content/uploads/2019/09/TP_FKC_MG_JFM_2019.pdf), Journal of Fluid Mechanics, 2019. [\_Cover\_](http://mattia-lab.com/wp-content/uploads/2019/10/00221120_878.pdf)
{: style="font-size:smaller"}

## Soft systems immersed in flows
Soft, elastic and compliant structures immersed in flows are ubiquitous
in engineering and biology, and especially in soft robotics, bio-medical and
microfluidic devices. To dissect the mechanisms underlying such systems, we
have analyzed archetypes of soft structure–flow interaction, using theoretical
and numerical methods. The insights gained potentially pave way for novel means of
flow manipulation in applications such as drug-delivery via compliant robotic devices.
{: style="text-align: justify;"}

{% include gallery id="soft_gallery" %}

### More information

- An [online sandbox](https://gazzolalab.github.io/parallel_slab_sandbox/) I made to investigate the dynamics of an archetypal immersed soft structure.
{: style="font-size:smaller"}

- **Tejaswin Parthasarathy**, Bhosale, Gazzola.<br>
[A hyperelastic oscillatory Couette system](http://mattia-lab.com/wp-content/uploads/2021/12/tp_yb_mg_2021.pdf), arXiv:2011.09453.
{: style="font-size:smaller"}

- **Tejaswin Parthasarathy**^, Bhosale^, Gazzola.<br>
[A remeshed vortex method for mixed rigid/soft body fluid–structure interaction.](http://mattia-lab.com/wp-content/uploads/2021/07/yb_tp_mg_JCP_2021.pdf), Journal of Computational Physics, 2021.
{: style="font-size:smaller"}

- Zhang, Chan, **Tejaswin Parthasarathy**, Gazzola.<br>
[Modeling and simulation of complex dynamic musculoskeletal architectures](http://mattia-lab.com/wp-content/uploads/2019/11/xz_fkc_tp_mg_2019.pdf), Nature Communications, 2019.
{: style="font-size:smaller"}

## Filamentous soft creatures
From bridges and DNA to shoelaces, the ubiquity of elastic rods or filaments plays an important role in everyday life. We developed a numerical model for the simulation of soft filaments deforming in three-dimensional space, and accounting for all possible deformation modes, bending, twisting, shearing and stretching at every cross-section. These assemblies of soft tods are able to interact with the environment via models of muscular activity, sensory feedbacks, self-contact, surface friction and hydrodynamics, thus providing a physically accurate virtual playground to inquire into the functioning of complex muscular and robotics architectures.
{: style="text-align: justify;"}

{% include gallery id="filaments_gallery" %}

### More information

- An [online sandbox](https://gazzolalab.github.io/kinematic_snake_sandbox/snake_sandbox.html) I made to investigate limbless locomotion by soft snakes.
{: style="font-size:smaller"}

- Zhang, Naughton, **Tejaswin Parthasarathy**, Gazzola.<br>
[Friction modulation in limbless, three-dimensional gaits and heterogeneous terrains](http://mattia-lab.com/wp-content/uploads/2021/10/xz_nn_tp_mg_2021.pdf), Nature Communications, 2021.
{: style="font-size:smaller"}

- Naughton, Sun, Tekinalp, **Tejaswin Parthasarathy**, Chowdhary, Gazzola.<br>
[Elastica: A compliant mechanics environment for soft robotic control](http://mattia-lab.com/wp-content/uploads/2021/04/nn_js_at_tp_gc_mg_2021.pdf), IEEE Robotics and Automation Letters, 2021.
{: style="font-size:smaller"}

- Chang, Halder, Shih, Tekinalp, **Tejaswin Parthasarathy**, Gribkova, Chowdhary, Gillette, Gazzola, Mehta.
[Energy shaping control of a CyberOctopus soft arm](http://mattia-lab.com/wp-content/uploads/2021/02/hsg_uh_mg_pm_2020.pdf), IEEE Conference on Decision and Control (CDC), 2020.
{: style="font-size:smaller"}

- Zhang, Chan, **Tejaswin Parthasarathy**, Gazzola.<br>
[Modeling and simulation of complex dynamic musculoskeletal architectures](http://mattia-lab.com/wp-content/uploads/2019/11/xz_fkc_tp_mg_2019.pdf), Nature Communications, 2019.
{: style="font-size:smaller"}


<!-- ## Flow Control using ZNMF Devices
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
</figure> -->

---
layout: page 
title: Research Interests 
date:   2017-09-10 12:00:00
order: 4
---

<p><small>	I'm passionate about fluid dynamics, across the length and time scales they operate in - be it Stokes, intermediate or turbulent flows, and concomitant applications. I'm really interested in fluid physics, Numerical simulations of Fluid flows, Numerical Algorithms, High Performance - Parallel Computing, Flow and Instability Control, Aeroacoustics and Sound Control and possibly applying learning techniques in fluids. Thus the core of my present (and future) research is broadly in applied math, HPC, theoretical and applied mechanics and dynamical system concepts.</small></p>

<p><small>	Here are some instances of stuff that I have worked/ am working on:</small></p>
<br>
<h3><u> Viscous Streaming </u></h3>
<h1 class="title"><img id="centerimg" src="/images/profile.jpg"></h1>
<p></p>
<p><small>	Oscillatory flows initiated by solid bodies in harmonic motions are immensely rich in their dynamics. Low amplitude oscillations of simple bodies lead to a well studied phenomenon called viscous streaming, and high amplitude motion (with and without flow separation) are classified as Keulegan-Carpenter (KC) flows. The non-linear nature of the Navier Stokes equations leads to a significant rectified component in case of streaming, while higher fundamental modes kick in for KC flows.

While the math (for streaming) has been set in stone for some time now, the physics of streaming in varied form and function, is IMHO, is still in part elusive. I'm hunting for the mechanics through two dimensional direct numerical investigations, guided by <a href="http://mattia-lab.com/">Prof. Mattia Gazzola</a>. <a href="http://mattia-lab.com/">We</a> use Remeshed Vortex Method(RvM) for the same, which has been used for Fluid Structure Interaction (FSI) problems in the past. I'm the principal scientific and software developer for fluid dynamics in the lab - thus I am comfortable in topics involving numerics, applied math, HPC, dynamical systems (Model reduction, FTLE), programming, visualization & data analysis. You can get a sense of what we are working towards by glancing through our <a href="https://parthas1.github.io/publications/">DFD abstracts</a>. We're also coming out with publications soon!</small></p>  
<br>
<h3><u> Flow Control using ZNMF Devices </u></h3>
<h1 class="title"><img id="centerimg9" src="/images/websiteCollatedStreamlines.png"></h1><center><small>The effect of a synthetic jet : (a) A stalled NACA0012 airfoil at AoA = 20°, (b) Actuating with the right set of parameters streamlines the body, image is a representative snapshot of the periodic dynamics and (c) The wrong set of parameters degrades the lift and stall performance</small></center>
<p></p>
<p><small>	We stand to gain immensely by manipulating fluid flows - in ways more than one can think of! An essential part of control is knowing the global dynamics of the system - which is usually unavailable in complicated scenarios like flow past a bluff, or for that matter, a streamlined body. Model reduction comes in handy - but understanding the basic flow dynamics is also insightful in the task of achieving perfect flow control. 

Part of my bachelor's thesis went into investigating the dynamics of (un)controlled flow past a NACA 0012 airfoil at moderate Reynolds numbers, ultimately to achieve separation control in turbomachines (where separation is notoriously responsible for astounding performance degradation) and mUAVs. Control was achieved through ZNMF (Zero-Net Mass Flux) devices or synthetic jets, a concept that is an attractive option for active control. Flows due to ZNMFs are closely related to viscous streaming/KC flows because their origin is similar, although there are marked differences as well. This work with <a href="http://mech.iitm.ac.in/Faculty/spdas/home.php">Prof. Shyama Prasad Das</a> at <a href="https://www.iitm.ac.in/">IIT Madras</a>, involved us carrying out a parametric design analysis, and we could come up with a phase space relating the jet characteristics with the load and separation performance. Based on flow characteristics, we could see that by imparting alternatively sucking in low momentum fluid near the walls and injecting high momentum fluid, when aligned right, the ZNMF devices offers can assist in performance control. Utilizing the inherent energy in the flow modes is also one more way that we can think about the action of these nifty devices. Actuating with multiple modes, say like using a quick return mechanism instead of the sinusoidal mechanism, didn't have too much of an impact in the regime that we were operating in. 

We presented an aspect of the project at the 15th Asian Congress of Fluid Mechanics in Malaysia and the entire study can be found in our journal publication linked <a href="https://parthas1.github.io/publications/">here</a>.</small></p>
<br>
<h3><u> Virtual Development of a Robotic Arm</u></h3>
<h1 class="title"><img id="centerimg" src="/images/robot.png"></h1>
<center><small> The modeled robot in the ADAMS environment</small></center>

<h1 class="title"><img id="centerimg" src="/images/controlled.jpg"></h1>
<center><small> Results of the simulation carried out with and without using appropriate control systems</small></center>
<p></p>
<p><small>	Developing intuition for physical concepts is something crucial in a student's learning process. When I was pursuing my undergraduate, I did not have immediate access to fancy modules or learning kits, and learning by doing/exploring was instrumental in developing my skill set. This was especially true for courses involving dynamics and controls - it was interesting to read about, but also frustrating to not understand and visualize how a conceptually simple (though mechanically rich) four bar mechanism can be scaled up to manufacture robotic arms. Having a framework for such a conceptual visualization would have been nice. 

In pursuit of this goal, myself, <a href="https://sites.google.com/site/vigneshsrinivasaragavan/"> Vignesh </a> and <a href="https://home.iitm.ac.in/sspandian/"> Prof. Soundarapandian </a> at IITM, reverse engineered, modeled and & drafted a path planning algorithm for a defunct robotic arm. Our goal was to make use of such defunct robotic arms, lying in disuse in many institutes across Chennai, and (i) retrofit them for uses such as simple manoeuvring and (ii) develop a framework for virtual robotic development in education. Using MATLAB, ADAMS and some VBA programming (for real-time database application), we could achieve a real-time virtual simulation of a robotic arm following a trajectory given by the end user. We also designed the control software for the aforesaid robotic arm, ensuring precise and accurate path adherence, with a far reaching goal of achieving orthopaedic surgery application.

Before moving on to other ventures, we arrived at a final design for retrofitting the arm to meet high degrees of precision and accuracy at affordable costs, with help from ABB, after an iterative design process. This project is now actively being carried out by a PhD student at IIT Madras. You can take a look at our initial publication at ICMME 2016, Shanghai <a href="https://parthas1.github.io/publications/">here</a>.</small></p>


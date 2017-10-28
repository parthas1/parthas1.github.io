---
layout: page 
title: Academic Projects 
date:   2017-09-10 12:00:00
order: 5
---

<h3> Graduate </h3>
<h3><u> A steady Stokes-PDE solver using Integral Equations Theory and Fast Algorithms </u></h3>
<h4> Instructor : <a href="https://mathema.tician.de/aboutme/">Prof. Andreas Kloeckner</a>, <a href="https://relate.cs.illinois.edu/course/cs598apk-f17/">CS598</a>, UIUC </h4>
<h1 class="title"><img id="centerimg" src="/images/dipole.png"></h1><center><small>The dipole kernel in evaluating the free-space Green's function for the 2-D Laplace equation (credits: Prof. Andreas Kloeckner)</small></center>
<p></p>
<p><small>	I am currenly developing a numerical solver in Python that can solve the linearized Navier Stokes equation (popularly known as the Stokes flow equations, for highly viscous fluids), using the Integral Equation version of the PDE, coupled with numerical techniques of Fast Algorithms. Using these techniques (such as the Fast Multipole Method (FMM)), it is possible to reduce the super-linear run time scaling of algorithms (a matrix-vector solve scales cubically) into a linear run time variant, using the low-rank properties of the fundamental PDE kernels! These tools are also amenable for easily generalizing to higher order, and thus offers amazing accuracy with less time to solution, which is not the case with other techniques, such as Finite Difference Methods. <br>
Numerical solutions to the Stokes PDE may seem like a nasty problem, mainly because it is am indefinite elliptic and coupled PDE, which on discretizing frequently leads to ill-conditioned systems. By transforming the Stokes PDE into the integral equations form, it is possible to obtain a representation, called the second kind Fredholm equation, which leads to a decoupled system that has a bounded condition number independent of the mesh size. Solutions to the Stokes PDE are then easily obtained using Fast Algorithm techniques.<br>
This solver adds on to existing infrastructure developed by <a href="https://github.com/inducer">Prof. Kloeckner</a> for such PDEs, and is targeted towards simulating complex geometries in Stokes flows. This ties nicely with my long-time research focus of applying streaming-based technologies to bio-hybrid systems enhance mixing, transport and drug-delivery applications to name a few. I also want to extend this to unsteady Stokes equations as future work.<br>
[<a href="/docs/stokespde.pdf">pdf</a>]
</small></p>
<p></p>
<h3><u> 3-D Navier-Stokes solver for simulation of atmospheric phenomena </u></h3>
<h4> Instructor : <a href="https://www.atmos.illinois.edu/~bjewett/">Prof. Brian Ford Jewett</a>, <a href="https://www.atmos.illinois.edu/~bjewett/atms502.html">ATMS502</a>, UIUC </h4>
<h1 class="title"><img id="centerimg" src="/images/cleft.png"></h1><center><small>A snapshot of a 3-D simulation of cold bubbles interacting with one another under the influence of gravity. You can see the cleft and lobe instability in the images</small></center>
<p></p>
<p><small>	I developed a 3-D nonlinear quasi-compressible flow solver using a combination of higher order finite difference (FDM) and a piecewise linear finite volume method (FVM) for spatial discretization. Explicit and implicit temporal treatment for different terms was also implemented, using Strang splitting. For adherence to conservation laws and accuracy, grid staggering was employed. Shared memory parallelism was done through OpenMP. An equivalent version for 2-D with Adaptive Mesh Refinement (AMR) capabilities was also implemented.<br>
[<a href="/docs/nfd.pdf">pdf</a>]
</small></p>
<p></p>
<h3><u> Spectral Methods in MATLAB </u></h3>
<h4> Instructor : <a href="http://fischerp.cs.illinois.edu/">Prof. Paul Fischer</a>, <a href="http://fischerp.cs.illinois.edu/tam470/">TAM470</a>, UIUC </h4>
<p><small>	I developed a similar, but scaled down version of a 2-D Navier Stokes solver in MATLAB in this course. I used higher order spectral methods, which offers amazing accuracy and resolution characteristics, with highly efficient and vectorized operators.</small></p>
<p><br></p>
<h3> Undergraduate </h3>
<h3><u> Quick solutions for inviscid flow past arbitrarily distributed circular cylinders </u></h3>
<h4> Instructor : <a href="https://apm.iitm.ac.in/fmlab/arul/"> Prof. Arul K Prakash</a>, AM5530, IITM </h4>
<h1 class="title"><img id="centerimg" src="/images/am5530Streamlines.png"></h1><center><small>Streamlines for uniform inviscid flow past a two cylinder system for 45° flow angle, with the ratio of radii being 2</small></center><p></p>
<p><small>	Analysis of inviscid flows are tractable using complex number theory, with suitable domain transformations. Such analyses gives an intuition to the user about the physics of fluids. Using Crowdy's <a href="http://wwwf.imperial.ac.uk/~dgcrowdy/_producer/PubFiles/Paper-15.pdf"> work</a>, I was able to reconstruct solutions for uniform oriented flows past a set of cylinders. This called for implementing numerical algorithms efficiently in MATLAB (predominantly) and Mathematica (for symbolic computations), enabling me to compute solutions for complicated systems within 30s.<br>
[<a href="/docs/PF_Cylinders_TejaswinP.pdf">pdf</a>]
</small></p>
<p></p>
<h3><u> Software for heat pipe design  </u></h3>
<h4> Instructor : Prof. Sarit K Das, ME6220, IITM </h4>
<p><small>	In a specialized course on Heat Exchangers and their design, I had to engineer a software that was capable of designing heat pipes, given a wide selection of input parameters. A heat pipe is a heat transfer device that combines the principles of both thermal conductivity and phase transition to efficiently manage the transfer of heat between two solid interfaces. The software was designed to select the fluid material, solid material, the dimensions of the pipe among other parameters, while solving a constrained optimization problem.<br>
[<a href="/docs/HeatPipe_TejaswinP.pdf">pdf</a>]
</small></p>
<p></p>
<h3><u> In house CPV system  </u></h3>
<h4> Instructor : Prof. Arvind Pattamatta, ME3260, IITM </h4>
<p><small>	In a course on Power Generation and Power Plant Engineering, I was posed a challenging problem of making recommendations to a chair panel on the feasibility of implementing a 10 kW Concentrated Photo Voltaic system for satisfying in house electricity requirements of residence halls within the institute. After thorough analysis on various modules - solar cells, concentrators, cooling systems, tracking systems, and obtaining on-field data, a report citing the recommendations was submitted to the aforesaid panel.<br>
[<a href="/docs/CPV_TejaswinP.pdf">pdf</a>]
</small></p>
<p></p>
<h3><u> Lid Driven Cavity Flow </u></h3>
<h4> Instructor : <a href="https://apm.iitm.ac.in/fmlab/arul/"> Prof. Arul K Prakash</a>, AM5630, IITM </h4>
<h1 class="title"><img id="centerimg" src="/images/am5630velocity.jpg"></h1><center><small>X velocity contours</small></center><p></p>
<p><small>	In my undergraduate course on CFD, I had to develop a custom code for the classic lid driven cavity problem, using different discretization schemes and solution algorithms - to test for convergence, complexity and time to solution. This included different temporal and spatial discretization schemes, and using FFT/GMRES for solving the Streamfunction-Vorticity poisson equation.<br>
[<a href="/docs/LDC_GMRES_TejaswinP.pdf">pdf</a>]
</small></p>
<p></p>
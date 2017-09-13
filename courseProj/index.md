---
layout: page 
title: Academic Projects 
date:   2017-09-10 12:00:00
order: 5
---

<h3><u> 3-D Navier-Stokes solver for simulation of atmospheric phenomena </u></h3>
<h4> Instructor : <a href="https://www.atmos.illinois.edu/~bjewett/">Prof. Brian Ford Jewett</a>, <a href="https://www.atmos.illinois.edu/~bjewett/atms502.html">ATMS502</a>, UIUC </h4>
<h1 class="title"><img id="centerimg" src="/images/cleft.png"></h1><center><small>A snapshot of a 3-D simulation of cold bubbles interacting with one another under the influence of gravity. You can see the cleft and lobe instability in the images</small></center><br>
####I developed a 3-D nonlinear quasi-compressible flow solver using a combination of higher order finite difference (FDM) and a piecewise linear finite volume method (FVM) for spatial discretization. Explicit and implicit temporal treatment for different terms was also implemented, using Strang splitting. For adherence to conservation laws and accuracy, grid staggering was employed. Shared memory parallelism was done through OpenMP. An equivalent version for 2-D with Adaptive Mesh Refinement (AMR) capabilities was also implemented. 
<br>
<h3><u> Quick solutions for inviscid flow past arbitrarily distributed circular cylinders </u></h3>
<h4> Instructor : <a href="https://apm.iitm.ac.in/fmlab/arul/"> Prof.Arul K Prakash</a>, AM5530, IITM </h4>
<h1 class="title"><img id="centerimg" src="/images/am5530Streamlines.jpg"></h1><center><small>Streamlines for uniform inviscid flow past a two cylinder system for 45° flow angle, with the ratio of radii being 2</small></center><br>
####Analysis of inviscid flows are tractable using complex number theory, with suitable domain transformations. Using Crowdy's <a href="http://wwwf.imperial.ac.uk/~dgcrowdy/_producer/PubFiles/Paper-15.pdf"> work</a>, I was able to recontruct solutions for uniform oriented flows past a set of cylinders. This called for implementing numerical algorithms efficiently in MATLAB (predominantly) and Mathematica (for symbolic computations), enabling me to compute solutions for complicated systems within 30s.    
<br>

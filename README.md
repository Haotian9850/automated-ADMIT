# automated-ADMIT
A python program to automate molecular line identification from raw ALMA data package (.fits) based on CASA with ADMIT 

# Start and deploy
This application requires installation of the CASA software (5.0.0+) and ADMIT package. To start admit in CASA, run
<code>import admit</code>

# Set expected molecular lines
The programs takes a <code>.txt</code> named <code>input.txt</code> as input. The first line of <code>input.txt</code> should be the <i>number of expected lines</i> and each following line the <i>frequency</i> range of every expected line. An example if <code>input.txt</code> is shown below:
<code>input.txt</code>
<br/>
<code>3</code> 
<br/>
<code>317.29 317.30</code>
<br/>
<code>318.77 318.89</code>
<br/>
<code>319.69 320.00</code>

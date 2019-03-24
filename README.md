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

# Set parameter range
Currently, the program supports user-defined range for <code>numsigma</code>, <code>minchan</code> and <code>maxchan</code>, presented as lists <code>numsigmaRange</code>, <code>minchanRange</code> and <code>maxchanRange</code> in <code>Main.py</code>. Changing the value of these lists will redefine parameter range. More parameters will be added in the future to allow for better customizability. 

# Automate parameter finding process
In CASA's iPython environment, run 
<br/>
<code>%run Main.py</code>
<br/>
The program will run all ADMIT tasks based on parameter range and then print out the best-fit parameter set in the console. 

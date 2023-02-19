
~ 396 Artificial Life ~ 
=======================


Creature Possibilities
======================
These creatures are randomly generated with the following parameters: 
  - Number of Boxes: 2 - 11 
  - Probability of floating joint: 10% 
  - Probability of Sensor: 50% 
  - Probability of Motor: 100% 
  - Height: 0.01 - 1.01 
  - Depth: 0.01 - 1.01 
  - Width: 0.01 - 2.01 
  
  They can branch to the left, towards the viewer, or upwards. The program does not currently keep track of all possible branching points, so the creature only branches off the most recent branch. 

  The bodies are generated with a large looping process that, after determining the number of boxes total, loops through creating specifics for each bpx. The choice of which direction to branch is determined by a random number generator (1 means to left, 2 towards viewer, 3 upwards). The height, depth, width, whether there is a sensor, and the type of joint are also all generated with random number generators given the parameters above. 

  As noted above, all joints have motors. All sensors are also connected to all motors right now, with the brain being created after the physical body is created. I did mess around with random motor assignment, and a small amount with mapping the body so that motors would only be connected to sensors near them, but I found that it increased the complexity and often created worse results instead of better. 


TO RUN: 
===================
Simply run "python3 main.py" and it will simulate 10 creatures for 100 frames each. For some reason it changes the view on creatures 2-10, but these can be slowed down and played with using the constants.py  


Documentation:
==============
To view a 10 second snipit of the work: 
To view a longer version of rhe same video: 



Citations:
===========
Note: This work builds extensively off of the work of Karl Sims, r/ludobots, and the pyrosim library. Without this prior work none of this would have been possible, esspecially without the guidance of the pyrosim documentation and the helpful people over at r/ludobots who teach a great lesson on the basics. 


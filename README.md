
~ 396 Artificial Life ~ 
=======================


Creature Generation
======================
These creatures are randomly generated with the following parameters: 
  - Number of Boxes: 2 - 11 
  - Probability of floating joint: 10% 
  - Probability of Sensor: 50% 
  - Probability of Motor: 100% 
  - Height: 0.01 - 1.01 
  - Depth: 0.01 - 1.01 
  - Width: 0.01 - 2.01 

They can branch to the left, towards the viewer, or upwards. The program does not currently keep track of all possible
branching points, so the creature only branches off the most recent branch. 

The bodies are generated with a large looping process that, after determining the number of boxes total, loops through
creating specifics for each bpx. The choice of which direction to branch is determined by a random number generator (1
means to left, 2 towards viewer, 3 upwards). The height, depth, width, whether there is a sensor, and the type of 
joint are also all generated with random number generators given the parameters above. 

As noted above, all joints have motors to begin with. All sensors are also connected to all motors right now, with the 
brain being created after the physical body is created. I did mess around with random motor assignment, and a small 
amount with mapping the body so that motors would only be connected to sensors near them, but I found that it increased 
the complexity and often created worse results instead of better. 


Creature Generation Diagram
==========================
![Example Creature Generation](https://github.com/austin-py/ArtificialLife/blob/0de940c026fa403e7679c0dfe1757fd9218d8eff/
creature_gen_diagram.jpg)


Creature Mutation
======================
  The creatures are randomly mutated every generation with the following probabilities:
  - Change Motor Weight (70%)
  - Add Motor Neuron (5%)
  - Remove Motor Neuron (5%)
  - Add Link (2%)
  - Remove Link (3%)
  - Mutate Body (15%)
      Subdivides into the following mutations:
        -Add Sensor Neuron 
        -Remove Sensor Neuron
        -Change Joint Axis
      These are chosen based on what piece of the body is randomly selected, and as such cannot be assigned probabilities. 
  
   

TO RUN: 
===================
Simply run "python3 main.py" and it will simulate 10 hill climbers which each have 10 members of population for 100 generations. Only the best from each hill climber run is shown visually, and only when show=True in main.py.  Viewing can be slowed down by adjusting the sleep time in constants. 


Documentation:
==============
To view a 10 second snipit of the work: 
To view a longer version of the same video:  
To view an evolutionary run of one creature: 



Citations:
===========
Note: This work builds extensively off of the work of Karl Sims, r/ludobots, and the pyrosim library. Without this prior work none of this would have been possible, esspecially without the guidance of the pyrosim documentation and the helpful people over at r/ludobots who teach a great lesson on the basics.

Additionally, some ideas were crowdsourced from the class campuswire page. Specifically I got ideas from the class page about how to re-generate bodies. 

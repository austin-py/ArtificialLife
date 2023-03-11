
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
![Creature Generation](https://github.com/austin-py/ArtificialLife/blob/1287086658b21dccd191fafcf91148e8217c4194/creature_gen_diagram.jpg)


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
  
   
Creature Mutation Diagram
=========================
![Creature Mutation](https://github.com/austin-py/ArtificialLife/blob/1287086658b21dccd191fafcf91148e8217c4194/creature_mutation.jpg)


Selection:
==========
Selection algorithm was varried, as detailed in the experimental results below. However the fitness measure remained the same. Namely how far the creature could travel from the origin in any direction. 

Experimentation:
=======================
For the purpose of experimentation, 420,000 simulations were run. The full writeup of the results and more details can be found [Here](https://github.com/austin-py/ArtificialLife/blob/final-project/Final_Writeup.md)


TO RUN: 
===================
Simply run "python3 main.py" and it will simulate 5 hill climbers which each have 10 members of population for 10 generations. Only the best from each hill climber run is shown visually, and only when show=True in main.py. The fitness values of the creatures will be saved in the whatever file the variable "FILE NAME" points to within the Data folder.

You are also able to comment out lines 9-14, and uncomment lines 16-18 to simulate one robot that was the result of evolution.

Viewing can be slowed down by adjusting the sleep time in constants. 


Documentation:
==============
To view a 10 teaser gif: https://youtu.be/STcML44qikA  <br>
To view a summary video of the work:  https://youtu.be/rgEhXUmA4ew <br>
Bloopers: https://youtu.be/1omTaGXlKPc <br>
To view one creature in both an evolved and random state: https://youtu.be/_wVzwvb8V4w <br>
To view an evolutionary run of one creature (every 50 generations is shown): https://youtu.be/Oq9HjgO-8LM <br>



Citations:
===========
Note: This work builds extensively off of the work of Karl Sims, r/ludobots, and the pyrosim library. Without this prior work none of this would have been possible, esspecially without the guidance of the pyrosim documentation and the helpful people over at r/ludobots who teach a great lesson on the basics.

Additionally, some ideas were crowdsourced from the class campuswire page. Specifically I got ideas from the class page about how to re-generate bodies. 

Ideas and inspiration from Comp-Sci 396 Artificial Life at Northwestern University with Sam Kriegman teaching. 



Older Graphs of some fitness plots:
==================================
![Five Fitness Plots](https://github.com/austin-py/ArtificialLife/blob/39d9d5bc3599a9c651ec6e205fc7436c8247c498/Fitness_Graph1.png)
![Many Fitness Plots](https://github.com/austin-py/ArtificialLife/blob/39d9d5bc3599a9c651ec6e205fc7436c8247c498/Fitness_Graph2.png)


=======================
~ 396 Artificial Life ~ 
=======================
My creature is a torso with two legs that I have evolved to walk as close to a little pyramid of blocks as possible. It uses a 3D distance formula (pythagorian theorem more or less) to calculate how far the creature is from the top of the center block.  The select functions chooses the robot with the minimal distance to the center of the pyramid. 

For the video I used 100 generations of 10 creatures. Running the main.py file will re-create this first by simulating a random creature, and then by evolving (while printing the fitness of children and parents) and then simulate the final product. This may take some time given the number of generations. Feel free to reduce the number of generations within constants.py to reduce the running time. 

I also messed around with potentially using two joints for the legs, one that rotates outwards while the other rotates forward and backward (similar to a human body where our hips rotate out, and knees hinge). The robot struggled however with this configuration and was less succesfull than when it had less motors. 

Additionally, I increased the maximum joint rotation to .7 which I found helped it move further without being too floppy. In the future directly evolvign the maximum rotation angle will likely help further refine the robot. 
____________________________________________________________________________________________________________________________________________

Kalpish Singhal
LMS-perceptron
____________________________________________________________________________________________________________________________________________
===============================================================
##Preamble
===============================================================
The idea of this assignment is to explore the material presented as part of Chapter 5 on constructing Linear Discriminant Functions based on various approaches such as Perceptron criterion function and Mean Squared Error.


===============================================================
##Implementation
===============================================================
Given there are two class w1 and w2. 
There are n samples (y1, y2.............yn).
We need to determine the weight vector a such that it properly classified the n samples in the two classes w1 and w2.

The algorithm that can be used to classify the n samples in two classes are :
	#Single-sample perceptron
	#Single-sample perceptron with margin
	#Relaxation algorithm with margin
	#Widrow-Hoff or Least Mean Squared (LMS) Rule

===============================================================
##Code (Algo)
===============================================================
-> Form the training set (w1 + w2).
-> g(x) = w1x1 + w2x2 + w0 
-> Classification Rule:
	if g(x) > 0 -> It belongs to w1
	if g(x) < 0 -> It belongs to w2
	if g(x) =0 -> It lies on the hyperplane separating the two classes.
-> The given samples are augmented by adding 1 at the end.	
-> Negate one of the class say class w2.
-> Now, if ay>0 then the sample is considered to be classified, otherwise missclassified.
-> Starting with any arbitary weight vector, the given algos updates the weight vector which classifies the two classes properly.
-> The weight vector is plotted using the corresponding straight line equatio w1x1 + w2x2 + w0.

===============================================================
                      INPUT FORMAT
===============================================================
## How to run code:-
-> Language used :-Python
-> $ python 201505513_assignment1.py
-> give the desired input
->The value of margin, learning rate and weight vector can be modified at run time so to make analysis as a part of different questions.
===============================================================
                      INPUT FORMAT
===============================================================
Enter your choice: 
i) 1 for Single-sample perceptron 
ii)2 for Single-sample perceptron with margin 
iii)3 for Relaxation algorithm with margin 
iv)4 for Widrow-Hoff or Least Mean Squared (LMS) Rule
v)5 LMS and perceptron solution align 
Enter Choice
1

===============================================================
                      OUTPUT FORMAT
===============================================================
weight is:
Number of iterations for conversion are :
Accuracy for the test set:


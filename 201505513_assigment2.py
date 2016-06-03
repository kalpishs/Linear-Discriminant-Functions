from numpy import *
from pylab import *
from math import *
import matplotlib.pyplot as plt
w12_y=[1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
X_NON_seprable=[(1, 6),(3, 3),(5, 2), (9, 9), (4, 8), (8, 5), (2, 7),  (7, 2), (2, 4), (7, 1), (1, 3), (8, 9) ]
Xnew= [(1, 5.6), (7, 4.3), (8, 9), (9, 9), (4, 8), (8, 4.4), (2, 1), (3, 3), (2, 4), (7, 0.5), (1, 3), (5, 2)]
def plot_bndry_double(weight_ss,weight,passing):
	X,Y,training_set=normal_train_set(passing)
	x_points=X[:,0]
	length=len(x_points)
	y_points =X[:,1]
	plt.axis([0,10,0,10])
	plt.plot(x_points[:length/2],y_points[:length/2],'gs');
	plt.plot(x_points[length/2:],y_points[length/2:],'rs');
	x_cordinate=-(float(weight[2]))/(float(weight[0]))
	y_cordinate=-(float(weight[2]))/(float(weight[1]))
	Lms,=plt.plot([0, x_cordinate],[y_cordinate, 0],'red',label='Lms')
	x_cordinate=-(float(weight_ss[2]))/(float(weight_ss[0]))
	y_cordinate=-(float(weight_ss[2]))/(float(weight_ss[1]))
	Perceptron_Line,=plt.plot([0, x_cordinate],[y_cordinate, 0],'y--',label='Perceptron')
	plt.legend([Lms, Perceptron_Line],['Lms', 'Perceptron'],loc=2)
	plt.show()
	pass
w12_x=[(1, 6), (7, 2), (8, 9), (9, 9), (4, 8), (8, 5), (2, 1), (3, 3), (2, 4), (7, 1), (1, 3), (5, 2)]

def plot_bndry(weight,passing):
	X,Y,training_set=normal_train_set(passing)
	x_points=X[:,0]
	length=len(x_points)
	y_points =X[:,1]
	plt.axis([0,10,0,10])
	plt.plot(x_points[:length/2],y_points[:length/2],'gs');
	plt.plot(x_points[length/2:],y_points[length/2:],'rs');
	x_cordinate=-(float(weight[2]))/(float(weight[0]))
	y_cordinate=-(float(weight[2]))/(float(weight[1]))
	plt.plot([0, x_cordinate],[y_cordinate, 0],'b--')
	plt.show()
	pass
def compute_accuracy(weight):
	pred_list = []
	X_test = [(7 , 5) ,(6, 7), (8 , 3), (1, 0), (0 ,1) ,(1, 1) ]
	Y_test = [ 1, 1, 1, 2, 2, 2]
	X_test_len=len(X_test)
	X_test=hstack((X_test, ones((X_test_len, 1))))
	
	for i in range(0,len(X_test)):
		dot_value = dot(X_test[i], weight)
		if dot_value>0:
			pred_list.append(1)
		elif dot_value<0:
			pred_list.append(2)
		elif dot_value == 0:
			pass
	print pred_list
	count=0
	for i in range(len(pred_list)):
		if pred_list[i] == Y_test[i]:
			count+=1

	length = len(pred_list)
	accuracy = (count/length)*100
	return accuracy
	pass

def relaxation_algo_with_margin(margin,learning_rate,passing):
	X,Y,training_set=normal_train_set(passing)
	n=len(training_set)
	i=count=0
	k=-1
	weight=[1,1,1]
	while i!=n:
		k=(k+1)%n
		dot_p=dot(training_set[k],weight)
		if margin>=dot_p:
			temp=float((float(margin-dot_p)/float(dot(training_set[k],training_set[k])))*2)
			weight=weight + (learning_rate * dot(temp,training_set[k]))
			i=0
		else:
			i=i+1
			count=count+1
	plot_bndry(weight,passing)		
	print "Number of iterations for conversion are %d." % count	 
	print "weight is: %s" % weight	
	return weight	
	pass	
def normal_train_set(passing):
	if passing==1:
		X=asarray(w12_x)
		Y=asarray(w12_y)
	elif passing==2:
		X=asarray(Xnew)
		Y=asarray(w12_y)
		pass
	elif passing==3:
		X=asarray(X_NON_seprable)
		Y=asarray(w12_y)
	LEN_X=len(X)
	train_set=hstack((X, ones((LEN_X, 1))))
	convert_truth= Y==unique(Y)[1]
	train_set[convert_truth]=-train_set[convert_truth]
	return X,Y,train_set
	pass
def perceptron_single_sample(margin,learning_rate,passing):
	X,Y,training_set=normal_train_set(passing)
	n=len(training_set)
	weight=[1,1,1]
	i=count=0
	k=-1
	while i!=n:
		count=count+1
		k = (k+1)%n
		if margin>=dot(training_set[k],weight):
			weight=training_set[k]* learning_rate + weight
			i=0
		else:
			i=i+1
	if passing==1:
		plot_bndry(weight,passing)		
	print "Number of iterations for conversion are %d." % count	 
	print "weight is: %s" % weight
	return weight
	pass


def least_mean_square(margin,learning_rate,passing):
	X,Y,training_set=normal_train_set(passing)
	
	count=0
	k=-1
	weight=[0.5,0.5,-1]
	var=1
	while var == 1:
		count=count+1
		flag=1
		k=(k+1)%len(training_set)
		nk=1.0/2000.0
		temp=dot((nk* (margin - dot(training_set[k],weight))),training_set[k])
		if sqrt(dot(temp,temp))<margin:
			flag=0
		weight=sum([weight,temp],axis=0)
		if(flag==1 or count==2000):
			break;
	print "weight is: %s" % weight		
	if passing==1 or passing ==3 :
		plot_bndry(weight,passing)		
	elif passing==2:
		weight_ss=perceptron_single_sample(margin,learning_rate,passing)
		plot_bndry_double(weight_ss,weight,passing)
	
	print "Number of iterations for conversion are %d." % count
	return weight	
	#Obtained the values as required (Augmented and negated)
	pass

def main():
	print 'Enter your choice: \ni) 1 for Single-sample perceptron \nii)2 for Single-sample perceptron with margin \niii)3 for Relaxation algorithm with margin  \niv)4 for Widrow-Hoff or Least Mean Squared (LMS) Rule.\nv)5 LMS and perceptron solution align'
	input_case=input("Enter Choice\n")
	if input_case == 1:
		m=0.0
		lern_rate = 1.0
		weight=perceptron_single_sample(m,lern_rate,1)
		accuracy = compute_accuracy(weight)
		print "Accuracy is: %d" % accuracy + "%"
		pass
		
	if input_case == 2:
		m=2
		lern_rate = 1.0
		weight=perceptron_single_sample(m,lern_rate,1)
		accuracy = compute_accuracy(weight)
		print "Accuracy is: %d" % accuracy + "%"
		pass

	if input_case == 3:
		m=15
		lern_rate=1.0
		weight=relaxation_algo_with_margin(m,lern_rate,1)
		accuracy = compute_accuracy(weight)
		print "Accuracy is: %d" % accuracy + "%"
		pass

	if input_case == 4:
		m=1
		lern_rate=0.01
		weight=least_mean_square(m,lern_rate,1)
		accuracy = compute_accuracy(weight)
		print "Accuracy is: %d" % accuracy + "%"
		print 'Non Separable Data Plotting'
		weights = least_mean_square(m,lern_rate,3)
		pass
	if input_case == 5:
		lern_rate =0.01
		m = 1.0
		weight=least_mean_square(m,lern_rate,2)
	if input_case>5 or input_case<1:
		print "wrong input"	


main()
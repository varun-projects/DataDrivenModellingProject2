
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 17:09:11 2018

@author: Varun Garg
"""
import numpy as np


n_experiments=100
x1=np.array(np.random.uniform(-1,1,n_experiments))
ones=np.ones(n_experiments)
x=np.column_stack((ones,x1))
print "shape of x"

print np.shape(x)

#######################forming the t equation properly########
w0 =-0.3
w1 = 0.5
w_matrix= np.column_stack((w0,w1))
e=np.random.normal(0,0.2,(n_experiments,1))

first_t_term = np.matmul(w_matrix,np.transpose(x) )
print "shape of w x"
print np.shape(first_t_term)
print "shape of e"
print np.shape(e)
t= np.add(np.transpose(first_t_term),e)
print "shape of t"
print np.shape(t)
#######################generalization as a 2d array 


term_a= np.matmul(x.T,x)
print "shape of term a"
print np.shape(term_a)
term_b= np.matmul(x.T,t)
print "shape of term b"
print np.shape(term_b)
##########################solve for w #############

w_result = np.linalg.solve(term_a,term_b)
print w_result
print np.shape(w_result)
print np.linalg.cond(w_result)

####################################################

print np.linalg.cond(first_t_term)


######################################################
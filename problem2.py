
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 21:06:49 2018

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



####################### likelyhood calculation
loglikelyhood = np.square(t - first_t_term) 


sum_loglikelyhood = np.sum(loglikelyhood)

mle_noise_variance = n_experiments*(1/sum_loglikelyhood)
print "mle_noise_variance"
print mle_noise_variance
print "variance of error t -wx  numpy function"

print np.var(t - first_t_term)  #use the variance fomula 


print "shape of t"
print np.shape(t)
tset=t
expected_t_2nd =np.sum(np.square(tset))/n_experiments
expected_t_square =np.square(np.mean(tset))
print "variance of error t numpy raw"
var_raw_t =expected_t_2nd -expected_t_square
print var_raw_t




identity=np.identity(2)

# wmap for q=1 
xTxvprod = np.matmul(x.T,x)

print "shape of xTxvprod"
print  np.shape(xTxvprod)
wmap = xTxvprod + mle_noise_variance*(1/1)*identity
print wmap
#
#for line in data_array:
#    result = do_stuff(line)
#    result_array = np.append(result_array, result)
size = (2,1)
wmap_array_t=np.zeros(size)
print wmap_array_t

#for q in range(1,10):
#    wmap_array_t[q]=vprod(x) + mle_noise_variance*(1/q)*identity


wmap_1 = xTxvprod + mle_noise_variance*(1.0/1)*identity

wmap_2 = xTxvprod + mle_noise_variance*(1.0/2)*identity

wmap_3 = xTxvprod + mle_noise_variance*(1.0/3)*identity

wmap_4 = xTxvprod + mle_noise_variance*(1.0/4)*identity

wmap_5 = xTxvprod + mle_noise_variance*(1.0/5)*identity

wmap_6 = xTxvprod + mle_noise_variance*(1.0/6)*identity

wmap_7 = xTxvprod + mle_noise_variance*(1.0/7)*identity

wmap_8 = xTxvprod + mle_noise_variance*(1.0/8)*identity

wmap_9 = xTxvprod + mle_noise_variance*(1.0/9)*identity

wmap_10 = xTxvprod + mle_noise_variance*(1.0/10)*identity


print "condition number3"


term_a_q1= wmap_1

term_b= np.matmul(x.T,t)

##########################solve for w #############

print "solution of equation"
w_map_q1 = np.linalg.solve(wmap_1,term_b)
print w_map_q1

print "solution of equation "
w_map_q2 = np.linalg.solve(wmap_2,term_b)
print w_map_q2

print "solution of equation q=3 "
w_map_q3 = np.linalg.solve(wmap_3,term_b)
print w_map_q3

print "solution of equation q=4 "
w_map_q4 = np.linalg.solve(wmap_4,term_b)
print w_map_q4


print "solution of equation q=5 "
w_map_q5 = np.linalg.solve(wmap_5,term_b)
print w_map_q5


print "solution of equation q=6"
w_map_q6 = np.linalg.solve(wmap_6,term_b)
print w_map_q6


print "solution of equation q=7 "
w_map_q7 = np.linalg.solve(wmap_7,term_b)
print w_map_q7


print "solution of equation q=8 "
w_map_q8 = np.linalg.solve(wmap_8,term_b)
print w_map_q8


print "solution of equation q=9 "
w_map_q9 = np.linalg.solve(wmap_9,term_b)
print w_map_q9


print "solution of equation q=10 "
w_map_q10 = np.linalg.solve(wmap_10,term_b)
print w_map_q10




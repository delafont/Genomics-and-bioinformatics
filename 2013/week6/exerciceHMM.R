install.packages("HMM")
library(HMM)
####Isochore of 10bp over 100bp#####
prob_of_I_knowing_I<-1-1/10
prob_of_N_knowing_I<-1/10
prob_of_I_knowing_N<-2/90
prob_of_N_knowing_N<-1-2/90

#initailization of the model#########
hmm_Isochore<-initHMM(c("I","N"), c("A","T","C","G"),c(0.5,0.5), transProbs=matrix(c(prob_of_I_knowing_I,prob_of_I_knowing_N,prob_of_N_knowing_I,prob_of_N_knowing_N),2), emissionProbs=matrix(c(0.25,0.45,0.25,0.45,0.25,0.05,0.25,0.05),2))

# Simulation using the model#
simulation<-simHMM(hmm_Isochore,100)

# plotting the model simulation
obsToVal<-function(obs){
    if(obs == "A"){return(2)}
    if(obs == "T"){return(2)}
    else {return(4)}
}

stateToVal<-function(st){
    if(st == "I"){return (1)}
    if(st == "N"){return (3)}
    else {return ("NA")}

}

par(mfrow=c(2,1))
plot( sapply(simulation$observation, obsToVal),pch=19,ylim=c(0,8),col=sapply(simulation$observation, obsToVal),cex=.5)
legend("topright",c("A/T","G/C"),pch=19,col=c("red","blue"))
plot( sapply(simulation$states, stateToVal),type="l",ylim=c(0,5))

# analysing a given sequence of observation
observations = c("A","T","T","A","A","G","T","A","C","T","T","A","A","G","T","G","A","C","T","A")
observations2 = c("A","C","C","G","A","G","T","C","T","G","T","A","A","G","T","G","A","T","T","A")
logForwardProbabilities = forward(hmm_Isochore,observations)  #forward probability
print(exp(logForwardProbabilities))
logBackwardProbabilities = backward(hmm_Isochore,observations) #bacward probability
print(exp(logBackwardProbabilities))
viterbi = viterbi(hmm_Isochore,observations) # viterbi algorithm
print(viterbi)
posterior = posterior(hmm_Isochore,observations) # posterior probability
print(posterior)

logForwardProbabilities = forward(hmm_Isochore,observations2)  #forward probability
print(exp(logForwardProbabilities))
logBackwardProbabilities = backward(hmm_Isochore,observations2) #bacward probability
print(exp(logBackwardProbabilities))
viterbi = viterbi(hmm_Isochore,observations2) # viterbi algorithm
print(viterbi)
posterior = posterior(hmm_Isochore,observations2) # posterior probability
print(posterior)

bw = baumWelch(hmm_Isochore,observations,10) # Baum Welch optimization of the HMM
print(bw$hmm)







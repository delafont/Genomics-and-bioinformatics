
f <- function(n){factorial(n)}

L0 <- function(c1,c2) {
    C = f(sum(c1))*f(sum(c2)) / prod(f(c1))*prod(f(c2))
    C * prod( ((c1+c2)/sum(c1+c2))^(c1+c2))
}
L1 <- function(c1,c2) {
    C = f(sum(c1))*f(sum(c2)) / prod(f(c1))*prod(f(c2))
    C * prod((c1/sum(c1))^c1) * prod((c2/sum(c2))^c2)
}

multest <- function(c1,c2){
    A = L0(c1,c2)
    B = L1(c1,c2)
    LR = A/B
    lr = -2*log(LR)
    pvalue = 1-pchisq(lr,length(c1))
    LR
}

multest(c(17,4,1,0),c(6,7,4,1)) # P7-P10
multest(c(6,1,0,0),c(2,2,2,0))  # P3-P4
multest(c(0,5,2,1),c(0,5,2,2))  # P1-P2 control
